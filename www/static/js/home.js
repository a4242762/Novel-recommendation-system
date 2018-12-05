// $(function() {
// 	var swiper = new Swiper('.swiper-container', {
// 		pagination: '.swiper-pagination',
// 		paginationClickable: true,
// 		nextButton: '.swiper-button-next',
// 		prevButton: '.swiper-button-prev',
// 		spaceBetween: 30,
// 		effect: 'fade',
//         loop: true,
//         // 如果需要分页器
//         autoplay:4000
// 	});
// 	$('#icon').click(function () {
// 		window.open('/Movie/upload_img', target='_self',)
//     });

// $('#change').hover(function () {
// 	console.log(1)
// 	var num = $(this).attr('num')
// 	var movie_content = $(this).attr('movie_content')
// 	$.getJSON('/Movie/collect',{'num':num,'movie_content':movie_content},function (data) {
// 		if(data['status']=='200'){
// 			count = $(this).next().text()
// 			console.log($(this).next())
// 			$(this).next().html(count+1)
// 			$(this).attr('color','red')
// 		}
// 	})
// },function () {
// 	count = $(this).next().text()
// 	console.log($(this).next())
// 	$(this).next().html(count-1)
// 	$(this).attr('color','white')
// })

$(function () {
    jQuery(document).ready(function ($) {
        $(".scroll").click(function (event) {
            event.preventDefault();
            $('html,body').animate({scrollTop: $(this.hash).offset().top}, 1000);
        });
    });
//<![CDATA[
    $(document).ready(function () {

        $("#jquery_jplayer_1").jPlayer({
            ready: function () {
                $(this).jPlayer("setMedia", {
                    title: "Finding Nemo Teaser",
                    m4v: "http://www.jplayer.org/video/m4v/Finding_Nemo_Teaser.m4v",
                    poster: "images/cake.jpg"

                });
            },
            swfPath: "../../dist/jplayer",
            supplied: "m4v",
            size: {
                width: "100%",
                height: "275px",
                cssClass: "jp-video-360p"
            },
            useStateClassSkin: true,
            autoBlur: false,
            smoothPlayBar: true,
            keyEnabled: true,
            remainingDuration: true,
            toggleDuration: true
        });
    });
//]]>

    $(document).ready(function () {
        $('.popup-with-zoom-anim').magnificPopup({
            type: 'inline',
            fixedContentPos: false,
            fixedBgPos: true,
            overflowY: 'auto',
            closeBtnInside: true,
            preloader: false,
            midClick: true,
            removalDelay: 300,
            mainClass: 'my-mfp-zoom-in'
        });

    });

    $(window).load(function () {
        $("#flexiselDemo1").flexisel({
            visibleItems: 4,
            animationSpeed: 1000,
            autoPlay: false,
            autoPlaySpeed: 3000,
            pauseOnHover: true,
            enableResponsiveBreakpoints: true,
            responsiveBreakpoints: {
                portrait: {
                    changePoint: 480,
                    visibleItems: 2
                },
                landscape: {
                    changePoint: 640,
                    visibleItems: 3
                },
                tablet: {
                    changePoint: 768,
                    visibleItems: 3
                }
            }
        });

    });
    //  导航栏提示
            $('.find').keyup(function () {
            var input_val = $(this).val()
                // console.log('进入这里')
            $.ajax({
                        url: '/App/word_tip/',
                        type: 'get',
                        async:true,
                        dataType: 'jsonp',
                        data: {word:input_val}
                    })
                        .done(function (data) {
                            // console.log('接收到数据::::',data);
                            // console.log(JSON.stringify(data))

                            if(JSON.stringify(data) !== '{}'){
                                var aData = data[input_val];
                                console.log(aData)

                                $('.tip').empty();
                                for(var i=0;i<aData.length;i++){
                                    var $li = $('<div>'+aData[i]+'</div>');
                                    $li.appendTo($('.tip'))
                             }
                            }
                        })
                });


    $(document).ready(function () {
        /*
        var defaults = {
              containerID: 'toTop', // fading element id
            containerHoverID: 'toTopHover', // fading element hover id
            scrollSpeed: 1200,
            easingType: 'linear'
         };
        */

        $().UItoTop({easingType: 'easeOutQuart'});

    });

    $('#find_click').click(function () {
        // 获取输入框内的内容
        var input_text = $('.find').val()
        window.location.href = '../../templates/html/main/find_page.html?word='+input_text
    })

});


