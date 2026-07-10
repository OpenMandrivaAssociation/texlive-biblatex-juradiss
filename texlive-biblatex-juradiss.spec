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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a custom citation-style for typesetting a German
law thesis with LaTeX. The package (using BibLaTeX) is based on
biblatex-dw and uses biber.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-juradiss
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-juradiss
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-juradiss/Changes
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-juradiss/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-juradiss/biblatex-juradiss.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-juradiss/biblatex-juradiss.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-juradiss/biblatex-juradiss.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-juradiss/biblatex-juradiss.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-juradiss/biblatex-juradiss.dbx
