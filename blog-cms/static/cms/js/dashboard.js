/* Congo Prime CMS — Dashboard JS */

// Auto-generate slug from title
function initSlugGenerator() {
  const titleInput = document.getElementById('id_title');
  const slugInput = document.getElementById('id_slug');
  const slugStatus = document.getElementById('slug-status');
  if (!titleInput || !slugInput) return;

  let userEditedSlug = slugInput.value.trim() !== '';

  titleInput.addEventListener('input', function() {
    if (!userEditedSlug) {
      slugInput.value = makeSlug(this.value);
      checkSlug();
    }
  });

  slugInput.addEventListener('input', function() {
    userEditedSlug = true;
    checkSlug();
  });

  function checkSlug() {
    const slug = slugInput.value.trim();
    if (!slug || !slugStatus) return;
    const pk = document.getElementById('article-pk') ? document.getElementById('article-pk').value : '';
    fetch(`/cms/articles/slug-check/?slug=${encodeURIComponent(slug)}&pk=${pk}`)
      .then(r => r.json())
      .then(data => {
        slugStatus.textContent = data.available ? '✓ Available' : '✗ Already taken';
        slugStatus.className = 'slug-status ' + (data.available ? 'ok' : 'taken');
      });
  }
}

function makeSlug(str) {
  return str.toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

// Character counters
function initCharCounters() {
  document.querySelectorAll('[data-maxlength]').forEach(function(el) {
    const max = parseInt(el.dataset.maxlength);
    const counter = document.getElementById(el.id + '-counter');
    if (!counter) return;
    function update() {
      const len = el.value.length;
      counter.textContent = len + ' / ' + max;
      counter.className = 'char-counter' + (len > max ? ' danger' : len > max * 0.85 ? ' warning' : '');
    }
    el.addEventListener('input', update);
    update();
  });
}

// Quill rich text editor
function initQuillEditor() {
  const editorEl = document.getElementById('quill-editor-container');
  const hiddenTextarea = document.getElementById('id_content');
  if (!editorEl || !hiddenTextarea || typeof Quill === 'undefined') return;

  const quill = new Quill('#quill-editor-container', {
    theme: 'snow',
    modules: {
      toolbar: [
        [{ 'header': [2, 3, 4, false] }],
        ['bold', 'italic', 'underline', 'strike'],
        [{ 'list': 'ordered' }, { 'list': 'bullet' }],
        ['blockquote', 'code-block'],
        ['link', 'image'],
        [{ 'align': [] }],
        ['clean']
      ]
    }
  });

  // Populate from textarea
  if (hiddenTextarea.value.trim()) {
    quill.root.innerHTML = hiddenTextarea.value;
  }

  // On form submit, copy Quill HTML to textarea
  const form = document.getElementById('article-form');
  if (form) {
    form.addEventListener('submit', function() {
      hiddenTextarea.value = quill.root.innerHTML;
    });
  }

  // Toggle HTML source view
  const toggleBtn = document.getElementById('toggle-html-btn');
  let showingHTML = false;
  if (toggleBtn) {
    toggleBtn.addEventListener('click', function() {
      if (!showingHTML) {
        hiddenTextarea.value = quill.root.innerHTML;
        editorEl.style.display = 'none';
        hiddenTextarea.style.display = 'block';
        toggleBtn.textContent = 'Visual Editor';
        showingHTML = true;
      } else {
        quill.root.innerHTML = hiddenTextarea.value;
        hiddenTextarea.style.display = 'none';
        editorEl.style.display = 'block';
        toggleBtn.textContent = 'HTML Source';
        showingHTML = false;
      }
    });
  }
}

// Publish action buttons
function initPublishButtons() {
  document.querySelectorAll('[data-action]').forEach(function(btn) {
    btn.addEventListener('click', function() {
      const actionInput = document.getElementById('publish-action');
      if (actionInput) actionInput.value = this.dataset.action;
    });
  });
}

// Alert auto-dismiss
function initAlerts() {
  document.querySelectorAll('.alert[data-auto-dismiss]').forEach(function(el) {
    setTimeout(function() { el.style.opacity = '0'; setTimeout(function() { el.remove(); }, 400); }, 4000);
  });
}

// Confirm delete
function confirmDelete(msg) {
  return confirm(msg || 'Are you sure you want to delete this? This cannot be undone.');
}

// Mobile sidebar toggle
function initSidebarToggle() {
  const toggle = document.getElementById('sidebar-toggle');
  const sidebar = document.querySelector('.cms-sidebar');
  if (toggle && sidebar) {
    toggle.addEventListener('click', function() { sidebar.classList.toggle('open'); });
  }
}

// Init on DOM ready
document.addEventListener('DOMContentLoaded', function() {
  initSlugGenerator();
  initCharCounters();
  initQuillEditor();
  initPublishButtons();
  initAlerts();
  initSidebarToggle();
});
