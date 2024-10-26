package utils

import "cmp"

type Node[T cmp.Ordered] struct {
	value T
	left  *Node[T]
	right *Node[T]
}

type BinarySearchTree[T cmp.Ordered] struct {
	root *Node[T]
}
