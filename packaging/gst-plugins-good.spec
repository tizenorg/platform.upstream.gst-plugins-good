%bcond_with x
%define gst_branch 1.0

Name:           gst-plugins-good
Version:        1.6.1
Release:        3
License:        LGPL-2.1+
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Url:            http://gstreamer.freedesktop.org/
Group:          Multimedia/Framework
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz
Source100:      common.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  libjpeg-devel
BuildRequires:  orc >= 0.4.16
BuildRequires:  python
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gudev-1.0) >= 143
##BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.9
# TODO find where process.h comes from, not kernel-devel and not wxWidgets so far.
%if %{with x}
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
# used by libgstvideo4linux2.so
BuildRequires:  pkgconfig(xv)
%endif

BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(vconf)
Requires:       gst-plugins-base >= 1.0.0
Requires:       gstreamer >= 1.0.5

%description
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package extra
Summary:        Complementary plugins for %{name}
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Enhances:       gst-plugins-good

%description extra
This package provides complementary plugins for
%{name}.

%prep
%setup -q -n gst-plugins-good-%{version}
%setup -q -T -D -a 100

%build
# FIXME:
# warning: failed to load external entity "xml/element-v4l2src-details.xml"
# warning: failed to load external entity "xml/plugin-video4linux2.xml"
export V=1
NOCONFIGURE=1 ./autogen.sh
export CFLAGS+=" -DGST_EXT_V4L2SRC_MODIFIED\
		-DGST_EXT_WAVPARSE_MODIFICATION\
		-DGST_EXT_MP3PARSE_MODIFICATION\
		-DGST_EXT_AACPARSE_MODIFICATION"
%configure\
%if ! 0%{?ENABLE_AALIB}
	--disable-aalib\
%endif
	--disable-gtk-doc\
	--with-gtk=3.0\
	--disable-monoscope\
	--disable-y4m\
	--disable-taglib\
	--disable-wavpack\
	--enable-experimental\
	--disable-effectv
make %{?_smp_mflags} CFLAGS+="-Wno-error" CXXFLAGS+="-Wno-error"

%install
%make_install
%find_lang %{name}-%{gst_branch}

%lang_package -f %{name}-%{gst_branch}

%files
%manifest %{name}.manifest
%defattr(-, root, root)
%license COPYING
%{_libdir}/gstreamer-%{gst_branch}/libgstalaw.so
%{_libdir}/gstreamer-%{gst_branch}/libgstalpha.so
%{_libdir}/gstreamer-%{gst_branch}/libgstalphacolor.so
%{_libdir}/gstreamer-%{gst_branch}/libgstapetag.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiofx.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudioparsers.so
%{_libdir}/gstreamer-%{gst_branch}/libgstauparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstautodetect.so
%{_libdir}/gstreamer-%{gst_branch}/libgstavi.so
# Not yet ported
%{_libdir}/gstreamer-%{gst_branch}/libgstcutter.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdebug.so
# Not yet ported
%{_libdir}/gstreamer-%{gst_branch}/libgstdeinterlace.so
#%{_libdir}/gstreamer-%{gst_branch}/libgsteffectv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstequalizer.so
%{_datadir}/gstreamer-%{gst_branch}/presets/GstIirEqualizer10Bands.prs
%{_datadir}/gstreamer-%{gst_branch}/presets/GstIirEqualizer3Bands.prs
#%{_datadir}/gstreamer-%{gst_branch}/presets/GstVP8Enc.prs
%{_libdir}/gstreamer-%{gst_branch}/libgstflv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstflxdec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgoom.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgoom2k1.so
%{_libdir}/gstreamer-%{gst_branch}/libgsticydemux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstid3demux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstimagefreeze.so
%{_libdir}/gstreamer-%{gst_branch}/libgstinterleave.so
%{_libdir}/gstreamer-%{gst_branch}/libgstisomp4.so
%{_libdir}/gstreamer-%{gst_branch}/libgstjpeg.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlevel.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmatroska.so
#%{_libdir}/gstreamer-%{gst_branch}/libgstmonoscope.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmulaw.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmultifile.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmultipart.so
%{_libdir}/gstreamer-%{gst_branch}/libgstnavigationtest.so
%{_libdir}/gstreamer-%{gst_branch}/libgstoss4audio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstossaudio.so
#%{_libdir}/gstreamer-%{gst_branch}/libgstpng.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpulse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstreplaygain.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtsp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstshapewipe.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsmpte.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspectrum.so
#%{_libdir}/gstreamer-%{gst_branch}/libgstspeex.so
%{_libdir}/gstreamer-%{gst_branch}/libgstudp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideobox.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideocrop.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideofilter.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideomixer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwavenc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwavparse.so
%if %{with x}
%{_libdir}/gstreamer-%{gst_branch}/libgstximagesrc.so
%endif
#%{_libdir}/gstreamer-%{gst_branch}/libgsty4menc.so
#%{_libdir}/gstreamer-%{gst_branch}/libgstcairo.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsouphttpsrc.so
#%{_libdir}/gstreamer-%{gst_branch}/libgstflac.so
#%{_libdir}/gstreamer-%{gst_branch}/libgstvpx.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdtmf.so


%if 0%{?ENABLE_AALIB}
%files extra
%manifest %{name}.manifest
%defattr(-, root, root)
%{_libdir}/gstreamer-%{gst_branch}/libgstaasink.so
%endif
