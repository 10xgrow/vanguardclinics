(function($, window, document, undefined) {
    "use strict";

    jQuery(document).ready(function($) {

        jQuery.fn.dmsmp_marker_html = function(options) {

                let map_obj = jQuery(options.wpgmp_map_selector).data("wpgmp_maps");

                map_obj.addon_create_marker = function() {

                    var map_obj = this;

                    if (map_obj.map_data.map_options.custom_url_filter != undefined && map_obj.map_data.map_options.custom_url_filter != '') {
                        $.each(map_obj.map_data.map_options.custom_url_filter, function(flt, flt_val) {

                            if ($('select[data-name="%' + flt + '%"]').length > 0) {
                                if ($('.categories_filter option[value="' + flt_val + '"]').length > 0) {
                                    $('select[data-name="%' + flt + '%"]').val(flt_val).trigger('change');
                                }

                            } else if ($('select[data-name="taxonomy=' + flt + '"]').length > 0) {
                                if ($('.categories_filter option[value="' + flt_val + '"]').length > 0) {
                                    $('select[data-name="taxonomy=' + flt + '"]').val(flt_val).trigger('change');
                                }

                            } else if ($('select[data-name="' + flt + '"]').length > 0) {
                                if ($('.categories_filter option[value="' + flt_val + '"]').length > 0) {
                                    $('select[data-name="' + flt + '"]').val(flt_val).trigger('change');
                                }

                            }



                        });
                    }

                }
                map_obj.addon_create_marker();
            },

            jQuery("div.wpgmp_map_container").each(function(index, element) {

                let wpgmp_map_selector = "#" + $(this).attr('rel');
                let wpgmp_layout_args = {
                    'wpgmp_map_selector': wpgmp_map_selector
                };
                jQuery(wpgmp_map_selector).dmsmp_marker_html(wpgmp_layout_args);

            });

    });
}(jQuery, window, document));