# PPP DEBUGGER - PLUSH PUPPY PARALLEL DEBUGGER

## Introduction

The **PPP Debugger** (Plush Puppy Parallel Debugger) is an innovative tool designed to facilitate the debugging process for programs in parallel programming environments. With an intuitive graphical interface that integrates functionalities from GDB (GNU Debugger), the PPP Debugger is tailored to meet the needs of developers working with multicore systems who require an effective and accessible solution for identifying and correcting errors in their code.

## Download

You can download the executable for your system from the following link: [PPP Debugger Download](https://vinigperuzzi.github.io/PPP-Debugger/)

## Motivation

The **PPP Debugger** project was conceived during the final stages of my undergraduate studies in Computer Science at the Federal University of Pelotas (UFPel). The primary goal is to provide a graphical interface for GDB, with a special focus on programs that utilize the parallel programming paradigm. The need for an intuitive and accessible tool for developers working with multicore systems was the driving force behind the development of this software.

## Scientific Content

This project was developed as part of my thesis for my undergraduate degree. The complete work can be found in the UFPel library and serves as a foundation for future studies and developments in the field of parallel debugging. The research and results presented aim to contribute to the academic community by offering insights into debugging techniques in parallel programming environments.

## Features

The **PPP Debugger** offers the following features:

- **Intuitive Graphical Interface**: Easy navigation for both beginners and experienced developers.
- **Integration with GDB**: Access to all GDB functionalities through a graphical interface.
- **Support for Parallel Programming**: Specific features to debug applications using multiple threads and processes.
- **Thread Visualization**: Real-time monitoring of the state of running threads, facilitating the identification of concurrency issues.
- **Breakpoint Management**: Simple and visual creation and management of breakpoints.
- **Variable Display**: Real-time visualization of variables, allowing quick analysis of the program state.

## Prerequisites

Before running the PPP Debugger, ensure that the following requirements are met:

- **Operating System**: The PPP Debugger is compatible with Windows, macOS, and Linux.
- **GDB**: The GNU Debugger must be installed on your system. You can download it from the [official GDB website](https://www.gnu.org/software/gdb/).

## How to Run

To run the PPP Debugger, follow the steps below:

1. **Download the Executable**: Access the provided link above and select the appropriate version for your operating system.
2. **Installation**: You just have to unzip it and then run it (Because it do not have the certificate, it's possible that the system will show an security alert, don't worry, you can permit it)
3. **Usage**:
   - Start the PPP Debugger.
   - Configure the debugging environment (specify the executable to be debugged, parameters, etc.).
   - Use the interface to set breakpoints and monitor the execution of the program.

### Usage Examples

- **Debugging a Simple Program**: Use the tool to load a program that employs multiple threads and observe how the PPP Debugger allows for the identification of race conditions and synchronization problems.
- **Variable Analysis**: During execution, you can pause the program and check the values of variables in real-time, providing detailed control over the state of the application.

## Contributions

Contributions are welcome! If you wish to collaborate on the project, please follow these steps:

1. **Fork the Repository**: Create a copy of the repository to your account.
2. **Create a New Branch**: Work on a new feature or bug fix in a separate branch.
3. **Submit a Pull Request**: Send your changes to the original repository for review.

## Limitations

It is important to note that a significant limitation of the tool lies in how **pygdbmi** handles the inputs and outputs from GDB. The standard output of the program is managed by the program itself, meaning that GDB is unaware that the program is writing to the terminal. As a result, inputs and outputs are invisible to the graphical interface, which may limit the visibility of some real-time operations.

## Acknowledgments

I would like to thank everyone who contributed to the development of this project, especially my advisors and colleagues at UFPel. Your support and feedback were crucial to the completion of this work.

## License

This project are using technologies licensed under the LGPL License - see the [LICENSE](https://www.gnu.org/licenses/lgpl-3.0.pt-br.html) file for more details.


Happy coding! 🌐💻🧙‍♂️