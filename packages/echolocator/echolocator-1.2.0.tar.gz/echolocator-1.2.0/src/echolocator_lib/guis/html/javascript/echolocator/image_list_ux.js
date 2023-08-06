// Class backing the actions ux.

class echolocator__ImageListUx extends echolocator__UxAutoUpdate {
    COOKIE_NAME = "IMAGE_LIST_UX";
    FETCH_IMAGE_LIST = "echolocator_guis::commands::fetch_image_list";
    EXPORT_TO_SOAKDB3 = "echolocator_guis::commands::export_to_soakdb3";
    EXPORT_TO_CSV = "echolocator_guis::commands::export_to_csv";

    #jquery_objects = {};
    #visit_filter = "undefined";
    #should_show_only_undecided = "undefined";

    constructor(runtime, plugin_link_name, $interaction_parent) {
        super(runtime);

        this.plugin_link_name = plugin_link_name;
        this.$interaction_parent = $interaction_parent;
        this.filename_rows = undefined;
    }

    // -------------------------------------------------------------
    // Activate things on the UX.

    activate() {
        super.activate()

        this.#jquery_objects.$div = $(".T_composed", this.$interaction_parent);
        this.#jquery_objects.$visit_filter = $(".T_visit_filter", this.$interaction_parent);
        this.#jquery_objects.$should_show_only_undecided = $(".T_should_show_only_undecided", this.$interaction_parent);
        this.#jquery_objects.$export_to_soakdb3_button = $(".T_export_to_soakdb3_button", this.$interaction_parent);
        this.#jquery_objects.$export_to_csv_button = $(".T_export_to_csv_button", this.$interaction_parent);

        var that = this;
        this.#jquery_objects.$visit_filter.change(
            function (jquery_event_object) {
                that._handle_filter_change(jquery_event_object);
            });

        this.#jquery_objects.$should_show_only_undecided.change(
            function (jquery_event_object) {
                that._handle_filter_change(jquery_event_object);
            });

        this.#jquery_objects.$export_to_soakdb3_button.click(
            function (jquery_event_object) {
                that._handle_export_to_soakdb3_clicked(jquery_event_object);
            });

        this.#jquery_objects.$export_to_csv_button.click(
            function (jquery_event_object) {
                that._handle_export_to_csv_clicked(jquery_event_object);
            });

    } // end method

    // -------------------------------------------------------------
    // Request update from database.

    request_update() {

        var json_object = {}
        json_object[this.COMMAND] = this.FETCH_IMAGE_LIST;
        json_object[this.ENABLE_COOKIES] = [this.COOKIE_NAME];

        json_object["visit_filter"] = this.#visit_filter;
        json_object["should_show_only_undecided"] = this.#should_show_only_undecided;

        this.send(json_object);

    } // end method

    // -------------------------------------------------------------
    // Handle the response when it comes.

    handle_ajax_success(response, status, jqXHR) {
        var F = "echolocator__ImageListUx::_handle_ajax_success";

        // Let the base class have a look at the response.
        super.handle_ajax_success(response, status, jqXHR);

        var filters = response.filters;
        if (filters !== undefined) {
            var t;

            t = filters["visit_filter"];
            if (t === undefined)
                t = "";
            this.#jquery_objects.$visit_filter.val(t);

            t = filters["should_show_only_undecided"];
            if (t === undefined)
                t = false;
            this.#jquery_objects.$should_show_only_undecided.prop("checked", t);
        }

        var html = response.html;

        if (html !== undefined) {
            this.#jquery_objects.$div.html(html);
            // Attach events to all the individual job links in the "recent jobs" grid.
            this._attach_links();
        }
    }

    // -------------------------------------------------------------

    _handle_filter_change(jquery_event_object) {
        var F = "echolocator__ImageListUx::_handle_filter_change"

        this.#visit_filter = this.#jquery_objects.$visit_filter.val()
        this.#should_show_only_undecided = this.#jquery_objects.$should_show_only_undecided.prop("checked")
        this.request_update()

    } // end method

    // -------------------------------------------------------------

    _handle_export_to_soakdb3_clicked(jquery_event_object) {
        var F = "echolocator__ImageListUx::_handle_export_to_soakdb3_clicked"

        this.#visit_filter = this.#jquery_objects.$visit_filter.val()

        // Enable no cookie for this request.
        var json_object = {}
        json_object[this.COMMAND] = this.EXPORT_TO_SOAKDB3;

        json_object["visit_filter"] = this.#visit_filter;

        this.send(json_object);

    } // end method

    // -------------------------------------------------------------

    _handle_export_to_csv_clicked(jquery_event_object) {
        var F = "echolocator__ImageListUx::_handle_export_to_csv_clicked"

        this.#visit_filter = this.#jquery_objects.$visit_filter.val()

        // Enable no cookie for this request.
        var json_object = {}
        json_object[this.COMMAND] = this.EXPORT_TO_CSV;

        json_object["visit_filter"] = this.#visit_filter;

        this.send(json_object);

    } // end method

    // -------------------------------------------------------------

    _handle_filename_clicked(jquery_event_object) {

        var $filename_row = $(jquery_event_object.target);

        // User clicked on a cell within the row?
        if ($filename_row.get(0).tagName == "TD")
            $filename_row = $filename_row.parent();

        // The row has the attribute holding the crystal well of this row.
        var crystal_well_uuid = $filename_row.attr("crystal_well_uuid");

        this._load_image(crystal_well_uuid);

        this.set_and_render_auto_update(false);

    } // end method

    // -------------------------------------------------------------

    _load_image(crystal_well_uuid) {
        var F = "echolocator__ImageListUx::_load_image";

        console.log(F + ": loading image for crystal_well_uuid " + crystal_well_uuid)

        //     this.$filename_rows.removeClass("T_picked");
        //     image_info.$filename_row.addClass("T_picked");

        // Trigger an event that the index.js will use to coordinate cross-widget changes.
        var custom_event = new CustomEvent(echolocator__Events_IMAGE_PICKED_EVENT,
            {
                detail: { crystal_well_uuid: crystal_well_uuid }
            });

        this.dispatchEvent(custom_event);

    } // end method

    // -------------------------------------------------------------
    // Attach events to all the individual job links in the grid.

    _attach_links() {
        var F = "echolocator__ImageListUx::_attach_links";

        var that = this;

        this.$filename_rows = $(".T_image_list TR", this.$interaction_parent);
        this.$filename_rows.click(function (jquery_event_object) { that._handle_filename_clicked(jquery_event_object); })

    }

}
