#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-randomNames
Version  : 1.5.0.0
Release  : 26
URL      : https://cran.r-project.org/src/contrib/randomNames_1.5-0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/randomNames_1.5-0.0.tar.gz
Summary  : Generate Random Given and Surnames
Group    : Development/Tools
License  : GPL-3.0
Requires: R-crayon
Requires: R-data.table
Requires: R-toOrdinal
BuildRequires : R-crayon
BuildRequires : R-data.table
BuildRequires : R-toOrdinal
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n randomNames
cd %{_builddir}/randomNames

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619144764

%install
export SOURCE_DATE_EPOCH=1619144764
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randomNames
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randomNames
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randomNames
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc randomNames || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/randomNames/CITATION
/usr/lib64/R/library/randomNames/DESCRIPTION
/usr/lib64/R/library/randomNames/INDEX
/usr/lib64/R/library/randomNames/Meta/Rd.rds
/usr/lib64/R/library/randomNames/Meta/data.rds
/usr/lib64/R/library/randomNames/Meta/features.rds
/usr/lib64/R/library/randomNames/Meta/hsearch.rds
/usr/lib64/R/library/randomNames/Meta/links.rds
/usr/lib64/R/library/randomNames/Meta/nsInfo.rds
/usr/lib64/R/library/randomNames/Meta/package.rds
/usr/lib64/R/library/randomNames/Meta/vignette.rds
/usr/lib64/R/library/randomNames/NAMESPACE
/usr/lib64/R/library/randomNames/NEWS
/usr/lib64/R/library/randomNames/R/randomNames
/usr/lib64/R/library/randomNames/R/randomNames.rdb
/usr/lib64/R/library/randomNames/R/randomNames.rdx
/usr/lib64/R/library/randomNames/data/Rdata.rdb
/usr/lib64/R/library/randomNames/data/Rdata.rds
/usr/lib64/R/library/randomNames/data/Rdata.rdx
/usr/lib64/R/library/randomNames/data/datalist
/usr/lib64/R/library/randomNames/doc/index.html
/usr/lib64/R/library/randomNames/doc/randomNames.R
/usr/lib64/R/library/randomNames/doc/randomNames.Rmd
/usr/lib64/R/library/randomNames/doc/randomNames.html
/usr/lib64/R/library/randomNames/help/AnIndex
/usr/lib64/R/library/randomNames/help/aliases.rds
/usr/lib64/R/library/randomNames/help/paths.rds
/usr/lib64/R/library/randomNames/help/randomNames.rdb
/usr/lib64/R/library/randomNames/help/randomNames.rdx
/usr/lib64/R/library/randomNames/html/00Index.html
/usr/lib64/R/library/randomNames/html/R.css
