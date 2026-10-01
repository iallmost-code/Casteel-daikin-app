(function(){
  const radios=[...document.querySelectorAll('.page-radio')];
  const global=document.getElementById('global-search');
  const dialog=document.getElementById('more-resources');
  function current(){return radios.find(r=>r.checked)?.id||'page-start';}
  function page(id){const r=document.getElementById(id);if(!r)return;r.checked=true;r.dispatchEvent(new Event('change'));window.scrollTo({top:0});}
  function section(){const ids={'page-start':'sec-start','page-fault':'sec-fault-codes','page-zoning':'sec-zoning','page-catalog':'sec-catalog-differences','page-ahri':'sec-ahri'};return document.getElementById(ids[current()]||'sec-start');}
  function sync(){
    const id=current();
    document.querySelectorAll('.bottom-nav label').forEach(label=>{
      const active=label.htmlFor===id;
      label.classList.toggle('active',active);
      if(active)label.setAttribute('aria-current','page');else label.removeAttribute('aria-current');
    });
    const target=section()?.querySelector('input.section-search,#ahri-search,#start-input');
    global.value=target?.value||'';
  }
  radios.forEach(r=>r.addEventListener('change',sync));sync();
  global.addEventListener('input',()=>{const query=global.value;let target=section()?.querySelector('input.section-search,#ahri-search,#start-input');if(!target){page('page-start');target=document.getElementById('start-input');}if(target){global.value=query;target.value=query;target.dispatchEvent(new Event('input',{bubbles:true}));}});
  document.getElementById('search-options').addEventListener('click',()=>{const target=section()?.querySelector('input.section-search,#ahri-search');if(target){target.focus();target.scrollIntoView({block:'center',behavior:'smooth'});}else global.focus();});
  // Existing mobile menu handler is retained; this dialog exposes the extra resources.
  document.getElementById('mobile-nav-toggle').addEventListener('click',()=>dialog.showModal());
  function close(){dialog.close();const menu=document.getElementById('mobile-nav-toggle');menu.setAttribute('aria-expanded','false');document.querySelector('header').classList.remove('mobile-nav-open');}
  document.getElementById('close-resources').addEventListener('click',close);
  dialog.addEventListener('close',()=>{document.getElementById('mobile-nav-toggle').setAttribute('aria-expanded','false');});
  dialog.addEventListener('click',e=>{if(e.target===dialog)close();const label=e.target.closest('label[for]');if(label){page(label.htmlFor);close();}});
  document.addEventListener('keydown',e=>{const label=e.target.closest('label[for]');if(label&&(e.key==='Enter'||e.key===' ')){e.preventDefault();label.click();const radio=document.getElementById(label.htmlFor);if(radio)radio.dispatchEvent(new Event('change'));}});
})();
