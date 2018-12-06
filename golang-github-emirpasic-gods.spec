%global goipath  github.com/emirpasic/gods
Version: 1.9.0

%global common_description %{expand:
GoDS (Go Data Structures)

Implementation of various data structures and algorithms in Go.

Containers (Sets, Lists, Stacks, Maps, Trees), Sets (HashSet, TreeSet), Lists
(ArrayList, SinglyLinkedList, DoublyLinkedList), Stacks (LinkedListStack,
ArrayStack), Maps (HashMap, TreeMap, HashBidiMap, TreeBidiMap), Trees
(RedBlackTree, AVLTree, BTree, BinaryHeap), Comparators, Iterators, Enumerables,
Sort, JSON}

%gometa

Name: %{goname}
Release: 2%{?dist}
Summary: Implementation of various data structures and algorithms in Go
License: BSD and MIT
URL: %{gourl}
Source0: %{gosource}

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Dominik Mierzejewski <dominik@greysector.net> - 1.9.0-1
- First package for Fedora
