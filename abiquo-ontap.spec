%define abiquo_basedir /opt/abiquo/ontap

Name:           abiquo-ontap
Version:        1.7
Release:        7%{?dist}%{?buildstamp}
Url:            http://www.abiquo.com/
License:        Multiple
Group:          Development/Tools
Summary:        Abiquo Lvmiscsi Storage plugin
Source0:        abiquo-ontap-tomcat.tar.gz
Source1:        ontap.war	
Source2: 	config.xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:	scsi-target-utils
BuildRequires:  /usr/bin/unzip
BuildArch: 	noarch

%description
Abiquo is the Next Generation Cloud Management Solution

This package includes ontap storage plugin.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n abiquo-ontap-tomcat

%clean
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/examples/
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}
mkdir -p $RPM_BUILD_ROOT/%{_initrddir}
cp -r tomcat $RPM_BUILD_ROOT/%{abiquo_basedir}
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/ROOT
install -m 755 abiquo-ontap.init $RPM_BUILD_ROOT/%{_initrddir}/abiquo-ontap
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/ROOT/ %{SOURCE1}
cp %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}/examples/

%post
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add abiquo-ontap

%preun
/sbin/chkconfig --del abiquo-ontap

%files
%{abiquo_basedir}/tomcat/bin
%{abiquo_basedir}/tomcat/lib
%{abiquo_basedir}/tomcat/logs
%{abiquo_basedir}/tomcat/temp
%{abiquo_basedir}/tomcat/LICENSE
%{abiquo_basedir}/tomcat/RUNNING.txt
%{abiquo_basedir}/tomcat/NOTICE
%{abiquo_basedir}/tomcat/RELEASE-NOTES
%{abiquo_basedir}/tomcat/webapps
%{abiquo_basedir}/tomcat/work
%{_docdir}/%{name}
%config(noreplace) %{abiquo_basedir}/tomcat/conf/*
%{_initrddir}/abiquo-ontap

%changelog
* Fri Feb 25 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-7
- set buildarch to noarch

* Wed Feb 16 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-6
- fix release string

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-5.GA
- GA build

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- added sample config file

* Thu Jan 27 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- upstream update

* Tue Jan 25 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- upstream update

* Wed Jan 19 2011 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Tue Nov 02 2010 Sergio Rubio <srubio@abiquo.com> 1.6-3.abiquo
- run abiquo-initenv at startup

* Tue Oct 26 2010 Sergio Rubio <srubio@abiquo.com> 1.6-2.abiquo
- changed default port to 8280

* Thu Oct 21 2010 Sergio Rubio <srubio@abiquo.com> 1.6-1.abiquo
- initial release

