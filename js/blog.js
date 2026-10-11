(function () {
  'use strict';

  var listing = document.querySelector('.blog-page-section');
  var cards = listing ? Array.prototype.slice.call(listing.querySelectorAll('.blog-card')) : [];
  var forms = document.querySelectorAll('.blog-search-form');
  var categoryLinks = document.querySelectorAll('[data-category-filter]');
  var resultMessage = document.getElementById('blog-results-message');
  var params;
  var selectedCategory;
  var searchQuery;

  if (!listing || !cards.length) {
    return;
  }

  params = new URLSearchParams(window.location.search);
  selectedCategory = params.get('category') || 'all';
  searchQuery = (params.get('q') || '').trim();

  function updateUrl(category, query) {
    var nextParams = new URLSearchParams();
    if (category && category !== 'all') {
      nextParams.set('category', category);
    }
    if (query) {
      nextParams.set('q', query);
    }
    window.history.replaceState({}, '', 'blog.html' + (nextParams.toString() ? '?' + nextParams.toString() : ''));
  }

  function render() {
    var visibleCount = 0;
    var normalizedQuery = searchQuery.toLowerCase();

    cards.forEach(function (card) {
      var categories = (card.getAttribute('data-categories') || '').split(/\s+/);
      var searchableText = (card.getAttribute('data-search') || card.textContent).toLowerCase();
      var categoryMatches = selectedCategory === 'all' || categories.indexOf(selectedCategory) !== -1;
      var queryMatches = !normalizedQuery || searchableText.indexOf(normalizedQuery) !== -1;
      var visible = categoryMatches && queryMatches;

      card.style.display = visible ? '' : 'none';
      if (visible) {
        visibleCount += 1;
      }
    });

    categoryLinks.forEach(function (link) {
      var active = link.getAttribute('data-category-filter') === selectedCategory;
      link.classList.toggle('active', active);
      link.setAttribute('aria-current', active ? 'page' : 'false');
    });

    if (resultMessage) {
      if (!visibleCount) {
        resultMessage.textContent = searchQuery
          ? 'No blogs found matching your search.'
          : 'No blogs found in this category yet.';
        resultMessage.hidden = false;
      } else {
        resultMessage.textContent = visibleCount + (visibleCount === 1 ? ' blog found.' : ' blogs found.');
        resultMessage.hidden = false;
      }
    }
  }

  forms.forEach(function (form) {
    form.addEventListener('submit', function (event) {
      var input = form.querySelector('input[name="q"]');
      event.preventDefault();
      searchQuery = input ? input.value.trim() : '';
      updateUrl(selectedCategory, searchQuery);
      render();
    });
  });

  categoryLinks.forEach(function (link) {
    link.addEventListener('click', function (event) {
      var category = link.getAttribute('data-category-filter');
      if (!category) {
        return;
      }
      event.preventDefault();
      selectedCategory = category;
      updateUrl(selectedCategory, searchQuery);
      render();
    });
  });

  forms.forEach(function (form) {
    var input = form.querySelector('input[name="q"]');
    if (input) {
      input.value = searchQuery;
    }
  });

  render();
}());
