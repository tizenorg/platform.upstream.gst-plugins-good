plugin_LTLIBRARIES = libgstvideomixer.la

ORC_SOURCE=videomixerorc

include $(top_srcdir)/common/orc.mak

libgstvideomixer_la_SOURCES = \
	blend.c \
	videoconvert.c \
	gstcms.c \
	videomixer2.c

nodist_libgstvideomixer_la_SOURCES = $(ORC_NODIST_SOURCES)
libgstvideomixer_la_CFLAGS = $(GST_PLUGINS_BASE_CFLAGS) \
	$(GST_BASE_CFLAGS) $(GST_CFLAGS) $(ORC_CFLAGS)
libgstvideomixer_la_LIBADD = $(GST_PLUGINS_BASE_LIBS) \
	-lgstvideo-@GST_API_VERSION@ \
	$(GST_BASE_LIBS) $(GST_LIBS) $(ORC_LIBS) $(LIBM)
libgstvideomixer_la_LDFLAGS = $(GST_PLUGIN_LDFLAGS)
libgstvideomixer_la_LIBTOOLFLAGS = $(GST_PLUGIN_LIBTOOLFLAGS)

# headers we need but don't want installed
noinst_HEADERS = \
	blend.h \
	videomixer2.h \
	videomixer2pad.h \
	videoconvert.h \
	gstcms.h

Android.mk: Makefile.am $(BUILT_SOURCES)
	androgenizer \
	-:PROJECT libgstvideomixer -:SHARED libgstvideomixer \
	 -:TAGS eng debug \
         -:REL_TOP $(top_srcdir) -:ABS_TOP $(abs_top_srcdir) \
	 -:SOURCES $(libgstvideomixer_la_SOURCES) \
	 	   $(nodist_libgstvideomixer_la_SOURCES) \
	 -:CFLAGS $(DEFS) $(DEFAULT_INCLUDES) $(libgstvideomixer_la_CFLAGS) \
	 -:LDFLAGS $(libgstvideomixer_la_LDFLAGS) \
	           $(libgstvideomixer_la_LIBADD) \
	           -ldl \
	 -:PASSTHROUGH LOCAL_ARM_MODE:=arm \
		       LOCAL_MODULE_PATH:='$$(TARGET_OUT)/lib/gstreamer-0.10' \
	> $@
