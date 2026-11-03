(function () {
  'use strict';

  var shareContainers = document.querySelectorAll('[data-blog-share]');
  var cardButtons = document.querySelectorAll('[data-share-card]');
  var shareTitle = document.querySelector('meta[property="og:title"]');
  var shareDescription = document.querySelector('meta[property="og:description"]');
  var canonicalLink = document.querySelector('link[rel="canonical"]');
  var title = shareTitle ? shareTitle.getAttribute('content') : document.title;
  var description = shareDescription ? shareDescription.getAttribute('content') : '';
  var pageUrl = canonicalLink ? canonicalLink.getAttribute('href') : window.location.href.split('#')[0];

  function openShareWindow(url) {
    window.open(url, '_blank', 'noopener,noreferrer');
  }

  function createButton(label, icon, className, handler) {
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'blog-share-button ' + className;
    button.setAttribute('aria-label', label);
    button.innerHTML = '<span class="fa ' + icon + '" aria-hidden="true"></span><span class="blog-share-label">' + label + '</span>';
    button.addEventListener('click', handler);
    return button;
  }

  function copyLink(button) {
    var showStatus = function (label) {
      var originalLabel = button.getAttribute('aria-label');
      button.setAttribute('aria-label', label);
      button.querySelector('.blog-share-label').textContent = label === 'Link copied successfully' ? 'Copied' : 'Copy failed';
      window.setTimeout(function () {
        button.setAttribute('aria-label', originalLabel);
        button.querySelector('.blog-share-label').textContent = 'Copy link';
      }, 2200);
    };
    var confirmation = function () {
      showStatus('Link copied successfully');
    };

    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(pageUrl).then(confirmation).catch(function () {
        fallbackCopy(confirmation, function () {
          showStatus('Unable to copy link');
        });
      });
    } else {
      fallbackCopy(confirmation, function () {
        showStatus('Unable to copy link');
      });
    }
  }

  function fallbackCopy(onSuccess, onFailure) {
    var input = document.createElement('textarea');
    input.value = pageUrl;
    input.setAttribute('readonly', '');
    input.style.position = 'fixed';
    input.style.opacity = '0';
    document.body.appendChild(input);
    input.select();
    try {
      if (document.execCommand('copy')) {
        onSuccess();
      } else {
        onFailure();
      }
    } finally {
      document.body.removeChild(input);
    }
  }

  function appendShareButtons(container) {
    var encodedUrl = encodeURIComponent(pageUrl);
    var encodedTitle = encodeURIComponent(title);
    var encodedText = encodeURIComponent(title + ' - ' + pageUrl);

    container.appendChild(createButton('Facebook', 'fa-facebook', 'blog-share-facebook', function () {
      openShareWindow('https://www.facebook.com/sharer/sharer.php?u=' + encodedUrl);
    }));
    container.appendChild(createButton('LinkedIn', 'fa-linkedin', 'blog-share-linkedin', function () {
      openShareWindow('https://www.linkedin.com/sharing/share-offsite/?url=' + encodedUrl);
    }));
    container.appendChild(createButton('X (Twitter)', 'fa-twitter', 'blog-share-twitter', function () {
      openShareWindow('https://twitter.com/intent/tweet?url=' + encodedUrl + '&text=' + encodedTitle);
    }));
    container.appendChild(createButton('WhatsApp', 'fa-whatsapp', 'blog-share-whatsapp', function () {
      openShareWindow('https://api.whatsapp.com/send?text=' + encodedText);
    }));
    container.appendChild(createButton('Copy link', 'fa-link', 'blog-share-copy', function (event) {
      copyLink(event.currentTarget);
    }));

    if (navigator.share) {
      container.appendChild(createButton('Share', 'fa-share-alt', 'blog-share-native', function () {
        navigator.share({
          title: title,
          text: description,
          url: pageUrl
        }).catch(function (error) {
          if (error.name !== 'AbortError') {
            console.error('Native sharing failed:', error);
          }
        });
      }));
    }
  }

  Array.prototype.forEach.call(shareContainers, appendShareButtons);

  Array.prototype.forEach.call(cardButtons, function (button) {
    button.addEventListener('click', function () {
      var url = button.getAttribute('data-share-url');
      var cardTitle = button.getAttribute('data-share-title');
      if (navigator.share) {
        navigator.share({ title: cardTitle, text: cardTitle, url: url }).catch(function (error) {
          if (error.name !== 'AbortError') {
            console.error('Native sharing failed:', error);
          }
        });
      } else {
        openShareWindow('https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(url));
      }
    });
  });
}());
