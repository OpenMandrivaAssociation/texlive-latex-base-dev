Name:		texlive-latex-base-dev
Version:	64899
Release:	2
Summary:	Development pre-release of the LaTeX kernel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latex-base-dev
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-base-dev.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-base-dev.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-base-dev.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a testing release for upcoming LaTeX2e
kernel changes. Testing by the LaTeX team itself suggests that
the code is stable and usable, but wider use by knowledgeable
users is required by adding these changes to the release LaTeX
kernel. Typically, the code here will be used by a TeX system
to create dedicated formats, for example pdflatex-dev, which
can then be used explicitly for testing.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/source
%doc %{_texmfdistdir}/source/latex-dev
%doc %{_texmfdistdir}/source/latex-dev/base
%doc %{_texmfdistdir}/source/latex-dev/base/utf8ienc.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/unpack.ins
%doc %{_texmfdistdir}/source/latex-dev/base/tulm.ins
%doc %{_texmfdistdir}/source/latex-dev/base/tulm.fdd
%doc %{_texmfdistdir}/source/latex-dev/base/syntonly.ins
%doc %{_texmfdistdir}/source/latex-dev/base/syntonly.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/slifonts.fdd
%doc %{_texmfdistdir}/source/latex-dev/base/slides.ins
%doc %{_texmfdistdir}/source/latex-dev/base/slides.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/proc.ins
%doc %{_texmfdistdir}/source/latex-dev/base/proc.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/preload.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/oldlfont.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/olddc.ins
%doc %{_texmfdistdir}/source/latex-dev/base/nfssfont.ins
%doc %{_texmfdistdir}/source/latex-dev/base/nfssfont.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/newlfont.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/newdc.ins
%doc %{_texmfdistdir}/source/latex-dev/base/makeindx.ins
%doc %{_texmfdistdir}/source/latex-dev/base/makeindx.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltxref.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltxdoc.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltvers.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltthm.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/lttextcomp.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/lttab.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltspace.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltshipout.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltsect.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltplain.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltpictur.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltpara.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltpar.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltpageno.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltpage.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltoutput.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltoutenc.ins
%doc %{_texmfdistdir}/source/latex-dev/base/ltoutenc.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltmiscen.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltmeta.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltmath.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltmarks.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltluatex.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltlogos.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltlists.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltlength.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltkeys.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltidxglo.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/lthyphen.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/lthooks.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfsstrc.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfssini.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfssdcl.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfsscmp.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfssbas.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfssaxes.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfntcmd.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfloat.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfinal.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfiles.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltfilehook.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltexpl.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/lterror.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltdirchk.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltdefns.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltcounts.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltcntrl.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltcmdhooks.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltcmd.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltclass.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltboxes.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltbibl.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ltalloc.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/letter.ins
%doc %{_texmfdistdir}/source/latex-dev/base/letter.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/latexsym.ins
%doc %{_texmfdistdir}/source/latex-dev/base/latexsym.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/latexrelease.ins
%doc %{_texmfdistdir}/source/latex-dev/base/latexrelease.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/latex209.ins
%doc %{_texmfdistdir}/source/latex-dev/base/latex209.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/inputenc.ins
%doc %{_texmfdistdir}/source/latex-dev/base/inputenc.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ifthen.ins
%doc %{_texmfdistdir}/source/latex-dev/base/ifthen.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/graphpap.ins
%doc %{_texmfdistdir}/source/latex-dev/base/graphpap.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/format.ins
%doc %{_texmfdistdir}/source/latex-dev/base/fontdef.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/fix-cm.ins
%doc %{_texmfdistdir}/source/latex-dev/base/fix-cm.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/exscale.ins
%doc %{_texmfdistdir}/source/latex-dev/base/exscale.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/ec.ins
%doc %{_texmfdistdir}/source/latex-dev/base/docstrip.ins
%doc %{_texmfdistdir}/source/latex-dev/base/docstrip.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/doc.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/cmfonts.ins
%doc %{_texmfdistdir}/source/latex-dev/base/cmfonts.fdd
%doc %{_texmfdistdir}/source/latex-dev/base/cmextra.ins
%doc %{_texmfdistdir}/source/latex-dev/base/classes.ins
%doc %{_texmfdistdir}/source/latex-dev/base/classes.dtx
%doc %{_texmfdistdir}/source/latex-dev/base/alltt.ins
%doc %{_texmfdistdir}/source/latex-dev/base/alltt.dtx
%{_texmfdistdir}/tex
%{_texmfdistdir}/tex/latex-dev
%{_texmfdistdir}/tex/latex-dev/base
%{_texmfdistdir}/tex/latex-dev/base/x2enc.dfu
%{_texmfdistdir}/tex/latex-dev/base/utf8enc.dfu
%{_texmfdistdir}/tex/latex-dev/base/utf8.def
%{_texmfdistdir}/tex/latex-dev/base/utf8-2018.def
%{_texmfdistdir}/tex/latex-dev/base/ullasy.fd
%{_texmfdistdir}/tex/latex-dev/base/ulasy.fd
%{_texmfdistdir}/tex/latex-dev/base/ucmtt.fd
%{_texmfdistdir}/tex/latex-dev/base/ucmss.fd
%{_texmfdistdir}/tex/latex-dev/base/ucmr.fd
%{_texmfdistdir}/tex/latex-dev/base/tulmvtt.fd
%{_texmfdistdir}/tex/latex-dev/base/tulmtt.fd
%{_texmfdistdir}/tex/latex-dev/base/tulmssq.fd
%{_texmfdistdir}/tex/latex-dev/base/tulmss.fd
%{_texmfdistdir}/tex/latex-dev/base/tulmr.fd
%{_texmfdistdir}/tex/latex-dev/base/tulmdh.fd
%{_texmfdistdir}/tex/latex-dev/base/tuenc.def
%{_texmfdistdir}/tex/latex-dev/base/ts1enc.dfu
%{_texmfdistdir}/tex/latex-dev/base/ts1enc.def
%{_texmfdistdir}/tex/latex-dev/base/ts1cmvtt.fd
%{_texmfdistdir}/tex/latex-dev/base/ts1cmtt.fd
%{_texmfdistdir}/tex/latex-dev/base/ts1cmss.fd
%{_texmfdistdir}/tex/latex-dev/base/ts1cmr.fd
%{_texmfdistdir}/tex/latex-dev/base/tracefnt.sty
%{_texmfdistdir}/tex/latex-dev/base/textcomp.sty
%{_texmfdistdir}/tex/latex-dev/base/textcomp-2018-08-11.sty
%{_texmfdistdir}/tex/latex-dev/base/texsys.cfg
%{_texmfdistdir}/tex/latex-dev/base/testpage.tex
%{_texmfdistdir}/tex/latex-dev/base/t2cenc.dfu
%{_texmfdistdir}/tex/latex-dev/base/t2benc.dfu
%{_texmfdistdir}/tex/latex-dev/base/t2aenc.dfu
%{_texmfdistdir}/tex/latex-dev/base/t1lcmtt.fd
%{_texmfdistdir}/tex/latex-dev/base/t1lcmss.fd
%{_texmfdistdir}/tex/latex-dev/base/t1enc.sty
%{_texmfdistdir}/tex/latex-dev/base/t1enc.dfu
%{_texmfdistdir}/tex/latex-dev/base/t1enc.def
%{_texmfdistdir}/tex/latex-dev/base/t1cmvtt.fd
%{_texmfdistdir}/tex/latex-dev/base/t1cmtt.fd
%{_texmfdistdir}/tex/latex-dev/base/t1cmss.fd
%{_texmfdistdir}/tex/latex-dev/base/t1cmr.fd
%{_texmfdistdir}/tex/latex-dev/base/t1cmfr.fd
%{_texmfdistdir}/tex/latex-dev/base/t1cmfib.fd
%{_texmfdistdir}/tex/latex-dev/base/t1cmdh.fd
%{_texmfdistdir}/tex/latex-dev/base/syntonly.sty
%{_texmfdistdir}/tex/latex-dev/base/structuredlog.sty
%{_texmfdistdir}/tex/latex-dev/base/source2edoc.cls
%{_texmfdistdir}/tex/latex-dev/base/small2e.tex
%{_texmfdistdir}/tex/latex-dev/base/slides.sty
%{_texmfdistdir}/tex/latex-dev/base/slides.def
%{_texmfdistdir}/tex/latex-dev/base/slides.cls
%{_texmfdistdir}/tex/latex-dev/base/size12.clo
%{_texmfdistdir}/tex/latex-dev/base/size11.clo
%{_texmfdistdir}/tex/latex-dev/base/size10.clo
%{_texmfdistdir}/tex/latex-dev/base/showidx.sty
%{_texmfdistdir}/tex/latex-dev/base/shortvrb.sty
%{_texmfdistdir}/tex/latex-dev/base/sfonts.def
%{_texmfdistdir}/tex/latex-dev/base/sample2e.tex
%{_texmfdistdir}/tex/latex-dev/base/report.sty
%{_texmfdistdir}/tex/latex-dev/base/report.cls
%{_texmfdistdir}/tex/latex-dev/base/proc.sty
%{_texmfdistdir}/tex/latex-dev/base/proc.cls
%{_texmfdistdir}/tex/latex-dev/base/preload.ltx
%{_texmfdistdir}/tex/latex-dev/base/preload.cfg
%{_texmfdistdir}/tex/latex-dev/base/ot4enc.def
%{_texmfdistdir}/tex/latex-dev/base/ot2enc.dfu
%{_texmfdistdir}/tex/latex-dev/base/ot1lcmtt.fd
%{_texmfdistdir}/tex/latex-dev/base/ot1lcmss.fd
%{_texmfdistdir}/tex/latex-dev/base/ot1enc.dfu
%{_texmfdistdir}/tex/latex-dev/base/ot1enc.def
%{_texmfdistdir}/tex/latex-dev/base/ot1cmvtt.fd
%{_texmfdistdir}/tex/latex-dev/base/ot1cmtt.fd
%{_texmfdistdir}/tex/latex-dev/base/ot1cmss.fd
%{_texmfdistdir}/tex/latex-dev/base/ot1cmr.fd
%{_texmfdistdir}/tex/latex-dev/base/ot1cmfr.fd
%{_texmfdistdir}/tex/latex-dev/base/ot1cmfib.fd
%{_texmfdistdir}/tex/latex-dev/base/ot1cmdh.fd
%{_texmfdistdir}/tex/latex-dev/base/openbib.sty
%{_texmfdistdir}/tex/latex-dev/base/omxlcmex.fd
%{_texmfdistdir}/tex/latex-dev/base/omxcmex.fd
%{_texmfdistdir}/tex/latex-dev/base/omslcmsy.fd
%{_texmfdistdir}/tex/latex-dev/base/omsenc.dfu
%{_texmfdistdir}/tex/latex-dev/base/omsenc.def
%{_texmfdistdir}/tex/latex-dev/base/omscmsy.fd
%{_texmfdistdir}/tex/latex-dev/base/omscmr.fd
%{_texmfdistdir}/tex/latex-dev/base/omllcmm.fd
%{_texmfdistdir}/tex/latex-dev/base/omlenc.def
%{_texmfdistdir}/tex/latex-dev/base/omlcmr.fd
%{_texmfdistdir}/tex/latex-dev/base/omlcmm.fd
%{_texmfdistdir}/tex/latex-dev/base/oldlfont.sty
%{_texmfdistdir}/tex/latex-dev/base/nfssfont.tex
%{_texmfdistdir}/tex/latex-dev/base/next.def
%{_texmfdistdir}/tex/latex-dev/base/newlfont.sty
%{_texmfdistdir}/tex/latex-dev/base/minimal.cls
%{_texmfdistdir}/tex/latex-dev/base/makeidx.sty
%{_texmfdistdir}/tex/latex-dev/base/macce.def
%{_texmfdistdir}/tex/latex-dev/base/ly1enc.dfu
%{_texmfdistdir}/tex/latex-dev/base/ltxguide.cls
%{_texmfdistdir}/tex/latex-dev/base/ltxdoc.cls
%{_texmfdistdir}/tex/latex-dev/base/ltxdoc.cfg
%{_texmfdistdir}/tex/latex-dev/base/ltxcheck.tex
%{_texmfdistdir}/tex/latex-dev/base/ltnews.cls
%{_texmfdistdir}/tex/latex-dev/base/ltluatex.tex
%{_texmfdistdir}/tex/latex-dev/base/ltluatex.lua
%{_texmfdistdir}/tex/latex-dev/base/lppl.tex
%{_texmfdistdir}/tex/latex-dev/base/letter.sty
%{_texmfdistdir}/tex/latex-dev/base/letter.cls
%{_texmfdistdir}/tex/latex-dev/base/leqno.sty
%{_texmfdistdir}/tex/latex-dev/base/leqno.clo
%{_texmfdistdir}/tex/latex-dev/base/lcyenc.dfu
%{_texmfdistdir}/tex/latex-dev/base/latin9.def
%{_texmfdistdir}/tex/latex-dev/base/latin5.def
%{_texmfdistdir}/tex/latex-dev/base/latin4.def
%{_texmfdistdir}/tex/latex-dev/base/latin3.def
%{_texmfdistdir}/tex/latex-dev/base/latin2.def
%{_texmfdistdir}/tex/latex-dev/base/latin10.def
%{_texmfdistdir}/tex/latex-dev/base/latin1.def
%{_texmfdistdir}/tex/latex-dev/base/latexsym.sty
%{_texmfdistdir}/tex/latex-dev/base/latexrelease.sty
%{_texmfdistdir}/tex/latex-dev/base/latex209.def
%{_texmfdistdir}/tex/latex-dev/base/latex.ltx
%{_texmfdistdir}/tex/latex-dev/base/lablst.tex
%{_texmfdistdir}/tex/latex-dev/base/inputenc.sty
%{_texmfdistdir}/tex/latex-dev/base/ifthen.sty
%{_texmfdistdir}/tex/latex-dev/base/idx.tex
%{_texmfdistdir}/tex/latex-dev/base/hyphen.ltx
%{_texmfdistdir}/tex/latex-dev/base/graphpap.sty
%{_texmfdistdir}/tex/latex-dev/base/fonttext.ltx
%{_texmfdistdir}/tex/latex-dev/base/fonttext.cfg
%{_texmfdistdir}/tex/latex-dev/base/fontmath.ltx
%{_texmfdistdir}/tex/latex-dev/base/fontmath.cfg
%{_texmfdistdir}/tex/latex-dev/base/fontenc.sty
%{_texmfdistdir}/tex/latex-dev/base/fltrace.sty
%{_texmfdistdir}/tex/latex-dev/base/fleqn.sty
%{_texmfdistdir}/tex/latex-dev/base/fleqn.clo
%{_texmfdistdir}/tex/latex-dev/base/flafter.sty
%{_texmfdistdir}/tex/latex-dev/base/fixltx2e.sty
%{_texmfdistdir}/tex/latex-dev/base/fix-cm.sty
%{_texmfdistdir}/tex/latex-dev/base/exscale.sty
%{_texmfdistdir}/tex/latex-dev/base/docstrip.tex
%{_texmfdistdir}/tex/latex-dev/base/doc.sty
%{_texmfdistdir}/tex/latex-dev/base/doc-2021-06-01.sty
%{_texmfdistdir}/tex/latex-dev/base/doc-2016-02-15.sty
%{_texmfdistdir}/tex/latex-dev/base/decmulti.def
%{_texmfdistdir}/tex/latex-dev/base/cp865.def
%{_texmfdistdir}/tex/latex-dev/base/cp858.def
%{_texmfdistdir}/tex/latex-dev/base/cp852.def
%{_texmfdistdir}/tex/latex-dev/base/cp850.def
%{_texmfdistdir}/tex/latex-dev/base/cp437de.def
%{_texmfdistdir}/tex/latex-dev/base/cp437.def
%{_texmfdistdir}/tex/latex-dev/base/cp1257.def
%{_texmfdistdir}/tex/latex-dev/base/cp1252.def
%{_texmfdistdir}/tex/latex-dev/base/cp1250.def
%{_texmfdistdir}/tex/latex-dev/base/book.sty
%{_texmfdistdir}/tex/latex-dev/base/book.cls
%{_texmfdistdir}/tex/latex-dev/base/bk12.clo
%{_texmfdistdir}/tex/latex-dev/base/bk11.clo
%{_texmfdistdir}/tex/latex-dev/base/bk10.clo
%{_texmfdistdir}/tex/latex-dev/base/bezier.sty
%{_texmfdistdir}/tex/latex-dev/base/atveryend-ltx.sty
%{_texmfdistdir}/tex/latex-dev/base/atbegshi-ltx.sty
%{_texmfdistdir}/tex/latex-dev/base/ascii.def
%{_texmfdistdir}/tex/latex-dev/base/article.sty
%{_texmfdistdir}/tex/latex-dev/base/article.cls
%{_texmfdistdir}/tex/latex-dev/base/applemac.def
%{_texmfdistdir}/tex/latex-dev/base/ansinew.def
%{_texmfdistdir}/tex/latex-dev/base/alltt.sty
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/latex-dev
%doc %{_texmfdistdir}/doc/latex-dev/base
%doc %{_texmfdistdir}/doc/latex-dev/base/webcomp.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/webcomp.err
%doc %{_texmfdistdir}/doc/latex-dev/base/utf8ienc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/usrguide.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/usrguide.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/usrguide-historic.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/usrguide-historic.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/tulm.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/tlc2.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/tlc2.err
%doc %{_texmfdistdir}/doc/latex-dev/base/syntonly.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/source2e.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/source2e.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/slifonts.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/slides.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/proc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/nfssfont.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/modguide.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/modguide.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/manifest.txt
%doc %{_texmfdistdir}/doc/latex-dev/base/makeindx.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltxdoc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltx3info.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltx3info.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltshipout-doc.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltshipout-doc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltshipout-code.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltshipout-code.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltpara-doc.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltpara-doc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltpara-code.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltpara-code.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews36.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews36.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews35.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews35.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews34.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews34.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews33.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews33.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews32.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews32.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews31.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews31.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews30.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews30.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews29.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews29.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews28.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews28.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews27.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews27.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews26.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews26.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews25.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews25.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews24.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews24.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews23.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews23.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews22.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews22.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews21.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews21.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews20.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews20.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews19.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews19.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews18.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews18.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews17.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews17.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews16.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews16.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews15.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews15.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews14.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews14.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews13.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews13.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews12.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews12.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews11.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews11.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews10.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews10.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews09.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews09.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews08.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews08.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews07.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews07.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews06.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews06.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews05.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews05.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews04.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews04.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews03.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews03.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews02.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews02.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews01.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews01.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltnews.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltmarks-doc.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltmarks-doc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltmarks-code.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltmarks-code.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltluatex.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/lthooks-doc.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/lthooks-doc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/lthooks-code.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/lthooks-code.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltfilehook-doc.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltfilehook-doc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltfilehook-code.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltfilehook-code.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltcmdhooks-doc.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltcmdhooks-doc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ltcmdhooks-code.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/ltcmdhooks-code.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/lppl.txt
%doc %{_texmfdistdir}/doc/latex-dev/base/lppl.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/lppl-1-2.txt
%doc %{_texmfdistdir}/doc/latex-dev/base/lppl-1-1.txt
%doc %{_texmfdistdir}/doc/latex-dev/base/lppl-1-0.txt
%doc %{_texmfdistdir}/doc/latex-dev/base/lgc2.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/lgc2.err
%doc %{_texmfdistdir}/doc/latex-dev/base/letter.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/legal.txt
%doc %{_texmfdistdir}/doc/latex-dev/base/lb2.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/lb2.err
%doc %{_texmfdistdir}/doc/latex-dev/base/latexsym.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/latexrelease.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/lamport-manual.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/lamport-manual.err
%doc %{_texmfdistdir}/doc/latex-dev/base/inputenc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/ifthen.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/graphpap.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/fntguide.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/fntguide.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/fix-cm.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/exscale.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/encguide.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/encguide.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/docstrip.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/doc.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/doc-code.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/doc-code.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/cyrguide.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/cyrguide.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/cmfonts.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/clsguide.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/clsguide.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/classes.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/changes.txt
%doc %{_texmfdistdir}/doc/latex-dev/base/changes.old.txt
%doc %{_texmfdistdir}/doc/latex-dev/base/cfgguide.tex
%doc %{_texmfdistdir}/doc/latex-dev/base/cfgguide.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/bugs.txt
%doc %{_texmfdistdir}/doc/latex-dev/base/alltt.pdf
%doc %{_texmfdistdir}/doc/latex-dev/base/README.md

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
