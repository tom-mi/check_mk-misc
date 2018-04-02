register_notification_parameters("telegram", Dictionary(
    optional_keys = [],
    elements = [
        ("token", TextAscii(
            title = _("Token"),
            help = _('Telegram Bot Token. '
                     'See the <a href="https://core.telegram.org/bots/api">Telegram Bot API</a> '
                     'for how to get one'),
            size = 64,
            allow_empty = False,
        )),
        ('chat_id', TextAscii(
            title = _('Chat Id'),
            help = _('Chat the notifications shall be sent to'),
            size = 40,
            allow_empty = False,
        )),
        ('url_prefix', TextAscii(
              title = _('URL prefix for links to Check_MK'),
              help = _('Specify an absolute URL including '
                       'the <tt>.../check_mk/</tt>'),
              regex = '^(http|https)://.*/check_mk/$',
              regex_error = _('The URL must begin with <tt>http</tt> or '
                              '<tt>https</tt> and end with <tt>/check_mk/</tt>.'),
              size = 64,
              default_value = 'http://' + socket.getfqdn() + '/' + (
                      config.omd_site() and config.omd_site() + '/' or '') + 'check_mk/',
        )),
    ]
))
