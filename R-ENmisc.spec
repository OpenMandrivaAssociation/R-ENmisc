%global packname  ENmisc
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.2.7
Release:          1
Summary:          Neuwirth miscellaenous
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/ENmisc_1.2-7.tar.gz
BuildArch:        noarch
Requires:         R-core R-Hmisc R-vcd R-gWidgets R-gWidgetstcltk
Requires:         R-RColorBrewer
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Hmisc
BuildRequires:    R-vcd R-gWidgets R-gWidgetstcltk R-RColorBrewer
BuildRequires:    x11-server-xvfb

%description
The ENmisc library contains utility function for different purposes:
mtapply and mlapply (multivariate version of tapply and lapply),
wtd.boxplot (a boxplot with weights), and a visual interface to
restructuring mosaic plots.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
xvfb-run %{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help

