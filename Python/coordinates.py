<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
    <meta name="theme-color" content="#000000">
    <link rel="apple-touch-icon" sizes="180x180" href="/favicons/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicons/favicon-16x16.png">
    <link rel="manifest" href="/favicons/manifest.json">
    <link rel="mask-icon" href="/favicons/safari-pinned-tab.svg" color="#5bbad5">
    <link rel="shortcut icon" href="/favicons/favicon.ico">
    <meta name="theme-color" content="#ffffff">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://s3.amazonaws.com/cmu-cs-academy.lib.prod/112-highlight-style.css">
    <title>Arcs and Arrows | CMU CS Academy</title>
    <link href="/static/css/main.400c8d77.chunk.css" rel="stylesheet">
    <style data-styled="" data-styled-version="4.4.1"></style>
    <style id="ace_editor.css">
        .ace_editor {
            position: relative;
            overflow: hidden;
            font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;
            direction: ltr;
            text-align: left;
        }
        
        .ace_scroller {
            position: absolute;
            overflow: hidden;
            top: 0;
            bottom: 0;
            background-color: inherit;
            -ms-user-select: none;
            -moz-user-select: none;
            -webkit-user-select: none;
            user-select: none;
            cursor: text;
        }
        
        .ace_content {
            position: absolute;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            min-width: 100%;
        }
        
        .ace_dragging .ace_scroller:before {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            content: '';
            background: rgba(250, 250, 250, 0.01);
            z-index: 1000;
        }
        
        .ace_dragging.ace_dark .ace_scroller:before {
            background: rgba(0, 0, 0, 0.01);
        }
        
        .ace_selecting,
        .ace_selecting * {
            cursor: text !important;
        }
        
        .ace_gutter {
            position: absolute;
            overflow: hidden;
            width: auto;
            top: 0;
            bottom: 0;
            left: 0;
            cursor: default;
            z-index: 4;
            -ms-user-select: none;
            -moz-user-select: none;
            -webkit-user-select: none;
            user-select: none;
        }
        
        .ace_gutter-active-line {
            position: absolute;
            left: 0;
            right: 0;
        }
        
        .ace_scroller.ace_scroll-left {
            box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;
        }
        
        .ace_gutter-cell {
            padding-left: 19px;
            padding-right: 6px;
            background-repeat: no-repeat;
        }
        
        .ace_gutter-cell.ace_error {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");
            background-repeat: no-repeat;
            background-position: 2px center;
        }
        
        .ace_gutter-cell.ace_warning {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");
            background-position: 2px center;
        }
        
        .ace_gutter-cell.ace_info {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");
            background-position: 2px center;
        }
        
        .ace_dark .ace_gutter-cell.ace_info {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");
        }
        
        .ace_scrollbar {
            position: absolute;
            right: 0;
            bottom: 0;
            z-index: 6;
        }
        
        .ace_scrollbar-inner {
            position: absolute;
            cursor: text;
            left: 0;
            top: 0;
        }
        
        .ace_scrollbar-v {
            overflow-x: hidden;
            overflow-y: scroll;
            top: 0;
        }
        
        .ace_scrollbar-h {
            overflow-x: scroll;
            overflow-y: hidden;
            left: 0;
        }
        
        .ace_print-margin {
            position: absolute;
            height: 100%;
        }
        
        .ace_text-input {
            position: absolute;
            z-index: 0;
            width: 0.5em;
            height: 1em;
            opacity: 0;
            background: transparent;
            -moz-appearance: none;
            appearance: none;
            border: none;
            resize: none;
            outline: none;
            overflow: hidden;
            font: inherit;
            padding: 0 1px;
            margin: 0 -1px;
            text-indent: -1em;
            -ms-user-select: text;
            -moz-user-select: text;
            -webkit-user-select: text;
            user-select: text;
            white-space: pre!important;
        }
        
        .ace_text-input.ace_composition {
            background: inherit;
            color: inherit;
            z-index: 1000;
            opacity: 1;
            text-indent: 0;
        }
        
        .ace_layer {
            z-index: 1;
            position: absolute;
            overflow: hidden;
            word-wrap: normal;
            white-space: pre;
            height: 100%;
            width: 100%;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            pointer-events: none;
        }
        
        .ace_gutter-layer {
            position: relative;
            width: auto;
            text-align: right;
            pointer-events: auto;
        }
        
        .ace_text-layer {
            font: inherit !important;
        }
        
        .ace_cjk {
            display: inline-block;
            text-align: center;
        }
        
        .ace_cursor-layer {
            z-index: 4;
        }
        
        .ace_cursor {
            z-index: 4;
            position: absolute;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            border-left: 2px solid;
            transform: translatez(0);
        }
        
        .ace_slim-cursors .ace_cursor {
            border-left-width: 1px;
        }
        
        .ace_overwrite-cursors .ace_cursor {
            border-left-width: 0;
            border-bottom: 1px solid;
        }
        
        .ace_hidden-cursors .ace_cursor {
            opacity: 0.2;
        }
        
        .ace_smooth-blinking .ace_cursor {
            -webkit-transition: opacity 0.18s;
            transition: opacity 0.18s;
        }
        
        .ace_editor.ace_multiselect .ace_cursor {
            border-left-width: 1px;
        }
        
        .ace_marker-layer .ace_step,
        .ace_marker-layer .ace_stack {
            position: absolute;
            z-index: 3;
        }
        
        .ace_marker-layer .ace_selection {
            position: absolute;
            z-index: 5;
        }
        
        .ace_marker-layer .ace_bracket {
            position: absolute;
            z-index: 6;
        }
        
        .ace_marker-layer .ace_active-line {
            position: absolute;
            z-index: 2;
        }
        
        .ace_marker-layer .ace_selected-word {
            position: absolute;
            z-index: 4;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
        }
        
        .ace_line .ace_fold {
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            display: inline-block;
            height: 11px;
            margin-top: -2px;
            vertical-align: middle;
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="), url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");
            background-repeat: no-repeat, repeat-x;
            background-position: center center, top left;
            color: transparent;
            border: 1px solid black;
            border-radius: 2px;
            cursor: pointer;
            pointer-events: auto;
        }
        
        .ace_dark .ace_fold {}
        
        .ace_fold:hover {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="), url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");
        }
        
        .ace_tooltip {
            background-color: #FFF;
            background-image: -webkit-linear-gradient(top, transparent, rgba(0, 0, 0, 0.1));
            background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));
            border: 1px solid gray;
            border-radius: 1px;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
            color: black;
            max-width: 100%;
            padding: 3px 4px;
            position: fixed;
            z-index: 999999;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            cursor: default;
            white-space: pre;
            word-wrap: break-word;
            line-height: normal;
            font-style: normal;
            font-weight: normal;
            letter-spacing: normal;
            pointer-events: none;
        }
        
        .ace_folding-enabled > .ace_gutter-cell {
            padding-right: 13px;
        }
        
        .ace_fold-widget {
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            margin: 0 -12px 0 1px;
            display: none;
            width: 11px;
            vertical-align: top;
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");
            background-repeat: no-repeat;
            background-position: center;
            border-radius: 3px;
            border: 1px solid transparent;
            cursor: pointer;
        }
        
        .ace_folding-enabled .ace_fold-widget {
            display: inline-block;
        }
        
        .ace_fold-widget.ace_end {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");
        }
        
        .ace_fold-widget.ace_closed {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");
        }
        
        .ace_fold-widget:hover {
            border: 1px solid rgba(0, 0, 0, 0.3);
            background-color: rgba(255, 255, 255, 0.2);
            box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);
        }
        
        .ace_fold-widget:active {
            border: 1px solid rgba(0, 0, 0, 0.4);
            background-color: rgba(0, 0, 0, 0.05);
            box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);
        }
        
        .ace_dark .ace_fold-widget {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");
        }
        
        .ace_dark .ace_fold-widget.ace_end {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");
        }
        
        .ace_dark .ace_fold-widget.ace_closed {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");
        }
        
        .ace_dark .ace_fold-widget:hover {
            box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);
            background-color: rgba(255, 255, 255, 0.1);
        }
        
        .ace_dark .ace_fold-widget:active {
            box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);
        }
        
        .ace_fold-widget.ace_invalid {
            background-color: #FFB4B4;
            border-color: #DE5555;
        }
        
        .ace_fade-fold-widgets .ace_fold-widget {
            -webkit-transition: opacity 0.4s ease 0.05s;
            transition: opacity 0.4s ease 0.05s;
            opacity: 0;
        }
        
        .ace_fade-fold-widgets:hover .ace_fold-widget {
            -webkit-transition: opacity 0.05s ease 0.05s;
            transition: opacity 0.05s ease 0.05s;
            opacity: 1;
        }
        
        .ace_underline {
            text-decoration: underline;
        }
        
        .ace_bold {
            font-weight: bold;
        }
        
        .ace_nobold .ace_bold {
            font-weight: normal;
        }
        
        .ace_italic {
            font-style: italic;
        }
        
        .ace_error-marker {
            background-color: rgba(255, 0, 0, 0.2);
            position: absolute;
            z-index: 9;
        }
        
        .ace_highlight-marker {
            background-color: rgba(255, 255, 0, 0.2);
            position: absolute;
            z-index: 8;
        }
        
        .ace_br1 {
            border-top-left-radius: 3px;
        }
        
        .ace_br2 {
            border-top-right-radius: 3px;
        }
        
        .ace_br3 {
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        
        .ace_br4 {
            border-bottom-right-radius: 3px;
        }
        
        .ace_br5 {
            border-top-left-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        .ace_br6 {
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        .ace_br7 {
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        .ace_br8 {
            border-bottom-left-radius: 3px;
        }
        
        .ace_br9 {
            border-top-left-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br10 {
            border-top-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br11 {
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br12 {
            border-bottom-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br13 {
            border-top-left-radius: 3px;
            border-bottom-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br14 {
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br15 {
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        /*# sourceURL=ace/css/ace_editor.css */
    </style>
    <style id="ace-tm">
        .ace-tm .ace_gutter {
            background: #f0f0f0;
            color: #333;
        }
        
        .ace-tm .ace_print-margin {
            width: 1px;
            background: #e8e8e8;
        }
        
        .ace-tm .ace_fold {
            background-color: #6B72E6;
        }
        
        .ace-tm {
            background-color: #FFFFFF;
            color: black;
        }
        
        .ace-tm .ace_cursor {
            color: black;
        }
        
        .ace-tm .ace_invisible {
            color: rgb(191, 191, 191);
        }
        
        .ace-tm .ace_storage,
        .ace-tm .ace_keyword {
            color: blue;
        }
        
        .ace-tm .ace_constant {
            color: rgb(197, 6, 11);
        }
        
        .ace-tm .ace_constant.ace_buildin {
            color: rgb(88, 72, 246);
        }
        
        .ace-tm .ace_constant.ace_language {
            color: rgb(88, 92, 246);
        }
        
        .ace-tm .ace_constant.ace_library {
            color: rgb(6, 150, 14);
        }
        
        .ace-tm .ace_invalid {
            background-color: rgba(255, 0, 0, 0.1);
            color: red;
        }
        
        .ace-tm .ace_support.ace_function {
            color: rgb(60, 76, 114);
        }
        
        .ace-tm .ace_support.ace_constant {
            color: rgb(6, 150, 14);
        }
        
        .ace-tm .ace_support.ace_type,
        .ace-tm .ace_support.ace_class {
            color: rgb(109, 121, 222);
        }
        
        .ace-tm .ace_keyword.ace_operator {
            color: rgb(104, 118, 135);
        }
        
        .ace-tm .ace_string {
            color: rgb(3, 106, 7);
        }
        
        .ace-tm .ace_comment {
            color: rgb(76, 136, 107);
        }
        
        .ace-tm .ace_comment.ace_doc {
            color: rgb(0, 102, 255);
        }
        
        .ace-tm .ace_comment.ace_doc.ace_tag {
            color: rgb(128, 159, 191);
        }
        
        .ace-tm .ace_constant.ace_numeric {
            color: rgb(0, 0, 205);
        }
        
        .ace-tm .ace_variable {
            color: rgb(49, 132, 149);
        }
        
        .ace-tm .ace_xml-pe {
            color: rgb(104, 104, 91);
        }
        
        .ace-tm .ace_entity.ace_name.ace_function {
            color: #0000A2;
        }
        
        .ace-tm .ace_heading {
            color: rgb(12, 7, 255);
        }
        
        .ace-tm .ace_list {
            color: rgb(185, 6, 144);
        }
        
        .ace-tm .ace_meta.ace_tag {
            color: rgb(0, 22, 142);
        }
        
        .ace-tm .ace_string.ace_regex {
            color: rgb(255, 0, 0)
        }
        
        .ace-tm .ace_marker-layer .ace_selection {
            background: rgb(181, 213, 255);
        }
        
        .ace-tm.ace_multiselect .ace_selection.ace_start {
            box-shadow: 0 0 3px 0px white;
        }
        
        .ace-tm .ace_marker-layer .ace_step {
            background: rgb(252, 255, 0);
        }
        
        .ace-tm .ace_marker-layer .ace_stack {
            background: rgb(164, 229, 101);
        }
        
        .ace-tm .ace_marker-layer .ace_bracket {
            margin: -1px 0 0 -1px;
            border: 1px solid rgb(192, 192, 192);
        }
        
        .ace-tm .ace_marker-layer .ace_active-line {
            background: rgba(0, 0, 0, 0.07);
        }
        
        .ace-tm .ace_gutter-active-line {
            background-color: #dcdcdc;
        }
        
        .ace-tm .ace_marker-layer .ace_selected-word {
            background: rgb(250, 250, 255);
            border: 1px solid rgb(200, 200, 250);
        }
        
        .ace-tm .ace_indent-guide {
            background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;
        }
        /*# sourceURL=ace/css/ace-tm */
    </style>
    <style>
        .error_widget_wrapper {
            background: inherit;
            color: inherit;
            border: none
        }
        
        .error_widget {
            border-top: solid 2px;
            border-bottom: solid 2px;
            margin: 5px 0;
            padding: 10px 40px;
            white-space: pre-wrap;
        }
        
        .error_widget.ace_error,
        .error_widget_arrow.ace_error {
            border-color: #ff5a5a
        }
        
        .error_widget.ace_warning,
        .error_widget_arrow.ace_warning {
            border-color: #F1D817
        }
        
        .error_widget.ace_info,
        .error_widget_arrow.ace_info {
            border-color: #5a5a5a
        }
        
        .error_widget.ace_ok,
        .error_widget_arrow.ace_ok {
            border-color: #5aaa5a
        }
        
        .error_widget_arrow {
            position: absolute;
            border: solid 5px;
            border-top-color: transparent!important;
            border-right-color: transparent!important;
            border-left-color: transparent!important;
            top: -5px;
        }
    </style>
    <style id="ace_searchbox">
        .ace_search {
            background-color: #ddd;
            border: 1px solid #cbcbcb;
            border-top: 0 none;
            max-width: 325px;
            overflow: hidden;
            margin: 0;
            padding: 4px;
            padding-right: 6px;
            padding-bottom: 0;
            position: absolute;
            top: 0px;
            z-index: 99;
            white-space: normal;
        }
        
        .ace_search.left {
            border-left: 0 none;
            border-radius: 0px 0px 5px 0px;
            left: 0;
        }
        
        .ace_search.right {
            border-radius: 0px 0px 0px 5px;
            border-right: 0 none;
            right: 0;
        }
        
        .ace_search_form,
        .ace_replace_form {
            border-radius: 3px;
            border: 1px solid #cbcbcb;
            float: left;
            margin-bottom: 4px;
            overflow: hidden;
        }
        
        .ace_search_form.ace_nomatch {
            outline: 1px solid red;
        }
        
        .ace_search_field {
            background-color: white;
            color: black;
            border-right: 1px solid #cbcbcb;
            border: 0 none;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            float: left;
            height: 22px;
            outline: 0;
            padding: 0 7px;
            width: 214px;
            margin: 0;
        }
        
        .ace_searchbtn,
        .ace_replacebtn {
            background: #fff;
            border: 0 none;
            border-left: 1px solid #dcdcdc;
            cursor: pointer;
            float: left;
            height: 22px;
            margin: 0;
            position: relative;
        }
        
        .ace_searchbtn:last-child,
        .ace_replacebtn:last-child {
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        .ace_searchbtn:disabled {
            background: none;
            cursor: default;
        }
        
        .ace_searchbtn {
            background-position: 50% 50%;
            background-repeat: no-repeat;
            width: 27px;
        }
        
        .ace_searchbtn.prev {
            background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAADFJREFUeNpiSU1NZUAC/6E0I0yACYskCpsJiySKIiY0SUZk40FyTEgCjGgKwTRAgAEAQJUIPCE+qfkAAAAASUVORK5CYII=);
        }
        
        .ace_searchbtn.next {
            background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAADRJREFUeNpiTE1NZQCC/0DMyIAKwGJMUAYDEo3M/s+EpvM/mkKwCQxYjIeLMaELoLMBAgwAU7UJObTKsvAAAAAASUVORK5CYII=);
        }
        
        .ace_searchbtn_close {
            background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAcCAYAAABRVo5BAAAAZ0lEQVR42u2SUQrAMAhDvazn8OjZBilCkYVVxiis8H4CT0VrAJb4WHT3C5xU2a2IQZXJjiQIRMdkEoJ5Q2yMqpfDIo+XY4k6h+YXOyKqTIj5REaxloNAd0xiKmAtsTHqW8sR2W5f7gCu5nWFUpVjZwAAAABJRU5ErkJggg==) no-repeat 50% 0;
            border-radius: 50%;
            border: 0 none;
            color: #656565;
            cursor: pointer;
            float: right;
            font: 16px/16px Arial;
            height: 14px;
            margin: 5px 1px 9px 5px;
            padding: 0;
            text-align: center;
            width: 14px;
        }
        
        .ace_searchbtn_close:hover {
            background-color: #656565;
            background-position: 50% 100%;
            color: white;
        }
        
        .ace_replacebtn.prev {
            width: 54px
        }
        
        .ace_replacebtn.next {
            width: 27px
        }
        
        .ace_button {
            margin-left: 2px;
            cursor: pointer;
            -webkit-user-select: none;
            -moz-user-select: none;
            -o-user-select: none;
            -ms-user-select: none;
            user-select: none;
            overflow: hidden;
            opacity: 0.7;
            border: 1px solid rgba(100, 100, 100, 0.23);
            padding: 1px;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            color: black;
        }
        
        .ace_button:hover {
            background-color: #eee;
            opacity: 1;
        }
        
        .ace_button:active {
            background-color: #ddd;
        }
        
        .ace_button.checked {
            border-color: #3399ff;
            opacity: 1;
        }
        
        .ace_search_options {
            margin-bottom: 3px;
            text-align: right;
            -webkit-user-select: none;
            -moz-user-select: none;
            -o-user-select: none;
            -ms-user-select: none;
            user-select: none;
        }
        /*# sourceURL=ace/css/ace_searchbox */
    </style>
    <script type="text/javascript" src="https://s3.amazonaws.com/assets.freshdesk.com/widget/html2canvas.js?ver=2"></script>
    <link rel="stylesheet" type="text/css" href="https://s3.amazonaws.com/assets.freshdesk.com/widget/freshwidget.css?ver=2">
    <style id="ace-xcode">
        .ace-xcode .ace_gutter {
            background: #e8e8e8;
            color: #333
        }
        
        .ace-xcode .ace_print-margin {
            width: 1px;
            background: #e8e8e8
        }
        
        .ace-xcode {
            background-color: #FFFFFF;
            color: #000000
        }
        
        .ace-xcode .ace_cursor {
            color: #000000
        }
        
        .ace-xcode .ace_marker-layer .ace_selection {
            background: #B5D5FF
        }
        
        .ace-xcode.ace_multiselect .ace_selection.ace_start {
            box-shadow: 0 0 3px 0px #FFFFFF;
        }
        
        .ace-xcode .ace_marker-layer .ace_step {
            background: rgb(198, 219, 174)
        }
        
        .ace-xcode .ace_marker-layer .ace_bracket {
            margin: -1px 0 0 -1px;
            border: 1px solid #BFBFBF
        }
        
        .ace-xcode .ace_marker-layer .ace_active-line {
            background: rgba(0, 0, 0, 0.071)
        }
        
        .ace-xcode .ace_gutter-active-line {
            background-color: rgba(0, 0, 0, 0.071)
        }
        
        .ace-xcode .ace_marker-layer .ace_selected-word {
            border: 1px solid #B5D5FF
        }
        
        .ace-xcode .ace_constant.ace_language,
        .ace-xcode .ace_keyword,
        .ace-xcode .ace_meta,
        .ace-xcode .ace_variable.ace_language {
            color: #C800A4
        }
        
        .ace-xcode .ace_invisible {
            color: #BFBFBF
        }
        
        .ace-xcode .ace_constant.ace_character,
        .ace-xcode .ace_constant.ace_other {
            color: #275A5E
        }
        
        .ace-xcode .ace_constant.ace_numeric {
            color: #3A00DC
        }
        
        .ace-xcode .ace_entity.ace_other.ace_attribute-name,
        .ace-xcode .ace_support.ace_constant,
        .ace-xcode .ace_support.ace_function {
            color: #450084
        }
        
        .ace-xcode .ace_fold {
            background-color: #C800A4;
            border-color: #000000
        }
        
        .ace-xcode .ace_entity.ace_name.ace_tag,
        .ace-xcode .ace_support.ace_class,
        .ace-xcode .ace_support.ace_type {
            color: #790EAD
        }
        
        .ace-xcode .ace_storage {
            color: #C900A4
        }
        
        .ace-xcode .ace_string {
            color: #DF0002
        }
        
        .ace-xcode .ace_comment {
            color: #008E00
        }
        
        .ace-xcode .ace_indent-guide {
            background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==) right repeat-y
        }
        /*# sourceURL=ace/css/ace-xcode */
    </style>
</head>

<body>
    <div class="freshwidget-container responsive" id="FreshWidget" data-html2canvas-ignore="true" style="display: none;">
        <div class="widget-ovelay" id="freshwidget-overlay">&nbsp;</div>
        <div class="freshwidget-dialog" id="freshwidget-dialog">
            <div id="freshwidget-close" class="widget-close"></div>
            <div class="mobile-widget-close" id="mobile-widget-close"></div>
            <div class="mobile-widget-arrow" id="mobile-widget-arrow"></div>
            <div class="frame-container"> </div>
            <iframe title="Feedback Form" id="freshwidget-frame" src="https://csacademy.freshdesk.com/loading.html?ver=2" frameborder="0" scrolling="auto" allowtransparency="true" style="height: 500px">
        </div>
    </div>
    </iframe>
    </div>
    </div>
    <div id="freshwidget-button" data-html2canvas-ignore="true" class="freshwidget-button fd-btn-left" style="display: none; top: 450px;"><a href="javascript:void(0)" class="freshwidget-theme" style="color: white; background-color: rgb(71, 159, 186); border-color: white;">Support</a></div>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root">
        <div id="app" style="font-size: 14px;">
            <nav class="navbar-nav">
                <ul class="navbar" role="navigation">
                    <div class="group">
                        <li class="navitem"><a class="active" aria-current="page" href="/notes/554">Notes</a></li>
                        <li class="navitem"><a href="/ide">Sandbox</a></li>
                        <li class="navitem"><a href="/docs">Docs</a></li>
                        <li class="navitem"><a href="/resource/colors">Colors</a></li>
                    </div>
                    <div class="group center">
                        <li class="navbar-center navbar-title">
                            <div class="navbar-back-button show-arrow" role="button" tabindex="0">Back to lessons</div>
                        </li>
                    </div>
                    <div class="group right">
                        <li class="settings-button-container">
                            <button></button>
                        </li>
                        <li>
                            <div class="dropdown btn-group">
                                <div class="avatar-toggle" bsrole="toggle" id="avatar-dropdown" bsclass="dropdown-toggle"><img class="avatar" alt="your avatar" src="https://s3.amazonaws.com/cmu-cs-academy.lib.prod/default_avatar.png"><span class="caret"></span></div>
                                <ul role="menu" class="avatar-dropdown-menu dropdown-menu dropdown-menu-right" aria-labelledby="avatar-dropdown">
                                    <li role="presentation" class="disabled"><a role="menuitem" tabindex="-1" href="#">Signed in as jrashid</a></li>
                                    <li role="presentation" class="disabled"><a role="menuitem" tabindex="-1" href="#">1 Points</a></li>
                                    <li role="presentation" class=""><a role="menuitem" tabindex="-1" href="#">Teacher Portal</a></li>
                                    <li role="presentation" class="classroom"><a role="menuitem" tabindex="-1" href="#">pre-req</a></li>
                                    <li role="presentation" class="classroom"><a role="menuitem" tabindex="-1" href="#">Rahnuma Public School Class VII</a></li>
                                    <li role="presentation" class="classroom"><a role="menuitem" tabindex="-1" href="#">Rahnuma Public School Training</a></li>
                                    <li role="presentation" class="classroom"><a role="menuitem" tabindex="-1" href="#">Summer Workshop</a></li>
                                    <li role="separator" class="divider"></li>
                                    <li role="presentation" class=""><a role="menuitem" tabindex="-1" href="#">Change Password</a></li>
                                    <li role="presentation" class=""><a role="menuitem" tabindex="-1" href="#">Settings</a></li>
                                    <li role="presentation" class=""><a role="menuitem" tabindex="-1" href="#">Logout</a></li>
                                </ul>
                            </div>
                        </li>
                    </div>
                </ul>
            </nav>
            <div class="notes-page-with-nav ">
                <ul class="scrollspy-nav">
                    <li class=""><a href="#" class="">Arcs and Arrows</a></li>
                    <li class=""><a href="#" class="">Arcs</a></li>
                    <li class="active"><a href="#" class="">Angles</a></li>
                    <li class=""><a href="#" class="">startAngle and sweepAngle</a></li>
                    <li class=""><a href="#" class="">Circular Arcs</a></li>
                    <li class=""><a href="#" class="">Arrows</a></li>
                    <div class="strength-earned">0 <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAsCAYAAAB2d9g5AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gcFFQ0rEVnanQAAAxBJREFUWMPtmMtPE1EUxs8dWqGlvAzEAgXa8m6rogYCupD4gETUplHQSEWjWAyibCAKLnBh2Lrqn+DGlS5woRutUWgHmFJBJCo+8NUnJZTC0HbGhQlB2g69ZerCeHadO51fzp3vfPecQSzLwt8MAv5y/PtAAdciwzJwj+qfejNPqXAemoQIaJKfRVrlBbwMZ+YnABcGABBiGfixNGfE3lLSbtLGs21JKAlOKtquYQFDbBDGHC8exgNsKNDl50kK8UQz7R4HX3ARG5aVnA3HFa3fsVVqsZs648nuTIkBpQjEeGURZAIw7nxlxIVVZu7+VC09iF+HUy4SlkNLeAWNBHCuvEsRV+Fb7KYBbKHItPJoQuEEroZooFzDd3CFckKp/xyXtdlcZqCZFazsWoqvcAqFEzjqMBlxhVKTWx/z/Wj9eUiHlqHb1MIGmNWYHyAmxJAsFEVdZ1mAquzapvOVNx6HmTflGAYcGACAn/GDn/Zz3vPaQw4BAArbUvLnsyH+zz8E+rJOFPYOlwM+mPSOHeMbeFimrdqVUxcumjHHSwgyQV5hhWnFcLq0fSKiSkn7cwufsGQiBTrU/UhACCOXxeziTDWfwNbyTiRNlUVvMQyqXjTtsaoAoUB0iTPip98eWTdrLWul9YMH8ho3r8PN4uPCW7g72s35hxxRLgxUG5FImLr1rs3m5n7NAkIAHZqbUWHYQKtzhDM7naINKdIr+elLPbQLvvpmo66rs/ZaG4ua+WuEJ51mYCBygunCDGjX9O5BiOAPSDlHnkTxf7is6kHp27bz1+rToRWY9lqPRlprLNCVabJr+J0tZjxUxFOkSFIKupJL73gfZiinuTncukRg2NmHhBusa8tAFliwuc0PNl7XV3QhqTif/3Hty8J78K56/rhWt+PQ7f25RxIzH1pdw2HWpa+4PpiwgXTCZWbXT0VX1X0xd2jYQC/tgjnfh7Xfp5QXkTyjPHEjt81pWXMXddY+skHeDFsNTuCkm7z/27oyoV3TU4MAJRYokyhbJYI0MGhuxWxdWI3w/+80fMQv6UICCCr8x+gAAAAASUVORK5CYII=" alt="strength icon"></div>
                </ul>
                <div class="notes-page-container" tabindex="-1">
                    <div class="notes-page-inner">
                        <h1 id="toc-main-title">Arcs and Arrows</h1>
                        <div>
                            <h2></h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Let's learn about <b>arcs</b> and <b>arrows</b>, two shapes that can be very helpful at times.
                                </p>
                            </div>
                        </div>
                        <div id="toc-5103cbc412090de9918662743710b4664f72774a">
                            <h2>Arcs</h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    An <b>arc</b> is a part of an oval. For example:
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-df062dc0c3530aad5f6aa908c38f34a403a5605a" class=" ace_editor ace-xcode" style="width: 100%; height: 103.4px; font-size: 14px; font-family: Inconsolata;">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 44px; top: 72px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 115.2px; width: 40px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">6</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 72px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 40px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 372px; height: 115.2px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:72.00000286102295px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arcs Demo #1'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'A navy arc on a gold oval'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">400</span>, <span class="ace_constant ace_numeric">150</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">400</span>, <span class="ace_constant ace_numeric">150</span>, <span class="ace_constant ace_numeric">0</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 72px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 86.4px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 40px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 662px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Run the code and see that the navy arc covers a part of the gold oval. Let's take a closer look. First, here is how we drew the oval:
                                </p><pre><code class="hljs javascript">  Oval(<span class="hljs-number">200</span>, <span class="hljs-number">200</span>, <span class="hljs-number">400</span>, <span class="hljs-number">150</span>, fill=<span class="hljs-string">'gold'</span>)</code></pre> This draws a gold oval inside the rectangle centered at (200, 200) with a width of 400 and a height of 150.
                                <p></p>

                                <p>
                                    Now, let's look at the arc:
                                </p><pre><code class="hljs javascript">  Arc(<span class="hljs-number">200</span>, <span class="hljs-number">200</span>, <span class="hljs-number">400</span>, <span class="hljs-number">150</span>, <span class="hljs-number">0</span>, <span class="hljs-number">90</span>, fill=<span class="hljs-string">'navy'</span>)</code></pre> Notice that the first 4 values -- <code>200, 200, 400, 150</code> -- are the same as the oval's. This is because an arc is part of an oval, so we first specify that oval. So those values are the <code>centerX</code>, <code>centerY</code> , <code>width</code>, and <code>height</code> of the oval. The two additional values -- <code>0, 90</code> -- specify the <b>startAngle</b> and the <b>sweepAngle</b> of the arc. As we will next explore in more detail, these two values control how much of the oval is included in the arc.
                                <p></p>
                            </div>
                        </div>
                        <div id="toc-ff8084f15b2e36de1a91a87a056e597bc99716d5">
                            <h2>Angles</h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Here are the facts you need to know about angles in this course:
                                </p>
                                <ul>
                                    <li>Angles are measured in degrees.</li>
                                    <li>0 degrees heads straight up.</li>
                                    <li>Angles increase clockwise. Thus, for example, 90 degrees heads to the right.</li>
                                </ul>
                                This image may help:
                                <div width="200" class="cmu-cs-academy-img" img-src="angles.png" img-alt="counterclockwise unit circle with 0 degrees on top"><img src="https://s3.amazonaws.com/cmu-cs-academy.content.public.v2-prod/b4f833a32220a69e4198ea8936cce30a%3A%3Aangles.png" alt="counterclockwise unit circle with 0 degrees on top" width="200" class="img"></div>
                                <p></p>
                            </div>
                        </div>
                        <div class="notes-checkpoint">
                            <h3>Checkpoint 1<span><div class="status-icon complete"></div><button class="redo">Redo checkpoint</button></span></h3></div>
                        <div id="toc-8602ad4c3c2b3e46fa1e17865c46f7e2e6304d6b">
                            <h2>startAngle and sweepAngle</h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    The <code>startAngle</code> and <code>sweepAngle</code> work together to specify which part of the oval is in an arc. If you were drawing this by hand, the <code>startAngle</code> is where you should put your pen down on the paper to start drawing, and the <code>sweepAngle</code> is
                                    <b>how far</b> you should draw.
                                </p>

                                <p>
                                    Some examples would help. To start, let's look at different values of <code>startAngle</code> while keeping the <code>sweepAngle</code> fixed at 90 degrees (which is one-quarter of the oval):
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-a973e03661817862c39e938fa854597f0de338c2" style="width: 100%; height: 305px; font-size: 14px; font-family: Inconsolata;" class=" ace_editor ace-xcode">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 51px; top: 273.6px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 316.8px; width: 47px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">6</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">7</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">8</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">9</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">10</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">11</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">12</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">13</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">14</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">15</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">16</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">17</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">18</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">19</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">20</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 273.6px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 47px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 386px; height: 316.8px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:273.6000108718872px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arcs Demo #2'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Different startAngle values'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'The sweepAngle is always 90'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">65</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'startAngle = 0'</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">110</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">0</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'startAngle = 45'</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">110</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'startAngle = 90'</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">260</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'startAngle = 135'</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">260</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">135</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 273.6px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 288px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 47px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 652px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Run the code, and look carefully at the code and what is drawn. Be sure to understand how changing the <code>startAngle</code> affects the arc that is drawn.
                                </p>
                            </div>
                        </div>
                        <div class="notes-checkpoint">
                            <h3>Checkpoint 2<span><div class="status-icon complete"></div><button class="redo">Redo checkpoint</button></span></h3></div>
                        <div>
                            <h2></h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Here is another example that keeps the <code>startAngle</code> always at 90 degrees (to the right), and changes the <code>sweepAngle</code>:
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-bb01810755fd12a62ce344871fca232ee70090e1" style="width: 100%; height: 305px; font-size: 14px; font-family: Inconsolata;" class=" ace_editor ace-xcode">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 51px; top: 273.6px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 316.8px; width: 47px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">6</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">7</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">8</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">9</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">10</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">11</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">12</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">13</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">14</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">15</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">16</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">17</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">18</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">19</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">20</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 273.6px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 47px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 386px; height: 316.8px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:273.6000108718872px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arcs Demo #3'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Different sweepAngle values'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'The startAngle is always 90'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">65</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'sweepAngle = 45'</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">110</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'sweepAngle = 90'</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">110</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'sweepAngle = 135'</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">260</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_constant ace_numeric">135</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'sweepAngle = 180'</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">260</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_constant ace_numeric">180</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 273.6px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 288px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 47px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 652px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Run the code, and focus on how changing the <code>sweepAngle</code> affects the arc.
                                </p>
                            </div>
                        </div>
                        <div id="toc-3db6a4d4c8167c40e7f386e6df6fa5a9a630e85d">
                            <h2>Circular Arcs</h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Since an arc is part of an oval, and a circle is a kind of oval, an arc can be part of a circle. In fact, this is the most common use of arcs. To make an arc that is part of a circle, we set both its <code>width</code> and its <code>height</code> to the <b>diameter</b> of the circle, which is <b>twice</b> its <code>radius</code>. For example:
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-e71c5a7ec7424bde0fc91e8f4fa43f9fd94ebbb3" style="width: 100%; height: 103.4px; font-size: 14px; font-family: Inconsolata;" class=" ace_editor ace-xcode">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 44px; top: 72px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 115.2px; width: 40px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">6</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 72px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 40px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 386px; height: 115.2px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:72.00000286102295px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arcs Demo #4'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'A navy arc on a gold circle'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Circle</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">125</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">250</span>, <span class="ace_constant ace_numeric">250</span>, <span class="ace_constant ace_numeric">0</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 72px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 86.4px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 40px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 662px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Run the code and see how the arc covers part of the circle. Look closely and see that the <code>radius</code> of the circle is 125, and the <code>width</code> and <code>height</code> of the arc are both 250.
                                </p>

                                <p>
                                    To be clear, here is the same example without the circle:
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-dbf815e6dcc6dbe97c542f9a2b286fcec245d73d" style="width: 100%; height: 89px; font-size: 14px; font-family: Inconsolata;" class=" ace_editor ace-xcode">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 44px; top: 57.6px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 100.8px; width: 40px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 57.6px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 40px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 421px; height: 100.8px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:57.60000228881836px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arcs Demo #5'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'A navy arc by itself (no circle)'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">250</span>, <span class="ace_constant ace_numeric">250</span>, <span class="ace_constant ace_numeric">0</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 57.6px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 72px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 40px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 662px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                        </div>
                        <div class="notes-checkpoint">
                            <h3>Checkpoint 3<span><div class="status-icon complete"></div><button class="redo">Redo checkpoint</button></span></h3></div>
                        <div id="toc-0cf604cb001bdc6112fda3affb0c7674d1c4481b">
                            <h2>Arrows</h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    An <b>arrow</b> is simply a line with a triangular arrow head at one or both ends. We do not actually have an arrow shape. Instead, we use a line, and we set the <code>arrowStart</code> property to <code>True</code> to draw an arrow head at the start of the line. Similarly, we set
                                    <code>arrowEnd</code> to <code>True</code> to draw an arrow head at the end of the line. For example:
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-61aedb44ca96e5a6c00a19164abddb729277e2cc" style="width: 100%; height: 218.6px; font-size: 14px; font-family: Inconsolata;" class=" ace_editor ace-xcode">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 51px; top: 187.2px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 230.4px; width: 47px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">6</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">7</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">8</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">9</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">10</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">11</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">12</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">13</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">14</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 187.2px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 47px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 519px; height: 230.4px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:187.20000743865967px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arrows Demo'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Line with no arrows'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">85</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Line</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">105</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">105</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Line with a start arrow'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">155</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Line</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_identifier">arrowStart</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Line with an end arrow'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">225</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Line</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">245</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">245</span>, <span class="ace_identifier">arrowEnd</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Line with both a start arrow and an end arrow'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">295</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Line</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">315</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">315</span>, <span class="ace_identifier">arrowStart</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span>, <span class="ace_identifier">arrowEnd</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 187.2px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 201.6px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 47px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 746px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Run the code and see how the different lines have different arrow heads, depending on their values for <code>arrowStart</code> and <code>arrowEnd</code>.
                                </p>
                            </div>
                        </div>
                        <div class="notes-checkpoint">
                            <h3>Checkpoint 4<span><div class="status-icon complete"></div><button class="redo">Redo checkpoint</button></span></h3></div>
                        <button class="button flat small teal continue">Back to Lessons</button>
                    </div>
                </div>
                <div></div>
            </div>
            <div id="settings"></div>
            <div class="toaster-container"></div>
            <div id="support-popup"></div>
        </div>
    </div>
    <div id="application-target"></div>
    <div id="brython-target"></div>
    <script>
        var _rollbarConfig = {
            accessToken: "ce5718b091db44c2b31b4ff4d410d686",
            captureUncaught: !0,
            enabled: -1 === "ce5718b091db44c2b31b4ff4d410d686".indexOf("%"),
            checkIgnore: function(r, e, o) {
                return !!(o && o.body && o.body.message && "Error executing solution code" === o.body.message.body && o.request && o.request.url && 0 < o.request.url.indexOf("/sharing/")) || !!(r && o && o.body && o.body.trace && o.body.trace.exception && "SyntaxError" === o.body.trace.exception.class)
            },
            ignoredMessages: [],
            payload: {
                client: {
                    javascript: {
                        source_map_enabled: !0,
                        code_version: "1",
                        guess_uncaught_frames: !0
                    }
                },
                environment: "production"
            }
        };
        ! function(o) {
            function n(r) {
                if (t[r]) return t[r].exports;
                var e = t[r] = {
                    exports: {},
                    id: r,
                    loaded: !1
                };
                return o[r].call(e.exports, e, e.exports, n), e.loaded = !0, e.exports
            }
            var t = {};
            n.m = o, n.c = t, n.p = "", n(0)
        }([function(r, e, o) {
            "use strict";
            var n = o(1),
                t = o(4);
            (_rollbarConfig = _rollbarConfig || {}).rollbarJsUrl = _rollbarConfig.rollbarJsUrl || "https://cdnjs.cloudflare.com/ajax/libs/rollbar.js/2.4.2/rollbar.min.js", _rollbarConfig.async = void 0 === _rollbarConfig.async || _rollbarConfig.async;
            var a = n.setupShim(window, _rollbarConfig),
                l = t(_rollbarConfig);
            window.rollbar = n.Rollbar, a.loadFull(window, document, !_rollbarConfig.async, _rollbarConfig, l)
        }, function(r, e, o) {
            "use strict";

            function c(r) {
                return function() {
                    try {
                        return r.apply(this, arguments)
                    } catch (r) {
                        try {
                            console.error("[Rollbar]: Internal error", r)
                        } catch (r) {}
                    }
                }
            }

            function n(r, e) {
                this.options = r, this._rollbarOldOnError = null;
                var o = i++;
                this.shimId = function() {
                    return o
                }, "undefined" != typeof window && window._rollbarShims && (window._rollbarShims[o] = {
                    handler: e,
                    messages: []
                })
            }

            function t(o) {
                return c(function() {
                    var r = Array.prototype.slice.call(arguments, 0),
                        e = {
                            shim: this,
                            method: o,
                            args: r,
                            ts: new Date
                        };
                    window._rollbarShims[this.shimId()].messages.push(e)
                })
            }
            var a, l = o(2),
                i = 0,
                s = o(3),
                d = function(r, e) {
                    return new n(r, e)
                };
            a = s.curry ? s.curry(d) : s.bind(null, d), n.prototype.loadFull = function(l, r, e, o, i) {
                var n = !1,
                    t = r.createElement("script"),
                    a = r.getElementsByTagName("script")[0],
                    s = a.parentNode;
                t.crossOrigin = "", t.src = o.rollbarJsUrl, e || (t.async = !0), t.onload = t.onreadystatechange = c(function() {
                    if (!(n || this.readyState && "loaded" !== this.readyState && "complete" !== this.readyState)) {
                        t.onload = t.onreadystatechange = null;
                        try {
                            s.removeChild(t)
                        } catch (r) {}
                        n = !0,
                            function() {
                                var r;
                                if (void 0 === l._rollbarDidLoad) {
                                    r = new Error("rollbar.js did not load");
                                    for (var e, o, n, t, a = 0; e = l._rollbarShims[a++];)
                                        for (e = e.messages || []; o = e.shift();)
                                            for (n = o.args || [], a = 0; a < n.length; ++a)
                                                if ("function" == typeof(t = n[a])) {
                                                    t(r);
                                                    break
                                                }
                                }
                                "function" == typeof i && i(r)
                            }()
                    }
                }), s.insertBefore(t, a)
            }, n.prototype.wrap = function(o, r, n) {
                try {
                    var t;
                    if (t = "function" == typeof r ? r : function() {
                            return r || {}
                        }, "function" != typeof o) return o;
                    if (o._isWrap) return o;
                    if (!o._rollbar_wrapped && (o._rollbar_wrapped = function() {
                            n && "function" == typeof n && n.apply(this, arguments);
                            try {
                                return o.apply(this, arguments)
                            } catch (r) {
                                var e = r;
                                throw e && ("string" == typeof e && (e = new String(e)), e._rollbarContext = t() || {}, e._rollbarContext._wrappedSource = o.toString(), window._rollbarWrappedError = e), e
                            }
                        }, o._rollbar_wrapped._isWrap = !0, o.hasOwnProperty))
                        for (var e in o) o.hasOwnProperty(e) && (o._rollbar_wrapped[e] = o[e]);
                    return o._rollbar_wrapped
                } catch (r) {
                    return o
                }
            };
            for (var p = "log,debug,info,warn,warning,error,critical,global,configure,handleUncaughtException,handleUnhandledRejection,captureEvent,captureDomContentLoaded,captureLoad".split(","), u = 0; u < p.length; ++u) n.prototype[p[u]] = t(p[u]);
            r.exports = {
                setupShim: function(e, o) {
                    if (e) {
                        var n = o.globalAlias || "Rollbar";
                        if ("object" == typeof e[n]) return e[n];
                        e._rollbarShims = {}, e._rollbarWrappedError = null;
                        var t = new a(o);
                        return c(function() {
                            o.captureUncaught && (t._rollbarOldOnError = e.onerror, l.captureUncaughtExceptions(e, t, !0), l.wrapGlobals(e, t, !0)), o.captureUnhandledRejections && l.captureUnhandledRejections(e, t, !0);
                            var r = o.autoInstrument;
                            return !1 !== o.enabled && (void 0 === r || !0 === r || "object" == typeof r && r.network) && e.addEventListener && (e.addEventListener("load", t.captureLoad.bind(t)), e.addEventListener("DOMContentLoaded", t.captureDomContentLoaded.bind(t))), e[n] = t
                        })()
                    }
                },
                Rollbar: a
            }
        }, function(r, e) {
            "use strict";

            function l(n, r, e) {
                if (r.hasOwnProperty && r.hasOwnProperty("addEventListener")) {
                    for (var t = r.addEventListener; t._rollbarOldAdd && t.belongsToShim;) t = t._rollbarOldAdd;
                    var o = function(r, e, o) {
                        t.call(this, r, n.wrap(e), o)
                    };
                    o._rollbarOldAdd = t, o.belongsToShim = e, r.addEventListener = o;
                    for (var a = r.removeEventListener; a._rollbarOldRemove && a.belongsToShim;) a = a._rollbarOldRemove;
                    var l = function(r, e, o) {
                        a.call(this, r, e && e._rollbar_wrapped || e, o)
                    };
                    l._rollbarOldRemove = a, l.belongsToShim = e, r.removeEventListener = l
                }
            }
            r.exports = {
                captureUncaughtExceptions: function(a, l, r) {
                    if (a) {
                        var i;
                        "function" == typeof l._rollbarOldOnError ? i = l._rollbarOldOnError : a.onerror && !a.onerror.belongsToShim && (i = a.onerror, l._rollbarOldOnError = i);
                        var e = function() {
                            var r, e, o, n, t = Array.prototype.slice.call(arguments, 0);
                            e = l, o = i, n = t, (r = a)._rollbarWrappedError && (n[4] || (n[4] = r._rollbarWrappedError), n[5] || (n[5] = r._rollbarWrappedError._rollbarContext), r._rollbarWrappedError = null), e.handleUncaughtException.apply(e, n), o && o.apply(r, n)
                        };
                        e.belongsToShim = r, a.onerror = e
                    }
                },
                captureUnhandledRejections: function(r, t, e) {
                    if (r) {
                        "function" == typeof r._rollbarURH && r._rollbarURH.belongsToShim && r.removeEventListener("unhandledrejection", r._rollbarURH);
                        var o = function(r) {
                            var e, o, n;
                            try {
                                e = r.reason
                            } catch (r) {
                                e = void 0
                            }
                            try {
                                o = r.promise
                            } catch (r) {
                                o = "[unhandledrejection] error getting `promise` from event"
                            }
                            try {
                                n = r.detail, !e && n && (e = n.reason, o = n.promise)
                            } catch (r) {
                                n = "[unhandledrejection] error getting `detail` from event"
                            }
                            e || (e = "[unhandledrejection] error getting `reason` from event"), t && t.handleUnhandledRejection && t.handleUnhandledRejection(e, o)
                        };
                        o.belongsToShim = e, r._rollbarURH = o, r.addEventListener("unhandledrejection", o)
                    }
                },
                wrapGlobals: function(r, e, o) {
                    if (r) {
                        var n, t, a = "EventTarget,Window,Node,ApplicationCache,AudioTrackList,ChannelMergerNode,CryptoOperation,EventSource,FileReader,HTMLUnknownElement,IDBDatabase,IDBRequest,IDBTransaction,KeyOperation,MediaController,MessagePort,ModalWindow,Notification,SVGElementInstance,Screen,TextTrack,TextTrackCue,TextTrackList,WebSocket,WebSocketWorker,Worker,XMLHttpRequest,XMLHttpRequestEventTarget,XMLHttpRequestUpload".split(",");
                        for (n = 0; n < a.length; ++n) r[t = a[n]] && r[t].prototype && l(e, r[t].prototype, o)
                    }
                }
            }
        }, function(r, e) {
            "use strict";

            function o(r, e) {
                this.impl = r(e, this), this.options = e,
                    function(r) {
                        for (var e = function(e) {
                                return function() {
                                    var r = Array.prototype.slice.call(arguments, 0);
                                    if (this.impl[e]) return this.impl[e].apply(this.impl, r)
                                }
                            }, o = "log,debug,info,warn,warning,error,critical,global,configure,handleUncaughtException,handleUnhandledRejection,_createItem,wrap,loadFull,shimId,captureEvent,captureDomContentLoaded,captureLoad".split(","), n = 0; n < o.length; n++) r[o[n]] = e(o[n])
                    }(o.prototype)
            }
            o.prototype._swapAndProcessMessages = function(r, e) {
                this.impl = r(this.options);
                for (var o, n, t; o = e.shift();) n = o.method, t = o.args, this[n] && "function" == typeof this[n] && ("captureDomContentLoaded" === n || "captureLoad" === n ? this[n].apply(this, [t[0], o.ts]) : this[n].apply(this, t));
                return this
            }, r.exports = o
        }, function(r, e) {
            "use strict";
            r.exports = function(i) {
                return function(r) {
                    if (!r && !window._rollbarInitialized) {
                        for (var e, o, n = (i = i || {}).globalAlias || "Rollbar", t = window.rollbar, a = function(r) {
                                return new t(r)
                            }, l = 0; e = window._rollbarShims[l++];) o || (o = e.handler), e.handler._swapAndProcessMessages(a, e.messages);
                        window[n] = o, window._rollbarInitialized = !0
                    }
                }
            }
        }])
    </script>
    <script>
        ! function(l) {
            function e(e) {
                for (var r, t, n = e[0], o = e[1], u = e[2], f = 0, i = []; f < n.length; f++) t = n[f], p[t] && i.push(p[t][0]), p[t] = 0;
                for (r in o) Object.prototype.hasOwnProperty.call(o, r) && (l[r] = o[r]);
                for (s && s(e); i.length;) i.shift()();
                return c.push.apply(c, u || []), a()
            }

            function a() {
                for (var e, r = 0; r < c.length; r++) {
                    for (var t = c[r], n = !0, o = 1; o < t.length; o++) {
                        var u = t[o];
                        0 !== p[u] && (n = !1)
                    }
                    n && (c.splice(r--, 1), e = f(f.s = t[0]))
                }
                return e
            }
            var t = {},
                p = {
                    1: 0
                },
                c = [];

            function f(e) {
                if (t[e]) return t[e].exports;
                var r = t[e] = {
                    i: e,
                    l: !1,
                    exports: {}
                };
                return l[e].call(r.exports, r, r.exports, f), r.l = !0, r.exports
            }
            f.m = l, f.c = t, f.d = function(e, r, t) {
                f.o(e, r) || Object.defineProperty(e, r, {
                    enumerable: !0,
                    get: t
                })
            }, f.r = function(e) {
                "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                    value: "Module"
                }), Object.defineProperty(e, "__esModule", {
                    value: !0
                })
            }, f.t = function(r, e) {
                if (1 & e && (r = f(r)), 8 & e) return r;
                if (4 & e && "object" == typeof r && r && r.__esModule) return r;
                var t = Object.create(null);
                if (f.r(t), Object.defineProperty(t, "default", {
                        enumerable: !0,
                        value: r
                    }), 2 & e && "string" != typeof r)
                    for (var n in r) f.d(t, n, function(e) {
                        return r[e]
                    }.bind(null, n));
                return t
            }, f.n = function(e) {
                var r = e && e.__esModule ? function() {
                    return e.default
                } : function() {
                    return e
                };
                return f.d(r, "a", r), r
            }, f.o = function(e, r) {
                return Object.prototype.hasOwnProperty.call(e, r)
            }, f.p = "/";
            var r = window.webpackJsonp = window.webpackJsonp || [],
                n = r.push.bind(r);
            r.push = e, r = r.slice();
            for (var o = 0; o < r.length; o++) e(r[o]);
            var s = n;
            a()
        }([])
    </script>
    <script src="/static/js/2.064fcb15.chunk.js"></script>
    <script src="/static/js/main.d6ec4a6f.chunk.js"></script>
    <script type="text/javascript" src="https://s3.amazonaws.com/assets.freshdesk.com/widget/freshwidget.js"></script>
    <script src="/static/js/cmu-graphics.75de2005.js"></script>
</body>

</html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
    <meta name="theme-color" content="#000000">
    <link rel="apple-touch-icon" sizes="180x180" href="/favicons/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicons/favicon-16x16.png">
    <link rel="manifest" href="/favicons/manifest.json">
    <link rel="mask-icon" href="/favicons/safari-pinned-tab.svg" color="#5bbad5">
    <link rel="shortcut icon" href="/favicons/favicon.ico">
    <meta name="theme-color" content="#ffffff">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://s3.amazonaws.com/cmu-cs-academy.lib.prod/112-highlight-style.css">
    <title>Arcs and Arrows | CMU CS Academy</title>
    <link href="/static/css/main.400c8d77.chunk.css" rel="stylesheet">
    <style data-styled="" data-styled-version="4.4.1"></style>
    <style id="ace_editor.css">
        .ace_editor {
            position: relative;
            overflow: hidden;
            font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;
            direction: ltr;
            text-align: left;
        }
        
        .ace_scroller {
            position: absolute;
            overflow: hidden;
            top: 0;
            bottom: 0;
            background-color: inherit;
            -ms-user-select: none;
            -moz-user-select: none;
            -webkit-user-select: none;
            user-select: none;
            cursor: text;
        }
        
        .ace_content {
            position: absolute;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            min-width: 100%;
        }
        
        .ace_dragging .ace_scroller:before {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            content: '';
            background: rgba(250, 250, 250, 0.01);
            z-index: 1000;
        }
        
        .ace_dragging.ace_dark .ace_scroller:before {
            background: rgba(0, 0, 0, 0.01);
        }
        
        .ace_selecting,
        .ace_selecting * {
            cursor: text !important;
        }
        
        .ace_gutter {
            position: absolute;
            overflow: hidden;
            width: auto;
            top: 0;
            bottom: 0;
            left: 0;
            cursor: default;
            z-index: 4;
            -ms-user-select: none;
            -moz-user-select: none;
            -webkit-user-select: none;
            user-select: none;
        }
        
        .ace_gutter-active-line {
            position: absolute;
            left: 0;
            right: 0;
        }
        
        .ace_scroller.ace_scroll-left {
            box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;
        }
        
        .ace_gutter-cell {
            padding-left: 19px;
            padding-right: 6px;
            background-repeat: no-repeat;
        }
        
        .ace_gutter-cell.ace_error {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");
            background-repeat: no-repeat;
            background-position: 2px center;
        }
        
        .ace_gutter-cell.ace_warning {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");
            background-position: 2px center;
        }
        
        .ace_gutter-cell.ace_info {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");
            background-position: 2px center;
        }
        
        .ace_dark .ace_gutter-cell.ace_info {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");
        }
        
        .ace_scrollbar {
            position: absolute;
            right: 0;
            bottom: 0;
            z-index: 6;
        }
        
        .ace_scrollbar-inner {
            position: absolute;
            cursor: text;
            left: 0;
            top: 0;
        }
        
        .ace_scrollbar-v {
            overflow-x: hidden;
            overflow-y: scroll;
            top: 0;
        }
        
        .ace_scrollbar-h {
            overflow-x: scroll;
            overflow-y: hidden;
            left: 0;
        }
        
        .ace_print-margin {
            position: absolute;
            height: 100%;
        }
        
        .ace_text-input {
            position: absolute;
            z-index: 0;
            width: 0.5em;
            height: 1em;
            opacity: 0;
            background: transparent;
            -moz-appearance: none;
            appearance: none;
            border: none;
            resize: none;
            outline: none;
            overflow: hidden;
            font: inherit;
            padding: 0 1px;
            margin: 0 -1px;
            text-indent: -1em;
            -ms-user-select: text;
            -moz-user-select: text;
            -webkit-user-select: text;
            user-select: text;
            white-space: pre!important;
        }
        
        .ace_text-input.ace_composition {
            background: inherit;
            color: inherit;
            z-index: 1000;
            opacity: 1;
            text-indent: 0;
        }
        
        .ace_layer {
            z-index: 1;
            position: absolute;
            overflow: hidden;
            word-wrap: normal;
            white-space: pre;
            height: 100%;
            width: 100%;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            pointer-events: none;
        }
        
        .ace_gutter-layer {
            position: relative;
            width: auto;
            text-align: right;
            pointer-events: auto;
        }
        
        .ace_text-layer {
            font: inherit !important;
        }
        
        .ace_cjk {
            display: inline-block;
            text-align: center;
        }
        
        .ace_cursor-layer {
            z-index: 4;
        }
        
        .ace_cursor {
            z-index: 4;
            position: absolute;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            border-left: 2px solid;
            transform: translatez(0);
        }
        
        .ace_slim-cursors .ace_cursor {
            border-left-width: 1px;
        }
        
        .ace_overwrite-cursors .ace_cursor {
            border-left-width: 0;
            border-bottom: 1px solid;
        }
        
        .ace_hidden-cursors .ace_cursor {
            opacity: 0.2;
        }
        
        .ace_smooth-blinking .ace_cursor {
            -webkit-transition: opacity 0.18s;
            transition: opacity 0.18s;
        }
        
        .ace_editor.ace_multiselect .ace_cursor {
            border-left-width: 1px;
        }
        
        .ace_marker-layer .ace_step,
        .ace_marker-layer .ace_stack {
            position: absolute;
            z-index: 3;
        }
        
        .ace_marker-layer .ace_selection {
            position: absolute;
            z-index: 5;
        }
        
        .ace_marker-layer .ace_bracket {
            position: absolute;
            z-index: 6;
        }
        
        .ace_marker-layer .ace_active-line {
            position: absolute;
            z-index: 2;
        }
        
        .ace_marker-layer .ace_selected-word {
            position: absolute;
            z-index: 4;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
        }
        
        .ace_line .ace_fold {
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            display: inline-block;
            height: 11px;
            margin-top: -2px;
            vertical-align: middle;
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="), url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");
            background-repeat: no-repeat, repeat-x;
            background-position: center center, top left;
            color: transparent;
            border: 1px solid black;
            border-radius: 2px;
            cursor: pointer;
            pointer-events: auto;
        }
        
        .ace_dark .ace_fold {}
        
        .ace_fold:hover {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="), url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");
        }
        
        .ace_tooltip {
            background-color: #FFF;
            background-image: -webkit-linear-gradient(top, transparent, rgba(0, 0, 0, 0.1));
            background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));
            border: 1px solid gray;
            border-radius: 1px;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
            color: black;
            max-width: 100%;
            padding: 3px 4px;
            position: fixed;
            z-index: 999999;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            cursor: default;
            white-space: pre;
            word-wrap: break-word;
            line-height: normal;
            font-style: normal;
            font-weight: normal;
            letter-spacing: normal;
            pointer-events: none;
        }
        
        .ace_folding-enabled > .ace_gutter-cell {
            padding-right: 13px;
        }
        
        .ace_fold-widget {
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            margin: 0 -12px 0 1px;
            display: none;
            width: 11px;
            vertical-align: top;
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");
            background-repeat: no-repeat;
            background-position: center;
            border-radius: 3px;
            border: 1px solid transparent;
            cursor: pointer;
        }
        
        .ace_folding-enabled .ace_fold-widget {
            display: inline-block;
        }
        
        .ace_fold-widget.ace_end {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");
        }
        
        .ace_fold-widget.ace_closed {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");
        }
        
        .ace_fold-widget:hover {
            border: 1px solid rgba(0, 0, 0, 0.3);
            background-color: rgba(255, 255, 255, 0.2);
            box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);
        }
        
        .ace_fold-widget:active {
            border: 1px solid rgba(0, 0, 0, 0.4);
            background-color: rgba(0, 0, 0, 0.05);
            box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);
        }
        
        .ace_dark .ace_fold-widget {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");
        }
        
        .ace_dark .ace_fold-widget.ace_end {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");
        }
        
        .ace_dark .ace_fold-widget.ace_closed {
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");
        }
        
        .ace_dark .ace_fold-widget:hover {
            box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);
            background-color: rgba(255, 255, 255, 0.1);
        }
        
        .ace_dark .ace_fold-widget:active {
            box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);
        }
        
        .ace_fold-widget.ace_invalid {
            background-color: #FFB4B4;
            border-color: #DE5555;
        }
        
        .ace_fade-fold-widgets .ace_fold-widget {
            -webkit-transition: opacity 0.4s ease 0.05s;
            transition: opacity 0.4s ease 0.05s;
            opacity: 0;
        }
        
        .ace_fade-fold-widgets:hover .ace_fold-widget {
            -webkit-transition: opacity 0.05s ease 0.05s;
            transition: opacity 0.05s ease 0.05s;
            opacity: 1;
        }
        
        .ace_underline {
            text-decoration: underline;
        }
        
        .ace_bold {
            font-weight: bold;
        }
        
        .ace_nobold .ace_bold {
            font-weight: normal;
        }
        
        .ace_italic {
            font-style: italic;
        }
        
        .ace_error-marker {
            background-color: rgba(255, 0, 0, 0.2);
            position: absolute;
            z-index: 9;
        }
        
        .ace_highlight-marker {
            background-color: rgba(255, 255, 0, 0.2);
            position: absolute;
            z-index: 8;
        }
        
        .ace_br1 {
            border-top-left-radius: 3px;
        }
        
        .ace_br2 {
            border-top-right-radius: 3px;
        }
        
        .ace_br3 {
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        
        .ace_br4 {
            border-bottom-right-radius: 3px;
        }
        
        .ace_br5 {
            border-top-left-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        .ace_br6 {
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        .ace_br7 {
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        .ace_br8 {
            border-bottom-left-radius: 3px;
        }
        
        .ace_br9 {
            border-top-left-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br10 {
            border-top-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br11 {
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br12 {
            border-bottom-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br13 {
            border-top-left-radius: 3px;
            border-bottom-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br14 {
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        
        .ace_br15 {
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
            border-bottom-left-radius: 3px;
        }
        /*# sourceURL=ace/css/ace_editor.css */
    </style>
    <style id="ace-tm">
        .ace-tm .ace_gutter {
            background: #f0f0f0;
            color: #333;
        }
        
        .ace-tm .ace_print-margin {
            width: 1px;
            background: #e8e8e8;
        }
        
        .ace-tm .ace_fold {
            background-color: #6B72E6;
        }
        
        .ace-tm {
            background-color: #FFFFFF;
            color: black;
        }
        
        .ace-tm .ace_cursor {
            color: black;
        }
        
        .ace-tm .ace_invisible {
            color: rgb(191, 191, 191);
        }
        
        .ace-tm .ace_storage,
        .ace-tm .ace_keyword {
            color: blue;
        }
        
        .ace-tm .ace_constant {
            color: rgb(197, 6, 11);
        }
        
        .ace-tm .ace_constant.ace_buildin {
            color: rgb(88, 72, 246);
        }
        
        .ace-tm .ace_constant.ace_language {
            color: rgb(88, 92, 246);
        }
        
        .ace-tm .ace_constant.ace_library {
            color: rgb(6, 150, 14);
        }
        
        .ace-tm .ace_invalid {
            background-color: rgba(255, 0, 0, 0.1);
            color: red;
        }
        
        .ace-tm .ace_support.ace_function {
            color: rgb(60, 76, 114);
        }
        
        .ace-tm .ace_support.ace_constant {
            color: rgb(6, 150, 14);
        }
        
        .ace-tm .ace_support.ace_type,
        .ace-tm .ace_support.ace_class {
            color: rgb(109, 121, 222);
        }
        
        .ace-tm .ace_keyword.ace_operator {
            color: rgb(104, 118, 135);
        }
        
        .ace-tm .ace_string {
            color: rgb(3, 106, 7);
        }
        
        .ace-tm .ace_comment {
            color: rgb(76, 136, 107);
        }
        
        .ace-tm .ace_comment.ace_doc {
            color: rgb(0, 102, 255);
        }
        
        .ace-tm .ace_comment.ace_doc.ace_tag {
            color: rgb(128, 159, 191);
        }
        
        .ace-tm .ace_constant.ace_numeric {
            color: rgb(0, 0, 205);
        }
        
        .ace-tm .ace_variable {
            color: rgb(49, 132, 149);
        }
        
        .ace-tm .ace_xml-pe {
            color: rgb(104, 104, 91);
        }
        
        .ace-tm .ace_entity.ace_name.ace_function {
            color: #0000A2;
        }
        
        .ace-tm .ace_heading {
            color: rgb(12, 7, 255);
        }
        
        .ace-tm .ace_list {
            color: rgb(185, 6, 144);
        }
        
        .ace-tm .ace_meta.ace_tag {
            color: rgb(0, 22, 142);
        }
        
        .ace-tm .ace_string.ace_regex {
            color: rgb(255, 0, 0)
        }
        
        .ace-tm .ace_marker-layer .ace_selection {
            background: rgb(181, 213, 255);
        }
        
        .ace-tm.ace_multiselect .ace_selection.ace_start {
            box-shadow: 0 0 3px 0px white;
        }
        
        .ace-tm .ace_marker-layer .ace_step {
            background: rgb(252, 255, 0);
        }
        
        .ace-tm .ace_marker-layer .ace_stack {
            background: rgb(164, 229, 101);
        }
        
        .ace-tm .ace_marker-layer .ace_bracket {
            margin: -1px 0 0 -1px;
            border: 1px solid rgb(192, 192, 192);
        }
        
        .ace-tm .ace_marker-layer .ace_active-line {
            background: rgba(0, 0, 0, 0.07);
        }
        
        .ace-tm .ace_gutter-active-line {
            background-color: #dcdcdc;
        }
        
        .ace-tm .ace_marker-layer .ace_selected-word {
            background: rgb(250, 250, 255);
            border: 1px solid rgb(200, 200, 250);
        }
        
        .ace-tm .ace_indent-guide {
            background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;
        }
        /*# sourceURL=ace/css/ace-tm */
    </style>
    <style>
        .error_widget_wrapper {
            background: inherit;
            color: inherit;
            border: none
        }
        
        .error_widget {
            border-top: solid 2px;
            border-bottom: solid 2px;
            margin: 5px 0;
            padding: 10px 40px;
            white-space: pre-wrap;
        }
        
        .error_widget.ace_error,
        .error_widget_arrow.ace_error {
            border-color: #ff5a5a
        }
        
        .error_widget.ace_warning,
        .error_widget_arrow.ace_warning {
            border-color: #F1D817
        }
        
        .error_widget.ace_info,
        .error_widget_arrow.ace_info {
            border-color: #5a5a5a
        }
        
        .error_widget.ace_ok,
        .error_widget_arrow.ace_ok {
            border-color: #5aaa5a
        }
        
        .error_widget_arrow {
            position: absolute;
            border: solid 5px;
            border-top-color: transparent!important;
            border-right-color: transparent!important;
            border-left-color: transparent!important;
            top: -5px;
        }
    </style>
    <style id="ace_searchbox">
        .ace_search {
            background-color: #ddd;
            border: 1px solid #cbcbcb;
            border-top: 0 none;
            max-width: 325px;
            overflow: hidden;
            margin: 0;
            padding: 4px;
            padding-right: 6px;
            padding-bottom: 0;
            position: absolute;
            top: 0px;
            z-index: 99;
            white-space: normal;
        }
        
        .ace_search.left {
            border-left: 0 none;
            border-radius: 0px 0px 5px 0px;
            left: 0;
        }
        
        .ace_search.right {
            border-radius: 0px 0px 0px 5px;
            border-right: 0 none;
            right: 0;
        }
        
        .ace_search_form,
        .ace_replace_form {
            border-radius: 3px;
            border: 1px solid #cbcbcb;
            float: left;
            margin-bottom: 4px;
            overflow: hidden;
        }
        
        .ace_search_form.ace_nomatch {
            outline: 1px solid red;
        }
        
        .ace_search_field {
            background-color: white;
            color: black;
            border-right: 1px solid #cbcbcb;
            border: 0 none;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            float: left;
            height: 22px;
            outline: 0;
            padding: 0 7px;
            width: 214px;
            margin: 0;
        }
        
        .ace_searchbtn,
        .ace_replacebtn {
            background: #fff;
            border: 0 none;
            border-left: 1px solid #dcdcdc;
            cursor: pointer;
            float: left;
            height: 22px;
            margin: 0;
            position: relative;
        }
        
        .ace_searchbtn:last-child,
        .ace_replacebtn:last-child {
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        .ace_searchbtn:disabled {
            background: none;
            cursor: default;
        }
        
        .ace_searchbtn {
            background-position: 50% 50%;
            background-repeat: no-repeat;
            width: 27px;
        }
        
        .ace_searchbtn.prev {
            background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAADFJREFUeNpiSU1NZUAC/6E0I0yACYskCpsJiySKIiY0SUZk40FyTEgCjGgKwTRAgAEAQJUIPCE+qfkAAAAASUVORK5CYII=);
        }
        
        .ace_searchbtn.next {
            background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAADRJREFUeNpiTE1NZQCC/0DMyIAKwGJMUAYDEo3M/s+EpvM/mkKwCQxYjIeLMaELoLMBAgwAU7UJObTKsvAAAAAASUVORK5CYII=);
        }
        
        .ace_searchbtn_close {
            background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAcCAYAAABRVo5BAAAAZ0lEQVR42u2SUQrAMAhDvazn8OjZBilCkYVVxiis8H4CT0VrAJb4WHT3C5xU2a2IQZXJjiQIRMdkEoJ5Q2yMqpfDIo+XY4k6h+YXOyKqTIj5REaxloNAd0xiKmAtsTHqW8sR2W5f7gCu5nWFUpVjZwAAAABJRU5ErkJggg==) no-repeat 50% 0;
            border-radius: 50%;
            border: 0 none;
            color: #656565;
            cursor: pointer;
            float: right;
            font: 16px/16px Arial;
            height: 14px;
            margin: 5px 1px 9px 5px;
            padding: 0;
            text-align: center;
            width: 14px;
        }
        
        .ace_searchbtn_close:hover {
            background-color: #656565;
            background-position: 50% 100%;
            color: white;
        }
        
        .ace_replacebtn.prev {
            width: 54px
        }
        
        .ace_replacebtn.next {
            width: 27px
        }
        
        .ace_button {
            margin-left: 2px;
            cursor: pointer;
            -webkit-user-select: none;
            -moz-user-select: none;
            -o-user-select: none;
            -ms-user-select: none;
            user-select: none;
            overflow: hidden;
            opacity: 0.7;
            border: 1px solid rgba(100, 100, 100, 0.23);
            padding: 1px;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            color: black;
        }
        
        .ace_button:hover {
            background-color: #eee;
            opacity: 1;
        }
        
        .ace_button:active {
            background-color: #ddd;
        }
        
        .ace_button.checked {
            border-color: #3399ff;
            opacity: 1;
        }
        
        .ace_search_options {
            margin-bottom: 3px;
            text-align: right;
            -webkit-user-select: none;
            -moz-user-select: none;
            -o-user-select: none;
            -ms-user-select: none;
            user-select: none;
        }
        /*# sourceURL=ace/css/ace_searchbox */
    </style>
    <script type="text/javascript" src="https://s3.amazonaws.com/assets.freshdesk.com/widget/html2canvas.js?ver=2"></script>
    <link rel="stylesheet" type="text/css" href="https://s3.amazonaws.com/assets.freshdesk.com/widget/freshwidget.css?ver=2">
    <style id="ace-xcode">
        .ace-xcode .ace_gutter {
            background: #e8e8e8;
            color: #333
        }
        
        .ace-xcode .ace_print-margin {
            width: 1px;
            background: #e8e8e8
        }
        
        .ace-xcode {
            background-color: #FFFFFF;
            color: #000000
        }
        
        .ace-xcode .ace_cursor {
            color: #000000
        }
        
        .ace-xcode .ace_marker-layer .ace_selection {
            background: #B5D5FF
        }
        
        .ace-xcode.ace_multiselect .ace_selection.ace_start {
            box-shadow: 0 0 3px 0px #FFFFFF;
        }
        
        .ace-xcode .ace_marker-layer .ace_step {
            background: rgb(198, 219, 174)
        }
        
        .ace-xcode .ace_marker-layer .ace_bracket {
            margin: -1px 0 0 -1px;
            border: 1px solid #BFBFBF
        }
        
        .ace-xcode .ace_marker-layer .ace_active-line {
            background: rgba(0, 0, 0, 0.071)
        }
        
        .ace-xcode .ace_gutter-active-line {
            background-color: rgba(0, 0, 0, 0.071)
        }
        
        .ace-xcode .ace_marker-layer .ace_selected-word {
            border: 1px solid #B5D5FF
        }
        
        .ace-xcode .ace_constant.ace_language,
        .ace-xcode .ace_keyword,
        .ace-xcode .ace_meta,
        .ace-xcode .ace_variable.ace_language {
            color: #C800A4
        }
        
        .ace-xcode .ace_invisible {
            color: #BFBFBF
        }
        
        .ace-xcode .ace_constant.ace_character,
        .ace-xcode .ace_constant.ace_other {
            color: #275A5E
        }
        
        .ace-xcode .ace_constant.ace_numeric {
            color: #3A00DC
        }
        
        .ace-xcode .ace_entity.ace_other.ace_attribute-name,
        .ace-xcode .ace_support.ace_constant,
        .ace-xcode .ace_support.ace_function {
            color: #450084
        }
        
        .ace-xcode .ace_fold {
            background-color: #C800A4;
            border-color: #000000
        }
        
        .ace-xcode .ace_entity.ace_name.ace_tag,
        .ace-xcode .ace_support.ace_class,
        .ace-xcode .ace_support.ace_type {
            color: #790EAD
        }
        
        .ace-xcode .ace_storage {
            color: #C900A4
        }
        
        .ace-xcode .ace_string {
            color: #DF0002
        }
        
        .ace-xcode .ace_comment {
            color: #008E00
        }
        
        .ace-xcode .ace_indent-guide {
            background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==) right repeat-y
        }
        /*# sourceURL=ace/css/ace-xcode */
    </style>
</head>

<body>
    <div class="freshwidget-container responsive" id="FreshWidget" data-html2canvas-ignore="true" style="display: none;">
        <div class="widget-ovelay" id="freshwidget-overlay">&nbsp;</div>
        <div class="freshwidget-dialog" id="freshwidget-dialog">
            <div id="freshwidget-close" class="widget-close"></div>
            <div class="mobile-widget-close" id="mobile-widget-close"></div>
            <div class="mobile-widget-arrow" id="mobile-widget-arrow"></div>
            <div class="frame-container"> </div>
            <iframe title="Feedback Form" id="freshwidget-frame" src="https://csacademy.freshdesk.com/loading.html?ver=2" frameborder="0" scrolling="auto" allowtransparency="true" style="height: 500px">
        </div>
    </div>
    </iframe>
    </div>
    </div>
    <div id="freshwidget-button" data-html2canvas-ignore="true" class="freshwidget-button fd-btn-left" style="display: none; top: 450px;"><a href="javascript:void(0)" class="freshwidget-theme" style="color: white; background-color: rgb(71, 159, 186); border-color: white;">Support</a></div>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root">
        <div id="app" style="font-size: 14px;">
            <nav class="navbar-nav">
                <ul class="navbar" role="navigation">
                    <div class="group">
                        <li class="navitem"><a class="active" aria-current="page" href="/notes/554">Notes</a></li>
                        <li class="navitem"><a href="/ide">Sandbox</a></li>
                        <li class="navitem"><a href="/docs">Docs</a></li>
                        <li class="navitem"><a href="/resource/colors">Colors</a></li>
                    </div>
                    <div class="group center">
                        <li class="navbar-center navbar-title">
                            <div class="navbar-back-button show-arrow" role="button" tabindex="0">Back to lessons</div>
                        </li>
                    </div>
                    <div class="group right">
                        <li class="settings-button-container">
                            <button></button>
                        </li>
                        <li>
                            <div class="dropdown btn-group">
                                <div class="avatar-toggle" bsrole="toggle" id="avatar-dropdown" bsclass="dropdown-toggle"><img class="avatar" alt="your avatar" src="https://s3.amazonaws.com/cmu-cs-academy.lib.prod/default_avatar.png"><span class="caret"></span></div>
                                <ul role="menu" class="avatar-dropdown-menu dropdown-menu dropdown-menu-right" aria-labelledby="avatar-dropdown">
                                    <li role="presentation" class="disabled"><a role="menuitem" tabindex="-1" href="#">Signed in as jrashid</a></li>
                                    <li role="presentation" class="disabled"><a role="menuitem" tabindex="-1" href="#">1 Points</a></li>
                                    <li role="presentation" class=""><a role="menuitem" tabindex="-1" href="#">Teacher Portal</a></li>
                                    <li role="presentation" class="classroom"><a role="menuitem" tabindex="-1" href="#">pre-req</a></li>
                                    <li role="presentation" class="classroom"><a role="menuitem" tabindex="-1" href="#">Rahnuma Public School Class VII</a></li>
                                    <li role="presentation" class="classroom"><a role="menuitem" tabindex="-1" href="#">Rahnuma Public School Training</a></li>
                                    <li role="presentation" class="classroom"><a role="menuitem" tabindex="-1" href="#">Summer Workshop</a></li>
                                    <li role="separator" class="divider"></li>
                                    <li role="presentation" class=""><a role="menuitem" tabindex="-1" href="#">Change Password</a></li>
                                    <li role="presentation" class=""><a role="menuitem" tabindex="-1" href="#">Settings</a></li>
                                    <li role="presentation" class=""><a role="menuitem" tabindex="-1" href="#">Logout</a></li>
                                </ul>
                            </div>
                        </li>
                    </div>
                </ul>
            </nav>
            <div class="notes-page-with-nav ">
                <ul class="scrollspy-nav">
                    <li class=""><a href="#" class="">Arcs and Arrows</a></li>
                    <li class=""><a href="#" class="">Arcs</a></li>
                    <li class="active"><a href="#" class="">Angles</a></li>
                    <li class=""><a href="#" class="">startAngle and sweepAngle</a></li>
                    <li class=""><a href="#" class="">Circular Arcs</a></li>
                    <li class=""><a href="#" class="">Arrows</a></li>
                    <div class="strength-earned">0 <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAsCAYAAAB2d9g5AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gcFFQ0rEVnanQAAAxBJREFUWMPtmMtPE1EUxs8dWqGlvAzEAgXa8m6rogYCupD4gETUplHQSEWjWAyibCAKLnBh2Lrqn+DGlS5woRutUWgHmFJBJCo+8NUnJZTC0HbGhQlB2g69ZerCeHadO51fzp3vfPecQSzLwt8MAv5y/PtAAdciwzJwj+qfejNPqXAemoQIaJKfRVrlBbwMZ+YnABcGABBiGfixNGfE3lLSbtLGs21JKAlOKtquYQFDbBDGHC8exgNsKNDl50kK8UQz7R4HX3ARG5aVnA3HFa3fsVVqsZs648nuTIkBpQjEeGURZAIw7nxlxIVVZu7+VC09iF+HUy4SlkNLeAWNBHCuvEsRV+Fb7KYBbKHItPJoQuEEroZooFzDd3CFckKp/xyXtdlcZqCZFazsWoqvcAqFEzjqMBlxhVKTWx/z/Wj9eUiHlqHb1MIGmNWYHyAmxJAsFEVdZ1mAquzapvOVNx6HmTflGAYcGACAn/GDn/Zz3vPaQw4BAArbUvLnsyH+zz8E+rJOFPYOlwM+mPSOHeMbeFimrdqVUxcumjHHSwgyQV5hhWnFcLq0fSKiSkn7cwufsGQiBTrU/UhACCOXxeziTDWfwNbyTiRNlUVvMQyqXjTtsaoAoUB0iTPip98eWTdrLWul9YMH8ho3r8PN4uPCW7g72s35hxxRLgxUG5FImLr1rs3m5n7NAkIAHZqbUWHYQKtzhDM7naINKdIr+elLPbQLvvpmo66rs/ZaG4ua+WuEJ51mYCBygunCDGjX9O5BiOAPSDlHnkTxf7is6kHp27bz1+rToRWY9lqPRlprLNCVabJr+J0tZjxUxFOkSFIKupJL73gfZiinuTncukRg2NmHhBusa8tAFliwuc0PNl7XV3QhqTif/3Hty8J78K56/rhWt+PQ7f25RxIzH1pdw2HWpa+4PpiwgXTCZWbXT0VX1X0xd2jYQC/tgjnfh7Xfp5QXkTyjPHEjt81pWXMXddY+skHeDFsNTuCkm7z/27oyoV3TU4MAJRYokyhbJYI0MGhuxWxdWI3w/+80fMQv6UICCCr8x+gAAAAASUVORK5CYII=" alt="strength icon"></div>
                </ul>
                <div class="notes-page-container" tabindex="-1">
                    <div class="notes-page-inner">
                        <h1 id="toc-main-title">Arcs and Arrows</h1>
                        <div>
                            <h2></h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Let's learn about <b>arcs</b> and <b>arrows</b>, two shapes that can be very helpful at times.
                                </p>
                            </div>
                        </div>
                        <div id="toc-5103cbc412090de9918662743710b4664f72774a">
                            <h2>Arcs</h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    An <b>arc</b> is a part of an oval. For example:
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-df062dc0c3530aad5f6aa908c38f34a403a5605a" class=" ace_editor ace-xcode" style="width: 100%; height: 103.4px; font-size: 14px; font-family: Inconsolata;">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 44px; top: 72px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 115.2px; width: 40px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">6</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 72px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 40px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 372px; height: 115.2px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:72.00000286102295px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arcs Demo #1'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'A navy arc on a gold oval'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">400</span>, <span class="ace_constant ace_numeric">150</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">400</span>, <span class="ace_constant ace_numeric">150</span>, <span class="ace_constant ace_numeric">0</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 72px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 86.4px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 40px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 662px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Run the code and see that the navy arc covers a part of the gold oval. Let's take a closer look. First, here is how we drew the oval:
                                </p><pre><code class="hljs javascript">  Oval(<span class="hljs-number">200</span>, <span class="hljs-number">200</span>, <span class="hljs-number">400</span>, <span class="hljs-number">150</span>, fill=<span class="hljs-string">'gold'</span>)</code></pre> This draws a gold oval inside the rectangle centered at (200, 200) with a width of 400 and a height of 150.
                                <p></p>

                                <p>
                                    Now, let's look at the arc:
                                </p><pre><code class="hljs javascript">  Arc(<span class="hljs-number">200</span>, <span class="hljs-number">200</span>, <span class="hljs-number">400</span>, <span class="hljs-number">150</span>, <span class="hljs-number">0</span>, <span class="hljs-number">90</span>, fill=<span class="hljs-string">'navy'</span>)</code></pre> Notice that the first 4 values -- <code>200, 200, 400, 150</code> -- are the same as the oval's. This is because an arc is part of an oval, so we first specify that oval. So those values are the <code>centerX</code>, <code>centerY</code> , <code>width</code>, and <code>height</code> of the oval. The two additional values -- <code>0, 90</code> -- specify the <b>startAngle</b> and the <b>sweepAngle</b> of the arc. As we will next explore in more detail, these two values control how much of the oval is included in the arc.
                                <p></p>
                            </div>
                        </div>
                        <div id="toc-ff8084f15b2e36de1a91a87a056e597bc99716d5">
                            <h2>Angles</h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Here are the facts you need to know about angles in this course:
                                </p>
                                <ul>
                                    <li>Angles are measured in degrees.</li>
                                    <li>0 degrees heads straight up.</li>
                                    <li>Angles increase clockwise. Thus, for example, 90 degrees heads to the right.</li>
                                </ul>
                                This image may help:
                                <div width="200" class="cmu-cs-academy-img" img-src="angles.png" img-alt="counterclockwise unit circle with 0 degrees on top"><img src="https://s3.amazonaws.com/cmu-cs-academy.content.public.v2-prod/b4f833a32220a69e4198ea8936cce30a%3A%3Aangles.png" alt="counterclockwise unit circle with 0 degrees on top" width="200" class="img"></div>
                                <p></p>
                            </div>
                        </div>
                        <div class="notes-checkpoint">
                            <h3>Checkpoint 1<span><div class="status-icon complete"></div><button class="redo">Redo checkpoint</button></span></h3></div>
                        <div id="toc-8602ad4c3c2b3e46fa1e17865c46f7e2e6304d6b">
                            <h2>startAngle and sweepAngle</h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    The <code>startAngle</code> and <code>sweepAngle</code> work together to specify which part of the oval is in an arc. If you were drawing this by hand, the <code>startAngle</code> is where you should put your pen down on the paper to start drawing, and the <code>sweepAngle</code> is
                                    <b>how far</b> you should draw.
                                </p>

                                <p>
                                    Some examples would help. To start, let's look at different values of <code>startAngle</code> while keeping the <code>sweepAngle</code> fixed at 90 degrees (which is one-quarter of the oval):
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-a973e03661817862c39e938fa854597f0de338c2" style="width: 100%; height: 305px; font-size: 14px; font-family: Inconsolata;" class=" ace_editor ace-xcode">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 51px; top: 273.6px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 316.8px; width: 47px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">6</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">7</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">8</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">9</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">10</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">11</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">12</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">13</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">14</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">15</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">16</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">17</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">18</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">19</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">20</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 273.6px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 47px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 386px; height: 316.8px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:273.6000108718872px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arcs Demo #2'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Different startAngle values'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'The sweepAngle is always 90'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">65</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'startAngle = 0'</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">110</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">0</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'startAngle = 45'</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">110</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'startAngle = 90'</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">260</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'startAngle = 135'</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">260</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">135</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 273.6px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 288px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 47px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 652px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Run the code, and look carefully at the code and what is drawn. Be sure to understand how changing the <code>startAngle</code> affects the arc that is drawn.
                                </p>
                            </div>
                        </div>
                        <div class="notes-checkpoint">
                            <h3>Checkpoint 2<span><div class="status-icon complete"></div><button class="redo">Redo checkpoint</button></span></h3></div>
                        <div>
                            <h2></h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Here is another example that keeps the <code>startAngle</code> always at 90 degrees (to the right), and changes the <code>sweepAngle</code>:
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-bb01810755fd12a62ce344871fca232ee70090e1" style="width: 100%; height: 305px; font-size: 14px; font-family: Inconsolata;" class=" ace_editor ace-xcode">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 51px; top: 273.6px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 316.8px; width: 47px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">6</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">7</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">8</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">9</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">10</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">11</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">12</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">13</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">14</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">15</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">16</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">17</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">18</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">19</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">20</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 273.6px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 47px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 386px; height: 316.8px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:273.6000108718872px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arcs Demo #3'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Different sweepAngle values'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'The startAngle is always 90'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">65</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'sweepAngle = 45'</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">110</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'sweepAngle = 90'</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">110</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'sweepAngle = 135'</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">260</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_constant ace_numeric">135</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'sweepAngle = 180'</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">260</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Oval</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">325</span>, <span class="ace_constant ace_numeric">190</span>, <span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_constant ace_numeric">180</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 273.6px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 288px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 47px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 652px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Run the code, and focus on how changing the <code>sweepAngle</code> affects the arc.
                                </p>
                            </div>
                        </div>
                        <div id="toc-3db6a4d4c8167c40e7f386e6df6fa5a9a630e85d">
                            <h2>Circular Arcs</h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Since an arc is part of an oval, and a circle is a kind of oval, an arc can be part of a circle. In fact, this is the most common use of arcs. To make an arc that is part of a circle, we set both its <code>width</code> and its <code>height</code> to the <b>diameter</b> of the circle, which is <b>twice</b> its <code>radius</code>. For example:
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-e71c5a7ec7424bde0fc91e8f4fa43f9fd94ebbb3" style="width: 100%; height: 103.4px; font-size: 14px; font-family: Inconsolata;" class=" ace_editor ace-xcode">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 44px; top: 72px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 115.2px; width: 40px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">6</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 72px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 40px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 386px; height: 115.2px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:72.00000286102295px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arcs Demo #4'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'A navy arc on a gold circle'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Circle</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">125</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'gold'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">250</span>, <span class="ace_constant ace_numeric">250</span>, <span class="ace_constant ace_numeric">0</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 72px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 86.4px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 40px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 662px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Run the code and see how the arc covers part of the circle. Look closely and see that the <code>radius</code> of the circle is 125, and the <code>width</code> and <code>height</code> of the arc are both 250.
                                </p>

                                <p>
                                    To be clear, here is the same example without the circle:
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-dbf815e6dcc6dbe97c542f9a2b286fcec245d73d" style="width: 100%; height: 89px; font-size: 14px; font-family: Inconsolata;" class=" ace_editor ace-xcode">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 44px; top: 57.6px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 100.8px; width: 40px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 57.6px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 40px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 421px; height: 100.8px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:57.60000228881836px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arcs Demo #5'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'A navy arc by itself (no circle)'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">45</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Arc</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">250</span>, <span class="ace_constant ace_numeric">250</span>, <span class="ace_constant ace_numeric">0</span>, <span class="ace_constant ace_numeric">90</span>, <span class="ace_identifier">fill</span><span class="ace_keyword ace_operator">=</span><span class="ace_string">'navy'</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 57.6px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 72px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 40px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 662px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                        </div>
                        <div class="notes-checkpoint">
                            <h3>Checkpoint 3<span><div class="status-icon complete"></div><button class="redo">Redo checkpoint</button></span></h3></div>
                        <div id="toc-0cf604cb001bdc6112fda3affb0c7674d1c4481b">
                            <h2>Arrows</h2>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    An <b>arrow</b> is simply a line with a triangular arrow head at one or both ends. We do not actually have an arrow shape. Instead, we use a line, and we set the <code>arrowStart</code> property to <code>True</code> to draw an arrow head at the start of the line. Similarly, we set
                                    <code>arrowEnd</code> to <code>True</code> to draw an arrow head at the end of the line. For example:
                                </p>
                            </div>
                            <div class="inline-af-container">
                                <div class="inline-editor-container">
                                    <div id="inline-editor-61aedb44ca96e5a6c00a19164abddb729277e2cc" style="width: 100%; height: 218.6px; font-size: 14px; font-family: Inconsolata;" class=" ace_editor ace-xcode">
                                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 7px; left: 51px; top: 187.2px;"></textarea>
                                        <div class="ace_gutter">
                                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 230.4px; width: 47px;">
                                                <div class="ace_gutter-cell " style="height: 14.4px;">1</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">2</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">3</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">4</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">5</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">6</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">7</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">8</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">9</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">10</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">11</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">12</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">13</div>
                                                <div class="ace_gutter-cell " style="height: 14.4px;">14</div>
                                            </div>
                                            <div class="ace_gutter-active-line" style="top: 187.2px; height: 14.4px;"></div>
                                        </div>
                                        <div class="ace_scroller" style="left: 47px; right: 0px; bottom: 17px;">
                                            <div class="ace_content" style="margin-top: 0px; width: 519px; height: 230.4px; margin-left: 0px;">
                                                <div class="ace_layer ace_print-margin-layer">
                                                    <div class="ace_print-margin" style="left: 564px; visibility: visible;"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer">
                                                    <div class="ace_active-line" style="height:14.40000057220459px;top:187.20000743865967px;left:0;right:0;"></div>
                                                </div>
                                                <div class="ace_layer ace_text-layer" style="padding: 0px 4px;">
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Arrows Demo'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">20</span>, <span class="ace_identifier">bold</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Line with no arrows'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">85</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Line</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">105</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">105</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Line with a start arrow'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">155</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Line</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">175</span>, <span class="ace_identifier">arrowStart</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Line with an end arrow'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">225</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Line</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">245</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">245</span>, <span class="ace_identifier">arrowEnd</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Label</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">'Line with both a start arrow and an end arrow'</span>, <span class="ace_constant ace_numeric">200</span>, <span class="ace_constant ace_numeric">295</span>, <span class="ace_identifier">size</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_numeric">16</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Line</span><span class="ace_paren ace_lparen">(</span><span class="ace_constant ace_numeric">100</span>, <span class="ace_constant ace_numeric">315</span>, <span class="ace_constant ace_numeric">300</span>, <span class="ace_constant ace_numeric">315</span>, <span class="ace_identifier">arrowStart</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span>, <span class="ace_identifier">arrowEnd</span><span class="ace_keyword ace_operator">=</span><span class="ace_constant ace_language">True</span><span class="ace_paren ace_rparen">)</span></div>
                                                    <div class="ace_line" style="height:14.40000057220459px"></div>
                                                </div>
                                                <div class="ace_layer ace_marker-layer"></div>
                                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                                    <div class="ace_cursor" style="left: 4px; top: 187.2px; width: 7px; height: 14.4px;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 17px;">
                                            <div class="ace_scrollbar-inner" style="width: 22px; height: 201.6px;"></div>
                                        </div>
                                        <div class="ace_scrollbar ace_scrollbar-h" style="height: 22px; left: 47px; right: 0px;">
                                            <div class="ace_scrollbar-inner" style="height: 22px; width: 746px;"></div>
                                        </div>
                                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div>
                                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inline-editor-button-group">
                                    <button class="toolbar-button inline-af-play"></button>
                                </div>
                                <div></div>
                            </div>
                            <div class="dynamic-html notes-content teacher">
                                <p>
                                    Run the code and see how the different lines have different arrow heads, depending on their values for <code>arrowStart</code> and <code>arrowEnd</code>.
                                </p>
                            </div>
                        </div>
                        <div class="notes-checkpoint">
                            <h3>Checkpoint 4<span><div class="status-icon complete"></div><button class="redo">Redo checkpoint</button></span></h3></div>
                        <button class="button flat small teal continue">Back to Lessons</button>
                    </div>
                </div>
                <div></div>
            </div>
            <div id="settings"></div>
            <div class="toaster-container"></div>
            <div id="support-popup"></div>
        </div>
    </div>
    <div id="application-target"></div>
    <div id="brython-target"></div>
    <script>
        var _rollbarConfig = {
            accessToken: "ce5718b091db44c2b31b4ff4d410d686",
            captureUncaught: !0,
            enabled: -1 === "ce5718b091db44c2b31b4ff4d410d686".indexOf("%"),
            checkIgnore: function(r, e, o) {
                return !!(o && o.body && o.body.message && "Error executing solution code" === o.body.message.body && o.request && o.request.url && 0 < o.request.url.indexOf("/sharing/")) || !!(r && o && o.body && o.body.trace && o.body.trace.exception && "SyntaxError" === o.body.trace.exception.class)
            },
            ignoredMessages: [],
            payload: {
                client: {
                    javascript: {
                        source_map_enabled: !0,
                        code_version: "1",
                        guess_uncaught_frames: !0
                    }
                },
                environment: "production"
            }
        };
        ! function(o) {
            function n(r) {
                if (t[r]) return t[r].exports;
                var e = t[r] = {
                    exports: {},
                    id: r,
                    loaded: !1
                };
                return o[r].call(e.exports, e, e.exports, n), e.loaded = !0, e.exports
            }
            var t = {};
            n.m = o, n.c = t, n.p = "", n(0)
        }([function(r, e, o) {
            "use strict";
            var n = o(1),
                t = o(4);
            (_rollbarConfig = _rollbarConfig || {}).rollbarJsUrl = _rollbarConfig.rollbarJsUrl || "https://cdnjs.cloudflare.com/ajax/libs/rollbar.js/2.4.2/rollbar.min.js", _rollbarConfig.async = void 0 === _rollbarConfig.async || _rollbarConfig.async;
            var a = n.setupShim(window, _rollbarConfig),
                l = t(_rollbarConfig);
            window.rollbar = n.Rollbar, a.loadFull(window, document, !_rollbarConfig.async, _rollbarConfig, l)
        }, function(r, e, o) {
            "use strict";

            function c(r) {
                return function() {
                    try {
                        return r.apply(this, arguments)
                    } catch (r) {
                        try {
                            console.error("[Rollbar]: Internal error", r)
                        } catch (r) {}
                    }
                }
            }

            function n(r, e) {
                this.options = r, this._rollbarOldOnError = null;
                var o = i++;
                this.shimId = function() {
                    return o
                }, "undefined" != typeof window && window._rollbarShims && (window._rollbarShims[o] = {
                    handler: e,
                    messages: []
                })
            }

            function t(o) {
                return c(function() {
                    var r = Array.prototype.slice.call(arguments, 0),
                        e = {
                            shim: this,
                            method: o,
                            args: r,
                            ts: new Date
                        };
                    window._rollbarShims[this.shimId()].messages.push(e)
                })
            }
            var a, l = o(2),
                i = 0,
                s = o(3),
                d = function(r, e) {
                    return new n(r, e)
                };
            a = s.curry ? s.curry(d) : s.bind(null, d), n.prototype.loadFull = function(l, r, e, o, i) {
                var n = !1,
                    t = r.createElement("script"),
                    a = r.getElementsByTagName("script")[0],
                    s = a.parentNode;
                t.crossOrigin = "", t.src = o.rollbarJsUrl, e || (t.async = !0), t.onload = t.onreadystatechange = c(function() {
                    if (!(n || this.readyState && "loaded" !== this.readyState && "complete" !== this.readyState)) {
                        t.onload = t.onreadystatechange = null;
                        try {
                            s.removeChild(t)
                        } catch (r) {}
                        n = !0,
                            function() {
                                var r;
                                if (void 0 === l._rollbarDidLoad) {
                                    r = new Error("rollbar.js did not load");
                                    for (var e, o, n, t, a = 0; e = l._rollbarShims[a++];)
                                        for (e = e.messages || []; o = e.shift();)
                                            for (n = o.args || [], a = 0; a < n.length; ++a)
                                                if ("function" == typeof(t = n[a])) {
                                                    t(r);
                                                    break
                                                }
                                }
                                "function" == typeof i && i(r)
                            }()
                    }
                }), s.insertBefore(t, a)
            }, n.prototype.wrap = function(o, r, n) {
                try {
                    var t;
                    if (t = "function" == typeof r ? r : function() {
                            return r || {}
                        }, "function" != typeof o) return o;
                    if (o._isWrap) return o;
                    if (!o._rollbar_wrapped && (o._rollbar_wrapped = function() {
                            n && "function" == typeof n && n.apply(this, arguments);
                            try {
                                return o.apply(this, arguments)
                            } catch (r) {
                                var e = r;
                                throw e && ("string" == typeof e && (e = new String(e)), e._rollbarContext = t() || {}, e._rollbarContext._wrappedSource = o.toString(), window._rollbarWrappedError = e), e
                            }
                        }, o._rollbar_wrapped._isWrap = !0, o.hasOwnProperty))
                        for (var e in o) o.hasOwnProperty(e) && (o._rollbar_wrapped[e] = o[e]);
                    return o._rollbar_wrapped
                } catch (r) {
                    return o
                }
            };
            for (var p = "log,debug,info,warn,warning,error,critical,global,configure,handleUncaughtException,handleUnhandledRejection,captureEvent,captureDomContentLoaded,captureLoad".split(","), u = 0; u < p.length; ++u) n.prototype[p[u]] = t(p[u]);
            r.exports = {
                setupShim: function(e, o) {
                    if (e) {
                        var n = o.globalAlias || "Rollbar";
                        if ("object" == typeof e[n]) return e[n];
                        e._rollbarShims = {}, e._rollbarWrappedError = null;
                        var t = new a(o);
                        return c(function() {
                            o.captureUncaught && (t._rollbarOldOnError = e.onerror, l.captureUncaughtExceptions(e, t, !0), l.wrapGlobals(e, t, !0)), o.captureUnhandledRejections && l.captureUnhandledRejections(e, t, !0);
                            var r = o.autoInstrument;
                            return !1 !== o.enabled && (void 0 === r || !0 === r || "object" == typeof r && r.network) && e.addEventListener && (e.addEventListener("load", t.captureLoad.bind(t)), e.addEventListener("DOMContentLoaded", t.captureDomContentLoaded.bind(t))), e[n] = t
                        })()
                    }
                },
                Rollbar: a
            }
        }, function(r, e) {
            "use strict";

            function l(n, r, e) {
                if (r.hasOwnProperty && r.hasOwnProperty("addEventListener")) {
                    for (var t = r.addEventListener; t._rollbarOldAdd && t.belongsToShim;) t = t._rollbarOldAdd;
                    var o = function(r, e, o) {
                        t.call(this, r, n.wrap(e), o)
                    };
                    o._rollbarOldAdd = t, o.belongsToShim = e, r.addEventListener = o;
                    for (var a = r.removeEventListener; a._rollbarOldRemove && a.belongsToShim;) a = a._rollbarOldRemove;
                    var l = function(r, e, o) {
                        a.call(this, r, e && e._rollbar_wrapped || e, o)
                    };
                    l._rollbarOldRemove = a, l.belongsToShim = e, r.removeEventListener = l
                }
            }
            r.exports = {
                captureUncaughtExceptions: function(a, l, r) {
                    if (a) {
                        var i;
                        "function" == typeof l._rollbarOldOnError ? i = l._rollbarOldOnError : a.onerror && !a.onerror.belongsToShim && (i = a.onerror, l._rollbarOldOnError = i);
                        var e = function() {
                            var r, e, o, n, t = Array.prototype.slice.call(arguments, 0);
                            e = l, o = i, n = t, (r = a)._rollbarWrappedError && (n[4] || (n[4] = r._rollbarWrappedError), n[5] || (n[5] = r._rollbarWrappedError._rollbarContext), r._rollbarWrappedError = null), e.handleUncaughtException.apply(e, n), o && o.apply(r, n)
                        };
                        e.belongsToShim = r, a.onerror = e
                    }
                },
                captureUnhandledRejections: function(r, t, e) {
                    if (r) {
                        "function" == typeof r._rollbarURH && r._rollbarURH.belongsToShim && r.removeEventListener("unhandledrejection", r._rollbarURH);
                        var o = function(r) {
                            var e, o, n;
                            try {
                                e = r.reason
                            } catch (r) {
                                e = void 0
                            }
                            try {
                                o = r.promise
                            } catch (r) {
                                o = "[unhandledrejection] error getting `promise` from event"
                            }
                            try {
                                n = r.detail, !e && n && (e = n.reason, o = n.promise)
                            } catch (r) {
                                n = "[unhandledrejection] error getting `detail` from event"
                            }
                            e || (e = "[unhandledrejection] error getting `reason` from event"), t && t.handleUnhandledRejection && t.handleUnhandledRejection(e, o)
                        };
                        o.belongsToShim = e, r._rollbarURH = o, r.addEventListener("unhandledrejection", o)
                    }
                },
                wrapGlobals: function(r, e, o) {
                    if (r) {
                        var n, t, a = "EventTarget,Window,Node,ApplicationCache,AudioTrackList,ChannelMergerNode,CryptoOperation,EventSource,FileReader,HTMLUnknownElement,IDBDatabase,IDBRequest,IDBTransaction,KeyOperation,MediaController,MessagePort,ModalWindow,Notification,SVGElementInstance,Screen,TextTrack,TextTrackCue,TextTrackList,WebSocket,WebSocketWorker,Worker,XMLHttpRequest,XMLHttpRequestEventTarget,XMLHttpRequestUpload".split(",");
                        for (n = 0; n < a.length; ++n) r[t = a[n]] && r[t].prototype && l(e, r[t].prototype, o)
                    }
                }
            }
        }, function(r, e) {
            "use strict";

            function o(r, e) {
                this.impl = r(e, this), this.options = e,
                    function(r) {
                        for (var e = function(e) {
                                return function() {
                                    var r = Array.prototype.slice.call(arguments, 0);
                                    if (this.impl[e]) return this.impl[e].apply(this.impl, r)
                                }
                            }, o = "log,debug,info,warn,warning,error,critical,global,configure,handleUncaughtException,handleUnhandledRejection,_createItem,wrap,loadFull,shimId,captureEvent,captureDomContentLoaded,captureLoad".split(","), n = 0; n < o.length; n++) r[o[n]] = e(o[n])
                    }(o.prototype)
            }
            o.prototype._swapAndProcessMessages = function(r, e) {
                this.impl = r(this.options);
                for (var o, n, t; o = e.shift();) n = o.method, t = o.args, this[n] && "function" == typeof this[n] && ("captureDomContentLoaded" === n || "captureLoad" === n ? this[n].apply(this, [t[0], o.ts]) : this[n].apply(this, t));
                return this
            }, r.exports = o
        }, function(r, e) {
            "use strict";
            r.exports = function(i) {
                return function(r) {
                    if (!r && !window._rollbarInitialized) {
                        for (var e, o, n = (i = i || {}).globalAlias || "Rollbar", t = window.rollbar, a = function(r) {
                                return new t(r)
                            }, l = 0; e = window._rollbarShims[l++];) o || (o = e.handler), e.handler._swapAndProcessMessages(a, e.messages);
                        window[n] = o, window._rollbarInitialized = !0
                    }
                }
            }
        }])
    </script>
    <script>
        ! function(l) {
            function e(e) {
                for (var r, t, n = e[0], o = e[1], u = e[2], f = 0, i = []; f < n.length; f++) t = n[f], p[t] && i.push(p[t][0]), p[t] = 0;
                for (r in o) Object.prototype.hasOwnProperty.call(o, r) && (l[r] = o[r]);
                for (s && s(e); i.length;) i.shift()();
                return c.push.apply(c, u || []), a()
            }

            function a() {
                for (var e, r = 0; r < c.length; r++) {
                    for (var t = c[r], n = !0, o = 1; o < t.length; o++) {
                        var u = t[o];
                        0 !== p[u] && (n = !1)
                    }
                    n && (c.splice(r--, 1), e = f(f.s = t[0]))
                }
                return e
            }
            var t = {},
                p = {
                    1: 0
                },
                c = [];

            function f(e) {
                if (t[e]) return t[e].exports;
                var r = t[e] = {
                    i: e,
                    l: !1,
                    exports: {}
                };
                return l[e].call(r.exports, r, r.exports, f), r.l = !0, r.exports
            }
            f.m = l, f.c = t, f.d = function(e, r, t) {
                f.o(e, r) || Object.defineProperty(e, r, {
                    enumerable: !0,
                    get: t
                })
            }, f.r = function(e) {
                "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                    value: "Module"
                }), Object.defineProperty(e, "__esModule", {
                    value: !0
                })
            }, f.t = function(r, e) {
                if (1 & e && (r = f(r)), 8 & e) return r;
                if (4 & e && "object" == typeof r && r && r.__esModule) return r;
                var t = Object.create(null);
                if (f.r(t), Object.defineProperty(t, "default", {
                        enumerable: !0,
                        value: r
                    }), 2 & e && "string" != typeof r)
                    for (var n in r) f.d(t, n, function(e) {
                        return r[e]
                    }.bind(null, n));
                return t
            }, f.n = function(e) {
                var r = e && e.__esModule ? function() {
                    return e.default
                } : function() {
                    return e
                };
                return f.d(r, "a", r), r
            }, f.o = function(e, r) {
                return Object.prototype.hasOwnProperty.call(e, r)
            }, f.p = "/";
            var r = window.webpackJsonp = window.webpackJsonp || [],
                n = r.push.bind(r);
            r.push = e, r = r.slice();
            for (var o = 0; o < r.length; o++) e(r[o]);
            var s = n;
            a()
        }([])
    </script>
    <script src="/static/js/2.064fcb15.chunk.js"></script>
    <script src="/static/js/main.d6ec4a6f.chunk.js"></script>
    <script type="text/javascript" src="https://s3.amazonaws.com/assets.freshdesk.com/widget/freshwidget.js"></script>
    <script src="/static/js/cmu-graphics.75de2005.js"></script>
</body>

</html>