%global tl_name latex-base-dev
%global tl_revision 79242

Name:		texlive-%{tl_name}
Epoch:		1
Version:	pre~release.0
Release:	%{tl_revision}.1
Summary:	Development pre-release of the LaTeX kernel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex-dev/base
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-base-dev.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-base-dev.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-base-dev.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a test release for upcoming LaTeX2e kernel
changes. Testing by the LaTeX team itself suggests that the code is
stable and usable, but wider use by knowledgeable users is desired. The
code here is used by TeX systems to create dedicated formats, for
example pdflatex-dev and lualatex-dev, which can then be used explicitly
for testing, simply by changing your program invocation.

