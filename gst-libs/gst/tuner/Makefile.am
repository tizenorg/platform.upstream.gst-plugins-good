lib_LTLIBRARIES = libgsttuner-@GST_API_VERSION@.la

libgsttuner_@GST_API_VERSION@_la_SOURCES = \
	tuner.c  \
	tunerchannel.c \
	tunernorm.c


libgsttuner_@GST_API_VERSION@includedir = \
	$(includedir)/gstreamer-@GST_API_VERSION@/gst/tuner

libgsttuner_@GST_API_VERSION@include_HEADERS = \
	tuner.h \
	tunerchannel.h \
	tunernorm.h


libgsttuner_@GST_API_VERSION@_la_CFLAGS = \
	$(GST_PLUGINS_GOOD_CFLAGS) \
	-DGST_USE_UNSTABLE_API \
	$(GST_CFLAGS)

libgsttuner_@GST_API_VERSION@_la_LIBADD = \
	$(GST_BASE_LIBS) \
	$(GST_LIBS)

libgsttuner_@GST_API_VERSION@_la_LDFLAGS = \
	$(GST_LIB_LDFLAGS) \
	$(GST_ALL_LDFLAGS) \
	$(GST_LT_LDFLAGS)

glib_enum_headers= \
	tuner.h \
	tunerchannel.h \
	tunernorm.h

glib_enum_define=GST_TUNER
glib_gen_prefix=gst_tuner
glib_gen_basename=gsttuner


if HAVE_INTROSPECTION
BUILT_GIRSOURCES = GstTuner-@GST_API_VERSION@.gir

gir_headers=$(patsubst %,$(srcdir)/%, $(libgsttuner_@GST_API_VERSION@include_HEADERS))
gir_headers+=$(patsubst %,$(builddir)/%, $(built_headers))
gir_sources=$(patsubst %,$(srcdir)/%, $(libgsttuner_@GST_API_VERSION@_la_SOURCES))
gir_sources+=$(patsubst %,$(builddir)/%, $(built_sources))

GstTuner-@GST_API_VERSION@.gir: $(INTROSPECTION_SCANNER) libgsttuner-@GST_API_VERSION@.la
	$(AM_V_GEN)PKG_CONFIG_PATH="$(GST_PKG_CONFIG_PATH)" \
		GST_PLUGIN_SYSTEM_PATH_1_0="" GST_PLUGIN_PATH_1_0="" GST_REGISTRY_UPDATE=no \
		$(INTROSPECTION_SCANNER) -v --namespace GstTuner \
		--nsversion=@GST_API_VERSION@ \
		--identifier-prefix=GstTuner \
		--symbol-prefix=gst_tuner \
		--symbol-prefix=gst \
		--warn-all -v \
		--c-include "gst/tuner/tuner.h" \
		-I$(top_srcdir)/gst-libs \
		-I$(top_builddir)/gst-libs \
		--add-include-path=`PKG_CONFIG_PATH="$(GST_PKG_CONFIG_PATH)" $(PKG_CONFIG) --variable=girdir gstreamer-@GST_API_VERSION@` \
		--add-include-path=`PKG_CONFIG_PATH="$(GST_PKG_CONFIG_PATH)" $(PKG_CONFIG) --variable=girdir gstreamer-video-@GST_API_VERSION@` \
		--library=libgsttuner-@GST_API_VERSION@.la \
		--include=Gst-@GST_API_VERSION@ \
		--libtool="$(top_builddir)/libtool" \
		--pkg gstreamer-@GST_API_VERSION@ \
		--pkg gstreamer-video-@GST_API_VERSION@ \
		--pkg-export gstreamer-tuner-@GST_API_VERSION@ \
		--add-init-section="gst_init(NULL,NULL);" \
		-DGST_USE_UNSTABLE_API \
		--output $@ \
		$(gir_headers) \
		$(gir_sources)

# INTROSPECTION_GIRDIR/INTROSPECTION_TYPELIBDIR aren't the right place to
# install anything - we need to install inside our prefix.
girdir = $(datadir)/gir-1.0
gir_DATA = $(BUILT_GIRSOURCES)

typelibsdir = $(libdir)/girepository-1.0/

typelibs_DATA = $(BUILT_GIRSOURCES:.gir=.typelib)

%.typelib: %.gir $(INTROSPECTION_COMPILER)
	$(AM_V_GEN)PKG_CONFIG_PATH="$(GST_PKG_CONFIG_PATH)" \
		$(INTROSPECTION_COMPILER) \
		--includedir=$(srcdir) \
		--includedir=$(builddir) \
		--includedir=`PKG_CONFIG_PATH="$(GST_PKG_CONFIG_PATH)" $(PKG_CONFIG) --variable=girdir gstreamer-@GST_API_VERSION@` \
		--includedir=`PKG_CONFIG_PATH="$(GST_PKG_CONFIG_PATH)" $(PKG_CONFIG) --variable=girdir gstreamer-base-@GST_API_VERSION@` \
		$(INTROSPECTION_COMPILER_OPTS) $< -o $(@F)

CLEANFILES = $(BUILT_GIRSOURCES) $(typelibs_DATA)
endif

Android.mk:  $(BUILT_SOURCES) Makefile.am
	androgenizer -:PROJECT libgsttuner -:STATIC libgsttuner-@GST_API_VERSION@ \
	 -:TAGS eng debug \
         -:REL_TOP $(top_srcdir) -:ABS_TOP $(abs_top_srcdir) \
	 -:SOURCES $(libgsttuner_@GST_API_VERSION@_la_SOURCES) \
         $(built_sources) \
	 -:CFLAGS $(DEFS) $(libgsttuner_@GST_API_VERSION@_la_CFLAGS) \
	 -:LDFLAGS $(libgsttuner_@GST_API_VERSION@_la_LDFLAGS) \
	           $(libgsttuner@GST_API_VERSION@_la_LIBADD) \
	           -ldl \
	 -:HEADER_TARGET gstreamer-@GST_API_VERSION@/gst/tuner \
	 -:HEADERS $(libgsttunerinclude_HEADERS) \
         $(built_headers) \
	 -:PASSTHROUGH LOCAL_ARM_MODE:=arm \
	> $@

include $(top_srcdir)/common/gst-glib-gen.mak
