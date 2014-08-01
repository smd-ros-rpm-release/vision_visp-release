Name:           ros-hydro-vision-visp
Version:        0.7.5
Release:        0%{?dist}
Summary:        ROS vision_visp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/vision_visp
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-visp-auto-tracker
Requires:       ros-hydro-visp-bridge
Requires:       ros-hydro-visp-camera-calibration
Requires:       ros-hydro-visp-hand2eye-calibration
Requires:       ros-hydro-visp-tracker
BuildRequires:  ros-hydro-catkin

%description
Virtual package providing ViSP related packages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Aug 01 2014 Fabien Spindler <fabien.spindler@inria.fr> - 0.7.5-0
- Autogenerated by Bloom

