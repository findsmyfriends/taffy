$('#like').click(
    function (e) {
        e.preventDefault()
        var this_ = $(this)
        var likedUrl = this_.attr("data-url")
        var likeIcon = $('#like-icon')
        var likeCount = $('#likes_count')

        $.ajax({
            method: "GET",
            url: likedUrl,
            success: function (data) {
                if (data.liked) {
                    likeIcon.removeClass();
                    likeIcon.addClass('fas fa-heart fa-3x');
                    likeCount.text(data.likes_count)
                    
                } else {
                    likeIcon.removeClass();
                    likeIcon.addClass('far fa-heart fa-3x');
                    likeCount.text(data.likes_count)
                }
            },
            error: function (data) {
                console.log("error")
                console.log(data)
            }
        })
        if (likeIcon.attr('class').includes('far')) {
            likeIcon.toggleClass('fas')
        } else {
            likeIcon.toggleClass('far')
        }
    })


    var tinderContainer = document.querySelector('.tinder');
    var allCards = document.querySelectorAll('.tinder--card');
    var nope = document.getElementById('nope');
    var love = document.getElementById('love');
    
    function initCards(card, index) {
      var newCards = document.querySelectorAll('.tinder--card:not(.removed)');
    
      newCards.forEach(function (card, index) {
        card.style.zIndex = allCards.length - index;
        card.style.transform = 'scale(' + (20 - index) / 20 + ') translateY(-' + 30 * index + 'px)';
        card.style.opacity = (10 - index) / 10;
      });
      
      tinderContainer.classList.add('loaded');
    }
    
    initCards();
    
    allCards.forEach(function (el) {
      var hammertime = new Hammer(el);
    
      hammertime.on('pan', function (event) {
        el.classList.add('moving');
      });
    
      hammertime.on('pan', function (event) {
        if (event.deltaX === 0) return;
        if (event.center.x === 0 && event.center.y === 0) return;
    
        tinderContainer.classList.toggle('tinder_love', event.deltaX > 0);
        tinderContainer.classList.toggle('tinder_nope', event.deltaX < 0);
    
        var xMulti = event.deltaX * 0.03;
        var yMulti = event.deltaY / 80;
        var rotate = xMulti * yMulti;
    
        event.target.style.transform = 'translate(' + event.deltaX + 'px, ' + event.deltaY + 'px) rotate(' + rotate + 'deg)';
      });
    
      hammertime.on('panend', function (event) {
        el.classList.remove('moving');
        tinderContainer.classList.remove('tinder_love');
        tinderContainer.classList.remove('tinder_nope');
    
        var moveOutWidth = document.body.clientWidth;
        var keep = Math.abs(event.deltaX) < 80 || Math.abs(event.velocityX) < 0.5;
    
        event.target.classList.toggle('removed', !keep);
    
        if (keep) {
          event.target.style.transform = '';
        } else {
          var endX = Math.max(Math.abs(event.velocityX) * moveOutWidth, moveOutWidth);
          var toX = event.deltaX > 0 ? endX : -endX;
          var endY = Math.abs(event.velocityY) * moveOutWidth;
          var toY = event.deltaY > 0 ? endY : -endY;
          var xMulti = event.deltaX * 0.03;
          var yMulti = event.deltaY / 80;
          var rotate = xMulti * yMulti;
    
          event.target.style.transform = 'translate(' + toX + 'px, ' + (toY + event.deltaY) + 'px) rotate(' + rotate + 'deg)';
          initCards();
        }
      });
    });
    
    function createButtonListener(love) {
      return function (event) {
        var cards = document.querySelectorAll('.tinder--card:not(.removed)');
        var moveOutWidth = document.body.clientWidth * 1.5;
    
        if (!cards.length) return false;
    
        var card = cards[0];
    
        card.classList.add('removed');
    
        if (love) {
          card.style.transform = 'translate(' + moveOutWidth + 'px, -100px) rotate(-30deg)';
        } else {
          card.style.transform = 'translate(-' + moveOutWidth + 'px, -100px) rotate(30deg)';
        }
    
        initCards();
    
        event.preventDefault();
      };
    }
    
    var nopeListener = createButtonListener(false);
    var loveListener = createButtonListener(true);
    
    nope.addEventListener('click', nopeListener);
    love.addEventListener('click', loveListener);
    