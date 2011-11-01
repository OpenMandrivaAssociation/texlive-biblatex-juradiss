Name:		texlive-biblatex-juradiss
Version:	0.1e
Release:	1
Summary:	Biblatex stylefiles for German law thesis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-juradiss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-juradiss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-juradiss.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a style for creating a german law thesis
with LaTeX, based on biblatex and biblatex-dw.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
