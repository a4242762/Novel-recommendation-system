$(function () {
    // console.log('加载js')

    $.ajax({
        url: '/App/classify_inovel/',
        type: 'GET',
        dataType: 'json',
        data: {
            'label': '体育',
            'page': '1',
        },
        success: function (data) {
            add_content(data);
            add_page(data);
            clickevent(data)
        }
    })

    function add_content(data) {
        $('#ul').empty();
        var content = data['体育']
        for (var i = 0; i < content.length; i++) {
            // 修正图片url
            var img = content[i]['inovel_cover'].replace('%3A', ':')
            var $li = $('<li class="li"><div><img src="' + img + '" class="img">' +
                '</div><div class="name"><h4>' + content[i]['inovel_name'] + '</h4></div></li>')

            // console.log(img)
            // console.log(content[i]['inovel_cover'])
            $li.appendTo($('#ul'))
        }
    }

    function add_page(data) {
        console.log('添加页码')
        $('#page').empty()

        var page_counts = data.page_count
        console.log(page_counts)
        if (page_counts > 6) {
            // console.log('多页码')
            var $before = $('<li class="page_guide"><div class="onbutton">首页</div></li>' +
                '            <li class="page_guide" id="target"><div class="onbutton">上一页</div></li>\n')
            $before.appendTo($('#page'))

            for (var i = 1; i < 6; i++) {
                var $li = $('<li class="page_guide"><div class="onbutton">' + i + '</div></li>')
                $li.appendTo($('#page'))
            }
            var $lis = $('<div class="page_guide">...</div>')
            $lis.appendTo($('#page'))
            var $liss = $('<li class="page_guide"><div class="onbutton">' + page_counts + '</div></li>')
            $liss.appendTo($('#page'))

            var $after = $('<li class="page_guide" ><div class="onbutton">下一页</div></li>' +
                '<li class="page_guide"><div class="onbutton">尾页</div></li>')
            $after.appendTo($('#page'))

            //设置上一页不可点击
            $('#target').addClass('hideclick')

        } else {
            // console.log('少页码')

            var $before1 = $('<li class="page_guide"><div class="onbutton">首页</div></li>' +
                '            <li class="page_guide" id="target"><div class="onbutton">上一页</div></li>\n')
            $before1.appendTo($('#page'))

            for (var j = 1; j < page_counts + 1; j++) {
                var $li1 = $('<li class="page_guide"><div class="onbutton">' + j + '</div></li>');
                $li1.appendTo($('#page'))
            }

            var $after1 = $('<li class="page_guide" ><div class="onbutton">下一页</div></li>' +
                '<li class="page_guide"><div class="onbutton">尾页</div></li>')
            $after1.appendTo($('#page'))

            //设置上一页不可点击
            $('#target').addClass('hideclick')

        }

    }

    function clickevent(data) {
        $('.onbutton').click(function () {
            var current = $(this)
            var page = $(this).text()
            var page_length = data.page_count

            // console.log('点击之前',click_before)

            // 获取当前页码并设置样式
            // console.log('更改样式');
            current.addClass('changecolor');
            $('.onbutton').not(current).removeClass('changecolor')

            if (page !== '1') {
                // 如果当前页不为第一页设置可点击
                $('#target').removeClass('hideclick')
            } else {
                $('#target').addClass('hideclick')
            }

            if(page === '首页'){
                page = 1
            }
            if(page === '尾页'){
                page = page_length
            }

            console.log('真实页码::::',page)
            $.ajax({
                url: '/App/classify_inovel/',
                type: 'GET',
                dataType: 'json',
                data: {
                    'label': '体育',
                    'page': page,
                },
            })
                .done(function (data) {
                    console.log('更改页面内容')
                    add_content(data);
                    // clickevent(data)
                    if (data.page_count > 6) {
                        changenum(page)
                    }
                })
        })
    }

    function changenum(data) {
        if(page>=5){
            for (var i=3;i>0;i--){
                $('.onbutton').eq(5-i).text(page-i)
            }
            $('.onbutton').eq(6).text('page+1')
        }
    }
});

