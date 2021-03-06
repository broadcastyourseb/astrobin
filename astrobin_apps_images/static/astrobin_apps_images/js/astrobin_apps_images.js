$(document).ready(function() {
    /* TODO: make this a jQuery plugin */
    window.loadAstroBinImages = function(fragment) {
        var tries = {};

        $(fragment).find('img.astrobin-image').each(function(index) {
            var $img = $(this),
                random_timeout = Math.floor(Math.random() * 100) + 100, // 100-200 ms
                id = $img.data('id'),
                revision = $img.data('revision'),
                alias = $img.data('alias'),
                url = $img.data('get-thumb-url'),
                loaded = $img.data('loaded'),
                key = id + '.' + revision + '.' + alias;

            function load() {
                if (!loaded && url !== "") {
                    if (tries[key] === undefined) {
                        tries[key] = 0;
                    }

                    if (tries[key] >= 10) {
                        return;
                    }

                    $.ajax({
                        dataType: 'json',
                        timeout: 0,
                        cache: true,
                        url: url,
                        success: function(data, status, request) {
                            tries[key] += 1;
                            if (data.url === null) {
                                setTimeout(function() {
                                    load();
                                }, random_timeout * Math.pow(2, tries[key]));
                                return;
                            }

                            var $img =
                                $('img.astrobin-image[data-id=' + data.id +
                                '][data-alias=' + data.alias +
                                '][data-revision=' + data.revision +
                                ']');

                            $img
                                .attr('src', data.url)
                                .attr('data-loaded', 'true');

                            delete tries[key];
                        }
                    });
                }
            }

            setTimeout(function() {
                load();
            }, random_timeout);
        });
    };

    window.loadAstroBinImages($('body'));
});
