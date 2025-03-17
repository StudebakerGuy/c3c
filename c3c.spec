Name:		c3c
Version:	0.6.8
Release:	1
Source0:	https://github.com/c3lang/c3c/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	The C3 programming language compiler	
URL:		https://c3-lang.org/
License:	LGPL-3.0-only and MIT
Group:		Development/C3
BuildRequires:	clang
BuildRequires:	cmake
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(libedit)
BuildRequires:	pkgconfig(history)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(z3)
BuildRequires:	llvm
BuildRequires:	spirv-llvm-translator
BuildRequires:	lib64lld-devel
BuildRequires:	lib64mlir-devel
BuildRequires:	lib64lldCOFF-static-devel
BuildRequires:	lib64lldWasm-static-devel
BuildRequires:	lib64lldMinGW-static-devel
BuildRequires:	lib64lldELF-static-devel
BuildRequires:	lib64lldMachO-static-devel
BuildRequires:	lib64lldCommon-static-devel
BuildRequires:  lib64Polly-static-devel
BuildRequires:	lib64LLVMDemangle-static-devel
BuildRequires:	lib64LLVMSupport-static-devel
BuildRequires:	lib64LLVMTableGen-static-devel
BuildRequires:	lib64LLVMTableGenBasic-static-devel
BuildRequires:	lib64LLVMTableGenCommon-static-devel
BuildRequires:	lib64LLVMCore-static-devel
BuildRequires:	lib64LLVMFuzzerCLI-static-devel
BuildRequires:	lib64LLVMFuzzMutate-static-devel
BuildRequires:	lib64LLVMFileCheck-static-devel
BuildRequires:	lib64LLVMInterfaceStub-static-devel
BuildRequires:	lib64LLVMIRPrinter-static-devel
BuildRequires:	lib64LLVMIRReader-static-devel
BuildRequires:	lib64LLVMCodeGen-static-devel
BuildRequires:	lib64LLVMSelectionDAG-static-devel
BuildRequires:	lib64LLVMAsmPrinter-static-devel
BuildRequires:	lib64LLVMGlobalISel-static-devel
BuildRequires:	lib64LLVMCodeGenData-static-devel
BuildRequires:	lib64LLVMCodeGenTypes-static-devel
BuildRequires:	lib64LLVMBinaryFormat-static-devel
BuildRequires:	lib64LLVMBitReader-static-devel
BuildRequires:	lib64LLVMMIRParser-static-devel
BuildRequires:	lib64LLVMBitWriter-static-devel
BuildRequires:	lib64LLVMBitstreamReader-static-devel
BuildRequires:	lib64LLVMDWARFLinker-static-devel
BuildRequires:	lib64LLVMDWARFLinkerClassic-static-devel
BuildRequires:	lib64LLVMDWARFLinkerParallel-static-devel
BuildRequires:	lib64LLVMExtensions-static-devel
BuildRequires:	lib64LLVMFrontendDriver-static-devel
BuildRequires:	lib64LLVMFrontendHLSL-static-devel
BuildRequires:	lib64LLVMFrontendOpenACC-static-devel
BuildRequires:	lib64LLVMFrontendOpenMP-static-devel
BuildRequires:	lib64LLVMFrontendOffloading-static-devel
BuildRequires:	lib64LLVMTransformUtils-static-devel
BuildRequires:	lib64LLVMInstrumentation-static-devel
BuildRequires:	lib64LLVMAggressiveInstCombine-static-devel
BuildRequires:	lib64LLVMInstCombine-static-devel
BuildRequires:	lib64LLVMScalarOpts-static-devel
BuildRequires:	lib64LLVMipo-static-devel
BuildRequires:	lib64LLVMVectorize-static-devel
BuildRequires:	lib64LLVMObjCARCOpts-static-devel
BuildRequires:	lib64LLVMCoroutines-static-devel
BuildRequires:	lib64LLVMCFGuard-static-devel
BuildRequires:	lib64LLVMHipStdPar-static-devel
BuildRequires:	lib64LLVMLinker-static-devel
BuildRequires:	lib64LLVMAnalysis-static-devel
BuildRequires:	lib64LLVMLTO-static-devel
BuildRequires:	lib64LLVMMC-static-devel
BuildRequires:	lib64LLVMMCParser-static-devel
BuildRequires:	lib64LLVMMCDisassembler-static-devel
BuildRequires:	lib64LLVMMCA-static-devel
BuildRequires:	lib64LLVMObjCopy-static-devel
BuildRequires:	lib64LLVMObject-static-devel
BuildRequires:	lib64LLVMObjectYAML-static-devel
BuildRequires:	lib64LLVMOption-static-devel
BuildRequires:	lib64LLVMRemarks-static-devel
BuildRequires:	lib64LLVMDebuginfod-static-devel
BuildRequires:	lib64LLVMDebugInfoDWARF-static-devel
BuildRequires:	lib64LLVMDebugInfoGSYM-static-devel
BuildRequires:	lib64LLVMDebugInfoLogicalView-static-devel
BuildRequires:	lib64LLVMDebugInfoMSF-static-devel
BuildRequires:	lib64LLVMDebugInfoCodeView-static-devel
BuildRequires:	lib64LLVMDebugInfoPDB-static-devel
BuildRequires:	lib64LLVMSymbolize-static-devel
BuildRequires:	lib64LLVMDebugInfoBTF-static-devel
BuildRequires:	lib64LLVMDWP-static-devel
BuildRequires:	lib64LLVMExecutionEngine-static-devel
BuildRequires:	lib64LLVMInterpreter-static-devel
BuildRequires:	lib64LLVMJITLink-static-devel
BuildRequires:	lib64LLVMMCJIT-static-devel
BuildRequires:	lib64LLVMOrcJIT-static-devel
BuildRequires:	lib64LLVMOrcDebugging-static-devel
BuildRequires:	lib64LLVMOrcShared-static-devel
BuildRequires:	lib64LLVMOrcTargetProcess-static-devel
BuildRequires:	lib64LLVMRuntimeDyld-static-devel
BuildRequires:	lib64LLVMTarget-static-devel
BuildRequires:	lib64LLVMAArch64CodeGen-static-devel
BuildRequires:	lib64LLVMAArch64AsmParser-static-devel
BuildRequires:	lib64LLVMAArch64Disassembler-static-devel
BuildRequires:	lib64LLVMAArch64Desc-static-devel
BuildRequires:	lib64LLVMAArch64Info-static-devel
BuildRequires:	lib64LLVMAArch64Utils-static-devel
BuildRequires:	lib64LLVMAMDGPUCodeGen-static-devel
BuildRequires:	lib64LLVMAMDGPUAsmParser-static-devel
BuildRequires:	lib64LLVMAMDGPUDisassembler-static-devel
BuildRequires:	lib64LLVMAMDGPUTargetMCA-static-devel
BuildRequires:	lib64LLVMAMDGPUDesc-static-devel
BuildRequires:	lib64LLVMAMDGPUInfo-static-devel
BuildRequires:	lib64LLVMAMDGPUUtils-static-devel
BuildRequires:	lib64LLVMARMCodeGen-static-devel
BuildRequires:	lib64LLVMARMAsmParser-static-devel
BuildRequires:	lib64LLVMARMDisassembler-static-devel
BuildRequires:	lib64LLVMARMDesc-static-devel
BuildRequires:	lib64LLVMARMInfo-static-devel
BuildRequires:	lib64LLVMARMUtils-static-devel
BuildRequires:	lib64LLVMAVRCodeGen-static-devel
BuildRequires:	lib64LLVMAVRAsmParser-static-devel
BuildRequires:	lib64LLVMAVRDisassembler-static-devel
BuildRequires:	lib64LLVMAVRDesc-static-devel
BuildRequires:	lib64LLVMAVRInfo-static-devel
BuildRequires:	lib64LLVMBPFCodeGen-static-devel
BuildRequires:	lib64LLVMBPFAsmParser-static-devel
BuildRequires:	lib64LLVMBPFDisassembler-static-devel
BuildRequires:	lib64LLVMBPFDesc-static-devel
BuildRequires:	lib64LLVMBPFInfo-static-devel
BuildRequires:	lib64LLVMHexagonCodeGen-static-devel
BuildRequires:	lib64LLVMHexagonAsmParser-static-devel
BuildRequires:	lib64LLVMHexagonDisassembler-static-devel
BuildRequires:	lib64LLVMHexagonDesc-static-devel
BuildRequires:	lib64LLVMHexagonInfo-static-devel
BuildRequires:	lib64LLVMLanaiCodeGen-static-devel
BuildRequires:	lib64LLVMLanaiAsmParser-static-devel
BuildRequires:	lib64LLVMLanaiDisassembler-static-devel
BuildRequires:	lib64LLVMLanaiDesc-static-devel
BuildRequires:	lib64LLVMLanaiInfo-static-devel
BuildRequires:	lib64LLVMLoongArchCodeGen-static-devel
BuildRequires:	lib64LLVMLoongArchAsmParser-static-devel
BuildRequires:	lib64LLVMLoongArchDisassembler-static-devel
BuildRequires:	lib64LLVMLoongArchDesc-static-devel
BuildRequires:	lib64LLVMLoongArchInfo-static-devel
BuildRequires:	lib64LLVMMipsCodeGen-static-devel
BuildRequires:	lib64LLVMMipsAsmParser-static-devel
BuildRequires:	lib64LLVMMipsDisassembler-static-devel
BuildRequires:	lib64LLVMMipsDesc-static-devel
BuildRequires:	lib64LLVMMipsInfo-static-devel
BuildRequires:	lib64LLVMMSP430CodeGen-static-devel
BuildRequires:	lib64LLVMMSP430Desc-static-devel
BuildRequires:	lib64LLVMMSP430Info-static-devel
BuildRequires:	lib64LLVMMSP430AsmParser-static-devel
BuildRequires:	lib64LLVMMSP430Disassembler-static-devel
BuildRequires:	lib64LLVMNVPTXCodeGen-static-devel
BuildRequires:	lib64LLVMNVPTXDesc-static-devel
BuildRequires:	lib64LLVMNVPTXInfo-static-devel
BuildRequires:	lib64LLVMPowerPCCodeGen-static-devel
BuildRequires:	lib64LLVMPowerPCAsmParser-static-devel
BuildRequires:	lib64LLVMPowerPCDisassembler-static-devel
BuildRequires:	lib64LLVMPowerPCDesc-static-devel
BuildRequires:	lib64LLVMPowerPCInfo-static-devel
BuildRequires:	lib64LLVMRISCVCodeGen-static-devel
BuildRequires:	lib64LLVMRISCVAsmParser-static-devel
BuildRequires:	lib64LLVMRISCVDisassembler-static-devel
BuildRequires:	lib64LLVMRISCVDesc-static-devel
BuildRequires:	lib64LLVMRISCVTargetMCA-static-devel
BuildRequires:	lib64LLVMRISCVInfo-static-devel
BuildRequires:	lib64LLVMSparcCodeGen-static-devel
BuildRequires:	lib64LLVMSparcAsmParser-static-devel
BuildRequires:	lib64LLVMSparcDisassembler-static-devel
BuildRequires:	lib64LLVMSparcDesc-static-devel
BuildRequires:	lib64LLVMSparcInfo-static-devel
BuildRequires:	lib64LLVMSystemZCodeGen-static-devel
BuildRequires:	lib64LLVMSystemZAsmParser-static-devel
BuildRequires:	lib64LLVMSystemZDisassembler-static-devel
BuildRequires:	lib64LLVMSystemZDesc-static-devel
BuildRequires:	lib64LLVMSystemZInfo-static-devel
BuildRequires:	lib64LLVMVECodeGen-static-devel
BuildRequires:	lib64LLVMVEAsmParser-static-devel
BuildRequires:	lib64LLVMVEDisassembler-static-devel
BuildRequires:	lib64LLVMVEInfo-static-devel
BuildRequires:	lib64LLVMVEDesc-static-devel
BuildRequires:	lib64LLVMWebAssemblyCodeGen-static-devel
BuildRequires:	lib64LLVMWebAssemblyAsmParser-static-devel
BuildRequires:	lib64LLVMWebAssemblyDisassembler-static-devel
BuildRequires:	lib64LLVMWebAssemblyDesc-static-devel
BuildRequires:	lib64LLVMWebAssemblyInfo-static-devel
BuildRequires:	lib64LLVMWebAssemblyUtils-static-devel
BuildRequires:	lib64LLVMX86CodeGen-static-devel
BuildRequires:	lib64LLVMX86AsmParser-static-devel
BuildRequires:	lib64LLVMX86Disassembler-static-devel
BuildRequires:	lib64LLVMX86TargetMCA-static-devel
BuildRequires:	lib64LLVMX86Desc-static-devel
BuildRequires:	lib64LLVMX86Info-static-devel
BuildRequires:	lib64LLVMXCoreCodeGen-static-devel
BuildRequires:	lib64LLVMXCoreDisassembler-static-devel
BuildRequires:	lib64LLVMXCoreDesc-static-devel
BuildRequires:	lib64LLVMXCoreInfo-static-devel
BuildRequires:	lib64LLVMARCCodeGen-static-devel
BuildRequires:	lib64LLVMARCDisassembler-static-devel
BuildRequires:	lib64LLVMARCDesc-static-devel
BuildRequires:	lib64LLVMARCInfo-static-devel
BuildRequires:	lib64LLVMCSKYCodeGen-static-devel
BuildRequires:	lib64LLVMCSKYAsmParser-static-devel
BuildRequires:	lib64LLVMCSKYDisassembler-static-devel
BuildRequires:	lib64LLVMCSKYDesc-static-devel
BuildRequires:	lib64LLVMCSKYInfo-static-devel
BuildRequires:	lib64LLVMM68kCodeGen-static-devel
BuildRequires:	lib64LLVMM68kInfo-static-devel
BuildRequires:	lib64LLVMM68kDesc-static-devel
BuildRequires:	lib64LLVMM68kAsmParser-static-devel
BuildRequires:	lib64LLVMM68kDisassembler-static-devel
BuildRequires:	lib64LLVMSPIRVCodeGen-static-devel
BuildRequires:	lib64LLVMSPIRVDesc-static-devel
BuildRequires:	lib64LLVMSPIRVInfo-static-devel
BuildRequires:	lib64LLVMSPIRVAnalysis-static-devel
BuildRequires:	lib64LLVMXtensaCodeGen-static-devel
BuildRequires:	lib64LLVMXtensaAsmParser-static-devel
BuildRequires:	lib64LLVMXtensaDisassembler-static-devel
BuildRequires:	lib64LLVMXtensaDesc-static-devel
BuildRequires:	lib64LLVMXtensaInfo-static-devel
BuildRequires:	lib64LLVMSandboxIR-static-devel
BuildRequires:	lib64LLVMAsmParser-static-devel
BuildRequires:	lib64LLVMLineEditor-static-devel
BuildRequires:	lib64LLVMProfileData-static-devel
BuildRequires:	lib64LLVMCoverage-static-devel
BuildRequires:	lib64LLVMPasses-static-devel
BuildRequires:	lib64LLVMTargetParser-static-devel
BuildRequires:	lib64LLVMTextAPI-static-devel
BuildRequires:	lib64LLVMTextAPIBinaryReader-static-devel
BuildRequires:	lib64LLVMDlltoolDriver-static-devel
BuildRequires:	lib64LLVMLibDriver-static-devel
BuildRequires:	lib64LLVMXRay-static-devel
BuildRequires:	lib64LLVMWindowsDriver-static-devel
BuildRequires:	lib64LLVMWindowsManifest-static-devel
BuildRequires:	lib64LLVMSPIRVLib-static-devel
BuildRequires:	lib64LLVMBOLTCore-static-devel
BuildRequires:	lib64LLVMBOLTPasses-static-devel
BuildRequires:	lib64LLVMBOLTProfile-static-devel
BuildRequires:	lib64LLVMBOLTRewrite-static-devel
BuildRequires:	lib64LLVMBOLTRuntimeLibs-static-devel
BuildRequires:	lib64LLVMBOLTTargetAArch64-static-devel
BuildRequires:	lib64LLVMBOLTTargetX86-static-devel
BuildRequires:	lib64LLVMBOLTTargetRISCV-static-devel
BuildRequires:	lib64LLVMBOLTUtils-static-devel
BuildRequires:	lib64LLVMCFIVerify-static-devel
BuildRequires:	lib64LLVMDiff-static-devel
BuildRequires:	lib64LLVMExegesisX86-static-devel
BuildRequires:	lib64LLVMExegesisAArch64-static-devel
BuildRequires:	lib64LLVMExegesisPowerPC-static-devel
BuildRequires:	lib64LLVMExegesisMips-static-devel
BuildRequires:	lib64LLVMExegesis-static-devel
BuildRequires:	lib64LLVMOptDriver-static-devel



BuildSystem:	cmake
BuildOption:	-DCMAKE_INSTALL_LIBDIR:PATH="%{_libdir}/c3"
BuildOption:	-DCMAKE_INSTALL_BINDIR:PATH="%{_bindir}/c3c"

Patch0:			c3c-0.6.8.patch

%description
C3 is an evolution, not a revolution: the C-like for programmers who like C. C3
is a programming language that builds on the syntax and semantics of the C
language, with the goal of evolving it while still retaining familiarity for C
programmers.

C3 fits right into your C/C++ application with full C ABI compatibility out of
the box: no need for special "C compatible" types or functions, no limitations
on what C3 features you can use from C.

A simple and straightforward module system that doesn't get into the way with
defaults that makes sense.

Macros that are just as easy to read and write as regular functions. Packing
much more power than C's preprocessor, they're deliberately balanced to ensure
that code reading isn't made difficult.

%prep
%autosetup -p1

%files
%{_bindir}/%{name}
%{_libdir}/c3/std/*.c3
%{_libdir}/c3/std/*/*.c3
%{_libdir}/c3/std/*/*/*.c3
%{_mandir}/man1/%{name}.1.zst
%license LICENSE LICENSE_STDLIB
%doc	README.md
