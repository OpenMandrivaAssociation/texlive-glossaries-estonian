%global tl_name glossaries-estonian
%global tl_revision 49928

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Estonian language module for glossaries package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/glossaries-estonian
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-estonian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-estonian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-estonian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the Estonian language module for the glossaries
package.

