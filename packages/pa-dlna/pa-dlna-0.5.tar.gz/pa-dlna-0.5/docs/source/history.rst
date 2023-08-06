Release history
===============

Version 0.5
  - Log a warning upon an empty body in the HTTP response from a DLNA device.
  - UPnP discovery is triggered by NICs [#]_ state changes.
  - Add the ``--ip-addresses``, ``-a`` command line argument.
  - Fix changing the ``args`` encoder option is ignored.

Version 0.4
  - ``sample_format`` is a new encoder configuration option.
  - The encoders sample format is ``s16le`` except for the ``audio/l16``
    encoder.
  - The encoder command line is now updated with ``pa-dlna.conf`` user
    configuration.
  - Fix the parec command line length keeps increasing at each new track when
    the encoder is set to track metadata.
  - Fix failing to start a new stream session while the device is still playing
    when the encoder is set to not track metadata.
  - Fix ``pa-dlna`` hangs when one types <Control-S> in the terminal where the
    program has been started.

Version 0.3
  - The test coverage of ``pa-dlna`` is 95%.
  - UPnPControlPoint supports now the context manager protocol, not the
    asynchronous one.
  - UPnPControlPoint.get_notification() returns now QUEUE_CLOSED upon closing.
  - Fix some fatal errors on startup that were silent.
    Here are the  missing error messages that are now printed when one of those
    fatal errors occurs:

    + Error: No encoder is available.
    + Error: The pulseaudio 'parec' program cannot be found.
  - Fix curl: (18) transfer closed with outstanding read data remaining.
  - Fix a race condition upon the reception of an SSDP msearch response that
    occurs just after the reception of an SSDP notification and while the
    instantiation of the root device is not yet complete.
  - Failure to set SSDP multicast membership is reported only once.

Version 0.2
  - Test coverage of the UPnP library is 94%.
  - Fix unknown UPnPXMLFatalError exception.
  - The ``description`` commands of ``upnp-cmd`` don't prefix tags with a
    namespace.
  - Fix the ``description`` commands of ``upnp-cmd`` when run with Python 3.8.
  - Fix IndexError exception raised upon OSError in
    network.Notify.manage_membership().
  - Fix removing multicast membership when the socket is closed.
  - Don't print a stack traceback upon error parsing the configuration file.
  - Abort on error setting the file logging handler with ``--logfile PATH``.

Version 0.1
  - Publish the project on PyPi.

.. rubric:: Footnotes

.. [#] Network Interface Controller.
