%global tl_name biblatex-juradiss
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.23
Release:	%{tl_revision}.1
Summary:	BibLaTeX stylefiles for German law theses
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-juradiss
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-juradiss.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-juradiss.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a custom citation-style for typesetting a German
law thesis with LaTeX. The package (using BibLaTeX) is based on
biblatex-dw and uses biber.

