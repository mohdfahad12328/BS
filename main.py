import os
import sys
import subprocess

class Compiler:
    compiler_bin: str = None
    compiler_flags: list[str] = None
    
    def __init__(self, compiler_bin: str, compiler_flags: list[str] = []):
        self.compiler_bin = compiler_bin
        self.compiler_flags = compiler_flags

class Sources:
    sources: list[str] = None

    def __init__(self, sources: list[str] = []):
        self.sources = sources

class IncludeDirs:
    include_dirs: list[str] = None

    def __init__(self, include_dirs: list[str] = []):
        self.include_dirs = include_dirs

class Target:
    name: str = None
    compiler: Compiler = None
    sources: Sources = None

    def __init__(self, name: str, sources: Sources, compiler: Compiler):
        self.name = name
        self.compiler = compiler
        self.sources = sources

    def __repr__(self):
        return f"Target(name={self.name})"

    def run(self):
        os.mkdir("build")
        subprocess.run(
            [self.compiler.compiler_bin] + self.compiler.compiler_flags + self.sources.sources + ["-o", f"build/{self.name}"],
            check=True
        )
        print(f"Built target {self.name} with {self.compiler.compiler_bin}")

if __name__ == "__main__":
    gcc = Compiler("gcc", ["-O2", "-Wall"])
    sources = Sources(["main.c"])
    hello = Target("hello", sources, gcc)
    hello.run()