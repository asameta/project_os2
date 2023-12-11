import{u as a,_ as t}from"./VButton.vue_vue_type_style_index_0_lang-04276c31.js";import{p as e,z as s,A as l,B as o,F as n,G as i,J as r,C as c,r as u,a1 as d,L as p,H as m,E as v,u as f,I as h,T as g,D as b,K as y}from"./chunk-BGPNDDXN-18fd0b11.js";import{_ as k}from"./dayjs-5f21e00d.js";import{_,b as S}from"./route-block-26ba3c5b.js";const x={key:0},B={key:1},w={class:"flex-end"},q=e({__name:"VBlock",props:{title:{default:void 0},subtitle:{default:void 0},infratitle:{default:void 0},center:{type:Boolean},lighter:{type:Boolean},narrow:{type:Boolean},mResponsive:{type:Boolean},tResponsive:{type:Boolean}},setup(a){const t=a;return(a,e)=>(s(),l("div",{class:c([!t.center&&"media-flex",t.center&&"media-flex-center",t.narrow&&"no-margin",t.mResponsive&&"is-responsive-mobile",t.tResponsive&&"is-responsive-tablet-p"])},[o(a.$slots,"icon"),n("div",{class:c(["flex-meta",[t.lighter&&"is-lighter"]])},[o(a.$slots,"title",{},(()=>[n("span",null,i(t.title),1),t.subtitle?(s(),l("span",x,i(t.subtitle),1)):r("",!0),t.infratitle?(s(),l("span",B,i(t.infratitle),1)):r("",!0)])),o(a.$slots,"default")],2),n("div",w,[o(a.$slots,"action")])],2))}}),D=["src"],$=["src"],C=["src"],I=e({__name:"VAvatar",props:{picture:{default:void 0},pictureDark:{default:void 0},placeholder:{default:"https://via.placeholder.com/50x50"},badge:{default:void 0},initials:{default:"?"},size:{default:void 0},color:{default:void 0},dotColor:{default:void 0},squared:{type:Boolean},dot:{type:Boolean}},setup(a){const t=a,e=a=>{a.target.src=t.placeholder};return(u,d)=>(s(),l("div",{class:c(["v-avatar",[a.size&&`is-${t.size}`,a.dot&&"has-dot",a.dotColor&&`dot-${t.dotColor}`,a.squared&&a.dot&&"has-dot-squared"]])},[o(u.$slots,"avatar",{},(()=>[t.picture?(s(),l("img",{key:0,class:c(["avatar",[t.squared&&"is-squared",t.pictureDark&&"light-image"]]),src:t.picture,alt:"",onErrorOnce:e},null,42,D)):(s(),l("span",{key:1,class:c(["avatar is-fake",[t.squared&&"is-squared",t.color&&`is-${t.color}`]])},[n("span",null,i(t.initials),1)],2)),t.picture&&t.pictureDark?(s(),l("img",{key:2,class:c(["avatar dark-image",[t.squared&&"is-squared"]]),src:t.pictureDark,alt:"",onErrorOnce:e},null,42,$)):r("",!0)])),o(u.$slots,"badge",{},(()=>[t.badge?(s(),l("img",{key:0,class:"badge",src:t.badge,alt:"",onErrorOnce:e},null,40,C)):r("",!0)]))],2))}}),R={class:"account-wrapper"},j={class:"columns"},E={class:"column is-4"},z={class:"account-box is-navigation"},M={class:"account-menu"},O=n("i",{"aria-hidden":"true",class:"lnil lnil-user-alt"},null,-1),V=n("span",null,"Modbus",-1),P=n("span",{class:"end"},[n("i",{"aria-hidden":"true",class:"fas fa-arrow-right"})],-1),T=n("i",{"aria-hidden":"true",class:"lnil lnil-crown-alt"},null,-1),A=n("span",null,"Database",-1),G=n("span",{class:"end"},[n("i",{"aria-hidden":"true",class:"fas fa-arrow-right"})],-1),L={class:"account-box is-navigation mt-4"},N={key:0,class:"table is-hoverable is-fullwidth"},U=n("td",null,"System Time",-1),F=n("td",null,"CPU Serial",-1),H=n("td",null,"CPU Temperature",-1),J=n("td",null,"Ip",-1),K={class:"cta-block no-border"},W=n("div",{class:"head-text"},[n("h3",null,"Want to learn more?"),n("p",null,"Check out the Etki documentation")],-1),X={class:"head-action"},Q={class:"buttons"},Y={class:"column is-8"},Z=k.__esModule?k.default:k,aa=_.decode,ta=e({__name:"app",setup(e){const o=Z(),c=u(!1);a(),o.year().toString().substr(-2),(o.month()+1).toString().padStart(2,"0"),o.date().toString().padStart(2,"0"),o.hour().toString().padStart(2,"0"),o.minute().toString().padStart(2,"0"),d((async()=>{await k()}));const k=async()=>{if(!c.value){c.value=!0;const a=o.unix(),t=localStorage.getItem("hash");t||(localStorage.setItem("hash",""),localStorage.setItem("token",""));const e=Math.abs(a-t);Math.floor(e/60)<=10||(localStorage.setItem("hash",""),localStorage.setItem("token",""))}},_=u([]);u({});const S=u({}),x=u(!1);d((async()=>{B()}));const B=async()=>{await fetch("/data/connect.ini").then((a=>a.text())).then((a=>{_.value.push(...a.split("\n")),S.value=aa(_.value.join("\n")),x.value=!0})).catch((a=>console.log(a)))};return(a,e)=>{const o=I,c=q,u=p("RouterLink"),d=t,k=p("RouterView");return s(),l("div",R,[n("div",j,[n("div",E,[n("div",z,[m(c,{title:"Etki Online",subtitle:"",center:""},{icon:v((()=>[m(o,{size:"large",picture:"/favicon.svg"})])),_:1}),n("div",M,[m(u,{to:"/app",class:"account-menu-item"},{default:v((()=>[O,V,P])),_:1}),m(u,{to:"/app/database",class:"account-menu-item"},{default:v((()=>[T,A,G])),_:1})])]),n("div",L,[!0===f(x)?(s(),l("table",N,[n("tbody",null,[n("tr",null,[U,n("td",null,i(f(S).connect.time),1)]),n("tr",null,[F,n("td",null,i(f(S).connect.serial),1)]),n("tr",null,[H,n("td",null,i(f(S).connect.temperature),1)]),n("tr",null,[J,n("td",null,i(f(S).connect.ip_add),1)])])])):r("",!0)]),n("div",K,[W,n("div",X,[n("div",Q,[m(d,{class:"action-button",color:"primary",href:"https://etkiplatform.com"},{default:v((()=>[h(" Read the Docs ")])),_:1})])])])]),n("div",Y,[m(k,null,{default:v((({Component:a})=>[m(g,{name:"translate-page-y",mode:"in-out"},{default:v((()=>[(s(),b(y(a)))])),_:2},1024)])),_:1})])])])}}});"function"==typeof S&&S(ta);export{ta as default};
