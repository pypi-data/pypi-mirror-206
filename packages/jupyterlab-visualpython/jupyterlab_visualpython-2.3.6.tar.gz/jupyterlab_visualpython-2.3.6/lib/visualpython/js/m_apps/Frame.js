/*
 *    Project Name    : Visual Python
 *    Description     : GUI-based Python code generator
 *    File Name       : Frame.js
 *    Author          : Black Logic
 *    Note            : Apps > Frame
 *    License         : GNU GPLv3 with Visual Python special exception
 *    Date            : 2021. 11. 18
 *    Change Date     :
 */

//============================================================================
// [CLASS] Frame
//============================================================================
define([
    '!!text-loader!vp_base/html/m_apps/frame.html',   // INTEGRATION: unified version of text loader
    'vp_base/css/m_apps/frame.css',          // INTEGRATION: unified version of css loader
    'vp_base/js/com/com_Const',
    'vp_base/js/com/com_String',
    'vp_base/js/com/com_util',
    'vp_base/js/com/component/PopupComponent',
    'vp_base/js/com/component/SuggestInput',
    'vp_base/js/com/component/DataSelector',
    'vp_base/js/m_apps/Subset'
], function(frameHtml, frameCss, com_Const, com_String, com_util, PopupComponent, SuggestInput, DataSelector, Subset) {

    /**
     * Frame
     */
    class Frame extends PopupComponent {
        _init() {
            super._init();
            this.config.sizeLevel = 3;
            this.config.checkModules = ['pd'];

            // state
            this.state = {
                originObj: '',
                tempObj: '_vp',
                returnObj: '_vp',
                inplace: false,
                menu: '',
                menuItem: '',
                columnLevel: 1,
                columnList: [],
                indexLevel: 1,
                indexList: [],
                selected: [],
                axis: FRAME_AXIS.NONE,
                lines: TABLE_LINES,
                steps: [],
                popup: {
                    type: FRAME_EDIT_TYPE.NONE,
                    replace: { index: 0 }
                },
                selection: {
                    start: -1,
                    end: -1
                },
                ...this.state
            }

            // numpy.dtype or python type
            this.astypeList = [ 
                'datetime64', 
                'int', 'int32', 'int64', 
                'float', 'float64', 
                'object', 'category', 
                'bool', 'str'
            ];

            // {
            //     id: 'id',
            //     label: 'menu label',
            //     child: [
            //         { 
            //             id: 'id', label: 'label', code: 'code', 
            //             axis: 'col/row', single_select: true/false,
            //             numeric_only: true/false 
            //         }
            //     ]
            // }
            this.menuList = [
                {
                    id: 'edit',
                    label: 'Edit',
                    child: [
                        { id: 'add_col', label: 'Add column', selection: FRAME_SELECT_TYPE.NONE, menuType: FRAME_EDIT_TYPE.ADD_COL },
                        { id: 'add_row', label: 'Add row', selection: FRAME_SELECT_TYPE.NONE, menuType: FRAME_EDIT_TYPE.ADD_ROW },
                        { id: 'delete', label: 'Delete', selection: FRAME_SELECT_TYPE.MULTI, menuType: FRAME_EDIT_TYPE.DROP },
                        { id: 'rename', label: 'Rename', selection: FRAME_SELECT_TYPE.NONE, menuType: FRAME_EDIT_TYPE.RENAME },
                        { id: 'asType', label: 'As type', selection: FRAME_SELECT_TYPE.NONE, axis: FRAME_AXIS.COLUMN, menuType: FRAME_EDIT_TYPE.AS_TYPE },
                        { id: 'replace', label: 'Replace', selection: FRAME_SELECT_TYPE.SINGLE, axis: FRAME_AXIS.COLUMN, menuType: FRAME_EDIT_TYPE.REPLACE },
                        { id: 'discretize', label: 'Discretize', selection: FRAME_SELECT_TYPE.SINGLE, axis: FRAME_AXIS.COLUMN, numeric_only: true, menuType: FRAME_EDIT_TYPE.DISCRETIZE }
                    ]
                },
                {
                    id: 'transform',
                    label: 'Transform',
                    child: [
                        { id: 'set_index', label: 'Set index', axis: FRAME_AXIS.COLUMN, selection: FRAME_SELECT_TYPE.MULTI, menuType: FRAME_EDIT_TYPE.SET_IDX },
                        { id: 'reset_index', label: 'Reset index', selection: FRAME_SELECT_TYPE.NONE, menuType: FRAME_EDIT_TYPE.RESET_IDX },
                        { id: 'data_shift', label: 'Data shift', axis: FRAME_AXIS.COLUMN, selection: FRAME_SELECT_TYPE.NONE, menuType: FRAME_EDIT_TYPE.DATA_SHIFT }
                    ]
                },
                {
                    id: 'sort',
                    label: 'Sort',
                    axis: FRAME_AXIS.COLUMN,
                    child: [
                        { id: 'sort_index', label: 'Sort index', selection: FRAME_SELECT_TYPE.NONE, menuType: FRAME_EDIT_TYPE.SORT_INDEX },
                        { id: 'sort_values', label: 'Sort values', axis: FRAME_AXIS.COLUMN, selection: FRAME_SELECT_TYPE.MULTI, menuType: FRAME_EDIT_TYPE.SORT_VALUES },
                    ]
                },
                {
                    id: 'encoding',
                    label: 'Encoding',
                    axis: FRAME_AXIS.COLUMN,
                    selection: FRAME_SELECT_TYPE.SINGLE, 
                    child: [
                        { id: 'label_encoding', label: 'Label encoding', axis: FRAME_AXIS.COLUMN, selection: FRAME_SELECT_TYPE.SINGLE, menuType: FRAME_EDIT_TYPE.LABEL_ENCODING },
                        { id: 'one_hot_encoding', label: 'Onehot encoding', axis: FRAME_AXIS.COLUMN, selection: FRAME_SELECT_TYPE.SINGLE, menuType: FRAME_EDIT_TYPE.ONE_HOT_ENCODING },
                    ]
                },
                {
                    id: 'data_cleaning',
                    label: 'Data cleaning',
                    axis: FRAME_AXIS.COLUMN,
                    child: [
                        { id: 'fillna', label: 'Fill NA', axis: FRAME_AXIS.COLUMN, selection: FRAME_SELECT_TYPE.NONE, menuType: FRAME_EDIT_TYPE.FILL_NA },
                        { id: 'dropna', label: 'Drop NA', axis: FRAME_AXIS.COLUMN, selection: FRAME_SELECT_TYPE.NONE, menuType: FRAME_EDIT_TYPE.DROP_NA },
                        { id: 'drop_outlier', label: 'Drop outlier', axis: FRAME_AXIS.COLUMN, selection: FRAME_SELECT_TYPE.SINGLE, menuType: FRAME_EDIT_TYPE.DROP_OUT },
                        { id: 'drop_duplicates', label: 'Drop duplicates', axis: FRAME_AXIS.COLUMN, selection: FRAME_SELECT_TYPE.NONE, menuType: FRAME_EDIT_TYPE.DROP_DUP },
                    ]
                },
            ];

            // Add/Replace - subset
            this.subsetCm = null;
            this.subsetEditor = null;

            this.loading = false;

            // this._addCodemirror('previewCode', this.wrapSelector('#vp_fePreviewCode'), 'readonly');
        }

        loadState() {
            super.loadState();
            var {
                originObj,
                returnObj,
                steps
            } = this.state;
    
            // $(this.wrapSelector('#vp_feVariable')).val(originObj);
    
            // $(this.wrapSelector('#vp_feReturn')).val(returnObj);
    
            // // execute all steps
            if (steps && steps.length > 0) {
                var code = steps.join('\n');
                this.state.steps = [];
                this.loadCode(code);
            }
        }

        _bindEvent() {
            super._bindEvent();
            /** Implement binding events */
            let that = this;

            // select df
            $(document).on('change', this.wrapSelector('#vp_feVariable'), function() {
                // set temporary df
                var origin = $(this).val();

                if (origin) {
                    // initialize state values
                    that.state.originObj = origin;
                    that.state.tempObj = '_vp';
                    that.state.returnObj = that.state.tempObj;
                    if (that.state.inplace === true) {
                        that.state.returnObj = origin;
                    }
                    that.initState();

                    // reset return obj
                    $(that.wrapSelector('#vp_feReturn')).val(that.state.returnObj);
    
                    // reset table
                    $(that.wrapSelector('.' + VP_FE_TABLE)).replaceWith(function() {
                        return that.renderTable('');
                    });
    
                    // load code with temporary df
                    that.loadCode(that.getTypeCode(FRAME_EDIT_TYPE.INIT));
                    that.loadInfo();
                }
            });

            // refresh df
            $(document).on('click', this.wrapSelector('.vp-fe-df-refresh'), function() {
                that.loadVariableList();
            });

            $(document).on('click', this.wrapSelector('.' + VP_FE_INFO), function(evt) {
                evt.stopPropagation();
            });

            // input return variable
            $(document).on('change', this.wrapSelector('#vp_feReturn'), function() {
                var returnVariable = $(this).val();
                if (returnVariable == '') {
                    returnVariable = that.state.tempObj;
                }
                // check if it's same with origin obj
                if (returnVariable === that.state.originObj) {
                    $(that.wrapSelector('#inplace')).prop('checked', true);
                    that.state.inplace = true;
                } else {
                    $(that.wrapSelector('#inplace')).prop('checked', false);
                    that.state.inplace = false;
                }

                // show preview with new return variable
                that.state.returnObj = returnVariable;
                that.setPreview(that.getCurrentCode());
            });

            // check/uncheck inplace
            $(this.wrapSelector('#inplace')).on('change', function() {
                let checked = $(this).prop('checked');
                let returnVariable = '_vp';
                if (checked === true) {
                    returnVariable = that.state.originObj;
                }
                $(that.wrapSelector('#vp_feReturn')).val(returnVariable);

                // show preview with new return variable
                that.state.inplace = checked;
                that.state.returnObj = returnVariable;
                that.setPreview(that.getCurrentCode());
            });

            // menu on column (Deprecated on v2.3.6)
            // $(document).on('contextmenu', this.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN), function(event) {
            //     event.preventDefault();
            //     var hasSelected = $(this).hasClass('selected');
            //     $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_ROW)).removeClass('selected');
            //     // select col/idx
            //     if (!hasSelected) {
            //         $(this).addClass('selected');
            //         var newAxis = $(this).data('axis');
            //         that.state.axis = newAxis;
            //     }

            //     that.loadInfo();

            //     // show menu
            //     var thisPos = $(this).position();
            //     var thisRect = $(this)[0].getBoundingClientRect();
            //     that.showMenu(thisPos.left, thisPos.top + thisRect.height);
            // });

            // menu on row (Deprecated on v2.3.6)
            // $(document).on('contextmenu', this.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_ROW), function(event) {
            //     event.preventDefault();
            //     var hasSelected = $(this).hasClass('selected');
            //     $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN)).removeClass('selected');
            //     // select col/idx
            //     if (!hasSelected) {
            //         $(this).addClass('selected');
            //         var newAxis = $(this).data('axis');
            //         that.state.axis = newAxis;
            //     }

            //     that.loadInfo();

            //     // show menu
            //     var thisPos = $(this).position();
            //     var thisRect = $(this)[0].getBoundingClientRect();
            //     var tblPos = $(that.wrapSelector('.' + VP_FE_TABLE)).position();
            //     var scrollTop = $(that.wrapSelector('.' + VP_FE_TABLE)).scrollTop();
            //     that.showMenu(tblPos.left + thisRect.width, tblPos.top + thisPos.top - scrollTop);
            // });

            // un-select every selection
            $(document).on('click', this.wrapSelector('.vp-popup-body'), function() {
                $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_ROW)).removeClass('selected');
                $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN)).removeClass('selected');
                $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN_GROUP)).removeClass('selected');

                // reset selected columns/indexes
                that.state.axis = FRAME_AXIS.NONE;
                that.state.selected = [];
                // load toolbar
                that.renderToolbar();
            });

            // select column group
            $(document).on('click', this.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN_GROUP), function(evt) {
                evt.stopPropagation();

                let hasSelected = $(this).hasClass('selected');
                let colLabel = $(this).data('label');
                let firstIdx = $(that.wrapSelector(`.${VP_FE_TABLE} th[data-parent="${colLabel}"]:first`)).index();
                let lastIdx = $(that.wrapSelector(`.${VP_FE_TABLE} th[data-parent="${colLabel}"]:last`)).index();
                if (firstIdx === lastIdx) {
                    lastIdx = -1;
                }

                $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_ROW)).removeClass('selected');

                if (vpEvent.keyManager.keyCheck.ctrlKey) {
                    if (!hasSelected) {
                        that.state.selection = { start: firstIdx, end: -1 };
                        $(this).addClass('selected');
                        $(that.wrapSelector(`.${VP_FE_TABLE} th[data-parent="${colLabel}"]`)).addClass('selected');
                        var newAxis = $(this).data('axis');
                        that.state.axis = newAxis;
                    } else {
                        $(this).removeClass('selected');
                        $(that.wrapSelector(`.${VP_FE_TABLE} th[data-parent="${colLabel}"]`)).removeClass('selected');
                    }
                } else if (vpEvent.keyManager.keyCheck.shiftKey) {
                    var axis = that.state.axis;
                    var startIdx = that.state.selection.start;
                    if (axis != FRAME_AXIS.COLUMN) {
                        startIdx = -1;
                    }
                    
                    if (startIdx == -1) {
                        // no selection
                        that.state.selection = { start: firstIdx, end: -1 };
                    } else if (startIdx > firstIdx) {
                        // add selection from idx to startIdx
                        var tags = $(that.wrapSelector('.' + VP_FE_TABLE_COLUMN));
                        let parentSet = new Set();
                        for (var i = firstIdx - 1; i <= startIdx; i++) {
                            $(tags[i]).addClass('selected');
                            parentSet.add($(tags[i]).data('parent'));
                        }
                        parentSet.forEach(parentKey => {
                            let length = $(that.wrapSelector(`.${VP_FE_TABLE} th[data-parent="${parentKey}"]`)).length;
                            let selectedLength = $(that.wrapSelector(`.${VP_FE_TABLE} th.selected[data-parent="${parentKey}"]`)).length;
                            if (length === selectedLength) {
                                $(that.wrapSelector(`.${VP_FE_TABLE} th[data-label="${parentKey}"]`)).addClass('selected');
                            } else {
                                $(that.wrapSelector(`.${VP_FE_TABLE} th[data-label="${parentKey}"]`)).removeClass('selected');
                            }
                        });
                        that.state.selection = { start: startIdx, end: firstIdx };
                    } else if (startIdx <= firstIdx) {
                        // add selection from startIdx to idx
                        var tags = $(that.wrapSelector('.' + VP_FE_TABLE_COLUMN));
                        let parentSet = new Set();
                        for (var i = startIdx; i < lastIdx; i++) {
                            $(tags[i]).addClass('selected');
                            parentSet.add($(tags[i]).data('parent'));
                        }
                        parentSet.forEach(parentKey => {
                            let length = $(that.wrapSelector(`.${VP_FE_TABLE} th[data-parent="${parentKey}"]`)).length;
                            let selectedLength = $(that.wrapSelector(`.${VP_FE_TABLE} th.selected[data-parent="${parentKey}"]`)).length;
                            if (length === selectedLength) {
                                $(that.wrapSelector(`.${VP_FE_TABLE} th[data-label="${parentKey}"]`)).addClass('selected');
                            } else {
                                $(that.wrapSelector(`.${VP_FE_TABLE} th[data-label="${parentKey}"]`)).removeClass('selected');
                            }
                        });
                        that.state.selection = { start: startIdx, end: lastIdx };
                    }
                } else {
                    $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN)).removeClass('selected');
                    $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN_GROUP)).removeClass('selected');

                    $(this).addClass('selected');
                    $(that.wrapSelector(`.${VP_FE_TABLE} th[data-parent="${colLabel}"]`)).addClass('selected');
                    that.state.selection = { start: firstIdx, end: lastIdx };
                    var newAxis = $(this).data('axis');
                    that.state.axis = newAxis;
                }
                that.loadInfo();
                // load toolbar
                that.renderToolbar();
            });

            // select column
            $(document).on('click', this.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN), function(evt) {
                evt.stopPropagation();

                var idx = $(that.wrapSelector('.' + VP_FE_TABLE_COLUMN)).index(this); // 1 ~ n
                var hasSelected = $(this).hasClass('selected');

                $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_ROW)).removeClass('selected');

                if (vpEvent.keyManager.keyCheck.ctrlKey) {
                    if (!hasSelected) {
                        that.state.selection = { start: idx, end: -1 };
                        $(this).addClass('selected');
                        var newAxis = $(this).data('axis');
                        that.state.axis = newAxis;
                    } else {
                        $(this).removeClass('selected');
                    }
                    
                } else if (vpEvent.keyManager.keyCheck.shiftKey) {
                    var axis = that.state.axis;
                    var startIdx = that.state.selection.start;
                    if (axis != FRAME_AXIS.COLUMN) {
                        startIdx = -1;
                    }
                    
                    if (startIdx == -1) {
                        // no selection
                        that.state.selection = { start: idx, end: -1 };
                    } else if (startIdx > idx) {
                        // add selection from idx to startIdx
                        var tags = $(that.wrapSelector('.' + VP_FE_TABLE_COLUMN));
                        for (var i = idx; i <= startIdx; i++) {
                            $(tags[i]).addClass('selected');
                        }
                        that.state.selection = { start: startIdx, end: idx };
                    } else if (startIdx <= idx) {
                        // add selection from startIdx to idx
                        var tags = $(that.wrapSelector('.' + VP_FE_TABLE_COLUMN));
                        for (var i = startIdx; i <= idx; i++) {
                            $(tags[i]).addClass('selected');
                        }
                        that.state.selection = { start: startIdx, end: idx };
                    }
                } else {
                    $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN)).removeClass('selected');
                    $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN_GROUP)).removeClass('selected');

                    $(this).addClass('selected');
                    that.state.selection = { start: idx, end: -1 };
                    var newAxis = $(this).data('axis');
                    that.state.axis = newAxis;
                }
                // select its group
                $(that.wrapSelector(`.${VP_FE_TABLE} th[data-label="${$(this).data('parent')}"]`)).addClass('selected');

                that.loadInfo();
                // load toolbar
                that.renderToolbar();
            });

            // select row
            $(document).on('click', this.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_ROW), function(evt) {
                evt.stopPropagation();

                var idx = $(that.wrapSelector('.' + VP_FE_TABLE_ROW)).index(this); // 0 ~ n
                var hasSelected = $(this).hasClass('selected');

                $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN)).removeClass('selected');
                
                if (vpEvent.keyManager.keyCheck.ctrlKey) {
                    if (!hasSelected) {
                        that.state.selection = { start: idx, end: -1 };
                        $(this).addClass('selected');
                        var newAxis = $(this).data('axis');
                        that.state.axis = newAxis;
                    } else {
                        $(this).removeClass('selected');
                    }
                    
                } else if (vpEvent.keyManager.keyCheck.shiftKey) {
                    var axis = that.state.axis;
                    var startIdx = that.state.selection.start;
                    if (axis != FRAME_AXIS.ROW) {
                        startIdx = -1;
                    }
                    
                    if (startIdx == -1) {
                        // no selection
                        that.state.selection = { start: idx, end: -1 };
                    } else if (startIdx > idx) {
                        // add selection from idx to startIdx
                        var tags = $(that.wrapSelector('.' + VP_FE_TABLE_ROW));
                        for (var i = idx; i <= startIdx; i++) {
                            $(tags[i]).addClass('selected');
                        }
                        that.state.selection = { start: startIdx, end: idx };
                    } else if (startIdx <= idx) {
                        // add selection from startIdx to idx
                        var tags = $(that.wrapSelector('.' + VP_FE_TABLE_ROW));
                        for (var i = startIdx; i <= idx; i++) {
                            $(tags[i]).addClass('selected');
                        }
                        that.state.selection = { start: startIdx, end: idx };
                    }
                } else {
                    $(that.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_ROW)).removeClass('selected');
                    if (!hasSelected) {
                        $(this).addClass('selected');
                        that.state.selection = { start: idx, end: -1 };
                        var newAxis = $(this).data('axis');
                        that.state.axis = newAxis;
                    } else {
                        $(this).removeClass('selected');
                    }
                }
                that.loadInfo();
                // load toolbar
                that.renderToolbar();
            });

            // add column
            $(document).on('click', this.wrapSelector('.' + VP_FE_ADD_COLUMN), function() {
                // add column
                that.openInputPopup(FRAME_EDIT_TYPE.ADD_COL);
            });

            // add row
            $(document).on('click', this.wrapSelector('.' + VP_FE_ADD_ROW), function() {
                // add row
                that.openInputPopup(FRAME_EDIT_TYPE.ADD_ROW);
            });

            // more rows
            $(document).on('click', this.wrapSelector('.' + VP_FE_TABLE_MORE), function() {
                that.state.lines += TABLE_LINES;
                that.loadCode(that.getTypeCode(FRAME_EDIT_TYPE.SHOW), true);
            });

            // click toolbar item
            // $(document).on('click', this.wrapSelector('.vp-fe-toolbar-item'), function(evt) {
            //     evt.stopPropagation();
            //     var itemType = $(this).data('type');
            //     switch (parseInt(itemType)) {
            //         case FRAME_EDIT_TYPE.ADD_COL:
            //         case FRAME_EDIT_TYPE.ADD_ROW:
            //             that.openInputPopup(itemType);
            //             break;
            //     }
            // });

            // click menu item
            $(document).on('click', this.wrapSelector('.' + VP_FE_MENU_ITEM + ':not(.disabled)'), function(event) {
                event.stopPropagation();
                var editType = $(this).data('type');
                switch (parseInt(editType)) {
                    case FRAME_EDIT_TYPE.ADD_COL:
                    case FRAME_EDIT_TYPE.ADD_ROW:
                    case FRAME_EDIT_TYPE.RENAME:
                    case FRAME_EDIT_TYPE.REPLACE:
                    case FRAME_EDIT_TYPE.AS_TYPE:
                    case FRAME_EDIT_TYPE.DISCRETIZE:
                    case FRAME_EDIT_TYPE.DATA_SHIFT:
                    case FRAME_EDIT_TYPE.SORT_INDEX:
                    case FRAME_EDIT_TYPE.SORT_VALUES:
                    case FRAME_EDIT_TYPE.FILL_NA:
                    case FRAME_EDIT_TYPE.DROP_NA:
                    case FRAME_EDIT_TYPE.DROP: // check one more time
                        that.openInputPopup(editType);
                        break;
                    case FRAME_EDIT_TYPE.DROP_OUT:
                        that.config.checkModules = ['pd', 'np', 'vp_drop_outlier'];
                        that.checkAndRunModules(true).then(function() {
                            that.loadCode(that.getTypeCode(editType));
                        });
                        break;
                    default:
                        that.loadCode(that.getTypeCode(editType));
                        break;
                }
                that.hideMenu();
            });

            // popup : replace - add button
            $(document).on('click', this.wrapSelector('.vp-inner-popup-replace-add'), function() {
                var newInput = $(that.renderReplaceInput(++that.state.popup.replace.index));
                newInput.insertBefore(
                    $(that.wrapSelector('.vp-inner-popup-replace-table tr:last'))
                );
            });

            // popup : replace - delete row
            $(document).on('click', this.wrapSelector('.vp-inner-popup-delete'), function() {
                $(this).closest('tr').remove();
            });

            
            // popup : add column - dataframe selection 1
            $(document).on('var_changed change', this.wrapSelector('.vp-inner-popup-var1'), function() {
                var type = $(that.wrapSelector('.vp-inner-popup-var1box .vp-vs-data-type')).val();
                if (type == 'DataFrame') {
                    var df = $(this).val();
                    vpKernel.getColumnList(df).then(function(resultObj) {
                        let { result } = resultObj;
                        var { list } = JSON.parse(result);
                        var tag = new com_String();
                        tag.appendFormatLine('<select class="{0}">', 'vp-inner-popup-var1col');
                        list && list.forEach(col => {
                            tag.appendFormatLine('<option data-code="{0}" value="{1}">{2}</option>'
                                    , col.value, col.label, col.label);
                        });
                        tag.appendLine('</select>');
                        // replace column list
                        $(that.wrapSelector('.vp-inner-popup-var1col')).replaceWith(function() {
                            return tag.toString();
                        });
                    });
                }
            });

            // popup : add column - dataframe selection 2
            $(document).on('var_changed change', this.wrapSelector('.vp-inner-popup-var2'), function() {
                var type = $(that.wrapSelector('.vp-inner-popup-var2box .vp-vs-data-type')).val();
                if (type == 'DataFrame') {
                    var df = $(this).val();
                    vpKernel.getColumnList(df).then(function(resultObj) {
                        let { result } = resultObj;
                        var { list } = JSON.parse(result);
                        var tag = new com_String();
                        tag.appendFormatLine('<select class="{0}">', 'vp-inner-popup-var2col');
                        list && list.forEach(col => {
                            tag.appendFormatLine('<option data-code="{0}" value="{1}">{2}</option>'
                                    , col.value, col.label, col.label);
                        });
                        tag.appendLine('</select>');
                        // replace column list
                        $(that.wrapSelector('.vp-inner-popup-var2col')).replaceWith(function() {
                            return tag.toString();
                        });
                    });
                }
            });
        }

        handleInnerOk() {
            // ok input popup
            var type = parseInt(this.state.popup.type);
            var content = this.getPopupContent(type);
            // required data check
            if (type == FRAME_EDIT_TYPE.ADD_COL) {
                if (content.name === '') {
                    return;
                }
            }
            var code = this.loadCode(this.getTypeCode(this.state.popup.type, content));
            if (code == '') {
                return;
            }
            this.closeInnerPopup();
        }

        _unbindEvent() {
            super._unbindEvent();
            $(document).off(this.wrapSelector('*'));
    
            $(document).off('change', this.wrapSelector('#vp_feVariable'));
            $(document).off('click', this.wrapSelector('.vp-fe-df-refresh'));
            $(document).off('click', this.wrapSelector('.' + VP_FE_INFO));
            $(document).off('change', this.wrapSelector('#vp_feReturn'));
            $(document).off('click', this.wrapSelector('.vp-popup-body'));
            // $(document).off('contextmenu', this.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN));
            // $(document).off('contextmenu', this.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_ROW));
            $(document).off('click', this.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_COLUMN));
            $(document).off('click', this.wrapSelector('.' + VP_FE_TABLE + ' .' + VP_FE_TABLE_ROW));
            $(document).off('click', this.wrapSelector('.' + VP_FE_ADD_COLUMN));
            $(document).off('click', this.wrapSelector('.' + VP_FE_ADD_ROW));
            $(document).off('click', this.wrapSelector('.' + VP_FE_TABLE_MORE));
            $(document).off('click', this.wrapSelector('.vp-fe-toolbar-item'));
            $(document).off('click', this.wrapSelector('.' + VP_FE_MENU_ITEM));
            $(document).off('click', this.wrapSelector('.vp-inner-popup-replace-add'));
            $(document).off('click', this.wrapSelector('.vp-inner-popup-delete'));
            $(document).off('change', this.wrapSelector('.vp-inner-popup-var1'));
            $(document).off('change', this.wrapSelector('.vp-inner-popup-var2'));
        }

        bindEventForPopupPage(menuType) {
            var that = this;

            if (menuType === FRAME_EDIT_TYPE.ADD_COL
                || menuType === FRAME_EDIT_TYPE.ADD_ROW
                || menuType === FRAME_EDIT_TYPE.REPLACE) {
                ///// add page
                // 1. add type
                $(this.wrapSelector('.vp-inner-popup-addtype')).on('change', function() {
                    var tab = $(this).val();
                    $(that.wrapSelector('.vp-inner-popup-tab')).hide();
                    $(that.wrapSelector('.vp-inner-popup-tab.' + tab)).show();
                });
        
                // 2-1. hide column selection box
                $(this.wrapSelector('.vp-inner-popup-var1box .vp-vs-data-type')).on('change', function() {
                    var type = $(this).val();
                    if (type == 'DataFrame') {
                        $(that.wrapSelector('.vp-inner-popup-var1col')).show();
                    } else {
                        $(that.wrapSelector('.vp-inner-popup-var1col')).hide();
                    }
                });
        
                $(this.wrapSelector('.vp-inner-popup-var2box .vp-vs-data-type')).on('change', function() {
                    var type = $(this).val();
                    if (type == 'DataFrame') {
                        $(that.wrapSelector('.vp-inner-popup-var2col')).show();
                    } else {
                        $(that.wrapSelector('.vp-inner-popup-var2col')).hide();
                    }
                });
            } else if (menuType === FRAME_EDIT_TYPE.DISCRETIZE) {
                // change bins
                $(this.wrapSelector('.vp-inner-popup-bins')).on('change', function() {
                    let binsCount = $(this).val();
                    that.handleDiscretizeEdges(binsCount);
                });

                // change cut to qcut(quantile based discretization)
                $(this.wrapSelector('.vp-inner-popup-discretizetype')).on('change', function() {
                    let binsCount = $(that.wrapSelector('.vp-inner-popup-bins')).val();
                    let discretizeType = $(this).val();
                    // disable right and range table
                    if (discretizeType === 'qcut') {
                        $(that.wrapSelector('.vp-inner-popup-right')).prop('disabled', true);
                        $(that.wrapSelector('.vp-inner-popup-range-table input.vp-inner-popup-left-edge')).val('');
                        $(that.wrapSelector('.vp-inner-popup-range-table input.vp-inner-popup-right-edge')).val('');
                        $(that.wrapSelector('.vp-inner-popup-range-table input:not(.vp-inner-popup-label)')).prop('disabled', true);
                    } else {
                        $(that.wrapSelector('.vp-inner-popup-right')).prop('disabled', false);
                        $(that.wrapSelector('.vp-inner-popup-range-table input.vp-inner-popup-left-edge')).val('');
                        $(that.wrapSelector('.vp-inner-popup-range-table input.vp-inner-popup-right-edge')).val('');
                        $(that.wrapSelector('.vp-inner-popup-range-table input:not(.vp-inner-popup-label)')).prop('disabled', false);
                    }
                    that.handleDiscretizeEdges(binsCount);
                });

                // change right option
                $(this.wrapSelector('.vp-inner-popup-right')).on('change', function() {
                    let binsCount = $(that.wrapSelector('.vp-inner-popup-bins')).val();
                    let right = $(this).prop('checked');
                    that.handleDiscretizeEdges(binsCount, right);
                });
            } else if (menuType === FRAME_EDIT_TYPE.SORT_INDEX 
                    || menuType === FRAME_EDIT_TYPE.SORT_VALUES) {
                $(this.wrapSelector('.vp-inner-popup-sortby-up')).on('click', function() {
                    console.log('up', $(this));
                    let tag = $(this).closest('.vp-inner-popup-sortby-item');
                    tag.insertBefore(tag.prev());
                });
                $(this.wrapSelector('.vp-inner-popup-sortby-down')).on('click', function() {
                    console.log('down', $(this));
                    let tag = $(this).closest('.vp-inner-popup-sortby-item');
                    tag.insertAfter(tag.next());
                });
            }
            
        }

        handleDiscretizeEdges(binsCount=1, right=true) {
            let that = this;
            $(this.wrapSelector('.vp-inner-popup-range-table tbody')).html('');
            $(this.wrapSelector('.vp-inner-popup-islabelchanged')).val("false");
            $(that.wrapSelector('.vp-inner-popup-isedgechanged')).val("false");

            let code = new com_String();
            code.appendFormatLine("_out, _bins = pd.cut({0}[{1}], bins={2}, right={3}, labels=False, retbins=True)"
                , this.state.tempObj, this.state.selected[0].code, binsCount, right?'True':'False');
            code.append("_vp_print({'labels': _out.unique(), 'edges': list(_bins)})");
            vpKernel.execute(code.toString()).then(function(resultObj) {
                let { result } = resultObj;
                let { labels, edges } = JSON.parse(result);

                let edgeTbody = new com_String();
                labels && labels.forEach((label, idx) => {
                    let leftDisabled = 'disabled';
                    let rightDisabled = '';
                    if (idx === (labels.length - 1)) {
                        rightDisabled = 'disabled';
                    }
                    edgeTbody.append('<tr>');
                    edgeTbody.appendFormatLine('<td><input type="text" class="vp-input m vp-inner-popup-label" data-idx="{0}" value="{1}"/></td>', idx, label);
                    edgeTbody.appendLine('<td>:</td>');
                    edgeTbody.appendFormatLine('<td><input type="number" class="vp-input m vp-inner-popup-left-edge" data-idx="{0}" value="{1}" {2}/></td>', idx, edges[idx], leftDisabled);
                    edgeTbody.appendLine('<td>~</td>');
                    edgeTbody.appendFormatLine('<td><input type="number" class="vp-input m vp-inner-popup-right-edge" data-idx="{0}" value="{1}" {2}/></td>', idx + 1, edges[idx+1], rightDisabled);
                    edgeTbody.append('</tr>');
                });
                $(that.wrapSelector('.vp-inner-popup-range-table tbody')).html(edgeTbody.toString());

                // label change event
                $(that.wrapSelector('.vp-inner-popup-label')).change(function() {
                    $(that.wrapSelector('.vp-inner-popup-islabelchanged')).val("true");
                });

                // edge change event
                $(that.wrapSelector('.vp-inner-popup-left-edge')).change(function() {
                    let idx = $(this).data('idx');
                    let val = $(this).val();
                    $(that.wrapSelector(`.vp-inner-popup-right-edge[data-idx=${idx}]`)).val(val);
                    $(that.wrapSelector('.vp-inner-popup-isedgechanged')).val("true");
                });
                $(that.wrapSelector('.vp-inner-popup-right-edge')).change(function() {
                    let idx = $(this).data('idx');
                    let val = $(this).val();
                    $(that.wrapSelector(`.vp-inner-popup-left-edge[data-idx=${idx}]`)).val(val);
                    $(that.wrapSelector('.vp-inner-popup-isedgechanged')).val("true");
                });

            }).catch(function(errObj) {
                // TODO:
            });
        }

        templateForBody() {
            let page = $(frameHtml);

            let allocateSelector = new DataSelector({
                pageThis: this, id: 'vp_feReturn', placeholder: 'Variable name', required: true, value: '_vp'
            });
            $(page).find('#vp_feReturn').replaceWith(allocateSelector.toTagString());

            return page;
        }

        render() {
            super.render();

            var {
                originObj,
                returnObj,
                inplace,
                steps
            } = this.state;

            this.loadVariableList();

            this.renderToolbar();
    
            $(this.wrapSelector('#vp_feVariable')).val(originObj);
    
            $(this.wrapSelector('#vp_feReturn')).val(returnObj);

            $(this.wrapSelector('#inplace')).prop('checked', inplace);
    
            // execute all steps
            if (steps && steps.length > 0) {
                var code = steps.join('\n');
                // this.state.steps = [];
                this.loadCode(code);
            }

            // resize codeview
            $(this.wrapSelector('.vp-popup-codeview-box')).css({'height': '300px'})
        }

        renderVariableList(varList, defaultValue='') {
            let mappedList = varList.map(obj => { return { label: obj.varName, value: obj.varName, dtype: obj.varType } });

            var variableInput = new SuggestInput();
            variableInput.setComponentID('vp_feVariable');
            variableInput.addClass('vp-state');
            variableInput.setPlaceholder('Select variable');
            variableInput.setSuggestList(function () { return mappedList; });
            variableInput.addAttribute('required', true);
            variableInput.setSelectEvent(function (value) {
                $(this.wrapSelector()).val(value);
                $(this.wrapSelector()).trigger('change');
            });
            variableInput.setNormalFilter(true);
            variableInput.setValue(defaultValue);
            $(this.wrapSelector('#vp_feVariable')).replaceWith(function() {
                return variableInput.toTagString();
            });
        }

        renderToolbar() {
            let that = this;
            $(this.wrapSelector('.vp-fe-toolbox')).html('');
            // add menu list
            this.menuList & this.menuList.forEach(menuObj => {
                // show menu list dynamically
                let { id, label, child, axis, selection } = menuObj;
                let enabled = true;
                if ((that.state.axis !== FRAME_AXIS.NONE) && (axis !== undefined) && (axis !== FRAME_AXIS.NONE) && (that.state.axis !== axis)) {
                    enabled = false;
                }
                if (selection !== undefined && (selection !== FRAME_SELECT_TYPE.NONE)) {
                    if ((selection === FRAME_SELECT_TYPE.SINGLE) && (that.state.selected.length !== 1)) {
                        enabled = false;
                    }
                    if ((selection === FRAME_SELECT_TYPE.MULTI) && (that.state.selected.length === 0)) {
                        enabled = false;
                    }
                }
                let selected = id === that.state.menu;
                let $menu = $(`<div class="vp-dropdown ${enabled?'':'disabled'}">
                    <div class="vp-drop-button ${enabled?'':'disabled'} ${selected?'selected':''}" data-menu="${id}">${label}</div>
                    <div class="vp-dropdown-content"></div>
                </div>`);
                child && child.forEach(itemObj => {
                    let { id, label, menuType, axis, selection } = itemObj;
                    let enabled = true;
                    if ((that.state.axis !== FRAME_AXIS.NONE) && (axis !== undefined) && (axis !== FRAME_AXIS.NONE) && (that.state.axis !== axis)) {
                        enabled = false;
                    }
                    if (selection !== undefined && (selection !== FRAME_SELECT_TYPE.NONE)) {
                        if ((selection === FRAME_SELECT_TYPE.SINGLE) && (that.state.selected.length !== 1)) {
                            enabled = false;
                        }
                        if ((selection === FRAME_SELECT_TYPE.MULTI) && (that.state.selected.length === 0)) {
                            enabled = false;
                        }
                    }
                    let selected = that.state.menuItem === id;
                    $menu.find('.vp-dropdown-content')
                        .append($(`<div class="vp-dropdown-item ${VP_FE_MENU_ITEM} ${enabled?'':'disabled'} ${selected?'selected':''}" data-menu="${id}" data-type="${menuType}" data-parent="${menuObj.id}">${label}</div>`));
                });
                $(this.wrapSelector('.vp-fe-toolbox')).append($menu);
            });
        }

        renderTable(renderedText, isHtml=true) {
            var tag = new com_String();
            // Table
            tag.appendFormatLine('<div class="{0} {1} {2}">', VP_FE_TABLE, 'rendered_html', 'vp-scrollbar');
            if (isHtml) {
                tag.appendFormatLine('<table class="dataframe">{0}</table>', renderedText);
                // More button
                tag.appendFormatLine('<div class="{0} {1}">More...</div>', VP_FE_TABLE_MORE, 'vp-button');
            } else {
                tag.appendFormatLine('<pre>{0}</pre>', renderedText);
            }
            tag.appendLine('</div>'); // End of Table
            return tag.toString();
        }

        /**
         * Get last code to set preview
         * @returns 
         */
        getCurrentCode() {
            let { inplace, steps, tempObj, returnObj } = this.state;
            let codeList = steps;
            if (inplace === true) {
                codeList = steps.slice(1, steps.length);
            }
            
            // get last code
            let currentCode = codeList[codeList.length - 1];
            if (currentCode && currentCode != '') {
                currentCode = currentCode.replaceAll(tempObj, returnObj);
            } else {
                currentCode = '';
            }
            return currentCode;
        }

        generateCode() {
            var code = '';
            // if inplace is true, join steps without .copy()
            if (this.state.inplace === true) {
                code = this.state.steps.slice(1).join('\n');
            } else {
                code = this.state.steps.join('\n');
            }
            var returnVariable = $(this.wrapSelector('#vp_feReturn')).val();
            if (returnVariable != '') {
                code = code.replaceAll(this.state.tempObj, returnVariable);

                if (code != '') {
                    code += '\n' + returnVariable;
                }
            } else {
                code += '\n' + this.state.tempObj;
            }
            return code;
        }

        initState() {
            this.state.selected = [];
            this.state.axis = FRAME_AXIS.NONE;
            this.state.lines = TABLE_LINES;
            this.state.steps = [];
        }

        // FIXME: 
        renderButton() {
            // set button next to input tag
            var buttonTag = new com_String();
            buttonTag.appendFormat('<button type="button" class="{0} {1} {2}">{3}</button>'
                                    , VP_FE_BTN, this.uuid, 'vp-button', 'Edit');
            if (this.pageThis) {
                $(this.pageThis.wrapSelector('#' + this.targetId)).parent().append(buttonTag.toString());
            }
        }

        setPreview(previewCodeStr) {
            // get only last line of code
            var previewCode = previewCodeStr;
            if (previewCodeStr.includes('\n') === true) {
                let previewCodeLines = previewCodeStr.split('\n');
                previewCode = previewCodeLines.pop();
            }
            this.setCmValue('previewCode', previewCode);
        }

        loadVariableList() {
            var that = this;
            // load using kernel
            var dataTypes = ['DataFrame'];
            vpKernel.getDataList(dataTypes).then(function(resultObj) {
                let { result } = resultObj;
                try {
                    var varList = JSON.parse(result);
                    // render variable list
                    // get prevvalue
                    var prevValue = that.state.originObj;
                    // if (varList && varList.length > 0 && prevValue == '') {
                    //     prevValue = varList[0].varName;
                    //     that.state.originObj = prevValue;
                    // }
                    // replace
                    that.renderVariableList(varList, prevValue);
                    $(that.wrapSelector('#vp_feVariable')).trigger('change');
                } catch (ex) {
                    vpLog.display(VP_LOG_TYPE.ERROR, 'FrameEditor:', result);
                }
            });
        }

        /**
         * Render Inner popup page
         * @param {*} type
         * @returns 
         */
        renderAddPage(type = '') {
            var content = new com_String();
            content.appendFormatLine('<div class="{0}">', 'vp-inner-popup-addpage');
            content.appendLine('<div>');
            content.appendLine('<table class="vp-tbl-gap5 wp100"><colgroup><col width="110px"><col width="*"></colgroup>');
            content.appendFormatLine('<tr><th class="{0}">New {1}</th>', 'vp-orange-text', type);
            if (type === 'row') {
                content.appendFormatLine('<td><input type="text" class="{0}" placeholder="{1}"/>', 'vp-inner-popup-input0', 'Type row name');
            } else {
                content.appendFormatLine('<td><input type="text" class="{0}" placeholder="{1}"/>', 'vp-inner-popup-input0', 'level 0');
            }
            content.appendFormatLine('<label><input type="checkbox" class="{0}" checked/><span>{1}</span></label>'
                                    , 'vp-inner-popup-inputastext0', 'Text');
            content.appendLine('</td></tr>');
            if (type === 'column' && this.state.columnLevel > 1) {
                for (let i = 1; i < this.state.columnLevel; i++ ) {
                    content.appendLine('<tr><td></td>');
                    content.appendFormatLine('<td><input type="text" class="{0}" placeholder="{1}"/>', 'vp-inner-popup-input' + i, 'level ' + i);
                    content.appendFormatLine('<label><input type="checkbox" class="{0}" checked/><span>{1}</span></label>'
                                            , 'vp-inner-popup-inputastext' + i, 'Text');
                    content.appendLine('</td></tr>');
                }
            }
            if (type === 'column') {
                content.appendLine('<tr><th><label>Add Type</label></th>');
                content.appendFormatLine('<td><select class="{0}">', 'vp-inner-popup-addtype');
                content.appendFormatLine('<option value="{0}">{1}</option>', 'variable', 'Variable');
                content.appendFormatLine('<option value="{0}">{1}</option>', 'apply', 'Apply');
                content.appendLine('</select></td></tr>');
            }
            content.appendLine('</table>');
            content.appendLine('</div>'); // end of vp-inner-popup-header
    
            content.appendLine('<hr style="margin: 5px 0px;"/>');
            
            // tab 1. variable
            content.appendFormatLine('<div class="{0} {1}">', 'vp-inner-popup-tab', 'variable');
            content.appendLine('<table class="vp-tbl-gap5"><colgroup><col width="110px"><col width="*"></colgroup>');
            content.appendLine('<tr class="vp-inner-popup-value-row">');
            content.appendLine('<th><label>Variable</label></th>');
            content.appendFormatLine('<td><input type="text" class="{0}" data-idx="{1}" placeholder="Type value"/>', 'vp-inner-popup-value', 0);
            content.appendFormatLine('<label><input type="checkbox" class="{0}"/><span>{1}</span></label>', 'vp-inner-popup-istext','Text');
            // content.appendFormatLine('<span class="{0} vp-icon-close-small"></span>', 'vp-inner-popup-delete-value');
            content.appendLine('</td></tr>');
            content.appendFormatLine('<tr class="vp-inner-popup-addvalue-row"><td colspan="2"><button class="vp-button {0}">+ Variable</button></td></tr>', 'vp-inner-popup-addvalue');
            content.appendLine('</table>');
            content.appendLine('</div>'); // end of vp-inner-popup-tab value

            // tab 2. apply
            content.appendFormatLine('<div class="{0} {1}" style="display: none;">', 'vp-inner-popup-tab', 'apply');
            content.appendLine('<div class="vp-grid-box">');
            content.appendLine('<div class="vp-grid-col-110">');
            content.appendLine('<label>Column</label>');
            content.appendLine(this.renderColumnList(this.state.columnList));
            content.appendLine('</div>');
            content.appendFormatLine('<textarea type="text" id="{0}" class="{1}" placeholder="{2}">lambda x: x</textarea>'
                                    , 'vp_popupAddApply', 'vp-input vp-inner-popup-apply-lambda', 'Type code manually');
            content.appendLine('</div>');
            content.appendLine('</div>'); // end of vp-inner-popup-tab apply
            content.appendLine('</div>'); // end of vp-inner-popup-addpage
            
            // set content
            $(this.wrapSelector('.vp-inner-popup-body')).html(content.toString());
            return content.toString();
        }

        renderAddValueBox(idx) {
            // add dataselector
            let valueSelector = new DataSelector({
                pageThis: this, id: 'vp_addValue' + idx, classes: 'vp-inner-popup-value', placeholder: 'Type value'
            });
            $(this.wrapSelector('.vp-inner-popup-body')).find('.vp-inner-popup-value:nth(' + idx + ')').replaceWith(valueSelector.toTagString());
        }

        renderCalculator(idx) {
            let content = new com_String();
            content.appendFormatLine('<select class="{0}" data-idx="{1}">', 'vp-input s vp-inner-popup-oper', idx);
            let operList = ['+', '-', '*', '/', '%', '//', '==', '!=', '>=', '>', '<=', '<', 'and', 'or'];
            operList.forEach(oper => {
                content.appendFormatLine('<option value="{0}">{1}</option>', oper, oper);
            });
            content.appendFormatLine('</select>');
            return content.toString();
        }

        renderColumnList = function(columnList) {
            var selectTag = new com_String();
            selectTag.appendFormatLine('<select class="{0}">', 'vp-inner-popup-apply-column');
            columnList && columnList.forEach(col => {
                selectTag.appendFormatLine('<option value="{0}">{1}</option>', col.code, col.label);
            }); 
            selectTag.appendLine('</select>');
            return selectTag.toString();
        }

        renderDropPage() {
            var content = new com_String();
            content.appendFormatLine('<div class="{0} vp-grid-box vp-center">', 'vp-inner-popup-drop-page');
            content.appendFormatLine('Are you sure to delete {0} below?', (this.state.axis === FRAME_AXIS.COLUMN?'columns':'rows'));
            content.appendFormatLine('<pre>{0}</pre>', this.state.selected.map(col=>col.code).join(', '))
            content.appendLine('</div>');
            // set content
            $(this.wrapSelector('.vp-inner-popup-body')).html(content.toString());
            return content.toString();
        }

        /**
         * Render rename page
         * @param {string} type FRAME_AXIS
         * @returns 
         */
        renderRenamePage = function(type = FRAME_AXIS.COLUMN) {
            var content = new com_String();
            content.appendFormatLine('<div class="{0} {1}">', 'vp-inner-popup-rename-page', 'vp-scrollbar');
            if (type === FRAME_AXIS.COLUMN && this.state.columnLevel > 1) {
                content.appendFormatLine('<div class="{0}">', 'vp-grid-col-110');
                content.appendLine('<label>Level</label>');
                content.appendFormatLine('<select class="{0}">', 'vp-inner-popup-level');
                for (let i = 0; i < this.state.columnLevel; i++) {
                    content.appendFormatLine('<option value="{0}">{1}</option>', i, i);
                }
                content.appendLine('</select>');
                content.appendLine('</div>');
                content.appendLine('<hr style="margin: 5px 0;">');
            }
            content.appendLine('<table class="vp-tbl-gap5 wp100">');
            content.appendLine('<colgroup><col width="110px"><col width="*"></colgroup>');
            content.appendLine('<tbody>');
            if (this.state.columnLevel > 1) {
                let selectedList = this.state.selected;
                let selectedStr = '';
                if (selectedList.length === 0) {
                    // select all
                    selectedList = this.state.columnList;
                    selectedStr = selectedList.map(col => "(" + col.code.join(',') + ")").join(',')
                } else {
                    selectedStr = selectedList.map(col => col.code).join(',');
                }
                let codeStr = com_util.formatString("_vp_print([ list(col) for col in {0}[[{1}]].columns.to_list()])"
                    , this.state.tempObj, selectedStr);
                let that = this;
                vpKernel.execute(codeStr).then(function(resultObj) {
                    let { result } = resultObj;
                    let colList = JSON.parse(result);
                    let colTags = new com_String();
                    for (let i = 0; i < colList.length; i++) {
                        let colLevels = colList[i];
                        for (let j = 0; j < colLevels.length; j++) {
                            let idx = (i + 1) * j
                            colTags.appendFormatLine('<tr class="{0}">', 'vp-inner-popup-input-row');
                            colTags.appendFormatLine('<th><label style="padding-left:{0}px;">{1}</label></th>', j * 10, colLevels[j]);
                            colTags.appendFormatLine('<td><input type="text" class="{0}" data-code="{1}"/>'
                                , 'vp-inner-popup-input' + idx, com_util.convertToStr(colLevels[j], true)); // FIXME: text or num ?
                            colTags.appendFormatLine('<label><input type="checkbox" class="{0}" checked/><span>{1}</span></label></td>', 'vp-inner-popup-istext' + idx, 'Text');
                            colTags.appendLine('</tr>');
                        }
                    }
                    $(that.wrapSelector('.vp-inner-popup-rename-page tbody')).html(colTags.toString());
                });
            } else {
                let selectedList = this.state.selected;
                if (selectedList.length === 0) {
                    // select all
                    selectedList = this.state.columnList;
                }
                selectedList.forEach((col, idx) => {
                    content.appendFormatLine('<tr class="{0}">', 'vp-inner-popup-input-row');
                    content.appendFormatLine('<th><label>{0}</label></th>', col.label);
                    content.appendFormatLine('<td><input type="text" class="{0}" data-code="{1}"/>'
                        , 'vp-inner-popup-input' + idx, col.code);
                    content.appendFormatLine('<label><input type="checkbox" class="{0}" checked/><span>{1}</span></label></td>'
                        , 'vp-inner-popup-istext' + idx, 'Text');
                    content.appendLine('</tr>');
                });
            }
            content.appendLine('</tbody>');
            content.appendLine('</table>');
            content.appendLine('</div>');

            // set content
            $(this.wrapSelector('.vp-inner-popup-body')).html(content.toString());
            return content.toString();
        }

        renderDiscretizePage() {
            var content = new com_String();
            content.appendLine(`
            <div class="vp-inner-popup-discretize-page vp-grid-box">
                <div class="vp-grid-col-110">
                    <label class="vp-orange-text">New column</label>
                    <div>
                        <input type="text" class="vp-input vp-inner-popup-input" value=""/>
                        <label>
                            <input type="checkbox" class="vp-inner-popup-inputastext" checked>
                            <span>Text</span>
                        </label>
                    </div>
                    <label>Target column</label>
                    <input type="text" class="vp-input" value="${this.state.selected[0].label}" readonly />
                    <label>Bins count</label>
                    <input type="number" class="vp-input vp-inner-popup-bins" placeholder="Input count of bins"/>
                    <label>Discretize type</label>
                    <select class="vp-inner-popup-discretizetype">
                        <option value="cut">Interval based</option>
                        <option value="qcut">Quantile based</option>
                    </select>
                </div>
                <label title="right option">
                    <input type="checkbox" class="vp-inner-popup-right" checked>
                    <span>Include the rightmost edge</span>
                </label>
                <hr style="margin: 5px 0;"/>
                <table class="vp-tbl-gap5 vp-inner-popup-range-table">
                    <colgroup><col width="116px"><col width="5px"><col width="116px"><col width="5px"><col width="*"></colgroup>
                    <thead>
                        <tr>
                            <th>Label</th>
                            <th></th>
                            <th>Left edge</th>
                            <th></th>
                            <th>Right edge</th>
                        </tr>
                    </thead>
                    <tbody>
                    </tbody>
                </table>
                <label title="Set all labels as text">
                    <input type="checkbox" class="vp-inner-popup-labelastext">
                    <span>Label as Text</span>
                </label>
                <input type="hidden" class="vp-inner-popup-islabelchanged" value=false />
                <input type="hidden" class="vp-inner-popup-isedgechanged" value=false />
            </div>
            `)

            // set content
            $(this.wrapSelector('.vp-inner-popup-body')).html(content.toString());
            return content.toString();
        }

        renderShiftPage() {
            var content = new com_String();
            content.appendFormatLine('<div class="{0}">', 'vp-inner-popup-shift-page');
            content.appendLine('<table class="vp-tbl-gap5">');
            content.appendLine('<colgroup><col width="100px"><col width="*"></colgroup>');
            content.appendLine('<tr>');
            content.appendFormatLine('<th><label class="vp-orange-text">{0}</label></th>', 'Periods');
            content.appendFormatLine('<td><input type="number" class="{0}" placeholder="{1}" value="1" required></td>'
                , 'vp-inner-popup-periods', 'Type number');
            content.appendLine('</tr>');
            content.appendFormatLine('<td colspan="2"><label class="vp-orange-text vp-italic">{0}</label> <label class="vp-gray-text vp-italic">{1}</label></td>'
                , 'NOTE:', 'Number of periods to shift. Can be positive or negative.');
            content.appendLine('</tr>');
            content.appendLine('<tr>');
            content.appendFormatLine('<th><label>{0}</label></th>', 'Frequency');
            content.appendFormatLine('<td><input type="text" class="{0}" placeholder="{1}"></td>'
                , 'vp-inner-popup-freq', 'Offset for timeseries');
            content.appendLine('</tr>');
            content.appendLine('<tr>');
            content.appendFormatLine('<th><label>{0}</label></th>', 'Fill value');
            content.appendLine('<td>');
            content.appendFormatLine('<input type="text" class="{0}" placeholder="{1}">'
                , 'vp-inner-popup-fillvalue', 'Type value to fill');
            content.appendFormatLine('<label><input type="checkbox" class="{0}"/><span>{1}</span></label>', 'vp-inner-popup-fillvalueastext', 'Text');
            content.appendLine('</td>');
            content.appendLine('</tr>');
            content.appendLine('</table>');
            content.appendLine('</div>');

            // set content
            $(this.wrapSelector('.vp-inner-popup-body')).html(content.toString());
            return content.toString();
        }

        /**
         * 
         * @param {int} type FRAME_AXIS
         * @returns 
         */
        renderSortPage(type=FRAME_AXIS.COLUMN) {
            var content = new com_String();
            content.appendFormatLine('<div class="{0}">', 'vp-inner-popup-sort-page');
            content.appendLine('<div class="vp-grid-col-110">');
            // sort by
            let sortByStr = 'column';
            let sortByList = [];
            if (type === FRAME_AXIS.ROW) {
                sortByStr = 'level';
                sortByList = Array.from({ length:this.state.indexLevel },(v,k)=>{ return {label: k, code: k} });
            } else {
                sortByList = this.state.selected;
            }
            content.appendFormatLine('<label>{0} {1}</label>', 'Sort by', sortByStr);
            // movable list
            content.appendLine('<div class="vp-inner-popup-sortby">');
            sortByList.forEach((obj, idx) => {
                content.appendFormatLine('<div class="vp-inner-popup-sortby-item" data-code="{0}">', obj.code);
                content.appendFormatLine('<label>{0}</label>', obj.label);
                content.appendLine('<span class="vp-inner-popup-sortby-down vp-icon-chevron-down" title="Set lower priority on sorting"></span>');
                content.appendLine('<span class="vp-inner-popup-sortby-up vp-icon-chevron-up" title="Set upper priority on sorting"></span>');
                content.appendLine('</div>');
            });
            content.appendLine('</div>');

            // ascending
            content.appendFormatLine('<label>{0}</label>', 'Ascending');
            content.appendFormatLine('<select class="{0}">', 'vp-inner-popup-isascending');
            content.appendFormatLine('<option value="{0}">{1}</option>', "True", "True (default)");
            content.appendFormatLine('<option value="{0}">{1}</option>', "False", "False");
            content.appendLine('</select>');
            content.appendLine('</div>');
            content.appendLine('</div>');
            // set content
            $(this.wrapSelector('.vp-inner-popup-body')).html(content.toString());
            return content.toString();
        }

        renderReplacePage() {
            var content = new com_String();
            content.appendFormatLine('<div class="{0}">', 'vp-inner-popup-replacepage');
            content.appendLine('<div>');
            content.appendLine('<table class="vp-tbl-gap5 wp100"><colgroup><col width="80px"><col width="*"></colgroup>');
            content.appendFormatLine('<tr><th class="{0}">{1}</th>', '', 'Column');
            var target = this.state.selected.map(col => col.label).join(',');
            content.appendFormatLine('<td><input type="text" class="{0}" value="{1}" readonly/>', 'vp-inner-popup-input1', target);
            content.appendLine('</td></tr>');
            content.appendLine('</table>');
            content.appendLine('</div>'); // end of vp-inner-popup-header
    
            content.appendLine('<hr style="margin: 5px 0px;"/>');
            // replace page
            content.appendFormatLine('<div class="{0}">', 'vp-inner-popup-replace-table');
            // subset
            content.appendLine('<table class="vp-tbl-gap5"><colgroup><col width="80px"><col width="*"></colgroup>');

            content.appendLine('<tr><td><label>Condition</label></td>');
            content.appendLine('<td><div class="vp-fr-subset-box">');
            content.appendLine('<textarea class="vp-input vp-inner-popup-subset"></textarea>');
            content.appendLine('</div></td>');
            content.appendLine('</tr>');

            content.appendLine('<tr><th><label>Variable</label></th>');
            content.appendFormatLine('<td><input type="text" class="{0}"/>', 'vp-inner-popup-input3');
            content.appendFormatLine('<label><input type="checkbox" class="{0}"/><span>{1}</span></label>', 'vp-inner-popup-istext3','Text');
            content.appendLine('</td></tr>');
            content.appendLine('<tr><td colspan="2">');
            content.appendFormatLine('<label><input type="checkbox" class="{0}"/><span>{1}</span></label>', 'vp-inner-popup-use-regex', 'Use Regular Expression');
            content.appendLine('</td></tr>');
            content.appendLine('</table></div>');

            content.appendLine('</div>'); // end of vp-inner-popup-addpage

            // set content
            $(this.wrapSelector('.vp-inner-popup-body')).html(content.toString());
            return content.toString();
        }

        renderAsType() {
            var astypeList = this.astypeList;
            var content = new com_String();
            content.appendFormatLine('<div class="{0}">', 'vp-inner-popup-astype');
            content.appendFormatLine('<table class="{0}">', 'vp-inner-popup-astype-table');
            content.appendLine('<colgroup><col width="140px"><col width="80px"><col width="*"></colgroup>');
            content.appendFormatLine('<thead style="height: 30px"><th>{0}</th><th>{1}</th><th class="{2}">{3}</th></thead>'
                                    , 'Column', 'Data type', 'vp-orange-text', 'New data type');
            content.appendLine('<tbody>');
            this.state.selected.forEach((col, idx) => {
                content.appendLine('<tr>');
                content.appendFormatLine('<td title="{0}">{1}</td>', col.label, col.label);
                content.appendFormatLine('<td><input type="text" value="{0}" readonly/></td>', col.type);
                var suggestInput = new SuggestInput();
                suggestInput.addClass('vp-inner-popup-astype' + idx);
                suggestInput.addAttribute('data-col', col.code);
                suggestInput.setSuggestList(function() { return astypeList; });
                suggestInput.setPlaceholder('Data type');
                content.appendFormatLine('<td>{0}</td>', suggestInput.toTagString());
                content.appendLine('</tr>');
            });
            content.appendLine('</tbody></table>');
            content.append('</div>');

            // set content
            $(this.wrapSelector('.vp-inner-popup-body')).html(content.toString());
            return content.toString();
        }

        renderFillNAPage() {
            var content = new com_String();
            content.appendFormatLine('<div class="{0}">', 'vp-inner-popup-fillna-page');
            content.appendLine('<table class="vp-tbl-gap5">');
            content.appendLine('<colgroup><col width="100px"><col width="*"></colgroup>');
            content.appendLine('<tr>');
            content.appendFormatLine('<th><label class="vp-orange-text">{0}</label></th>', 'Fill value');
            content.appendLine('<td>');
            content.appendFormatLine('<input type="text" id="{0}" class="{1}" placeholder="{2}" required>'
                , 'vp_fillValue', 'vp-inner-popup-value', 'Type or select value');
            content.appendFormatLine('<label><input type="checkbox" class="{0}"/><span>{1}</span></label>'
                , 'vp-inner-popup-valueastext', 'Text');
            content.appendLine('</td>');
            content.appendLine('</tr>');
            content.appendLine('<tr>');
            content.appendFormatLine('<th><label>{0}</label></th>', 'Method');
            content.appendFormatLine('<td><select class="{0}">', 'vp-inner-popup-method');
            content.appendFormatLine('<option value="{0}">{1}</option>', "", "Select option...");
            content.appendFormatLine('<option value="{0}">{1}</option>', "ffill", "Forward fill");
            content.appendFormatLine('<option value="{0}">{1}</option>', "bfill", "Back fill");
            content.appendLine('</select></td>');
            content.appendLine('</tr>');
            content.appendLine('<tr>');
            content.appendFormatLine('<th><label>{0}</label></th>', 'Limit');
            content.appendLine('<td>');
            content.appendFormatLine('<input type="number" class="{0}" placeholder="{1}">'
                , 'vp-inner-popup-limit', 'Type limit to fill');
            content.appendLine('</td>');
            content.appendLine('</tr>');
            content.appendLine('</table>');
            content.appendLine('</div>');

            // set content
            $(this.wrapSelector('.vp-inner-popup-body')).html(content.toString());
            return content.toString();
        }

        openInputPopup(type, width=400, height=400) {
            var title = '';
            var content = '';
            let size = { width: width, height: height };
            let that = this;
    
            switch (parseInt(type)) {
                case FRAME_EDIT_TYPE.ADD_COL:
                    title = 'Add column';
                    size = { width: 450, height: 450 };
                    content = this.renderAddPage('column');
                    this.renderAddValueBox(0);

                    // bind event for adding values to calculate
                    $(this.wrapSelector('.vp-inner-popup-addvalue')).on('click', function() {
                        let valueCount = $(that.wrapSelector('.vp-inner-popup-value')).length;
                        $(`<tr class="vp-inner-popup-oper-row">
                            <td></td>
                            <td>${that.renderCalculator(valueCount)}</td>
                        </tr>
                        <tr class="vp-inner-popup-value-row">
                            <th><label>Variable</label></th>
                            <td>
                                <input type="text" class="vp-inner-popup-value"/>
                                <label><input type="checkbox" class="vp-inner-popup-istext"/><span>Text</span></label>
                                <span class="vp-inner-popup-delete-value vp-icon-close-small"></span>
                            </td>
                        </tr>`).insertBefore($(that.wrapSelector('.vp-inner-popup-addvalue-row')));
                        that.renderAddValueBox(valueCount);
                        
                        $(that.wrapSelector('.vp-inner-popup-delete-value')).off('click');
                        $(that.wrapSelector('.vp-inner-popup-delete-value')).on('click', function() {
                            // delete variable item
                            let index = $(this).closest('tr.vp-inner-popup-value-row').index();
                            $(that.wrapSelector('.vp-inner-popup-oper-row:nth(' + (index - 2) + ')')).remove();
                            $(that.wrapSelector('.vp-inner-popup-value-row:nth(' + (index - 1) + ')')).remove();
                        });
                    });

                    // bind codemirror for apply textarea
                    this.applyCm = this.initCodemirror({ 
                        key: 'vp-inner-popup-apply-lambda', 
                        selector: this.wrapSelector('.vp-inner-popup-apply-lambda'),
                    });
                    break;
                case FRAME_EDIT_TYPE.ADD_ROW:
                    title = 'Add row';
                    size = { width: 450, height: 450 };
                    content = this.renderAddPage('row');
                    this.renderAddValueBox(0);

                    // bind event for adding values to calculate
                    $(this.wrapSelector('.vp-inner-popup-addvalue')).on('click', function() {
                        let valueCount = $(that.wrapSelector('.vp-inner-popup-value')).length;
                        $(`<tr class="vp-inner-popup-oper-row">
                            <td></td>
                            <td>${that.renderCalculator(valueCount)}</td>
                        </tr>
                        <tr class="vp-inner-popup-value-row">
                            <th><label>Variable</label></th>
                            <td>
                                <input type="text" class="vp-inner-popup-value"/>
                                <label><input type="checkbox" class="vp-inner-popup-istext"/><span>Text</span></label>
                                <span class="vp-inner-popup-delete-value vp-icon-close-small"></span>
                            </td>
                        </tr>`).insertBefore($(that.wrapSelector('.vp-inner-popup-addvalue-row')));
                        that.renderAddValueBox(valueCount);
                        
                        $(that.wrapSelector('.vp-inner-popup-delete-value')).off('click');
                        $(that.wrapSelector('.vp-inner-popup-delete-value')).on('click', function() {
                            // delete variable item
                            let index = $(this).closest('tr.vp-inner-popup-value-row').index();
                            $(that.wrapSelector('.vp-inner-popup-oper-row:nth(' + (index - 2) + ')')).remove();
                            $(that.wrapSelector('.vp-inner-popup-value-row:nth(' + (index - 1) + ')')).remove();
                        });
                    });
                    break;
                case FRAME_EDIT_TYPE.DROP:
                    title = 'Drop ';
                    if (this.state.axis === FRAME_AXIS.COLUMN) {
                        title += 'columns';
                    } else {
                        title += 'rows';
                    }
                    size = { width: 400, height: 200 };
                    content = this.renderDropPage();
                    break;
                case FRAME_EDIT_TYPE.RENAME:
                    title = 'Rename ';
                    if (this.state.axis === FRAME_AXIS.ROW) {
                        title += 'rows';
                        content = this.renderRenamePage(FRAME_AXIS.ROW);
                    } else {
                        title += 'columns';
                        content = this.renderRenamePage(FRAME_AXIS.COLUMN);
                    }
                    break;
                case FRAME_EDIT_TYPE.DISCRETIZE:
                    title = 'Discretize';
                    size = { width: 450, height: 450 };
                    content = this.renderDiscretizePage();
                    break;
                case FRAME_EDIT_TYPE.DATA_SHIFT:
                    title = 'Data shift';
                    size = { width: 450, height: 300 };
                    content = this.renderShiftPage();

                    // set suggestinput
                    let freqFormats = [
                        {'label': 'infer', 'value': 'infer'},
                        {'label': 'second', 'value': 's'},
                        {'label': 'minute', 'value': 'T'},
                        {'label': 'hour', 'value': 'H'},
                        {'label': 'day', 'value': 'D'},
                        {'label': 'weekdays', 'value': 'B'},
                        {'label': 'week(Sunday)', 'value': 'W'},
                        {'label': 'week(Monday)', 'value': 'W-MON'},
                        {'label': 'first day of month', 'value': 'MS'},
                        {'label': 'last day of month', 'value': 'M'},
                        {'label': 'first weekday of month', 'value': 'BMS'},
                        {'label': 'last weekday of month', 'value': 'BM'}
                    ];
                    var freqInput = new SuggestInput();
                    freqInput.addClass('vp-inner-popup-freq');
                    freqInput.setPlaceholder('Type frequency');
                    freqInput.setSuggestList(freqFormats);
                    freqInput.setNormalFilter(true);
                    $(this.wrapSelector('.vp-inner-popup-freq')).replaceWith(function() {
                        return freqInput.toTagString();
                    });
                    break;
                case FRAME_EDIT_TYPE.SORT_INDEX:
                    title = 'Sort by index';
                    content = this.renderSortPage(FRAME_AXIS.ROW);
                    break;
                case FRAME_EDIT_TYPE.SORT_VALUES:
                    title = 'Sort by values';
                    content = this.renderSortPage(FRAME_AXIS.COLUMN);
                    break;
                case FRAME_EDIT_TYPE.REPLACE:
                    title = 'Replace';
                    // content = this.renderReplacePage();
                    content = this.renderReplacePage();
                    size = { width: 450, height: 300 };

                    // bind codemirror
                    this.subsetCm = this.initCodemirror({ 
                        key: 'vp-inner-popup-subset', 
                        selector: this.wrapSelector('.vp-inner-popup-subset'), 
                        type: 'readonly' 
                    });
                    // set subset
                    let contentState = that.getPopupContent(type);
                    this.subsetEditor = new Subset({ 
                        pandasObject: this.state.tempObj,
                        selectedColumns: [ com_util.convertToStr(contentState.name, contentState.nameastext) ],
                        config: { name: 'Subset' } }, 
                    { 
                        useInputVariable: true,
                        useInputColumns: true,
                        targetSelector: this.wrapSelector('.vp-inner-popup-subset'),
                        pageThis: this,
                        allowSubsetTypes: ['iloc', 'loc'],
                        beforeOpen: function(subsetThis) {
                            let contentState = that.getPopupContent(type);
                            let name = com_util.convertToStr(contentState.name, contentState.nameastext);
                            subsetThis.state.selectedColumns = [ name ];
                        },
                        finish: function(code) {
                            that.subsetCm.setValue(code);
                            that.subsetCm.save();
                            setTimeout(function () {
                                that.subsetCm.refresh();
                            }, 1);
                        }
                    });
                    // initial code
                    var code = this.subsetEditor.generateCode();
                    this.subsetCm.setValue(code);
                    this.subsetCm.save();
                    setTimeout(function () {
                        that.subsetCm.refresh();
                    }, 1);

                    // data selector
                    // vp-inner-popup-input3
                    // set dataselector
                    let replaceVarSelector = new DataSelector({
                        pageThis: this, id: 'vp_replaceVariable', classes: 'vp-inner-popup-input3', placeholder: 'Type or select variable'
                    });
                    $(this.wrapSelector('.vp-inner-popup-body')).find('.vp-inner-popup-input3').replaceWith(replaceVarSelector.toTagString());
                    break;
                case FRAME_EDIT_TYPE.AS_TYPE:
                    title = 'Convert type';
                    content = this.renderAsType();
                    break;
                case FRAME_EDIT_TYPE.FILL_NA:
                    title = 'Fill NA';
                    content = this.renderFillNAPage();

                    // set dataselector
                    let valueSelector = new DataSelector({
                        pageThis: this, id: 'vp_fillValue', classes: 'vp-inner-popup-value', placeholder: 'Type or select value'
                    });
                    $(this.wrapSelector('.vp-inner-popup-body')).find('.vp-inner-popup-value').replaceWith(valueSelector.toTagString());

                    // bind event on method
                    $(this.wrapSelector('.vp-inner-popup-method')).on('change', function() {
                        let changedVal = $(this).val();
                        if (changedVal === '') {
                            // disable limit
                            $(that.wrapSelector('.vp-inner-popup-limit')).prop('disabled', true);
                        } else {
                            // enable limit
                            $(that.wrapSelector('.vp-inner-popup-limit')).prop('disabled', false);
                        }
                    });
                    break;
                default:
                    type = FRAME_EDIT_TYPE.NONE;
                    break;
            }
    
            this.state.popup.type = type;

            // set size
            $(this.wrapSelector('.vp-inner-popup-box')).css(size);
            
            // bindEventForAddPage
            this.bindEventForPopupPage(type);

            // set column list
            vpKernel.getColumnList(this.state.tempObj).then(function(resultObj) {
                let { result } = resultObj;
                var { list } = JSON.parse(result);
                var tag1 = new com_String();
                var tag2 = new com_String();
                tag1.appendFormatLine('<select class="{0}">', 'vp-inner-popup-var1col');
                tag2.appendFormatLine('<select class="{0}">', 'vp-inner-popup-var2col');
                list && list.forEach(col => {
                    tag1.appendFormatLine('<option data-code="{0}" value="{1}">{2}</option>'
                            , col.value, col.label, col.label);
                    tag2.appendFormatLine('<option data-code="{0}" value="{1}">{2}</option>'
                            , col.value, col.label, col.label);
                });
                tag1.appendLine('</select>');
                tag2.appendLine('</select>');
                // replace column list
                $(that.wrapSelector('.vp-inner-popup-var1col')).replaceWith(function() {
                    return tag1.toString();
                });
                $(that.wrapSelector('.vp-inner-popup-var2col')).replaceWith(function() {
                    return tag2.toString();
                });
            });
    
            // show popup box
            this.openInnerPopup(title);
        }

        getPopupContent = function(type) {
            let that = this;
            var content = {};
            switch (type) {
                case FRAME_EDIT_TYPE.ADD_COL:
                case FRAME_EDIT_TYPE.ADD_ROW:
                    let variableTuple = [];
                    let thisLevel = this.state.columnLevel;
                    if (type === FRAME_EDIT_TYPE.ADD_ROW) {
                        thisLevel = this.state.indexLevel;
                    }
                    for (let i = 0; i < thisLevel; i++) {
                        let val = $(this.wrapSelector('.vp-inner-popup-input' + i)).val();
                        let istext = $(this.wrapSelector('.vp-inner-popup-inputastext' + i)).prop('checked');
                        variableTuple.push(com_util.convertToStr(val, istext));
                    }
                    if (variableTuple.length > 1) {
                        content['name'] = '(' + variableTuple.join(',') + ')';
                    } else {
                        content['name'] = variableTuple.join(',');
                    }
                    var tab = $(this.wrapSelector('.vp-inner-popup-addtype')).val();
                    if (type === FRAME_EDIT_TYPE.ADD_ROW) {
                        tab = 'variable';
                    }
                    content['addtype'] = tab;
                    if (tab == 'variable') {
                        let values = [];
                        let opers = [];
                        $(this.wrapSelector('.vp-inner-popup-tab.variable tr.vp-inner-popup-value-row')).each((idx, tag) => {
                            let valueastext = $(tag).find('.vp-inner-popup-istext').prop('checked');
                            values.push(com_util.convertToStr($(tag).find('.vp-inner-popup-value').val(), valueastext));
                            let oper = $(that.wrapSelector('.vp-inner-popup-oper:nth(' + idx + ')')).val();
                            if (oper && oper !== '') {
                                opers.push(oper);
                            }
                        });
                        content['values'] = values;
                        content['opers'] = opers;
                    } else if (tab == 'apply') {
                        content['column'] = $(this.wrapSelector('.vp-inner-popup-apply-column')).val();
                        content['apply'] = $(this.wrapSelector('.vp-inner-popup-apply-lambda')).val();
                    }
                    break;
                case FRAME_EDIT_TYPE.REPLACE:
                    content['name'] = $(this.wrapSelector('.vp-inner-popup-input1')).val();
                    if (content['name'] == '') {
                        $(this.wrapSelector('.vp-inner-popup-input1')).attr({'placeholder': 'Required input'});
                        $(this.wrapSelector('.vp-inner-popup-input1')).focus();
                    }
                    content['subset'] = this.subsetCm?this.subsetCm.getValue():'';
                    content['value'] = $(this.wrapSelector('.vp-inner-popup-input3')).val();
                    content['valueastext'] = $(this.wrapSelector('.vp-inner-popup-istext3')).prop('checked');
                    break;
                case FRAME_EDIT_TYPE.RENAME:
                    content['list'] = {};
                    let inputLength = $(this.wrapSelector('.vp-inner-popup-input-row')).length;
                    for (let idx = 0; idx < inputLength; idx++) {
                        var label = $(this.wrapSelector('.vp-inner-popup-input'+idx)).data('code');
                        var value = $(this.wrapSelector('.vp-inner-popup-input'+idx)).val();
                        var istext = $(this.wrapSelector('.vp-inner-popup-istext'+idx)).prop('checked');
                        content['list'][idx] = {
                            label: label,
                            value: value,
                            istext: istext
                        };
                    }
                    if (this.state.axis !== FRAME_AXIS.ROW && this.state.columnLevel > 1) {
                        content['level'] = $(this.wrapSelector('.vp-inner-popup-level')).val();
                    }
                    break;
                case FRAME_EDIT_TYPE.SORT_INDEX:
                case FRAME_EDIT_TYPE.SORT_VALUES:
                    let values = [];
                    $(this.wrapSelector('.vp-inner-popup-sortby-item')).each((idx, tag) => {
                        values.push($(tag).data('code'));
                    });
                    content['values'] = values;
                    content['ascending'] = $(this.wrapSelector('.vp-inner-popup-isascending')).val();
                    break;
                case FRAME_EDIT_TYPE.AS_TYPE:
                    this.state.selected.forEach((col, idx) => {
                        var value = $(this.wrapSelector('.vp-inner-popup-astype'+idx)).val();
                        content[idx] = {
                            label: col.code,
                            value: value
                        };
                    });
                    break;
                case FRAME_EDIT_TYPE.DISCRETIZE:
                    content['input'] = $(this.wrapSelector('.vp-inner-popup-input')).val();
                    content['inputastext'] = $(this.wrapSelector('.vp-inner-popup-inputastext')).prop('checked');
                    content['bins'] = $(this.wrapSelector('.vp-inner-popup-bins')).val();
                    content['type'] = $(this.wrapSelector('.vp-inner-popup-discretizetype')).val();
                    content['isright'] = $(this.wrapSelector('.vp-inner-popup-right')).prop('checked');
                    let labelastext = $(this.wrapSelector('.vp-inner-popup-labelastext')).prop('checked');
                    let islabelchanged = $(this.wrapSelector('.vp-inner-popup-islabelchanged')).val() === 'true';
                    let isedgechanged = $(this.wrapSelector('.vp-inner-popup-isedgechanged')).val() === 'true';
                    let rangeTableTags = $(this.wrapSelector('.vp-inner-popup-range-table tbody tr'));
                    let labels = [];
                    let edges = [];
                    rangeTableTags && rangeTableTags.each((idx, tag) => {
                        if (islabelchanged === true) {
                            labels.push(com_util.convertToStr($(tag).find('.vp-inner-popup-label').val(), labelastext));
                        }
                        if (content['type'] === 'cut' && isedgechanged === true) {
                            edges.push($(tag).find('.vp-inner-popup-left-edge').val());
                            if (idx === (rangeTableTags.length - 1)) {
                                edges.push($(tag).find('.vp-inner-popup-right-edge').val());
                            }
                        }
                    });
                    content['labels'] = labels;
                    content['edges'] = edges;
                    break;
                case FRAME_EDIT_TYPE.DATA_SHIFT:
                    content['periods'] = $(this.wrapSelector('.vp-inner-popup-periods')).val();
                    content['freq'] = $(this.wrapSelector('.vp-inner-popup-freq')).val();
                    let fillValue = $(this.wrapSelector('.vp-inner-popup-fillvalue')).val();
                    let fillValueAsText= $(this.wrapSelector('.vp-inner-popup-fillvalueastext')).prop('checked');
                    content['fill_value'] = '';
                    if (fillValue && fillValue !== '') {
                        content['fill_value'] = com_util.convertToStr(fillValue, fillValueAsText);
                    }
                    break;
                case FRAME_EDIT_TYPE.FILL_NA:
                    content['value'] = $(this.wrapSelector('.vp-inner-popup-value')).val();
                    content['valueastext'] = $(this.wrapSelector('.vp-inner-popup-valueastext')).prop('checked');
                    content['method'] = $(this.wrapSelector('.vp-inner-popup-method')).val();
                    content['limit'] = $(this.wrapSelector('.vp-inner-popup-limit')).val();
                    break;
                default:
                    break;
            }
            return content;
        }

        templateForDataView() {
            return this.renderInfoPage('');
        }

        renderDataView() {
            super.renderDataView();

            this.loadInfo();
            $(this.wrapSelector('.vp-popup-dataview-box')).css('height', '300px');
        }

        renderInfoPage = function(renderedText, isHtml = true) {
            var tag = new com_String();
            tag.appendFormatLine('<div class="{0} {1} vp-close-on-blur vp-scrollbar">', VP_FE_INFO_CONTENT
                                , 'rendered_html'); // 'rendered_html' style from jupyter output area
            if (isHtml) {
                tag.appendLine(renderedText);
            } else {
                tag.appendFormatLine('<pre>{0}</pre>', renderedText);
            }
            tag.appendLine('</div>');
            return tag.toString();
        }

        loadInfo() {
            var that = this;
    
            // get selected columns/indexes
            var selected = [];
            $(this.wrapSelector(`.${VP_FE_TABLE} th:not(.${VP_FE_TABLE_COLUMN_GROUP}).selected`)).each((idx, tag) => {
                var label = $(tag).text();
                var code = $(tag).data('code');
                var type = $(tag).data('type');
                selected.push({ label: label, code: code, type: type });
            });
            this.state.selected = selected;
    
            var code = new com_String();
            var locObj = new com_String();
            locObj.appendFormat("{0}", this.state.tempObj);
            if (this.state.selected.length > 0) {
                var rowCode = ':';
                var colCode = ':';
                if (this.state.axis == FRAME_AXIS.ROW) {
                    rowCode = '[' + this.state.selected.map(col=>col.code).join(',') + ']';
                }
                if (this.state.axis == FRAME_AXIS.COLUMN) {
                    colCode = '[' + this.state.selected.map(col=>col.code).join(',') + ']';
                }
                locObj.appendFormat(".loc[{0},{1}]", rowCode, colCode);
            }
            // code.append(".value_counts()");
            code.appendFormat('_vp_display_dataframe_info({0})', locObj.toString());
    
            // CHROME: TODO: 6: use com_Kernel.execute
            // Jupyter.notebook.kernel.execute(
            vpKernel.execute(code.toString()).then(function(resultObj) {
                let { msg } = resultObj;
                if (msg.content.data) {
                    var htmlText = String(msg.content.data["text/html"]);
                    var codeText = String(msg.content.data["text/plain"]);
                    if (htmlText != 'undefined') {
                        $(that.wrapSelector('.' + VP_FE_INFO_CONTENT)).replaceWith(function() {
                            return that.renderInfoPage(htmlText);
                        });
                    } else if (codeText != 'undefined') {
                        // plain text as code
                        $(that.wrapSelector('.' + VP_FE_INFO_CONTENT)).replaceWith(function() {
                            return that.renderInfoPage(codeText, false);
                        });
                    } else {
                        $(that.wrapSelector('.' + VP_FE_INFO_CONTENT)).replaceWith(function() {
                            return that.renderInfoPage('');
                        });
                    }
                } else {
                    var errorContent = '';
                    if (msg.content.ename) {
                        errorContent = com_util.templateForErrorBox(msg.content.ename, msg.content.evalue);
                    }
                    vpLog.display(VP_LOG_TYPE.ERROR, msg.content.ename, msg.content.evalue, msg.content);
                    $(that.wrapSelector('.' + VP_FE_INFO_CONTENT)).replaceWith(function() {
                        return that.renderInfoPage(errorContent);
                    });
                }
            }).catch(function(resultObj) {
                let { msg } = resultObj;
                var errorContent = '';
                if (msg.content.ename) {
                    errorContent = com_util.templateForErrorBox(msg.content.ename, msg.content.evalue);
                }
                vpLog.display(VP_LOG_TYPE.ERROR, msg.content.ename, msg.content.evalue, msg.content);
                $(that.wrapSelector('.' + VP_FE_INFO_CONTENT)).replaceWith(function() {
                    return that.renderInfoPage(errorContent);
                });
            })
        }

        getTypeCode(type, content={}) {
            var tempObj = this.state.tempObj;
            var orgObj = this.state.originObj;
            var type = parseInt(type);
    
            if (!orgObj || orgObj == '') {
                // object not selected
    
                return '';
            }
    
            var selectedName = this.state.selected.map(col=>col.code).join(',');
            var axis = this.state.axis;
            var subsetObjStr = tempObj;
            if (selectedName && selectedName !== '') {
                if (this.state.selected.length > 1) {
                    subsetObjStr += "[[" + selectedName + "]]";
                } else {
                    subsetObjStr += "[" + selectedName + "]";
                }
            }
    
            var code = new com_String();
            switch (type) {
                case FRAME_EDIT_TYPE.INIT:
                    code.appendFormat('{0} = {1}.copy()', tempObj, orgObj);
                    this.config.checkModules = ['pd'];
                    break;
                case FRAME_EDIT_TYPE.DROP:
                    code.appendFormat("{0}.drop([{1}], axis={2}, inplace=True)", tempObj, selectedName, axis);
                    break;
                case FRAME_EDIT_TYPE.RENAME:
                    var renameList = [];
                    Object.keys(content['list']).forEach((key, idx) => {
                        if (content['list'][key].value !== undefined && content['list'][key].value !== '') {
                            renameList.push(com_util.formatString("{0}: {1}", content['list'][key].label, com_util.convertToStr(content['list'][key].value, content['list'][key].istext)));
                        }
                    });
                    if (renameList.length > 0) {
                        code.appendFormat("{0}.rename({1}={{2}}", tempObj, axis==FRAME_AXIS.ROW?'index':'columns', renameList.join(', '));
                        if (content['level'] !== undefined) {
                            code.appendFormat(", level={0}", content['level']);
                        }
                        code.append(', inplace=True)')
                    }
                    break;
                case FRAME_EDIT_TYPE.DROP_NA:
                    var locObj = '';
                    if (axis == FRAME_AXIS.ROW) {
                        locObj = com_util.formatString('.loc[[{0}],:]', selectedName);
                    } else {
                        locObj = com_util.formatString('.loc[:,[{0}]]', selectedName);
                    }
                    code.appendFormat("{0}{1}.dropna(axis={2}, inplace=True)", tempObj, locObj, axis);
                    break;
                case FRAME_EDIT_TYPE.DROP_DUP:
                    if (axis == FRAME_AXIS.COLUMN) {
                        code.appendFormat("{0}.drop_duplicates(subset=[{1}], inplace=True)", tempObj, selectedName);
                    }
                    break;
                case FRAME_EDIT_TYPE.DROP_OUT:
                    if (axis == FRAME_AXIS.COLUMN) {
                        code.appendFormat("{0} = vp_drop_outlier({1}, {2})", tempObj, tempObj, selectedName);
                    }
                    break;
                case FRAME_EDIT_TYPE.LABEL_ENCODING:
                    if (axis == FRAME_AXIS.COLUMN) {
                        let encodedColName = this.state.selected.map(col=> { 
                            if (col.code !== col.label) {
                                return com_util.formatString("'{0}'", col.label + '_label');
                            }
                            return col.label + '_label' 
                        }).join(',');
                        code.appendFormat("{0}[{1}] = pd.Categorical({2}[{3}]).codes", tempObj, encodedColName, tempObj, selectedName);
                    }
                    break;
                case FRAME_EDIT_TYPE.ONE_HOT_ENCODING:
                    if (axis == FRAME_AXIS.COLUMN) {
                        code.appendFormat("{0} = pd.get_dummies(data={1}, columns=[{2}])", tempObj, tempObj, selectedName);
                    }
                    break;
                case FRAME_EDIT_TYPE.SET_IDX:
                    if (axis == FRAME_AXIS.COLUMN) {
                        code.appendFormat("{0}.set_index([{1}], inplace=True)", tempObj, selectedName);
                    }
                    break;
                case FRAME_EDIT_TYPE.RESET_IDX:
                    code.appendFormat("{0}.reset_index(inplace=True)", tempObj);
                    break;
                case FRAME_EDIT_TYPE.SORT_INDEX:
                    let selectedStr = '';
                    if (content.values.length > 1) {
                        selectedStr = "[" + content.values.join(',') + "]";
                    }
                    code.appendFormat("{0}.sort_index(ascending={1}", tempObj, content.ascending);
                    if (selectedStr !== '') {
                        code.appendFormat(', level=[{0}])', selectedStr);
                    }
                    code.append(', inplace=True)');
                    break;
                case FRAME_EDIT_TYPE.SORT_VALUES:
                    if (axis == FRAME_AXIS.COLUMN) {
                        let selectedStr = '';
                        if (content.values.length > 1) {
                            selectedStr = "[" + content.values.join(',') + "]";
                        } else {
                            selectedStr = content.values[0];
                        }
                        code.appendFormat("{0}.sort_values(by={1}, ascending={2}, inplace=True)", tempObj, selectedStr, content.ascending);
                    }
                    break;
                case FRAME_EDIT_TYPE.ADD_COL:
                    // if no name entered
                    if (content.name == '') {
                        return '';
                    }
                    var tab = content.addtype;
                    if (tab == 'variable') {
                        let values = [];
                        content['values'] && content['values'].forEach((val, idx) => {
                            if (idx > 0) {
                                values.push(content['opers'][idx - 1]);
                            }
                            values.push(val);
                        });
                        code.appendFormat("{0}[{1}] = {2}", tempObj, content.name, values.join(' '));
                    } else if (tab == 'apply') {
                        code.appendFormat("{0}[{1}] = {2}[{3}].apply({4})", tempObj, content.name, tempObj, content.column, content.apply);
                    }
                    break;
                case FRAME_EDIT_TYPE.ADD_ROW: 
                    // if no name entered
                    if (content.name == '') {
                        return '';
                    }
                    var tab = content.addtype;
                    let values = [];
                    content['values'] && content['values'].forEach((val, idx) => {
                        if (idx > 0) {
                            values.push(content['opers'][idx - 1]);
                        }
                        values.push(val);
                    });
                    code.appendFormat("{0}.loc[{1}] = {2}", tempObj, content.name, values.join(' '));
                    break;
                case FRAME_EDIT_TYPE.REPLACE:
                    // if no name entered
                    if (content.name == '') {
                        return '';
                    }
                    var name = com_util.convertToStr(content.name, content.nameastext);
                    name = selectedName;
                    var value = com_util.convertToStr(content.value, content.valueastext);
                    code.appendFormat("{0} = {1}", content.subset, value);
                    break;
                case FRAME_EDIT_TYPE.AS_TYPE:
                    var astypeStr = new com_String();
                    Object.keys(content).forEach((key, idx) => {
                        if (idx == 0) {
                            astypeStr.appendFormat("{0}: '{1}'", content[key].label, content[key].value);
                        } else {
                            astypeStr.appendFormat(", {0}: '{1}'", content[key].label, content[key].value);
                        }
                    });
                    code.appendFormat("{0} = {1}.astype({{2}})", tempObj, tempObj, astypeStr.toString());
                    break;
                case FRAME_EDIT_TYPE.DISCRETIZE:
                    let newColumn = com_util.convertToStr(content['input'], content['inputastext']);
                    let method = content['type'];
                    let bins = content['bins'];
                    if (method === 'cut') {
                        if (content['edges'] && content['edges'].length > 0) {
                            bins = "[" + content['edges'].join(',') + "]";
                        }
                    }

                    code.appendFormat("{0}[{1}] = pd.{2}({3}[{4}], {5}"
                        , tempObj, newColumn, method, tempObj, selectedName, bins);

                    if (method === 'cut' && content['isright'] === false) {
                        code.append(", right=False");
                    }
                    if (content['labels'] && content['labels'].length > 0) {
                        code.appendFormat(", labels=[{0}]", content['labels'].join(', '));
                    } else {
                        code.append(", labels=False");
                    }
                    code.append(')');
                    break;
                case FRAME_EDIT_TYPE.DATA_SHIFT:
                    code.appendFormat("{0} = {1}.shift({2}", subsetObjStr, subsetObjStr, content['periods']);
                    if (content['freq'] && content['freq'] !== '') {
                        code.appendFormat(", freq='{0}'", content['freq']);
                    }
                    if (content['fill_value'] && content['fill_value'] !== '') {
                        code.appendFormat(", fill_value={0}", content['fill_value']);
                    }
                    code.append(')');
                    break;
                case FRAME_EDIT_TYPE.FILL_NA:
                    code.appendFormat("{0} = {1}.fillna({2}", subsetObjStr, subsetObjStr, com_util.convertToStr(content['value'], content['valueastext']));
                    if (content['method'] && content['method'] !== '') {
                        code.appendFormat(", method='{0}'", content['method']);
                        if (content['limit'] && content['limit'] !== '') {
                            code.appendFormat(", limit={0}", content['limit']);
                        }
                    }
                    code.append(')');
                    break;
                case FRAME_EDIT_TYPE.SHOW:
                    break;
            }
    
            return code.toString();
        }

        loadCode(codeStr, more=false) {
            if (this.loading) {
                return;
            }
    
            var that = this;
            let { tempObj, lines, indexList } = this.state;
            var prevLines = 0;
            var scrollPos = -1;
            if (more) {
                prevLines = indexList.length;
                scrollPos = $(this.wrapSelector('.vp-fe-table')).scrollTop();
            }
    
            var code = new com_String();
            code.appendLine(codeStr);
            code.appendFormat("{0}.iloc[{1}:{2}].to_json(orient='{3}')", tempObj, prevLines, lines, 'split');
            
            this.loading = true;
            vpKernel.execute(code.toString()).then(function(resultObj) {
                let { result } = resultObj;
                try {
                    if (!result || result.length <= 0) {
                        return;
                    }
                    result = result.substr(1,result.length - 2).replaceAll('\\\\', '\\');
                    result = result.replaceAll('\'', "\\'");    // TEST: need test
                    // result = result.replaceAll('\\"', "\"");
                    var data = JSON.parse(result);
                    
                    vpKernel.getColumnList(tempObj).then(function(colResObj) {
                        try {
                            let columnResult = colResObj.result;
                            var columnInfo = JSON.parse(columnResult);
                            let { name:columnName='', level:columnLevel, list:columnList } = columnInfo;
                            // var columnList = data.columns;
                            var indexList = data.index;
                            var dataList = data.data;

                            columnList = columnList.map(col => { return { label: col.label, type: col.dtype, code: col.value } });
                            indexList = indexList.map(idx => { return { label: idx, code: idx } });
            
                            if (!more) {
                                // table
                                var table = new com_String();
                                // table.appendFormatLine('<table border="{0}" class="{1}">', 1, 'dataframe');
                                table.appendLine('<thead>');
                                if (columnLevel > 1) {
                                    for (let colLevIdx = 0; colLevIdx < columnLevel; colLevIdx++) {
                                        table.appendLine('<tr><th></th>');
                                        let colIdx = 0;
                                        let colSpan = 1;
                                        while (colIdx < columnList.length) {
                                            let col = columnList[colIdx];
                                            let colCode = col.code.slice(0, colLevIdx + 1).join(',');
                                            let nextCol = columnList[colIdx + 1];
                                            if (nextCol && nextCol.code.slice(0, colLevIdx + 1).join(',') === colCode) {
                                                colSpan++;
                                            } else {
                                                let colClass = '';
                                                let selected = ''; // set class if it's leaf node of columns on multi-level
                                                if (that.state.axis == FRAME_AXIS.COLUMN && that.state.selected.map(col=>col.code[colLevIdx]).includes(colCode)) {
                                                    selected = 'selected';
                                                }
                                                if ((columnLevel - 1) === colLevIdx) {
                                                    colClass = VP_FE_TABLE_COLUMN;
                                                } else {
                                                    colClass = VP_FE_TABLE_COLUMN_GROUP;
                                                }
                                                table.appendFormatLine('<th data-code="({0})" data-axis="{1}" data-type="{2}" data-parent="{3}" data-label="{4}" class="{5} {6}" colspan="{7}">{8}</th>'
                                                                , colCode, FRAME_AXIS.COLUMN, col.type, col.label[colLevIdx-1], col.label[colLevIdx], colClass, selected, colSpan, col.label[colLevIdx]);
                                                colSpan = 1;
                                            }
                                            colIdx++;
                                        }
    
                                        // add column
                                        // LAB: img to url
                                        // table.appendFormatLine('<th class="{0}"><img src="{1}"/></th>', VP_FE_ADD_COLUMN, com_Const.IMAGE_PATH + 'plus.svg');
                                        if (colLevIdx === 0) {
                                            table.appendFormatLine('<th class="{0}"><div class="{1}"></div></th>', VP_FE_ADD_COLUMN, 'vp-icon-plus');
                                        }
                        
                                        table.appendLine('</tr>');
                                    }
                                } else {
                                    table.appendLine('<tr><th></th>');
                                    columnList && columnList.forEach(col => {
                                        var colCode = col.code;
                                        var colClass = '';
                                        if (that.state.axis == FRAME_AXIS.COLUMN && that.state.selected.map(col=>col.code).includes(colCode)) {
                                            colClass = 'selected';
                                        }
                                        table.appendFormatLine('<th data-code="{0}" data-axis="{1}" data-type="{2}" data-label="{3}" class="{4} {5}">{6}</th>'
                                                                , colCode, FRAME_AXIS.COLUMN, col.type, col.label, VP_FE_TABLE_COLUMN, colClass, col.label);
                                    });
                                    // add column
                                    table.appendFormatLine('<th class="{0}"><div class="{1}"></div></th>', VP_FE_ADD_COLUMN, 'vp-icon-plus');
                    
                                    table.appendLine('</tr>');
                                }
                                table.appendLine('</thead>');
                                table.appendLine('<tbody>');
                
                                dataList && dataList.forEach((row, idx) => {
                                    table.appendLine('<tr>');
                                    var idxName = indexList[idx].label;
                                    var idxLabel = com_util.convertToStr(idxName, typeof idxName == 'string');
                                    var idxClass = '';
                                    if (that.state.axis == FRAME_AXIS.ROW && that.state.selected.includes(idxLabel)) {
                                        idxClass = 'selected';
                                    }
                                    table.appendFormatLine('<th data-code="{0}" data-axis="{1}" class="{2} {3}">{4}</th>', idxLabel, FRAME_AXIS.ROW, VP_FE_TABLE_ROW, idxClass, idxName);
                                    row.forEach((cell, colIdx) => {
                                        if (cell == null) {
                                            cell = 'NaN';
                                        }
                                        var cellType = columnList[colIdx].type;
                                        if (cellType.includes('datetime')) {
                                            cell = new Date(parseInt(cell)).toLocaleString();
                                        }
                                        table.appendFormatLine('<td>{0}</td>', cell);
                                    });
                                    // empty data
                                    // table.appendLine('<td></td>');
                                    table.appendLine('</tr>');
                                });
                                // add row
                                table.appendLine('<tr>');
                                // LAB: img to url
                                // table.appendFormatLine('<th class="{0}"><img src="{1}"/></th>', VP_FE_ADD_ROW, com_Const.IMAGE_PATH + 'plus.svg');
                                table.appendFormatLine('<th class="{0}"><div class="{1}"></div></th>', VP_FE_ADD_ROW, 'vp-icon-plus');
                                table.appendLine('</tr>');
                                table.appendLine('</tbody>');
                                $(that.wrapSelector('.' + VP_FE_TABLE)).replaceWith(function() {
                                    return that.renderTable(table.toString());
                                });
                            } else {
                                var table = new com_String();
                                dataList && dataList.forEach((row, idx) => {
                                    table.appendLine('<tr>');
                                    var idxName = indexList[idx].label;
                                    var idxLabel = com_util.convertToStr(idxName, typeof idxName == 'string');
                                    var idxClass = '';
                                    if (that.state.axis == FRAME_AXIS.ROW && that.state.selected.includes(idxLabel)) {
                                        idxClass = 'selected';
                                    }
                                    table.appendFormatLine('<th data-code="{0}" data-axis="{1}" class="{2} {3}">{4}</th>', idxLabel, FRAME_AXIS.ROW, VP_FE_TABLE_ROW, idxClass, idxName);
                                    row.forEach((cell, colIdx) => {
                                        if (cell == null) {
                                            cell = 'NaN';
                                        }
                                        var cellType = columnList[colIdx].type;
                                        if (cellType.includes('datetime')) {
                                            cell = new Date(parseInt(cell)).toLocaleString();
                                        }
                                        table.appendFormatLine('<td>{0}</td>', cell);
                                    });
                                    // empty data
                                    // table.appendLine('<td></td>');
                                    table.appendLine('</tr>');
                                });
                                // insert before last tr tag(add row button)
                                $(table.toString()).insertBefore($(that.wrapSelector('.' + VP_FE_TABLE + ' tbody tr:last')));
                            }
        
                            // save columnList & indexList as state
                            that.state.columnLevel = columnLevel;
                            that.state.columnList = columnList;
                            if (!more) {
                                that.state.indexList = indexList;
                            } else {
                                that.state.indexList = that.state.indexList.concat(indexList);
                            }
        
        
                            // load info
                            that.loadInfo();
                            // load toolbar
                            that.renderToolbar();
                            // add to stack
                            if (codeStr !== '') {
                                let newSteps = codeStr.split('\n');
                                that.state.steps = [
                                    ...that.state.steps,
                                    ...newSteps
                                ]
                                var replacedCode = codeStr.replaceAll(that.state.tempObj, that.state.returnObj);
                                that.setPreview(replacedCode);
                            }
                            
                            // if scrollPos is saved, go to the position
                            if (scrollPos >= 0) {
                                $(that.wrapSelector('.vp-fe-table')).scrollTop(scrollPos);
                            }
            
                            that.loading = false;
                        } catch (err1) {
                            vpLog.display(VP_LOG_TYPE.ERROR, err1);
                            that.loading = false;
                            throw err1;
                        }
                    });
                } catch (err) {
                    vpLog.display(VP_LOG_TYPE.ERROR, err);
                    that.loading = false;
                }
            }).catch(function(resultObj) {
                let { result, type, msg } = resultObj;
                vpLog.display(VP_LOG_TYPE.ERROR, result.ename + ': ' + result.evalue, msg, code.toString());
                if (that.isHidden() == false) {
                    // show alert modal only if this popup is visible
                    com_util.renderAlertModal(result.ename + ': ' + result.evalue);
                }
                that.loading = false;
            });
    
            return code.toString();
        }

        showMenu(left, top) {
            if (this.state.axis == 0) {
                // row
                $(this.wrapSelector(com_util.formatString('.{0}', VP_FE_MENU_BOX))).find('div[data-axis="col"]').hide();
                $(this.wrapSelector(com_util.formatString('.{0}', VP_FE_MENU_BOX))).find('div[data-axis="row"]').show();

                // change sub-box style
                $(this.wrapSelector(com_util.formatString('.{0}.vp-fe-sub-cleaning', VP_FE_MENU_SUB_BOX))).css({ 'top': '90px'});
            } else if (this.state.axis == 1) {
                // column
                $(this.wrapSelector(com_util.formatString('.{0}', VP_FE_MENU_BOX))).find('div[data-axis="row"]').hide();
                $(this.wrapSelector(com_util.formatString('.{0}', VP_FE_MENU_BOX))).find('div[data-axis="col"]').show();

                // change sub-box style
                $(this.wrapSelector(com_util.formatString('.{0}.vp-fe-sub-cleaning', VP_FE_MENU_SUB_BOX))).css({ 'top': '120px'});
            }
            $(this.wrapSelector(com_util.formatString('.{0}', VP_FE_MENU_BOX))).css({ top: top, left: left })
            $(this.wrapSelector(com_util.formatString('.{0}', VP_FE_MENU_BOX))).show();
        }

        hideMenu() {
            $(this.wrapSelector(com_util.formatString('.{0}', VP_FE_MENU_BOX))).hide();
        }

        hide() {
            super.hide();
            this.subsetEditor && this.subsetEditor.hide();
        }

        close() {
            super.close();
            this.subsetEditor && this.subsetEditor.close();
        }

        remove() {
            super.remove();
            this.subsetEditor && this.subsetEditor.remove();
        }

    }

    const VP_FE_BTN = 'vp-fe-btn';

    const VP_FE_TITLE = 'vp-fe-title';

    const VP_FE_MENU_BOX = 'vp-fe-menu-box';
    const VP_FE_MENU_SUB_BOX = 'vp-fe-menu-sub-box';
    const VP_FE_MENU_ITEM = 'vp-fe-menu-item';

    const VP_FE_POPUP_BOX = 'vp-fe-popup-box';
    const VP_FE_POPUP_BODY = 'vp-fe-popup-body';
    const VP_FE_POPUP_OK = 'vp-fe-popup-ok';

    const VP_FE_TABLE = 'vp-fe-table';
    const VP_FE_TABLE_COLUMN = 'vp-fe-table-column';
    const VP_FE_TABLE_COLUMN_GROUP = 'vp-fe-table-column-group';
    const VP_FE_TABLE_ROW = 'vp-fe-table-row';
    const VP_FE_ADD_COLUMN = 'vp-fe-add-column';
    const VP_FE_ADD_ROW = 'vp-fe-add-row';
    const VP_FE_TABLE_MORE = 'vp-fe-table-more';

    const VP_FE_INFO = 'vp-fe-info';
    const VP_FE_INFO_CONTENT = 'vp-fe-info-content';

    const VP_FE_PREVIEW_BOX = 'vp-fe-preview-box';
    const VP_FE_BUTTON_PREVIEW = 'vp-fe-btn-preview';
    const VP_FE_BUTTON_DATAVIEW = 'vp-fe-btn-dataview';

    // search rows count at once
    const TABLE_LINES = 10;

    const FRAME_EDIT_TYPE = {
        NONE: -1,
        INIT: 0,

        ADD_COL: 97,
        ADD_ROW: 98,
        DROP: 3,
        RENAME: 2,
        AS_TYPE: 10,
        REPLACE: 9,
        DISCRETIZE: 15,

        SET_IDX: 7,
        RESET_IDX: 8,
        DATA_SHIFT: 14,

        SORT_INDEX: 16,
        SORT_VALUES: 17,

        ONE_HOT_ENCODING: 6,
        LABEL_ENCODING: 12,

        FILL_NA: 13,
        DROP_NA: 4,
        DROP_OUT: 11, 
        DROP_DUP: 5,

        SHOW: 99
    }

    const FRAME_AXIS = {
        NONE: -1,
        ROW: 0,
        COLUMN: 1
    }

    const FRAME_SELECT_TYPE = {
        NONE: -1,  // no problem with every selection type
        SINGLE: 0, // only single select supported
        MULTI: 1   // more than 1 selection needed
    }

    return Frame;
});