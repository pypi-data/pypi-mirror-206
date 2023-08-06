/*! For license information please see 54512-TVeSoffjEBs.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[54512],{53973:(e,t,n)=>{n(56299),n(65660),n(97968);var r=n(9672),o=n(50856),a=n(33760);(0,r.k)({_template:o.d`
    <style include="paper-item-shared-styles">
      :host {
        @apply --layout-horizontal;
        @apply --layout-center;
        @apply --paper-font-subhead;

        @apply --paper-item;
      }
    </style>
    <slot></slot>
`,is:"paper-item",behaviors:[a.U]})},82160:(e,t,n)=>{function r(e){return new Promise(((t,n)=>{e.oncomplete=e.onsuccess=()=>t(e.result),e.onabort=e.onerror=()=>n(e.error)}))}function o(e,t){const n=indexedDB.open(e);n.onupgradeneeded=()=>n.result.createObjectStore(t);const o=r(n);return(e,n)=>o.then((r=>n(r.transaction(t,e).objectStore(t))))}let a;function s(){return a||(a=o("keyval-store","keyval")),a}function u(e,t=s()){return t("readonly",(t=>r(t.get(e))))}function l(e,t,n=s()){return n("readwrite",(n=>(n.put(t,e),r(n.transaction))))}function p(e=s()){return e("readwrite",(e=>(e.clear(),r(e.transaction))))}n.d(t,{MT:()=>o,RV:()=>r,U2:()=>u,ZH:()=>p,t8:()=>l})}}]);
//# sourceMappingURL=54512-TVeSoffjEBs.js.map