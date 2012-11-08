Name:           gst-plugins-good
Version:        1.0.2
Release:        1
%define gst_branch 1.0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
License:        LGPL-2.1+
Group:          Productivity/Multimedia/Other
Url:            http://gstreamer.freedesktop.org/
Source0:        http://download.gnome.org/sources/gst-plugins-good/1.0/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.31.14
BuildRequires:  gstreamer-devel >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.0.2
BuildRequires:  gtk-doc >= 1.12
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
# used by libgstvideo4linux2.so
BuildRequires:  libXv-devel
BuildRequires:  bzip2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  orc >= 0.4.16
BuildRequires:  python
BuildRequires:  gettext-tools
# TODO find where process.h comes from, not kernel-devel and not wxWidgets so far.
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(cairo) >= 1.0.0
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(cairo-gobject) >= 1.10.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.8.0
BuildRequires:  pkgconfig(gudev-1.0) >= 143
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.9
BuildRequires:  pkgconfig(speex) >= 1.1.6
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
Requires:       gst-plugins-base >= 1.0.0
Requires:       gstreamer >= 1.0.0
Recommends:     %{name}-lang
Enhances:       gstreamer

%description
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package doc
Summary:        Documentation for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description doc
This package contains documentation for %{name}

%package extra
Summary:        Complementary plugins for %{name}
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Enhances:       gst-plugins-good

%description extra
This package provides complementary plugins for
%{name}.

%prep
chmod 0644 %{S:0}
%setup -q -n %{name}-%{version}

%build
# FIXME:
# warning: failed to load external entity "xml/element-v4l2src-details.xml"
# warning: failed to load external entity "xml/plugin-video4linux2.xml"
%configure\
%if ! 0%{?ENABLE_AALIB}
	--disable-aalib\
%endif
	--enable-gtk-doc\
	--with-gtk=3.0\
	--enable-experimental
make %{?jobs:-j%jobs}

%install
%make_install
%find_lang %{name}-%{gst_branch}
mv %{name}-%{gst_branch}.lang %{name}.lang

%lang_package

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING
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
%{_libdir}/gstreamer-%{gst_branch}/libgsteffectv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstequalizer.so
%{_datadir}/gstreamer-%{gst_branch}/presets/GstIirEqualizer10Bands.prs
%{_datadir}/gstreamer-%{gst_branch}/presets/GstIirEqualizer3Bands.prs
%{_libdir}/gstreamer-%{gst_branch}/libgstflv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstflxdec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgdkpixbuf.so
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
%{_libdir}/gstreamer-%{gst_branch}/libgstmonoscope.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmulaw.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmultifile.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmultipart.so
%{_libdir}/gstreamer-%{gst_branch}/libgstnavigationtest.so
%{_libdir}/gstreamer-%{gst_branch}/libgstoss4audio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstossaudio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpng.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpulse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstreplaygain.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtsp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstshapewipe.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsmpte.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspectrum.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspeex.so
%{_libdir}/gstreamer-%{gst_branch}/libgstudp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideobox.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideocrop.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideofilter.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideomixer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwavenc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwavparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstximagesrc.so
%{_libdir}/gstreamer-%{gst_branch}/libgsty4menc.so

%files doc
%defattr(-, root, root)
%{_datadir}/gtk-doc/html/gst-plugins-good-plugins-%{gst_branch}

%files extra
%defattr(-, root, root)
%if 0%{?ENABLE_AALIB}
%{_libdir}/gstreamer-%{gst_branch}/libgstaasink.so
%endif
