#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-resolver
Version  : 1.3.1
Release  : 2
URL      : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-api/1.3.1/maven-resolver-api-1.3.1.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-api/1.3.1/maven-resolver-api-1.3.1.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-api/1.3.1/maven-resolver-api-1.3.1.pom
Source2  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-connector-basic/1.3.1/maven-resolver-connector-basic-1.3.1.jar
Source3  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-connector-basic/1.3.1/maven-resolver-connector-basic-1.3.1.pom
Source4  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-impl/1.3.1/maven-resolver-impl-1.3.1.jar
Source5  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-impl/1.3.1/maven-resolver-impl-1.3.1.pom
Source6  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-spi/1.3.1/maven-resolver-spi-1.3.1.jar
Source7  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-spi/1.3.1/maven-resolver-spi-1.3.1.pom
Source8  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-transport-wagon/1.3.1/maven-resolver-transport-wagon-1.3.1.jar
Source9  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-transport-wagon/1.3.1/maven-resolver-transport-wagon-1.3.1.pom
Source10  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-util/1.3.1/maven-resolver-util-1.3.1.jar
Source11  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver-util/1.3.1/maven-resolver-util-1.3.1.pom
Source12  : https://repo1.maven.org/maven2/org/apache/maven/resolver/maven-resolver/1.3.1/maven-resolver-1.3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-resolver-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-resolver package.
Group: Data

%description data
data components for the mvn-maven-resolver package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-api/1.3.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-api/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-api/1.3.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-api/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-connector-basic/1.3.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-connector-basic/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-connector-basic/1.3.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-connector-basic/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-impl/1.3.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-impl/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-impl/1.3.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-impl/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-spi/1.3.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-spi/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-spi/1.3.1
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-spi/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-transport-wagon/1.3.1
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-transport-wagon/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-transport-wagon/1.3.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-transport-wagon/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-util/1.3.1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-util/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-util/1.3.1
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-util/1.3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver/1.3.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver/1.3.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-api/1.3.1/maven-resolver-api-1.3.1.jar
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-api/1.3.1/maven-resolver-api-1.3.1.pom
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-connector-basic/1.3.1/maven-resolver-connector-basic-1.3.1.jar
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-connector-basic/1.3.1/maven-resolver-connector-basic-1.3.1.pom
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-impl/1.3.1/maven-resolver-impl-1.3.1.jar
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-impl/1.3.1/maven-resolver-impl-1.3.1.pom
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-spi/1.3.1/maven-resolver-spi-1.3.1.jar
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-spi/1.3.1/maven-resolver-spi-1.3.1.pom
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-transport-wagon/1.3.1/maven-resolver-transport-wagon-1.3.1.jar
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-transport-wagon/1.3.1/maven-resolver-transport-wagon-1.3.1.pom
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-util/1.3.1/maven-resolver-util-1.3.1.jar
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver-util/1.3.1/maven-resolver-util-1.3.1.pom
/usr/share/java/.m2/repository/org/apache/maven/resolver/maven-resolver/1.3.1/maven-resolver-1.3.1.pom
