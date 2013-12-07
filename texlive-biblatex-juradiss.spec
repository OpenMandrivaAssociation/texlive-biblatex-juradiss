# revision 29252
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-juradiss
# catalog-date 2013-03-01 08:15:18 +0100
# catalog-license lppl
# catalog-version 0.1f
Name:		texlive-biblatex-juradiss
Version:	0.1f
Release:	5
Summary:	Biblatex stylefiles for German law thesis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-juradiss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-juradiss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-juradiss.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a style for use in typesetting a German
law thesis with LaTeX. The style (using biblatex) is based on
biblatex-dw.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-juradiss/biblatex-juradiss.bbx
%{_texmfdistdir}/tex/latex/biblatex-juradiss/biblatex-juradiss.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-juradiss/README
%doc %{_texmfdistdir}/doc/latex/biblatex-juradiss/biber.conf
%doc %{_texmfdistdir}/doc/latex/biblatex-juradiss/biblatex-juradiss.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-juradiss/biblatex-juradiss.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
