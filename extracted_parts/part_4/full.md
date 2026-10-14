PROOF. Let $X _ { 1 }$ and $X _ { 2 }$ be two matrices satisfying the Eqs. (3) through (6). By Eqs. (4) and (5), we have

$$
X _ { i } ^ { * } = X _ { i } ^ { * } A ^ { * } X _ { i } ^ { * } = A X _ { i } X _ { i } ^ { * } , \quad \quad i = 1 , 2 ,
$$

and hence $X _ { 1 } ^ { * } - X _ { 2 } ^ { * } = A ( X , X _ { 1 } ^ { * } - X , X _ { 2 } ^ { * } )$ . Thus

$$
\operatorname { I m } ( X _ { 1 } ^ { * } - X _ { 2 } ^ { * } ) \subset \operatorname { I m } A .\tag{7}
$$

On the other hand, using Eqs. (3) and (6), it is found that

$$
A ^ { * } = A ^ { * } X _ { i } ^ { * } A ^ { * } = X _ { i } A A ^ { * } , \quad \quad i = 1 , 2 ,
$$

which implies $( X _ { 1 } - X _ { 2 } ) A A ^ { * } = 0 \mathrm { o r } A A ^ { * } ( X _ { 1 } ^ { * } - X _ { 2 } ^ { * } ) = 0 .$ Hence

$$
\mathrm { I m } ( X _ { 1 } ^ { * } - X _ { 2 } ^ { * } ) \subset \mathrm { K e r } \ A A ^ { * } = \mathrm { K e r } \ A ^ { * }
$$

(by Exercise 5.3.6). But Ker $A ^ { * }$ is orthogonal to Im A (see Exercise 5.1.7) and therefore it follows from Eq. (7) that $X _ { 1 } ^ { * } - X _ { 2 } ^ { * } = 0 .$ ■

It was pointed out in Exercise 5.1.7 that for any $A \in \mathcal { F } ^ { m \times n }$

$$
\mathbf { I m } ~ A \oplus \mathbf { K e r } ~ A ^ { * } = { \mathcal { F } } ^ { m } ,
$$

$$
\operatorname { K e r } A \oplus \operatorname { I m } A ^ { * } = { \mathcal { F } } ^ { n } .
$$

Comparing this with Eqs. (1) and (2) the following proposition is obtained immediately.

Proposition 2. For any matrix A

$$
\begin{array} { r } { \operatorname { K e r } A ^ { + } = \operatorname { K e r } A ^ { * } , \qquad \operatorname { I m } A ^ { + } = \operatorname { I m } A ^ { * } . } \end{array}
$$

A straightforward computation can be applied to determine $A ^ { + }$ from A. Let r = rank A and let

$$
A = F R ^ { * } , \qquad F \in { \mathcal { F } } ^ { m \times r } , \qquad R ^ { * } \in { \mathcal { F } } ^ { r \times n }\tag{8}
$$

be a rank decomposition of A, that is, rank F = rank $R ^ { * } = r .$ Noting that the $r \times r$ matrices $F ^ { * } F$ and $R ^ { * } R$ are of full rank, and therefore invertible, we define the $n \times n$ matrix

$$
X = R ( R ^ { * } R ) ^ { - 1 } ( F ^ { * } F ) ^ { - 1 } F ^ { * } .\tag{9}
$$

It is easy to check that this is the Moore-Penrose inverse of $A ,$ that $X = A ^ { + }$ Note that the linearly independent columns of A can be chosen to be the columns of the matrix F in Eq. (8). This has the useful consequences of the next exercise.

Exercise 1. Let A be $m \times n$ and have full rank. Show that if $m \leq n ,$ then $A ^ { + } = A ^ { * } ( A A ^ { * } ) ^ { - 1 }$ and if $m \geq n ,$ then $A ^ { + } = ( A ^ { * } A ) ^ { - 1 } A ^ { * }$ □

Representation (9) can also be used in proving the following properties of the Moore-Penrose inverse.

Proposition 3. Let A+ be the Moore-Penrose inverse of A. Then $A ^ { + }$

(a) $( A ^ { * } ) ^ { + } = ( A ^ { + } ) ^ { * }$

(b) $( \alpha A ) ^ { + } = \alpha ^ { - 1 } A ^ { + }$ for any $\alpha \in \mathcal { F } , \alpha \neq 0$ 2

(c) If A is normal (Hermitian, positive semi-definite), then so is A+ ; $A ^ { + }$

(d) For unitary U, V,

$$
( U A V ) ^ { + } = V ^ { * } A ^ { + } U ^ { * } .
$$

ProoF. Let us illustrate the method used here on the proof of the assertion (d).

If $A = F R ^ { * }$ is a rank decomposition of A, then $( U F ) ( R ^ { * } V )$ is a rank decomposition for $U A V .$ Hence, using Eq. (9) and the unitary properties of U and V, we have

$$
\begin{array}{c} ( U A V ) ^ { + } = ( V ^ { * } R ) ( R ^ { * } V V ^ { * } R ) ^ { - 1 } ( F ^ { * } U U ^ { * } F ) ^ { - 1 } ( F ^ { * } U ^ { * } ) = V ^ { * } A ^ { + } U ^ { * } . \quad \mathbf { u } _ { L } \end{array}
$$

Additional properties of $A ^ { + }$ are listed in the next exercises.

## Exercise 2. Prove that

(a) ${ \boldsymbol { 0 } } ^ { + } = { \boldsymbol { 0 } } ^ { \mathtt { T } }$ ;

(b) $( A ^ { + } ) ^ { + } = A ;$

(c) $( A A ^ { * } ) ^ { + } = ( A ^ { + } ) ^ { * } A ^ { + }$ and $( A ^ { * } A ) ^ { + } = A ^ { + } ( A ^ { + } ) ^ { * }$ 2

(d) $( A ^ { k } ) ^ { + } = ( A ^ { + } ) ^ { k }$ for any positive integer k and a normal matrix A.

## Exercise 3. Show that

$$
A ^ { + } A { \bf x } = { \bf x } , \qquad A A ^ { + } y = { \bf y } ,
$$

for any ${ \mathfrak { x } } \in$ Im $A ^ { * } , y \in$ Im A.

## Hint. Use Exercise 12.7.2 and Proposition 2.

Now recall that in the proofs of Theorems 5.7.1 and 5.7.2, we introduced a pair of orthonormal eigenbases $\{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \ldots , \pmb { x } _ { n } \}$ and $\{ y _ { 1 } , y _ { 2 } , \dots , y _ { m } \}$ of the matrices $A ^ { * } A$ and $A A ^ { * }$ , respectively, such that

$$
A \mathbf { x } _ { i } = { \left\{ \begin{array} { l l } { s _ { i } \mathbf { y } _ { i } } & { \quad { \mathrm { i f } } \quad i = 1 , 2 , \ldots , r , } \\ { \mathbf { 0 } } & { \quad { \mathrm { i f } } \quad i = r + 1 , \ldots , n , } \end{array} \right. }\tag{10}
$$

where it is assumed that the nonzero singular values $s _ { i } ( 1 \leq i \leq r )$ of A are associated with the eigenvectors $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x _ { r } }$ . Note that since $A ^ { * } A { \bf x } _ { i } =$ $s _ { i } ^ { 2 } { \pmb x } _ { i }$ for $i = 1 , 2 , \ldots , n$ , the multiplication of (10) by A\* on the left yields $A ^ { * }$

$$
\begin{array} { r } { A ^ { * } y _ { i } = \left\{ \begin{array} { l l } { s _ { i } \mathbf { x } _ { i } } & { \quad \mathrm { i f } \quad i = 1 , 2 , \ldots , r , } \\ { 0 } & { \quad \mathrm { i f } \quad i = r + 1 , \ldots , m . } \end{array} \right. } \end{array}\tag{11}
$$

The bases constructed in this way are called the singular bases of A. It turns out that the singular bases allow us to gain deeper insight into the structure of Moore-Penrose inverses.

Proposition 4. Let $A \in \mathcal { F } ^ { m \times n }$ and let $s _ { 1 } \geq s _ { 2 } \geq \cdot \cdot \cdot \geq s _ { r } > 0 = s _ { r + 1 } = \cdot \cdot \cdot = s _ { n }$ be the singular values of A. Then $s _ { 1 } ^ { - 1 } , s _ { 2 } ^ { - 1 } , \ldots , s _ { r } ^ { - 1 }$ are the nonzero singular values of $A ^ { + }$ . Moreover, $i f \left\{ x _ { i } \right\} _ { i = 1 } ^ { n }$ and $\left\{ y _ { i } \right\} _ { i = 1 } ^ { m }$ are singular bases of A, then $\left\{ y _ { i } \right\} _ { i = 1 } ^ { m }$ and $\left\{ x _ { i } \right\} _ { i = 1 } ^ { n }$ are singular bases of $A ^ { + }$ , that is,

$$
A ^ { + } \mathbf { y } _ { i } = \left\{ \begin{array} { l l } { s _ { i } ^ { - 1 } \mathbf { x } _ { i } } & { \quad i f \quad i = 1 , 2 , \ldots , r , } \\ { 0 } & { \quad i f \quad i = r + 1 , \ldots , m , } \end{array} \right.\tag{12}
$$

$$
( A ^ { + } ) ^ { * } { \pmb x } _ { i } = \left\{ \begin{array} { l l } { s _ { i } ^ { - 1 } { \pmb y } _ { i } \quad } & { i f \quad i = 1 , 2 , \ldots , r , } \\ { 0 \quad } & { i f \quad i = r + 1 , \ldots , n . } \end{array} \right.\tag{13}
$$

PROOF. Consider the matrix $( A ^ { + } ) ^ { * } A ^ { + }$ and observe that, by Exercise 2(c) and Proposition 2,

$$
\mathrm { K e r } ( ( A ^ { + } ) ^ { * } A ^ { + } ) = \mathrm { K e r } ( ( A A ^ { * } ) ^ { + } ) = \mathrm { K e r } A A ^ { * } ,
$$

and each subspace has dimension $m - r .$ Thus $A ^ { + }$ has $m - r$ zero singular values and the bases $\{ y _ { j } \} _ { j = 1 } ^ { m }$ and $\left\{ x _ { i } \right\} _ { i = 1 } ^ { n }$ can be used as singular bases of $A ^ { + }$ Furthermore, applying $A ^ { + }$ to Eqs. (10) and using the first result of Exercise 3, we obtain, for $\pmb { x _ { i } } \in$ Im $A ^ { * } , i = 1 , 2 , \ldots , n .$

$$
\begin{array} { r } { { \bf x } _ { i } = A ^ { + } A { \bf x } _ { i } = \left\{ \begin{array} { l l } { s _ { i } A ^ { + } { \bf y } _ { i } \quad } & { \mathrm { i f } \quad i = 1 , 2 , \ldots , r , } \\ { { \bf \theta } \quad } & { \mathrm { i f } \quad i = r + 1 , \ldots , n , } \end{array} \right. } \end{array}
$$

which implies (12). Clearly, $s _ { i } ^ { - 1 } ( i = 1 , 2 , . . . , r )$ are the nonzero singular values of $A ^ { + }$

Now rewrite the first relation in Exercise 3 for the matrix $A ^ { * }$

$$
( A ^ { * } ) ^ { + } A ^ { * } z = z ,\tag{14}
$$

for any $z \in$ Im $A ,$ and apply $( A ^ { + } ) ^ { * } = ( A ^ { * } ) ^ { + }$ to (11). Then, since $y _ { 1 } , \ldots , y _ { r }$ belong to Im A, we have

$$
\begin{array} { r l } & { y _ { i } = ( A ^ { + } ) ^ { * } A ^ { * } y _ { i } = \left\{ \begin{array} { l l } { s _ { i } ( A ^ { + } ) ^ { * } x _ { i } \quad } & { \mathrm { i f } \quad i = 1 , 2 , \ldots , r , } \\ { 0 \quad } & { \mathrm { i f } \quad i = r + 1 , \ldots , n , } \end{array} \right. } \end{array}
$$

and the result in (13) follows.

Exercise 4. If $A = U D V ^ { * }$ as in Theorem 5.7.2, and det $D \neq 0 ,$ ,show that $A ^ { + } = V D ^ { - 1 } U ^ { * } . \quad \bigsqcup$

## 12.9 The Best Approximate Solution of the Equation $A x = b$

The Moore-Penrose inverse has a beautiful application in the study of the equation

$$
A \pmb { x } = \pmb { b } ,\tag{1}
$$

where $A \in \mathcal { F } ^ { m \times n }$ and $\pmb { b } \in \mathcal { F } ^ { m }$ , and we wish to solve for $\pmb { x } \in \mathcal { F } ^ { n } ,$ We have seen that there is a solution of Eq. (1) if and only if $\pmb { b } \in$ Im A. In general, the solution set is a “manifold" of vectors obtained by a “shift" of Ker A, as described in Theorem 3.10.2. Using Exercise 12.8.3, we see that the vector ${ \pmb x } _ { 0 } = { \pmb A } ^ { + } { \pmb b }$ is one of the solutions in this manifold :

$$
\pmb { A x } _ { 0 } = \pmb { A } \pmb { A } ^ { + } \pmb { b } = \pmb { b } ,
$$

and it is the only solution of Eq. (1) if and only if A is nonsingular, and then $A ^ { + } = A ^ { - 1 }$

Also, a vector $\pmb { x } \in \mathcal { F } ^ { n }$ is a solution of $\mathbf { E q . } \left( 1 \right)$ if and only if $\| A \pmb { x } - \pmb { b } \| = 0$ for any vector norm  ∥ in ${ \mathcal { F } } ^ { m }$

Consider the case $\Delta \notin$ Im A. Now there are no solutions of Eq. (1) but, keeping in mind the preceding remark, we can define an approximate solution of $A \mathbf { x } = \mathbf { b }$ to be a vector $\pmb { x _ { 0 } }$ for which $\| A \mathbf { x } - \mathbf { b } \|$ is minimized:

$$
\| A \mathbf { x } _ { 0 } - b \| = \operatorname* { m i n } _ { \mathbf { x } \in \mathcal { F } ^ { n } } \| A \mathbf { x } - b \|\tag{2}
$$

in the Euclidean vector norm ∥ |. (Then $\pmb { x _ { 0 } }$ is also known as a least squares solution of the inconsistent, or overdetermined, system $\pmb { A } \pmb { x } = \pmb { b }$ . Note that if $\pmb { x _ { 0 } }$ is such a vector, so is any vector of the form $\pmb { x } _ { 0 } + \pmb { u }$ where $u \in \mathrm { K e r } A . )$

Now for any $A \in \mathcal { F } ^ { m \times n }$ and any $\pmb { b } \in \mathcal { F } ^ { m }$ , the best approximate solution of Eq. (1) is a vector $\pmb { x _ { 0 } } \in \mathcal { F } ^ { n }$ of the least euclidean length satisfying Eq. (2). We are going to show that ${ \pmb x } _ { 0 } = { \pmb A } ^ { + } { \pmb b }$ is such a vector. Thus, if $\pmb { b } \in$ Im A, then $A ^ { + } b$ will be the vector of least norm in the manifold of solutions of Eq. (1) (or that equation's unique solution), and if $\Delta \notin$ Im $A ,$ then $A ^ { + } b$ is the unique vector which attains the minimum of (2), and also has minimum norm.

Theorem 1. The vector ${ \pmb x } _ { 0 } = A ^ { + } { \pmb b }$ is the best approximate solution of $A \pmb { x } = \pmb { b }$

PROOF. For any $\pmb { x } \in \mathcal { F } ^ { n }$ write

$$
A { \bf x } - { \bf b } = A ( { \bf x } - A ^ { + } { \bf b } ) + ( I - A A ^ { + } ) ( - { \bf b } ) ,
$$

and observe that, because $I - A A ^ { + }$ is the orthogonal projector onto $( \operatorname { I m } A ) ^ { \perp }$ (ref. Corollary 12.7.1), the summands on the right are mutually orthogonal vectors:

$$
A ( { \bf x } - A ^ { + } b ) \in \mathrm { I m } \ A , \qquad ( I - A A ^ { + } ) ( - b ) \in ( \mathrm { I m } \ A ) ^ { \bot } .
$$

Thus, the extension of the Pythagorean theorem implies

$$
\begin{array} { c } { { \| A { \mathbf { x } } - { \pmb { b } } \| ^ { 2 } = \| A ( { \pmb x } - { \pmb A } ^ { + } { \pmb b } ) \| ^ { 2 } + \| ( { \pmb I } - A { \pmb A } ^ { + } ) ( - { \pmb b } ) \| ^ { 2 } } } \\ { { = \| A ( { \pmb x } - { \pmb x } _ { 0 } ) \| ^ { 2 } + \| A { \pmb x } _ { 0 } - { \pmb b } \| ^ { 2 } } } \end{array}\tag{3}
$$

and, consequently, the relation (2).

It remains only to show that $\| \pmb { x } _ { 1 } \| \geq \| \pmb { x } _ { 0 } \|$ for any vector $\pmb { x } _ { 1 } \in \mathcal { F } ^ { n }$ minimizing $\| A \mathbf { x } - \pmb { b } \|$ . But then, substituting $\pmb { x _ { 1 } }$ instead of x in Eq. (3), $\| { \pmb { A } } { \pmb { x } } _ { 1 } - { \pmb { b } } \| =$ $\| A \mathbf { x _ { 0 } } - b \|$ yields $A ( \pmb { x } _ { 1 } - \pmb { x } _ { 0 } ) = \pmb { \theta }$ , and hence ${ \pmb x } _ { 1 } - { \pmb x } _ { 0 } \in { \pmb K }$ er A. According to Proposition 12.8.2, ${ \pmb x } _ { 0 } = { \pmb A } ^ { + } { \pmb b } \in$ Im $A ^ { * }$ and, since Ker $A \perp$ Im $A ^ { * }$ , it follows that ${ \pmb x } _ { 0 } \perp ( { \pmb x } _ { 1 } - { \pmb x } _ { 0 } )$ . Applying the Pythagorean theorem again, we finally obtain

$$
\| { \pmb x } _ { 1 } \| ^ { 2 } = \| { \pmb x } _ { 0 } \| ^ { 2 } + \| { \pmb x } _ { 1 } - { \pmb x } _ { 0 } \| ^ { 2 } \geq \| { \pmb x } _ { 0 } \| ^ { 2 } .
$$

The proof of the theorem is complete.■

Note that the uniqueness of the Moore-Penrose inverse yields the uniqueness of the best approximate solution of Eq. (1).

Exercise 1. Check that the best approximate solution of the equation $\pmb { A } \pmb { x } = \pmb { b } ,$ where

$$
A = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 2 } & { 0 } \\ { - 1 } & { 3 } \end{array} \right] } , \qquad b = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { 2 } \end{array} \right] } ,
$$

is given by the vector $\begin{array} { r } { \pmb { x } _ { 0 } = \frac { 1 } { 1 4 } [ 1 \quad 1 0 ] ^ { \mathbf { T } } } \end{array}$ . Find the best approximate solution of $B \mathbf { x } = c \mathrm { i f } B = A ^ { \mathrm { T } }$ and $\pmb { c } = [ 1 \quad 1 ] ^ { \mathbf { r } }$

Exercise 2. Generalize the idea of the “best approximate solution" for the matrix equation $A X = B ,$ where $\ b { A } \in \mathbb { C } ^ { m \times n } , \ \ b { X } \in \mathbb { C } ^ { n \times k }$ , and $\pmb { { \cal B } } \in \mathbb { C } ^ { m \times k }$ , and obtain the formula $X _ { 0 } = A ^ { + } B$ for this solution.

Exercise 3. Show that an approximate solution of $A \pmb { x } = \pmb { b }$ is the best approximate solution of the equation if and only if it belongs to the image of $A ^ { * } , \sqsubseteq$

If the singular basis $\{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \ldots , \pmb { x } _ { n } \}$ of $A \in { \mathcal { F } } ^ { m \times n }$ in the linear space ${ \mathcal { F } } ^ { n }$ and the nonzero singular values $s _ { 1 } , s _ { 2 } , \ldots , s _ { r }$ of A are known, then an explicit form of the best approximate solution of Eq. (1) can be given.

Theorem 2. With the notation of the preceding paragraph, the best approximate solution of $A \mathbf { x } = \mathbf { b }$ is given by the formula

$$
{ \pmb x } _ { 0 } = \alpha _ { 1 } { \pmb x } _ { 1 } + \alpha _ { 2 } { \pmb x } _ { 2 } + \cdot \cdot \cdot + \alpha _ { r } { \pmb x } _ { r } ,\tag{4}
$$

where

$$
\alpha _ { i } = \frac { ( A ^ { * } b , x _ { i } ) } { s _ { i } ^ { 2 } } , \qquad i = 1 , 2 , \ldots , r .\tag{5}
$$

ProoF. In Eq. (5) and in this proof we use the notation $^ { ( \mathrm { ~ , ~ } ) }$ for the standard inner product on ${ \mathcal { F } } ^ { m }$ , or on ${ \mathcal { F } } ^ { n }$ . Thus, $( u , v ) = v ^ { * } u { \mathrm { : } }$ Let $y _ { 1 } , y _ { 2 } , \ldots , y _ { m }$ be

an orthonormal eigenbasis of $A A ^ { * }$ in ${ \mathcal { F } } ^ { m }$ (the second singular basis of A). Write the representation of $\pmb { b }$ with respect to this basis:

$$
\pmb { b } = \beta _ { 1 } \pmb { y } _ { 1 } + \beta _ { 2 } \pmb { y } _ { 2 } + \cdot \cdot \cdot + \beta _ { m } \pmb { y } _ { m } ,
$$

and note that $\beta _ { i } = ( b , \mathbf { y } _ { i } ) , \ i = 1 , 2 , \ldots , m$ Then, using Eq. (12.8.12), we find that

$$
{ \pmb x } _ { 0 } = A ^ { + } { \pmb b } = \sum _ { i = 1 } ^ { m } \beta _ { i } A ^ { + } { \pmb y } _ { i } = \sum _ { i = 1 } ^ { r } \beta _ { i } s _ { i } ^ { - 1 } { \pmb x } _ { i } .
$$

In view of Eq. (12.8.10),

$$
{ \bf y } _ { i } = \frac { 1 } { s _ { i } } A { \bf x } _ { i } , \mathrm { ~ } i = 1 , 2 , \ldots , r ,
$$

and therefore

$$
\beta _ { i } s _ { i } ^ { - 1 } = \frac { 1 } { s _ { i } ^ { 2 } } \left( \pmb { b } , A \pmb { x } _ { i } \right) = \frac { 1 } { s _ { i } ^ { 2 } } \left( A ^ { * } \pmb { b } , \pmb { x } _ { i } \right) ,
$$

for $i = 1 , 2 , \ldots , r .$ This completes the proof.

## 12.10 Miscellaneous Exercises

1. Let $\ b { A } \in \mathcal { F } ^ { \ b { m } \times \ b { l } }$ and $B \in \mathcal { F } ^ { n \times k }$

(a) Prove Proposition 12.1.4 for rectangular matrices of appropriate sizes.

(b) Show that there are permutation matrices $P _ { 1 }$ and $P _ { 2 }$ such that $P _ { 1 } ( A \otimes B ) P _ { 2 } = B \otimes A .$ (This is a generalization of Proposition 12.1.3.)

2. If $\{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \dots , \pmb { x } _ { m } \}$ is a basis in ${ \mathcal { F } } ^ { m }$ and $\{ \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } , \ldots , \mathbf { y } _ { n } \}$ is a basis in ${ \mathcal { F } } ^ { n }$ prove that the Kronecker products ${ \pmb y } _ { j } ^ { \operatorname { T } } \otimes { \pmb x } _ { i } , ~ 1 \le j \le n , ~ 1 \le i \le m$ constitute a basis in $\mathcal { F } ^ { m \times n }$

3. Prove that the Kronecker product of any two square unitary (Hermitian, positive definite) matrices is a unitary (Hermitian, positive definite) matrix.

4. Let $A \in { \mathcal { F } } ^ { m \times m } , B \in { \mathcal { F } } ^ { n \times n }$ be fixed and consider the transformations $T _ { 1 }$ $T _ { 2 } \in \mathcal { L } ( \mathcal { F } ^ { m \times n } )$ defined by the rules

$$
T _ { 1 } ( X ) = A X B , \qquad T _ { 2 } ( X ) = A X + X B ,
$$

for any $X \in \mathcal { F } ^ { m \times n }$ . Prove that the matrix representations of $T _ { 1 }$ and $T _ { 2 }$ with respect to the standard basis $[ E _ { i j } ] _ { i , j = 1 } ^ { m , n }$ for ${ \mathcal { F } } ^ { m \times 1 }$ " (see Exercise 3.5.1(c)) are the matrices

$$
B ^ { \boldsymbol { \mathsf { T } } } \otimes A \qquad \mathrm { a n d } \qquad ( I _ { n } \otimes A ) + ( B ^ { \boldsymbol { \mathsf { T } } } \otimes I _ { m } ) ,
$$

respectively.

5. If $A \in \mathcal { F } ^ { m \times m } , B \in \mathcal { F } ^ { n \times n }$ , and $\parallel \parallel$ denotes either the spectral norm or the norm of Exercise 10.4.9, prove that

$$
\| A \otimes B \| = \| A \| \| B \| .
$$

Hint. For the spectral norm use Exercise 10.4.5. Compute row sums of the absolute values of the elements to prove the equality for the second norm.

6. Let $A \in \mathcal { F } ^ { m \times m }$ and $C \in \mathcal { F } ^ { n \times n }$ be invertible matrices. Prove that if $B \in \mathcal { F } ^ { m \times n }$ is left (respectively, right) invertible, so is the matrix ABC.

7. Let $A \in \mathcal { F } ^ { m \times n }$ be a left (or right) invertible matrix. Prove that there exists $\varepsilon > 0$ such that every matrix $B \in \mathcal { F } ^ { m \times n }$ satisfying the condition $\| A - B \| < \varepsilon$ also is left (or right) invertible.

In other words, one-sided invertibility is “stable" under small perturbations.

Hint. Pick $\varepsilon < \lVert A _ { \mathrm { L } } ^ { - 1 } \rVert ^ { - 1 }$ for the left invertibility case and show that $( I + C ) ^ { - 1 } A _ { \mathbf { L } } ^ { - 1 } B = I ,$ where $C = A _ { \mathrm { L } } ^ { - 1 } ( B - A )$

8. Let $A \in { \mathcal { F } } ^ { m \times r } , B \in { \mathcal { F } } ^ { r \times n } \left( r \leq \operatorname* { m i n } ( m , n ) \right)$ be matrices of full rank. Prove that

$$
( A B ) ^ { + } = B ^ { + } A ^ { + } .
$$

Find an example of two matrices A and B such that this relation does not hold.

Hint. Use Eq. (12.8.9) with $A = F , B = R ^ { * }$

9. If $A \in { \mathcal { F } } ^ { n \times n }$ and $A = H U = U _ { 1 } H _ { 1 }$ are the polar decompositions of A, show that $A ^ { + } = U ^ { * } H ^ { + } = H _ { 1 } ^ { + } U _ { 1 } ^ { * }$ are those of $A ^ { + }$

Hint. Use Proposition 12.8.3d.

10. Prove that a matrix X is the Moore-Penrose inverse of A if and only if

$$
X A A ^ { * } = A ^ { * } \qquad { \mathrm { a n d } } \qquad X = B A ^ { * }
$$

for some matrix B.

11. Verify that the matrices

$$
{ \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] } \qquad { \mathrm { a n d } } \qquad { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] }
$$

are mutual Moore-Penrose inverses, each of the other.

12. Consider the permutation matrix P of Proposition 12.1.3. Show that when $m = n , ~ P$ is a symmetric matrix. In this case, show also that $A \in { \mathcal { F } } ^ { n \times n }$ is a symmetric matrix if and only if vec $A = P ( \sec A )$

13. (a) Generalize Exercise 12.1.3(b) to admit rectangular A and B. (b) Let $A \in \mathbb { C } ^ { m \times n }$ and rank $A = r .$ Note that the equation $A X A = A$ (Eq. (12.7.1)) can be written in the form $( A ^ { \boldsymbol { \mathsf { T } } } \otimes A )$ vec X = vec A. Find the rank of $A ^ { \boldsymbol { \mathsf { T } } } \otimes A$ . What can be said about the number of linearly independent solutions of $A X A = A { \overset { \cdot } { ! } }$

14. Show by example that, in general, $( A B ) ^ { + } \neq B ^ { + } A ^ { + }$

15. If $B ^ { + }$ is the Moore-Penrose inverse of B and $\pmb { A } = [ \pmb { \bar { B } } ]$ , show that $A ^ { + } =$ 12 $\cdot \left[ B ^ { + } B ^ { + } \right]$

## Stability Problems

In Section 12.3 we defined a stable matrix. Matrices of this kind are of particular significance in the study of differential equations, as demonstrated by the following proposition: The matrix A is stable if and only $i f , f o r$ every solution vector ${ \pmb x } ( t )$ of ${ \dot { \pmb { x } } } = { \pmb { A } } { \pmb { x } } ,$ we have ${ \pmb x } ( t )  { \pmb \theta }$ as $t \to \infty$ . This result is evident when the solutions ${ \bf x } ( t ) = e ^ { A t } { \bf x _ { 0 } }$ of the equation $\dot { \pmb { x } } = \pmb { A } \pmb { x }$ (Theorem 9.10.3) are examined, as in the proof of Theorem 12.3.3 (see also Exercise 10.9.14).

In terms of inertia, a matrix $A \in \mathbb { C } ^ { n \times n }$ is stable if and only if its inertia (see Section 5.5) is $( 0 , n , 0 )$ . The Lyapunov method, presented in this chapter, expresses the inertia of any given matrix in terms of the inertia of a related Hermitian matrix and is of great theoretical importance.

In particular, the Lyapunov theory provides a criterion for a matrix to be stable that avoids a direct calculation of the characteristic polynomial of A and its zeros. Moreover, given a scalar polynomial with real coefficients, the distribution of its zeros with respect to the imaginary axis (the Routh-Hurwitz problem) will be obtained by use of the method of Lyapunov. Also, a solution of the Schur-Cohn problem of zero location with respect to the unit circle, as well as other problems concerning the location of zeros of a real polynomial, will be discussed.

## 13.1 The Lyapunov Stability Theory and Its Extensions

To illustrate Lyapunov's approach to stability theory, we shall be concerned in the beginning of this section with quadratic forms. Denote by v the quadratic form whose matrix is a real and symmetric matrix V (see Section

5.10), and similarly for w and W. The positive definiteness of V (or of W) will be expressed by writing $v > 0$ (or $w > 0 )$ and similarly for positive semi-definite forms.

Let $\pmb { A } \in \mathbb { R } ^ { n \times n }$ and consider the differential equation

$$
{ \dot { \mathbf { x } } } ( t ) = A { \mathbf { x } } ( t ) .\tag{1}
$$

Evaluate a quadratic form v at a solution $\pmb { x } ( t )$ of Eq. (1), where $\ b { x } ( t ) \in \mathbb { R } ^ { n }$ for each t. We have $v ( { \boldsymbol { \mathbf { x } } } ) = { \boldsymbol { \mathbf { \mathit { x } } } } ^ { \mathbf { T } } V { \boldsymbol { \mathbf { \mathit { x } } } }$ and hence

$$
\dot { v } ( { \pmb x } ) = \dot { { \pmb x } } ^ { \operatorname { T } } V { \pmb x } + { \pmb x } ^ { \operatorname { T } } V \dot { \pmb x } = { \pmb x } ^ { \operatorname { T } } ( A ^ { \operatorname { T } } V + V A ) { \pmb x } .
$$

If we write

$$
\begin{array} { r } { \boldsymbol { A } ^ { \mathrm { T } } \boldsymbol { V } + \boldsymbol { V } \boldsymbol { A } = - \boldsymbol { W } , } \end{array}\tag{2}
$$

then clearly W is real and symmetric and ${ \dot { v } } ( { \bf x } ) = - w ( { \bf x } )$ where $w ( { \pmb x } ) =$ $\mathbf { x } ^ { \mathrm { { T } } } W \mathbf { x }$

Lyapunov noted that, given a positive definite form w, the stability of A can be characterized by the existence of a positive definite solution matrix V for Eq. (2), for then $v ( { \pmb x } )$ is a viable measure of the size of x. Thus the equation ${ \dot { \pmb { x } } } = A { \pmb { x } }$ has the property that $\begin{array} { r } { \operatorname* { l i m } _ { t \to \infty } \pmb { x } ( t ) = 0 } \end{array}$ for every solution vector x(t) if and only if we can find positive definite forms w and v such that ${ \dot { v } } ( { \pmb x } ) =$ $- w ( { \pmb x } )$ . Furthermore, the positive definite matrix W of Eq. (2) can be chosen arbitrarily, so a natural choice is often $W = I .$

To see the significance of this heuristically, let A be $2 \times 2$ and consider a solution

$$
{ \pmb x } ( t ) = \left[ { \pmb x } _ { 1 } ( t ) \right] ,
$$

in which $x _ { 1 } ( t )$ and ${ \boldsymbol x } _ { 2 } ( t )$ are real-valued functions of t. The level curves for a positive definite form v (see Exercise 5.10.6) are ellipses in the $\mathbf { { x } _ { 1 } } , \mathbf { { x } _ { 2 } }$ plane (Fig. 1), and if ${ \pmb x } _ { 0 } = { \pmb x } ( t _ { 0 } )$ we locate a point on the ellipse $v ( { \bf { x } } ) = v ( { \bf { x } } _ { 0 } )$ corresponding to ${ \bf \mathfrak { x } } ( t _ { 0 } )$ . Now consider the continuous path (trajectory) of the solution ${ \pmb x } ( t )$ in a neighbourhood of $( x _ { 1 } ( t _ { 0 } ) , x _ { 2 } ( t _ { 0 } ) )$ . If $w > 0$ then $\dot { v } < 0 .$ and the path must go inside the ellipse $v ( { \bf { x } } ) = v ( { \bf { x } } _ { 0 } )$ as t increases. Furthermore, the path must come within an arbitrarily small distance of the origin for sufficiently large t.

Returning to a more precise and general discussion, let us now state an algebraic version of the classical Lyapunov theorem. More general inertia theorems are to be proved later in this section, as well as a more general stability theorem (Theorem 5).

![](images/0ce9d9801add4e3b474083731eda06db53aa0f352177e74c4cfa4ba17afd5b1d.jpg)  
Fig. 13.1 The trajectory for a solution when A is stable.

Theorem 1 (A. M. Lyapunov†). Let A, $W \in \mathbb { C } ^ { n \times n }$ and let W be positive defnite.

(a) If A is stable then the equation

$$
A H + H A ^ { * } = W\tag{3}
$$

has a unique solution matrix H and H is negative deinite.

(b) If there is a negative definite matrix H satisfying Eq. (3), then A is stable.

ProoF. (a) Let A be stable. Then A and $- A ^ { * }$ obviously have no eigenvalues in common and therefore Theorem 12.3.2 implies the solvability and uniqueness of the solution of Eq. (3). We may use Theorem 12.3.3 to write the solution H of Eq. (1) explicitly in the form

$$
H = - \int _ { 0 } ^ { \infty } e ^ { A t } W e ^ { A ^ { \ast } t } d t .
$$

To show that $H < O$ , compute

$$
x ^ { * } H x = - \int _ { 0 } ^ { \infty } ( x ^ { * } e ^ { A t } ) W ( x ^ { * } e ^ { A t } ) ^ { * } \ d t ,\tag{4}
$$

and observe that the positive definiteness of W and the nonsingularity of $e ^ { A t }$ for all t yield the positivity of the integrand in Eq. (4). Hence $x ^ { * } H x < 0$ for all nonzero $\pmb { x } \in \mathbb { C } ^ { n }$ and thus $H < \theta$

(b) Conversely, let λ be an eigenvalue of $A ^ { * } ,$ where $A ^ { * } x = \lambda { \bf { x } }$ with $\pmb { x } \neq \pmb { \theta }$ . Then we also have ${ \pmb x } ^ { * } { \pmb A } = \bar { \lambda } { \pmb x } ^ { * }$ . Multiplying Eq. (3) on the left and right by $\pmb { x } ^ { * }$ and x, respectively, we obtain

$$
( \bar { \lambda } + \lambda ) { \pmb x } ^ { * } H { \pmb x } = { \pmb x } ^ { * } W { \pmb x } .\tag{5}
$$

Our hypothesis implies that $x ^ { * } H x < 0$ and also ${ \pmb x } ^ { * } W { \pmb x } > 0 ,$ so we have $\bar { \lambda } + \lambda < 0 ,$ that is, $\mathcal { R } \mathscr { \lambda } < 0$ . Since this is true for each eigenvalue λ, it follows that A is stable.

Note that, in fact, a slightly stronger statement than part (b) of the theorem has been proved. If H is negative definite and satisfies the Lyapunov equation $A H + H A ^ { * } = W$ , then the stability of A can be deduced if ${ \pmb x } ^ { * } { \pmb W } { \pmb x } < 0$ for just one eigenvector x associated with each eigenvalue of A\*. Thus, if A has $A ^ { * }$ multiple eigenvalues, then W need not be definite on the whole space $\mathbb { C } ^ { n } .$

Exercise 1. Verify that if $a > 0$ then both eigenvalues of

$$
A = { \binom { 7 0 \ - 1 } { 1 } }
$$

have positive real parts. Show that the matrix

$$
H = \left[ \begin{array} { c c } { { 4 + a ^ { 2 } } } & { { - 2 a } } \\ { { - 2 a } } & { { 4 + a ^ { 2 } } } \end{array} \right]
$$

is positive definite, and so is $A H + H A ^ { \boldsymbol { \mathsf { T } } }$

Exercise 2. Check that the Matrix

$$
A = P ( S - Q ) ,
$$

where P and Q are positive definite, is stable for any skew-Hermitian matrix S.   
Hint. Compute $A ^ { * } P ^ { - 1 } + P ^ { - 1 } A$ and use Theorem 1.

Exercise 3. Show that if $\mathcal { R } \epsilon \ A = \textstyle { \frac { 1 } { 2 } } ( A + A ^ { * } )$ is negative definite then A is stable. Show that the converse does not hold by considering the matrix

$$
A = { \left[ \begin{array} { l l } { - \varepsilon } & { 1 } \\ { 0 } & { - \varepsilon } \end{array} \right] } ,
$$

where $\varepsilon > 0$ is small. □

In numerical practice, we can decide whether a given real matrix A is stable by solving for H in the equation $A H + H A ^ { * } = I ( \operatorname { o r } A H + H A ^ { * } = W ,$ for some other choice of W) and then applying the result of Exercise 8.5.2 to decide whether H is negative definite. Thus, A is stable if and only if the leading principal minors $d _ { 1 } , d _ { 2 } , \ldots , d _ { n }$ of H satisfy the conditions

$$
d _ { 1 } < 0 \qquad \mathrm { a n d } \qquad d _ { i } d _ { i + 1 } < 0 , i = 1 , 2 , \ldots , n - 1 .
$$

If the equation $A H + H A ^ { * } = I$ can be solved to give the coefficients of H explicitly in terms of the elements of A, then we obtain a direct determinantal characterization of stable matrices. For general matrices this is not a practical proposition, but for relatively simple classes of matrices, explicit stability criteria may be obtained in this way. In subsequent sections we develop this possibility in the particularly important case in which A is defined directly by its characteristic polynomial, for example, when A is a companion matrix. Here we keep the hypothesis that W is positive definite in Eq. (3), and we seek some connection between the inertia of A and that of H (where $H ^ { * } = H )$ , which should reduce to the hypothesis of Theorem 1 when A is stable.

We now consider a generalization of Lyapunov's theorem due to M. G. Krein† in the USSR and, independently, to A. Ostrowski and H. Schneider in the West.

Theorem 2. Let $\ b { A } \in \mathbb { C } ^ { n \times n }$ . If H is a Hermitian matrix such that

$$
A H + H A ^ { * } = W , \qquad W > 0 ,\tag{6}
$$

then H is nonsingular and

$$
\pi ( A ) = \pi ( H ) , \qquad \nu ( A ) = \nu ( H ) , \qquad \delta ( A ) = \delta ( H ) = 0 .\tag{7}
$$

Conversely, if $\delta ( A ) = 0 ,$ then there exists a Hermitian matrix H such that Eqs. (6) and (7) hold.

ProoF. Let Eq. (6) hold. Proceeding as in the proof of Theorem 1(b), we obtain Eq. (5), which shows that $W > 0$ yields $\lambda + \bar { \lambda } \neq 0$ Thus A has no pure imaginary eigenvalues and therefore In $A = \{ p , n - p , 0 \}$ for some integer $p \leq n .$ A Jordan form J of A can then be written in the form

$$
P ^ { - 1 } A P = J = { \left[ \begin{array} { l l } { J _ { 1 } } & { \ O } \\ { 0 } & { J _ { 2 } } \end{array} \right] } ,\tag{8}
$$

where $\begin{array} { r } { J _ { 1 } \in \mathbb { C } ^ { p \times p } , \quad J _ { 2 } \in \mathbb { C } ^ { ( n - p ) \times ( n - p ) } ; } \end{array}$ and In ${ \boldsymbol { J } } _ { 1 } = \{ p , 0 , 0 \}$ In $J _ { 2 } =$ $\{ 0 , n - p , 0 \}$ . Define $R \overset { - } { = } P ^ { - 1 } H ( P ^ { * } ) ^ { - 1 }$ and rewrite Eq. (6) in the form

$$
J R + R J ^ { * } = W _ { 0 } ,
$$

where $W _ { 0 } = P ^ { - 1 } W ( P ^ { * } ) ^ { - 1 } > 0$ . The partitions of R and $W _ { 0 }$ corresponding to that of J in Eq. (8) give

$$
\begin{array}{c} \begin{array}{c} \begin{array} { r l } { \bigg [ ^ { J _ { 1 } } } & { 0 } \\ { 0 } & { J _ { 2 } \bigg ] \bigg [ ^ { R _ { 1 } } _ { R _ { 2 } } } \end{array} {} { \begin{array} { l l } { R _ { 2 } } \\ { R _ { 3 } ^ { * } } \end{array} } \bigg ] + \bigg [ ^ { R _ { 1 } } _ { R _ { 2 } }  \end{array} { \begin{array} { l l } { R _ { 2 } } \\ { R _ { 3 } } \end{array} } \bigg ] \bigg [ ^ { J _ { 1 } ^ { * } }  & { 0 } \\ { 0 } & { J _ { 2 } ^ { * } \bigg ] = \bigg [ ^ { W _ { 1 } } _ { W _ { 3 } } \bigg ] , } \end{array}
$$

and hence

$$
\begin{array} { r } { J _ { 1 } R _ { 1 } + R _ { 1 } J _ { 1 } ^ { * } = W _ { 1 } , J _ { 2 } R _ { 3 } + R _ { 3 } J _ { 2 } ^ { * } = W _ { 3 } , } \end{array}
$$

where $W _ { 1 } > 0 , W _ { 3 } > 0 .$ By Theorem 1 the matrices $R _ { 1 } \in \mathbb { C } ^ { p \times p }$ and $- R _ { 3 } \in$ $\mathbb { C } ^ { ( n - p ) \times ( n - p ) }$ are positive definite. It remains to show that, in this case,

$$
\ln H = \operatorname { I n } { \left[ \begin{array} { l l } { R _ { 1 } } & { R _ { 2 } } \\ { R _ { 2 } ^ { * } } & { R _ { 3 } } \end{array} \right] } = \{ p , n - p , 0 \} = \operatorname { I n } A .
$$

This follows from the easily verified congruence relation

$$
\begin{array} { r l } { Q ^ { * } R Q = \biggl [ { R _ { 1 } } & { { } \qquad 0 } \\ { 0 } & { { } - { R _ { 2 } ^ { * } { R _ { 1 } ^ { - 1 } { R _ { 2 } } } + { R _ { 3 } } } \biggr ] } \mathrm { , } } \end{array}\tag{9}
$$

where

$$
Q = { \binom { I } { 0 } } \left[ { \begin{array} { c } { - R _ { 1 } ^ { - 1 } R _ { 2 } } \\ { I } \end{array} } \right] .
$$

Conversely, suppose that $\delta ( A ) = 0 ;$ ,so that J has a Jordan form as described in Eq. (8). A Hermitian matrix H is to be constructed so that Eqs. (6) and (7) are valid. To this end, apply Theorem 1, which ensures the existence of negative definite matrices $H _ { 1 } \in \mathbb { C } ^ { p \times p } , H _ { 2 } \in \mathbb { C } ^ { ( n - p ) \times ( n - p ) }$ such that

$$
\begin{array} { r } { - J _ { 1 } H _ { 1 } - H _ { 1 } J _ { 1 } ^ { * } > 0 , } \\ { J _ { 2 } H _ { 2 } + H _ { 2 } J _ { 2 } ^ { * } > 0 . } \end{array}
$$

Now it is easily checked by use of Sylvester's law of inertia that the matrix

$$
H = P { \left[ \begin{array} { l l } { - H _ { 1 } } & { ~ 0 } \\ { ~ 0 } & { ~ H _ { 2 } } \end{array} \right] } P ^ { * }
$$

is Hermitian and satisfies condition (6). It remains to recall that $H _ { 1 } < O$ $H _ { 2 } < O$ , and hence

$$
\mathrm { I n } \ H = \mathrm { I n } ( - H _ { 1 } ) + \mathrm { I n } \ H _ { 2 } = \{ p , n - p , 0 \} = \mathrm { I n } \ A .
$$

In contrast to Theorem 2 the next results are concerned with the case when $A H + H A ^ { * } = W$ is merely a positive semi-definite matrix. First, let us agree to write In $A \leq$ In B for any two $n \times n$ matrices A and B such that

$$
\pi ( A ) \leq \pi ( B ) , \qquad \nu ( A ) \leq \nu ( B ) .
$$

Clearly, in this case $\delta ( A ) \geq \delta ( B )$

Proposition 1. Let $\ b { A } \in \mathbb { C } ^ { n \times n }$ and $\delta ( A ) = 0 .$ If H is Hermitian and

$$
A H + H A ^ { * } = W \geq 0 ,\tag{10}
$$

then In $H \leq I n \ A$

ProoF. By Theorem 2, there exists a Hermitian matrix $H _ { 0 }$ such that

$$
A H _ { 0 } + H _ { 0 } A ^ { * } > 0 \qquad \mathrm { a n d } \qquad \mathrm { I n } \ A = \mathrm { I n } \ H _ { 0 } .
$$

Putting $H _ { \varepsilon } = H + \varepsilon H _ { 0 }$ , we observe that

$$
A H _ { \varepsilon } + H _ { \varepsilon } A ^ { * } = \left( A H + H A ^ { * } \right) + \varepsilon ( A H _ { 0 } + H _ { 0 } A ^ { * } ) > 0 ,
$$

for all $\varepsilon > 0 .$ Thus, using Theorem 2 again, we find that for any $\varepsilon > 0 _ { \mathrm { { i } } }$

$$
\operatorname { I n } A = \operatorname { I n } H _ { \varepsilon } .\tag{11}
$$

In particular, the last equality implies $\delta ( A ) = \delta ( H _ { \varepsilon } ) = 0 ,$ and hence the matrices A and $H _ { \varepsilon }$ have no eigenvalues on the imaginary axis. In particular, they are nonsingular. The continuity of the (real) eigenvalues of $H _ { \varepsilon }$ as functions of ε (see Section 10.5) then implies that none of them can, in the limit, “jump" through the origin. Hence the only possibility is that, as $\varepsilon  0 ,$ one or more eigenvalues of $H _ { \varepsilon }$ become zero as $H _ { \varepsilon }$ approaches H. The result now follows from Eq. (11):

$$
\operatorname { I n } A = \operatorname { I n } H _ { \varepsilon } \geq \operatorname { I n } H . \quad \operatorname { I n }
$$

Note that if A is stable, then certainly $\delta ( A ) = 0$ and the proposition shows that H is semidefinite, a result that has already been seen in Exercise 12.3.1.

Proposition 2. If $A \in \mathbb { C } ^ { n \times 1 }$ then, for any nonsingular Hermitian matrix $H \in \mathbb { C } ^ { n \times n }$ such that Eq. (10) holds,

$$
\operatorname { I n } A \leq \operatorname { I n } H .\tag{12}
$$

PROOF. Denote $A _ { \varepsilon } = A + \varepsilon H ^ { - 1 }$ for ε real. Then the matrix

$$
A _ { \varepsilon } H + H A _ { \varepsilon } ^ { * } = ( A H + H A ^ { * } ) + 2 \varepsilon I
$$

is positive definite for each $\varepsilon > 0$ Hence Theorem 2 implies In $A _ { \varepsilon } = \ln H$ and, in particular, $\delta ( A _ { \varepsilon } ) = 0$ for all $\varepsilon > 0 .$ The continuity of the eigenvalues of $A _ { \varepsilon }$ as functions of ε now implies that the inertia of A can differ from that of $A _ { \varepsilon }$ only by the number of eigenvalues that become pure imaginary in the limit as $\varepsilon  0 .$ Thus,

$$
\ln H = \operatorname { I n } A _ { \varepsilon } \geq \operatorname { I n } A ,
$$

and the proposition is established.

Combining the results of Propositions 1 and 2, we obtain a generalization of Theorem 2 in which W is semi-definite.

Theorem 3 (D. Carlson and H. Schneider†). $I f A \in \mathbb { C } ^ { n \times n } , \delta ( A ) = 0$ and the Hermitian nonsingular matrix $H \in \mathbb { C } ^ { n \times n }$ satisfies the condition $A H + H A ^ { * }$ $= W \geq 0$ , then In $A = \operatorname { I n } H$

When A, H, and W are related as in Eq. (10), with $H = H ^ { * }$ and W positive semi-definite, the equality of In A and In H is achieved at the expense of the further hypotheses that $\delta ( A ) = 0$ and H is nonsingular. A useful sufficient condition for these latter hypotheses, and hence for equality of the inertias, involves the idea of controllability of a matrix pair (see Section 5.13). Recall that an $n \times n$ matrix A and an $n \times m$ matrix B together are controllable if and only if

$$
\operatorname { r a n k } [ B \quad A B \quad \cdots \quad A ^ { n - 1 } B ] = n .\tag{13}
$$

Theorem 4. If $A H + H A ^ { * } = W \geq B B ^ { * } ,$ where $H ^ { * } = H$ and $( A , B )$ is controllable, then $\delta ( A ) = \delta ( H ) = 0$ and In $A = \operatorname { I n } H$

ProoF. We shall show that the controllability of $( A , W )$ yields $\delta ( A ) = 0$ and det $H \neq 0 ,$ so that the required assertion follows from Theorem 3.

Suppose on the contrary that $\delta ( A ) \neq 0$ ; hence there is a nonzero vector $\pmb { x } \in \mathbb { C } ^ { n }$ such that $\mathbf { x } ^ { * } A = i \alpha \mathbf { x } ^ { * }$ and α is real. Then $A ^ { * } x = - i \alpha x \mathrm { a n d }$

$$
x ^ { * } W x = x ^ { * } ( A H + H A ^ { * } ) { \bf x } = ( - i \alpha + i \alpha ) x ^ { * } H { \bf x } = 0 .
$$

Since $W \geq B B ^ { * } \geq 0 .$ it follows that $0 = { { \bf { x } } ^ { * } } W { \bf { x } } \ge \| { \boldsymbol { B } } ^ { * } { \bf { x } } \| ^ { 2 }$ . that is, ${ \pmb x } ^ { * } { \pmb B } = { \pmb \theta } ^ { \dagger }$ . But then the controllability condition is violated, since

$$
\begin{array} { r } { { \boldsymbol { x } } ^ { * } [ B \quad { \boldsymbol { A } } { \boldsymbol { B } } \quad \cdots \quad { \boldsymbol { A } } ^ { n - 1 } { \boldsymbol { B } } ] = [ { \boldsymbol { x } } ^ { * } { \boldsymbol { B } } \quad i { \boldsymbol { \alpha } } { \boldsymbol { x } } ^ { * } { \boldsymbol { B } } \quad \cdots \quad ( i { \boldsymbol { \alpha } } ) ^ { n - 1 } { \boldsymbol { x } } ^ { * } { \boldsymbol { B } } ] = { \boldsymbol { \theta } } ^ { \mathrm { { T } } } , } \end{array}
$$

for $\mathbf { \nabla } \mathbf { \mathbf { x } } \neq \mathbf { \nabla } \theta _ { \mathrm { { \mathrm { ~ } } } }$ , and hence rank $\lbrack B \quad A B \quad \cdot \cdot \quad A ^ { n - 1 } B ] < n .$ So we must have $\delta ( A ) = 0 .$

Assume now that H is singular. Then there is a vector ${ \pmb x } \neq { \pmb \theta }$ such that $H \pmb { x } = \pmb { \theta }$ and

$$
x ^ { * } W x = x ^ { * } ( A H + H A ^ { * } ) x = 0 .
$$

It follows that ${ \pmb x } ^ { * } W = { \pmb \theta } ^ { \mathnormal { \mathsf { T } } }$ and, as noted before, this implies that ${ \pmb x } ^ { * } { \pmb B } = { \pmb \theta } ^ { \mathsf { T } }$ Hence

$$
\mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } } \mathbf { { } { } } \mathbf { { } } \mathbf { { } { } } \mathbf { { } } \mathbf { { } { } } \mathbf { { } { } } \mathbf { { } { } } \mathbf { { } { } } \mathbf { { } { } } \mathbf { { } { } } \mathbf { { } { } } \mathbf { { } { } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { { } } } \mathbf { { } { } } \mathbf { { } { } } \mathbf { { } } \mathbf { { { } } } \mathbf { { } } \mathbf { { } } \mathbf\tag{14}
$$

Now we have

$$
x ^ { * } A B B ^ { * } A ^ { * } x \leq x ^ { * } A W A ^ { * } x = x ^ { * } ( A ^ { 2 } H A ^ { * } + A H ( A ^ { * } ) ^ { 2 } ) x = 0 ,
$$

using Eq. (14) twice. Thus, ${ \pmb x } ^ { * } A { \pmb B } = { \pmb \theta } ^ { \dagger }$ . Repeating this procedure, it is found that $\pmb { x } ^ { * } A ^ { k } B = \pmb { \theta } ^ { \mathnormal { \mathsf { T } } }$ for $k = 0 , 1 , \ldots , n - 1$ . Therefore we have found an $\boldsymbol { x } \neq \boldsymbol { \theta }$ such that

$$
x ^ { * } [ B \quad A B \quad \cdot \cdot \quad A ^ { n - 1 } B ] = \theta ^ { \mathrm { T } } ,
$$

and the pair (A, B) fails to be controllable. This shows that, actually, det $H \neq 0$ and hence the requirements of Theorem 3 are fulfilled.

It is clear that if (A, W) is controllable, then we may take $B = W ^ { 1 / 2 }$ (the unique positive semi-definite square root of W) and obtain the next conclusion.

Corollary 1 (C. T. Chen†; H. K. Wimmer) $I f \ A H + H A ^ { * } = W ,$ $H = H ^ { * } , ~ W \geq 0$ and $( A , W )$ is controllable, then $\delta ( A ) = \delta ( H ) = 0$ and In A = In H.

Now a useful generalization of the classical stability theorem is readily proved.

Theorem 5. Let $A \in \mathbb { C } ^ { m \times n }$ with (A, B) controllable, and let W be positive semi-definite, with

$$
W \geq B B ^ { * } \geq 0 .
$$

Then the conclusions (a) and (b) of Theorem 1 hold

ProoF. For conclusion (a) follow the proof of Theorem 1 and use Lemma 9.11.2 together with the controllability of (A, B) to establish the definite property of H.

Conclusion (b) is a special case of Theorem 4.

We conclude by noting that the inertia we have been using is often referred to as the inertia of a matrix with respect to the imaginary axis. In contrast, the triple $\{ \pi ^ { \prime } ( A ) , \nu ^ { \prime } ( A ) , \delta ^ { \prime } ( A ) \}$ , where $\pi ^ { \prime } ( A )$ (respectively, $\nu ^ { \prime } ( A )$ and $\delta ^ { \prime } ( A ) )$

denotes the number of eigenvalues (counted with their multiplicities) with positive (respectively, negative and zero) imaginary parts, is said to be the inertia of A with respect to the real axis. Note that obviously

$$
\{ \pi ( i A ) , \nu ( i A ) , \delta ( i A ) \} = \{ \nu ^ { \prime } ( A ) , \pi ^ { \prime } ( A ) , \delta ^ { \prime } ( A ) \} .
$$

Exercise 4. Check that the $n \times n$ Schwarz matrix

$$
S = { \left[ \begin{array} { l l l l l } { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { - c _ { n } } & { 0 } & { 1 } & { \ddots } & { \vdots } \\ { 0 } & { - c _ { n - 1 } } & { \ddots } & { 0 } \\ { \vdots } & { \ddots } & { \ddots } & { 0 } & { 1 } \\ { 0 } & { \cdots } & { 0 } & { - c _ { 2 } } & { - c _ { 1 } } \end{array} \right] }\tag{15}
$$

satisfies the Lyapunov equation

$$
\begin{array} { r } { S ^ { \mathrm { T } } H + H S = W , } \end{array}
$$

where $H = \mathrm { d i a g } [ c _ { 1 } c _ { 2 } \cdot \cdot \cdot c _ { n } , c _ { 2 } c _ { 3 } \cdot \cdot \cdot c _ { n } , . . . , c _ { n - 1 } c _ { n } , c _ { n } ]$ and

$$
W = \mathrm { d i a g } [ 0 , \dots 0 , - 2 c _ { n } ^ { 2 } ] .
$$

Exercise 5. If $c _ { 1 } , c _ { 2 } , \ldots , c _ { n }$ in (15) are nonzero real numbers, show that the pair of matrices $( W , S ^ { \mathrm { T } } )$ is controllable and hence

$$
\pi ( S ) = n - k , \qquad \nu ( S ) = k , \qquad \delta ( S ) = 0 ,
$$

where k is the number of positive terms in the sequence

$$
c _ { 1 } , \quad c _ { 1 } c _ { 2 } , \quad c _ { 1 } c _ { 2 } c _ { 3 } , \ldots , \quad c _ { 1 } c _ { 2 } \cdots c _ { n } .
$$

Exercise 6. (Sylvester). If A is an $n \times n$ positive definite matrix and $H \in \mathbb { C } ^ { n \times n }$ is Hermitian, show that In $A H = \operatorname { I n } H$

Exercise 7. (A generalization of Exercise 6 by H. Wielandt). If $\ b { A } \in \mathbb { C } ^ { n \times n }$ $\mathcal { R } _ { \mathcal { L } } \mathbf { \Psi } \mathcal { A }$ is positive definite, and $H \in \mathbb { C } ^ { n \times n }$ is Hermitian, show that In $A H =$ In H.

Exercise 8. (W. Hahn†). Show that if $\mathcal { R } \mathscr { A } \leq 0$ and $( A , { \mathcal { R } } _ { \epsilon } \ A )$ is a controllable pair, then A is stable (see Exercise 3).

Exercise 9. Show that if $W _ { \mathrm { 1 } } \geq W _ { \mathrm { 2 } } \geq 0 .$ , then Ker $W _ { 1 } \subset \mathsf { K e r } \ W _ { 2 }$ . □

## 13.2 Stability with Respect to the Unit Circle

We have seen that the stability problem for a linear differential equation with constant coefficients is closely related to the location of the eigenvalues of a matrix with respect to the imaginary axis. An analogous role for linear difference equations is played by the location of eigenvalues relative to the unit circle.

To illustrate these ideas, let $A \in \mathbb { C } ^ { n \times n }$ and a nonzero $\pmb { x _ { 0 } } \in \mathbb { C } ^ { n }$ be given, and consider the simplest difference equation:

$$
\pmb { x } _ { j } = A \pmb { x } _ { j - 1 } , \qquad \pmb { x } _ { j } \in \mathbb { C } ^ { n } , \qquad j = 1 , 2 , \ldots .\tag{1}
$$

This equation is a difference analogue of the differential equation (13.1.1), but its solution is much more simple: $\pmb { x } _ { j } = A ^ { j } \pmb { x } _ { 0 }$ for $j = 0 , 1 , \ldots$ We say that the matrix A in Eq. (1) is stable (with respect to the unit circle) if the solution sequence $\pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \ldots , \pmb { x } _ { j } , \ldots$ . of (1) converges to zero for any choice of the initial vector $\pmb { x _ { 0 } }$ . It is easily seen that this occurs if and only if $A ^ { j }  0$ as $j \to \infty$ , and this occurs (see Exercise 11.1.8) if and only if the spectral radius of A is less than 1. Thus, a matrix A is stable (with respect to the unit circle) if and only if all its eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ lie inside the unit circle, that $i s , | \lambda _ { i } | < 1$ for $i = 1 , 2 , \ldots , n .$

In this section we develop a method analogous to that of Lyapunov for determining the number of eigenvalues of a matrix (counted with their multiplicities) lying inside and outside the unit circle and on its circumference. It turns out that this problem is closely related to the existence of positive definite solutions H of a Stein equation $H - A ^ { * } H A = V$ for some positive definite V.

Theorem 1. Let A, $V \in \mathbb { C } ^ { n \times n }$ and let V be positive definite.

(a) If A is stable with respect to the unit circle, then the equation

$$
H - A ^ { * } H A = V\tag{2}
$$

has a unique solution H, and H is positive definite.

(b) If there is a positive definite matrix H satisfying Eq. (2), then A is stable with respect to the unit circle.

ProOF. First suppose that A is stable and let $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ denote the eigenvalues of A, so that $| \lambda _ { i } | < 1$ for $i = 1 , 2 , \ldots , n .$ Then (see Exercise 9.4.3) $A ^ { * } + I$ is nonsingular and therefore we may define the matrix

$$
C = ( A ^ { * } + I ) ^ { - 1 } ( A ^ { * } - I ) .\tag{3}
$$

Observe that, by Exercise 9.4.4, the matrix C is stable (with respect to the imaginary axis). A little calculation shows that for any $H \in \mathbb { C } ^ { n \times n }$

$$
\begin{array} { r c l } { { } } & { { } } & { { C H + H C ^ { * } = ( A ^ { * } + I ) ^ { - 1 } [ ( A ^ { * } - I ) H ( A + I ) + ( A ^ { * } + I ) H ( A - I ) ] } } \\ { { } } & { { } } & { { \times ~ ( A + I ) ^ { - 1 } } } \\ { { } } & { { } } & { { = 2 ( A ^ { * } + I ) ^ { - 1 } [ A ^ { * } H A - H ] ( A + I ) ^ { - 1 } . } } \end{array}
$$

and hence

$$
C ( - H ) + ( - H ) C ^ { * } = 2 ( A ^ { * } + I ) ^ { - 1 } [ H - A ^ { * } H A ] ( A + I ) ^ { - 1 } .\tag{4}
$$

Now apply Theorem 13.1.1(a) to Eq. (4) to see that, if $H - A ^ { * } H A$ is positive definite, so that the matrix on the right of Eq. 4 is positive definite, then H is unique and is positive definite.

The converse is proved with the line of argument used in proving Theorem 13.1.1(b). Suppose that Eq. (2) holds with $H > O$ . If λ is an eigenvalue of A corresponding to the eigenvector x, then $A { \boldsymbol { \mathbf { x } } } = \lambda { \boldsymbol { \mathbf { x } } }$ and ${ \pmb x } ^ { * } { \pmb A } ^ { * } = \bar { \lambda } { \pmb x } ^ { * } ,$ so that Eq. (2) implies

$$
x ^ { * } V x = ( 1 - | \lambda | ^ { 2 } ) x ^ { * } H x .\tag{5}
$$

The positive definiteness of the matrices V and H now clearly implies $| \lambda | < 1$ for each eigenvalue λ of A.

Following the lead set in the previous section, we now seek a generalization of Theorem 1 of the following kind: retain the hypotheses $V > o$ and $H ^ { * } = H$ , det $H \neq 0 ;$ for matrices of Eq. (2) and look for a connection between the inertia of H (relative to the imaginary axis) and that of A (relative to the unit circle). Theorem 2 provides such a generalization and is due to Taussky, Hill, and Wimmer.†

Theorem 2. Let $\ b { A } \in \mathbb { C } ^ { n \times n }$ . If H is a Hermitian matrix satisfying the Stein equation (2) with $V > 0 ,$ then H is nonsingular and the matrix A has π(H) (respectively, v(H)) eigenvalues lying inside (respectively, outside) the (open) unit circle and no eigenvalues of modulus 1.

Conversely, if A has no eigenvalues of modulus 1, then there exists a Hermitian matrix H such that Eq. (2) holds and its inertia gives the distribution of eigenvalues of A with respect to the unit circle, as described above.

ProoF. If Eq. (2) is valid, then the relation (5) shows that A has no eigenvalues of modulus 1. Proceeding as in the proof of Theorem 13.1.2, let the Jordan form of A be

$$
\begin{array} { r } { J = \left[ \begin{array} { c c } { J _ { 1 } } & { 0 } \\ { 0 } & { J _ { 2 } } \end{array} \right] = \mathbb { S } ^ { - 1 } A S , } \end{array}\tag{6}
$$

where $\begin{array} { r } { J _ { 1 } \in \mathbb { C } ^ { p \times p } , \ J _ { 2 } \in \mathbb { C } ^ { ( n - p ) \times ( n - p ) } , } \end{array}$ and the eigenvalues of $J _ { 1 }$ and $J _ { 2 }$ lie inside and outside the unit circle, respectively. Preserving the notation of the proof of Theorem 13.1.2, Eq. (2) yields the equation

$$
R - J ^ { \ast } R J = V _ { 0 } , \qquad V _ { 0 } > 0 ,
$$

and, partitioning R and $V _ { 0 }$ compatibly with $J ,$ we obtain

$$
R _ { 1 } - J _ { 1 } ^ { * } R _ { 1 } J _ { 1 } = V _ { 1 } , \qquad R _ { 3 } - J _ { 2 } ^ { * } R _ { 3 } J _ { 2 } = V _ { 3 } ,
$$

where $V _ { 1 } > 0 , ~ V _ { 3 } > 0 .$ Now Theorem 1 yields $R _ { 1 } > 0$ and $R _ { 3 } < 0$ and therefore, using Eq. (13.1.9), it is found that

$$
\operatorname { I n } H = \operatorname { I n } R = ( p , n - p , 0 ) ,
$$

as required.

Conversely, suppose that $| \lambda | \neq 1$ for any eigenvalue λ of A. Then A can be transformed to the Jordan form (6). By Theorem 1 there are positive definite matrices $H _ { 1 } \in \mathbb { C } ^ { p \times p } , H _ { 2 } \in \mathbb { C } ^ { ( n - p ) \times ( n - p ) }$ such that

$$
\begin{array} { r l r } { H _ { 1 } - J _ { 1 } ^ { * } H _ { 1 } J _ { 1 } = V _ { 1 } , } & { { } } & { V _ { 1 } > 0 , } \\ { \qquad } & { { } } & { H _ { 2 } - ( J _ { 2 } ^ { * } ) ^ { - 1 } H _ { 2 } J _ { 2 } ^ { - 1 } = V _ { 2 } , \qquad V _ { 2 } > 0 . } \end{array}
$$

Hence the positive definite matrix

$$
\begin{array} { r l r } { H = ( S ^ { * } ) ^ { - 1 } \Bigg [ \frac { H _ { 1 } } { \ d _ { 1 } } } & { { } } & { 0 \Bigg ] _ { \cfrac { 1 } { 2 } } } \\ { 0 } & { { } } & { - ( J _ { 2 } ^ { * } ) ^ { - 1 } H _ { 2 } J _ { 2 } ^ { - 1 } \Bigg ] ^ { \zeta ^ { - 1 } } } \end{array}
$$

satisfies the condition $H - A ^ { * } H A > 0$ Obviously, the number of eigenvalues of A lying inside (respectively, outside) the unit circle is equal to $p = \pi ( H )$ (respectively, $n - p = \nu ( H ) )$ , as required.■

The following results are analogues of Theorems 13.1.3 and 13.1.4 and can be established in the same fashion. They are stated here without proof.

Theorem 3. Let $\ b { A } \in \mathbb { C } ^ { n \times n }$ and let A have no eigenvalues of modulus 1. If there exists an $n \times n$ nonsingular Hermitian matrix H such that

$$
H - A ^ { * } H A = V , \quad \quad V \geq 0 ,\tag{7}
$$

then A has $\pi ( H )$ and v(H) eigenvalues of modulus less than 1 and greater than 1, respectively.

Theorem 4. If $E q . ( 7 )$ holds and the pair $( A ^ { * } , V )$ is controllable, then A has no eigenvalues of modulus 1, det $H \neq 0 ,$ and the assertion of Theorem 3 is valid.

## 13.3 The Bezoutian and the Resultant

The proofs of the stability results given in the following sections depend on two broad areas of development. The first is the development of inertia theory for matrices, which we have already presented, and the second is a more recent development of properties of Bezout matrices for a pair of scalar polynomials, which will now be discussed.

Let $\begin{array} { r } { a ( \lambda ) = \sum _ { j = 0 } ^ { l } a _ { j } \lambda ^ { j } } \end{array}$ and $\begin{array} { r } { b ( \lambda ) = \sum _ { i = 0 } ^ { m } b _ { i } \lambda ^ { j } ( a _ { i } \neq 0 , b _ { m } \neq 0 , l \ge m ) } \end{array}$ be arbitrary complex polynomials. Since $b ( \lambda )$ can be viewed as $\sum _ { j = 0 } ^ { l } b _ { j } \lambda ^ { j }$ , where $b _ { m + 1 } = \cdots = b _ { l } = 0 _ { ! }$ , we may assume without loss of generality that the polynomials are of the form $\dot { \sum _ { j = 0 } ^ { l } } a _ { j } \lambda ^ { j } , a _ { l } \neq 0 .$ and $\sum _ { j = 0 } ^ { l } b _ { j } \lambda ^ { j } .$ The expression

$$
\frac { a ( \lambda ) b ( \mu ) - b ( \lambda ) a ( \mu ) } { \lambda - \mu }
$$

is easily verified to be a polynomial in the two variables λ and $\mu { : }$

$$
\frac { a ( \lambda ) b ( \mu ) - b ( \lambda ) a ( \mu ) } { \lambda - \mu } = \sum _ { i , j = 0 } ^ { l - 1 } \gamma _ { i j } \lambda ^ { i } \mu ^ { j } .\tag{1}
$$

Then the matrix $B = [ \gamma _ { i j } ] _ { i , j = 0 } ^ { l - 1 }$ is called the Bezout matrix (or Bezoutian) associated with the polynomials $a ( \lambda )$ and $b ( \lambda )$ . To emphasize this, we also write $B = \operatorname { \mathbf { B e z } } ( a , b )$

The main objectives of this section are to obtain formulae expressing $\mathtt { B e z } ( a , b )$ in terms of the coefficients of a and b (Eqs. (7), (17), and (20), in particular), to make the connection with the resultant of $a ( \lambda )$ and $b ( \lambda )$ (Eq. (24)), and to make the first deductions from these concerning the greatest common divisor of $a ( \lambda )$ and $b ( \lambda )$ in the form of Theorems 1 and 2.

Exercise 1. Check that

$$
\operatorname { B e z } ( a , b ) = - \operatorname { B e z } ( b , a ) ,
$$

for any two polynomials $a ( \lambda )$ and $b ( \lambda )$ and that $\mathtt { B e z } ( a , b )$ is symmetric.

Exercise 2. Show that the matrix

$$
B = \left[ { \begin{array} { r r r } { 0 } & { - 1 } & { 4 } \\ { - 1 } & { 4 } & { 0 } \\ { 4 } & { 0 } & { - 2 } \end{array} } \right]
$$

is the Bezout matrix associated with the polynomials $a ( \lambda ) = 1 - \lambda ^ { 2 } + 2 \lambda ^ { 3 }$ and $b ( \lambda ) = 2 - \lambda ^ { 2 } = 2 - \lambda ^ { 2 } + 0 \lambda ^ { 3 }$ □

If $a ( \lambda ) = a _ { 0 } + a _ { 1 } \lambda + \cdots + a _ { l } \lambda _ { \mathrm { ~ } } ^ { l }$ , the triangular Hankel matrix of coefficients,

$$
S ( a ) = { \left[ \begin{array} { l l l l } { a _ { 1 } } & { a _ { 2 } } & { \cdots } & { a _ { l } } \\ { a _ { 2 } } & { \cdots } & { a _ { l } } & { 0 } \\ { \vdots } & { \ldots } & { \ldots } & { \vdots } \\ { a _ { l } } & { 0 } & { \cdots } & { 0 } \end{array} \right] } ,\tag{2}
$$

arises very frequently. For a reason that will be clear in a moment (see Exercises 3 and 4), we call $S ( a )$ the symmetrizer of $a ( \lambda )$ . Note that $S ( a )$ does not depend on $a _ { 0 }$

Exercise 3. If $C _ { a }$ denotes the companion matrix of $a ( \lambda )$

$$
\boldsymbol C _ { a } = \left[ \begin{array} { l l l l l } { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 1 } & { \ddots } & { \vdots } \\ { \vdots } & { } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \cdots } & { } & { 0 } & { 1 } \\ { - \tilde { a } _ { 0 } } & { - \tilde { a } _ { 1 } } & { \cdots } & { - \tilde { a } _ { l - 1 } } \end{array} \right] , \qquad \boldsymbol C _ { a } \in \mathbb { C } ^ { l \times l } ,
$$

where $\tilde { a } _ { j } = a _ { l } ^ { - 1 } a _ { j } , j = 0 , 1 , \ldots , l - 1$ , check that

$$
S ( { a } ) C _ { a } = \left[ \begin{array} { c c c c } { { - a _ { 0 } } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { 0 } } & { { a _ { 2 } } } & { { \cdots } } & { { a _ { l } } } \\ { { } } & { { } } & { { } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { \cdots } } & { { \vdots } } \\ { { } } & { { } } & { { } } & { { } } \\ { { 0 } } & { { a _ { l } } } & { { 0 } } & { { \cdots } } & { { 0 } } \end{array} \right] .
$$

and note that this matrix is symmetric. □

Define the polynomial $\hat { a } ( \lambda ) = \lambda ^ { l } a ( \lambda ^ { - 1 } ) = a _ { 0 } \lambda ^ { l } + \dots + a _ { l - 1 } \lambda + a _ { l } ;$ its symmetrizer is

$$
S ( \hat { a } ) = \left[ { \begin{array} { c c c c } { a _ { l - 1 } } & { a _ { l - 2 } } & { \cdot \cdot \cdot } & { a _ { 0 } } \\ { a _ { l - 2 } } & { \cdot \cdot \cdot } & { a _ { 0 } } & { 0 } \\ { \vdots } & { \cdot \cdot } & { \cdot \cdot } & { \vdots } \\ { a _ { 0 } } & { 0 } & { \cdot \cdot \cdot } & { 0 } \end{array} } \right] .\tag{3}
$$

Another device will also be useful. Define the permutation matrix P (the rotation matrix) by

$$
P = { \left[ \begin{array} { l l l l l } { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \\ { 0 } & { \cdots } & { 0 } & { 1 } & { 0 } \\ { \vdots } & { \cdots } & { \cdots } & { \cdots } & { \vdots } \\ { 0 } & { 1 } & { } & { } & { } \\ { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \end{array} \right] } ,\tag{4}
$$

and observe that $P ^ { 2 } = I$ and that ${ \pmb S } ( a ) P$ and $P S ( a )$ are Toeplitz matrices:

$$
S ( a ) P = \left[ \begin{array} { c c c c } { { a _ { \imath } } } & { { \cdots } } & { { a _ { 2 } } } & { { a _ { 1 } } } \\ { { 0 } } & { { } } & { { a _ { 2 } } } \\ { { \vdots } } & { { \ddots } } & { { \ddots } } & { { \vdots } } \\ { { 0 } } & { { \cdots } } & { { 0 } } & { { a _ { l } } } \end{array} \right] , \qquad P S ( a ) = \left[ \begin{array} { c c c c } { { a _ { \imath } } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { } } & { { \ddots } } & { { \vdots } } \\ { { a _ { 2 } } } & { { } } & { { } } & { { 0 } } \\ { { a _ { 1 } } } & { { a _ { 2 } } } & { { \cdots } } & { { a _ { l } } } \end{array} \right] .
$$

Exercise 4. Generalize the result of Exercise 3. Namely, show that, for any $1 \leq k \leq l - 1$

$$
\begin{array} { r l r l } & { S ( \boldsymbol { a } ) C _ { \boldsymbol { a } } ^ { k } = \mathrm { d i a g } [ - P S _ { 1 } P , S _ { 2 } ] , } & & { P , S _ { 1 } \in { \mathbb C } ^ { k \times k } , \quad S _ { 2 } \in { \mathbb C } ^ { ( l - k ) \times ( l - k ) } , } \end{array}\tag{5}
$$

where $S _ { 1 }$ and $s _ { z }$ stand for the symmetrizers of the polynomials $a _ { 1 } ( \lambda ) =$ $a _ { \scriptscriptstyle \ k } + a _ { \scriptscriptstyle \ k - 1 } \lambda + \cdot \cdot \cdot + a _ { 0 } \lambda ^ { k }$ and $a _ { 2 } ( \lambda ) = a _ { k } + a _ { k + 1 } \lambda + \cdots + a _ { l } \lambda ^ { l - k } ;$ respectively.

Also, show that

$$
\begin{array} { r } { S ( a ) C _ { a } ^ { l } = - P S ( \hat { a } ) P . \quad \varTheta } \end{array}\tag{6}
$$

The formula derived in the following proposition will be useful in the sequel.

Proposition 1. With the previous notation, the Bezoutian B of scalar polynomials $a ( \lambda )$ and $b ( \lambda )$ is given by

$$
B = S ( a ) S ( \hat { b } ) P - S ( b ) S ( \hat { a } ) P .\tag{7}
$$

PROOF. Rewrite Eq. (1) in the form

$$
( \lambda - \mu ) \sum _ { i = 0 } ^ { l - 1 } \gamma _ { i } ( \mu ) \lambda ^ { i } = a ( \lambda ) b ( \mu ) - b ( \lambda ) a ( \mu ) ,
$$

where $\begin{array} { r } { \gamma _ { i } ( \mu ) = \sum _ { j = 0 } ^ { l - 1 } \gamma _ { i j } \mu ^ { j } \mathrm { f o r } i = 0 , 1 , . . . , l - 1 } \end{array}$ . Comparing the coefficients of $\lambda ^ { i }$ on both sides of the equation we obtain

$$
\begin{array} { c } { { \gamma _ { 0 } ( \mu ) - \mu \gamma _ { 1 } ( \mu ) = a _ { 1 } b ( \mu ) - b _ { 1 } a ( \mu ) , } } \\ { { \gamma _ { 1 } ( \mu ) - \mu \gamma _ { 2 } ( \mu ) = a _ { 2 } b ( \mu ) - b _ { 2 } a ( \mu ) , } } \\ { { \vdots } } \\ { { \gamma _ { l - 2 } ( \mu ) - \mu \gamma _ { l - 1 } ( \mu ) = a _ { l - 1 } b ( \mu ) - b _ { l - 1 } a ( \mu ) , } } \\ { { \gamma _ { l - 1 } ( \mu ) = a _ { l } b ( \mu ) - b _ { l } a ( \mu ) . } } \end{array}
$$

From these equations it is easily deduced that for $i = 0 , 1 , \ldots , l - 1$

$$
\begin{array} { c } { { \gamma _ { i } ( \mu ) = ( \mu ^ { l - i - 1 } a _ { l } + \mu ^ { l - i - 2 } a _ { 1 - 1 } + \cdots + \mu a _ { i + 2 } + a _ { i + 1 } ) b ( \mu ) } } \\ { { - ( \mu ^ { l - i - 1 } b _ { l } + \mu ^ { l - i - 2 } b _ { l - 1 } + \cdots + \mu b _ { i + 2 } + b _ { i + 1 } ) a ( \mu ) . } } \end{array}
$$

Note that $\deg ( \gamma _ { i } ( \mu ) ) \leq l - 1 { \mathrm { ~ f o r ~ } } 0 \leq i \leq l - 1$ . Defining

$$
\gamma _ { i } ^ { \mathrm { { T } } } = \left[ { { \gamma _ { i } } _ { 0 } } \quad { { \gamma _ { i 1 } } } \quad { { \cdot \cdot } } \quad { { \gamma _ { i , l - 1 } } } \right]
$$

for $i = 0 , 1 , \ldots , l - 1$ we see that $\gamma _ { i } ^ { \mathrm { T } }$ forms row $( i + 1 )$ in the Bezout matrix B and that the last equation implies

$$
\begin{array} { r } { \gamma _ { i } ^ { \operatorname { r } } \left[ \begin{array} { c } { 1 } \\ { \mu } \\ { \vdots } \\ { \mu ^ { l - 1 } } \end{array} \right] = \left[ a _ { i + 1 } \quad a _ { i + 2 } \quad \cdots \quad a _ { l } \quad 0 \quad \cdots \quad 0 \right] \left[ \begin{array} { c } { b ( \mu ) } \\ { b ( \mu ) \mu } \\ { \vdots } \\ { b ( \mu ) \mu ^ { l - 1 } } \end{array} \right] } \end{array}
$$

$$
- \left[ b _ { i + 1 } \quad b _ { i + 2 } \quad \cdots \quad b _ { l } \quad 0 \quad \cdots \quad 0 \right] \left[ { \begin{array} { c } { a ( \mu ) } \\ { a ( \mu ) \mu } \\ { \vdots } \\ { a ( \mu ) \mu ^ { l - 1 } } \end{array} } \right] .\tag{8}
$$

Now a little calculation will verify that for any polynomial $c ( \mu )$ with degree at most l,

$$
\mathrm { c o l } ( c ( \mu ) \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } = S ( \hat { c } ) P \mathrm { c o l } ( \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } + P S ( c ) \mathrm { c o l } ( \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } \mu ^ { l } ,\tag{9}
$$

where by definition

$$
\begin{array} { r } { \mathrm { c o l } ( R _ { i } ) _ { i = 0 } ^ { l - 1 } \underline { { \boldsymbol { \ b \mathrm { a } } } } \left[ \begin{array} { c } { { \bf R } _ { 0 } } \\ { R _ { 1 } } \\ { \vdots } \\ { R _ { l - 1 } } \end{array} \right] , } \end{array}\tag{10}
$$

and, in general, $R _ { 0 } , R _ { 1 } , \ldots , R _ { l - 1 }$ may be scalars or matrices of the same size.

Using Eq. (9) for $a ( \lambda )$ and $b ( \lambda )$ , we find from Eq. (8) that

$$
\begin{array} { r l } & { B \operatorname { c o l } ( \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } = S ( \mathfrak { a } ) ( S ( \widehat { b } ) P \operatorname { c o l } ( \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } + P S ( \mathfrak { b } ) \operatorname { c o l } ( \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } \mu ^ { l } ) } \\ & { \qquad - S ( \mathfrak { b } ) ( S ( \widehat { \mathfrak { a } } ) P \operatorname { c o l } ( \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } + P S ( \mathfrak { a } ) \operatorname { c o l } ( \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } \mu ^ { l } ) . } \end{array}
$$

Note that for any $a ( \lambda )$ and $b ( \lambda )$

$$
S ( a ) P S ( b ) = S ( b ) P S ( a ) , \qquad S ( \hat { a } ) P S ( \hat { b } ) = S ( \hat { b } ) P S ( \hat { a } ) .\tag{12}
$$

Thus, using the first equality in (12), we obtain

$$
B \operatorname { c o l } ( \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } = S ( a ) S ( \hat { b } ) P \operatorname { c o l } ( \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } \cdot - S ( b ) S ( \hat { a } ) P \operatorname { c o l } ( \mu ^ { i - 1 } ) _ { i = 1 } ^ { l } .
$$

Since the last relation holds for any $\mu \in \mathbb { C } ,$ and the Vandermonde matrix for distinct $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { l }$ is nonsingular (see Exercise 2.3.6), the required formula (7) is established.■

A dual expression for the Bezoutian $B = \mathop { \bf B e z } ( a , b )$ is presented next.

Exercise 5. Check that

$$
- B = P S ( \hat { a } ) S ( b ) - P S ( \hat { b } ) S ( a ) .\tag{13}
$$

Hint. Rewrite Eq. (9) in terms of rows. □

It is easily seen that, if the polynomial a is fixed then the matrix $\mathtt { B e z } ( a , b )$ is a linear function of the polynomial b. Indeed, if $b ( \lambda )$ and $c ( \lambda )$ are polynomials with degree not exceeding l and $\beta , \gamma \in \mathbb { C }$ , we see that in the definition of Eq. (1),

$$
\begin{array} { r l } { { } } & { { a ( \lambda ) \{ \beta b ( \mu ) + \gamma c ( \mu ) \} - \{ \beta b ( \lambda ) + \gamma c ( \lambda ) \} a ( \mu ) } } \\ { { } } & { { = \beta \{ a ( \lambda ) b ( \mu ) - b ( \lambda ) a ( \mu ) \} + \gamma \{ a ( \lambda ) c ( \mu ) - c ( \lambda ) a ( \mu ) \} . } } \end{array}
$$

This immediately implies that

$$
\displaystyle \mathtt { B e z } ( a , \beta b + \gamma c ) = \beta \mathtt { B e z } ( a , b ) + \gamma \mathtt { B e z } ( a , c ) .\tag{14}
$$

In particular, writing $\begin{array} { r } { b ( \lambda ) = \sum _ { j = 0 } ^ { m } b _ { j } \lambda ^ { j } } \end{array}$ we have

$$
\operatorname { B e z } ( a , b ) = \sum _ { j = 0 } ^ { m } b _ { j } \operatorname { B e z } ( a , \lambda ^ { j } ) .\tag{15}
$$

Now examine the “primitive"Bezout matrices $\mathrm { B e z } ( a , \lambda ^ { j } )$ for $j = 0 , 1 , 2 ,$ $\cdots , m .$ Calculating directly with the definition of Eq. (1) we find first of all that Be $z ( a , 1 ) = S ( a )$ . More generally, to study $\mathtt { B e z } ( a , \lambda ^ { k } )$ we note that

$$
\begin{array} { l } { \displaystyle \frac { a ( \lambda ) \mu ^ { k } - \lambda ^ { k } a ( \mu ) } { \lambda - \mu } = \displaystyle \sum _ { j = 0 } ^ { l } a _ { j } \frac { \lambda ^ { j } \mu ^ { k } - \lambda ^ { k } \mu ^ { i } } { \lambda - \mu } } \\ { = - \displaystyle \sum _ { j = 0 } ^ { k - 1 } a _ { j } ( \lambda ^ { k } \mu ^ { j } + \dots + \lambda ^ { j } \mu ^ { k - 1 } ) } \\ { + \displaystyle \sum _ { j = k + 1 } ^ { l } a _ { j } ( \lambda ^ { j - 1 } \mu ^ { k } + \dots + \lambda ^ { k } \mu ^ { j - 1 } ) . } \end{array}
$$

Checking the form of the matrices in Eq. (5) we find that

$$
\mathtt { B e z } ( a , \lambda ^ { k } ) = \mathrm { d i a g } [ - P S _ { 1 } P , S _ { 2 } ] = S ( a ) C _ { a } ^ { k } .\tag{16}
$$

Combining this with Eq. (15) we get the first part of the following proposition, known as the Barnett factorization of $\mathtt { B e z } ( a , b )$

Proposition 2.

$$
\mathrm { B e z } ( a , b ) =  { \boldsymbol { S } } ( a ) b (  { \boldsymbol { C } } _ { a } ) = -  { \boldsymbol { S } } ( b ) a (  { \boldsymbol { C } } _ { b } ) .\tag{17}
$$

ProoF. For the second statement, we first use Exercise 1 and then apply the first statement. Thus,

$$
\mathtt { B e z } ( a , b ) = - \mathtt { B e z } ( b , a ) = - S ( b ) a ( C _ { b } ) ,
$$

as required.

It will be useful to have at hand another representation for the Barnett factorization. Observe first that by the Cayley-Hamilton theorem, $a ( C _ { a } ) = 0 ,$ and therefore

$$
b ( C _ { a } ) = b ( C _ { a } ) - a _ { l } ^ { - 1 } b _ { l } a ( C _ { a } ) = \sum _ { j = 0 } ^ { l } \tilde { b } _ { j } C _ { a } ^ { j } ,
$$

where $\tilde { b } _ { j } = b _ { j } - a _ { l } ^ { - 1 } b _ { l } a _ { j } , \mathrm { f o r } j = 0 , 1 , \ldots , l - 1$ . Define

$$
\mathfrak { f } ^ { T } = [ \hat { b } _ { 0 } \quad \tilde { b } _ { 1 } \quad \cdot \cdot \cdot \quad \tilde { b } _ { l - 1 } ]\tag{18}
$$

and denote the ith row of $b ( C _ { a } )$ by $\pmb { d } _ { i } ^ { T }$ for $i = 1 , 2 , \dots , l .$ Since

$$
e _ { 1 } ^ { T } C _ { a } ^ { j } = [ \underbrace { 0 \quad \cdots \quad 0 } _ { j } \quad 1 \quad 0 \quad \cdots \quad 0 ]
$$

we obtain

$$
\pmb { d } _ { 1 } ^ { T } = e _ { 1 } ^ { T } b ( C _ { a } ) = [ \tilde { b } _ { 0 } \quad \tilde { b } _ { 1 } \quad \cdots \quad \tilde { b } _ { l - 1 } ] = \pmb { \mathbb { \{ \beta } }  ^ { T } .\tag{19}
$$

Furthermore, for $j = 2 , 3 , \dots , l ,$

$$
d _ { j } ^ { T } = e _ { j } ^ { T } b ( C _ { a } ) = e _ { j - 1 } ^ { T } C _ { a } b ( C _ { a } ) = e _ { j - 1 } ^ { T } b ( C _ { a } ) C _ { a } = d _ { j - 1 } ^ { T } C _ { a } = d _ { 1 } ^ { T } C _ { a } ^ { j - 1 } = \ S ^ { T } C _ { a } ^ { j - 1 } .
$$

Thus,

$$
b ( \boldsymbol { C _ { a } } ) = \left[ \begin{array} { c } { \boldsymbol { \beta } ^ { T } } \\ { \boldsymbol { \beta } ^ { T } \boldsymbol { C _ { a } } } \\ { \boldsymbol { \updownarrow } } \\ { \boldsymbol { \beta } ^ { T } \boldsymbol { C _ { a } } ^ { l - 1 } } \end{array} \right] ,
$$

and combining with the first equation of (17) we have

$$
\begin{array} { r } { \mathbf { B e z } ( a , b ) = S ( a ) \left[ \begin{array} { c } { \mathbf { \beta } ^ { T } } \\ { \mathbf { \beta } ^ { T } C _ { a } } \\ { \vdots } \\ { \mathbf { \beta } ^ { T } C _ { a } ^ { l - 1 } } \end{array} \right] } \end{array}\tag{20}
$$

Theorem 1. The polynomials $a ( \lambda )$ and $b ( \lambda )$ have no zeros in common if and only if the associated Bezout matrix $\mathtt { B e z } ( a , b )$ is nonsingular.

PRoOF. For definiteness, let $l = \deg a ( \lambda ) \geq \deg b ( \lambda )$ Write the corresponding Bezout matrix $\boldsymbol { B } = \boldsymbol { \mathrm { B e z } } ( a , b )$ in the first form of (17) and observe that det $B \neq 0$ if and only if $b ( C _ { a } )$ is nonsingular. Since the eigenvalues of the latter matrix are of the form $b ( \lambda _ { i } )$ , where $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { l }$ are the zeros of $a ( \lambda )$ , the result follows.

Let $\begin{array} { r } { a ( \lambda ) = \sum _ { i = 0 } ^ { l } a _ { i } \lambda ^ { i } , a _ { l } \ne 0 , } \end{array}$ and $\begin{array} { r } { b ( \lambda ) = \sum _ { i = 0 } ^ { m } b _ { i } \lambda ^ { i } , b _ { m } \neq 0 } \end{array}$ , where $l \geq m$ As in the definition of the Bezout matrix, we may assume without loss of generality that $b ( \lambda )$ is written in the form $\sum _ { i = 0 } ^ { l } b _ { i } \lambda _ { i } ^ { i }$ , where the coefficients of the higher powers are, perhaps, zeros. With this assumption, we define the resultant (or Sylvester) matrix $R ( a , b )$ associated with the polynomials $a ( \lambda )$ and $b ( \lambda )$ as the $2 l \times 2 l$ matrix

$$
R ( a , b ) = [ \begin{array} { c c c c c c c c c } { a _ { 0 } } & { a _ { 1 } } & { \cdots } & { . } & { a _ { l - 1 } } & { a _ { l } } & & & \\ & & { . \cdot . . \cdot . } & & & & { . \cdot . } & { \cdot . } & \\ & & & { a _ { 0 } } & { a _ { 1 } } & { \cdots } & & { a _ { l - 1 } } & { a _ { l } } \\ { b _ { 0 } } & { b _ { 1 } } & { \cdots } & { b _ { m } } & { 0 } & { \cdots } & { 0 } & & \\ & & { \cdot . . \cdot . } & & { \cdot . . } & & { \cdot . } & & \\ & & & { b _ { 0 } } & { b _ { 1 } } & { \cdots } & { b _ { m } } & { 0 } & { \cdots } & { 0 } \end{array} ] \} \begin{array} { l } { \begin{array} { l } { { \dot { \chi } } } \\ { { \dot { \chi } } } \\ { { \dot { \chi } } } \\ { { \dot { \chi } } } \\ { { \dot { \chi } } } \end{array} } \\ { \begin{array} { l } { \begin{array} { r c c c c c c c c c } { \qquad } \end{array} } \\ { [ \begin{array} { c } { \dot { \chi } } \\ { \dot { \chi } } \\ { \dot { \chi } } \end{array} ] } \\ { \begin{array} { r c c c c c c c c } \end{array} } \end{array} } \\ { \begin{array} { r c c c c c c c c } \end{array} } \end{array}  \\ { [ \begin{array} { c } { \dot { \chi } } \\ { \dot { \chi } } \\ { \dot { \chi } } \end{array} ] } \\  \begin{array} { r c c c c c c c } { [ \begin{array} {array} { c \dot { \chi } } \\ { \dot { \chi } } \\ { \dot { \chi } } \end{array} ] + [ \begin{array} { c } { \dot { \chi } } \\ { \dot { \chi } } \\ { \dot { \chi } } \\ { \dot { \chi } } \end{array} ] } \\  [ \begin{array} { c } { \dot { \chi } } \\ { \dot { \chi } } \\ { \dot { \chi } } \end{array} \end{array}
$$

Partitioning $R ( a , b )$ into $l \times l$ matrices and using the notation introduced above we may also write

$$
R ( a , b ) = { \left[ \begin{array} { l l } { S ( { \hat { a } } ) P } & { P S ( a ) } \\ { S ( { \hat { b } } ) P } & { P S ( b ) } \end{array} \right] } .
$$

Using Eqs. (7) and (12) it follows that

$$
\begin{array} { r l } { \biggl [ \begin{array} { c c } { P } & { 0 } \\ { - S ( b ) } & { S ( a ) } \end{array} \biggr ] R ( a , b ) = \biggl [ \begin{array} { c c } { P S ( \hat { a } ) P } & { S ( a ) } \\ { \mathrm { B e z } ( a , b ) } & { 0 } \end{array} \biggr ] } & { } \\ { = \biggl [ \begin{array} { c c } { I } & { 0 } \\ { 0 } & { \mathrm { B e z } ( a , b ) } \end{array} \biggr ] \biggl [ \begin{array} { c c } { P S ( \hat { a } ) P } & { S ( a ) } \\ { I } & { 0 } \end{array} \biggr ] . } \end{array}\tag{21}
$$

This equation demonstrates an intimate connection between the resultant of $a ( \lambda )$ and $b ( \lambda )$ and their Bezout matrix. In particular, it is clear from equation (21) that $R ( a , b )$ and $\mathtt { B e z } ( a , b )$ have the same rank. Also, the resultant matrix (as well as the Bezoutian) can be used in solving the problem of whether the polynomials $a ( \lambda )$ and $b ( \lambda )$ have zeros in common.

Theorem 2. The polynomials $a ( \lambda )$ and $b ( \lambda )$ defined above have no common zeros $i f$ and only if the resultant matrix $R ( a , b )$ is nonsingular.

PrOOF. Since $S ( a )$ is nonsingular, it follows immediately from Eq. (21) that $R ( a , b )$ is nonsingular if and only if $\mathtt { B e z } ( a , b )$ is nonsingular. So the result follows from Theorem 1.

There is an interesting and more general result that we will not discuss. Namely, that the degree of the greatest common divisor of $a ( \lambda )$ and $b ( \lambda )$ is just $l -$ rank $R ( a , b )$

Note that the use of the resultant matrix may be more convenient than the use of the Bezoutian in the search for common divisors since, despite its double size, the elements of the resultant are just the coefficients of the given polynomials (or zero).

Exercise 6. Verify that the Bezout matrix associated with the polynomials $\begin{array} { r } { a ( \lambda ) = \sum _ { i = 0 } ^ { l } a _ { i } \lambda ^ { i } } \end{array}$ and $\begin{array} { r } { \bar { a } ( \lambda ) = \sum _ { i = 0 } ^ { l } \bar { a } _ { i } \lambda ^ { i } } \end{array}$ is skew-Hermitian. Combine this with Exercise 1 to show that the elements of $\mathtt { B e z } ( a , \bar { a } )$ are all pure imaginary,

Exercise 7. Check that the Bezout matrix B associated with the polynomials $\begin{array} { r } { a ( \lambda ) = \sum _ { i = 0 } ^ { l } a _ { i } \lambda ^ { i } , a _ { \mathrm { I } } \ne 0 , } \end{array}$ and $\begin{array} { r } { b ( \lambda ) = \sum _ { i = 0 } ^ { m } b _ { i } \lambda ^ { i } , l \ge m _ { \mathrm { i } } } \end{array}$ satisfies the equation

$$
\hat { C } _ { a } B = B C _ { a } ,\tag{22}
$$

where $C _ { a }$ and $\hat { C } _ { a }$ denote the first and second companion matrices associated with $a ( \lambda )$ , respectively. (The second companion matrix is defined by $\hat { C } _ { a } =$ $C _ { a } ^ { \mathbf { T } } ;$ and $C _ { a }$ is defined in Exercise 3.)

Hint. Apply Eq. (17).

Exercise 8. Let $\mathtt { B e z } ( a , b )$ denote the Bezout matrix associated with the polynomials $a ( \lambda )$ and $b ( \lambda )$ of degrees l and m $( 1 \geq m )$ , respectively. Show that

$$
\operatorname { B e z } ( { \hat { a } } , { \hat { b } } ) = - P \operatorname { B e z } ( a , b ) P ,
$$

where P is defined in Eq. (4).

Exercise 9. Let $a ( \lambda )$ and $b ( \lambda )$ be two polynomials of degrees l and m $( l \geq m )$ , respectively. Denote $a _ { \alpha } = a _ { \alpha } ( \lambda ) = a ( \lambda + \alpha ) , b _ { \alpha } = b _ { \alpha } ( \lambda ) = b ( \lambda + \alpha ) .$ and check that

$$
\mathbf { B e z } ( a _ { \mathfrak { x } } , b _ { \mathfrak { x } } ) = V _ { \mathfrak { x } } ^ { \scriptscriptstyle ( l ) } \mathbf { B e z } ( a , b ) ( V _ { \mathfrak { x } } ^ { \scriptscriptstyle ( l ) } ) ^ { \mathrm { T } } ,
$$

where $V _ { \alpha } ^ { ( l ) } = \left[ \binom { j } { i } \alpha ^ { j - i } \right] _ { i , j = 0 } ^ { l - 1 }$ and it is assumed that ${ \binom { j } { i } } = 0 { \mathrm { ~ f o r ~ } } j < i .$

Exercise 10. Prove that, for any polynomials $a ( \lambda )$ and $b ( \lambda )$ of degree not exceeding l,

$$
R ^ { \mathrm { T } } ( - b , a ) { \left[ \begin{array} { l l } { P } & { 0 } \\ { 0 } & { P } \end{array} \right] } R ( a , b ) = { \left[ \begin{array} { l l } { 0 } & { - B } \\ { B } & { 0 } \end{array} \right] } , \qquad B = \mathrm { B e z } ( a , b ) . \quad \bigsqcup
$$

## 13.4 The Hermite and the Routh-Hurwitz Theorems

The question of stability of eigenvalues can always be posed in terms of the zeros of a polynomial rather than the eigenvalues of a matrix. We need only replace the eigenvalue equation, $A { \boldsymbol { \mathbf { x } } } = \lambda { \boldsymbol { \mathbf { x } } }$ , by the characteristic equation, det $( \lambda I - A ) = 0$ . One advantage of the Lyapunov theorem of Section 13.1 is that it enables us to avoid computation of the coefficients of this polynomial and any consequent loss of accuracy. Nevertheless, it is important that we develop necessary and sufficient conditions that all the zeros of a polynomial lie in the left half of the complex plane. Consider a polynomial

$$
a ( \lambda ) = a _ { 0 } + a _ { 1 } \lambda + \cdots + a _ { l } \lambda ^ { l } , \qquad a _ { \mathrm { I } } \neq 0 ,
$$

with complex coefficients. The inertia In(a) of the polynomial $a ( \lambda )$ is defined as the triple of nonnegative integers $\{ \pi ( a ) , \nu ( a ) , \delta ( a ) \}$ , where $\pi ( a )$ (respectively, $\nu ( a )$ and $\delta ( a ) )$ denotes the number of zeros of $a ( \lambda ) .$ , counting multiplicities, with positive (respectively, negative and zero) real parts. Like matrices, the inertia of a polynomial $a ( \lambda )$ is also called the inertia of $\mathbf { \dot { \boldsymbol { a } } } ( \lambda )$ with respect to the imaginary axis. In particular, a polynomial $a ( \lambda )$ with $\pi ( a ) = \delta ( a ) = 0$ is said to be a stable polynomial (with respect to the imaginary axis).

In contrast, there is the triple ${ \cal I } n ^ { \prime } ( a ) = \{ \pi ^ { \prime } ( a ) , \nu ^ { \prime } ( a ) , \delta ^ { \prime } ( a ) \}$ , where $\pi ^ { \prime } ( a )$ $\nu ^ { \prime } ( a ) , \delta ^ { \prime } ( a )$ denote the number of zeros of $a ( \lambda )$ lying in the open upper halfplane, the open lower half-plane, and on the real axis, respectively. This triple is referred to as the inertia of $a ( \lambda )$ with respect to the real axis. Clearly,

$$
\{ \pi ^ { \prime } ( \tilde { a } ) , \nu ^ { \prime } ( \tilde { a } ) , \delta ^ { \prime } ( \tilde { a } ) \} = \{ \pi ( a ) , \nu ( a ) , \delta ( a ) \} ,
$$

where $\tilde { a } = \tilde { a } ( \lambda ) = a ( - i \lambda ) . \operatorname { I f } a ( \lambda )$ is a polynomial with real coefficients, then its complex zeros occur in conjugate pairs and hence $\pi ^ { \prime } ( a ) = \nu ^ { \prime } ( a )$

The main result of this section is due to C. Hermite† and is concerned with the distribution of zeros of a complex polynomial with respect to the real axis. The formulation in terms of the Bezoutian is due to M. Fujiwara in 1926. Indeed, it was Fujiwara who first used Bezout matrices to develop a systematic approach to stability criteria, including those of Sections 13.4 and 13.5.

Consider a polynomial $\begin{array} { r } { a ( \lambda ) = \sum _ { j = 0 } ^ { l } a _ { j } \lambda ^ { j } ( a _ { l } \neq 0 ) } \end{array}$ and let $\begin{array} { r } { \bar { a } ( \lambda ) = \sum _ { j = 0 } ^ { l } \bar { a } _ { j } \lambda ^ { j } . } \end{array}$ If $\boldsymbol { B } = \mathbf { B e z } ( \boldsymbol { a } , \overline { { \boldsymbol { a } } } )$ denotes the Bezout matrix associated with $a ( \lambda )$ and $\overline { { { a } } } ( \lambda ) ,$ then it is skew-Hermitian (see Exercise 13.3.6) and it is also nonsingular if and only if $a ( \lambda )$ and $\overline { { a } } ( \lambda )$ have no zeros in common (Theorem 13.3.1). Thus, det $B \neq 0$ if and only if a(λ) has no real zeros and no zeros occuring in conjugate pairs.

Theorem 1. With the notation of the previous paragraph, assume that det $B \neq 0$ . Then

$$
\pi ^ { \prime } ( a ) = \pi \bigg ( \frac { 1 } { i } B \bigg ) ,
$$

$$
\nu ^ { \prime } ( a ) = \nu \bigg ( \frac { 1 } { i } B \bigg ) ,
$$

$$
\delta ^ { \prime } ( a ) = \delta \left( { \frac { 1 } { i } } B \right) = 0 .
$$

ProoF. In applying formula (13.3.22), observe that

$$
\hat { C } _ { a } = C _ { a } ^ { * } - [ \pmb { \theta } \quad \cdot \cdot \cdot \quad \pmb { \theta } \quad \pmb { v } ] ,
$$

where $\pmb { v } = [ a _ { 0 } a _ { l } ^ { - 1 } - \bar { a } _ { 0 } \bar { a } _ { l } ^ { - 1 } , \ldots , a _ { l - 1 } a _ { l } ^ { - 1 } - \bar { a } _ { l - 1 } \bar { a } _ { l } ^ { - 1 } ] ^ { \mathrm { T } } .$

Thus

$$
C _ { a } ^ { * } B - B C _ { a } = [ \pmb { \theta } \quad \cdots \quad \pmb { \theta } \quad \pmb { v } ] B = W ,\tag{1}
$$

and we are now to show that $W \geq 0$ . Using the first factorization of (13.3.17), and noting that

$$
[ \pmb { \theta } \quad \cdots \quad \pmb { \theta } \quad \pmb { v } ] S ( \pmb { a } ) = a _ { l } [ \pmb { v } \quad \pmb { \theta } \quad \cdots \quad \pmb { \theta } ] ,
$$

we have

$$
W = [ \pmb { \theta } \quad \cdots \pmb { \theta } \quad \pmb { v } ] \pmb { B } = a _ { l } [ \pmb { v } \quad \pmb { \theta } \quad \cdots \quad \pmb { \theta } ] \overline { { \mathfrak { a } } } ( C _ { a } ) = a _ { l } \pmb { v } \pmb { e } _ { 1 } ^ { T } \overline { { \mathfrak { a } } } ( C _ { a } ) .
$$

But

$$
e _ { 1 } ^ { T } \bar { a } ( C _ { a } ) = \sum _ { j = 0 } ^ { l } \bar { a } _ { j } e _ { 1 } ^ { T } C _ { a } ^ { j } = \sum _ { j = 0 } ^ { l - 1 } \bar { a } _ { j } e _ { j + 1 } ^ { T } + \bar { a } _ { l } e _ { l } ^ { T } C _ { a } = - \bar { a } _ { l } v ,
$$

and consequently, $W = - | a _ { l } | ^ { 2 } v v ^ { T } = | a _ { l } | ^ { 2 } v v ^ { \ast } \geq 0 .$

Write Eq. (1) in the form

$$
( - i C _ { a } ) ^ { * } \bigg ( \frac { 1 } { i } B \bigg ) + \bigg ( \frac { 1 } { i } B \bigg ) ( - i C _ { a } ) = W \geq 0 ,\tag{2}
$$

and recall that the assumption of nonsingularity of B implies that $\delta ( i C _ { a } ) = 0 .$ Hence Theorem 13.1.3 yields

$$
\mathbf { I n } ( - i C _ { a } ^ { * } ) = \mathbf { I n } \Big ( \frac { 1 } { i } B \Big ) ,
$$

and the assertion follows in view of the relations

$$
\pi ( - i C _ { a } ) ^ { * } = \pi ( - i C _ { a } ) = v ( i C _ { a } ) = \pi ^ { \prime } ( C _ { a } ) = \pi ^ { \prime } ( a ) ,
$$

and similarly for $\nu ( - i C _ { a } ) ^ { * }$ . ■

Corollary 1. All the zeros of the polynomial a(λ) lie in the open upper halfplane if and only $i f \left( 1 / i \right) B > { \cal O } _ { : }$ where $\boldsymbol { B } = \mathrm { B e z } ( \boldsymbol { a } , \overline { { \boldsymbol { a } } } )$

Example 1. The polynomial

$$
a ( \lambda ) = \lambda ^ { 4 } + 4 i \lambda ^ { 3 } - 4 \lambda ^ { 2 } - 1 = ( \lambda + i ) ^ { 2 } ( \lambda ^ { 2 } + 2 i \lambda + 1 )
$$

clearly has zeros $- i , - i , ( - 1 \pm \sqrt { 2 } ) i ,$ We have

$$
\begin{array} { r l } { B = \mathbf { B } x \boldsymbol { \alpha } ( u , \vec { u } ) } & { } \\ { = } & { \left[ \begin{array} { l l l l } { 0 } & { - 4 } & { 4 \ell } & { 1 } \\ { - 4 } & { 4 } & { 1 } & { 1 } \\ { 4 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } \end{array} \right] \left[ \begin{array} { l l l l } { - 1 } & { 0 } & { - 4 } & { - 4 \ell } \\ { 0 } & { - 1 } & { 0 } & { - 4 } \\ { 0 } & { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - 1 } \end{array} \right] } \\ { \mathrm { ~ } } & { } \\ { - \left[ \begin{array} { l l l l } { 0 } & { - 4 } & { - \vec { u } } & { 1 } \\ { - 4 } & { - 4 \ell } & { 1 } & { 1 } \\ { - 4 } & { 1 } & { 0 } & { 0 } \\ { \ell } & { 0 } & { 0 } & { 0 } \end{array} \right] \left[ \begin{array} { l l l l } { - 1 } & { 0 } & { - 4 } & { \vec { u } } \\ { 0 } & { - 1 } & { 0 } & { - 4 } \\ { 0 } & { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - 1 } \end{array} \right] } \\ { = } & { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { - 8 } & { 0 } \\ { 0 } & { - 8 } & { 0 } & { 0 } \\ { - 8 } & { 0 } & { - 3 2 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - 8 } \end{array} \right] , } \end{array}
$$

Hence, using the Jacobi theorem, Theorem 8.6.1,

$$
\mathrm { I n } \left( { \frac { 1 } { i } } B \right) = \mathrm { I n } \left[ { \begin{array} { r r r r } { - 8 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { - 3 2 } & { 0 } & { - 8 } \\ { 0 } & { 0 } & { - 8 } & { 0 } \\ { 0 } & { - 8 } & { 0 } & { 0 } \end{array} } \right] = \{ 1 , 3 , 0 \} .
$$

Thus, $\pi ^ { \prime } ( a ) = 1$ and $\nu ^ { \prime } ( a ) = 3 ,$ as required. □

Note that Theorem 1 gives no information if $a ( \lambda )$ is a real polynomial since in this case $B = \theta$ . Methods for evaluating the inertia of a real polynomial with respect to the real axis, as well as a condition for a polynomial to have no real zeros, are discussed in Section 6.

As soon as the zero-location problem is solved with respect to the upper and lower half-planes, the results can be reformulated for any other pair of mutually complementary half-planes in the complex plane. The problem of determining the distribution of zeros relative to the imaginary axis is of particular interest in view of the application to differential equations (see Section13.1); this is known as the Routh-Hurwitz problem.

Let $\begin{array} { r } { a ( \lambda ) = \sum _ { j = 0 } ^ { l } a _ { j } \lambda ^ { j } ( a _ { l } \neq 0 ) } \end{array}$ and let $\widehat { B }$ stand for the Bezout matrix associated with $a ( \lambda )$ and $\tilde { a } ( - \lambda )$ . Define $D = \mathrm { d i a g } [ 1 , - 1 , . . . , ( - 1 ) ^ { t - 1 } ]$ and note that the matrix $\tilde { \pmb { B } } = \hat { \pmb { B } } \pmb { D }$ is nonsingular if and only if $a ( \lambda )$ has no pure imaginary zeros or zeros symmetric relative to the origin.

Theorem 2. With the notation of the previous paragraph, the matrix $\widetilde { B } = \widehat { B } D$ is Hermitian. $I f \widetilde { B }$ is also nonsingular, then

$$
\begin{array} { l } { { \pi ( a ) = v ( \widetilde { B } ) , } } \\ { { \nu ( a ) = \pi ( \widetilde { B } ) , } } \\ { { \delta ( a ) = \delta ( \widetilde { B } ) = 0 . } } \end{array}
$$

ProoF. The assertion of the theorem follows from Theorem 1 and the easily verified relation

$$
F \biggl ( \frac { 1 } { i } B \biggr ) F ^ { * } = - \widetilde { B } ,
$$

where $F = \mathrm { d i a g } [ i ^ { l - 1 } , i ^ { l - 2 } , \ldots , i , 1 ]$ and B is the Bezoutian associated with $a _ { 1 } ( \lambda ) = a ( - i \lambda )$ and $\overline { { { a } } } _ { 1 } ( \lambda ) = \overline { { { a } } } ( i \lambda )$ ■

Corollary 1. A polynomial $a ( \lambda )$ is stable if and only if the matrix $\widetilde { B }$ is positive denite.

Example 2. Consider the polynomials $a ( \lambda ) = \lambda ^ { 2 } - 2 \lambda + 5$ and $a ( - \lambda ) =$ $\lambda ^ { 2 } + 2 \lambda + 5$ The corresponding Bezoutian is

$$
{ \widehat { B } } = { \left[ \begin{array} { l l } { - 2 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l } { 5 } & { 2 } \\ { 0 } & { 5 } \end{array} \right] } - { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l } { 5 } & { - 2 } \\ { 0 } & { 5 } \end{array} \right] } = { \left[ \begin{array} { l l } { - 2 0 } & { 0 } \\ { 0 } & { 4 } \end{array} \right] } ,
$$

and hence the matrix

$$
\widetilde { B } = \left[ \begin{array} { r r } { { - 2 0 } } & { { 0 } } \\ { { 0 } } & { { - 4 } } \end{array} \right]
$$

is negative definite. Thus both zeros, $\lambda _ { 1 }$ and $\lambda _ { 2 }$ , of the polynomial lie in the open right half-plane, as required, since $\lambda _ { 1 } = 1 + 2 i$ and $\lambda _ { 2 } = 1 - 2 i$ □

If $a ( \lambda )$ in Theorem 2 is a real polynomial, then those i, jth elements of the matrix B with $i + j$ odd are zeros. This is illustrated in the following exercise.

Exercise 3. Check that the matrix $\widetilde { B }$ defined in Theorem 2 and associated with the real polynomial $a ( \lambda ) = a _ { 0 } + a _ { 1 } \lambda + a _ { 2 } \lambda ^ { 2 } + a _ { 3 } \lambda ^ { 3 } + a _ { 4 } \lambda ^ { 4 }$ is

$$
\widetilde { B } = 2 \left[ \begin{array} { c c c c c } { a _ { 0 } a _ { 1 } } & { 0 } & { a _ { 0 } a _ { 3 } } & { 0 } \\ { 0 } & { a _ { 1 } a _ { 2 } - a _ { 0 } a _ { 3 } } & { 0 } & { a _ { 1 } a _ { 4 } } \\ { a _ { 0 } a _ { 3 } } & { \mathrm { ~ \iota ~ ~ } \cdot \mathrm { ~ 0 ~ } } & { a _ { 2 } a _ { 3 } - a _ { 1 } a _ { 4 } } & { 0 } \\ { 0 } & { a _ { 1 } a _ { 4 } } & { 0 } & { a _ { 3 } a _ { 4 } } \end{array} \right] . \quad \square
$$

The existence of symmetrical patterns of zeros in the matrix allows us to compute the inertia of the matrix

$$
\boldsymbol { Q } ^ { \mathrm { T } } \tilde { \boldsymbol { B } } \boldsymbol { Q } = \left[ \begin{array} { l l } { B _ { 1 } } & { \phantom { - } \theta } \\ { \phantom { - } \theta } & { B _ { 2 } } \end{array} \right]
$$

instead of In ${ \pmb { \widetilde { B } } } .$ Here

$$
Q = [ Q _ { 1 } \quad Q _ { 2 } ]\tag{3}
$$

is a permutation matrix defined by

$$
Q _ { 1 } = [ e _ { 1 } \quad e _ { 3 } \quad \cdots \quad e _ { k } ] , \qquad Q _ { 2 } = [ e _ { 2 } \quad e _ { 4 } \quad \cdots \quad e _ { j } ] ,
$$

where $e _ { 1 } , e _ { 2 } , \ldots , e _ { i }$ are the unit vectors in $\mathbb { C } ^ { l } , k = l - 1$ and $j = l \dot { \mathbf { u } }$ l is even, $k = l$ and $j = l - 1$ if l is odd.

Exercise 4. Show that the inertia of the matrix B discussed in Exercise 3 $\widetilde { B }$ is equal to In $B _ { 1 } +$ In $B _ { 2 }$ , where

$$
\begin{array}{c} \begin{array}{c} \begin{array} { c c } { { B _ { 1 } = \left[ { a _ { 0 } a _ { 1 } } \right]} & { { a _ { 0 } a _ { 3 } } } \\ { { a _ { 0 } a _ { 3 } } } & { { a _ { 2 } a _ { 3 } - a _ { 1 } a _ { 4 } } } \end{array}  , ~ }  & { { B _ { 2 } = \left[ { a _ { 1 } a _ { 2 } - a _ { 0 } a _ { 3 } } \right]} & { { a _ { 1 } a _ { 4 } } } \\ { { a _ { 1 } a _ { 4 } } } & { { a _ { 3 } a _ { 4 } } } \end{array}  . ~ { \boxed { 1 } } }  \end{array}
$$

A different form of the Routh-Hurwitz theorem for real polynomials will be obtained in Section 13.9.

## 13.5 The Schur-Cohn Theorem

The determination of the number of zeros of a polynomial lying inside the unit circle is known as the Schur-Cohn problem and, as noted in Section 13.2, it is closely related to the stability problem for linear difference equations. A solution of this problem in terms of a corresponding Bezout matrix is presented in this section.

Consider a complex polynomial $a ( \lambda ) = a _ { 0 } + a _ { 1 } \lambda + \cdots + a _ { l } \lambda ^ { l } \left( a _ { l } \neq 0 \right)$ and define the inertia of a(λ) with respect to the unit circle to be the triple of numbers $\alpha ( a ) = \{ \alpha _ { + } ( a ) , \alpha _ { - } ( a ) , \alpha _ { 0 } ( a ) \}$ , where $\alpha _ { + } ( a )$ (respectively, $\alpha _ { - } ( a )$ and $\alpha _ { 0 } ( a ) )$ denotes the number of zeros of $a ( \lambda )$ , counted with their multiplicities, lying inside the open unit circle (respectively, outside and on the unit circumference).

Theorem 1. Let $\begin{array} { r } { a ( \lambda ) = \sum _ { j = 0 } ^ { l } a _ { j } \lambda ^ { j } \left( a _ { l } \neq 0 \right) } \end{array}$ and let B stand for the Bezoutian associated with ā(λ) and $\overline { { \hat { a } } } ( \lambda ) \triangleq \lambda ^ { l } \bar { a } ( \lambda ^ { - 1 } )$ . If P is a rotation matrix then the matrix $\check { B } = P B ;$ , is Hermitian and, if it is nonsingular,

$$
\alpha _ { + } ( a ) = \pi ( \check { B } ) ,
$$

$$
\alpha _ { - } ( a ) = \nu ( \check { B } ) ,
$$

$$
\alpha _ { \bf 0 } ( a ) = \delta ( \breve { B } ) = 0 .
$$

ProoF. The proof of the theorem consists in proving the relation

$$
\vec { B } - C _ { a } ^ { * l } \vec { B } C _ { a } ^ { l } = ( \hat { \bar { a } } ( C _ { a } ) ) ^ { * } \hat { \bar { a } } ( C _ { a } ) > 0\tag{1}
$$

and in applying Theorem 13.2.2. Note that the equality $\check { B } = \check { B } ^ { * }$ is easily established by transposing the expression for B in Eq. (13.3.7) and reducing it by use of the relation $P ^ { 2 } = I$ to the expression in Eq. (13.3.13).

First use the identity (13.3.6) to deduce that

$$
S ( \hat { \bar { a } } ) P S ( a ) C _ { a } ^ { l } = - S ( \hat { \bar { a } } ) S ( \hat { a } ) P ,
$$

and then (13.3.12) implies

$$
S ( \widehat { \bar { a } } ) S ( \widehat { a } ) P = - S ( a ) P S ( \widehat { \bar { a } } ) C _ { a } ^ { l } .
$$

Use this in the representation for B given by Proposition 13.3.1:

$$
\begin{array} { l } { { B = S ( a ) S ( \bar { a } ) P - S ( \hat { \bar { a } } ) S ( \hat { a } ) P } } \\ { { \ = S ( a ) S ( \bar { a } ) P + S ( a ) P S ( \hat { \bar { a } } ) C _ { a } ^ { l } . } } \end{array}
$$

But Proposition 13.3.2 also gives $B = S ( a ) \widehat { \bar { a } } ( C _ { a } ) ,$ and so

$$
\widehat { \bar { a } } ( C _ { a } ) = S ( \bar { a } ) P + P S ( \widehat { \bar { a } } ) C _ { a } ^ { l } .
$$

Consider the conjugate transposed relation and postmultiply by $\hat { \bar { a } } ( C _ { a } )$ $= S ( a ) ^ { - 1 } B$ to obtain

$$
\widehat { \bar { a } } ( C _ { a } ) ^ { * } \widehat { \bar { a } } ( C _ { a } ) = { \cal P } B + C _ { a } ^ { * l } S ( \widehat { a } ) { \cal P } \widehat { \bar { a } } ( C _ { a } ) .\tag{2}
$$

But using (13.3.6) again,

$$
\begin{array} { c } { { S ( \widehat { a } ) P \widehat { \widehat { a } } ( C _ { a } ) = - P S ( a ) C _ { a } ^ { l } \widehat { \widehat { a } } ( C _ { a } ) = - P S ( a ) \widehat { \widehat { a } } ( C _ { a } ) C _ { a } ^ { l } } } \\ { { = - P B C _ { a } ^ { l } . } } \end{array}
$$

Thus, Eq. (2) takes the form

$$
\widehat { \bar { a } } ( C _ { a } ) ^ { * } \widehat { \bar { a } } ( C _ { a } ) = \check { \cal B } - C _ { a } ^ { * } { } ^ { l } \check { \cal B } C _ { a } ^ { l } ,
$$

which is Eq. (1).

Hence by Theorem 13.2.2, the matrix $C _ { a } ^ { i }$ has $\pi ( { \\\check { B } } )$ eigenvalues inside the unit circle and $v ( \tilde { B } )$ eigenvalues outside it. Obviously, the same can be said about the eigenvalues of $C _ { \pmb { a } }$ and, consequently, about the zeros of the polynomial $a ( \lambda )$

Corollary 1. A polynomial $a ( \lambda )$ is stable with respect to the unit circle if and only $i f$ the matrix $\check { B }$ is positive deinite.

## 13.6 Perturbations of a Real Polynomial

Let $a ( \lambda )$ be a polynomial of degree l with real coefficients. In this section we are concerned with the effect of perturbing the coefficients of $a ( \lambda )$ with purely imaginary numbers. In particular, we will study the relation between the inertias (with respect to the real axis) of the original and the perturbed polynomials. These results will be applied in subsequent sections to obtain criteria for a real polynomial to be stable.

The main result of this section is presented first and then is used to provide a unified approach to some classical stability criteria.

Theorem 1 (P. Lancaster and M. Tismenetsky†). Let $\begin{array} { r } { a ( \lambda ) = \sum _ { i = 0 } ^ { l } a _ { i } \lambda ^ { i } } \end{array}$ $( a _ { l } \neq 0 )$ and $\begin{array} { r } { \dot { b } ( \lambda ) = \sum _ { i = 0 } ^ { l - 1 } b _ { i } \lambda ^ { i } } \end{array}$ be polynomials with real coefficients. Write $\tilde { a } ( \lambda ) = a ( \lambda ) + i b ( \lambda )$ . If the Bezout matrix $\pmb { { \cal B } } = \mathbf { B e z } ( a , b )$ is nonsingular, that is, $i f a ( \lambda )$ and b(λ) are relatively prime, then

$$
\delta ^ { \prime } ( \tilde { a } ) = 0\tag{1}
$$

and

$$
\pi ^ { \prime } ( a ) \leq \pi ^ { \prime } ( { \tilde { a } } ) = \nu ( B ) , \qquad \nu ^ { \prime } ( a ) \leq \nu ^ { \prime } ( { \tilde { a } } ) = \pi ( B ) .\tag{2}
$$

Furthermore, equalities hold throughout Eq. (2) $i f \delta ^ { \prime } ( a ) = 0 .$

This theorem means that the perturbation $b ( \lambda )$ has the effect of shifting all real zeros of $a ( \lambda )$ off the real axis, and the numbers $\pi ^ { \prime } ( \tilde { a } )$ and $\nu ^ { \prime } ( \tilde { a } )$ of eigenvalues of the perturbed polynomial above and below the real axis, respectively, can be counted using the inertia properties of B.

PROOF. Suppose that $\tilde { a } ( \lambda _ { 0 } ) = 0$ and $\lambda _ { 0 }$ is real. Then $a ( \lambda _ { 0 } ) , b ( \lambda _ { 0 } )$ are real and so $\tilde { a } ( \lambda _ { 0 } ) = a ( \lambda _ { 0 } ) + i b ( \lambda _ { 0 } ) = 0$ implies that $a ( \lambda _ { 0 } ) = b ( \lambda _ { 0 } ) = 0$ Thus $a ( \lambda )$ and b(λ) have a common zero, contradicting the hypothesis that B is nonsingular. Hence the relation (1).

As noted earlier, the Bezout matrix B satisfies Eq. (13.3.22) which, when $\tilde { a } ( \lambda ) = a ( \lambda )$ , can be written in the form $C _ { a } ^ { * } B = B C _ { a }$ , where $C _ { a }$ is the companion matrix associated with $a ( \lambda )$ , or, what is equivalent,

$$
( i C _ { a } ) ^ { * } B + B ( i C _ { a } ) = 0 .\tag{3}
$$

We also know (see Exercise 13.3.1) that B is real and symmetric.

The companion matrix $C _ { \tilde { a } }$ is related to $C _ { a }$ by

$$
C _ { a } = C _ { \tilde { a } } + F D ,\tag{4}
$$

where $D = \mathrm { d i a g } [ b _ { 0 } , b _ { 1 } , . . . , b _ { l - 1 } ]$ and

$$
F = \left[ \begin{array} { l l l } { 0 } & { \cdots } & { 0 } \\ { \vdots } & { } & { \vdots } \\ { 0 } & { \cdots } & { 0 } \\ { i a _ { l } ^ { - 1 } } & { \cdots } & { i a _ { l } ^ { - 1 } } \end{array} \right]
$$

Substituting from Eq. (4) into Eq. (3), it is found that

$$
( i C _ { \tilde { a } } ) ^ { * } B + B ( i C _ { \tilde { a } } ) = i D F ^ { * } B - i B F D .\tag{5}
$$

Now use the representation (13.3.20) for B to obtain

$$
i D F ^ { * } B = D \left[ \begin{array} { c c c c } { { 1 } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { 1 } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { 1 } } & { { 0 } } & { { \cdots } } & { { 0 } } \end{array} \right] \left[ \begin{array} { c } { { \pmb { b } ^ { \operatorname { T } } } } \\ { { \pmb { b } ^ { \operatorname { T } } C _ { a } } } \\ { { \vdots } } \\ { { \pmb { b } ^ { \operatorname { T } } C _ { a } ^ { l - 1 } } } \end{array} \right] = D A D ,
$$

where $\pmb { b } ^ { \mathrm { { I } } } = [ b _ { 0 } \quad b _ { 1 } \quad \cdots \quad b _ { l - 1 } ]$ and A is the $l \times l$ matrix with all elements equal to 1. Furthermore, $- i B F D = ( i D F ^ { * } B ) ^ { * } = D A D$ and therefore Eq. (5) implies

$$
( i C _ { \tilde { a } } ) ^ { * } B + B ( i C _ { \tilde { a } } ) = W ,\tag{6}
$$

where $W = 2 D A D \geq 0 .$

Since $\delta ^ { \prime } ( \tilde { a } ) = 0 ;$ then $\delta ( i C _ { \tilde { a } } ) = 0$ and, by Theorem 13.1.3, ${ \bf I n } ( i C _ { \tilde { a } } ) =$ In B. When B is nonsingular, Proposition 13.1.2 can be applied to Eq. (3) to yield the inequalities in (2).

The additional condition $\delta ^ { \prime } ( a ) = \delta ( i C _ { a } ) = 0$ together with det $B \neq 0$ yields (in view of Theorem 13.1.3 and Eq. (3)) equality throughout (2). This completes the proof.

Corollary 1. If, in the previous notation, $B < 0 o r B > 0 ,$ then the zeros of the polynomial $\tilde { \pmb { a } } ( \lambda )$ lie in the open upper half-plane or open lower half-plane, respectively.

Example 1. The polynomial $a ( \lambda ) = \lambda ^ { 2 } - 1$ has two real zeros. The perturbation $i b ( \lambda ) = 2 i \lambda$ satisfies the hypothesis of Theorem 1 and

$$
B = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l } { 0 } & { 2 } \\ { 2 } & { 0 } \end{array} \right] } = 2 I > 0 .
$$

Hence both zeros of $\lambda ^ { 2 } + 2 i \lambda - 1$ are in the open lower half-plane.

Exercise 2. By use of Theorem 1, check that the polynomial $\tilde { a } ( \lambda ) = \lambda ^ { 4 } +$ $4 i \lambda ^ { 3 } - 4 \lambda ^ { 2 } - 1$ has three zeros with negative imaginary parts and a zero with a positive imaginary part. □

Another hypothesis leading to the main conclusion (Eq. (2)) of Theorem 1 is expressed in terms of controllability.

Theorem 2. With the notation of Theorem 1 (and its proof), let the pair $( C _ { \tilde { a } } ^ { * } , W )$ be controllable. Then the Bezout matrix B associated with $a ( \lambda )$ and $b ( \lambda )$ is nonsingular, $\delta ( \tilde { a } ) = 0 ,$ and the relations (2) hold.

The proof of Theorem 2 is easily obtained by applying Theorem 13.1.4 to Eq. (6).

Exercise 3. Let $\begin{array} { r } { a ( \lambda ) = \sum _ { i = 0 } ^ { l } a _ { i } \lambda ^ { i } , a _ { l } \neq 0 , a _ { i } = \bar { a } _ { i } , i = 0 , 1 , \ldots , l . } \end{array}$ Prove that the polynomial $\tilde { a } ( \lambda ) = a ( \lambda ) + i b _ { 0 } ( b _ { 0 } > 0 )$ has no real spectrum and that

$$
v ^ { \prime } ( a ) - \pi ^ { \prime } ( a ) = \left\{ \begin{array} { l l } { 0 \quad } & { \mathrm { i f } \quad l \mathrm { i s e v e n } , } \\ { \mathrm { s g n } a _ { l } \quad } & { \mathrm { i f } \quad l \mathrm { i s o d d } . } \end{array} \right.
$$

Hint. Apply Theorem 2. □

## 13.7 The Liénard-Chipart Criterion

The names of A. Liénard and M. Chipart are strongly associated with a stability criterion for the zeros of real polynomials. Using the results of the previous section, we can now present a modified version of the original Liénard-Chipart† stability criterion in terms of a Bezoutian.

Consider a polynomial $\begin{array} { r } { a ( \lambda ) = \sum _ { j = 0 } ^ { l } a _ { j } \lambda ^ { j } . } \end{array}$ with $a _ { \imath } \neq 0$ and real coefficients. If l is even, define

$$
h ( \lambda ) = \sum _ { j = 0 } ^ { l / 2 } a _ { 2 j } \lambda ^ { j } , \qquad g ( \lambda ) = \sum _ { j = 0 } ^ { ( l / 2 ) - 1 } a _ { 2 j + 1 } \lambda ^ { j } .
$$

If l is odd, then we put

$$
h ( \lambda ) = \sum _ { j = 0 } ^ { 1 / 2 ( l - 1 ) } a _ { 2 j } \lambda ^ { j } , \qquad g ( \lambda ) = \sum _ { j = 0 } ^ { 1 / 2 ( l - 1 ) } a _ { 2 j + 1 } \lambda ^ { j } .
$$

For brevity, we refer to $h ( \lambda )$ and $g ( \lambda )$ , as well as to the obvious representation

$$
a ( \lambda ) = h ( \lambda ^ { 2 } ) + \lambda g ( \lambda ^ { 2 } ) ,\tag{1}
$$

as the $L { - } C$ splitting of $a ( \lambda )$

Theorem 1. Let Eq. (1) be the L-C splitting of the real polynomial $a ( \lambda )$ Denote

$$
a _ { 1 } ( \lambda ) = \left\{ \begin{array} { l } { { h ( - \lambda ^ { 2 } ) \qquad i f \quad l \ i s \ e v e n , } } \\ { { \lambda g ( - \lambda ^ { 2 } ) \qquad i f \quad l \ i s \ o d d ; } } \end{array} \right.
$$

$$
a _ { 2 } ( \lambda ) = \left\{ \begin{array} { l } { { \lambda g ( - \lambda ^ { 2 } ) ~ i f ~ l ~ i s ~ e v e n , } } \\ { { - h ( - \lambda ^ { 2 } ) ~ i f ~ l ~ i s ~ o d d . } } \end{array} \right.
$$

If the Bezout matrix B associated with $a _ { 1 } ( \lambda )$ and $a _ { 2 } ( \lambda )$ is nonsingular, then a(λ) has no pure imaginary zeros and

$$
\pi ( a ) = \pi ( B ) , \qquad \nu ( a ) = \nu ( B ) .\tag{2}
$$

ProoF. Let / be even. Define the polynomial ã(λ) by $\tilde { a } ( \lambda ) = a ( i \lambda ) =$ $h ( - \lambda ^ { 2 } ) + i \lambda g ( - \lambda ^ { 2 } ) = a _ { 1 } ( \lambda ) + i a _ { 2 } ( \lambda )$ and observe that $\tilde { a } ( \lambda )$ has no real zeros. Indeed, if there were a real $\lambda _ { 0 }$ such that $a _ { 1 } ( \lambda _ { 0 } ) + i a _ { 2 } ( \lambda _ { 0 } ) = 0$ then, taking complex conjugates, we would obtain $a _ { 1 } ( \lambda _ { 0 } ) - i a _ { 2 } ( \lambda _ { 0 } ) = 0 .$ Thus, it would follow by comparison that $a _ { 2 } ( \lambda _ { 0 } ) = 0$ and hence $a _ { \mathrm { 1 } } ( \lambda _ { 0 } ) = 0$ This conflicts with the assumed relative primeness of $a _ { 1 } ( \lambda )$ and $a _ { 2 } ( \lambda )$ (implied by det $B \neq 0 )$

Now applying Theorem 13.6.1, we obtain

$$
\begin{array} { c } { { \displaystyle v ( B ) = \pi ^ { \prime } ( \tilde { a } ) = v ( a ) , } } \\ { { } } \\ { { \pi ( B ) = \nu ^ { \prime } ( \tilde { a } ) = \pi ( a ) , } } \\ { { } } \\ { { \delta ( B ) = \delta ^ { \prime } ( \tilde { a } ) = \delta ( a ) , } } \end{array}
$$

and the theorem is established for the case of an even l.

If l is odd, then write

$$
- i \tilde { a } ( \lambda ) = \lambda g ( - \lambda ^ { 2 } ) - i h ( - \lambda ^ { 2 } ) = a _ { \mathrm { i } } ( \lambda ) + i a _ { 2 } ( \lambda )
$$

and observe that the zeros of $\tilde { a } ( \lambda )$ and $- i \tilde { a } ( \lambda )$ coincide. Now apply Theorem 13.6.1 again.

Corollary 1. The polynomial a(λ) is stable if and only if $B = \mathtt { B e z } ( a _ { 1 } , a _ { 2 } )$ is negative definite.

PROOF. If $a ( \lambda )$ is stable, then the polynomials $a _ { 1 } ( \lambda )$ and $a _ { 2 } ( \lambda )$ defined above are relatively prime. Indeed, if $a _ { 1 } ( \lambda _ { 0 } ) = a _ { 2 } ( \lambda _ { 0 } ) = 0$ then also $a _ { \mathrm { 1 } } ( \tilde { \lambda } _ { \mathrm { 0 } } ) =$ $a _ { 2 } ( \bar { \lambda } _ { 0 } ) = 0$ and $\tilde { a } ( \lambda _ { 0 } ) = \tilde { a } ( \lambda _ { 0 } ) = 0$ Hence $a ( \lambda )$ has complex zeros $\mu$ and $- \bar { \mu } ~ ( \mu = i \lambda _ { 0 } )$ or a pure imaginary zero $i \lambda _ { 0 } \ ( \lambda _ { 0 } = \bar { \lambda } _ { 0 } )$ . In both cases we contradict the assumption that all zeros of $a ( \lambda )$ lie in the open left half-plane. Thus, B is nonsingular and, by the theorem, must be negative definite.■

Example 1. Consider the polynomial $a ( \lambda ) = ( \lambda - 1 ) ^ { 2 } ( \lambda + 2 )$ and the representation

$$
- i \tilde { a } ( \lambda ) = - i a ( i \lambda ) = \lambda ( - 3 - \lambda ^ { 2 } ) - 2 i .
$$

Here $a _ { 1 } ( \lambda ) = - \lambda ( 3 + \lambda ^ { 2 } ) , a _ { 2 } ( \lambda ) = - 2$ , and the corresponding Bezoutian is

$$
B = { \left[ \begin{array} { l l l } { 6 } & { 0 } & { 2 } \\ { 0 } & { 2 } & { 0 } \\ { 2 } & { 0 } & { 0 } \end{array} \right] } ,
$$

with In $B = \{ 2 , 1 , 0 \}$ . (To see this, use the Jacobi method.) Thus, by Eqs. (2), also $\mathbf { I n } ( a ) = \{ 2 , 1 , 0 \}$ . □

The following result is a consequence of Theorem 1 and permits the description of the inertia of a real polynomial in terms of that of two Bezoutians of smaller size

Theorem 2. If $a ( \lambda )$ is a real polynomial and $h ( \lambda )$ and $g ( \lambda )$ form the $L { - } C$ splitting of $\dot { \mathbf { \alpha } } a ( \lambda )$ , where the Bezoutians $B _ { 1 } = \mathrm { B e z } ( h ( \lambda ) , g ( \lambda ) )$ and $B _ { 2 } = \mathtt { B e z } ( h ( \lambda )$ $\lambda g ( \lambda ) )$ are nonsingular, then $a ( \lambda )$ has no pure imaginary zeros and

$$
\begin{array} { r } { \pi ( a ) = v ( B _ { 1 } ) + \pi ( B _ { 2 } ) , } \\ { \nu ( a ) = \pi ( B _ { 1 } ) + v ( B _ { 2 } ) . } \end{array}
$$

In particular, $\alpha ( \lambda )$ is stable if and only $i f B _ { 1 } > 0$ and $B _ { 2 } < 0 .$

ProoF. We give the proof for the case of l even, say $l = 2 k$

Let B denote the Bezout matrix associated with the polynomials $a _ { 1 } ( \lambda )$ and a2(λ) defined in Theorem 1. Applying Proposition 13.3.2 and Eq. $a _ { 2 } ( \lambda )$ (13.3.5), it is found that

$$
B = \sum _ { j = 1 } ^ { k } ( - 1 ) ^ { j - 1 } a _ { 2 j - 1 } \mathrm { d i a g } [ A _ { 2 j - 1 } ^ { ( 1 ) } , A _ { 2 j - 1 } ^ { ( 2 ) } ] ,\tag{4}
$$

where

$$
\begin{array} { r } { { \cal A } _ { 2 j - 1 } ^ { ( 1 ) } = \left[ \begin{array} { c c c c c } { 0 } & { \cdots } & { 0 } & { - a _ { 0 } } \\ & & { \cdots } & { - a _ { 0 } } & { 0 } \\ { \vdots } & { \cdots } & & & { a _ { 2 } } \\ & & { \cdots } & { \cdots } & { 0 } \\ & & & { \cdots } & { \vdots } \\ { 0 } & & & & { \cdots } & { \vdots } \\ { - a _ { 0 } } & { 0 } & { a _ { 2 } } & { 0 } & { \cdots } & { ( - 1 ) ^ { j } a _ { 2 j - 2 } } \end{array} \right] , } \end{array}
$$

$$
A _ { 2 j - 1 } ^ { ( 2 ) } = \left[ \begin{array} { c c c c } { { ( - 1 ) ^ { j + 1 } a _ { 2 j } } } & { { 0 } } & { { \cdots } } & { { ( - 1 ) ^ { k } a _ { l } } } \\ { { 0 } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \cdots } } & { { \vdots } } \\ { { ( - 1 ) ^ { k } a _ { l } } } & { { 0 } } & { { \cdots } } & { { 0 } } \end{array} \right] .
$$

Consider the matrix $\ Q = [ Q _ { 1 } \quad Q _ { 2 } ]$ defined by Eq. (13.4.3). For $j =$ $1 , 2 , \ldots , k .$ we have

$$
Q ^ { T } \mathrm { d i a g } [ A _ { 2 j - 1 } ^ { ( 1 ) } , A _ { 2 j - 1 } ^ { ( 2 ) } ] Q = \mathrm { d i a g } [ A _ { 2 j + 1 } ^ { [ 1 ] } , A _ { 2 j + 1 } ^ { [ 2 ] } , A _ { 2 j - 1 } ^ { [ 1 ] } , A _ { 2 j - 1 } ^ { [ 2 ] } ] ,\tag{5}
$$

where

$$
\begin{array} { r l } & { A _ { 2 s - 1 } ^ { [ 1 ] } = \left[ \begin{array} { l l l l } { 0 } & { \cdots } & { 0 } & { - a _ { 0 } } \\ { \vdots } & { \cdots } & { \cdot } & { a _ { 2 } } \\ { 0 } & { } & { \cdot } & { \cdot } & { \vdots } \\ { - a _ { 0 } } & { a _ { 2 } } & { \cdots } & { ( - 1 ) ^ { s - 1 } a _ { 2 s - 4 } } \end{array} \right] , } \\ & { A _ { 2 s - 1 } ^ { [ 2 ] } = \left[ \begin{array} { l l l l } { ( - 1 ) ^ { s } a _ { 2 s } } & { \cdots } & { ( - 1 ) ^ { k } a _ { 1 } } \\ { \vdots } & { \cdots } & { \cdot } & { 0 } \\ { \vdots } & { \cdot } & { \cdot } & { \vdots } \\ { ( - 1 ) ^ { k } a _ { l } } & { 0 } & { \cdots } & { \dot { 0 } } \end{array} \right] . } \end{array}
$$

Thus, by use of Eq. (5), it follows from Eq. (4) that

$$
Q ^ { \mathrm { T } } B Q = \mathrm { d i a g } [ \tilde { B } _ { 2 } , \tilde { B } _ { 1 } ] ,\tag{6}
$$

where, appealing to Eq. (13.3.5) and writing C for the companion matrix of $g ( - \lambda )$

$$
\begin{array} { r l } & { \widetilde { B } _ { 1 } = \displaystyle \sum _ { j = 1 } ^ { k } ( - 1 ) ^ { j - 1 } a _ { 2 - 1 } \le \mathrm { i d } \mathrm { i d } [ A _ { 2 \rho - 1 } ^ { ( 1 ) } , A _ { 2 \rho - 1 } ^ { ( 2 ) } ] } \\ & { \quad = \displaystyle \left[ \begin{array} { l l l } { - a _ { 2 } } & { a _ { 4 } } & { \cdots } & { ( - 1 ) ^ { j } a _ { 1 } } \\ { a _ { 4 } } & { \cdots } & { \cdots } & { 0 } \\ { \vdots } & { \ddots } & { \ddots } & { \vdots } \\ { ( - 1 ) ^ { k } a _ { 4 } } & { 0 } & { \cdots } & { 0 } \end{array} \right] ( a _ { 1 } I - a _ { s } C + \cdots + ( - 1 ) ^ { k - 1 } a _ { 1 - 1 } C ^ { ( - 1 ) } ) } \\ & { \quad \widetilde { B } _ { 2 } = \displaystyle \sum _ { j = 1 } ^ { k } ( - 1 ) ^ { j - 1 } a _ { 2 - 1 } \ \mathrm { i d } \mathrm { i d } [ A _ { 2 \rho - 1 } ^ { ( 1 ) } , A _ { 2 \rho + 1 } ^ { ( 1 ) } ] } \\ & { \quad = \displaystyle \left[ \begin{array} { l l l } { - a _ { 2 } } & { a _ { 4 } } & { \cdots } & { ( - 1 ) ^ { j } a _ { 1 } } \\ { \vdots } & { \ddots } & { \ddots } \\ { ( - 1 ) ^ { k } a _ { 4 } } & { 0 } & { \cdots } & { 0 } \end{array} \right] ( a _ { 1 } C - a _ { 3 } C ^ { 2 } + \cdots + ( - 1 ) ^ { k - 1 } a _ { i - 1 } C ^ { ( - 1 ) } ) . } \end{array}
$$

Now use Proposition 13.3.2 again to obtain

$$
\widetilde { B } _ { 1 } = B ( h ( - \lambda ) , g ( - \lambda ) ) , \qquad \widetilde { B } _ { 2 } = B ( h ( - \lambda ) , \lambda g ( - \lambda ) ) .
$$

Using Eq. (13.3.7), we easily check that

$$
{ \cal P } \tilde { B } _ { 1 } { \cal P } = - B _ { 1 } , \quad { \cal P } \tilde { B } _ { 2 } { \cal P } = - B ( h ( \lambda ) , - \lambda g ( \lambda ) ) = B _ { 2 } ,\tag{7}
$$

where $P = \mathrm { d i a g } [ 1 , \ - 1 , \ldots , ( - 1 ) ^ { k - 1 } ] \in \mathbb { C } ^ { k }$ Now Sylvester's law of inertia applied to Eqs. (6) and (7) yields, in view of Theorem 1, the required result provided l is even. The case of l odd is similarly established.

Example 2. Let $a ( \lambda )$ be the polynomial considered in Example 1. We have $h ( \lambda ) = 2 , g ( \lambda ) = - 3 + \lambda .$ and

$$
B _ { 1 } = - 2 , \qquad B _ { 2 } = \biggl [ - 2 \qquad 0 \biggr ] .
$$

Thus In $\boldsymbol { B } _ { 1 } = \left\{ 0 , 1 , 0 \right\}$ , In $B _ { 2 } = \{ 1 , 1 , 0 \}$ , and $a ( \lambda )$ has two zeros in the open right half-plane and one zero in the open left half-plane, as required.

Example 3. Let $a ( \lambda ) = ( \lambda - 1 ) ^ { 3 } ( \lambda + 2 )$ .Then $h ( \lambda ) = - 2 - 3 \lambda + \lambda ^ { 2 } , g ( \lambda ) =$ $5 - \lambda ,$ and

$$
B _ { 1 } = { \left[ \begin{array} { l l } { - 1 7 } & { 5 } \\ { 5 } & { - 1 } \end{array} \right] } , \qquad B _ { 2 } = { \left[ \begin{array} { l l } { 1 0 } & { - 2 } \\ { - 2 } & { 2 } \end{array} \right] } .
$$

Since In $B _ { 1 } = \{ 1 , 1 , 0 \}$ , In $B _ { 2 } = \{ 2 , 0 , 0 \}$ , then, by Eq. (3), $\operatorname { I n } ( a ) = \{ 3 , 1 , 0 \}$ as required. □

A simplified version of the criteria of Theorem 2 will be presented in Section 13.10.

## 13.8 The Markov Criterion

Let $a ( \lambda ) = a _ { 0 } + a _ { 1 } \lambda + \cdots + a _ { l } \lambda ^ { l }$ be a polynomial with real coefficients and $a _ { l } \neq 0 ,$ , and let $a _ { 1 } ( \lambda ) , a _ { 2 } ( \lambda )$ be defined as in Theorem 13.7.1. Note that generally deg $a _ { 2 } ( \lambda ) \leq \deg a _ { 1 } ( \lambda )$ . Hence we may define a rational function $r ( \lambda ) = a _ { 2 } ( \lambda ) / a _ { 1 } ( \lambda )$ with the property $\begin{array} { r } { \operatorname* { l i m } _ { \lambda  \infty } \{ r ( \lambda ) \} < \infty } \end{array}$

For sufficiently large |λ, we may represent r(λ) by a Laurent series,

$$
r ( \lambda ) = \sum _ { j = 0 } ^ { \infty } h _ { j } \lambda ^ { - j } ,
$$

and construct the corresponding (truncated) Hankel matrix H of the Markov parameters $h _ { j } \colon H = [ h _ { i + j - 1 } ] _ { i , j = 1 } ^ { l }$ . It turns out that the results obtained in Sections 13.3 and 13.4 can be reformulated in terms of the inertia of a Hankel matrix of Markov parameters. This is possible in view of the relationship between Hankel and Bezout matrices that is established in the next proposition.

Proposition 1. Let $\begin{array} { r } { b ( \lambda ) = \sum _ { j = 0 } ^ { l } b _ { j } \lambda ^ { j } } \end{array}$ and $\begin{array} { r } { c ( \lambda ) = \sum _ { j = 0 } ^ { l } c _ { j } \lambda ^ { j } } \end{array}$ be two real polynomials in which $c _ { \iota } \neq 0$ If $B = \mathbf { B e z } ( c , b )$ denotes the Bezout matrix associated with $c ( \lambda )$ and b(λ), then

$$
B = S ( c ) H S ( c ) ,\tag{1}
$$

where H denotes the Hankel matrix of Markov parameters of the rational function $R ( \lambda ) = b ( \lambda ) / c ( \lambda )$

PROOF. Let $H = [ h _ { i + j - 1 } ] _ { i , j = 1 } ^ { l }$ , where $h _ { 1 } , h _ { 2 } , \ldots , h _ { 2 l - 1 }$ are defined by

$$
b ( \lambda ) = ( h _ { 0 } + h _ { 1 } \lambda ^ { - 1 } + h _ { 2 } \lambda ^ { - 2 } + \cdots ) c ( \lambda ) .\tag{2}
$$

It is easily found, by comparing the corresponding coefficients on both sides of Eq. (2), that

$$
\begin{array} { r } { \pmb { b } ^ { \operatorname { \cal T } } = \pmb { h } _ { 1 } ^ { \operatorname { \cal T } } S ( c ) , } \end{array}\tag{3}
$$

where $\pmb { b } ^ { \mathrm { r } } = [ \tilde { b } _ { \pmb { 0 } } \quad \tilde { b } _ { 1 } \quad \cdots \quad \tilde { b } _ { l - 1 } ] , \tilde { b } _ { j } = b _ { j } - b _ { l } c _ { j } c _ { l } ^ { - 1 } , j = 0 , 1 , \ldots , l - 1 ,$ , and $\pmb { h } _ { 1 } ^ { \operatorname { T } } = [ h _ { 1 } \quad h _ { 2 } \quad \cdots \quad h _ { l } ] .$

Furthermore, using Eq. (13.3.5), it is found that

$$
\boldsymbol { b } ^ { \boldsymbol { \mathsf { T } } } C _ { c } ^ { j } = \boldsymbol { h } _ { 1 } ^ { \boldsymbol { \mathsf { T } } } \operatorname { d i a g } \left[ - \left[ \begin{array} { c c c c } & & { c _ { 0 } } \\ & & { c _ { 1 } } \\ & & { \ddots } \\ { c _ { 0 } } & { c _ { 1 } } & { \cdots } & { c _ { j - 1 } } \end{array} \right] , \left[ \begin{array} { l l l } { c _ { j + 1 } } & { \cdots } & { c _ { l } } \\ { \vdots } & { \ddots } & \\ { c _ { l } } & & \end{array} \right] \right] = \boldsymbol { h } _ { j + 1 } ^ { \boldsymbol { \mathsf { T } } } S ( c ) ,
$$

where $\pmb { h } _ { j + 1 } ^ { \mathsf { T } } = [ h _ { j + 1 } \quad h _ { j + 2 } \quad \cdots \quad h _ { j + l } ]$ and $j = 1 , 2 , \dots , l - 1$ . Combining this with Eq. (3) we obtain

$$
\begin{array} { r } { \left[ \begin{array} { l } { b ^ { \operatorname { T } } } \\ { b ^ { \operatorname { T } } C _ { c } } \\ { \vdots } \\ { b ^ { \operatorname { T } } C _ { c } ^ { l - 1 } } \end{array} \right] = H S ( c ) . } \end{array}
$$

It remains only to use Eq. (13.3.20) to obtain Eq. (1).

Now we are in a position to state a modified Markov stability test.

Theorem 1. Let H be the Hankel matrix of the Markov parameters of the polynomial a(λ) and assume that det $H \neq 0 .$ Then

$$
\pi ( a ) = \pi ( H ) , \qquad \nu ( a ) = \nu ( H ) , \qquad \delta ( a ) = 0 .\tag{5}
$$

ProoF. The assertion of the theorem trivially follows from Theorem 13.7.1, Proposition 1, and Sylvester's law of inertia.

Corollary 1. A real polynomial a(λ) is stable if and only if $H < 0 .$

Example 1. Let $a ( \lambda ) = ( \lambda + 1 ) ^ { 2 } ( \lambda + 2 )$ . Then

$$
r ( \lambda ) = \frac { a _ { 2 } ( \lambda ) } { a _ { 1 } ( \lambda ) } = \frac { - 2 + 4 \lambda ^ { 2 } } { \lambda ( 5 - \lambda ^ { 2 } ) } = \sum _ { j = 1 } ^ { \infty } h _ { j } \lambda ^ { - j } ,
$$

where the coefficients $h _ { 1 } , h _ { 2 } , \ldots , h _ { 5 }$ are found to be $h _ { 1 } = - 4 , h _ { 2 } = h _ { 4 }$ $= 0 , h _ { 3 } = - 1 8 , h _ { 5 } = - 9 0$ Hence the Hankel matrix

$$
H = \left[ { \begin{array} { r r r } { - 4 } & { 0 } & { - 1 8 } \\ { 0 } & { - 1 8 } & { 0 } \\ { - 1 8 } & { 0 } & { - 9 0 } \end{array} } \right]
$$

is negative definite (use Jacobi's method to see this), and therefore $a ( \lambda )$ is stable. □

Applying Eq. (1) and Sylvester's law of inertia to the Bezout matrices $B _ { 1 }$ and $B _ { 2 }$ , the next result follows from Theorem 13.7.2.

Theorem 2 (A. A. Markov†). In the notation of this section, let

$$
H _ { 1 } = \left[ \begin{array} { l l l l } { h _ { 1 } } & { h _ { 2 } } & { \cdots } & { h _ { k } } \\ { h _ { 2 } } & { } & { \cdot } & { \vdots } \\ { \vdots } & { } & { \cdot } & { \vdots } \\ { h _ { k } } & { } & { \cdots } & { h _ { 2 k - 1 } } \end{array} \right] , \qquad H _ { 2 } = \left[ \begin{array} { l l l l } { h _ { 2 } } & { h _ { 3 } } & { \cdots } & { h _ { m + 1 } } \\ { h _ { 3 } } & { } & { } & { \vdots } \\ { \vdots } & { } & { \cdot } & { \vdots } \\ { h _ { m + 1 } } & { } & { \cdots } & { h _ { 2 m } } \end{array} \right] ,\tag{6}
$$

where $\begin{array} { r } { k = m = { \frac { 1 } { 2 } } l o r k = { \frac { 1 } { 2 } } ( l + 1 ) , m = { \frac { 1 } { 2 } } ( l - 1 ) } \end{array}$ , according as l is even or odd, and where the Markov parameters $h _ { i } , j = 0 , 1 , \ldots ,$ are dened by

$$
\sum _ { j = 0 } ^ { \infty } h _ { j } \lambda ^ { - j } = \left\{ \begin{array} { l l } { { g ( \lambda ) / h ( \lambda ) } } & { { \quad i f \quad l \ i s \ e v e n , } } \\ { { h ( \lambda ) / \lambda g ( \lambda ) } } & { { \quad i f \quad l \ i s \ o d d . } } \end{array} \right.\tag{7}
$$

${ \cal I } f { \cal H } _ { 1 }$ and $H _ { 2 }$ are nonsingular, then $a ( \lambda )$ has no pure imaginary zeros and

$$
\begin{array} { r } { \pi ( a ) = \nu ( H _ { 1 } ) + \pi ( H _ { 2 } ) , } \\ { \nu ( a ) = \pi ( H _ { 1 } ) + \nu ( H _ { 2 } ) . } \end{array}\tag{8}
$$

PRoOF. Let l be even. Then deg $g ( \lambda ) < \deg h ( \lambda )$ and hence, in Eq. (7), $h _ { 0 } = 0$ . Note that since the leading coefficient of $h ( \lambda )$ is nonzero, formula (1) yields the congruence of $\boldsymbol { B } _ { 1 } = B ( h ( \boldsymbol { \lambda } ) , g ( \boldsymbol { \lambda } ) )$ and $H _ { 1 }$ . Furthermore, it follows that

$$
\frac { \lambda g ( \lambda ) } { h ( \lambda ) } = \sum _ { j = 0 } ^ { \infty } h _ { j + 1 } \lambda ^ { - j }
$$

for sufficiently large $| \lambda |$ . Therefore by Eq. (1) the matrices $B _ { 2 } = B ( h ( \lambda ) , \lambda g ( \lambda ) )$ and $H _ { 2 }$ are congruent. This proves the theorem in the even case.

Now consider the case when l is odd. Here deg $h ( \lambda ) \leq \deg g ( \lambda )$ and

$$
\frac { h ( \lambda ) } { g ( \lambda ) } = \sum _ { j = 0 } ^ { \infty } h _ { j + 1 } \lambda ^ { - j } , \qquad \frac { h ( \lambda ) } { \lambda g ( \lambda ) } = \sum _ { j = 1 } ^ { \infty } h _ { j } \lambda ^ { - j } .
$$

Thus $H _ { 1 }$ (respectively, $H _ { 2 } )$ is congruent to the Bezoutian $- B _ { 2 } = B ( \lambda g ( \lambda ) , h ( \lambda ) )$ (respectively, $- B _ { 1 } = B ( g ( \lambda ) , h ( \lambda ) ) )$ , and Eqs. (8) follow from Theorem 13.7.2.

Corollary 1. A real polynomial $a ( \lambda )$ is stable if and only if $H _ { 1 } > 0$ and $H _ { 2 } < 0 ,$ where $H _ { 1 }$ and $H _ { 2 }$ are defined in Eqs. (6).

Note that by writing the Markov parameters in the traditional form (l is even),

$$
\frac { g ( \lambda ) } { h ( \lambda ) } = r _ { - 1 } + \frac { r _ { 0 } } { \lambda } - \frac { r _ { 1 } } { \lambda ^ { 2 } } + \frac { r _ { 2 } } { \lambda ^ { 3 } } - \frac { r _ { 3 } } { \lambda ^ { 4 } } + \cdots ,\tag{9}
$$

it is found that

$$
H _ { 1 } = P \tilde { H } _ { 1 } P , H _ { 2 } = - P \tilde { H } _ { 2 } P ,
$$

where $P = \operatorname { d i a g } [ 1 , - 1 , . . . , ( - 1 ) ^ { m - 1 } ]$ and $\begin{array} { r } { m = \frac { 1 } { 2 } l , } \end{array}$ and

$$
\tilde { H } _ { 1 } = \left[ \begin{array} { c c c c } { r _ { 0 } } & { r _ { 1 } } & { \cdots } & { r _ { m - 1 } } \\ { r _ { 1 } } & { \hphantom { - } } & { \hphantom { - } } & { \vdots } \\ { \vdots } & { \hphantom { - } } & { \hphantom { - } } & { \vdots } \\ { r _ { m - 1 } } & { \hphantom { - } } & { r _ { 2 m - 2 } } \end{array} \right] , \qquad \tilde { H } _ { 2 } = \left[ \begin{array} { c c c c } { r _ { 1 } } & { r _ { 2 } } & { \cdots } & { r _ { m } } \\ { r _ { 2 } } & { \hphantom { - } } & { \hphantom { - } } & { \vdots } \\ { \vdots } & { \hphantom { - } } & { \hphantom { - } } & { \vdots } \\ { r _ { m } } & { \hphantom { - } } & { \hphantom { - } } & { r _ { 2 m - 1 } } \end{array} \right]
$$

Thus, the stability criterion with respect to the form (9) is equivalent to the conditions $\tilde { H } _ { 1 } > 0 , \tilde { H } _ { 2 } > 0$ , as required.

Example 2. Let $a ( \lambda )$ be as defined in Example 1. Then $h ( \lambda ) = 2 + 4 \lambda$ $g ( \lambda ) = 5 + \lambda$ , and

$$
{ \frac { h ( \lambda ) } { \lambda g ( \lambda ) } } = 4 \lambda ^ { - 1 } - 1 8 \lambda ^ { - 2 } + 9 0 \lambda ^ { - 3 } + \cdots .
$$

Hence

$$
H _ { 1 } = { \binom { h _ { 1 } } { h _ { 2 } } } = { \binom { 4 } { - 1 8 } } = 9 0 \mathbf { \cdot } H _ { 2 } = [ h _ { 2 } ] = [ - 1 8 ] ,
$$

and the properties $H _ { 1 } > 0 , H _ { 2 } < 0$ yield the stability of the given polynomial.

## 13.9 A Determinantal Version of the Routh-Hurwitz Theorem

A disadvantage of the previous methods for computing the inertia of a given polynomial is that this inertia is expressed in terms of the inertia of a matrix with elements that must first be calculated. In this section we determine the inertia of a real polynomial by computing the leading principal minors of a matrix whose non-zero elements are simply the coefficients of the polynomial.

Let $\begin{array} { r } { a ( \lambda ) = \sum _ { j = 0 } ^ { l } a _ { j } \lambda ^ { j } } \end{array}$ be a polynomial with real coefficients and $a _ { l } \neq 0 ,$ and define the $1 \times 1$ matrix

$$
\begin{array} { r } { \hat { H } = \left[ \begin{array} { c c c c c } { a _ { \iota - 1 } } & { a _ { \iota - 3 } } & { \cdots } & & \\ { a _ { \iota } } & { a _ { \iota - 2 } } & { \cdots } & & \\ { 0 } & { a _ { \iota - 1 } } & { a _ { \iota - 3 } } & { \cdots } \\ { 0 } & { a _ { \iota } } & { a _ { \iota - 2 } } & { \cdots } \\ { 0 } & { 0 } & { a _ { \iota - 1 } } & { \cdots } \\ { 0 } & { 0 } & { a _ { \iota } } & { \cdots } \\ { \vdots } & { \vdots } & { \vdots } & & \end{array} \right] , } \end{array}\tag{1}
$$

called the Hurwitz matrix associated with $a ( \lambda )$ . We shall show that the Hermitian matrix H from Section 13.8 and the non-Hermitian Hurwitz matrix $\hat { H }$ have the same leading principal minors. We state a more general result due to A. Hurwitz.†

Proposition 1. Let $\begin{array} { r } { b ( \lambda ) = \sum _ { j = 0 } ^ { l } b _ { j } \lambda ^ { j } } \end{array}$ and $\begin{array} { r } { c ( \lambda ) = \sum _ { j = 0 } ^ { l } c _ { j } \lambda ^ { j } } \end{array}$ be two real polynomials with $c _ { \iota } \neq 0 ,$ and let $h _ { 0 } , h _ { 1 } , h _ { 2 } , . . .$ . denote the Markov parameters of the rational function $r ( \lambda ) = b ( \lambda ) / c ( \lambda )$ . Then if we define $b _ { j } = c _ { j } = 0$ for $j < 0 ,$

$$
c _ { l } ^ { 2 s } \operatorname* { d e t } { \left[ \begin{array} { l l l l } { h _ { 1 } } & { h _ { 2 } } & { \cdots } & { h _ { s } } \\ { h _ { 2 } } & { \cdots } & { h _ { s + 1 } } \\ { \vdots } & { \ddots } & { \ddots } & { \vdots } \\ { h _ { s } } & { h _ { s + 1 } } & { \cdots } & { h _ { 2 s - 1 } } \end{array} \right] } = \operatorname* { d e t } { \left[ \begin{array} { l l l l l } { c _ { l } } & { c _ { l - 1 } } & { \cdots } & { c _ { l - 2 s + 1 } } \\ { b _ { l } } & { b _ { l - 1 } } & { \cdots } & { b _ { l - 2 s + 1 } } \\ { 0 } & { c _ { l } } & { c _ { l - 1 } } & { \cdots } & { c _ { l - 2 s + 2 } } \\ { 0 } & { b _ { l } } & { b _ { l - 1 } } & { \cdots } & { b _ { l - 2 s + 2 } } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 0 } & { \cdots } & { c _ { l } } & { \cdots } & { c _ { l - { s } } } \\ { 0 } & { \cdots } & { b _ { l } } & { \cdots } & { b _ { l - { s } } } \end{array} \right] } ,
$$

for $s = 1 , 2 , \ldots , l .$

(2)

PROOF. Introduce the $1 \times 2 s$ vectors

$$
\pmb { h } _ { k } ^ { \operatorname { T } } = [ 0 \quad \cdots \quad 0 \quad h _ { 0 } \quad h _ { 1 } \quad \cdots \quad h _ { k } ]
$$

and

$$
\pmb { b } _ { k } ^ { \sf T } = [ 0 \mathrm { ~  ~ \cdots ~ } 0 _ { . } b _ { l } b _ { l - 1 } \mathrm { ~  ~ \cdots ~ } b _ { l - k } ] ,
$$

for $k = 0 , 1 , \ldots , 2 s - 1$ . Note that

$$
\pmb { h } _ { 2 s - 1 } ^ { \operatorname { T } } = [ h _ { 0 } \quad h _ { 1 } \quad \cdots \quad h _ { 2 s - 1 } ]
$$

and

$$
\pmb { b } _ { 2 s - 1 } ^ { \sf T } = [ \pmb { b } _ { l } \quad \pmb { b } _ { l - 1 } \quad \cdots \quad \pmb { b } _ { l - 2 s + 1 } ] .
$$

Using Eq. (13.8.3), it is found that, for each $k ,$

$$
\begin{array} { r } { h _ { k } ^ { \operatorname { T } } \left[ \begin{array} { c c c c c } { c _ { l } } & { c _ { l - 1 } } & { \cdots } & { c _ { l - 2 s + 1 } } \\ { 0 } & { c _ { l } } & { \ddots } \\ { \vdots } & { \ddots } & { \ddots } & { c _ { l - 1 } } \\ { 0 } & { } & { 0 } & { c _ { l } } \end{array} \right] = \pmb { b } _ { k } ^ { \operatorname { T } } . } \end{array}\tag{3}
$$

Hence, denoting the unit vectors in $\mathbb { C } ^ { 2 s }$ by ${ \pmb u } _ { 1 } , { \pmb u } _ { 2 } , \dots , { \pmb u } _ { 2 s }$ , we easily check that

$$
\left[ \begin{array} { l } { u _ { 1 } ^ { \mathsf { T } } } \\ { h _ { 2 s - 1 } ^ { \mathsf { T } } } \\ { u _ { 2 } ^ { \mathsf { T } } } \\ { h _ { 2 s - 2 } ^ { \mathsf { T } } } \\ { \vdots } \\ { u _ { s } ^ { \mathsf { T } } } \\ { u _ { s } ^ { \mathsf { T } } } \\ { h _ { s } ^ { \mathsf { T } } } \end{array} \right] \left[ \begin{array} { l l l l l } { c _ { l } } & { c _ { l - 1 } } & { \cdots } & { c _ { l - 2 s + 1 } } \\ { 0 } & & & \\ { \vdots } & & & { \ddots } \\ { \vdots } & & { \ddots } & { \ddots } & { \vdots } \\ & & & { \hphantom { \ddots } } c _ { l - 1 }  \\ { 0 } & & & { 0 } & { c _ { l } } \end{array} \right] = \left[ \begin{array} { l } { c _ { 2 s - 1 } ^ { \mathsf { T } } } \\ { b _ { 2 s - 1 } ^ { \mathsf { T } } } \\ { c _ { 2 s - 2 } ^ { \mathsf { T } } } \\ { b _ { 2 s - 2 } ^ { \mathsf { T } } } \\ { \vdots } \\ { c _ { s } ^ { \mathsf { T } } } \\ { b _ { s } ^ { \mathsf { T } } } \end{array} \right] ,\tag{4}
$$

where

$$
\begin{array} { l l l l l l } { { c _ { k } ^ { \bf T } = [ 0 } } & { { \cdots \mathrm { } } } & { { 0 } } & { { c _ { l } } } & { { c _ { l - 1 } } } & { { \cdots } } & { { c _ { l - k } ] , } } & { { } } & { { k = 0 , 1 , \ldots , 2 s - 1 , } } \end{array}
$$

and $c _ { j } = b _ { j } = 0$ for $j > l .$ Observe that the Toeplitz matrix in Eq. (4) coincides with the matrix in Eq. (3), and therefore their determinants are equal. Computing the determinant on the left side in Eq. (4), we find that it is equal to

$$
( - 1 ) ^ { s } c _ { l } ^ { 2 s } \operatorname* { d e t } \left[ \begin{array} { c } { u _ { 1 } ^ { \mathsf { T } } } \\ { u _ { 2 } ^ { \mathsf { T } } } \\ { \vdots } \\ { u _ { s } ^ { \mathsf { T } } } \\ { h _ { 2 s - 2 } ^ { \mathsf { T } } } \\ { h _ { 2 s - 2 } ^ { \mathsf { T } } } \\ { \vdots } \\ { h _ { s } ^ { \mathsf { T } } } \end{array} \right] = c _ { l } ^ { 2 s } \operatorname* { d e t } \left[ \begin{array} { c c } { I } & { 0 } \\ { V _ { s } } & { W _ { s } } \end{array} \right] ,
$$

where

$$
V _ { s } = { \left[ \begin{array} { l l l l } { h _ { 0 } } & { h _ { 1 } } & { \cdots } & { h _ { s - 1 } } \\ { 0 } & { h _ { 0 } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { h _ { 1 } } \\ { 0 } & { \cdots } & { 0 } & { h _ { 0 } } \end{array} \right] } , \qquad W _ { s } = { \left[ \begin{array} { l l l l } { h _ { s } } & { h _ { s + 1 } } & { \cdots } & { h _ { 2 s - 1 } } \\ { h _ { s - 1 } } & { h _ { s } } & { \cdots } & { h _ { 2 s - 2 } } \\ { \vdots } & { \ddots } & { \ddots } & { \vdots } \\ { h _ { 1 } } & { \cdots } & { h _ { s - 1 } } & { h _ { s } } \end{array} \right] } .
$$

Thus the determinant of the matrix on the right in Eq. (2) is

$$
( - 1 ) ^ { s } c _ { l } ^ { 2 s } \operatorname* { d e t } W _ { s } = c _ { l } ^ { 2 s } \operatorname* { d e t } \left[ h _ { 1 } \quad h _ { 2 } \quad \cdots \quad h _ { s } \quad \right] ,
$$

as required.■

The famous Routh-Hurwitz stability result is presented in the following theorem.

Theorem 1. $I f a ( \lambda )$ is a real polynomial and there are no zeros in the sequence

$$
\Delta _ { 1 } , \Delta _ { 2 } , \ldots , \Delta _ { l } ,\tag{5}
$$

of leading principal minors of the corresponding Hurwitz matrix, then $a ( \lambda )$ has no pure imaginary zeros and

$$
\pi ( a ) = V { \left( a _ { l } , \Delta _ { 1 } , \frac { \Delta _ { 2 } } { \Delta _ { 1 } } , \ldots , \frac { \Delta _ { l } } { \Delta _ { l - 1 } } \right) } ,
$$

$$
\nu ( a ) = l - V { \left( a _ { l } , \Delta _ { 1 } , \frac { \Delta _ { 2 } } { \Delta _ { 1 } } , \cdot \cdot \cdot , \frac { \Delta _ { l } } { \Delta _ { l - 1 } } \right) } = P { \left( a _ { l } , \Delta _ { 1 } , \frac { \Delta _ { 2 } } { \Delta _ { 1 } } , \cdot \cdot \cdot , \frac { \Delta _ { l } } { \Delta _ { l - 1 } } \right) } ,\tag{6}
$$

where V (respectively, P) denotes the number of alterations (respectively, constancies) of sign in the appropriate sequence.

ProoF. Consider the case of l even, say $l = 2 k$ For $s = 1 , 2 , \ldots , k ,$ denote by $\delta _ { s } ^ { ( 1 ) }$ (respectively, $\delta _ { s } ^ { ( 2 ) } )$ the leading principal minor of order s of the matrix $H _ { 1 }$ (respectively $H _ { 2 } )$ defined in Eqs. (13.8.6). For $s = 1 , 2 , \ldots , l ,$ let $\Delta _ { s }$ stand for the leading principal minor of order s of the Hurwitz matrix H. Applying Eq. (2) for the polynomials $b ( \lambda ) = \lambda g ( \lambda ) , c ( \lambda ) = h ( \lambda )$ , where $h ( \lambda )$ and $g ( \lambda )$ generate the $L { - } C$ splitting of $a ( \lambda )$ , it is found that, after s interchanges of rows in the matrix on the right in Eq. (2),

$$
a _ { l } ^ { 2 s } \delta _ { s } ^ { ( 2 ) } = ( - 1 ) ^ { s } \Delta _ { 2 s } , \qquad s = 1 , 2 , \ldots , k .\tag{7}
$$

Now apply Eq. (2) for $b ( \lambda ) = g ( \lambda ) , c ( \lambda ) = h ( \lambda )$ to obtain, for $s = 1 , 2 , \ldots , k ,$

$$
a _ { i } ^ { 2 s } \delta _ { s } ^ { ( 1 ) } = \operatorname * { d e t } \left[ \begin{array} { c c c c } { a _ { i } } & { a _ { l - 2 } } & { \cdots } & \\ { 0 } & { a _ { { l - 1 } } } & { a _ { { l - 3 } } } & { \cdots } \\ { 0 } & { a _ { l } } & { a _ { { l - 2 } } } & { \cdots } \\ { 0 } & { 0 } & { a _ { { l - 1 } } } & { \cdots } \\ { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { a _ { 1 } } \end{array} \right] = a _ { l } \Delta _ { 2 s - 1 } .\tag{8}
$$

Using Theorem 13.8.2 and the Jacobi rule, if $\Delta _ { i } \neq 0$ for $i = 1 , 2 , \ldots , l ,$ we obtain

$$
\pi ( a ) = V ( 1 , \delta _ { 1 } ^ { ( 1 ) } , \ldots , \delta _ { l } ^ { ( 1 ) } ) + P ( 1 , \delta _ { 1 } ^ { ( 2 ) } , \ldots , \delta _ { l } ^ { ( 2 ) } ) ,\tag{9}
$$

where V (respectively, P) denotes the number of alterations (respectively, constancies) of sign in the appropriate sequence. In view of Eqs. (7) and (8), we find from Eq. (9) in the case of a positive $a _ { \mathrm { I } }$ that

$$
\begin{array} { r l } & { \pi ( a ) = V ( 1 , \Delta _ { 1 } , \Delta _ { 3 } , . . . , \Delta _ { l - 1 } ) + P ( 1 , - \Delta _ { 2 } , \Delta _ { 4 } , . . . , ( - 1 ) ^ { k } \Delta _ { l } ) } \\ & { \qquad = V ( 1 , \Delta _ { 1 } , \Delta _ { 3 } , . . . , \Delta _ { l - 1 } ) + V ( 1 , \Delta _ { 2 } , \Delta _ { 4 } , . . . , \Delta _ { l } ) , } \end{array}\tag{10}
$$

which is equivalent (in the case $a _ { i } > 0 )$ to the first equality in Eq. (6). The second equality in Eq. (6), as well as the proof of both of them for $a _ { i } < 0 ,$ is similar. It remains to mention that the case for l odd is established in a similar way.

Corollary 1. A real polynomial $a ( \lambda )$ of degree l with $a _ { \imath } > 0$ is stable if and only if

$$
\Delta _ { 1 } > 0 , \Delta _ { 2 } > 0 , \ldots , \Delta _ { l } > 0 .\tag{11}
$$

Example 1. $I f a ( \lambda ) = ( \lambda - 1 ) ^ { 3 } ( \lambda + 2 )$ (see Example 13.7.3), then

$$
\hat { H } = \left[ \begin{array} { c c c c } { - 1 } & { 5 } & { 0 } & { 0 } \\ { 1 } & { - 3 } & { - 2 } & { 0 } \\ { 0 } & { - 1 } & { 5 } & { 0 } \\ { 0 } & { 1 } & { - 3 } & { - 2 } \end{array} \right] ,
$$

with $\Delta _ { 1 } = \ : - 1 , \Delta _ { 2 } = \ : - 2 , \Delta _ { 3 } = \ : - 8 , \Delta _ { 4 } = 1 6$ Hence

$$
\pi ( a ) = V ( 1 , - 1 , 2 , 4 , - 2 ) = 3 , \qquad \nu ( a ) = 1 ,
$$

as required.□

Note that the Gundelfinger-Frobenius method of Section 8.6 permits us to generalize the Routh-Hurwitz theorem in the form (10) or in the form

$$
\pi ( a ) = V ( a _ { l } , \Delta _ { 1 } , \Delta _ { 3 } , . . . , \Delta _ { l } ) + V ( 1 , \Delta _ { 2 } , . . . , \Delta _ { l - 1 } ) ,\tag{12}
$$

according as l is even or odd. It can be seen from the proof of Theorem 1 that this extension holds whenever Theorem 13.8.2 and the Grundelfinger-Frobenius method apply. Theorem 13.8.2 requires the nonsingularity of $H _ { 1 }$ and $H _ { 2 }$ ; that is, $\delta _ { k } ^ { ( 1 ) } \neq 0$ and $\delta _ { m } ^ { ( 2 ) } \neq 0$ (or, equivalently, $\Delta _ { 2 k - 1 } \neq 0$ and $\Delta _ { 2 m } \neq 0 )$ , where k and m are as defined in that theorem.

Application of the Gundelfinger-Frobenius method to the sequences of leading principal minors of $H _ { 1 }$ and $H _ { 2 } , \delta _ { 1 } ^ { ( 1 ) } , \delta _ { 2 } ^ { ( 1 ) } , \ldots , \delta _ { k } ^ { ( 1 ) }$ and $\delta _ { 1 } ^ { ( 2 ) } , \delta _ { 2 } ^ { ( 2 ) } ,$ $\cdots , \delta _ { m } ^ { ( 2 ) }$ , requires no two consecutive zeros in these sequences and $\delta _ { k } ^ { ( 1 ) } \neq 0 ,$ $\delta _ { m } ^ { ( 2 ) } \neq 0$ . In terms of the $\Delta { \boldsymbol { \mathsf { s } } }$ this means that there must be no two consecutive zeros in the sequences $\Delta _ { 1 } , \Delta _ { 3 } , \ldots , \Delta _ { 2 k - 1 }$ and $\Delta _ { 2 } , \Delta _ { 4 } , \ldots , \Delta _ { 2 m }$ , and also $\Delta _ { l - 1 } \neq 0 , \Delta _ { l } \neq 0$

Example 2. For the polynomial $a ( \lambda )$ discussed in Example 13.7.1, it is found that

$$
{ \hat { H } } = { \left[ \begin{array} { l l l } { 0 } & { 2 } & { 0 } \\ { 1 } & { - 3 } & { 0 } \\ { 0 } & { 0 } & { 2 } \end{array} \right] } ,
$$

with $\Delta _ { 1 } = 0 , \Delta _ { 2 } = - 2 , \Delta _ { 3 } = - 4$ . Thus, in view of the Eq. (12),

$$
\pi ( a ) = V ( 1 , 0 , - 4 ) + V ( 1 , - 2 ) = 2 ,
$$

as required. □

## 13.10 The Cauchy Index and its Applications

The notion of the Cauchy index for a rational function clarifies some properties of the polynomials involved in the quotient and, as a result, plays an important role in stability problems.

Consider a real rational function $r ( \lambda ) = b ( \lambda ) / c ( \lambda )$ , where $b ( \lambda )$ and $c ( \lambda )$ are real polynomials. The difference between the number of points at which $r ( \lambda )$ suffers discontinuity from $- \infty \ t \ o \ + \infty$ as λ increases from a to b $( a , b \in \mathbb { R } , a < b )$ and the number of points at which $r ( \lambda )$ suffers discontinuity from + ∞ to — ∞ on the same interval is called the Cauchy index of $r ( \lambda )$ on $( a , b )$ and is written $I _ { a } ^ { b } b ( \lambda ) / c ( \lambda )$ . Note that a and b may be assigned the values a = - ∞ and/or $b = + \infty$

Exercise 1. Verify that if $r ( \lambda ) = \mu _ { 0 } / ( \lambda - \lambda _ { 0 } )$ , where $\mu _ { 0 }$ and $\lambda _ { 0 }$ are real, then

$$
I _ { - \infty } ^ { + \infty } = \mathrm { s g n } \mu _ { 0 } = \left\{ \begin{array} { r l } { { 1 } } & { { ~ \mathrm { i f } \mu _ { 0 } > 0 , } } \\ { { - 1 } } & { { ~ \mathrm { i f } \mu _ { 0 } < 0 , } } \\ { { 0 } } & { { ~ \mathrm { i f } \mu _ { 0 } = 0 . } } \end{array} \right.
$$

Exercise 2. Verify that if

$$
r ( \lambda ) = \sum _ { i = 1 } ^ { s } \frac { \mu _ { i } } { \lambda - \lambda _ { i } } + r _ { 1 } ( \lambda ) ,
$$

where $\mu _ { i } , \lambda _ { i }$ are real $( i = 1 , 2 , \ldots , s )$ and $r _ { 1 } ( \lambda )$ is a rational function without real poles, then $\begin{array} { r } { I _ { a } ^ { b } r ( \lambda ) = \sum _ { i } \mathrm { s g n } \mu _ { i } } \end{array}$ , where the summation is over all $\lambda _ { i }$ lying in (a, b).

Exercise 3. Check that

$$
I _ { a } ^ { b } \frac { b ( \lambda ) } { c ( \lambda ) } = \sum _ { a < \lambda _ { i } < b } \operatorname { s g n } \frac { b ( \lambda _ { i } ) } { c ^ { \prime } ( \lambda _ { i } ) } ,
$$

provided that all zeros $\lambda _ { i }$ of $c ( \lambda )$ are simple. □

Proposition 1. The Cauchy index $I _ { a } ^ { b } c ^ { \prime } ( \lambda ) / c ( \lambda )$ is equal to the number of distinct real zeros in (a, b) of the real polynomial c(λ).

PROOF. Let $c ( \lambda ) = c _ { 0 } ( \lambda - \lambda _ { 1 } ) ^ { \mu _ { 1 } } ( \lambda - \lambda _ { 2 } ) ^ { \mu _ { 2 } } \cdot \cdot \cdot ( \lambda - \lambda _ { k } ) ^ { \mu _ { k } }$ , where $\lambda _ { i } \neq \lambda _ { j }$ for $i \neq j , i , j = 1 , 2 , \ldots , k$ .Suppose that only the first p distinct zeros of $c ( \lambda )$ are real. If $p = 0 ,$ then $c ^ { \prime } ( \lambda ) / c ( \lambda )$ has no real poles and hence the Cauchy index is zero. If $1 \leq p \leq k ,$ then

$$
{ \frac { c ^ { \prime } ( \lambda ) } { c ( \lambda ) } } = \sum _ { i = 1 } ^ { k } { \frac { \mu _ { i } } { \lambda - \lambda _ { i } } } = \sum _ { i = 1 } ^ { p } { \frac { \mu _ { i } } { \lambda - \lambda _ { i } } } + r _ { 1 } ( \lambda ) ,
$$

where $r _ { 1 } ( \lambda )$ has no real poles. It remains now to apply the result of Exercise 2.

Our first theorem links the Cauchy index of polynomials $b ( \lambda )$ and $c ( \lambda )$ with the inertia properties of the corresponding Bezout matrix. First recall the notion of the signature of a Hermitian matrix as introduced in Section 5.5.

Theorem 1. Let b(λ) and c(λ) be two real polynomials such that

$$
\deg b ( \lambda ) \leq \deg c ( \lambda )
$$

and let $B = { \bf B e z } ( b , c )$ denote the corresponding Bezout matrix. Then

$$
I _ { - \infty } ^ { + \infty } \frac { b ( \lambda ) } { c ( \lambda ) } = \mathrm { s i g } B .\tag{1}
$$

Note that, in view of Eq. (13.8.1), the Bezout matrix B in $\operatorname { E q . } ( 1 )$ can be replaced by the Hankel matrix H of the Markov parameters of $b ( \lambda ) / c ( \lambda )$

ProoF. Let us establish Eq. (1) for the case when all the real zeros of the polynomial $c ( \lambda )$ are simple. Then we may write the rational function $\bar { r } ( \lambda ) = b ( \lambda ) / c ( \lambda )$ in the form

$$
r ( \lambda ) = \sum _ { i = 1 } ^ { s } \frac { \mu _ { i } } { \lambda - \lambda _ { i } } + r _ { 1 } ( \lambda ) ,\tag{2}
$$

where $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ are the distinct real zeros of the polynomial $c ( \lambda )$ and $r _ { 1 } ( \lambda )$ is a real polynomial without real poles. Since

$$
{ \frac { 1 } { \lambda - \lambda _ { i } } } = \sum _ { k = 0 } ^ { \infty } { \frac { \lambda _ { i } ^ { k } } { \lambda ^ { k + 1 } } }\tag{3}
$$

for sufficiently large λ, we may substitute from Eq. (3) into Eq. (2) and find

$$
r ( \lambda ) = \sum _ { k = 0 } ^ { \infty } \left( \sum _ { i = 1 } ^ { s } \mu _ { i } \lambda _ { i } ^ { k } \right) \Biggl / \lambda ^ { k + 1 } + r _ { 1 } ( \lambda ) .
$$

Therefore $\begin{array} { r } { h _ { k } = \sum _ { i = 1 } ^ { s } \mu _ { i } \lambda _ { i } ^ { k } } \end{array}$ are the Markov parameters of the function $r ( \lambda )$ for $k = 0 , 1 , \ldots .$

Now observe that in view of Eq. (13.8.1) and Exercise 2, Eq. (1) will be proved for the case being considered if we establish that

$$
\begin{array} { r } { \operatorname { s i g } \left[ \begin{array} { c c c } { h _ { 0 } } & { h _ { 1 } } & { \cdots } & { h _ { n - 1 } } \\ { h _ { 1 } } & { } & { } \\ { \vdots } & { \cdots } & { } & { \vdots } \\ { h _ { n - 1 } } & { } & { \cdots } & { h _ { 2 n - 1 } } \end{array} \right] = \displaystyle \sum _ { i = 1 } ^ { s } \operatorname { s g n } \mu _ { i } , } \end{array}\tag{4}
$$

in which $n = \deg \cdot c ( \lambda )$ and $\begin{array} { r } { h _ { k } = \sum _ { i = 1 } ^ { n } \mu _ { i } \lambda _ { i } ^ { k } , k = 0 , 1 , . . . } \end{array}$ .But if $H _ { n } =$ $[ h _ { i + j } ] _ { i , j = 0 } ^ { n - 1 }$ , a simple verification shows that

$$
H _ { n } = V _ { n } \mathrm { d i a g } [ \mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { s } , 0 , \ldots , 0 ] V _ { n } ^ { \mathrm { T } } ,\tag{5}
$$

where $V _ { n }$ stands for the $n \times n$ Vandermonde matrix associated with $\lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { s } , x _ { 1 } , x _ { 2 } , . . . , x _ { n - s }$ for some distinct real numbers $x _ { 1 } , x _ { 2 } , \ldots , x _ { n - s }$ different from $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ . Using Sylvester's law of inertia and the nonsingularity of the Vandermonde matrix Vn, the relation (4) readily follows. $V _ { n } ,$

In the general case of multiple real zeros of c(λ), the reasoning becomes $c ( \lambda )$ more complicated because the decomposition of a rational function into elementary fractions contains sums of expressions of the form $( \lambda - \lambda _ { i } ) ^ { m }$ for $m = - 1 , - 2 , \ldots , - l _ { i } .$ where $l _ { i }$ is the multiplicity of $\lambda _ { i }$ as a zero of $c ( \lambda )$ Differentiating Eq. (3), the Markov parameters can be evaluated. The details are left as an exercise.

The result of Theorem 1 has several applications. We will start with some simplifications of the Liénard-Chipart and Markov stability criteria, but we first present an interesting preliminary result.

Proposition 2. If the real polynomial $a ( \lambda ) = a _ { 0 } + a _ { 1 } \lambda + \cdot \cdot \cdot + a _ { l } \lambda ^ { l }$ with $a _ { l } > 0$ is stable, then

$$
a _ { 0 } > 0 , a _ { 1 } > 0 , \ldots , a _ { l - 1 } > 0 , a _ { l } > 0 .\tag{6}
$$

ProOF. Any real polynomial $a ( \lambda )$ of degree l can be represented

$$
a ( \lambda ) = a _ { l } \prod _ { i = 1 } ^ { s } { ( \lambda + \lambda _ { i } ) \prod _ { j = 1 } ^ { k } { ( \lambda ^ { 2 } + \mu _ { j } \lambda + \nu _ { j } ) } } ,\tag{7}
$$

where $s + 2 k = n$ and the numbers $\lambda _ { i } , \mu _ { j } , \nu _ { j }$ are all real. Obviously, the condition that $a ( \lambda )$ has only zeros with negative real parts implies that $\lambda _ { i } > 0 ,$ $i = 1 , \ 2 , \ldots , \ s ,$ and also that the quadratic polynomials $\lambda ^ { 2 } + \mu _ { j } \lambda + \nu _ { j } ,$ $j = 1 , 2 , \dots , k$ have zeros in the open left half-plane. The last requirement yields $\mu _ { j } > 0 , \nu _ { j } > 0$ for all j. Now it is obvious from Eq. (7) that since the coefficients of $a ( \lambda )$ are sums of products of positive numbers, they are positive.■

Note that the condition (6) is not sufficient for the stability of $a ( \lambda ) .$ , as the example of the polynomial $\lambda ^ { 2 } + 1$ shows.

Thus, in the investigation of stability criteria we may first assume that the coefficients of a(λ) are positive. It turns out that in this case the determinantal inequalities in (13.9.11) are not independent. Namely, the positivity of the Hurwitz determinants $\Delta _ { i }$ of even order implies that of the Hurwitz determinants of odd order, and vice versa. This fact will follow from Theorem 4. We first establish simplifications of the Liénard-Chipart and Markov stability criteria. This is done with the help of the Cauchy index.

Theorem 2. (The Liénard-Chipart criterion). Let $\begin{array} { r } { a ( \lambda ) = \sum _ { i = 0 } ^ { l } a _ { i } \lambda ^ { i } } \end{array}$ be a real polynomial and let

$$
a ( \lambda ) = h ( \lambda ^ { 2 } ) + \lambda g ( \lambda ^ { 2 } )
$$

be its $L { - } C$ splitting. Then $a ( \lambda )$ is stable if and only if the coefficients of h(λ) have the same sign as $a _ { l }$ and the Bezoutian $B _ { 1 } = B ( h , g )$ is positive denite.

ProoF. The necessity of the condition follows easily from Theorem 13.7.2 and Proposition 2. The converse statemer . will be proved for the even case, $l = 2 k$ , while the verification of the odd case is left as an exercise.

Let $B _ { 1 } = B ( h , g ) > O$ and assume the coefficients $a _ { 0 } , a _ { 2 } , \ldots , a _ { l }$ of $h ( \lambda )$ are positive. Then obviously $h ( \lambda ) \geq 0$ for all positive $\lambda \in \mathbb { R }$ Furthermore, if $h ( \lambda _ { 1 } ) = 0$ for $\lambda _ { 1 } > 0$ then $g ( \lambda _ { 1 } ) \neq 0$ since otherwise the Bezoutian B will be singular (Theorem 13.3.1). Thus, although the fractions $g ( \lambda ) / h ( \lambda )$ and $\lambda g ( \lambda ) / h ( \lambda )$ may suffer infinite discontinuity as λ passes from $0 \ : 1 0 \ : + \infty$ , there is no discontinuity in the value of the quotients from $- \infty \ t \ o \ + \infty$ , or from $+ \infty \mathrm { \ t o \ - \infty }$ . Hence

$$
I _ { 0 } ^ { + \infty } \frac { g ( \lambda ) } { h ( \lambda ) } = I _ { 0 } ^ { + \infty } \frac { \lambda g ( \lambda ) } { h ( \lambda ) } = 0 .
$$

Furthermore, it is clear that

$$
I _ { - \infty } ^ { 0 } \frac { g ( \lambda ) } { h ( \lambda ) } = - I _ { - \infty } ^ { 0 } \frac { \lambda g ( \lambda ) } { h ( \lambda ) } ,
$$

and therefore

$$
I _ { - \infty } ^ { + \infty } \frac { g ( \lambda ) } { h ( \lambda ) } = I _ { - \infty } ^ { 0 } \frac { g ( \lambda ) } { h ( \lambda ) } + I _ { 0 } ^ { + \infty } \frac { g ( \lambda ) } { h ( \lambda ) } = I _ { - \infty } ^ { 0 } \frac { g ( \lambda ) } { h ( \lambda ) } = - I _ { - \infty } ^ { 0 } \frac { \lambda g ( \lambda ) } { h ( \lambda ) } .\tag{8}
$$

But the Bezoutian $B _ { 1 } = \operatorname { B e z } ( h , g )$ is assumed to be positive definite, and therefore, by Theorem 1,

$$
I _ { - \infty } ^ { \infty } \frac { g ( \lambda ) } { h ( \lambda ) } = k .
$$

Applying Theorem 1 again, we find from Eq. (8) that $B _ { 2 } = \mathop { \bf B e z } ( h , \lambda g )$ is negative definite. Theorem 13.7.2 now provides the stability of the polynomial a(λ). ■

Note that Theorem 2 can be reformulated in an obvious way in terms of the Bezoutian $B _ { 2 } = { \bf B e z } ( h , g )$ and the coefficients of $h ( \lambda )$ (or $g ( \lambda ) )$

The congruence of the matrices $B _ { 1 }$ and $H _ { 1 }$ defined in Theorem 13.8.2 leads to the following result.

Theorem 3 (The Markov criterion). A real polynomial $a ( \lambda )$ is stable if and only if the coefficients of $h ( \lambda )$ from the L-C splitting of $a ( \lambda )$ have the same sign as the leading coefficient of a(λ) and also $H _ { 1 } > 0 .$

The remark made after Theorem 2 obviously applies to Theorem 3. This fact, as well as the relations (13.9.7) and (13.9.8), permit us to obtain a different form of the Liénard-Chipart criterion.

Theorem 4 (The Liénard-Chipart criterion). A real polynomial $a ( \lambda ) =$ $\sum _ { i = 0 } ^ { l } a _ { i } \lambda ^ { i } , a _ { l } > 0 .$ is stable if and only if one of the following four conditions holds:

$$
( a ) \quad a _ { 0 } > 0 , a _ { 2 } > 0 , \ldots ; \qquad \Delta _ { 1 } > 0 , \Delta _ { 3 } > 0 , \ldots ;
$$

$$
( b ) \quad a _ { 0 } > 0 , a _ { 2 } > 0 , \ldots ; \qquad \Delta _ { 2 } > 0 , \Delta _ { 4 } > 0 , \ldots ;
$$

$$
\begin{array} { r l } { ( c ) } & { { } a _ { 0 } > 0 , a _ { 1 } > 0 , a _ { 3 } > 0 , . . . ; \qquad \Delta _ { 1 } > 0 , \Delta _ { 3 } > 0 , . . . ; } \end{array}
$$

$$
\begin{array} { r l } { ( d ) } & { { } a _ { 0 } > 0 , a _ { 1 } > 0 , a _ { 3 } > 0 , . . . ; \qquad \Delta _ { 2 } > 0 , \Delta _ { 4 } > 0 , . . . . } \end{array}
$$

The detailed proof is left to the reader.

We conclude this section with one more application of Theorem 1, but first we need the following statement, which is of independent interest.

Theorem 5. The number of distinct zeros of a real polynomial $a ( \lambda )$ of degree l is equal to the rank of the Hankel matrix $H = [ s _ { i + j } ] _ { i , j = 0 } ^ { l - 1 }$ of the Newton sums $s _ { 0 } = l , s _ { k } = \lambda _ { 1 } ^ { k } + \lambda _ { 2 } ^ { k } + \cdot \cdot \cdot + \lambda _ { l } ^ { k } , k = 1 , 2 , . . . ,$ where $\lambda _ { 1 }$ $\lambda _ { 2 } , \ldots , \lambda _ { i }$ are the zeros of $a ( \lambda )$

PRoOF. We first observe that $H = V V ^ { \mathbf { T } }$ , where V denotes the $l \times l$ Vandermonde matrix associated with $\lambda _ { 1 } , ~ \lambda _ { 2 } , \ldots , \lambda _ { i }$ . Hence rank $H =$ rank V and the result follows.

Note that the significance of this and the following theorem lies in the fact that the Newton sums $s _ { 0 } , s _ { 1 } , \ldots$ can be evaluated recursively via the coefficients of the polynomial. If $a ( \lambda ) = a _ { 0 } + a _ { 1 } \lambda + \cdots + a _ { l - 1 } \lambda ^ { l - 1 } + \lambda ^ { l } { } _ { \mathrm { { \scriptscriptstyle \dag } } }$ then

$$
s _ { 0 } = l , \qquad k a _ { l - k } + a _ { l - k + 1 } s _ { 1 } + \cdot \cdot \cdot + a _ { l - 1 } s _ { k - 1 } + s _ { k } = 0 ,\tag{9}
$$

for $k = 1 , 2 , \ldots , l - 1$ , and

$$
a _ { 0 } s _ { k - l } + a _ { 1 } s _ { k - l - 1 } + \cdots + a _ { l - 1 } s _ { k - 1 } + s _ { k } = 0 ,\tag{10}
$$

for $k = l , l + 1 , \ldots ,$

Theorem 6 (C. Borhardt and G. Jacobi†). The real polynomial $a ( \lambda ) =$ $\sum _ { i = 0 } ^ { l } a _ { i } \lambda ^ { i }$ has v different pairs of complex conjugate zeros and π – v different real zeros, where $\{ \pi , \nu , \delta \}$ is the inertia of the Hankel matrix $\pmb { H } = [ s _ { i + j } ] _ { i , j = 0 } ^ { l - 1 }$ of the Newton sums associated with $a ( \lambda )$

PROOF. Putting $c ( \lambda ) = a ( \lambda ) , b ( \lambda ) = a ^ { \prime } ( \lambda )$ in Theorem 1, we obtain

$$
{ \bf B e z } ( a , a ^ { \prime } ) = I _ { - \infty } ^ { + \infty } \frac { a ^ { \prime } ( \lambda ) } { a ( \lambda ) } .
$$

Since

$$
a ^ { \prime } ( \lambda ) = ( s _ { 0 } \lambda ^ { - 1 } + s _ { 1 } \lambda ^ { - 2 } + \cdot \cdot \cdot ) a ( \lambda ) ,\tag{11}
$$

where $s _ { 0 } , s _ { 1 } , s _ { 2 } , \ldots$ . are the Newton sums associated with $a ( \lambda ) ,$ , it follows that by formula (13.8.1) the matrices $\mathtt { B e z } ( a , a ^ { \prime } )$ and the matrix H of the Newton sums are congruent. Hence the relation (1) shows, in view of Proposition 1, that the number of distinct real zeros of $a ( \lambda )$ is equal to sig $H = \pi - \nu .$ By Theorem 5, rank $H = \pi + \nu$ is equal to the total number of distinct zeros of $a ( \lambda )$ and therefore $a ( \lambda )$ has $2 \nu$ distinct complex zeros. The result follows.

Exercise 4. Evaluate the number of distinct real zeros and the number of different pairs of complex conjugate zeros of the polynomial $a ( \lambda ) = \lambda ^ { 4 } -$ $2 \lambda ^ { 3 } + 2 \lambda ^ { 2 } - 2 \lambda + 1$

SoLUTION. To find the Newton sums of $a ( \lambda )$ , we may use formulas (9) and (10) or the representation (11). We have $s _ { 0 } = 4 , s _ { 1 } = 2 , s _ { 2 } = 0 , s _ { 3 } = 2 $ $s _ { 4 } = 4 , s _ { 5 } = 2 , s _ { 6 } = 0$ , and hence the corresponding Hankel matrix H is

$$
H = { \left[ \begin{array} { l l l l } { 4 } & { 2 } & { 0 } & { 2 } \\ { 2 } & { 0 } & { 2 } & { 4 } \\ { 0 } & { 2 } & { 4 } & { 2 } \\ { 2 } & { 4 } & { 2 } & { 0 } \end{array} \right] } .
$$

Since In $H = \{ 2 , 1 , 1 \}$ , there is one pair of distinct complex conjugate zeros (ν = 1) and one real zero $( \pi - \nu = 1 )$ . It is easily checked that, actually, $a ( \lambda ) = ( \lambda - 1 ) ^ { 2 } ( \lambda ^ { 2 } + 1 )$ , and the results are confirmed.

## Matrix Polynomials

It was seen in Sections 4.13 and 9.10 that the solution of a system of constant-coefficient (or time-invariant) differential equations, ${ \dot { \mathbf { x } } } ( t ) - A { \mathbf { x } } ( t )$ $\mathbf { \mu } = f ( t ) .$ , where $A \in \mathbb { C } ^ { n \times n }$ and ${ \pmb x } ( 0 )$ is prescribed, is completely determined by the properties of the matrix-valued function $\lambda I - A$ More specifically, the solution is determined by the zeros of det $( \lambda I - A )$ and by the bases for the subspaces $\boldsymbol { \mathrm { K e r } } ( \lambda I - A ) ^ { j }$ of $\mathbb { C } ^ { n } , \ j = 0 , 1 , 2 , \ldots , n .$ These spectral properties are, in turn, summarized in the Jordan form for A or, as we shall now say, in the Jordan form for $\lambda I - A$

The analysis of this chapter† will admit the description of solutions for initial-value problems for higher-order systems:

$$
L _ { l } \mathbf { \boldsymbol { x } } ^ { ( l ) } ( t ) + L _ { l - 1 } \mathbf { \boldsymbol { x } } ^ { ( l - 1 ) } ( t ) + \cdot \cdot \cdot + L _ { 1 } \mathbf { \boldsymbol { x } } ^ { ( 1 ) } ( t ) + L _ { 0 } \mathbf { \boldsymbol { x } } ( t ) = f ( t ) ,\tag{1}
$$

where $L _ { 0 } , L _ { 1 } , \dots , L _ { l } \in \mathbb { C } ^ { n \times n } ,$ det $L _ { l } \neq 0 ,$ and the indices denote derivatives with respect to the independent variable t. The underlying algebraic problem now concerns the associated matrix polynomial $\begin{array} { r } { L ( \lambda ) = \sum _ { j = 0 } ^ { l } \lambda ^ { j } L _ { j } } \end{array}$ of degree $l ,$ as introduced in Section 7.1. We shall confine our attention to the case in which det $L _ { l } \neq 0$ Since the coefficient of $\lambda ^ { l n }$ in the polynomial det $L ( \lambda )$ is just det $L _ { t }$ , it follows that $L ( \lambda )$ is regular or, in the terminology of Section 7.5, has rank n.

As for the first-order system of differential equations, the formulation of general solutions for Eq. (1) (even when the coefficients are Hermitian) requires the development of a “Jordan structure” for $L ( \lambda )$ , and that will be done in this chapter. Important first steps in this direction have been taken in Chapter 7; we recall particularly the Smith normal form and the elementary divisors, both of which are invariant under equivalence transformations of $L ( \lambda )$ . In Chapter 7, these notions were used to develop the Jordan structure of $\lambda I - A$ (or of A). Now they will be used in the analysis of the spectral properties of more general matrix polynomials.

## 14.1 Linearization of a Matrix Polynomial

It has been seen on several occasions in earlier chapters that if $a ( \lambda ) =$ $\Sigma _ { j = 0 } ^ { l } a _ { j } \lambda ^ { j }$ is a monic scalar polynomial then the related $l \times l$ companion matrix,

$$
C _ { a } = { \left[ \begin{array} { l l l l l } { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 1 } & { } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { } & { 1 } \\ { - a _ { 0 } } & { - a _ { 1 } } & { - a _ { 2 } } & { \cdots } & { - a _ { l - 1 } } \end{array} \right] } ,\tag{1}
$$

is a useful idea. Recall the important part played in the formulation of the first natural normal form of Chapter 7 and in the formulation of stability criteria in Chapter 13 (see also Exercises 6.6.3 and 7.5.4). In particular, note that $a ( \lambda ) = \operatorname* { d e t } ( \lambda I - C _ { a } )$ , so that the zeros of ${ \pmb a } ( \lambda )$ correspoņd to the eigenvalues of $C _ { a }$

For a matrix polynomial of size $n \times n ,$

$$
L ( \lambda ) = \sum _ { j = 0 } ^ { l } \lambda ^ { j } L _ { j } , \qquad \operatorname * { d e t } L _ { l } \neq 0 ,\tag{2}
$$

we formulate the generalization of the matrix in (1):

$$
\boldsymbol C _ { L } = \left[ \begin{array} { c c c c c } { \boldsymbol \theta } & { \boldsymbol I _ { n } } & { \boldsymbol \theta } & { \cdots } & { \boldsymbol \theta } \\ { \boldsymbol \theta } & { \boldsymbol \theta } & { \boldsymbol I _ { n } } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { \boldsymbol \dot { I _ { n } } } \\ { - \hat { \boldsymbol L } _ { 0 } } & { - \hat { \boldsymbol L } _ { 1 } } & { - \hat { \boldsymbol L } _ { 2 } } & { \cdots } & { - \hat { \boldsymbol L } _ { l - 1 } } \end{array} \right] ,\tag{3}
$$

where $\widehat { L } _ { j } = L _ { l } ^ { - 1 } L _ { j }$ for $j = 0 , 1 , \ldots , l - 1$ . Now consider the relationships between $L ( \lambda )$ and $\lambda I _ { i n } - C _ { L }$ . The ln × ln matrix $C _ { L }$ is called the $( \hslash r s t )$ companion matrix for $L ( \lambda )$

The first observation is that the characteristic polynomials satisfy

$$
\operatorname* { d e t } L ( \lambda ) = \operatorname* { d e t } ( \lambda I _ { l n } - C _ { L } ) ( \operatorname* { d e t } L _ { l } ) .\tag{4}
$$

This means that the latent roots of $L ( \lambda )$ (as defined in Section 7.7) coincide with the eigenvalues of $C _ { L }$ . Admitting an ambiguity that should cause no difficulties, the set of latent roots of $L ( \lambda )$ is called the spectrum of $L ( \lambda )$ and is·written $\sigma ( L )$ . From the point of view of matrix polynomials, the relation (4) says that $L ( \lambda )$ and $\lambda I - C _ { L }$ have the same invariant polynomial of highest degree. However, the connection is deeper than this, as the first theorem shows.

Theorem 1. The ln × ln matrix polynomials

$$
\left[ \begin{array} { c c } { { L ( \lambda ) } } & { { 0 } } \\ { { 0 } } & { { I _ { ( l - 1 ) n } } } \end{array} \right] \qquad a n d \qquad \lambda I _ { l n } - C _ { L }
$$

are equivalent.

PRooF. First define ln × ln matrix polynomials E(λ) and $F ( \lambda )$ by

$$
\boldsymbol { F } ( \lambda ) = \left[ \begin{array} { c c c c } { \boldsymbol { I } } & { \boldsymbol { 0 } } & { \cdots } & { \boldsymbol { 0 } } \\ { - \lambda \boldsymbol { I } } & { \boldsymbol { I } } & & { \vdots } \\ { \boldsymbol { 0 } } & { - \lambda \boldsymbol { I } } & { \boldsymbol { I } _ { \cdot _ { \cdot _ { \cdot _ { \cdot } } } } } & { \boldsymbol { \cdot } } \\ { \vdots } & & & { \boldsymbol { \cdot } } & { \boldsymbol { I } } \\ { \boldsymbol { 0 } } & { \cdots } & & { - \lambda \boldsymbol { I } } & { \boldsymbol { I } } \end{array} \right] ,
$$

$$
E ( \lambda ) = \left[ \begin{array} { c c c c c } { { B _ { \iota - 1 } ( \lambda ) } } & { { B _ { \iota - 2 } ( \lambda ) } } & { { \cdots } } & { { B _ { 0 } ( \lambda ) } } \\ { { } } & { { } } & { { } } & { { } } \\ { { - I } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { } } & { { } } & { { } } & { { } } \\ { { 0 } } & { { - I } } & { { \ddots } } & { { \vdots } } \\ { { \vdots } } & { { } } & { { \ddots } } & { { \ddots } } \\ { { 0 } } & { { \cdots } } & { { } } & { { - I } } & { { 0 } } \end{array} \right] ,
$$

where $B _ { 0 } ( \lambda ) = L _ { l } , B _ { r + 1 } ( \lambda ) = \lambda B _ { r } ( \lambda ) + L _ { l - r - 1 }$ for $r = 0 , 1 , \ldots , l - 2 .$ and $I = I _ { n }$ . Clearly

$$
\operatorname* { d e t } E ( \lambda ) \equiv \pm \operatorname* { d e t } L _ { \iota } , \operatorname* { d e t } F ( \lambda ) \equiv 1 .\tag{5}
$$

Hence $F ( \lambda ) ^ { - 1 }$ is also a matrix polynomial. It is easily verified that

$$
E ( \lambda ) ( \lambda I - C _ { L } ) = \binom { L ( \lambda ) } { O } \ { \cal I } _ { ( l - 1 ) n } \Biggr ] F ( \lambda ) ,\tag{6}
$$

and so

$$
\left[ \begin{array} { c c } { L ( \lambda ) } & { O } \\ { O } & { I _ { ( l - 1 ) n } } \end{array} \right] = E ( \lambda ) ( \lambda I - C _ { L } ) F ( \lambda ) ^ { - 1 }
$$

determines the equivalence stated in the theorem.

Theorem 1 (together with Theorem 7.5.1 and its corollary) shows that all of the nontrivial invariant polynomials (and hence all of the elementary divisors) of $L ( \lambda )$ and $\lambda I - C _ { L }$ coincide. Here, “nontrivial" means a polynomial that is not identically equal to 1.

Exercise 1. Establish the relations (4) and (5).

Exercise 2. Show that if λ is an eigenvalue of $C _ { L }$ then the dimension of $\mathsf { K e r } ( \lambda I - C _ { L } )$ cannot exceed n. (Note the special case $n = 1 . )$

Exercise 3. Formulate the first companion matrix and find all elementary divisors of (a) $L ( \lambda ) = \lambda ^ { l } I _ { n }$ and (b) $L ( \lambda ) = \lambda ^ { l } I _ { n } - I _ { n }$ □

Observe now that there are other matrices A, as well as $C _ { L }$ , for which $\lambda I - A$ and $\mathrm { d i a g } [ L ( \lambda ) , I _ { ( l - 1 ) n } ]$ are equivalent. In particular, if A is a matrix similar to $C _ { L } .$ say $A = \dot { T } \dot { C _ { L } } T ^ { - 1 }$ , then $\lambda I - A = T ( \lambda I - C _ { L } ) T ^ { - 1 }$ , so that $\lambda I - A$ and $\lambda I - C _ { L }$ are equivalent and, by the transitivity of the equivalence relation, $\lambda I - A$ and diag[ $L ( \lambda ) , I _ { ( l - 1 ) n } ]$ are equivalent. It is useful to make a formal definition: If $L ( \lambda )$ is an $n \times n$ matrix polynomial of degree l with nonsingular leading coefficient, then any ln × ln matrix A for which $\lambda I - A$ and diag[L(λ), $I _ { ( \ell - 1 ) n } ]$ are equivalent is called a linearization of $L ( \lambda )$

The next theorem shows that the matrices A that are similar to $C _ { L }$ are, in fact, all of the linearizations of $L ( \lambda )$

Theorem 2. Any matrix A is a linearization of $L ( \lambda )$ if and only if A is similar to the companion matrix $C _ { L }$ of L(λ).

PRooF. It has been shown that if A is similar to $C _ { L }$ then it is a linearization of $L ( \lambda )$ . Conversely, if A is a linearization of $L ( \lambda )$ then $\lambda I - A \sim L ( \lambda ) \dot { + }$ $I _ { ( l - 1 ) n }$ (using \~ as an abbreviation for “equivalent to"). But by Theorem $\dot { 1 , } L ( \lambda ) \dot { + } I _ { ( l - 1 ) n } \sim \lambda I - C _ { L }$ so, using transitivity again, $\lambda I - A \sim \lambda I - C _ { L }$ Then Theorem 7.6.1 shows that A and $C _ { L }$ are similar.

This result, combined with Theorem 6.5.1 (or 7.8.2), shows that there is a matrix in Jordan normal form that is a linearization for $L ( \lambda )$ and, therefore, it includes all the information concerning the latent roots of $L ( \lambda )$ and their algebraic multiplicities (i.e., the information contained in a Segre characteristic, as described in Section 6.6).

Exercise 4. Use Exercise 6.6.3 to find a matrix in Jordan normal form that is a linearization for a scalar polynomial (i.e., a $1 \times 1$ matrix polynomial $L ( \lambda ) )$

Exercise 5. Find matrices in Jordan normal form that are linearizations for the matrix polynomials of Exercise 3. Do the same for

$$
L ( \lambda ) = \left[ \begin{array} { l l } { \lambda ^ { 2 } } & { - \lambda } \\ { 0 } & { \lambda ^ { 2 } } \end{array} \right] .
$$

SoLUTION. The solution in the latter case is either

$$
{ \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } \qquad { \mathrm { o r } } \qquad { \left[ \begin{array} { l l l l } { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } \ .
$$

Exercise 6. Let $\widehat { L } _ { j } = L _ { j } L _ { l } ^ { - 1 }$ for $j = 0 , 1 , \ldots , l - 1$ , and define the second companion matrix for $L ( \lambda )$ to be the $l n \times$ ln matrix

$$
C _ { 2 } = \left[ \begin{array} { l l l l l } { 0 } & { 0 } & { \cdots } & { 0 } & { - \widetilde { L } _ { 0 } } \\ { I } & { 0 } & & { \vdots } & { \vdots } \\ { 0 } & { I } & & { \vdots } & \\ { \vdots } & & { \ddots } & { 0 } & { - \widetilde { L } _ { l - 2 } } \\ { 0 } & { \cdots } & & { I } & { - \widetilde { L } _ { l - 1 } } \end{array} \right] .
$$

Also (see Chapter 13) define the symmetrizer for $L ( \lambda )$ to be

$$
S _ { L } = \left[ \begin{array} { c c c c c } { L _ { 1 } } & { L _ { 2 } } & { \cdots } & { L _ { l - 1 } } & { L _ { l } } \\ { L _ { 2 } } & { } & { } & { L _ { l } } & { 0 } \\ { \vdots } & { \cdot } & { \cdot } & { \cdot } & { \vdots } \\ { L _ { l - 1 } } & { L _ { l } } & { } & { } & { } \\ { L _ { l } } & { 0 } & { \cdots } & { } & { 0 } \end{array} \right] .\tag{7}
$$

Show that $S _ { L }$ is nonsingular, that $C _ { 2 } = S _ { L } C _ { L } S _ { L } ^ { - 1 }$ and, hence, that $C _ { 2 }$ is a linearization of $L ( \lambda )$

## 14.2 Standard Triples and Pairs

In the spectral theory of a general matrix $\pmb { A } \in \mathbb { C } ^ { n \times n }$ , the resolvent function $( \lambda I - A ) ^ { - 1 }$ plays an important part on several occasions. For a matrix polynomial $L ( \lambda )$ , as defined in the relations (14.1.2), the matrix-valued function $L ( \lambda ) ^ { - 1 }$ (defined for all $\lambda \notin \sigma ( L ) )$ plays the corresponding role and is called the resolvent of $L ( \lambda )$ . The next step in our analysis shows how the resolvent of the first companion matrix $C _ { L }$ can be used to determine the resolvent of $L ( \lambda )$

Theorem 1. For every complex $\lambda \notin \sigma ( L )$

$$
L ( \lambda ) ^ { - 1 } = P _ { 1 } ( \lambda I - C _ { L } ) ^ { - 1 } R _ { 1 } ,\tag{1}
$$

where $P _ { 1 } , R _ { 1 }$ are the matrices of size $n \times$ nl and ln $\times \ n ,$ respectively, defined by

$$
\begin{array} { r } { P _ { 1 } = [ I _ { n } \quad 0 \quad \cdots \quad 0 ] , \qquad R _ { 1 } = \left[ \begin{array} { c } { 0 } \\ { \vdots } \\ { 0 } \\ { L _ { l } ^ { - 1 } } \end{array} \right] . } \end{array}\tag{2}
$$

ProoF. First observe that, because of Eq. (14.1.4), the matrix $( \lambda I - C _ { L } ) ^ { - 1 }$ is defined at just those points λ where $L ( \lambda ) ^ { - 1 }$ exists. Now consider the proof of Theorem 14.1.1 once more. The relation (14.1.6) implies that

$$
\left[ \begin{array} { c c } { { L ( \lambda ) ^ { - 1 } } } & { { 0 } } \\ { { 0 } } & { { I _ { ( l - 1 ) n } } } \end{array} \right] = F ( \lambda ) ( \lambda I - C _ { L } ) ^ { - 1 } E ( \lambda ) ^ { - 1 } .\tag{3}
$$

Using the definition of $E ( \lambda )$ , it is easily verified that

$$
E ( \lambda ) \left[ \begin{array} { c } { { 0 } } \\ { { \vdots } } \\ { { 0 } } \\ { { L _ { l } ^ { - 1 } } } \end{array} \right] = \left[ \begin{array} { c } { { I } } \\ { { 0 } } \\ { { \vdots } } \\ { { 0 } } \end{array} \right] ,
$$

and this means that the first n columns of $E ( \lambda ) ^ { - 1 }$ are simply equal to $R _ { 1 }$ Since the first n rows of $F ( \lambda )$ are equal to $P _ { 1 }$ , if we equate the leading $n \times n$ submatrices on the left and right of Eq. (3), we obtain Eq. (1).■

Three matrices $( U , T , V )$ are said to be admissible for the $n \times n$ matrix polynomial $L ( \lambda )$ of degree l (as defined in Eq. (14.1.2)) if they are of sizes $n \times l n ,$ In $\times \ l n ,$ and ln $\times \ n ,$ respectively. Then two admissible triples for $L ( \lambda )$ , say $( U _ { 1 } , T _ { 1 } , V _ { 1 } )$ and $( U _ { 2 } , T _ { 2 } , V _ { 2 } )$ , are said to be similar if there is a nonsingular matrix S such that

$$
U _ { 1 } = U _ { 2 } S , \qquad T _ { 1 } = S ^ { - 1 } T _ { 2 } S , \qquad V _ { 1 } = S ^ { - 1 } V _ { 2 } .\tag{4}
$$

Exercise 1. Show that similarity of triples is an equivalence relation on the set of all admissible triples for L(λ).

Now, the triple $( P _ { 1 } , C _ { L } , R _ { 1 } )$ is admissible for $L ( \lambda ) ,$ , and any triple similar to $( P _ { 1 } , C _ { L } , R _ { 1 } )$ is said to be a standard triple for L(λ). Of course, with a transforming matrix $S = I ,$ this means that $( P _ { 1 } , C _ { L } , R _ { 1 } )$ is itself a standard triple. Note that, by Theorem 14.1.2, the second member of a standard triple for $L ( \lambda )$ is always a linearization of $L ( \lambda )$ . Now Theorem 1 is easily generalized.

Theorem 2. $I f ( U , T , V )$ is a standard triple for $L ( \lambda )$ and $\lambda \notin \sigma ( L )$ , then

$$
L ( \lambda ) ^ { - 1 } = U ( \lambda I - T ) ^ { - 1 } V .
$$

PROOF. Since $( U , T , V )$ is a standard triple, there is a nonsingular matrix S such that

$$
P _ { 1 } = U S , \qquad C _ { L } = S ^ { - 1 } T S , \qquad R _ { 1 } = S ^ { - 1 } V .
$$

Observe that $( \lambda I - C _ { L } ) ^ { - 1 } = ( S ^ { - 1 } ( \lambda I - T ) S ) ^ { - 1 } = S ^ { - 1 } ( \lambda I - T ) ^ { - 1 } S ,$ and substitute into Eq. (1) to obtain the result.

Thus we obtain a representation of the resolvent of $L ( \lambda )$ in terms of the resolvent of any linearization for $L ( \lambda )$ . Our next objective is to characterize standard triples for $L ( \lambda )$ in a more constructive and direct way; it is not generally reasonable to try to find the matrix S of the proof of Theorem 2 explicitly. First we will show how to “recover" the companion matrix $C _ { L }$ from any given standard triple.

Lemma 1. Let $( U , T , V )$ be a standard triple for $L ( \lambda )$ and define

$$
\boldsymbol { Q } = \left[ \begin{array} { c } { \boldsymbol { U } } \\ { \boldsymbol { U } \boldsymbol { T } } \\ { \vdots } \\ { \boldsymbol { U } \boldsymbol { T } ^ { l - 1 } } \end{array} \right] .\tag{5}
$$

Then $Q$ is nonsingular and $C _ { L } = Q T Q ^ { - 1 }$

PROOF. Recall that $P _ { 1 } = [ I _ { n } \quad 0 \quad \cdots \quad 0 ]$ and $C _ { L }$ is given by Eq. (14.1.3). It is easily seen that

$$
\left[ \begin{array} { c } { P _ { 1 } } \\ { P _ { 1 } C _ { L } } \\ { \vdots } \\ { P _ { 1 } C _ { L } ^ { l - 1 } } \end{array} \right] = I _ { l N } .\tag{6}
$$

Substitute for $P _ { 1 }$ and $C _ { L }$ from Eqs. (4) to obtain $Q S = I _ { l n }$ . Obviously, Q is nonsingular and $S = Q ^ { - 1 }$ . In particular, $C _ { L } = Q T Q ^ { - 1 }$ L

In fact, this lemma shows that for any standard triple $( U , T , V ) ,$ the primitive triple $( P _ { 1 } , C _ { L } , R _ { 1 } )$ can be recovered from Eqs. (4) on choosing $S = Q ^ { - 1 }$ 9 where Q is given by Eq. (5).

Theorem 3. An admissible triple (U, T, V) for L(λ) is a standard triple if and only if the three following conditions are satisfied:

(a) The matrix Q of Eq. (5) is nonsingular;

(b) $\begin{array} { r } { L _ { l } U T ^ { l } + L _ { l - 1 } U T ^ { l - 1 } + \cdots + L _ { 1 } U T + L _ { 0 } U = 0 . } \end{array}$

(c) $V = Q ^ { - 1 } R _ { 1 }$ , where Q and $R _ { 1 }$ are given by Eqs. (5) and (2), respectively

PRooF. We first check that conditions (a), (b), and (c) are satisfied by the standard triple $( P _ { 1 } , C _ { L } , R _ { 1 } )$ . Condition (a) is proved in the proof of Lemma 1. The relation (6) also gives

$$
P _ { 1 } C _ { L } ^ { l } = ( P _ { 1 } C _ { L } ^ { l - 1 } ) C _ { L } = [ 0 \quad \cdots \quad 0 \quad I ] C _ { L } = [ - \widehat { L } _ { 0 } \quad \cdots \quad - \widehat { L } _ { l - 1 } ] .
$$

Consequently,

$$
\begin{array} { r } { L _ { l } P _ { 1 } C _ { L } ^ { l } = \left[ - L _ { 0 } \quad - L _ { 1 } \quad \cdots \quad - L _ { l - 1 } \right] . } \end{array}\tag{7}
$$

But also,

$$
\sum _ { j = 0 } ^ { l - 1 } L _ { j } P _ { 1 } C _ { L } ^ { j } = [ L _ { 0 } \quad L _ { 1 } \quad \cdots \quad L _ { l - 1 } ] \left[ \begin{array} { c } { { P _ { 1 } } } \\ { { P _ { 1 } C _ { L } } } \\ { { \vdots } } \\ { { P _ { 1 } C _ { L } ^ { l - 1 } } } \end{array} \right] = [ L _ { 0 } \quad L _ { 1 } \quad \cdots \quad L _ { l - 1 } ] .
$$

So, adding the last two relations, we get $\sum _ { j = 0 } ^ { l } L _ { j } P _ { 1 } C _ { L } ^ { j } = 0 .$ which is just the relation (b) with $( U , T , V )$ replaced by $( P _ { 1 } , C _ { L } , R _ { 1 } )$ . In this case $Q = I ,$ so condition (c) is trivially satisfied.

Now let $( U , T , V )$ be any standard triple and let

$$
U = P _ { 1 } S , \qquad T = S ^ { - 1 } C _ { L } S , \qquad V = S ^ { - 1 } R _ { 1 } .
$$

Then

$$
Q = \left[ \begin{array} { c } { { U } } \\ { { U T } } \\ { { \vdots } } \\ { { U T ^ { l - 1 } } } \end{array} \right] = \left[ \begin{array} { c } { { P _ { 1 } } } \\ { { P _ { 1 } C _ { L } } } \\ { { \vdots } } \\ { { P _ { 1 } C _ { L } ^ { l - 1 } } } \end{array} \right] S = S ,
$$

using (6) so that (a) is satisfied. Then

$$
\sum _ { j = 0 } ^ { l } L _ { j } U T ^ { j } = \left( \sum _ { j = 0 } ^ { l } L _ { j } P _ { 1 } C _ { L } ^ { j } \right) S = 0 ,
$$

which is condition (b). Finally, $Q V = S ( S ^ { - 1 } R _ { 1 } ) = R _ { 1 }$ , which is equivalent to (c).

Conversely, suppose that we are given an admissible triple for $L ( \lambda )$ that satisfies conditions (a), (b), and (c). We must show that $( U , T , V )$ is similar to $( P _ { 1 } , C _ { L } , R _ { 1 } )$ . First, from the definition (5) of Q, it is obvious that $U = { \pmb { P } } _ { 1 } Q$ and, using condition (a), Q is nonsingular.

Then use condition (b) to verify that $Q T = C _ { L } Q$ by multiplying out the partitioned matrices. Thus, $T = { Q } ^ { - 1 } C _ { L } { Q }$

Combine these results with condition (c) to get

$$
U = P _ { 1 } Q , \qquad T = Q ^ { - 1 } C _ { L } Q , \qquad V = Q ^ { - 1 } R _ { 1 } ,
$$

and so $( U , T , V )$ is similar to $( P _ { 1 } , C _ { L } , R _ { 1 } )$ and hence is a standard triple.■

## 14.2 STANDARD TRIPLES AND PAIRS

This theorem makes it clear that a standard triple is completely determined by its first two members. It is frequently useful to work in terms of such a pair and so they are given a name: a standard pair for $L ( \lambda )$ is the first two members of any standard triple for $L ( \lambda )$ . Thus $( U , T )$ is a standard pair for $L ( \lambda )$ if and only if conditions (a) and (b) of the theorem are satisfied.

Exercise 2. Show that, if $( U , T )$ is a standard pair for $L ( \lambda ) .$ then $( U , T )$ is also a standard pair for any matrix polynomial of the form $A L ( \lambda )$ , where det $A \neq 0 .$

Exercise 3. Let $C _ { 2 }$ be the second companion matrix for $L ( \lambda )$ , as defined in Exercise 14.1.6. Show that the admissible triple

$$
[ 0 \quad \cdots \quad 0 \quad L _ { l } ^ { - 1 } ] , \qquad C _ { 2 } , \qquad \left[ { \begin{array} { l } { I } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} } \right]
$$

forms a standard triple for $L ( \lambda )$

Exercise 4. Let $( U , T , V )$ be a standard triple for $L ( \lambda ) ,$ , and let Γ be a contour in the complex plane with $\sigma ( L )$ inside Γ. If $f ( \lambda )$ is a function that is analytic inside Γ and continuous on Γ, show that

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \Gamma } f ( \lambda ) L ( \lambda ) ^ { - 1 } d \lambda = U f ( T ) V .
$$

Exercise 5. If U, T) is a standard pair for $L ( \lambda )$ , show that in the terminology of Section 5.13, (U, T) is an observable pair of index l. (This is also a sufficient condition for $( U , T )$ of sizes n × ln and $l n \times l n ,$ , respectively, to be a standard pair for some monic matrix polynomials of degree l; see Theorem 1).□

There is a useful converse statement for Theorem 2.

Theorem 4. Let $( U , T , V )$ be an admissible triple for L(λ) and assume that

$$
L ( \lambda ) ^ { - 1 } = U ( \lambda I - T ) ^ { - 1 } V .\tag{8}
$$

Then $( U , T , V )$ is a standard triple for L(λ).

PRoOF. For |λ| sufficiently large, $L ( \lambda ) ^ { - 1 }$ has a Laurent expansion of the form

$$
L ( \lambda ) ^ { - 1 } = \lambda ^ { - l } L _ { l } ^ { - 1 } + \lambda ^ { - l - 1 } A _ { 1 } + \lambda ^ { - l - 2 } A _ { 2 } + \cdots ,\tag{9}
$$

for some matrices $A _ { 1 } , A _ { 2 } , \ldots$ . Now let Γ be a circle in the complex plane with centre at the origin and having $\sigma ( L )$ and the eigenvalues of T in its

interior. Then integrating Eq. (9) term by term and using the theorem of residues,

$$
\frac { 1 } { 2 \pi i } \int _ { L } \lambda ^ { j } \boldsymbol { L } ( \lambda ) ^ { - 1 } ~ d \lambda = \left\{ \begin{array} { l l } { \boldsymbol { 0 } } & { \quad \mathrm { i f } \quad j = 0 , 1 , \ldots , l - 2 ; } \\ { \boldsymbol { L } _ { l } ^ { - 1 } } & { \quad \mathrm { i f } \quad j = l - 1 . } \end{array} \right.
$$

But also (see Theorem 9.9.2),

$$
\frac { 1 } { 2 \pi i } \int _ { L } \lambda ^ { j } ( \lambda I - T ) ^ { - 1 } d \lambda = T ^ { j } , \qquad j = 0 , 1 , 2 , \ldots .\tag{10}
$$

It therefore follows from Eq. (8) (using \* to denote an $n \times n$ matrix of no immediate interest) that

$$
\begin{array}{c} { \begin{array} { r l } & { { \frac { 1 } { 2 \pi \mathrm { i } } } { \Biggl [ } { \left[ \begin{array} { l l l } { 1 } & { \cdots } & { { \bar { A } } ^ { - 1 } } \\ { \lambda } & { \cdots } & { \vdots } \\ { \lambda } & { \cdots } & { \lambda } \end{array} \right] } L ( \mathbb { A } ) ^ { - 4 } d \lambda = { \left[ \begin{array} { l l l } { \theta } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \cdots } & { L ^ { - 1 } } \\ { \vdots } & { \cdots } & { \vdots } \\ { 0 } & { L _ { i } ^ { - 1 } } & { \cdots } & { \vdots } \\ { L _ { i } ^ { - 1 } } & { \cdots } & { \cdots } & { \vdots } \end{array} \right] } } \\ & { \quad = { \left[ \begin{array} { l l l } { U V } & { U T V } & { \cdots } & { U T ^ { \ast } } \\ { U T V } & { \cdots } & { \cdots } & { \vdots } \\ { \vdots } & { \cdots } & { \vdots } \\ { U T ^ { \ast } } & { \cdots } & { \cdots } & { U T ^ { \ast - 1 } V } \end{array} \right] } } \\ & { \quad = { \left[ \begin{array} { l } { U } \\ { U } \\ { \cdots } \\ { U T ^ { \ast } } \end{array} \right] } { \left[ \begin{array} { l } { U } \\ { U } \\ { T } \end{array} \right] } } \\ & { \quad \cdots } \end{array} } \qquad { \mathrm { ( f o r ~ } } { \left[ \begin{array} { l } { U } \\ { \cdots } \\ { \cdots } \\ { \cdots } \\ { \cdots } \\ { \cdots } \end{array} \right] }  \\ & { \qquad = { \left[ \begin{array} { l } { U } \\ { U ^ { \ast } } \\ { \cdots } \\ { U T ^ { \ast - 1 } } \end{array} \right] } { \left[ \begin{array} { l } { U } \\ { \cdots } \\ { \cdots } \\ { \cdots } \\ { \cdots } \end{array} \right] } } \end{array}\tag{1}
$$

Both matrices in the last factorization are $l n \times l n$ and must be nonsingular, since the matrix above of triangular form is clearly nonsingular.

Using (10) once more we also have, for $j = 0 , 1 , . . . , l - 1$

$$
\begin{array} { l } { { \displaystyle { \cal O } = \frac { 1 } { 2 \pi i } \int _ { \Gamma } \lambda ^ { j } { \cal L } ( \lambda ) { \cal L } ( \lambda ) ^ { - 1 } d \lambda = \frac { 1 } { 2 \pi i } \int _ { \Gamma } \lambda ^ { j } { \cal L } ( \lambda ) U ( \lambda I - T ) ^ { - 1 } V d \lambda } } \\ { { { } } } \\ { { { } } } \\ { { { } = ( L _ { l } U T ^ { l } + \cdot \cdot \cdot + L _ { 1 } U T + L _ { 0 } U ) T ^ { j } V . } } \end{array}
$$

Hence,

$$
( L _ { l } U T ^ { l } + \cdots + L _ { 1 } U T + L _ { 0 } U ) [ V \quad T V \quad \cdots \quad T ^ { l - 1 } V ] = { \cal O } ,
$$

and since $[ V \quad T V \quad \cdots \quad T ^ { l - 1 } V ]$ is nonsingular, $\textstyle \sum _ { j = 0 } ^ { l } L _ { j } U T ^ { j } = O ($

## 14.2 STANDARD TRIPLES AND PAIRS

It has now been shown that U and T satisfy conditions (a) and (b) of Theorem 3. But condition (c) is also contained in Eqs. (11). Hence $( U , T , V )$ is a standard triple.

Corollary 1. $I f ( U , T , V )$ is a standard triple for $L ( \lambda )$ , then $( V ^ { \boldsymbol { \mathsf { T } } } , T ^ { \boldsymbol { \mathsf { T } } } , U ^ { \boldsymbol { \mathsf { T } } } )$ is a standard triple for $\begin{array} { r } { L ^ { \mathbf { T } } ( \lambda ) \triangleq \sum _ { j = 0 } ^ { l } \lambda ^ { j } L _ { j } ^ { \mathbf { T } } } \end{array}$ , and $( V ^ { * } , T ^ { * } , U ^ { * } )$ is a standard triple for $\begin{array} { r } { L ^ { * } ( \lambda ) \triangleq \sum _ { j = 0 } ^ { l } \lambda _ { j } L _ { j } ^ { * } } \end{array}$

PRooF. Apply Theorem 2 to obtain Eq. (8). Then take transposes and apply Theorem 4 to get the first statement. Take conjugate transposes to get the second.

Exercise 6. Let $( U , T , V )$ be a standard triple for $L ( \lambda )$ and show that

$$
U T ^ { j } V = \left\{ { \begin{array} { l l } { { 0 } } & { { \mathrm { i f } j = 0 , 1 , \ldots , l - 2 ; } } \\ { { L _ { l } ^ { - 1 } \phantom { - } } } & { { \mathrm { i f } j = l - 1 . } } \end{array} } \right.\tag{12}
$$

Hint. Examine Eqs. (11). □

The properties in the preceding example can be seen as special cases of the following useful result for standard triples.

Theorem 5. If $( U , T , V )$ is a standard triple for $L ( \lambda ) , S _ { L }$ is the symmetrizer $f o r \dot { L } ( \lambda )$ as defined in Eq. (14.1.7), and matrices Q, R are defined by

$$
Q = \left[ \begin{array} { c } { { U } } \\ { { U T } } \\ { { \vdots } } \\ { { U T ^ { l - 1 } } } \end{array} \right] , R = [ V \quad T V \quad \cdots \quad T ^ { l - 1 } V ] ,\tag{13}
$$

then

$$
R S _ { L } Q = I .\tag{14}
$$

PRoOF. First use Exercise 14.1.6 to write ${ \cal C } _ { L } = S _ { L } ^ { - 1 } { \cal C } _ { 2 } S _ { L }$ (where $C _ { 2 }$ is the second companion matrix for $L ( \lambda ) )$ so that, for $j = 0 , 1 , 2 , \ldots$

$$
C _ { L } ^ { j } R _ { 1 } = S _ { L } ^ { - 1 } C _ { 2 } ^ { j } ( S _ { L } R _ { 1 } ) = S _ { L } ^ { - 1 } C _ { 2 } ^ { j } P _ { 1 } ^ { \mathrm { \scriptscriptstyle T } } .
$$

Now it is easily verified that

$$
[ R _ { 1 } \quad C _ { L } R _ { 1 } \quad \cdots \quad C _ { L } ^ { l - 1 } R _ { 1 } ] = S _ { L } ^ { - 1 } [ P _ { 1 } ^ { \Gamma } \quad C _ { 2 } P _ { 1 } ^ { \Gamma } \quad \cdots \quad C _ { 2 } ^ { l - 1 } P _ { 1 } ^ { \Gamma } ] = S _ { L } ^ { - 1 } .\tag{15}
$$

For any triple $( U , T , V )$ there is a nonsingular S such that $U = { \pmb { P } } _ { 1 } { \pmb { S } } _ { 3 }$ $T = S ^ { - 1 } C _ { L } S .$ and $V = S ^ { - 1 } R _ { 1 }$ . Thus, using Eq. (6),

$$
\boldsymbol { Q } = \left[ \begin{array} { c } { \boldsymbol { P } _ { 1 } } \\ { \boldsymbol { P } _ { 1 } \boldsymbol { C } _ { L } } \\ { \vdots } \\ { \boldsymbol { P } _ { 1 } \boldsymbol { C } _ { L } ^ { l - 1 } } \end{array} \right] \boldsymbol { S } = \boldsymbol { S }
$$

and, using Eq. (15),

$$
R = S ^ { - 1 } [ R _ { 1 } \quad C _ { L } R _ { 1 } \quad \cdot \cdot \quad C _ { L } ^ { l - 1 } R _ { 1 } ] = S ^ { - 1 } S _ { L } ^ { - 1 } .
$$

Thus, $R S _ { L } Q = ( S ^ { - 1 } S _ { L } ^ { - 1 } ) S _ { L } S = I ,$ as required.

## 14.3 The Structure of Jordan Triples

By definition, all standard triples for a matrix polynomial $L ( \lambda )$ with nonsingular leading coefficient are similar to one another in the sense of Eqs. (14.2.4). Thus, there are always standard triples for which the second term, the linearization of L(λ), is in Jordan normal form, J. In this case, a standard $L ( \lambda ) .$ triple (X, J, Y) is called a Jordan triple for L(λ). Similarly, the matrices (X, J) from a Jordan triple are called a Jordan pair for r $L ( \lambda )$ . We will now show that complete spectral information is explicitly given by a Jordan triple.

Let us begin by making a simplifying assumption that will subsequently be dropped. Suppose that $L ( \lambda )$ is an $n \times n$ matrix polynomial of degree l with det $L _ { l } \neq 0$ and with all linear elementary divisors. This means that any Jordan matrix J that is a linearization for $L ( \lambda )$ is diagonal. This is certainly the case if all latent roots of $L ( \lambda )$ are distinct. Write $J = \mathrm { d i a g } [ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { \iota n } ]$

Let $( X , J )$ be a Jordan pair for $L ( \lambda )$ and let $\pmb { x } _ { j } \in \mathbb { C } ^ { n }$ be the jth column of X, for $j = 1 , 2 , \dots , l r$ n. Since a Jordan pair is also a standard pair, it follows from Theorem 14.2.3 that the ln × ln matrix

$$
Q = { \left[ \begin{array} { l } { \ X } \\ { X J } \\ { \ } \\ { \vdots } \\ { X J ^ { \ell - 1 } } \end{array} \right] }\tag{1}
$$

is nonsingular. Also,

$$
L _ { l } X J ^ { l } + \cdot \cdot \cdot + L _ { 1 } X J + L _ { 0 } X = 0 .\tag{2}
$$

First observe that for each $j ,$ the vector $\qquad x _ { j } \neq \pmb \theta ,$ , otherwise $Q$ has a complete column of zeros, contradicting its nonsingularity. Then note that each term in Eq. (2) is an $n \times l n$ matrix; pick out the jth column of each. Since J is assumed to be diagonal, it is found that for $j = 1 , 2 , \dots , l n ,$

$$
L _ { l } \lambda _ { j } ^ { l } x _ { j } + \cdot \cdot \cdot + L _ { 1 } \lambda _ { j } x _ { j } + L _ { 0 } { \bf x } _ { j } = { \bf 0 } .
$$

In other words $L ( \lambda _ { j } ) { \bf x } _ { j } = { \bf \pmb \theta }$ and $\pmb { x } _ { j } \neq \pmb { \theta }$ ; or $\pmb { x } _ { j } \in \operatorname { K e r } L ( \lambda _ { j } )$

Now, the nonzero vectors in Ker $L ( \lambda _ { j } )$ are defined to be the $( r i g h t )$ latent vectors of $L ( \lambda )$ corresponding to the latent root $\lambda _ { j }$ . Thus, when $( X , J )$ is a Jordan pair and J is diagonal, every column of X is a latent vector of $L ( \lambda )$

The general situation, in which J may have blocks of any size between 1 and ln, is more complicated, but it can be described using the same kind of procedure. First it is necessary to generalize the idea of $\hat { \textbf { a } } ^ { 6 6 }$ latent vector" of a matrix polynomial in such a way that it will include the notion of Jordan chains introduced in Section 6.3. Let $L ^ { ( r ) } ( \lambda )$ be the matrix polynomial obtained by differentiating L(λ) r times with respect to $\lambda .$ Thus, when $L ( \lambda )$ has degree l, $L ^ { ( r ) } ( \lambda ) = 0$ for $r > l .$ The set of vectors $\mathbf { x } _ { 0 } , \mathbf { x } _ { 1 } , \ldots , \mathbf { x } _ { k }$ , with $\begin{array} { r } { { \pmb x } _ { 0 } \neq { \pmb \theta } , } \end{array}$ is a Jordan chain of length $k + 1$ for $L ( \lambda )$ corresponding to the latent root $\lambda _ { 0 }$ if the following $k + 1$ relations hold:

$$
\begin{array} { r l r } & { } & { L ( \lambda _ { 0 } ) \boldsymbol { x } _ { 0 } = \boldsymbol { \theta } ; } \\ & { } & \\ & { } & { L ( \lambda _ { 0 } ) \boldsymbol { x } _ { 1 } + \displaystyle \frac { 1 } { 1 ! } L ^ { ( 1 ) } ( \lambda _ { 0 } ) \boldsymbol { x } _ { 0 } = \boldsymbol { \theta } ; } \\ & { } & \\ & { } & { \vdots } \\ & { } & { L ( \lambda _ { 0 } ) \boldsymbol { x } _ { k } + \displaystyle \frac { 1 } { 1 ! } L ^ { ( 1 ) } ( \lambda _ { 0 } ) \boldsymbol { x } _ { k - 1 } + \cdots + \displaystyle \frac { 1 } { k ! } L ^ { ( k ) } ( \lambda _ { 0 } ) \boldsymbol { x } _ { 0 } = \boldsymbol { \theta } . } \end{array}\tag{3}
$$

Observe that $\scriptstyle { \mathbf { 1 } } _ { 0 }$ , the leading vector of the chain, is a latent vector of $L ( \lambda )$ associated with $\lambda _ { 0 }$ , and the successive vectors of the chain each satisfy an inhomogeneous equation with the singular coefficient matrix $L ( \lambda _ { 0 } )$

Exercise 1. Show that if $L ( \lambda ) = \lambda I - T ,$ then this definition of a Jordan chain is consistent with that of Eqs. (6.3.3).

Now we will show that if $( X , J )$ is a Jordan pair of the $n \times n$ matrix polynomial $L ( \lambda )$ , then the columns of $X$ are made up of Jordan chains for $L ( \lambda )$ Let $J = \mathrm { d i a g } [ J _ { 1 } , \dots , J _ { s } ]$ , where $J _ { j }$ is a Jordan block of size $n _ { j } , j = 1 , 2 , \ldots , s .$ Form the partition $X = [ X _ { 1 } \quad { \ ' } X _ { 2 } \quad \cdots \quad X _ { s } ]$ , where $X _ { j }$ is $n \times n _ { j }$ for $j = 1 , 2 , \dots , s ,$ and observe that for $r = 0 , 1 , 2 , \ldots$

$$
X J ^ { r } = [ X _ { 1 } J _ { 1 } ^ { r } \quad X _ { 2 } J _ { 2 } ^ { r } \quad \cdot \cdot \quad X _ { s } J _ { s } ^ { r } ] .
$$

Thus, Eq. (2) implies that, for $j = 1 , 2 , \ldots , s ,$

$$
L _ { l } X _ { j } J _ { j } ^ { l } + \cdot \cdot \cdot + L _ { 1 } X _ { j } J _ { j } + L _ { 0 } X _ { j } = 0 .\tag{4}
$$

Now name the columns of $X _ { j }$ •

$$
X _ { j } = [ { \pmb x } _ { 1 } ^ { j } \mathrm { ~ \pmb ~ { ~ x } } _ { 2 } ^ { j } \mathrm { ~  ~ \cdot ~ } \mathrm { ~ \pmb ~ { ~ \mathscr { ~ x ~ } } ~ } { \pmb x } _ { n _ { j } } ^ { j } ] .
$$

With the convention $\lambda _ { j } ^ { r - p } = 0$ if $r < p ,$ we can write

$$
J _ { j } ^ { r } = \left[ \begin{array} { c c c c c c } { \lambda _ { j } ^ { r } } & { \left( \overset { j } { 1 } \right) \lambda _ { j } ^ { r - 1 } } & { \cdots } & { \left( \begin{array} { c } { j } \\ { n _ { j } - 1 } \end{array} \right) \lambda _ { j } ^ { r - n _ { j } + 1 } } \\ { 0 } & { \lambda _ { j } ^ { r } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \lambda _ { j } ^ { r } } & { \left( \overset { j } { 1 } \right) \lambda _ { j } ^ { r - 1 } } \\ { 0 } & { \cdots } & { 0 } & { \lambda _ { j } ^ { r } } \end{array} \right]
$$

Using the expressions in (4) and examining the columns in the order $1 , 2 , \ldots , n _ { j } ,$ a chain of the form (3) is obtained with $i _ { 2 }$ replaced by $\lambda _ { j }$ , and so on. Thus, for each $j ,$ the columns of $X _ { j }$ form a Jordan chain of length $n _ { j }$ corresponding to the latent root $\lambda _ { j }$

The complete set of Jordan chains generated by $X _ { 1 } , X _ { 2 } , \ldots , X _ { s }$ is said to be a canonical set of Jordan chains for L(λ). The construction of a canonical $L ( \lambda )$ set from a given polynomial $L ( \lambda )$ is easy when J is a diagonal matrix: simply choose any basis of latent vectors in Ker $L ( \lambda _ { j } )$ for each distinct $\lambda _ { j }$ . The construction when J has blocks of general size is more delicate and is left for $J$ more intensive studies of the theory of matrix polynomials. However, an example is analyzed in the first exercise below, which also serves to illustrate the linear dependencies that can occur among the latent vectors and Jordan chains.

Exercise 2. Consider the $2 \times 2$ monic matrix polynomial of degree 2,

$$
L ( \lambda ) = \lambda ^ { 2 } { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] } + \lambda { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { - 1 } \end{array} \right] } + { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} \right] } = { \left[ \begin{array} { l l } { \lambda ^ { 2 } } & { 0 } \\ { \lambda + 1 } & { \lambda ( \lambda - 1 ) } \end{array} \right] } ,
$$

and note that det $L ( \lambda ) = \lambda ^ { 3 } ( \lambda - 1 )$ . Thus, L(λ) has two distinct latent roots: $\lambda _ { 1 } = 0$ and $\lambda _ { 2 } = 1$ . Since

$$
L ( 0 ) = { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} \right] } \qquad { \mathrm { a n d } } \qquad L ( 1 ) = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 2 } & { 0 } \end{array} \right] } ,
$$

any vector of the form [0 $\alpha ] ^ { \boldsymbol { \mathsf { T } } } \left( \alpha \neq 0 \right)$ can be used as a latent vector for $L ( \lambda )$ corresponding to either of the latent roots.

Now observe that the Jordan chain for $L ( \lambda )$ corresponding to the latent root $\lambda _ { 2 } = 1$ has only one member, that is, the chain has length 1. Indeed, if $\mathbf { \pmb { x } } _ { 0 } = [ 0 \quad \alpha ] ^ { \pmb { \tau } }$ and $\alpha \neq 0 ,$ , the equation for $\mathbf { x } _ { 1 }$ is

$$
L ( 1 ) \mathbf { x _ { 1 } } + L ^ { ( 1 ) } ( 1 ) \mathbf { x _ { 0 } } = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 2 } & { 0 } \end{array} \right] } \mathbf { x _ { 1 } } + { \left[ \begin{array} { l l } { 2 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 0 } \\ { \alpha } \end{array} \right] } = { \left[ \begin{array} { l } { 0 } \\ { 0 } \end{array} \right] } ,
$$

which has no solution.

The corresponding equation at the latent root $\lambda _ { 1 } = 0$ is

$$
L ( 0 ) x _ { 1 } + L ^ { ( 1 ) } ( 0 ) x _ { 0 } = { \binom { 0 } { 1 } } x _ { 1 } + { \binom { 0 } { 1 } } x _ { - 1 } ] { \binom { 0 } { \alpha } } = { \binom { 0 } { 0 } } ,
$$

which has the general solution $\mathbf { \pmb { x } } _ { 1 } = [ { \pmb { \alpha } } \quad \beta ] ^ { \pmb { \tau } }$ , where $\beta$ is an arbitrary complex number.

A third member of the chain, $\mathbf { \boldsymbol { x } } _ { 2 }$ , is obtained from the equation

$$
\begin{array} { r l } { { \cal L } ( 0 ) x _ { 2 } + { \cal L } ^ { ( 1 ) } ( 0 ) x _ { 1 } + \frac { 1 } { 2 } { \cal L } ^ { ( 2 ) } ( 0 ) x _ { 0 } = \left[ 0 \right. } & { { 0 } } \\ { { \mathrm { } } } & { { 0 } } \end{array} { }
$$

which gives $\mathbf { x } _ { 2 } = [ - 2 \alpha + \beta \mathbf { \Gamma } \gamma ] ^ { \mathbf { T } }$ for arbitrary γ.

For a fourth member of the chain, we obtain

$$
{ \begin{array} { r l } { L ( 0 ) x _ { 3 } + L ^ { ( 1 ) } ( 0 ) x _ { 2 } + { \frac { 1 } { 2 } } L ^ { ( 2 ) } ( 0 ) x _ { 1 } = { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} \right] } x _ { 3 } + { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { - 1 } \end{array} \right] } { \left[ \begin{array} { l l } { - 2 \alpha + \beta } \\ & { \gamma } \end{array} \right] } } \\ { + { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { \alpha } \\ { \beta } \end{array} \right] } } \\ { = { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} \right] } x _ { 3 } + { \left[ \begin{array} { l l } { \alpha } & { \alpha } \\ { - 2 \alpha + 2 \beta - \gamma } \end{array} \right] } = { \left[ \begin{array} { l } { 0 } \\ { 0 } \end{array} \right] } , } \end{array} }
$$

which has no solution since $\alpha \neq 0$ , whatever value of $\gamma$ may be chosen. Choosing $\alpha = 1 , \beta = \gamma = 0$ , we have a chain

$$
\begin{array} { r } { x _ { 0 } = \bigg [ 0 _ { 1 } \bigg ] , \qquad x _ { 1 } = \bigg [ 0 _ { 0 } \bigg ] , \qquad x _ { 2 } = \bigg [ \begin{array} { c } { - 2 } \\ { 0 } \end{array} \bigg ] , } \end{array}
$$

corresponding to the latent root $\lambda _ { 1 } = 0$

It is easily verified that the matrices

$$
X = { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 1 } & { - 2 } \\ { 1 } & { 1 } & { 0 } & { 0 } \end{array} \right] } , \qquad J = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] }
$$

form a Jordan pair for $L ( \lambda )$

Exercise 3. Find a Jordan pair for the matrix polynomial

$$
L ( \lambda ) = \left[ \begin{array} { c c } { { \lambda ^ { 2 } - 2 \lambda - 2 } } & { { \lambda + 2 } } \\ { { \lambda + 2 } } & { { \lambda ^ { 2 } - 2 \lambda - 2 } } \end{array} \right] .
$$

Hint. First confirm that $\sigma ( L ) = \{ - 1 , 0 , 1 , 4 \}$

Exercise 4. As in Exercise 14.1.5, let

$$
L ( \lambda ) = \left[ \begin{array} { c c } { { \lambda ^ { 2 } } } & { { - \lambda } } \\ { { 0 } } & { { \lambda ^ { 2 } } } \end{array} \right] .
$$

Verify that

$$
X = { \left[ \begin{array} { l l l l } { 0 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 1 } & { 0 } \end{array} \right] } , \qquad J = { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] }
$$

is a Jordan pair for $L ( \lambda )$

Exercise 5. Find a Jordan pair for each of the scalar polynomials $L _ { 1 } ( \lambda ) =$ $( \lambda - \lambda _ { 0 } ) ^ { l }$ and $L _ { 2 } ( \lambda ) = ( \lambda - \lambda _ { 1 } ) ^ { p } ( \lambda - \lambda _ { 2 } ) ^ { q }$ , where $\lambda _ { 1 } \neq \lambda _ { 2 }$ and $p , q$ are positive integers.

Now suppose that $( X , J , Y )$ is a Jordan triple for L(λ). The roles of X and J are understood, but what about the matrix Y? Its interpretation in terms of spectral data can be obtained from Corollary 14.2.1, which says that $( Y ^ { \mathsf { T } } , J ^ { \mathsf { T } } , X ^ { \mathsf { T } } )$ is a standard triple for $L ^ { \operatorname { T } } ( \lambda )$ . Note that this is not a Jordan triple, because the linearization $J ^ { \boldsymbol { \mathsf { T } } }$ is the transpose of a Jordan form and so is not, in general, in Jordan form itself. To transform it to Jordan form we introduce the matrix

$$
P = \mathrm { d i a g } [ P _ { 1 } , P _ { 2 } , . . . , P _ { s } ] ,
$$

where $P _ { j }$ is the $n _ { j } \times n _ { j }$ rotation matrix:

$$
P _ { j } = { \left[ \begin{array} { l l l l } { 0 } & { \cdots } & { 0 } & { 1 } \\ { \vdots } & { \cdots } & { \cdot } & { 1 } & { 0 } \\ { 0 } & { 1 } & { \cdot } & { \cdot } & { \vdots } \\ { 1 } & { 0 } & { \cdots } & { 0 } \end{array} \right] } .
$$

(Recall that $J = \mathrm { d i a g } [ J _ { 1 } , \dots , J _ { s } ]$ , where $J _ { j }$ has size $n _ { j } . )$ Note that $P ^ { 2 } = I$ (so that $P ^ { - 1 } = P )$ and $P ^ { * } = P$ . It is easily verified that for each j, $P _ { j } J _ { j } ^ { \mathrm { T } } P _ { j } = J _ { j }$ and hence that $P J ^ { \boldsymbol { \mathsf { T } } } P = J$ . Now the similarity transformation

$$
Y ^ { \mathrm { T } } P , \qquad J = P J ^ { \mathrm { T } } P , \qquad P X ^ { \mathrm { T } }
$$

of $( Y ^ { \boldsymbol { \mathsf { T } } } , J ^ { \boldsymbol { \mathsf { T } } } , X ^ { \boldsymbol { \mathsf { T } } } )$ yields a standard triple for $L ^ { \operatorname { T } } ( \lambda )$ in which the middle term is in Jordan form. Thus, $( Y ^ { \mathsf { T } } P , J , P X ^ { \mathsf { T } } )$ is a Jordan triple for $L ^ { \operatorname { T } } ( \lambda )$ , and our

discussion of Jordan pairs can be used to describe Y. Thus, let Y be partitioned in the form

$$
Y = { \left[ \begin{array} { l } { Y _ { 1 } } \\ { Y _ { 2 } } \\ { \vdots } \\ { Y _ { s } } \end{array} \right] } ,
$$

where $Y _ { j }$ is $n _ { j } \times n$ for $j = 1 , 2 , \dots , s .$ Then $\boldsymbol { Y } ^ { \mathrm { T } } \boldsymbol { P } = [ Y _ { 1 } ^ { \mathrm { T } } \boldsymbol { P } _ { 1 } \quad \cdot \cdot \cdot \quad Y _ { s } ^ { \mathrm { T } } \boldsymbol { P } _ { s } ]$ , and it follows that, for each $j ,$ the transposed rows of $Y _ { j }$ taken in reverse order form a Jordan chain of $L ^ { \mathbb { T } } ( \lambda )$ of length $n _ { j }$ corresponding to $\lambda _ { j }$

These Jordan chains are called left Jordan chains of $L ( \lambda ) ,$ and left latent vectors of $L ( \lambda )$ are the nonzero vectors in Ker $L ^ { \mathsf { T } } ( \lambda _ { j } ) , j = 1 , 2 , \ldots , \bar { s } .$ Thus, the leading members of left Jordan chains are left latent vectors.

Exercise 6. (a) Let $\ b { A } \in \mathbb { C } ^ { n \times n }$ and assume $A$ has only linear elementary divisors. Use Exercises 4.14.3 and 4.14.4 to show that right and left eigenvectors of A can be defined in such a way that the resolvent of $A$ has the spectral representation

$$
( \lambda I - A ) ^ { - 1 } = \sum _ { j = 1 } ^ { n } { \frac { x _ { j } y _ { j } ^ { \operatorname { T } } } { \lambda - \lambda _ { j } } } .
$$

(b) Let $L ( \lambda )$ be an $n \times n$ matrix polynomial of degree l with det $L _ { l } \neq 0$ and only linear elementary divisors. Show that right and left latent vectors for $L ( \lambda )$ can be defined in such a way that

$$
L ( \lambda ) ^ { - 1 } = \sum _ { j = 1 } ^ { l n } \frac { x _ { j } y _ { j } ^ { \operatorname { T } } } { \lambda - \lambda _ { j } } .
$$

Exercise 7. Suppose that $\lambda _ { j } \in \sigma ( L )$ has just one associated Jordan block $J _ { j }$ , and the size of $J _ { j }$ is v. Show that the singular part of the Laurent expansion for $L ^ { - 1 } ( \lambda )$ about $\lambda _ { j }$ can be written in the form

$$
\sum _ { k = 1 } ^ { \nu } \sum _ { r = 0 } ^ { \nu - k } \frac { \mathbf { x } _ { \nu - k - r } \mathbf { y } _ { r } ^ { \mathsf { T } } } { ( \lambda - \lambda _ { j } ) ^ { k } }
$$

for some right and left Jordan chains $\{ \pmb { x } _ { 1 } , \ldots , \pmb { x } _ { \nu } \}$ and $\{ \pmb { y } _ { 1 } , \ldots , \pmb { y } _ { \nu } \}$ , respectively (see Exercise 9.5.2).

Hint. First observe that

$$
( \lambda I - J _ { j } ) ^ { - 1 } = [ { \begin{array} { c c c c } { ( \lambda - \lambda _ { j } ) ^ { - 1 } } & { ( \lambda - \lambda _ { j } ) ^ { - 2 } } & { \cdots } & { ( \lambda - \lambda _ { j } ) ^ { - \upsilon } } \\ { 0 } & { ( \lambda - \lambda _ { j } ) ^ { - 1 } } & { \ddots } & { \vdots } \\ & & { \ddots } & { \ddots } & { \vdots } \\ & & & { ( \lambda - \lambda _ { j } ) ^ { - 1 } } & { ( \lambda - \lambda _ { j } ) ^ { - 2 } } \\ { 0 } & { \cdots } & { 0 } & { ( \lambda - \lambda _ { j } ) ^ { - 1 } } \end{array} } ] . \quad \boxed { \begin{array} { c c c c } { \boxed { ( \lambda - \lambda _ { j } ) ^ { - 1 } } } & { } & { \boxed { ( \lambda - \lambda _ { j } ) ^ { - 1 } } } & { } \\ { \vdots } & { } & { \ddots } & { \vdots } \\ { \vdots } & { } & { \ddots } & { ( \lambda - \lambda _ { j } ) ^ { - 1 } } & { \vdots } \\ { \end{array} } } \quad { \begin{array} { c c c c } { \boxed { ( \lambda - \lambda _ { j } ) ^ { - 1 } } } & { } & { \boxed { ( \lambda - \lambda _ { j } ) ^ { - 1 } } } & { } \\ { \vdots } & { } & { \vdots } & { \ddots } \\ { ( \lambda - \lambda _ { j } ) ^ { - 1 } } & { } & { ( \lambda - \lambda _ { j } ) ^ { - 1 } } \end{array} } ] .
$$

## 14.4 Applications to Differential Equations

Consider the constant-coefficient-matrix differential equation of order l given by

$$
L _ { l } { \pmb x } ^ { ( l ) } ( t ) + L _ { l - 1 } { \pmb x } ^ { ( l - 1 ) } ( t ) + \dots + L _ { 1 } { \pmb x } ^ { ( 1 ) } ( t ) + L _ { 0 } { \pmb x } ( t ) = { \pmb f } ( t ) ,\tag{1}
$$

where $L _ { 0 } , L _ { 1 } , \dots , L _ { l } \in \mathbb { C } ^ { n \times n }$ , det $L _ { l } \neq 0 ;$ , and the indices on x denote derivatives with respect to the independent variable t. The vector function $f ( t )$ has values in $\mathbb { C } ^ { n } .$ , is piecewise continuous, and supposed given; $\mathbf { \boldsymbol { x } } ( t )$ is to be found. The equation is inhomogeneous when $\begin{array} { r } { f ( t ) \neq \pmb { \theta } , } \end{array}$ and the equation

$$
L _ { l } { \mathbf { } x } ^ { ( l ) } ( t ) + \cdots + L _ { 1 } { \mathbf { } x } ^ { ( 1 ) } ( t ) + L _ { 0 } { \mathbf { } x } ( t ) = { \boldsymbol { 0 } }\tag{2}
$$

is said to be homogeneous and has already been introduced in Section 7.10. Recall the discussion in that section of the space ${ \mathcal { C } } ( \mathbb { C } ^ { n } )$ of all continuous vector-valued functions $\pmb { x } ( t )$ defined for real t with values in $\mathbb { C } ^ { n }$ We now discuss the relationship between Jordan chains of $L ( \lambda )$ and primitive solutions from ${ \mathcal { C } } ( \mathbb { C } ^ { n } )$ of the homogeneous Eq. (2).

Observe first that if $\lambda _ { 0 }$ is a latent root of $L ( \lambda )$ with latent vector $\mathbf { x _ { 0 } }$ , so that $L ( \lambda _ { 0 } ) { \bf x } _ { 0 } = { \bf \nabla } \theta ,$ then Eq. (2) has a solution $\pmb { x } _ { 0 } e ^ { \lambda _ { 0 } t }$ , and conversely. This is because

$$
\cdot \qquad { \biggl ( } { \frac { d } { d t } } { \biggr ) } ^ { j } ( x _ { 0 } e ^ { \lambda _ { 0 } t } ) = \lambda _ { 0 } ^ { j } x _ { 0 } e ^ { \lambda _ { 0 } t } ,
$$

so that

$$
L \left( { \frac { d } { d t } } \right) \left( x _ { 0 } e ^ { \lambda _ { 0 } t } \right) = \sum _ { j = 0 } ^ { l } L _ { j } \left( { \frac { d } { d t } } \right) ^ { j } ( x _ { 0 } e ^ { \lambda _ { 0 } t } ) = L ( \lambda _ { 0 } ) x _ { 0 } = \theta .
$$

Now suppose that $\mathbf { x _ { 0 } } , \mathbf { x _ { 1 } }$ are two leading members of a Jordan chain of $L ( \lambda )$ associated with the latent root $\lambda _ { 0 }$ . We claim that

$$
u _ { 0 } ( t ) = x _ { 0 } e ^ { \lambda _ { 0 } t } \qquad \mathrm { a n d } \qquad u _ { 1 } ( t ) = ( t x _ { 0 } + x _ { 1 } ) e ^ { \lambda _ { 0 } t }
$$

are linearly independent solutions of Eq. (2). We have already seen that the first function is a solution. Also, the first function obviously satisfies

$$
\bigg ( \frac { d } { d t } - \lambda _ { 0 } I \bigg ) u _ { 0 } ( t ) = 0 .\tag{3}
$$

Now observe that, for the second function,

$$
\left( { \frac { d } { d t } } - \lambda _ { 0 } I \right) ( t x _ { 0 } + x _ { 1 } ) e ^ { \lambda _ { 0 } t } = x _ { 0 } e ^ { \lambda _ { 0 } t } .
$$

In other words,

$$
\bigg ( \frac { d } { d t } - \lambda _ { 0 } I \bigg ) \pmb { \mu } _ { 1 } ( t ) = \pmb { \mu } _ { 0 } ( t ) ,
$$

so that, using Eq. (3),

$$
\Biggl ( \frac { d } { d t } - \lambda _ { 0 } I \Biggr ) ^ { 2 } u _ { 1 } ( t ) = 0 .\tag{4}
$$

Let us represent the differential operator $L ( d / d t )$ in terms of $( d / d t ) \mathrm { ~ - ~ } \lambda _ { 0 } I .$ To do this, first write the Taylor expansion for $L ( \lambda )$ about $\lambda _ { 0 }$

$$
L ( \lambda ) = L ( \lambda _ { 0 } ) + \frac { 1 } { 1 ! } L ^ { ( 1 ) } ( \lambda _ { 0 } ) ( \lambda - \lambda _ { 0 } ) + \cdots + \frac { 1 } { l ! } L ^ { ( l ) } ( \lambda _ { 0 } ) ( \lambda - \lambda _ { 0 } ) ^ { l } .
$$

It follows that

$$
L \left( \frac { d } { d t } \right) = L ( \lambda _ { 0 } ) + \frac { 1 } { 1 ! } L ^ { ( 1 ) } ( \lambda _ { 0 } ) \left( \frac { d } { d t } - \lambda _ { 0 } I \right) + \cdots + \frac { 1 } { l ! } L ^ { ( l ) } ( \lambda _ { 0 } ) \left( \frac { d } { d t } - \lambda _ { 0 } I \right) ^ { l } .\tag{5}
$$

Now Eq. (4) implies that

$$
\begin{array} { r } { \bigg ( \displaystyle \frac { d } { d t } - \lambda _ { 0 } I \bigg ) ^ { j } \pmb { \mathscr { u } } _ { 1 } ( t ) = \pmb { \mathscr { 0 } } , \qquad j = 2 , 3 , \ldots . } \end{array}
$$

Thus

$$
\begin{array} { l } { { \displaystyle { \cal L } \biggl ( \frac { d } { d t } \biggr ) u _ { 1 } ( t ) = { \cal L } ( \lambda _ { 0 } ) u _ { 1 } ( t ) + \frac { 1 } { 1 ! } { \cal L } ^ { ( 1 ) } ( \lambda _ { 0 } ) u _ { 0 } ( t ) } } \\ { ~ } \\ { { ~ = ( { \cal L } ( \lambda _ { 0 } ) { \bf x } _ { 0 } ) t e ^ { \lambda _ { 0 } t } + \biggl ( { \cal L } ( \lambda _ { 0 } ) { \bf x } _ { 1 } + \frac { 1 } { 1 ! } { \cal L } ^ { ( 1 ) } ( \lambda _ { 0 } ) { \bf x } _ { 0 } \biggr ) e ^ { \lambda _ { 0 } t } } } \\ { { ~ = \theta , } } \end{array}
$$

using the first two relations of Eqs. (14.3.3), which define a Jordan chain. Thus ${ \pmb u } _ { 1 } ( t )$ is also a solution of Eq. (2)

To see that ${ \pmb u } _ { 0 } ( t )$ and ${ \pmb u } _ { 1 } ( t )$ are linearly independent functions of t, observe the fact that $\alpha { \pmb u } _ { 0 } ( t ) + \beta { \pmb u } _ { 1 } ( t ) = 0$ for all t implies

$$
t ( \alpha { \pmb x } _ { 0 } ) + ( \alpha { \pmb x } _ { 1 } + \beta { \pmb x } _ { 0 } ) = { \pmb \theta } .
$$

Since this is true for all t we must have $\alpha = 0$ ,and the equation reduces to $\beta \mathbf { x } _ { 0 } = \pmb { \theta } .$ Therefore $\beta = 0$ since $\pmb { x _ { 0 } } \neq \pmb { \theta } .$ Hence ${ \pmb u } _ { 0 } ( t )$ and ${ \pmb u } _ { 1 } ( t )$ are linearly independent.

The argument we have just completed cries out for generalization to a sequence of functions ${ \pmb u } _ { 0 } ( t ) , { \pmb u } _ { 1 } ( t ) , \ldots , { \pmb u } _ { k - 1 } ( t )$ , where $\pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \ldots , \pmb { x } _ { k - 1 }$ is a Jordan chain and

$$
u _ { 2 } ( t ) = \bigg ( \frac { 1 } { 2 ! } t ^ { 2 } x _ { 0 } + t x _ { 1 } + x _ { 2 } \bigg ) e ^ { \lambda _ { 0 } t } ,
$$

and so on. It is left as an exercise to complete this argument and to prove the next result.

Theorem 1. Let $\pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \ldots , \pmb { x } _ { k - 1 }$ be a Jordan chain for $L ( \lambda )$ at $\lambda _ { 0 }$ . Then the k functions

$$
\begin{array} { c } { { \displaystyle { u _ { 0 } ( t ) = x _ { 0 } e ^ { \lambda _ { 0 } t } } , } } \\ { { \displaystyle { u _ { 1 } ( t ) = ( t x _ { 0 } + x _ { 1 } ) e ^ { \lambda _ { 0 } t } } , } } \\ { { \vdots } } \\ { { \displaystyle { u _ { k - 1 } ( t ) = \left( \sum _ { j = 0 } ^ { k - 1 } \frac { t ^ { j } } { j ! } x _ { k - 1 - j } \right) e ^ { \lambda _ { 0 } t } } } } \end{array}\tag{6}
$$

are linearly independent solutions of Eq. (2).

There is also a converse statement.

Theorem 2. Let $\mathbf { x } _ { 0 } , \mathbf { x } _ { 1 } , \ldots , \mathbf { x } _ { k - 1 } \in \mathbb { C } ^ { n }$ with $\mathbf { \boldsymbol { x } } _ { 0 } \neq \mathbf { \boldsymbol { 0 } } .$ If the vector-valued function

$$
u _ { k - 1 } ( t ) = \left( { \frac { t ^ { k - 1 } } { ( k - 1 ) ! } } x _ { 0 } + \cdots + t x _ { k - 2 } + x _ { k - 1 } \right) e ^ { \lambda _ { 0 } t }
$$

is a solution of Eq. (2), then $\lambda _ { 0 }$ is a latent root of $L ( \lambda )$ and $\pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \ldots , \pmb { x } _ { k - 1 }$ is $^ { a }$ Jordan chain for $L ( \lambda )$ corresponding to $\lambda _ { 0 }$

PROOF. Let functions ${ \pmb u } _ { 0 } ( t ) , \dots , { \pmb u } _ { k - 2 } ( t )$ be defined as in Eqs. (6) and, for convenience, let ${ \pmb u } _ { i } ( t )$ be identically zero if $i = - 1 , - 2 , \dots { . }$ It is found (see Eqs. (3) and (4)) that

$$
\left( \frac { d } { d t } - \lambda _ { 0 } I \right) ^ { j } u _ { k - 1 } ( t ) = u _ { k - j - 1 } ( t ) ,
$$

for $j = 0 , 1 , 2 , \ldots$ Using the expansion (5),

$$
\begin{array} { l } { { \displaystyle \theta = L \bigg ( \frac { d } { d t } \bigg ) u _ { k - 1 } ( t ) } } \\ { { } } \\ { { \displaystyle \quad = L ( \lambda _ { 0 } ) u _ { k - 1 } ( t ) + L ^ { ( 1 ) } ( \lambda _ { 0 } ) u _ { k - 2 } ( t ) + \cdots + \frac { 1 } { l ! } L ^ { ( l ) } ( \lambda _ { 0 } ) u _ { k - l - 1 } ( t ) . } } \end{array}
$$

Now the function $e ^ { \lambda _ { 0 } t }$ can be cancelled from this equation. Equating the vector coefficients of powers of t to zero in the remaining equation, the relations (14.3.3) are obtained and since we assume $\mathbf { \boldsymbol { x } } _ { 0 } \neq \mathbf { \boldsymbol { \theta } }$ we see that $\lambda _ { 0 }$ is a latent root of $L ( \lambda )$ and $\pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \ldots , \pmb { x } _ { k - 1 }$ is a corresponding Jordan chain.

Exercise 1. Complete the proof of Theorem 1.

Exercise 2. Use Theorem 1 and the results of Exercise 14.3.2 to find four linearly independent solutions of the system of differential equations

$$
\frac { d ^ { 2 } x _ { 1 } } { d t ^ { 2 } } = 0 ,
$$

$$
{ \frac { d ^ { 2 } x _ { 2 } } { d t ^ { 2 } } } + { \frac { d x _ { 1 } } { d t } } - { \frac { d x _ { 2 } } { d t } } + x _ { 1 } = 0 .
$$

SoLUTION Written in the form of Eq. (2), where $\mathbf { x } = [ x _ { 1 } \quad x _ { 2 } ] ^ { \mathbf { T } }$ , we have

$$
{ \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] } { \boldsymbol { x } } ^ { ( 2 ) } ( t ) + { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { - 1 } \end{array} \right] } { \boldsymbol { x } } ^ { ( 1 ) } ( t ) + { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} \right] } { \boldsymbol { x } } ( t ) = { \boldsymbol { \theta } } .\tag{7}
$$

So the associated matrix polynomial is $L ( \lambda )$ of Exercise 14.3.2.

There is a latent root $\lambda _ { 1 } = 1$ with latent vector ${ \begin{array} { r l } \end{array} } [ 0  &  { } 1 ] ^ { \mathtt { T } }$ , hence one solution is

$$
v _ { 0 } ( t ) = { \binom { 7 } { 1 } } e ^ { t } .
$$

Then there is the latent root $\lambda _ { 2 } = 0$ with Jordan chain $[ 0 \quad 1 ] ^ { \mathbf { T } } , [ 1 \quad 0 ] ^ { \mathbf { T } }$ $[ - 2 \ \mathbf { \Lambda } 0 ] ^ { \mathbf { r } }$ , and there are three corresponding linearly independent solutions:

$$
\begin{array} { r } { u _ { 0 } ( t ) = \small \left[ 0 \atop 1 \right] , \qquad u _ { 1 } ( t ) = \small \left[ 1 \atop t \right] , \qquad u _ { 2 } ( t ) = \small \left[ { - 2 + t } \atop { \frac { 1 } { 2 } t ^ { 2 } } \right] . } \end{array}
$$

It is easily verified that $\{ \pmb { v } _ { 0 } ( t ) , \pmb { u } _ { 0 } ( t ) , \pmb { u } _ { 1 } ( t ) , \pmb { v } _ { 2 } ( t ) \}$ is a linearly independent set of vector-valued functions in ${ \mathcal { C } } ( \mathbb { C } ^ { 2 } )$ . Furthermore, it follows from Theorem 7.10.1 that they form a basis for the solution space of Eq. (7). □

## 14.5 General Solutions of Differential Equations

Results obtained in the preceding section are natural generalizations of Proposition 9.10.1. Indeed, this line of investigation can be pursued further to generalize Theorem 9.10.1 and show that the ln-dimensional solution space of Eq. (14.4.2) (see Theorem 7.10.1) can be spanned by linearly independent vector functions defined (as in Theorem 14.4.1) in terms of all latent roots and a canonical set of Jordan chains. The completion of this argument is indicated in Exercise 2 of this section. But first we turn our attention to the question of general solutions of initial-value problems in the spirit of Theorems 9.10.4 and 9.10.5. Our main objective is to show how a general solution of Eq. (14.4.1) can be expressed in terms of any standard triple for L(λ).

Consider first the idea of linearization of Eq. (14.4.1), or of Eq. (14.4.2), as used in the theory of differential equations. Functions $\mathbf { x } _ { 0 } ( t ) , \ldots , \mathbf { x } _ { l - 1 } ( t )$ are defined in terms of a solution function x(t) and its derivatives by

$$
\pmb { x } _ { 0 } ( t ) = \pmb { x } ( t ) , \qquad \pmb { x } _ { 1 } ( t ) = \pmb { x } ^ { ( 1 ) } ( t ) , \dots , \pmb { x } _ { l - 1 } ( t ) = \pmb { x } ^ { ( l - 1 ) } ( t ) .\tag{1}
$$

Then Eq. (14.4.1) takes the form

$$
L _ { l } \frac { d { \bf x } _ { l - 1 } ( t ) } { d t } + L _ { l - 1 } { \bf x } _ { l - 1 } ( t ) + \cdots + L _ { 0 } { \bf x } _ { 0 } ( t ) = f ( t ) .\tag{2}
$$

If we define

$$
\tilde { \mathbf { x } } ( t ) = \left[ \begin{array} { c } { \mathbf { x } _ { 0 } ( t ) } \\ { \mathbf { x } _ { 1 } ( t ) } \\ { \vdots } \\ { \mathbf { x } _ { l - 1 } ( t ) } \end{array} \right] , \qquad \mathbf { \pmb { g } } ( t ) = \left[ \begin{array} { c } { \mathbf { 0 } } \\ { \vdots } \\ { \mathbf { 0 } } \\ { L _ { l } ^ { - 1 } \pmb { f } ( t ) } \end{array} \right] ,\tag{3}
$$

and let $C _ { L }$ be the now-familiar companion matrix for L(λ), Eqs. (1) and (2) can be condensed to the form

$$
\frac { d \tilde { { \mathbf { x } } } ( t ) } { d t } = C _ { L } \tilde { { \mathbf { x } } } ( t ) + { \mathbf { \mathbf { \mathit { g } } } } ( t ) .\tag{4}
$$

In fact, it is easily verified that Eqs. (1), (2), and (3) determine a one-to-one correspondence between the solutions x(t) of Eq. (14.4.1) and x(t) of Eq. (4). Thus, the problem is reduced from order l to order 1 in the derivatives, but at the expense of increasing the size of the vector variable from l to ln and, of course, at the expense of a lot of redundancies in the matrix $C _ { L }$

However, we take advantage of Theorem 9.10.5 and observe that every solution of Eq. (4) has the form

$$
\tilde { x } ( t ) = e ^ { C _ { L } t } z + \int _ { 0 } ^ { t } e ^ { C _ { L } ( t - \tau ) } g ( \tau ) d \tau ,
$$

for some $z \in \mathbb { C } ^ { l n }$ . Now recall the definitions (14.2.2) of matrices $P _ { 1 }$ and $R _ { 1 }$ in the standard triple $( P _ { 1 } , C _ { L } , R _ { 1 } )$ for $L ( \lambda )$ . Noting that $P _ { 1 } \tilde { \mathbf { x } } ( t ) = \mathbf { x } ( t )$ , it is found that, multiplying the last equation on the left by $P _ { 1 }$

$$
\begin{array} { l } { \displaystyle { \pmb x ( t ) = P _ { 1 } e ^ { C _ { L } t } \pmb z + P _ { 1 } \int _ { 0 } ^ { t } e ^ { C _ { L } ( t - \tau ) } R _ { 1 } { \pmb f } ( \tau ) d \tau . } } \end{array}\tag{5}
$$

We have now proved the following result.

## Lemma 1. Every solution of Eq. (14.4.1) has the form (5) for some $z \in \mathbb { C } ^ { t n } .$ L

Note that this lemma achieves the preliminary objective of expressing all solutions of Eq. (14.4.1) in terms of the standard triple $( P _ { 1 } , C _ { L } , R _ { 1 } )$ . Also, the general solution of Eq. (14.4.2) is obtained from Eq. (4) on setting $\pmb { f } ( t ) \equiv \pmb { \theta } .$

The step from the lemma to our main result is a small one.

Theorem 1. Let $( U , T , V )$ be a standard triple for $L ( \lambda )$ . Then every solution of Eq. (14.4.1) has the form

$$
{ \boldsymbol { x } } ( t ) = U e ^ { T t } { \boldsymbol { z } } + U \int _ { 0 } ^ { t } e ^ { T ( t - \tau ) } V f ( \tau ) d \tau ,\tag{6}
$$

for some $z \in \mathbb { C } ^ { l n }$

ProoF. Recall that, from the definition of a standard triple (see the proof of Theorem 14.2.2), there is a nonsingular $\pmb { S } \in \mathbb { C } ^ { i n \times i n }$ such that

$$
P _ { 1 } = U S , \qquad C _ { L } = S ^ { - 1 } T S , \qquad R _ { 1 } = S ^ { - 1 } V
$$

Also, using Theorem 9.4.2, $e ^ { C _ { L } \alpha } = S ^ { - 1 } e ^ { T \alpha } S$ for any $\alpha \in \mathbb { R }$ Consequently,

$$
P _ { 1 } e ^ { C _ { L } \alpha } = U e ^ { T \alpha } S , ~ P _ { 1 } e ^ { C _ { L } \alpha } R _ { 1 } = U e ^ { T \alpha } V .
$$

Substitution of these expressions into Eq. (5) with $\alpha = t$ concludes the proof.

In practice there are two important candidates for the triple $( U , T , V )$ of the theorem. The first is the triple $( P _ { 1 } , C _ { L } , R _ { 1 } )$ , as used in the lemma that expresses the general solution in terms of the coefficients of the differential equation. The second is a Jordan triple $( X , J , Y )$ , in which case the solution is expressed in terms of the spectral properties of $L ( \lambda )$ . The latter choice of triple is, of course, intimately connected to the ideas of the preceding section.

Exercise 1. Suppose that, in Eq. (14.4.1),

$$
f ( t ) = \left\{ \begin{array} { l l } { f _ { 0 } } & { \quad \mathrm { f o r } \quad t \geq 0 , } \\ { \pmb { \theta } } & { \quad \mathrm { f o r } \quad t < 0 . } \end{array} \right.
$$

Let $L _ { 0 }$ be nonsingular and $\mathcal { R } \lambda < 0$ for every $\lambda \in \sigma ( L )$ . Show that the solution $\pmb { x } ( t )$ satisfies

$$
\operatorname * { l i m } _ { t  \infty } \mathbf { x } ( t ) = L _ { 0 } ^ { - 1 } f _ { 0 } .
$$

Exercise 2. Let $( X , J )$ be a Jordan pair for the matrix polynomial L(λ) associated with Eq. (14.1.2). Show that every solution of that equation has

the form $\mathbf { \boldsymbol { x } } ( t ) = X e ^ { J t } \mathbf { \boldsymbol { z } }$ for some $z \in \mathbb { C } ^ { l n }$ . Hence show that the solution space has a basis of ln functions of the form described in Theorem 14.4.1.

Theorem 1 can be used to give an explicit representation for the solution of a classical initial-value problem.

Theorem 2. Let $( U , T , V )$ be a standard triple for L(λ). Then there is a unique solution of the differential equation (14.4.1) satisfying initial conditions

$$
\begin{array} { r } { { \pmb x } ^ { ( j ) } ( 0 ) = { \pmb x } _ { j } , \qquad j = 0 , 1 , \ldots , l - 1 , } \end{array}\tag{7}
$$

for any given vectors $\mathbf { x } _ { 0 } , \mathbf { x } _ { 1 } , \ldots , \mathbf { x } _ { l - 1 } \in \mathbb { C } ^ { n } ,$ This solution is given by Eq. (6) with

$$
\boldsymbol { z } = [ V \quad T V \quad \cdots \quad T ^ { l - 1 } . V ] S _ { L } \left[ \begin{array} { c } { \boldsymbol { x } _ { 0 } } \\ { \vdots } \\ { \boldsymbol { x } _ { l - 1 } } \end{array} \right] ,\tag{8}
$$

where $S _ { L }$ is the symmetrizer for $L ( \lambda )$

PRoOF. We first verify that the function $\mathbf { \boldsymbol { x } } ( t )$ given by Eqs. (6) and (8) does, indeed, satisfy the initial conditions (7). Differentiating Eq. (6), it is found that

$$
\left[ \begin{array} { c } { { \pmb x } ( 0 ) } \\ { { \pmb x } ^ { ( 1 ) } ( 0 ) } \\ { \vdots } \\ { { \pmb x } ^ { ( l - 1 ) } ( 0 ) } \end{array} \right] = \left[ \begin{array} { c } { { U } } \\ { { U T } } \\ { \vdots } \\ { { U T } ^ { l - 1 } } \end{array} \right] z = Q z ,\tag{9}
$$

in the notation of Eq. (14.2.13). But the result of Theorem 14.2.5 implies that $Q R S _ { L } = I ,$ and so substitution of z from Eq. (8) into Eq. (9) shows that x(t) defined in this way satisfies the initial conditions.

Finally, the uniqueness of z follows from Eq. (9) in view of the invertibility of Q.

## 14.6 Difference Equations

Consider the constant-coefficient-matrix difference equation of order l given by

$$
L _ { l } \pmb { x } _ { j + l } + L _ { l - 1 } \pmb { x } _ { j + l - 1 } + \cdots + L _ { 1 } \pmb { x } _ { j + 1 } + L _ { 0 } \pmb { x } _ { j } = f _ { j } , \qquad j = 0 , 1 , \ldots ,\tag{1}
$$

where $L _ { 0 } , L _ { 1 } , \dots , L _ { l } \in \mathbb { C } ^ { n \times n } ,$ det $L _ { l } \neq 0 ,$ the sequence $\pmb { f } = ( \pmb { f } _ { 0 } , \pmb { f } _ { 1 } , \dots )$ of vectors in $\mathbb { C } ^ { n }$ is given, and a sequence ${ \pmb x } = ( { \pmb x } _ { 0 } , { \pmb x } _ { 1 } , \dots )$ , called a solution of Eq. (1), is to be found.

The theory of difference equations is analogous to that of differential equations developed in the previous sections, and therefore some of the proofs and technicalities are omitted from this presentation.

The following results are analogues of Theorems 14.4.1 and 14.4.2 for the homogeneous difference equation

$$
L _ { l } { \bf x } _ { j + l } + L _ { l + 1 } { \bf x } _ { j + l - 1 } + \cdots + L _ { 1 } { \bf x } _ { j + 1 } + L _ { 0 } { \bf x } _ { j } = \theta , \mathrm { ~ } j = 0 , 1 , \ldots ,\tag{2}
$$

associated with the matrix polynomial $\begin{array} { r } { L ( \lambda ) = \sum _ { j = 0 } ^ { l } \lambda ^ { j } L _ { j } } \end{array}$ , where det $L _ { l } \neq 0 .$ Once again, we recall the discussion and result of Section 7.10 concerning the homogeneous equation. In particular, recall that ${ \mathcal { S } } ( \mathbb { C } ^ { n } )$ denotes the linear space of infinite sequences of vectors from $\mathbb { C } ^ { n } .$ Here, it is convenient to define “binomial” coefficients ${ \binom { j } { r } } \triangleq 0$ for integers $j , r$ with $j < r .$

Theorem 1. $I f { \pmb x } _ { 0 } , { \pmb x } _ { 1 } , \ldots , { \pmb x } _ { k - 1 }$ is a Jordan chain for $L ( \lambda )$ corresponding to $\lambda _ { 0 }$ , then the k sequences $( \pmb { u } _ { 0 } ^ { ( s ) } , \pmb { u } _ { 1 } ^ { ( s ) } , . . . ) \in \mathcal { S } ( \mathbb { C } ^ { n } ) , s = 0 , 1 , . . . , k - 1$ , with

$$
\begin{array} { r l r } {  { { \boldsymbol u } _ { j } ^ { ( 0 ) } = \lambda _ { 0 } ^ { j } { \boldsymbol x } _ { 0 } } } \\ & { } & \\ & { } & { { \boldsymbol u } _ { j } ^ { ( 1 ) } = ( \begin{array} { l } { j } \\ { 1 } \end{array} ) \lambda _ { 0 } ^ { j - 1 } { \boldsymbol x } _ { 0 } + \lambda _ { 0 } ^ { j } { \boldsymbol x } _ { 1 } , } \\ & { \vdots } \\ & { } & \\ { { \boldsymbol u } _ { j } ^ { ( k - 1 ) } = ( \begin{array} { c } { j } \\ { k - 1 } \end{array} ) \ \lambda _ { 0 } ^ { j - k + 1 } { \boldsymbol x } _ { 0 } + ( \begin{array} { c } { j } \\ { k - 2 } \end{array} ) \lambda _ { 0 } ^ { j - k + 2 } { \boldsymbol x } _ { 1 } + \dots + ( \begin{array} { c } { j } \\ { 1 } \end{array} ) \lambda _ { 0 } ^ { j - 1 } { \boldsymbol x } _ { k - 2 } } \\ & { } & \\ & { } & { ( 3 } \end{array}\tag{}
$$

for j = 0, 1, . . . , are linearly independent solutions of Eq. (2).

Theorem 2. Let $\mathbf { x } _ { 0 } , \mathbf { x } _ { 1 } , \ldots , \mathbf { x } _ { k - 1 } \in \mathbb { C } ^ { n }$ , with $\pmb { x } _ { 0 } \neq \pmb { \theta } _ { }$ If the sequence $( u _ { 0 } ^ { ( k - 1 ) }$ $\pmb { u } _ { 1 } ^ { ( k - 1 ) } , \dots ) \in \mathcal { S } ( \mathbb { C } ^ { n } )$ , with

$$
u _ { j } ^ { ( k - 1 ) } = \sum _ { s = 0 } ^ { k - 1 } { \binom { j } { s } } \lambda _ { 0 } ^ { j - s } x _ { k - 1 - s } ,
$$

is a solution of Eq. (2), then $\lambda _ { 0 }$ is a latent root of L(λ) and $\pmb { x } _ { 0 } , \pmb { x } _ { 1 } , \ldots , \pmb { x } _ { k - 1 }$ is a Jordan chain for L(λ) corresponding to $\lambda _ { 0 }$

Exercise 1. Solve the system of difference equations for $j = 0 , 1 , \ldots ,$

$$
x _ { j + 2 } ^ { ( 1 ) } = 0 ,
$$

$$
x _ { j + 2 } ^ { ( 2 ) } + x _ { j + 1 } ^ { ( 1 ) } - x _ { j + 1 } ^ { ( 1 ) } + x _ { j } ^ { ( 1 ) } = 0 .
$$

SOLUTION. Write the given system in the form (2):

$$
{ \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] } { \boldsymbol { x } } _ { j + 2 } + { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { - 1 } \end{array} \right] } { \boldsymbol { x } } _ { j + 1 } + { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 1 } & { 0 } \end{array} \right] } { \boldsymbol { x } } _ { j } = \theta , \qquad j = 0 , 1 , \ldots ,
$$

where $\mathbf { x } _ { j } = [ x _ { j } ^ { ( 1 ) } x _ { j } ^ { ( 2 ) } ] ^ { \mathrm { T } }$ for each j. Since the leading coefficient of the associated matrix polynomial $L ( \lambda )$ is nonsingular $( L _ { 2 } = I ) ,$ it follows from the corollary to Theorem 7.10.2 that the given system has four linearly independent solutions. To find four such solutions, recall the result of Exercise 14.3.2 and use Theorem 1:

$$
\begin{array} { r l } & { u _ { j } ^ { ( 0 ) } = [ 0 \quad 1 ] ^ { \mathrm { T } } , \qquad j = 0 , 1 , \dots , } \\ & { v _ { 0 } ^ { ( 0 ) } = [ 0 \quad 1 ] ^ { \mathrm { T } } , \qquad v _ { j } ^ { ( 0 ) } = \theta , \quad j = 1 , 2 , \dots , } \\ & { v _ { 0 } ^ { ( 1 ) } = [ 1 \quad 0 ] ^ { \mathrm { T } } , \qquad v _ { 1 } ^ { ( 1 ) } = [ 0 \quad 1 ] ^ { \mathrm { T } } , \qquad v _ { j } ^ { ( 1 ) } = \theta , j = 2 , 3 , \dots , } \\ & { v _ { 0 } ^ { ( 2 ) } = [ - 2 \quad 0 ] ^ { \mathrm { T } } , \qquad v _ { 1 } ^ { ( 2 ) } = [ 1 \quad 0 ] ^ { \mathrm { T } } , \qquad v _ { 2 } ^ { ( 2 ) } = [ 0 \quad 1 ] ^ { \mathrm { T } } , } \\ & { v _ { j } ^ { ( 2 ) } = \theta , \quad j = 3 , 4 , \dots . } \end{array}
$$

The verification of the linear independence of the vectors ${ \pmb u } ^ { ( 0 ) } , { \pmb v } ^ { ( 0 ) } , { \pmb v } ^ { ( 1 ) } , { \pmb v } ^ { ( 2 ) }$ in ${ \mathcal { S } } ( \mathbb { C } ^ { 2 } )$ is left as an exercise.

Since the solution space has dimension 4, every solution has the form

$$
\alpha _ { 1 } u ^ { ( 0 ) } + \alpha _ { 2 } v ^ { ( 0 ) } + \alpha _ { 3 } v ^ { ( 1 ) } + \alpha _ { 4 } v ^ { ( 2 ) }
$$

for some $\qquad \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } , \alpha _ { 4 } \in \mathbb { C } .$ □

Consider now the formulation of a general solution of the inhomogeneous difference equation (1). Observe first that the general solution $\mathbf { { } } { \mathbf { { } } { \mathbf { { } } } } { \mathbf { { } } } { \mathbf { { } } } { \mathbf { { } } } { \mathbf { { } } } { \mathbf { { } } } { \mathbf { { } } } { \mathbf { { } } } { \mathbf { { } } } { \mathbf { { } } }  \mathbf { { } { } \mathbf { { } } } { \mathbf { { } { } \mathbf { { } } } } { \mathbf { { } { } \mathbf { { } } } } { \mathbf { { } } } { \mathbf { { } { } \mathbf { { } } } } { \mathbf { { } { } \mathbf { { } } } } { \mathbf { { } } } { \mathbf { { } { } \mathbf { { } } } } { \mathbf { { } } }  \mathbf { { } { } \mathbf { { } { } } } { \mathbf { { } { } \mathbf { { } } } } { \mathbf { { } { } \mathbf { { } { } } \mathbf { { } { } } } { \mathbf { { } { } \mathbf { { } } } } { \mathbf { { } { } \mathbf { { } { } } \mathbf { { } { } } } } { \mathbf { { } \mathbf { { } { } } \mathbf { { } { } } } { \mathbf { { } } \mathbf { { { } } \mathbf { { } { } } \mathbf { { } { } \mathbf { { } } } } { \mathbf { { } \mathbf { { } { } } \mathbf { { } } } } { \mathbf { { } \mathbf { { } } \mathbf { { } { } } \mathbf { { } } } } { \mathbf { { } \mathbf { { } } \mathbf { { } } \mathbf { { } } } } { \mathbf { \Sigma } } { \mathbf { } \mathbf { { } } \mathbf { { } } \mathbf { { } \Sigma } } } { \mathbf { \Sigma } } { \mathbf { } \Sigma } { \mathbf { } \Sigma } } { \mathbf { \Sigma } \Sigma } { \Sigma } \Sigma { \Sigma } \Sigma \Sigma \Sigma \Sigma }  \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma $ of (1) can be represented in the following way:

$$
\begin{array} { r } { \pmb { x } = \pmb { x } ^ { ( 0 ) } + \pmb { x } ^ { ( 1 ) } , } \end{array}\tag{4}
$$

where $\mathbf { x } ^ { ( 0 ) }$ is a general solution of the homogeneous equation (2) and $\mathbf { x } ^ { ( 1 ) }$ is a fixed particular solution of Eq. (1). Indeed, it is easily checked that the sequence in Eq. (4) satisfies Eq. (1) for every solution $\pmb { x } ^ { ( 0 ) }$ of Eq. (2) and, conversely, the difference $\mathbf { x } - \mathbf { x } ^ { ( 1 ) }$ is a solution of Eq. (2).

Now we take advantage of the idea of linearization to show how a general solution of Eq. (1) can be expressed in terms of any standard triple of $L ( \lambda )$

Lemma 1. The general solution ${ \pmb x } = ( { \pmb x } _ { 0 } , { \pmb x } _ { 1 } , \dots )$ of the nonhomogeneous equation (1) is given by $\pmb { x } _ { 0 } = P _ { 1 } \pmb { z }$ , and for j = 1, 2, . . . ,

$$
{ \bf x } _ { j } = P _ { 1 } C _ { L } ^ { j } z + P _ { 1 } \sum _ { k = 0 } ^ { j - 1 } C _ { L } ^ { j - k - 1 } R _ { 1 } { \bf f } _ { k } .\tag{5}
$$

where the matrices $P _ { 1 }$ and $R _ { 1 }$ are defined by Eq. (14.2.2) and $z \in \mathbb { C } ^ { l n }$ is arbitrary.

PRooF. First observe that the general solution $\mathbf { x } ^ { ( 0 ) } = \bigl ( \mathbf { x } _ { 0 } ^ { ( 0 ) } , \mathbf { x } _ { 1 } ^ { ( 0 ) } , \ldots \bigr )$ of the homogeneous equation (2) is given by

$$
\mathfrak { x } _ { j } ^ { ( 0 ) } = { P } _ { 1 } C _ { L } ^ { j } z , \qquad j = 0 , 1 , 2 , \dotsc ,\tag{6}
$$

where $z \in \mathbb { C } ^ { l n }$ is arbitrary. This is easily verified by substitution and by using Theorem 7.10.2 to prove that Eq. (6) gives all the solutions of Eq. (2).

Thus it remains to show that the sequence $( \pmb { \theta } , \pmb { x } _ { 1 } ^ { ( 1 ) } , \pmb { x } _ { 2 } ^ { ( 1 ) } , \dots )$ , with

$$
\pmb { x } _ { j } ^ { ( 1 ) } = P _ { 1 } \sum _ { k = 0 } ^ { j - 1 } C _ { L } ^ { j - k - 1 } R _ { 1 } \pmb { f } _ { k } , \qquad j = 1 , 2 , \ldots ,
$$

is a particular solution of Eq. (1). This is left as an exercise. We only note that the proof relies, in particular, on the use of Theorem 14.2.3 and Exercise 14.2.6 applied to the companion triple $( P _ { 1 } , C _ { L } , R _ { 1 } )$

Using the similarity of the standard triples of L(λ) and the assertion of Lemma 1, we easily obtain the following analogue of Theorem 14.5.1.

Theorem 3. If (U, T, V) is a standard triple for L(λ), then every solution of Eq. (2) has the form $\begin{array} { r } { { \bf x } _ { 0 } = U { \bf z } , } \end{array}$ and for $j = 1 , 2 , \ldots$

$$
\pmb { x } _ { j } = U T ^ { j } \pmb { z } + U \sum _ { k = 0 } ^ { j - 1 } T ^ { j - k - 1 } V \pmb { f } _ { k } ,
$$

where $\pmb { z } \in \mathbb { C } ^ { t n } ,$

We conclude this section by giving an explicit solution of the initial-value problem for a system of difference equations (compare with Theorem 14.5.2).

Theorem 4. Let $( U , T , V )$ be a standard triple for L(λ). There is a unique solution of Eq. (1) satisfying initial conditions

$$
\begin{array} { r } { \pmb { x } _ { j } = \pmb { a } _ { j } , \qquad j = 0 , 1 , \ldots , l - 1 , } \end{array}\tag{7}
$$

for any given vectors $\mathbf { \Delta } _ { a _ { 0 } } , \mathbf { \Delta } _ { a _ { 1 } } , \dots , \mathbf { \Delta } _ { a _ { l - 1 } } \in \mathbb { C } ^ { n }$ . This solution is given explicitly by the results of Theorem 3 together with the choice

$$
\boldsymbol { z } = [ V \quad T V \quad \cdots \quad T ^ { l - 1 } V ] \boldsymbol { S } _ { L } \left[ \begin{array} { c } { \mathbf { 0 } _ { 0 } } \\ { \mathbf { 4 } _ { 1 } } \\ { \vdots } \\ { \mathbf { 4 } _ { l - 1 } } \end{array} \right] ,
$$

where $S _ { L }$ is the symmetrizer for L(λ).

The proof of this result is similar to that of Theorem 14.5.2.

Exercise 2. Complete the proofs of Theorems 1, 2, and 4.

Exercise 3. Suppose that $f _ { j } = f$ for $j = 0 , 1 , 2 , , .$ . in Eq. (1), and assume that all latent roots of $L ( \lambda )$ are inside the unit circle. Show that the solution of Eq. (1) satisfies

$$
\operatorname * { l i m } _ { j \to \infty } \pmb { x } _ { j } = ( L _ { l } + L _ { l - 1 } + \cdots + L _ { 0 } ) ^ { - 1 } \pmb { f } . \pmb { \big \sqcup }
$$

## 14.7 A Representation Theorem

It has already been seen, in Theorem 14.2.2, that any standard triple for a matrix polynomial $L ( \lambda )$ (with det $L _ { l } \neq 0 )$ can be used to give an explicit representation of the (rational) resolvent function $L ( \lambda ) ^ { - 1 }$ . In this section we look for a representation of $L ( \lambda )$ itself, that is, of the coefficient matrices $L _ { 0 } , L _ { 1 } , \ldots , L _ { t }$ , in terms of a standard triple. We will show that, in particular, the representations given here provide a generalization of the reduction of a square matrix to Jordan normal form by similarity.

Theorem 1. Let (U, T, V) be a standard triple for a matrix polynomial $L ( \lambda )$ (as defined in $E q .$ (14.1.2)). Then the coefficients of $L ( \lambda )$ admit the following representations:

$$
L _ { l } = ( U T ^ { l - 1 } V ) ^ { - 1 } ,\tag{1}
$$

$$
[ L _ { 0 } \quad L _ { 1 } \quad \cdots \quad L _ { l - 1 } ] = - L _ { l } U T ^ { l } \left[ \begin{array} { c } { { U } } \\ { { U T } } \\ { { \vdots } } \\ { { U T ^ { l - 1 } } } \end{array} \right] ^ { - 1 } ,\tag{2}
$$

and

$$
\left[ \begin{array} { c } { L _ { 0 } } \\ { L _ { 1 } } \\ { \vdots } \\ { L _ { l - 1 } } \end{array} \right] = - \left[ V \quad T V \quad . . . \quad T ^ { l - 1 } V \right] ^ { - 1 } T ^ { l } V L _ { l } .\tag{3}
$$

PRooF. We first show that Eqs. (1) and (2) hold when $( U , T , V )$ is the special standard triple $( P _ { 1 } , C _ { L } , R _ { 1 } )$ . First, Eq. (1) is obtained from Eq. (14.2.12). Then Eqs. (14.2.6) and (14.2.7) give the special case of Eq. (2):

$$
\begin{array} { r } { L _ { l } P _ { 1 } C _ { L } ^ { l } \left[ \begin{array} { c } { P _ { 1 } } \\ { P _ { 1 } C _ { L } } \\ { \vdots } \\ { P _ { 1 } C _ { L } ^ { l - 1 } } \end{array} \right] ^ { - 1 } = - [ L _ { 0 } \quad L _ { 1 } \quad \cdots \quad L _ { l - 1 } ] . } \end{array}
$$

For any other standard triple (U, T, V), write

$$
P _ { 1 } = U S , \qquad C _ { L } = S ^ { - 1 } T S , \qquad R _ { 1 } = S ^ { - 1 } V .
$$

Then

$$
P _ { 1 } C _ { L } ^ { \iota } \left[ \begin{array} { c } { P _ { 1 } } \\ { \vdots } \\ { P _ { 1 } C _ { L } ^ { \iota - 1 } } \end{array} \right] ^ { - 1 } = U T ^ { \iota } \left[ \begin{array} { c } { U } \\ { \vdots } \\ { U T ^ { \iota - 1 } } \end{array} \right] ^ { - 1 } ,
$$

and Eqs. (1) and (2) are established.

To obtain Eq. (3), observe that Corollary 14.2.1 shows that $( V ^ { \boldsymbol { \mathsf { T } } } , T ^ { \boldsymbol { \mathsf { T } } } , U ^ { \boldsymbol { \mathsf { T } } } )$ is a standard triple for $L ^ { \mathrm { { T } } } ( \lambda )$ , so applying the already established Eq. (2),

$$
- [ L _ { 0 } ^ { \mathsf { T } } L _ { 1 } ^ { \mathsf { T } } \quad \cdots \quad L _ { l - 1 } ^ { \mathsf { T } } ] = L _ { l } ^ { \mathsf { T } } V ^ { \mathsf { T } } ( T ^ { \mathsf { T } } ) ^ { l } \left[ \begin{array} { c } { { V ^ { \mathsf { T } } } } \\ { { V ^ { \mathsf { T } } T ^ { \mathsf { T } } } } \\ { { \vdots } } \\ { { V ^ { \mathsf { T } } ( T ^ { \mathsf { T } } ) ^ { l - 1 } } } \end{array} \right] ^ { - 1 } .
$$

Taking transposes, Eq. (3) is obtained.

Observe that if $L ( \lambda )$ is monic, that is, if $L _ { l } = I ,$ , then the l coefficients $L _ { 0 } , \dots , L _ { \iota - 1 }$ of $L ( \lambda )$ are determined by any standard pair (U, T), or by a left standard pair $( T , V )$ . Note also that if the theorem is applied using a Jordan triple $( X , J , Y )$ in place of $( U , T , V )$ the coefficients of $L ( \lambda )$ are completely determined in terms of the spectral properties of $L ( \lambda )$

Consider, in particular, the case in which $L ( \lambda ) = I \lambda - A .$ Thus, $L ( \lambda )$ is monic and $l = 1$ . In this case Eqs. (1) and (2), written in terms of a Jordan triple $( X , J , Y )$ , yield

$$
I = ( X Y ) ^ { - 1 } , \qquad A = X J Y .
$$

Thus the left Jordan chains (or columns of Y) are given by $Y = X ^ { - 1 }$ , and the second equation gives the expression of an arbitrary $\ b { A } \in \mathbb { C } ^ { n \times n }$ in terms of its Jordan form and chains, namely, $A = X J X ^ { - 1 }$

Exercise 1. Let $B , \ C \in \mathbb { C } ^ { n \times n }$ and define the matrix polynomial $L ( \lambda ) =$ $\lambda ^ { 2 } I + \lambda B + C$ . Show that if $( U , T )$ is a standard pair for $L ( \lambda )$ , then

$$
[ C , B ] = - U T ^ { 2 } \biggl [ U  \\  U T \biggr ] ^ { - 1 } .
$$

$\operatorname { I f } \left( U , T , V \right)$ is a standard triple for $L ( \lambda )$ , show also that

$$
B = - U T ^ { 2 } V , C = - U T ^ { 3 } V + B ^ { 2 } " \bigsqcup
$$

## 14.8 Multiples and Divisors

The idea of division of one matrix polynomial by another was introduced in Section 7.2. Recall that a matrix polynomial $L _ { 1 } ( \lambda )$ with invertible leading coefficient is said to be a right divisor of a matrix polynomial $L ( \lambda )$ if $L ( \lambda ) =$ $L _ { 2 } ( \lambda ) L _ { 1 } ( \lambda )$ for some other matrix polynomial $L _ { 2 } ( \lambda )$ . The reason for requiring that $L _ { 1 } ( \lambda )$ have invertible leading coefficient is to avoid the multiplicities of divisors that would arise otherwise. For example, a factorization like

$$
{ \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] } = { \left[ \begin{array} { l l } { a \lambda ^ { k } } & { 0 } \\ { b \lambda ^ { l } } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { c \lambda ^ { m } } & { d \lambda ^ { n } } \end{array} \right] } ,
$$

where $a , b , c , d \in \mathbb { C }$ and k, l, m, n are nonnegative integers, should be excluded, not only because there are so many candidates, but mainly because such factorizations are not very informative. Here we go a little further and confine our attention to divisors that are monic, where the coefficient of the highest power of λ is I. In fact, it will be convenient to consider only monic divisors of monic polynomials.

It turns out that, from the point of view of spectral theory, multiples of matrix polynomials are more easily analyzed than questions concerning divisors. One reason for this concerns the question of existence of divisors. Thus, it is not difficult to verify that the monic matrix polynomial

$$
\left[ { \begin{array} { l l } { \lambda ^ { 2 } } & { 1 } \\ { 0 } & { \lambda ^ { 2 } } \end{array} } \right]\tag{1}
$$

has no monic divisor of degree 1 in λ. A thorough analysis of the existence question is beyond the scope of this brief introduction to questions concerning spectral theory, multiples, and divisors.

Standard triples, and hence spectral properties (via Jordan triples), of products of monic matrix polynomials are relatively easy to describe if triples of the factors are known. Observe first that the following relation between monic matrix polynomials, $L ( \lambda ) = L _ { 2 } ( \lambda ) L _ { 1 } ( \lambda )$ , implies some obvious statements:

$$
\mathrm { ( a ) } \ \sigma ( L _ { 1 } ) \cup \sigma ( L _ { 2 } ) = \sigma ( L ) ;
$$

(b) Latent vectors of $L _ { 1 } ( \lambda )$ and $L _ { 2 } ^ { \mathrm { T } } ( \lambda )$ are latent vectors of $L ( \lambda )$ and $L ^ { \mathrm { { T } } } ( \lambda )$ , respectively.

Some of the complications of this theory are associated with cases in which $\sigma ( L _ { 1 } ) \cap \sigma ( L _ { 2 } ) \neq \emptyset$ in condition (a). In any case, it is possible to extend statement (b) considerably. This will be done in the first corollary to the following theorem.

Theorem 1. Let $L ( \lambda ) , L _ { 1 } ( \lambda ) , L _ { 2 } ( \lambda )$ be monic matrix polynomials such that $L ( \lambda ) = L _ { 2 } ( \lambda ) L _ { 1 } ( \lambda )$ and let $( U _ { 1 } , T _ { 1 } , V _ { 1 } ) , ( U _ { 2 } , T _ { 2 } , V _ { 2 } )$ be standard triples for $L _ { 1 } ( \lambda )$ and $L _ { 2 } ( \lambda )$ , respectively. Then the admissible triple

$$
U = [ U _ { 1 } \quad 0 ] , \qquad T = { \left[ \begin{array} { l l } { T _ { 1 } } & { V _ { 1 } U _ { 2 } } \\ { 0 } & { T _ { 2 } } \end{array} \right] } , \qquad V = { \left[ \begin{array} { l } { 0 } \\ { V _ { 2 } } \end{array} \right] }\tag{2}
$$

for $L ( \lambda )$ is a standard triple for L(λ).

PRoOF. With T defined in (2), it is easily seen that

$$
( \lambda I - T ) ^ { - 1 } = { \binom { ( \lambda I - T _ { 1 } ) ^ { - 1 } } { 0 } } ^ { ( \lambda I - T _ { 1 } ) ^ { - 1 } V _ { 1 } U _ { 2 } ( \lambda I - T _ { 2 } ) ^ { - 1 } } \Biggr ] .
$$

Then the definitions of U and V give

$$
\begin{array} { r l } & { U ( \lambda I - T ) ^ { - 1 } V = U _ { 1 } ( \lambda I - T _ { 1 } ) ^ { - 1 } V _ { 1 } U _ { 2 } ( \lambda I - T _ { 2 } ) ^ { - 1 } V _ { 2 } } \\ & { \phantom { = \ } = L _ { 1 } ( \lambda ) ^ { - 1 } L _ { 2 } ( \lambda ) ^ { - 1 } = ( L _ { 2 } ( \lambda ) L _ { 1 } ( \lambda ) ) ^ { - 1 } } \\ & { \phantom { = \ } = L ( \lambda ) ^ { - 1 } , } \end{array}
$$

where Theorem 14.2.2 has been used. The result now follows from Theorem 14.2.4.

To see the significance of this result for the spectral properties of $L ( \lambda )$ $L _ { 1 } ( \lambda )$ , and $L _ { 2 } ( \lambda )$ , replace the standard triples for $L _ { 1 } ( \lambda )$ and $L _ { 2 } ( \lambda )$ by Jordan triples $( X _ { 1 } , J _ { 1 } , Y _ { 1 } )$ and $( X _ { 2 } , J _ { 2 } , Y _ { 2 } )$ , respectively. Then $L ( \lambda )$ has a standard triple (not necessarily a Jordan triple)

$$
[ X _ { 1 } \quad 0 ] , \qquad \left[ { J _ { 1 } \quad Y _ { 2 } X _ { 1 } } \right] , \qquad \left[ { \begin{array} { c } { { \theta } } \\ { { Y _ { 2 } } } \end{array} } \right] .\tag{3}
$$

Although the second matrix is not in Jordan form, it does give important partial information about the spectrum of $L ( \lambda )$ because of its triangular form. Property (b) of Theorem 14.2.3 implies, for example, (see also Eq. (14.3.4)) that $\sum _ { j = 0 } ^ { l } L _ { j } X _ { 1 } J _ { 1 } ^ { j } = 0$ , where $\begin{array} { r } { L ( \bar { \lambda } ) = \sum _ { j = 0 } ^ { l } \lambda ^ { j } L _ { j } } \end{array}$ . This implies the following corollary.

Corollary 1. Under the hypotheses of Theorem 1, $\sigma ( L _ { 1 } ) \subset \sigma ( L )$ , and if $\lambda _ { 0 } \in \sigma ( L _ { 1 } )$ , then every Jordan chain for $L _ { 1 } ( \lambda )$ corresponding to $\lambda _ { 0 }$ is also a Jordan chain for $L ( \lambda )$ corresponding to $\lambda _ { 0 }$

Similarly, $\sigma ( L _ { 2 } ) \subset \sigma ( L )$ and every Jordan chain of $L _ { 2 } ^ { \mathrm { T } } ( \lambda )$ is a Jordan chain of $L ^ { \mathbf { T } } ( \lambda )$

Given the standard triple (3) for L(λ), it is natural to ask when the two matrices

$$
{ \begin{array} { r l } { \left[ J _ { 1 } \quad Y _ { 2 } X _ { 1 } {  } , \quad } & { {\right] \left[ \begin{array} { l l } { J _ { 1 } } & { \ 0 } \\ { 0 } & { J _ { 2 } } \end{array} \right] } } \end{array} }\tag{4}
$$

are similar, in which case a Jordan form for $L ( \lambda )$ is just the direct sum of Jordan forms for the factors. An answer is provided immediately by Theorem 12.5.3, which states that the matrices of (4) are similar if and only if there exists a solution $Z$ (generally rectangular) for the equation

$$
J _ { 1 } Z - Z J _ { 2 } = Y _ { 2 } X _ { 1 } .\tag{5}
$$

This allows us to draw the following conclusions.

Corollary 2. Let $( X _ { 1 } , J _ { 1 } , Y _ { 1 } )$ and $( X _ { 2 } , J _ { 2 } , Y _ { 2 } )$ be Jordan triples for $L _ { 1 } ( \lambda )$ and $L _ { 2 } ( \lambda )$ , respectively. Then diag $\left[ J _ { 1 } , J _ { 2 } \right]$ is a linearization for $L ( \lambda ) =$ $L _ { 2 } ( \lambda ) L _ { 1 } ( \lambda )$ if and only if there is a solution Z for Eq. (5); in this case

$$
\left[ { J } _ { 1 } \quad 0 \\ { 0 \quad J _ { 2 } } \right] = \left[ { I } _ { 0 } \quad Z \right] \left[ { J } _ { 1 } \quad { Y } _ { 2 } { X } _ { 1 } \right] \left[ { I } _ { \phantom { { J } } } - Z \right] .\tag{6}
$$

PROOF. Observe that

$$
\left[ \begin{array} { l l } { I } & { - Z } \\ { 0 } & { I } \end{array} \right] = \left[ \begin{array} { l l } { I } & { Z } \\ { 0 } & { I } \end{array} \right] ^ { - 1 } ,
$$

so that the relation (6) is, in fact, the explicit similarity between the matrices of (4). To verify Eq. (6), it is necessary only to multiply out the product on the right and use Eq. (5).

An important special case of Corollary 2 arises when $\sigma ( L _ { 1 } ) \cap \sigma ( L _ { 2 } ) = \emptyset$ for then, by Theorem 12.3.2, Eq. (5) has a solution and it is unique. Thus, $\sigma ( L _ { 1 } ) \cap \sigma ( L _ { 2 } ) = \emptyset$ is a sufficient condition for diag[ $[ J _ { 1 } , J _ { 2 } ]$ to be a linearization of $L _ { 2 } ( \lambda ) L _ { 1 } ( \lambda )$

## 14.9 Solvents of Monic Matrix Polynomials

As in the preceding section, we confine attention here to $n \times n$ monic matrix polynomials $\begin{array} { r } { L ( \lambda ) = \lambda ^ { \iota } I + \sum _ { j = 0 } ^ { l - 1 } \lambda ^ { j } L _ { j } } \end{array}$ An $n \times n$ matrix S is said to be a (right) solvent of L(λ) if, in the notation of Section 7.2, the right value of $L ( \lambda )$ at S is the zero-matrix, that is,

$$
S ^ { l } + L _ { l - 1 } S ^ { l - 1 } + \cdot \cdot \cdot + L _ { 1 } S + L _ { 0 } = O .\tag{1}
$$

This is, of course, a natural generalization of the notion of a zero of a scalar polynomial, and it immediately suggests questions concerning the factorizations of $L ( \lambda )$ determined by solvents of $L ( \lambda )$

It has been shown in the Corollary to Theorem 7.2.3 that S satisfies Eq. (1) if and only if $\lambda I - s$ is a right divisor of $L ( \lambda )$ , that is, if and only if $L ( \lambda ) =$ $L _ { 2 } ( \lambda ) ( \lambda I - S )$ for some monic matrix polynomial $L _ { 2 } ( \lambda )$ of degree $l - 1$ This immediately puts questions concerning solvents of $L ( \lambda )$ in the context of the preceding section. In particular, recall that matrix polynomials may have no solvent at all (see the polynomial of Eq. (14.8.1)). Furthermore, it is deduced from Corollary 1 of Theorem 14.8.1 that when a solvent S exists, all eigenvalues of S are latent roots of $L ( \lambda )$ and all Jordan chains of $\lambda I - s$ must be Jordan chains of $L ( \lambda )$ . Also, if $S = { { X } _ { 1 } } { { J } _ { 1 } } { { X } _ { 1 } } ^ { - 1 }$ , where $J _ { \textrm { 1 } }$ is in Jordan normal form, then $( X _ { 1 } , J _ { 1 } )$ is a Jordan pair for $\lambda I - S$ Thus, the matrix

$$
R _ { 1 } = \left[ \begin{array} { c } { X _ { 1 } } \\ { X _ { 1 } J _ { 1 } } \\ { \vdots } \\ { X _ { 1 } J _ { 1 } ^ { l - 1 } } \end{array} \right]
$$

has rank n and its columns form Jordan chains for $C _ { L }$ . It follows that Im $R _ { 1 }$ is a $C _ { L } .$ -invariant subspace of dimension n. Development of this line of argument leads to the following criterion.

Theorem 1 (H. Langer†). The monic matrix polynomial $L ( \lambda )$ of degree l has a right solvent S if and only if there exists an invariant subspáce $\mathcal { S }$ of $C _ { L }$ of the form $\mathcal { S } =$ Im $Q _ { 1 }$ where

$$
\begin{array} { r } { Q _ { 1 } = \left[ \begin{array} { c } { I } \\ { S } \\ { S ^ { 2 } } \\ { \vdots } \\ { S ^ { i - 1 } } \end{array} \right] . } \end{array}\tag{2}
$$

PRoOF. If S is a right solvent of $L ( \lambda )$ then, as we have seen, $\lambda I - s$ is a right divisor of $L ( \lambda )$ . It is easily verified that $( I , S , I )$ is a standard triple for $\lambda I - S ,$ so if $( U _ { 2 } , T _ { 2 } , V _ { 2 } )$ is a standard triple for the quotient $L ( \lambda ) ( \lambda \bar { I } - S ) ^ { - 1 }$ , then Theorem 14.8.1 implies that $L ( \lambda )$ has a standard pair of the form

$$
X = [ I \quad 0 ] , \qquad T = \left[ \begin{array} { l l } { { S } } & { { U _ { 2 } } } \\ { { 0 } } & { { T _ { 2 } } } \end{array} \right] .
$$

Defining an ln × ln matrix $Q$ by

$$
Q = \left[ \begin{array} { c } { { X } } \\ { { X T } } \\ { { \vdots } } \\ { { X T ^ { l - 1 } } } \end{array} \right] = \left[ \begin{array} { c c } { { I } } & { { 0 } } \\ { { S } } & { { U _ { 2 } } } \\ { { S ^ { 2 } } } & { { * } } \\ { { \vdots } } & { { \vdots } } \\ { { S ^ { l - 1 } } } & { { * } } \end{array} \right]
$$

(where \* denotes a matrix of no immediate interest), it follows, as in Lemma 14.2.1, that $C _ { L } Q = Q T .$ This implies $C _ { L } Q _ { 1 } = Q _ { 1 } S$ , where $Q _ { 1 }$ is defined by Eq. (2). Consequently, $C _ { L } \mathcal { S } \subset \mathcal { S } .$

Conversely, let $\mathcal { S } =$ Im $Q _ { 1 }$ , where $Q _ { 1 }$ is defined by Eq. (2) for some $n \times n$ matrix $s ,$ and let $\mathcal { S }$ be $C _ { L } .$ -invariant. Then for any $\pmb { y } \in \mathbb { C } ^ { n }$ there is a $z \in \mathbb { C } ^ { n }$ such that

$$
C _ { L } Q _ { 1 } \mathbf { y } = Q _ { 1 } \mathbf { z } .
$$

Using the definition (14.1.3) of $C _ { L } ,$ this means that

$$
\left[ \begin{array} { c } { S } \\ { S ^ { 2 } } \\ { \vdots } \\ { S ^ { l - 1 } } \\ { - \displaystyle \sum _ { j = 0 } ^ { l - 1 } L _ { j } S ^ { j } } \end{array} \right] y = \left[ \begin{array} { c } { I } \\ { S } \\ { \vdots } \\ { S ^ { l - 2 } } \\ { S ^ { l - 1 } } \end{array} \right] z .
$$

In particular, $z = S y$ and so $- \textstyle \sum _ { j = 0 } ^ { l - 1 } L _ { j } S ^ { j } y = S ^ { l - 1 }$ z implies

$$
( S ^ { l } + L _ { l - 1 } S ^ { l - 1 } + \cdot \cdot \cdot + L _ { 1 } S + L _ { 0 } ) y = 0 .
$$

Since this is true for any $\pmb { y } \in \mathbb { C } ^ { n }$ , Eq. (1) follows and S is a right solvent of $L ( \lambda )$ ■

Note that a subspace $\mathcal { S }$ of the form Im $Q _ { 1 }$ , with $Q _ { 1 }$ given by Eq. (2), can be characterized as an n-dimensional subspace containing no nonzero vectors of the form

$$
\begin{array} { r } { \boldsymbol { \Phi } = [ \pmb { \theta } \quad \boldsymbol { \Phi } _ { 1 } ^ { \mathrm { T } } \quad \cdots \quad \boldsymbol { \Phi } _ { i - 1 } ^ { \mathrm { T } } ] ^ { \mathrm { T } } , } \end{array}
$$

where $\pmb { \theta } , \Phi _ { i } \in \mathbb { C } ^ { n } , i = 1 , 2 , \ldots , l - 1$ . Indeed, if φ $\in \mathcal { S }$ is such a vector, then

$$
\boldsymbol { \Phi } = \left[ \begin{array} { c } { I } \\ { \boldsymbol { S } } \\ { \boldsymbol { S } ^ { 2 } } \\ { \vdots } \\ { \boldsymbol { S } ^ { i - 1 } } \end{array} \right] \boldsymbol { z }
$$

for some $z \in \mathbb { C } ^ { n } .$ Therefore, comparing the first n coordinates of φ and $Q _ { 1 } z ,$ it is found that $z = \theta$ and consequently ${ \mathfrak { P } } = \theta .$

By using Theorem 1, we show in the next example that certain monic matrix polynomials have no solvents. This generalizes the example in Eq. (14.8.1).

Example 1. Consider the monic $n \times n \left( l \geq 2 \right)$ matrix polynomial

$$
L ( \lambda ) = \lambda ^ { l } I _ { n } - J _ { n } ,
$$

where $J _ { n }$ denotes the $n \times n$ Jordan block with zeros on the main diagonal. Clearly $\sigma ( L ) = \{ 0 \}$ and the kernel of $L ( 0 )$ has dimension 1. It follows that $L ( \lambda )$ has just one elementary divisor, $\lambda ^ { l n }$ , and so the Jordan matrix associated with $L ( \lambda )$ is $J _ { l n }$ , the Jordan block size ln with zeros on the main diagonal. Observe that $J _ { { t n } }$ has just one invariant subspace $\mathcal { S } _ { j }$ of dimension j for $j = 1 , 2 , \dots , n ,$ and it is given by

$$
{ \mathcal { S } } _ { j } = \operatorname { s p a n } \{ e _ { 1 } , e _ { 2 } , \ldots , e _ { j } \} \subset \mathbb { C } ^ { l n } .
$$

By Lemma 14.2.1, it follows that $C _ { L }$ also has just one n-dimensional invariant subspace and it is given by $Q \mathcal { S } _ { n } ,$ where

$$
\boldsymbol { Q } = \left[ \begin{array} { c } { \boldsymbol { X } } \\ { \boldsymbol { X } \boldsymbol { J } _ { l n } } \\ { \vdots } \\ { \boldsymbol { X } \boldsymbol { J } _ { l n } ^ { l - 1 } } \end{array} \right] , \qquad \boldsymbol { \mathcal { S } } _ { n } = \mathrm { I m } \left[ \begin{array} { c } { \boldsymbol { I } } \\ { \boldsymbol { 0 } } \\ { \vdots } \\ { \boldsymbol { 0 } } \end{array} \right]
$$

and $( X , J _ { \imath n } )$ is a Jordan pair for $L ( \lambda )$ . If $X _ { 1 }$ is the leading $n \times n$ block of $X ,$ then

$$
\boldsymbol { Q } \boldsymbol { \mathcal { S } } _ { n } = \operatorname { I m } \left[ \begin{array} { c } { X _ { 1 } } \\ { X _ { 1 } J _ { n } } \\ { \vdots } \\ { X _ { 1 } J _ { n } ^ { l - 1 } } \end{array} \right] .
$$

For this subspace to have the form described in Theorem 1 it is necessary and sufficient that $X _ { 1 }$ be nonsingular. However, since $L ^ { ( k ) } ( 0 ) = 0$ for $k =$ $1 , 2 , \ldots , l - 1$ , it is easily seen that we may choose the unit vector $\pmb { e _ { 1 } }$ in $\mathbb { C } ^ { n }$ for each of the first l columns of X. Thus $X _ { 1 }$ cannot be invertible if $l \geq 2 ,$ and $C _ { L }$ has no invariant subspace of the required form.

In contrast to Example 1, a monic matrix polynomial may have many distinct solvents, as shown in the following example.

Exercise 2. Check that the matrices

$$
S _ { 1 } = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] } , \qquad S _ { 2 } = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { - 2 } & { 1 } \end{array} \right] } , \qquad S _ { 3 } = { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] }
$$

are solvents of the matrix polynomial

$$
L ( \lambda ) = \lambda ^ { 2 } I + \lambda { \left[ \begin{array} { l l } { ~ 1 } & { ~ 1 } \\ { - 2 } & { - 3 } \end{array} \right] } + { \left[ \begin{array} { l l } { 0 } & { - 1 } \\ { 0 } & { 2 } \end{array} \right] } . \boxed { 1 }
$$

The example of scalar polynomials suggests that we investigate the possibility of capturing spectral information about a monic polynomial of degree l in a set of n solvents. Thus, define a set of solvents $S _ { 1 } , S _ { 2 } , \ldots , S _ { l }$ of $L ( \lambda )$ to be a complete set of solvents of $L ( \lambda )$ if the corresponding Vandermonde (block) matrix

$$
V = \left[ \begin{array} { c c c c } { I } & { I } & { . . . } & { I } \\ { S _ { 1 } } & { S _ { 2 } } & { . . . } & { S _ { l } } \\ { . . } & { . . } & { . . } \\ { S _ { 1 } ^ { l - 1 } } & { S _ { 2 } ^ { l - 1 } } & { . . . } & { S _ { l - 1 } ^ { l } } \end{array} \right] \in \mathbb { C } ^ { l n }\tag{3}
$$

is nonsingular. Note that in the case $l = 2$ ,this condition is equivalent to the nonsingularity of the $n \times n$ matrix $s _ { 2 } - s _ { 1 }$

Clearly, in the scalar case $( n = 1 )$ , if $L ( \lambda )$ has a set of l distinct zeros then, according to this definition, they form a complete set of solvents (zeros) of the polynomial. This observation shows that not every (matrix or scalar) polynomial possesses a complete set of solvents. However, if such a set of solvents does exist, then there are remarkable parallels with the theory of scalar polynomial equations.

Theorem 2. If $S _ { 1 } , S _ { 2 } , \ldots , S _ { l }$ is a complete set of solvents of a monic $n \times n$ matrix polynomial $L ( \lambda ) ,$ , then diagl $[ S _ { 1 } , S _ { 2 } , \ldots , S _ { l } ]$ is a linearization of L(λ) In particular,

$$
\sigma ( L ) = \bigcup _ { i = 1 } ^ { l } \sigma ( S _ { i } ) .
$$

ProoF. The assertion of the theorem immediately follows from the easily verified relation

$$
C _ { L } V = V \mathrm { d i a g } [ S _ { 1 } , S _ { 2 } , \ldots , S _ { l } ] ,\tag{4}
$$

where V is given by Eq. (3) (see Exercise 7.11.14).

The converse problem of finding a monic matrix polynomial with a given set of solvents is readily solved; it forms the contents of the next exercise.

Exercise 3. Prove that if the Vandermonde matrix V associated with prescribed $n \times n$ matrices $S _ { 1 } , S _ { 2 } , \ldots , S _ { l }$ is invertible, then there exists a monic $n \times n$ matrix polynomial $L ( \lambda )$ of degree l such that $\{ S _ { 1 } , S _ { 2 } , \ldots , S _ { l } \}$ is a complete set of solvents for $L ( \lambda )$

Hint. Consider the n × ln matrix $[ - S _ { 1 } ^ { l } \quad - S _ { 2 } ^ { l } \quad \cdot \cdot \cdot \quad - S _ { l } ^ { l } ] V ^ { - 1 } . \quad \bigsqcup$

Theorem 3. Let $S _ { 1 } , S _ { 2 } , \ldots , S _ { l }$ form a complete set of solvents of the monic $n \times n$ matrix polynomial $L ( \lambda )$ of degree l. Then every solution of the differential equation $L ( d / d t ) \mathbf { x } = \pmb { \theta }$ is of the form

$$
\pmb { x } ( t ) = e ^ { S _ { 1 } t } \pmb { z } _ { 1 } + e ^ { S _ { 2 } t } \pmb { z } _ { 2 } + \cdot \cdot \cdot + e ^ { S _ { l } t } \pmb { z } _ { l } ,\tag{5}
$$

where $z _ { 1 } , z _ { 2 } , \ldots , z _ { l } \in \mathbb { C } ^ { n } .$

PRoOF. Substituting Eq. (4) in the formula (14.5.5) (with $\pmb { f } ( t ) = \pmb { \theta } )$ we obtain

$$
\pmb { x } ( t ) = \pmb { \mathcal { P } } _ { 1 } e ^ { V D V ^ { - 1 } t } \pmb { z } = P _ { 1 } V e ^ { D t } V ^ { - 1 } \pmb { z } ,
$$

where $D = \mathrm { d i a g } [ S _ { 1 } , S _ { 2 } , . . . , S _ { l } ]$ . Since $P _ { 1 } V = [ I \quad I \quad \cdots \quad I ]$ and $e ^ { D t } =$ diag $[ e ^ { S _ { 1 } t } , e ^ { S _ { 2 } t } , \ldots , e ^ { S _ { t } t } ]$ , the result in Eq. (5) follows if we write $V ^ { - 1 } z =$ $[ \pmb { z } _ { 1 } ^ { \mathrm { { T } } } \quad \pmb { z } _ { 2 } ^ { \mathrm { { T } } } \quad \cdots \quad \pmb { z } _ { l } ^ { \mathrm { { T } } } ] ^ { \mathbf { \mathrm { { T } } } } ,$ ■

## Example 4. Consider the differential equation

$$
{ \ddot { \pmb x } } ( t ) + \left[ - \frac { 1 } { 2 } \mathbf { \nabla } - \frac { 1 } { 3 } \right] { \dot { \pmb x } } ( t ) + \left[ \frac { 0 } { 0 } \mathbf { \nabla } - 1 \right] { \pmb x } ( t ) = \pmb \theta ,\tag{6}
$$

and the matrix equation

$$
X ^ { 2 } + \biggl [ - \frac { 1 } { 2 } - \frac { 1 } { 3 } \biggr ] X + \biggl [ 0 - 1 \biggr ] = 0 .\tag{7}
$$

We saw in Exercise 2 that the matrices

$$
S _ { 1 } = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] } , \qquad S _ { 2 } = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { - 2 } & { 1 } \end{array} \right] }\tag{8}
$$

satisfy Eq. (7), and since det $( S _ { 2 } - S _ { 1 } ) \neq 0 .$ , they form a complete pair of solvents for the corresponding matrix polynomial. Thus the general solution of Eq. (6) is of the form (5) with $l = 2 ,$ where $S _ { 1 }$ and $S _ { 2 }$ are given by (8). To simplify this, observe that

$$
e ^ { S _ { 1 } t } = I + S _ { 1 } t + { \textstyle \frac { 1 } { 2 } } S _ { 1 } ^ { 2 } t ^ { 2 } + \dots = I + S _ { 1 } t = { \left[ \begin{array} { l l } { 1 } & { t } \\ { 0 } & { 1 } \end{array} \right] } ,
$$

while

$$
\begin{array} { r } { \left[ { \begin{array} { c c } { 1 } & { 0 } \\ { - 2 } & { 1 } \end{array} } \right] = \left[ { \begin{array} { c c } { 0 } & { - \frac { 1 } { 2 } } \\ { 1 } & { 0 } \end{array} } \right] \left[ { \begin{array} { c c } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} } \right] \left[ { \begin{array} { c c } { 0 } & { - \frac { 1 } { 2 } } \\ { 1 } & { 0 } \end{array} } \right] ^ { - 1 } . \qquad } \end{array}
$$

Therefore

$$
e ^ { S _ { 2 } t } = { \left[ \begin{array} { l l } { 0 } & { - { \frac { 1 } { 2 } } } \\ { 1 } & { ~ 0 } \end{array} \right] } { \left[ \begin{array} { l l } { e ^ { t } } & { t e ^ { t } } \\ { 0 } & { e ^ { t } } \end{array} \right] } { \left[ \begin{array} { l l } { ~ 0 } & { 1 } \\ { - 2 } & { 0 } \end{array} \right] } = { \left[ \begin{array} { l l } { ~ e ^ { t } } & { ~ 0 } \\ { - 2 t e ^ { t } } & { ~ e ^ { t } } \end{array} \right] } .
$$

Thus, the general solution of Eq. (6) is

$$
{ \left[ \begin{array} { l } { x _ { 1 } ( t ) } \\ { x _ { 2 } ( t ) } \end{array} \right] } = { \pmb x } ( t ) = { \pmb \left[ \begin{array} { l l } { 1 } & { t } \\ { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { \alpha _ { 1 } } \\ { \alpha _ { 2 } } \end{array} \right] } + { \left[ \begin{array} { l l } { e ^ { t } } & { 0 } \\ { - 2 t e ^ { t } } & { e ^ { t } } \end{array} \right] } { \left[ \begin{array} { l } { \alpha _ { 3 } } \\ { \alpha _ { 4 } } \end{array} \right] } ,
$$

and hence

$$
\begin{array} { l } { { x _ { 1 } } ( t ) = { \alpha _ { 1 } } + { \alpha _ { 2 } } t + { \alpha _ { 3 } } e ^ { t } , } \\ { ~ x _ { 2 } ( t ) = { \alpha _ { 2 } } - 2 { \alpha _ { 3 } } t e ^ { t } + { \alpha _ { 4 } } e ^ { t } , } \end{array}
$$

for arbitrary $\alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } , \alpha _ { 4 } \in \mathbb { C }$ □

Note that the conditions of Theorem 3 can be relaxed by requiring only similarity between $C _ { L }$ and any block-diagonal matrix. This leads to a generalization of the notion of a complete set of solvents for a monic matrix polynomial and to the form $\sum _ { i = 1 } ^ { l } \mathbf { \bar { C } } _ { i } e ^ { X _ { i } t } z _ { i }$ for the solution of the differential equation. Also, the notion of a solvent of multiplicity r of a matrix polynomial can be developed to obtain a complete analogue of the form of solutions for a linear differential equation of order l with scalar coefficients in terms of zeros of the corresponding characteristic equation.

Exercise 5. (a) Let A be a Hermitian matrix. Show that the equation

$$
X ^ { 2 } - X + A = 0\tag{9}
$$

has Hermitian solutions if and only if $\sigma ( A ) \subset ( - \infty , { \frac { 1 } { 4 } } ]$

(b) Let A be positive semidefinite. Show that all Hermitian solutions of Eq. (9) are positive semidefinite if and only if $\sigma ( A ) \subset [ 0 , { \frac { 1 } { 4 } } ]$ and in this case $\sigma ( X ) \subset [ 0 , 1 ]$ □

# Nonnegative Matrices

A matrix $A \in \mathbb { R } ^ { m \times n }$ is said to be nonnegative if no element of A is negative. If all the elements of A are positive, then A is referred to as a positive matrix. Square matrices of this kind arise in a variety of problems and it is perhaps surprising that this defining property should imply some strong results concerning their structure. The remarkable Perron-Frobenius theorem is the central result for nonnegative matrices and is established in Theorems 15.3.1 and 15.4.2.

Matrices whose inverses are nonnegative, or positive, also play an important part in applications, and a brief introduction to such matrices is also contained in this chapter.

If $A = [ a _ { i j } ]$ and $B = [ b _ { i j } ]$ are matrices from $\mathbb { R } ^ { m \times n }$ , we shall write $A \geq B$ (respectively, $A > B )$ if $a _ { i j } \geq b _ { i j }$ (respectively, $a _ { i j } > b _ { i j } )$ for all pairs $( i , j )$ such that $1 \leq i \leq m , 1 \leq j \leq n .$ With this notation, A is nonnegative if and only if $A \geq 0 .$ It should be noted that $A \geq 0$ and $A \neq 0$ do not imply $A > 0$ Also, if $A \ge 0 , B \ge C$ and AB is defined, then $A B \geq A C$ ; and if $A \ge 0 , B > 0$ , and $A B = 0 ,$ then $A = 0$ Note that most of these remarks apply to vectors as well as to matrices.

The duplication of notations with those for definite and semidefinite square matrices is unfortunate. However, as the latter concepts do not play an important part in this chapter, no confusion should arise.

## 15.1 Irreducible Matrices

The concept of reducibility of square matrices plays an important part in this chapter. This was introduced in Section 10.7; it would be wise to read the discussion there once more. Here, the combinatorial aspect of this concept will be emphasized.

It is interesting that the concept of reducibility is not connected in any way with the magnitudes or signs of the elements of a matrix but depends only on the disposition of zero and nonzero elements. This idea is developed in the concept of the directed graph associated with a matrix; we shall take only the first step in this theory to obtain a second characterization of an irreducible matrix in Theorem 1.

Let $P _ { 1 } , P _ { 2 } , \ldots , P _ { n }$ be distinct points of the complex plane and let $A \in \mathbb { C } ^ { n \times n }$ For each nonzero element $a _ { i j }$ of A, connect $P _ { i }$ to $P _ { j }$ with a directed line $\overline { { \boldsymbol { P } _ { i } \boldsymbol { P } _ { j } } }$ . The resulting figure in the complex plane is a directed graph for A. We illustrate this in Fig. 15.1 with a $3 \times 3$ matrix and is directed graph.

$$
\begin{array} { r } { \left[ 1 - 2 0 \right] } \\ { 0 4 2 } \\ { 1 - 1 0 } \end{array}
$$

We say that a directed graph is strongly connected if, for each pair of nodes $P _ { i } , P _ { j }$ with $i \neq j ,$ there is a directed path

$$
\overrightarrow { P _ { i } P _ { k _ { 1 } } } , \overrightarrow { P _ { k _ { 1 } } P _ { k _ { 2 } } } , \dotsc , \overrightarrow { P _ { k _ { r - 1 } } P _ { j } }
$$

connecting $P _ { i }$ to $P _ { j }$ . Here, the path consists of r directed lines.

Observe that nodes i and j may be connected by a directed path while j and i are not.

Exercise 1. Check that the graph of Fig. 1 is strongly connected.

![](images/1e8008052b658790a7a41c246601385c3f85f24878c9959b8b595a0132bf335f.jpg)  
Fig. 15.1 The directed graph of a matrix.

Exercise 2. Verify that the directed graph associated with the matrix

$$
\left[ { \begin{array} { r r r } { 2 } & { 0 } & { 0 } \\ { 3 } & { 1 } & { 0 } \\ { 0 } & { 4 } & { - 1 } \end{array} } \right]
$$

fails to be strongly connected.

Exercise 3. Show that if all the off-diagonal entries of a row A (or a column of A) are zero, then the graph of A is not strongly connected.

SoLuTioN. In the case of a row of A, say row i, there are no directed lines $\overrightarrow { P _ { i } P _ { j } }$ starting at node i. So there is no connection from node i to any other node. So the graph is not strongly connected. □

The next two exercises form part of the proof of the next theorem.

Exercise 4. Let $A \in \mathbb { C } ^ { n \times n }$ have the partitioned form

$$
A = { \left[ \begin{array} { l l } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} \right] } ,
$$

where $A _ { 1 1 }$ is $k \times k$ and $1 \leq k \leq n - 1$ (so that A is trivially reducible).   
Show that the directed graph of A is not strongly connected.

SoLuTioN. Consider any directed path from a node i with $i > k .$ The first segment of the path is determined by the presence of a nonzero element $a _ { i j }$ in the ith row of A. This row has zeros in the first k positions, so it is possible to make a connection from node i to node j only $\operatorname { i f } j > k .$ Similarly, the path can be extended from node j only to another node greater than k. Continuing in this way, it is found that a directed path from node i with $i > k$ cannot be connected to a node less than $k + 1$ . Hence the directed graph is not strongly connected.

Exercise 5. Let $A \in \mathbb { C } ^ { n \times n }$ and let P be an $n \times n$ permutation matrix. Show that the directed graph of A is strongly connected if and only if the directed graph of $P A P ^ { \mathrm { \bf T } }$ is strongly connected.

SoLUTION. Observe that the graph of $P A P ^ { \mathrm { \bf T } }$ is obtained from that of A just by renumbering the nodes, and this operation does not affect the connectedness of the graph.□

Theorem 1. A square matrix is irreducible if and only if its directed graph is strongly connected.

ProoF. Exercise 4 shows that if A is reducible, then the graph of $P A P ^ { \mathrm { \bf T } }$ is not strongly connected, for some permutation matrix P. Then Exercise 5 shows that this is equivalent to the statement that A itself has a directed graph that is not strongly connected. Thus, a strongly connected directed graph implies that the matrix is irreducible. Proof of the converse statement is postponed to Exercise 15.3.3.

In testing particular matrices for reducibility, it is important to keep in mind the obvious fact that if A is irreducible and B is obtained from A by replacing zero entries by nonzero entries, then B is also irreducible.

Exercise 6. Check that the following matrices are irreducible. In both cases the elements $a _ { i j }$ not set equal to zero are, in fact, nonzero.

$$
{ [ \begin{array} { l l l l l } { 0 } & { a _ { 1 2 } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { a _ { 2 3 } } & { } & { \vdots } \\ { \vdots } & { \vdots } & { } & { \ddots } & { } & { 0 } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { a _ { n - 1 , n } } \\ { a _ { n 1 } } & { 0 } & { \cdots } & { 0 } & { 0 } \end{array} ] } , \qquad { [ \begin{array} { l l l l l } { 0 } & { a _ { 1 2 } } & { 0 } & { \cdots } & { 0 } \\ { a _ { 2 1 } } & { 0 } & { a _ { 2 3 } } & { \ddots } & { \vdots } \\ { 0 } & { a _ { 3 2 } } & { \ddots } & { \ddots } & { 0 } \\ { \vdots } & { \ddots } & { } & { 0 } & { a _ { n - 1 , n } } \\ { 0 } & { \cdots } & { 0 } & { a _ { n , n - 1 } } & { 0 } \end{array} ] } . \qquad { [ \begin{array} { l l l l l } { 0 } & { a _ { 1 2 } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { a _ { 2 3 } } & { \cdots } & { a _ { n - 1 , n } } & { 0 } \\ { 0 } & { a _ { 3 2 } } & { \ddots } & { \ddots } & { 0 } \\ { \vdots } & { \ddots } & { } & { 0 } & { a _ { n - 1 , n } } \\ { 0 } & { \cdots } & { 0 } & { a _ { n , n - 1 } } & { 0 } \end{array} ] } . \qquad [ \begin{array} { l l l l l } { a _ { 1 2 } } & { 0 } & { 0 } & { \cdots } & { a _ { 1 2 } } \\ { a _ { 2 3 } } & { 0 } & { a _ { 2 3 } } & { \cdots } & { a _ { n - 1 , n } } \\ { a _ { 2 3 } } & { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { a _ { n - 1 } } & { 0 } & { a _ { 2 3 } } & { \cdots } &  a  \end{array}
$$

## 15.2 Nonnegative Matrices and Nonnegative Inverses†

Let $A \in \mathbb { C } ^ { n \times n }$ with elements $a _ { j k }$ and let $| A |$ denote the nonnegative matrix in $\mathbb { R } ^ { n \times n }$ with elements $\vert a _ { j k } \vert$ . Clearly, one of the properties shared by A and $\vert A \vert$ is that of reducibility or irreducibility. In addition, many norms of A and $| A |$ take the same value (see Sections 10.3 and 10.4). However, the relationship between the spectral radii of A and $\left| A \right|$ is more delicate, and it is frequently of interest. It is plausible that $\mu _ { A } \leq \mu _ { | A | }$ , and we first show that this is the case. We return in Section 15.4 to the important question of conditions under which $\mu _ { A } < \mu _ { | A | }$

Theorem 1. Let $A \in \mathbb { C } ^ { n \times n }$ and $B \in \mathbb { R } ^ { n \times n } . ~ I f | A | \leq B .$ then $\mu _ { A } \leq \mu _ { B }$

ProoF. Let ε be an arbitrary positive number and define the scalar multiples

$$
A _ { \varepsilon } = ( \mu _ { B } + \varepsilon ) ^ { - 1 } A , \qquad B _ { \varepsilon } = ( \mu _ { B } + \varepsilon ) ^ { - 1 } B .
$$

Clearly $\left| A _ { \varepsilon } \right| \leq B _ { \varepsilon }$ , and it is easily seen (see Exercise 1) that for $k = 1 , 2 , \ldots ,$ $|  A _ { \varepsilon } | ^ { k } \leq B _ { \varepsilon } ^ { k }$

Now it is also clear that $\mu _ { B _ { c } } < 1$ , and so (see Exercise 9.8.5) $B _ { \varepsilon } ^ { k } \to 0 { \mathrm { ~ a s ~ } } k \to \infty$ Since $| A _ { \varepsilon } ^ { k } | \leq | A _ { \varepsilon } | ^ { k } \leq B _ { \varepsilon } ^ { k } .$ , it follows that $A _ { \mathfrak { r } } ^ { \mathtt { k } } \to \theta$ as $k \to \infty$ and so (by Exercise 9.8.5 again) $\mu _ { A _ { \varepsilon } } < 1$ . But this implies $\mu _ { A } < \mu _ { B } + \varepsilon ,$ and since ε is arbitrary, $\mu _ { A } \leq \mu _ { B }$ 门

Note that on putting $B = \left| \boldsymbol { A } \right|$ , we obtain $\mu _ { A } \leq \mu _ { | A | }$ from the theorem.

Consider now the question of solving an equation $A \mathbf { x } = b ,$ where $A \in \mathbb { R } ^ { n \times n }$ and $\pmb { b } \in \mathbb { R } ^ { n }$ are given and A is invertible. The unique solution is, of course, $x = A ^ { - 1 } b$ . However, if b is not known precisely and we are given only bounding vectors $\pmb { b } _ { 1 } , \pmb { b } _ { 2 } \in \mathbb { R } ^ { n }$ in the sense that $\pmb { b } _ { 1 } \leq \pmb { b } \leq \pmb { b } _ { 2 }$ , what can then be said about the solution vector $\pmb { x } ?$ The perturbation analysis of Section 11.1 gives one answer in terms of the condition number of A. But if $A ^ { - 1 }$ is a nonnegative matrix, we can give precise bounds for the solution vector because, in this case,

$$
A ^ { - 1 } b _ { 1 } \leq A ^ { - 1 } b = x \leq A ^ { - 1 } b _ { 2 } .
$$

A matrix $A \in \mathbb { R } ^ { n \times n }$ is said to be monotone if it is nonsingular and $A ^ { - 1 } \geq 0 .$ Monotone matrices frequently occur with a sign pattern among the elements; for example, main-diagonal elements positive and off-diagonal elements nonpositive. Such matrices are given their own name: a monotone matrix is called an M-matrix if all the off-diagonal elements are nonpositive. The matrices A and B of Exercise 2.11.17 are monotone, and B is an M-matrix.

Exercise 1. Use Exercise 1.8.5 to prove that if $0 \leq A \leq B _ { \cdot }$ then $A ^ { k } \leq B ^ { k }$ for $k = 1 , 2 , \ldots$

Exercise 2. Prove that if A is an M-matrix, then each main-diagonal element of A is positive.

Hint. Observe that if not, then A has a complete column that is nonpositive, say the jth column, and then $A e _ { j } \leq 0 , \bigstar \bigstar$

We now discuss some criteria that ensure that a matrix $A \in \mathbb { R } ^ { n \times n }$ is an Mmatrix. They all give sufficient conditions that are often easy to check.

Theorem 2. Let $\pmb { { \cal B } } \in \mathbb { R } ^ { n \times n }$ with $B \geq \theta$ The matrix $I - B$ is an M- matrix if and only $j f \mu _ { B } < 1$

PROOF. If $\mu _ { B } < 1$ then Theorems 10.3.1 and 11.1.1 imply that ${ \pmb I } - { \pmb B }$ is nonsingular and

$$
( I - B ) ^ { - 1 } = I + B + B ^ { 2 } + \cdots .
$$

Since $B \geq 0$ it is clear that $\left( I - B \right) ^ { - 1 } \geq 0 .$ Obviously, the elements of $I \sim B$ off the main diagonal are nonpositive and so $I - B$ is an M-matrix.

Conversely, if $I - B$ is an M-matrix, then $\left( I - B \right) ^ { - 1 } \geq 0 .$ Let $\lambda \in \sigma ( B )$ and $\lambda { \mathbf { x } } = B { \mathbf { x } }$ with $\mathbf { x } \neq \mathbf { 0 } .$ Then, since $B \geq 0 ,$ it is easily seen that

$$
| \lambda | | x | \leq B | x | ,
$$

which implies $( I - B ) | { \boldsymbol { x } } | \leq ( 1 - | \lambda | ) | { \boldsymbol { x } } |$ , and hence

$$
| x | \leq ( 1 - | \lambda | ) ( I - B ) ^ { - 1 } | x | .
$$

Since $| { \pmb x } | \geq \pmb 0$ and $( I - B ) ^ { - 1 } \geq 0$ , it follows that $| \lambda | < 1$ . But this is the case for any $\lambda \in \sigma ( B )$ , so have $\mu _ { B } < 1$ .■

Theorem 3. Let $\boldsymbol { A } = [ a _ { i j } ] _ { i , j = 1 } ^ { n } \in \mathbb { R } ^ { n \times n }$ and assume that $a _ { i i } > 0$ for each i and $a _ { i j } \leq 0$ whenever $i \neq j .$ If A is diagonally dominant, that is,

$$
a _ { i i } > \sum _ { j = 1 , \ j \neq i } ^ { n } | a _ { i j } | , \qquad i = 1 , 2 , \ldots , n ,
$$

or, if A is irreducible and

$$
a _ { i i } \geq \sum _ { j = 1 , \ j \neq i } ^ { n } | a _ { i j } | , \qquad i = 1 , 2 , \ldots , n ,
$$

with strict inequality for at least one i, then A is an M-matrix.

ProoF. First consider the case in which A is diagonally dominant. Let $D = \mathrm { d i a g } [ a _ { 1 1 } , \dotsc , a _ { n n } ]$ and define $B = I - D ^ { - 1 } A$ . Note that B has zero elements on the main diagonal and that $B \geq 0$ . Also, the fact that A is diagonally dominant implies that

$$
\sum _ { j = 1 } ^ { n } | b _ { i j } | < 1 , \qquad i = 1 , 2 , \ldots , n .
$$

It follows immediately from the Geršgorin theorem (Section 10.6) that $\mu _ { B } < 1$ Now we have $D ^ { - 1 } A = I - B ,$ and it follows from Theorem 2 that $D ^ { - 1 } A$ is an M-matrix. Consequently, A is also an M-matrix.

With the second set of hypotheses we follow the same line of argument but use the corollary to Theorem 10.7.2 to ensure that $\mu _ { B } < 1$

Exercise 3. Show that, under either of the hypotheses of Theorem 3, In $A = \{ n , 0 , 0 \}$ . If, in addition, A is symmetric then A is positive definite.

Exercise 4. Let A be a lower-triangular matrix, with positive elements on the main diagonal and nonpositive elements elsewhere. Show that A is an M-matrix.

Exercise 5. Show that if A is an M-matrix and D is a nonnegative diagonal matrix, then $A + D$ is an M-matrix.

Exercise 6. Show that a symmetric M-matrix is positive definite. (Such a matrix is called a Stieltjes matrix.)

SoLUTIoN. Let A be a symmetric M-matrix and $\lambda \in \sigma ( A )$ If $\lambda \leq 0$ then, by Exercise $5 , A - \lambda I$ is also an M-matrix and must therefore be nonsingular. This contradicts the assumption that $\lambda \in \sigma ( A )$ . Thus $\lambda \in \sigma ( A )$ implies $\lambda > 0$ and hence A is positive definite. □

## 15.3 The Perron-Frobenius Theorem (I)

It is obvious that if $A \geq 0$ then $A ^ { p } \geq 0$ for any positive integer p. We might also expect that if A has a sufficiently high density of nonzero elements then, for large enough p, we would obtain $A ^ { p } > 0 .$ Our first result is of this kind.

Proposition 1. If the matrix $A \in \mathbb { R } ^ { n \times n }$ is nonnegative and irreducible, then

$$
( I + A ) ^ { n - 1 } > 0 .
$$

ProoF. Consider a vector $\boldsymbol { \mathsf { y } } \in \mathbb { R } ^ { n }$ such that $\pmb { y } \geq \pmb { \theta }$ and $y \neq \theta$ and write

$$
z = ( I + A ) { \bf y } = { \bf y } + A { \bf y } .\tag{1}
$$

Since $A \geq 0 ,$ the product $A { \bf y } \geq \theta$ and so z has at least as many nonzero (and hence positive) elements as y. If y is not already positive, we shall prove that z has at least one more nonzero element than y. Indeed, if P is a permutation matrix such that $\begin{array} { r } { P \mathbf { y } = [ \pmb { u } ^ { \mathrm { T } } \quad \pmb { \theta } ^ { \mathrm { T } } ] ^ { \mathbf { T } } } \end{array}$ and $u > \theta$ , then it follows from Eq. (1) and the relation $P P ^ { \mathrm { T } } = I$ that

$$
P z = { \binom { u } { \theta } } + P A P ^ { \operatorname { T } } { \left[ \begin{array} { l } { u } \\ { \theta } \end{array} \right] } .\tag{2}
$$

Hence, if we partition z and $P A P ^ { \mathbf { T } }$ consistently with the partition of ${ \mathfrak { p } } ,$

$$
z = { \binom { v } { w } } , \qquad P A P ^ { \operatorname { T } } = { \binom { A _ { 1 1 } \quad A _ { 1 2 } } { A _ { 2 1 } \quad A _ { 2 2 } } } ,
$$

then Eq. (2) implies

$$
v = \pmb { u } + A _ { 1 1 } \pmb { u } \qquad \mathrm { a n d } \qquad \pmb { w } = A _ { 2 1 } \pmb { u } .\tag{3}
$$

Now observe that the matrix $P A P ^ { \mathrm { \bf T } }$ is nonnegative and irreducible. Hence, in particular, $A _ { 1 1 } \geq 0 , A _ { 2 1 } \geq 0 , A _ { 2 1 } \neq 0 .$ and therefore it follows from (3) that ${ \mathfrak { v } } > { \pmb { \theta } } , { \pmb { w } } \geq { \pmb { \theta } } .$ But $u > \theta$ and, therefore, $w \neq \theta .$ Thus, z has at least one more positive element than y.

If $( I + A ) y$ is not already positive then, starting with the element $( I + A ) z = ( I + A ) ^ { 2 } y$ and repeating the argument, it follows that it has at least two more positive elements than y. Continuing this process, we find after at most $n - 1$ steps that

$$
( I + A ) ^ { n - 1 } y > 0
$$

for any $\mathbf { y } \geq \mathbf { 0 } , \mathbf { y } \neq \mathbf { 0 }$ Putting $y = e _ { j } \operatorname { f o r } j = 1 , 2 , \ldots , n .$ we obtain the desired result.

Observe that there is a simple result in the other direction. $\operatorname { I f } \left( I + A \right) ^ { j } > 0$ for any $A \in \mathbb { R } ^ { n \times n }$ and any positive integer $j ,$ then A must be irreducible. Otherwise, assuming that A has the partitioned form of Exercise 15.1.4, we easily obtain a contradiction with the hypothesis.

Exercise 1. If $A \in \mathbb { R } ^ { n \times n }$ is irreducible and D is a nonsingular, nonnegative diagonal matrix, prove that $( D + A ) ^ { n - 1 } > 0$

Exercise 2. Let $A \in \mathbb { R } ^ { n \times n }$ be nonnegative and irreducible, and let $a _ { i j } ^ { ( q ) }$ be the $i , j$ element of $A ^ { q } .$ Show that there is a positive integer $q$ such that $a _ { i j } ^ { ( q ) } > 0$ Show also that if $\psi ( \lambda )$ is the minimal polynomial of $A ,$ then we may choose $q \leq \deg ( \psi )$

Hint. Observe that $A ( I + A ) ^ { n - 1 } > 0$ and use the binomial theorem. For the second part let $r ( \lambda )$ be the remainder on division of $\lambda ( 1 + \lambda ) ^ { n - 1 }$ by $\psi ( \lambda )$ and use the fact that $r ( A ) > 0$

Exercise 3. Let matrix A be as in Exercise 2.

(a) Show that $a _ { i j } ^ { ( q ) } > 0$ if and only if there is a sequence of $q$ edges in the directed graph of A connecting nodes $P _ { i }$ and $P _ { j }$

(b) Use the result of Exercise 2 to show that A has a strongly connected directed graph.□

If A is a nonnegative irreducible matrix, consider the real-valued function r defined on the nonzero vectors $x \ge \theta$ by

$$
r ( \pmb { x } ) = \operatorname* { m i n } _ { \stackrel { 1 \leq i \leq n } { { \pmb x } _ { i } \neq 0 } } \frac { ( A \pmb { x } ) _ { i } } { { \pmb x } _ { i } } ,\tag{4}
$$

where $( A { \pmb x } ) _ { i }$ denotes the ith element of the vector $A \mathbf { x } .$ Then $r ( { \boldsymbol { \mathbf { x } } } ) \geq 0$ and for $j = 1 , 2 , \ldots , n , r ( \pmb { x } ) x _ { j } \leq ( A \pmb { x } ) _ { j }$ , with equality for some j. Thus $r ( x ) x \leq A x$ and, furthermore, $r ( { \boldsymbol { \mathbf { x } } } )$ is the largest number $\rho$ such that $\rho x \leq A x$ for this x.

Exercise 4. Find r(x) if

$$
A = { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 3 } \end{array} \right] } \qquad { \mathrm { a n d } } \qquad x = { \left[ \begin{array} { l } { 1 } \\ { 0 } \end{array} \right] } .
$$

SOLUTION. Since $\mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf $ , the largest number $\pmb { \rho }$ such that $\rho x \leq A x$ is 2. Thus $r ( { \pmb x } ) = 2$

Exercise 5. If $\begin{array} { r } { A = [ a _ { i j } ] _ { i , j = 1 } ^ { n } } \end{array}$ and $\pmb { x } = [ 1 \quad 1 \quad \cdots \quad 1 ] ^ { \mathbf { I } }$ , show that

$$
r ( \boldsymbol { x } ) = \operatorname* { m i n } _ { 1 \le i \le n } \sum _ { k = 1 } ^ { n } a _ { i k } . \quad \bigsqcup
$$

Let $\mathcal { L }$ denote the domain of the function $r ,$ that is, the set of all nonzero nonnegative vectors of order $n _ { \mathnormal { , } }$ and define the number $r$ (not to be confused with the function r) by

$$
r = \operatorname* { s u p } _ { \mathbf { x } \in { \mathcal { L } } } r ( \mathbf { x } ) .\tag{5}
$$

From the definition of $r ( { \boldsymbol { \mathbf { x } } } ) _ { : }$ , we observe that r is invariant if x is replaced by αx for any $\alpha > 0$ Thus, in evaluating this supremum, we need only

consider the closed set $\mathcal { M }$ of vectors x such that ${ \pmb x } \geq { \pmb \theta }$ and $\sum _ { i } x _ { i } ^ { 2 } = 1$ Thus, ${ \mathcal { M } } \subset { \mathcal { L } }$ and

$$
r = \operatorname* { s u p } _ { \mathbf { x } \in \mathcal { M } } r ( \mathbf { x } ) .
$$

If the function $r ( x )$ were continuous on ${ \mathcal { M } } ,$ we could equate this to max $r ( { \pmb x } )$ $\boldsymbol { x } \in \mathcal { M }$ (see Appendix 2). However $r ( { \pmb x } )$ may have discontinuities at points where elements of x vanish. We therefore consider the set $\mathcal { N }$ of vectors y defined by

$$
\mathbf { y } = ( I + A ) ^ { n - 1 } \pmb { x } , \qquad \pmb { x } \in \mathcal { M } .
$$

By Proposition 1 every member of $\mathcal { N }$ is a positive vector and so ${ \mathcal { N } } \subset { \mathcal { L } } .$ $\operatorname { N o w } , \mathcal { N }$ is the image of the closed and bounded set $\mathcal { M }$ under a continuous function and is therefore also closed and bounded. Furthermore, $r ( \mathbf { y } )$ is continuous on $\mathcal { N }$

For any $\pmb { x } \in \mathcal { M }$ and corresponding y,

$$
r ( { \pmb x } ) { \pmb y } = r ( { \pmb x } ) ( { \pmb I } + { \pmb A } ) ^ { n - 1 } { \pmb x } \leq ( { \pmb I } + { \pmb A } ) ^ { n - 1 } { \pmb A } { \pmb x } ,
$$

since $r ( { \pmb x } ) { \pmb x } \leq A { \pmb x }$ , and hence $r ( { \mathfrak { x } } ) { \mathfrak { y } } \leq A { \mathfrak { y } }$ for every $\mathbf { \boldsymbol { y } } \in \mathcal { N } .$ Now, $r ( \boldsymbol { \mathbf { y } } )$ is the greatest number $\rho$ such that $\rho \mathbf { y } \leq A \mathbf { y }$ and hence $r ( \mathbf { x } ) \leq r ( \mathbf { y } )$ . Thus,

$$
r = \operatorname* { s u p } _ { \mathbf { x } \in \mathcal { M } } r ( \mathbf { x } ) \leq \operatorname* { m a x } _ { \mathbf { y } \in \mathcal { N } } r ( \mathbf { y } ) .
$$

But since ${ \mathcal { N } } \subset { \mathcal { L } } ,$

$$
\operatorname* { m a x } _ { \pmb { y } \in \mathcal { N } } r ( \mathbf { y } ) \leq \operatorname* { s u p } _ { \pmb { x } \in \mathcal { L } } r ( \pmb { x } ) = \operatorname* { s u p } _ { \pmb { x } \in \mathcal { M } } r ( \pmb { x } ) .
$$

Hence

$$
r = \operatorname* { m a x } _ { \mathbf { y } \in \mathcal { N } } r ( \mathbf { y } ) ,\tag{6}
$$

and there is a $\mathbf { y } > \pmb { \theta }$ such that $r = r ( \mathbf { y } )$

There may be other vectors in $\mathcal { L }$ for which $r ( x )$ attains the value r. Any such vector is called an extremal vector of A. Thus, a nonzero vector $z \geq \theta$ is an extremal vector of A if $r ( z ) = r \mathrm { o r }$ , what is equivalent $r z \leq A z$

The reason for our interest in the number r is clarified in the next result.

Proposition 2. If the matrix $A \in \mathbb { R } ^ { n \times n }$ is nonnegative and irreducible, then the number r defined by $E q . ( 5 )$ is positive and is an eigenvalue of A. Furthermore, every extremal vector of A is positive and is a right eigenvector of A associated with the eigenvalue r.

PROOF. Let $\pmb { x } = [ 1 \quad 1 \quad \cdots \quad 1 ] ^ { \mathbf { I } }$ Then (see Exercise 5) $\begin{array} { r } { r ( { \bf x } ) = \operatorname* { m i n } _ { i } \sum _ { k } a _ { i k } } \end{array}$ $> 0 .$ For, if any row of A consists entirely of zeros, then A is reducible. Since $r \geq r ( { \pmb x } )$ , we deduce that $r > 0$

Let z be an extremal vector and let $w = ( I + A ) ^ { n - 1 } z$ Without loss of generality, we may suppose that $z \in \mathcal { M }$ . Proposition 1 implies that $w > 0 ,$ and clearly $w \in { \mathcal { N } } .$ We also have $A z - r z \geq 0$ and, if $A z - r z \neq 0$ then

$$
( I + A ) ^ { n - 1 } ( A z - r z ) > 0 .
$$

Hence $A w \mathrm { ~ - ~ } r w > 0 ,$ or $r w < A w _ { : }$ , which implies that $r < r ( w )$ . But this contradicts the definition (5) or r, and so we must have $A z = r z$ Thus, any extremal vector z is a right eigenvector of A with associated eigenvalue r.

Finally, since $A z = r z$ , we have

$$
w = ( I + A ) ^ { n - 1 } z = ( 1 + r ) ^ { n - 1 } z ,
$$

and since $w > 0$ and $r > 0 ,$ we must have $z > \theta .$

We can now state and prove the first part of the Perron-Frobenius theorem for irreducible matrices.

Theorem 1. If the matrix $A \in \mathbb { R } ^ { n \times n }$ is nonnegative and irreducible, then

(a) The matrix A has a positive eigenvalue, r, equal to the spectral radius of A;

(b) There is a positive (right) eigenvector associated with the eigenvalue r;

(c) The eigenvalue r has algebraic multiplicity 1.

ProoF. In Proposition 2 we have established the existence of a positive eigenvalue with an associated positive eigenvector. To complete parts (a) and (b) of the theorem it suffices to show that other eigenvalues of A cannot exceed r in absolute value.

Indeed, if we have $\alpha \mathbf { y } = A \mathbf { y }$ and $\mathbf { \boldsymbol { y } } \neq \mathbf { \boldsymbol { \theta } } _ { : }$ then, since $A \geq 0 ,$ it is easily seen that

$$
| \alpha | | { \mathbf { y } } | = | A { \mathbf { y } } | \leq A | { \mathbf { y } } | ,
$$

where if $z \in \mathbb { R } ^ { n } , | z |$ denotes the vector obtained from z by replacing all its components by their absolute values. Hence $| \alpha | \leq r ( | \mathbf { y } | ) \leq r ,$ which is what we wanted to prove.

Suppose now that z is any right eigenvector associated with r. Thus, $A z = r z$ and $z \neq \theta ,$ and, as we just showed,

$$
r | z | \leq A | z | .
$$

This implies that $| z |$ is an extremal vector and, by Proposition $2 , | z | > \pmb { \theta } .$ Thus, $z _ { i } \neq 0 , i = 1 , 2 , \ldots , n .$ Hence the dimension of the right eigenspace of r is 1. Otherwise, we could find two linearly independent right eigenvectors ${ \tt z } _ { 1 } , { \tt z } _ { 2 }$ and then determine numbers $\alpha , \beta$ such that $\alpha z _ { 1 } + \beta z _ { 2 }$ has a zero element. This proves that the geometric multiplicity of r is 1.

To complete the proof,† we show that in the terminology of section 6.3, there is no generalized eigenvector of order 2 associated with $r ,$ and this will imply that the algebraic multiplicity of r is 1. To see this, let $\pmb { x } _ { 1 } > \pmb { \theta }$ and $y > \pmb { \theta }$ be eigenvectors of A and $A ^ { \boldsymbol { \mathsf { T } } }$ , respectively, associated with eigenvalue r. Thus,

$$
( r I - A ) \pmb { x } _ { 1 } = \pmb { 0 } , ( r I - A ^ { \top } ) \pmb { y } = \pmb { 0 } .
$$

Suppose that there is a generalized eigenvector $\pmb { x } _ { 2 } \neq \pmb { \theta }$ for which $( r I - A ) \pmb { x } _ { 2 }$ $\mathbf { \mu } = \mathbf { \mu } \mathbf { x } _ { 1 }$ (see Eqs. (6.3.3)). Then, since $\mathbf { y } ^ { \mathrm { T } } ( r I - A ) { \overset { - } { = } } \mathbf { 0 } ^ { \mathrm { T } }$ , we have $\mathbf { y } ^ { \mathrm { T } } \mathbf { x } _ { 1 } = 0 .$ But this contradicts the positivity of the vectors x and ${ \mathfrak { y } } ,$ and r must have algebraic multiplicity 1.

Exercise 6. Using the above notations and taking advantage of Exercise 7.9.1 show that if $B ( \lambda ) = \operatorname { a d j } ( \lambda I - A )$ , then

$$
B ( \lambda ) ( \lambda I - A ) = c ( \lambda ) I .
$$

Deduce that the derivative $c ^ { \prime } ( r ) > 0 _ { ; }$ and hence

$$
B ( r ) = k { \mathbf x } { \mathbf y } ^ { \mathrm { T } } > 0
$$

for some positive k.

Exercise 7. If $\boldsymbol { A } \in \mathbb { R } ^ { n \times n }$ is irreducible and nonnegative and $\begin{array} { r } { \sigma _ { j } = \sum _ { k = 1 } ^ { n } a _ { j k } } \end{array}$ $j = 1 , 2 , \dots , n ,$ prove that

$$
\operatorname* { m i n } _ { j } \sigma _ { j } \leq r \leq \operatorname* { m a x } _ { j } \sigma _ { j } ,
$$

and that there is equality in either case if and only if $\sigma _ { 1 } = \sigma _ { 2 } = \cdots = \sigma _ { n }$

SOLUTION. Adding the first $n - 1$ columns of $r I - A$ to the last one, we obtain

$$
\operatorname* { d e t } ( r I - A ) = \operatorname* { d e t } { \left[ \begin{array} { l l l l l } { r - a _ { 1 1 } } & { - a _ { 1 2 } } & { \cdots } & { - a _ { 1 , n - 1 } } & { r - \sigma _ { 1 } } \\ { - a _ { 2 1 } } & { r - a _ { 2 2 } } & { - a _ { 2 , n - 1 } } & { r - \sigma _ { 2 } } \\ { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { \qquad \vdots } & & { r - a _ { n - 1 , n - 1 } } & { r - \sigma _ { n - 1 } } \\ { - a _ { n 1 } } & { - a _ { n 2 } } & { \cdots } & { - a _ { n , n - 1 } } & { r - \sigma _ { n } } \end{array} \right] } = 0 .
$$

Expanding by the last column and denoting the $i ,$ jth element of $B ( r ) =$ $\operatorname { a d j } ( r I - A )$ by $b _ { i j } ( r )$ , we obtain

$$
\sum _ { j = 1 } ^ { n } ( r - \sigma _ { j } ) b _ { n j } ( r ) = 0 .
$$

But we have seen in Exercise 6 that $B ( r ) > 0$ and so $b _ { n j } ( r ) > 0$ for $j = 1$ $2 , \ldots , n .$ It follows that either $\sigma _ { 1 } = \sigma _ { 2 } = \cdot \cdot \cdot = \sigma _ { n }$ or there exist indices k, l such that $r < \sigma _ { k }$ and $r > \sigma _ { l }$ . Hence the result

Exercise 8. Using Exercise 7, and without examining the characteristic polynomial, prove that the following matrix has the maximal real eigenvalue 7 and that there is an eigenvalue equal to 4:

$$
{ \left[ \begin{array} { l l l l } { 3 } & { 0 } & { 1 } & { 0 } \\ { 1 } & { 6 } & { 1 } & { 1 } \\ { 2 } & { 0 } & { 2 } & { 0 } \\ { 1 } & { 3 } & { 1 } & { 4 } \end{array} \right] } .
$$

Exercise 9. If $A > \theta$ and G is the component matrix of A associated with r, prove that $G > 0 .$

Exercise 10. If A is irreducible and nonnegative and C(λ) is the reduced adjoint of A (see Section 7.9), prove that $C ( r ) > 0$

Hint. Observe that $\delta ( r ) = d _ { n - 1 } ( r ) > 0$ (Section 7.9).

Exercise 11. If A is nonnegative and irreducible, show that A cannot have two linearly independent nonnegative eigenvectors (even associated with distinct eigenvalues).

Hint. Use Exercise 10.7.2 and Theorem 1(c) for the matrices A and $A ^ { \boldsymbol { \mathsf { T } } }$ to obtain a contradiction.

## 15.4 The Perron-Frobenius Theorem (II)

The main results of the preceding section generalize results established first by Perron†. Frobenius published them in 1912 along with deeper results of this section, results that give more information on the structure of a nonnegative irreducible matrix A in those cases where A has more than one eigenvalue with absolute value equal to r, the spectral radius of A.

An important first step in our argument is a result due to Wielandt that is independently useful and gives a stronger result than the comparison theorem, Theorem 15.2.1, provided the bounding matrix is irreducible. Note that the proof depends heavily on the Perron-Frobenius results already established.

Theorem 1 (H. Wielandt†). Let $A \in \mathbb { C } ^ { n \times n } , B \in \mathbb { R } ^ { n \times n }$ satisfy $| A | \leq B$ and let B be irreducible. Then $\mu _ { _ { A } } = r ,$ where $\mu _ { A }$ and r are the spectral radii of A and B, respectively, if and only if A is of the form

$$
\pmb { A } = \omega \pmb { D } \pmb { B } \pmb { D } ^ { - 1 } ,\tag{1}
$$

where $| \omega | = 1 , | D | = I ,$ and $\omega r \in \sigma ( A )$

Note first of all that, by Theorem 15.3.1, r is in fact an eigenvalue of B.

PRooF. If A has the form (1), it is clear that A and B have the same spectral radius.

Conversely, let $\mu _ { A } = r$ and $\lambda \in \sigma ( A )$ with $| \lambda | = \mu _ { A } = r$ . Let a be a left eigenvector of A corresponding to $\lambda ,$ that is, ${ \pmb a } \neq { \pmb \theta }$ and $a ^ { * } A = \lambda a ^ { * }$ . Then

$$
| \lambda \pmb { a } ^ { * } | = | \lambda | | \pmb { a } ^ { * } | = r | \pmb { a } ^ { * } | \leq | \pmb { a } ^ { * } | | \boldsymbol { A } | \leq | \pmb { a } ^ { * } | \pmb { B } .\tag{2}
$$

Hence for any positive vector u,

$$
r | \mathbf { \mu } \mathbf { \pmb { a } } ^ { * } | \mathbf { \mu } \leq | \mathbf { \mu } \mathbf { \pmb { a } } ^ { * } | B \mathbf { \mu } .\tag{3}
$$

By Theorem 15.3.1 there is a $u > \theta$ such that $B u = r u .$ , so for this u we have $r | \mathbf { \nabla } a ^ { * } | \mathbf { \nabla } u = | \mathbf { \nabla } a ^ { * } | B u$ . Thus, for this choice of u equality obtains in (3) and hence, also, throughout (2). It follows that $| a ^ { * } | B = r | a ^ { * } |$ and, applying Theorem 15.3.1 again, we must have $| \pmb { a } ^ { * } | > 0$

Then (2) also yields

$$
| a ^ { * } | ( B - | A | ) = \theta ^ { * }
$$

which, together with $B \geq | A |$ , implies $B = | A |$

Now define $\omega = \lambda / r$ and

$$
D = \mathrm { d i a g } \biggl [ \frac { a _ { 1 } } { | a _ { 1 } | } , \ldots , \frac { a _ { n } } { | a _ { n } | } \biggr ] ,
$$

where $\mathbf { \Omega } \bullet = [ a _ { 1 } \quad \cdots \quad a _ { n } ] ^ { \mathbf { T } } .$ Then $| \omega | = 1 , | D | = I$ , and it is easily verified that $a ^ { * } D = | a ^ { * } |$ . Now, $a ^ { * } A = \lambda a ^ { * }$ implies

$$
| a ^ { * } | D ^ { - 1 } A = \lambda | a ^ { * } | D ^ { - 1 } ,
$$

so that

$$
| { \pmb a } ^ { * } | D ^ { - 1 } A D = \omega r | { \pmb a } ^ { * } | ,
$$

and

$$
| \pmb { a } ^ { * } | \omega ^ { - 1 } D ^ { - 1 } A D = r | \pmb { a } ^ { * } | = | \pmb { a } ^ { * } | B .
$$

In other words,

$$
| a ^ { * } | ( \omega ^ { - 1 } D ^ { - 1 } A D - B ) = 0 ^ { * } .\tag{4}
$$

But $B = | A | = | \omega ^ { - 1 } D ^ { - 1 } A D |$ and, since $| a ^ { * } | > 0 ^ { * }$ , it follows from Eq. (4) that $B = \omega ^ { - 1 } D ^ { - 1 } A D$ , and hence conclusion (1).

A particular deduction from Theorem 1 will be important for the proof of Theorem 2. Suppose that, in the theorem, A is nonnegative and irreducible. Apply the theorem with $B = A$ , so that $| A | \leq B$ and $\mu _ { A } = r$ are trivially satisfied. The conclusion is as follows:

Corollary 1. Let A be nonnegative and irreducible and let $\lambda \in \sigma ( A )$ with $| \lambda | = \mu _ { A } = r ,$ the spectral radius of A. Then A satisfies the condition

$$
A = \frac { \lambda } { r } D A D ^ { - 1 }\tag{5}
$$

for some diagonal matrix D with $| D | = I$

Exercise 1. Let the matrix A of Theorem 1 be nonnegative. Show that $\mu _ { A } = r$ if and only if $A = B .$

Exercise 2. Suppose that, in Theorem 1, the matrix A is obtained from B by replacing certain rows and/or columns by zero rows and/or columns, respectively. Show that $\mu _ { A } < r$ □

Theorem 2. Let the matrix $\boldsymbol { A } \in \mathbb { R } ^ { n \times n }$ be nonnegative and irreducible and have eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ . If there are exactly k eigenvalues $\lambda _ { 1 } = r ,$ $\lambda _ { 2 } , \ldots , \lambda _ { k }$ of modulus r and if $\omega _ { 1 } , \ldots , \omega _ { k }$ are the distinct kth roots of unity, then $\lambda _ { j } = \omega _ { j } r , j = 1 , 2 , . . . , k$

Moreover, the n points of the complex plane corresponding to $\lambda _ { 1 } , \ldots , \lambda _ { n }$ are invariant under rotations about the origin through 2π/k. If $k > 1$ , then there is a permutation matrix P such that $P ^ { \mathbf { T } } A P$ has the symmetrically partitioned form

$$
{ \left[ \begin{array} { l l l l l l } { 0 } & { A _ { 1 2 } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { A _ { 2 3 } } & { . } & { 0 } \\ { \vdots } & { \vdots } & { . } & { . } & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { A _ { k - 1 , k } } \\ { A _ { k 1 } } & { 0 } & { \cdots } & { 0 } & { 0 } \end{array} \right] } .
$$

PROOF. Let $\lambda _ { j } = \omega _ { j } r$ denote all the eigenvalues of A of modulus r, where $\omega _ { i } = e ^ { i \varphi _ { j } } , 0 = \stackrel { \cdot } { \varphi } _ { 1 } < \varphi _ { 2 } < \cdot \cdot \cdot < \varphi _ { k } < 2 \pi$ . To show that $\omega _ { 1 } , \omega _ { 2 } , \ldots , \omega _ { k }$ are the kth roots of unity, apply the result of Corollary 1 and write

$$
A = \omega _ { j } D _ { j } A D _ { j } ^ { - 1 } , ~ j = 1 , 2 , \ldots , k .\tag{6}
$$

By Theorem 15.3.1(b), there exists a vector $\pmb { x } \in \mathbb { R } ^ { n } , \ \pmb { x } > \pmb { \theta }$ , such that Ax $\mathbf { \mu } = \mathbf { \nabla } r \mathbf { x } .$ Then Eq. (6) implies that the vector $\pmb { x } _ { j } = D _ { j } \pmb { x }$ is an eigenvector of A associated with $\lambda _ { j } , j = 1 , 2 , \ldots , k$ Moreover, since r has algebraic multiplicity 1, the algebraic multiplicity of $\lambda _ { j } = \omega _ { j } r$ is also 1, $, j = 1 , 2 , \ldots , k .$ Indeed, r is a simple zero of the characteristic polynomial of A and hence $\omega _ { j } r$ is a simple zero of the characteristic polynomial of $\omega _ { j } A , 1 \leq j \leq k$ . In view of Eq. (6) these polynomials coincide:

$$
\operatorname* { d e t } ( \lambda I - A ) = \operatorname* { d e t } ( \lambda I - \omega _ { j } A ) , \qquad 1 \leq j \leq k ,
$$

and therefore the result follows.

Note that the geometric multiplicity of each of $\lambda _ { \mathrm { I } } , \lambda _ { 2 } , \ldots , \lambda _ { k }$ is then also 1 and hence the vectors $\mathbf { \delta } _ { \mathbf { x } _ { j } }$ , and therefore the matrices $D _ { j } , j = 1 , 2 , \ldots , k ,$ are defined uniquely up to scalar multiples. We thus assume that $D _ { 1 } = I$ and that all ones appearing in the matrices $D _ { 2 } , D _ { 3 } , \ldots , D _ { k }$ are located in the first parts of the main diagonals. With this assumption, the matrices $D _ { 1 } , D _ { 2 } , \ldots , D _ { k }$ are uniquely defined.

Now observe that Eq. (6) implies the relation

$$
A = \omega _ { j } D _ { j } A D _ { j } ^ { - 1 } = \omega _ { j } D _ { j } ( \omega _ { s } D _ { s } A D _ { s } ^ { - 1 } ) D _ { j } ^ { - 1 } = \omega _ { j } \omega _ { s } D _ { j } D _ { s } A ( D _ { j } D _ { s } ) ^ { - 1 }
$$

for any pair j, s, where $1 \leq j , s \leq k ,$ and therefore the same reasoning implies that the vector $D _ { j } D _ { s } { \pmb x }$ is an eigenvector of A associated with the eigenvalue $\omega _ { j } \omega _ { s } r$ of modulus r. Hence $\omega _ { j } \omega _ { s } = \omega _ { i }$ for some i, $1 \leq i \leq k _ { \mathrm { { m } } }$ , and, consequently, $D _ { j } D _ { s } = D _ { i }$ . Thus, $\left\{ \omega _ { 1 } , \omega _ { 2 } , \ldots , \omega _ { k } \right\}$ is a finite commutative (or Abelian) group consisting of k distinct elements.

It is well known that the kth power of any element of this group is equal to its identity element. Thus, $\omega _ { 1 } , \omega _ { 2 } , \ldots , \omega _ { k }$ are all the kth roots of unity, as required.

Note that the relation (6) can now be rewritten in the form

$$
A = e ^ { 2 \pi i / k } D A D ^ { - 1 }\tag{7}
$$

for some diagonal D with $| D | = I ,$ and therefore the matrix A is similar to the matrix $e ^ { 2 \pi i / k } A$ .Thus the spectrum $\sigma ( A )$ is carried into itself if it is rotated bodily about the origin through $2 \pi / k .$

Furthermore, the argument used above yields $D _ { j } ^ { k } = I , j = 1 , 2 , \ldots , k ,$ and therefore the diagonal elements of $D = D _ { j }$ are kth roots of unity. If $k > 1$ , there exists a permutation matrix P such that

$$
D _ { 0 } = P ^ { \mathrm { T } } D P = \mathrm { d i a g } [ \mu _ { 1 } I _ { 1 } , \mu _ { 2 } I _ { 2 } , \dots , \mu _ { s } I _ { s } ] ,\tag{8}
$$

where the $I _ { t }$ are identity matrices of appropriate sizes, $l = 1 , 2 , \ldots , s ,$ and $\mu _ { \iota } = e ^ { i \psi _ { \iota } } , \ \psi _ { \iota } = n _ { \iota } 2 \pi / k , \ 0 = n _ { 1 } < n _ { 2 } < \cdots < n _ { s } < k .$ Note that in view of Eq. (7),

$$
A _ { 0 } = \varepsilon D _ { 0 } A _ { 0 } D _ { 0 } ^ { - 1 } , \qquad \varepsilon = e ^ { 2 \pi i / k } ,\tag{9}
$$

in which $A _ { \bf 0 } = P ^ { \bf T } A P$ If $A _ { 0 } = [ A _ { i j } ] _ { i , j = 1 } ^ { s }$ is a partition of $A _ { 0 }$ consistent with that of $D _ { \mathbf { 0 } }$ in (8), then Eq. (9) implies

$$
A _ { i j } = \varepsilon \mu _ { i } \mu _ { j } ^ { - 1 } A _ { i j } , \qquad 1 \leq i , j \leq s .\tag{10}
$$

In particular, this implies $A _ { i i } = O$ for $i = 1 , 2 , \ldots , s .$ Note also that no block-row in $A _ { 0 }$ consists entirely of zeros, since otherwise we contractict the assertion of Proposition 15.3.1. Thus, starting with $i = 1$ in Eq. (10), at least one of the matrices $A _ { 1 2 } , A _ { 1 3 } , . . . , A _ { 1 s }$ is not the zero-matrix and therefore at least one of the numbers

$$
\varepsilon \mu _ { 1 } \mu _ { j } ^ { - 1 } = \exp [ 2 \pi i ( 1 + n _ { 1 } - n _ { j } ) / k ]
$$

is equal to 1. This is possible only if $n _ { j } = 1 + n _ { 1 } = 1 , 1 \leq j \leq s ,$ Since $n _ { 1 } , n _ { 2 } , \ldots , n _ { s }$ are integers and $n _ { 1 } < n _ { 2 } < \cdots < n _ { s }$ , this implies $j = 2 .$ Hence $A _ { 1 3 } = A _ { 1 4 } = \cdot \cdot \cdot = A _ { 1 s } = O$ . Putting $i = 2$ in Eq. (10), we similarly derive that $A _ { 2 j } = O , j = 1 , 2 , \ldots ,$ s but j $\neq 3 .$ Continuing this process, the following form of $A _ { 0 }$ is obtained:

$$
{ \left[ \begin{array} { l l l l l l } { 0 } & { A _ { 1 2 } } & { 0 } & { \dots } & { 0 } \\ { 0 } & { 0 } & { A _ { 2 3 } } & { \ddots } & { } & { \vdots } \\ { \vdots } & { } & { \ddots } & { \ddots } & { } & { 0 } \\ { 0 } & { } & { } & { 0 } & { A _ { s - 1 , s } } \\ { A _ { s 1 } } & { A _ { s 2 } } & { \dots } & { A _ { s , s - 1 } } & { 0 } \end{array} \right] } .
$$

The same argument applied for the case i = s in Eq. (10) yields the existence of at least one $j , 1 \le j \le s - 1$ , such that

$$
\exp [ 2 \pi i ( 1 + n _ { s } - n _ { j } ) / k ] = 1 , \qquad 1 \leq j \leq s - 1 .
$$

Since $0 \leq n _ { i } < n _ { s } < k , \ 1 \leq j \leq s - 1$ , this equality holds only if $1 + n _ { s }$ $- n _ { i } = k .$ But $n _ { 1 } = 0 , n _ { 2 } = 1 , \ldots , n _ { s - 1 } = s - 2 ,$ and therefore $n _ { s } = k - 1$ and $n _ { j } = 0 ,$ hence $j = 1$ . Thus $A _ { s 2 } = A _ { s 3 } = \cdot \cdot \cdot = A _ { s , s - 1 } = 0$ It remains to observe that $s = k$ . To this end, recall that when $i = s - 1$ , the relation (10) holds for $A _ { i j } \neq 0$ only if $j = s .$ Thus $1 + n _ { s - 1 } - n _ { s } = 0$ and since $n _ { s - 1 } =$ $s - 2$ and $n _ { s } = k - 1$ , we obtain $s = k .$ The proof is complete.■

Perron's original results of 1907 can now be stated as a corollary to Theorems 2 and 15.3.1.

Corollary 2. A positive square matrix A has a real and positive eigenvalue r that has algebraic multiplicity 1 and exceeds the moduli of all other eigenvalues of A. To the eigenvalue r corresponds a positive right eigenvector.

PRooF. The last part of Theorem 2 implies that if $A > O$ we must have $k = 1$ and hence r exceeds the moduli of all other eigenvalues of A.

## 15.5 Reducible Matrices

We now consider the possibility of removing the assumption that A is irreducible from the hypothesis of Theorem 15.3.1. Conclusions (a) and (b) of that theorem yield results for reducible matrices because such a matrix can be thought of as the limit of a sequence of positive (and hence irreducible) matrices. Our conclusions will then follow from the continuous dependence of the dominant eigenvalue (and its normalized right eigenvector) on the matrix elements.

In contrast to this, we know from our experience with perturbation theory in Chapter 11 that the structure of a matrix (as determined by its elementary divisors) does not depend continuously on the matrix elements. For this reason, conclusion (c) of Theorem 15.3.1 yields no useful results in the reducible case.

Theorem 1. If the matrix $A \in \mathbb { R } ^ { n \times n }$ is nonnegative, then

(a) The matrix A has a real eigenvalue, r, equal to the spectral radius of A;

(b) There is a nonnegative (right) eigenvector associated with the eigenvalue r.

PROOF. Define the matrix $D ( t ) \in \mathbb { R } ^ { n \times n }$ by its elements $d _ { i j } ( t )$ as follows:

$$
d _ { i j } ( t ) = \left\{ { a _ { i j } } \begin{array} { l l } { \quad { \mathrm { i f } } \quad a _ { i j } > 0 , } \\ { t \quad } & { { \mathrm { i f } } \quad a _ { i j } = 0 . } \end{array} \right.
$$

Then $D ( t ) > 0$ for $t > 0$ and $D ( 0 ) = A$ Let $\rho ( t )$ be the maximal real eigenvalue of $D ( t )$ for $t > 0$ Then all the eigenvalues of $D ( t )$ are continuous functions of t (Section 11.3) and, since $\rho ( t )$ is equal to the spectral radius of $D ( t )$ for $t > 0 ,$ 1 ${ \mathrm { i m } } _ { t  0 + } \rho ( t ) = r$ is an eigenvalue of $D ( 0 ) = A$ . Furthermore, this eigenvalue is equal to the spectral radius of A.

We also know (see Exercise 11.7.6) that there is a right eigenvector $\pmb { x } ( t )$ that can be associated with $\rho ( t )$ and that depends continuously on t for $t \geq 0$ By Theorem 15.3.1, $\mathbf { \boldsymbol { x } } ( t ) > \mathbf { \boldsymbol { \theta } }$ for $t > 0$ and hence $\mathbf { \boldsymbol { x } } ( t ) \geq \mathbf { \boldsymbol { \theta } }$ at $t = 0 .$

Exercise 1. What happens if we try to extend the results of Theorem 15.4.2 to reducible matrices by means of a continuity argument?

Exercise 2. If $A \in \mathbb { R } ^ { n \times n }$ is nonnegative and $\begin{array} { r } { \sigma _ { j } = \sum _ { k = 1 } ^ { n } \sigma _ { j k } } \end{array}$ , prove that

$$
\operatorname* { m i n } _ { j } \sigma _ { j } \leq r \leq \operatorname* { m a x } _ { j } \sigma _ { j } .
$$

Hint. Note Exercise 15.3.7 and apply a continuity argument.

Exercise 3. Show that for any reducible matrix $A \in \mathbb { R } ^ { n \times n }$ there exists a permutation matrix $P$ such that

$$
\begin{array} { r } { P ^ { \mathrm { T } } A P = \left[ \begin{array} { c c c c } { B _ { 1 1 } } & { B _ { 1 2 } } & { \cdots } & { B _ { 1 k } } \\ { 0 } & { B _ { 2 2 } } & { \cdots } & { B _ { 2 k } } \\ { \vdots } & { \ddots } & { \ddots } & { \vdots } \\ { 0 } & { \cdots } & { 0 } & { B _ { k k } } \end{array} \right] , } \end{array}\tag{1}
$$

where the square matrices $B _ { i i } , i = 1 , 2 , \ldots , k ,$ are either irreducible or $1 \times 1$ zero-matrices.□

The form (1) of A is often called a normal form of a reducible matrix.

Exercise 4. Check that the matrix

$$
A = { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 1 } & { 0 } \\ { 1 } & { 1 } & { 1 } & { 3 } \\ { 1 } & { 0 } & { 2 } & { 0 } \\ { 2 } & { 2 } & { 0 } & { 1 } \end{array} \right] }
$$

is reducible and show that its normal form is

$$
B = { \left[ \begin{array} { l l l l } { 1 } & { 2 } & { ; 0 } & { 2 } \\ { 3 } & { 1 } & { 1 } & { 1 } \\ { . . . . . } & { . . . . } & { . . . } \\ { 0 } & { 0 } & { ; 2 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 0 } \end{array} \right] } .
$$

Exercise 5. If $A \in \mathbb { R } ^ { n \times n }$ and $a _ { j k } > 0$ for $j \neq k ,$ prove that the eigenvalue $\rho$ of A with largest real part is real and has multiplicity 1. Prove also that there is a positive (right) eigenvector of A associated with $\rho _ { \mathrm { \ell } }$ What can be said if we have only $a _ { j k } \geq 0$ for $j \neq k ?$

Hint. Consider $A + \alpha I$ for large α. □

## 15.6 Primitive and Imprimitive Matrices

The Perron-Frobenius theorems make it clear that the structure of a nonnegative irreducible matrix A depends on the number k of eigenvalues whose moduli are equal to the spectral radius of A. In particular, it is convenient to distinguish between the cases $k = 1$ and $k > 1$ . Thus, an irreducible nonnegative matrix is said to be primitive or imprimitive according as $k = 1$ or $k > 1$ . The number k is called the index of imprimitivity.

Exercise 1. Check that any positive matrix is primitive.

Exercise 2. Check that the index of imprimitivity of the matrix

$$
A = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] }
$$

is equal to 2. □

The index of imprimitivity is easily found (see Exercise 2) if the characteristic polynomial is known. Suppose that

$$
c ( \lambda ) = \lambda ^ { n } + a _ { 1 } \lambda ^ { n _ { 1 } } + a _ { 2 } \lambda ^ { n _ { 2 } } + \cdot \cdot \cdot + a _ { t } \lambda ^ { n _ { t } }\tag{1}
$$

is the characteristic polynomial of $A \in \mathbb { R } ^ { n \times n }$ , where $a _ { 1 } , a _ { 2 } , \ldots , a _ { t }$ are nonzero and

$$
n > n _ { 1 } > n _ { 2 } > \cdots > n _ { t } \geq 0 .
$$

If $\lambda _ { 0 }$ is any eigenvalue and $\omega _ { 1 } , \ldots , \omega _ { k }$ are the kth roots of unity, then we saw in Theorem 15.3.1 that $\omega _ { j } \lambda _ { 0 } , j = 1 , 2 , \ldots , k _ { : }$ ,are all eigenvalues of A. Thus, $c ( \lambda )$ is divisible by the product

$$
( \lambda - \omega _ { 1 } \lambda _ { 0 } ) ( \lambda - \omega _ { 2 } \lambda _ { 0 } ) \cdots ( \lambda - \omega _ { k } \lambda _ { 0 } ) = \lambda ^ { k } - \lambda _ { 0 } ^ { k } ,
$$

without remainder. Hence, for some polynomial g and an integer s, we have

$$
c ( \lambda ) = g ( \lambda ^ { k } ) \lambda ^ { s } .
$$

Comparing this with Eq. (1), we see that k is a common factor of the differences $n - n _ { j } , j = 1 , 2 , . . . , t .$ Suppose that l is the greatest common divisor of these differences; then using the reverse argument we see that the spectrum of A is invariant under rotations $2 \pi / l .$ If $k < l ,$ then $2 \pi / l < 2 \pi / k$ and the invariance under rotations through 2π/l is not consistent with the $2 \pi / l$ definition of k. Hence $k = l$ and we have established the following fact.

Proposition 1. If $A \in \mathbb { R } ^ { n \times n }$ is irreducible and nonnegative, and $c ( \lambda )$ written in the form (1) is the characteristic polynomial of A, then k, the index of imprimitivity of A, is the greatest common divisor of the differences

$$
n - n _ { 1 } , \qquad n - n _ { 2 } , \ldots , n - n _ { t } .
$$

For example, if

$$
c ( \lambda ) = \lambda ^ { 1 0 } + a _ { 1 } \lambda ^ { 7 } + a _ { 2 } \lambda , \qquad a _ { 1 } , a _ { 2 } \ne 0 ,
$$

then $k = 3 .$ However, if

$$
c ( \lambda ) = \lambda ^ { 1 0 } + a _ { 1 } \lambda ^ { 7 } + a _ { 2 } \lambda + a _ { 3 } , \qquad a _ { 1 } , a _ { 2 } , a _ { 3 } \ne 0 ,
$$

then k = 1.

The next result provides a rather different characterization of primitive matrices.

Theorem 1. A square nonnegative matrix A is primitive if and only if there is a positive integer p such that $A ^ { p } \ > 0$

ProOF. First suppose that $A ^ { p } > 0$ and hence that $A ^ { p }$ is irreducible. We have seen (Exercise 10.7.1) that A reducible would imply $A ^ { p }$ reducible, hence $A ^ { p } > 0$ implies that A is irreducible. If A has index of imprimitivity $k > 1$ then since the eigenvalues of $A ^ { p }$ are the pth powers of those of A, the matrix $A ^ { p }$ also has index of imprimitivity $k > 1$ . But this contradicts Perron's theorem applied to the positive matrix $A ^ { p }$ . Hence $k = 1$ and A is primitive.

Conversely, we suppose A to be primitive; hence A has a dominant real eigenvalue $r$ of multiplicity 1 (Theorems 15.3.1 and 15.4.2). Using Theorem 9.5.1 and writing $r = \lambda _ { 1 }$ , we have

$$
A ^ { p } = r ^ { p } Z _ { 1 0 } + \sum _ { l = 2 } ^ { s } \sum _ { j = 0 } ^ { m _ { l } - 1 } \ f _ { l , j } Z _ { l j } ,
$$

where $f ( \lambda ) = \lambda ^ { p }$ and $f _ { l , j }$ is the jth derivative of f at $\lambda _ { l }$ . We easily deduce from this equation that, since r is the dominant eigenvalue,

$$
\operatorname * { l i m } _ { p  \infty } { \frac { A ^ { p } } { r ^ { p } } } = Z _ { 1 0 } .\tag{2}
$$

From Exercise 9.9.7 we also have

$$
Z _ { 1 0 } = \frac { C ( r ) } { m ^ { ( 1 ) } ( r ) } ,
$$

and the minimal polynomial m is given by

$$
m ( \lambda ) = ( \lambda - r ) \prod _ { l = 2 } ^ { s } ( \lambda - \lambda _ { l } ) ^ { m _ { l } } .
$$

Since r is the largest real zero of $m ( \lambda )$ and $m ( \lambda )$ is monic, it follows that $m ^ { ( 1 ) } ( r ) > 0$ . Then since $C ( r ) > 0$ (Exercise 15.3.10), we have $Z _ { 1 0 } > 0 .$ It now follows from Eq. (2) that $A ^ { p } > 0$ from some p onward.

Exercise 3. If A is primitive and p is a positive integer, prove that $A ^ { p }$ is primitive.

Exercise 4. If $A \geq 0$ is irreducible and $\varepsilon > 0 _ { : }$ , prove by examining eigenvalues that εI + A is primitive. Compare this with Proposition 15.3.1.

Exercise 5. Check that the first matrix in Exercise 15.1.6 fails to be primitive for any $n > 1$

Exercise 6. Check that the matrices

$$
{ \begin{array} { r l } { { \frac { 1 } { 1 0 } } { \left[ \begin{array} { l l l l } { 9 } & { 0 } & { 1 } & { 1 } \\ { 1 } & { 7 } & { 0 } & { 1 } \\ { 0 } & { 2 } & { 8 } & { 0 } \\ { 0 } & { 1 } & { 1 } & { 8 } \end{array} \right] } \qquad { \mathrm { ~ a n d ~ } } \qquad { \left[ \begin{array} { l l l } { 0 } & { { \frac { 1 } { 2 } } } & { { \frac { 2 } { 3 } } } \\ { { \frac { 3 } { 4 } } } & { 0 } & { { \frac { 1 } { 3 } } } \\ { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 2 } } } & { 0 } \end{array} \right] } } \end{array} }
$$

are primitive.□

The number $p$ such that $A ^ { p } > 0$ for an n × n nonnegative primitive matrix A can be estimated as follows:

$$
p \leq n ^ { 2 } - 2 n + 2 .
$$

Since $p = n ^ { 2 } - 2 n + 2$ for the matrix

$$
A = { \left[ \begin{array} { l l l l l } { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 1 } & & \\ { \vdots } & & & { \ddots } & \\ { 0 } & & & & { 1 } \\ { 1 } & { 1 } & { 0 } & { \cdots } & { 0 } \end{array} \right] } , \qquad A \in \mathbb { R } ^ { n \times n } ,
$$

the estimation (3) is exact. We omit the proof.

## 15.7 Stochastic Matrices

The real matrix $P = [ p _ { i j } ] _ { i , j = 1 } ^ { n }$ is said to be a stochastic matrix if $P \geq \theta$ and all its row sums are equal to 1:

$$
\sum _ { j = 1 } ^ { n } p _ { i j } = 1 , \qquad i = 1 , 2 , \ldots , n .\tag{1}
$$

Matrices of this kind arise in problems of probability theory, which we shall introduce in Section 15.8. In this section we derive some of the more important properties of stochastic matrices.

Theorem 1. A nonnegative matrix P is stochastic if and only if it has the eigenvalue 1 with (right) eigenvector given by $\pmb { \mathscr { u } } = [ 1 \quad 1 \quad \cdots \quad 1 ] ^ { \mathbf { T } }$ . Furthermore, the spectral radius of a stochastic matrix is 1.

ProoF. If P is stochastic, then the condition (1) may obviously be written $P _ { \mathbf { \delta } } \mathbf { \delta } _ { u } = \mathbf { \delta } _ { u }$ . Hence 1 is an eigenvalue with (right) eigenvector u.

Conversely, $P _ { \mathbf { \delta } } \mathbf { \delta } _ { u } = \mathbf { \delta } _ { u }$ implies Eq. (1) and hence that P is stochastic.

For the last part of the theorem we use Exercise 15.3.7 to show that the dominant real eigenvalue of P is 1.

In the next theorem we see that a wide class of nonnegative matrices can be reduced to stochastic matrices by a simple transformation.

Theorem 2. Let A be an n × n nonnegative matrix with maximal real eigenvalue r. If there is a positive (right) eigenvector $\mathbf { x } = [ x _ { 1 } \quad x _ { 2 } \quad \cdot \cdot \cdot \quad x _ { n } ] ^ { \mathrm { T } }$ associated with r and we write $X = \operatorname { d i a g } [ x _ { 1 } , \ldots , x _ { n } ]$ , then

$$
\begin{array} { r } { \pmb { { \cal A } } = r { \pmb { X } } { \pmb { P } } { \pmb { X } } ^ { - 1 } , } \end{array}
$$

where P is a stochastic matrix.

Note that some nonnegative matrices are excluded from Theorem 2 by the hypothesis that x is positive (see Theorem 15.5.1).

PROOF. Let $P = r ^ { - 1 } X ^ { - 1 } A X$ . We have only to prove that P is stochastic. Since $A { \boldsymbol { \mathbf { x } } } = r { \boldsymbol { \mathbf { x } } }$ we have

$$
\sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } = r x _ { i } , \qquad i = 1 , 2 , \ldots , n .
$$

By definition, $p _ { i j } = r ^ { - 1 } x _ { i } ^ { - 1 } a _ { i j } x _ { j }$ and hence

$$
\sum _ { j \mathop { = } 1 } ^ { n } p _ { i j } = r ^ { - 1 } x _ { i } ^ { - 1 } \sum _ { j \mathop { = } 1 } ^ { n } a _ { i j } x _ { j } \mathop { = } 1 .
$$

Thus, P is stochastic and the theorem is proved.■

Finally, we consider the sequence of nonnegative matrices $P , P ^ { 2 } , P ^ { 3 } , \ldots ,$ where P is stochastic. We are interested in conditions under which

$$
P ^ { \infty } = \operatorname* { l i m } _ { p \to \infty } P ^ { p }
$$

exists. We already know that $P ^ { \infty } \neq \theta ,$ for P has an eigenvalue equal to 1 and $P ^ { r }  0$ as $r \to \infty$ if and only if all the eigenvalues of P are less than 1 (Exercise 11.1.8).

Theorem 3. If P is an irreducible stochastic matrix, then the matrix $P ^ { \infty }$ $= \operatorname* { l i m } _ { p \to \infty } P ^ { p }$ exists if and only if P is primitive.

PRooF. We know that the maximal real eigenvalue $\lambda _ { 1 }$ of $P$ is equal to 1. Recall that, since P is irreducible, the eigenvalue 1 is unrepeated (Theorem 15.3.1(c)). So let $\lambda _ { 2 } , \ldots , \lambda _ { k }$ be the other eigenvalues of $P$ with modulus 1 and let $\lambda _ { k + 1 } , \ldots , \lambda _ { s }$ be the distinct eigenvalues of P with modulus less than 1. We write $f ( \lambda ) = \lambda ^ { p }$ and $f _ { l , . }$ for the jth derivative of f at $\lambda _ { l }$ , and using Theorem 9.5.1 again we have

$$
P ^ { p } = Z _ { 1 0 } + \sum _ { l = 2 } ^ { k } \sum _ { j = 0 } ^ { m _ { l } - 1 } f _ { l , j } Z _ { l j } + \sum _ { l = k + 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { l } - 1 } f _ { l , j } Z _ { l j } .\tag{2}
$$

For p sufficiently large we have

$$
f _ { l , j } = \frac { p ! } { ( p - j + 1 ) ! } \lambda _ { l } ^ { p - j + 1 } ,\tag{3}
$$

and since $| \lambda _ { l } | < 1$ for $l = k + 1 , \ldots , s ,$ it follows that the last term in $\mathtt { E q }$ (2) approaches the zero-matrix as $p  \infty$ . If we now assume that P is primitive, then the second term on the right of Eq. (2) does not appear. Hence it is clear that $P ^ { \infty }$ exists and, furthermore $P ^ { \infty } = Z _ { 1 0 }$

Conversely, suppose it is known that $P ^ { \infty }$ exists; then we deduce from Eq. (2) that

$$
Q = \operatorname* { l i m } _ { p  \infty } \sum _ { l = 2 } ^ { k } \sum _ { j = 0 } ^ { m _ { l } - 1 } f _ { l , j } Z _ { l j }
$$

exists. The $m _ { 2 } + m _ { 3 } + \cdots + m _ { k }$ matrices $Z _ { \imath j }$ appearing in this summation are linearly independent members of $\mathbb { C } ^ { n \times n }$ (Theorem 9.5.1) and generate a subspace ${ \mathcal { S } } ,$ say, of $\mathbb { C } ^ { n \times n }$ . Since $Q$ must also belong to ${ \mathcal { S } } ,$ there are numbers $a _ { i j }$ such that

$$
Q = \sum _ { l = 2 } ^ { k } \sum _ { j = 0 } ^ { m _ { l } - 1 } a _ { l j } Z _ { l j } .
$$

It now follows that, for each l and $j ,$

$$
a _ { l j } = \operatorname* { l i m } _ { p \to \infty } f _ { l , j } .
$$

But for $l = 2 , 3 , \ldots ,$ we have $| \lambda _ { l } | = 1 ( \lambda _ { l } \neq 1 )$ and it follows from Eq. (3) that the limit on the right does not exist. Thus, we have a contradiction that can be resolved only if the existence of $P ^ { \infty }$ implies $k = 1$

It should be noted that the hypothesis that P be irreducible is not necessary. It can be proved that the eigenvalue 1 of P has only linear elementary divisors even when P is reducible. Thus, Eq. (2) is still valid and the above argument goes through. The proof of the more general result requires a deeper analysis of reducible nonnegative matrices than we have chosen to present.

Note also that, using Exercise 9.9.7, we may write

$$
P ^ { \infty } = \frac { C ( 1 ) } { m ^ { ( 1 ) } ( 1 ) } ,
$$

where $C ( \lambda )$ and $m ( \lambda )$ are the reduced adjoint and the minimal polynomial of $P ,$ respectively. If $B ( \lambda ) = \mathrm { a d j } ( I \lambda - P )$ and $c ( \lambda )$ is the characteristic polynomial of $P ,$ then the polynomial identity

$$
{ \frac { B ( \lambda ) } { c ( \lambda ) } } = { \frac { C ( \lambda ) } { m ( \lambda ) } }
$$

implies that we may also write

$$
P ^ { \infty } = \frac { B ( 1 ) } { c ^ { ( 1 ) } ( 1 ) } .
$$

Yet another alternative arises if we identify $Z _ { 1 0 }$ with the constituent matrix $G _ { 1 }$ of Exercise 4.14.3. Thus, in the case in which P is irreducible, there are positive right and left eigenvectors $\mathbf { x } , \mathbf { y } ;$ respectively, of P associated with the eigenvalue 1 such that

$$
y ^ { \mathrm { T } } x = 1 \qquad { \mathrm { a n d } } \qquad P ^ { \infty } = { \bf x } y ^ { \mathrm { T } } .\tag{4}
$$

Exercise 1. A nonnegative matrix $P \in \mathbb { R } ^ { n \times n }$ is called doubly stochastic if both P and $P ^ { \mathbf { T } }$ are stochastic matrices. Check that the matrices

$$
P _ { 1 } = { \left[ \begin{array} { l l l } { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 3 } } } & { 0 } \\ { 0 } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 3 } } } & { 0 } & { { \frac { 2 } { 3 } } } \end{array} \right] } \qquad \mathrm { ~ a n d ~ } \qquad P _ { 2 } = { \left[ \begin{array} { l l l } { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } \\ { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 3 } } } & { 0 } \\ { 0 } & { { \frac { 1 } { 3 } } } & { { \frac { 2 } { 3 } } } \end{array} \right] }
$$

are stochastic and doubly stochastic matrices, respectively, and that $P _ { 1 } ^ { \infty }$ and $P _ { 2 } ^ { \infty }$ exist. □

## 15.8 Markov Chains

Nonnegative matrices arise in a variety of physical problems. We shall briefly present a problem of probability theory that utilizes some of the theorems developed earlier in the chapter.

For simplicity, we consider a physical system whose state, or condition, or position, can be described in n mutually exclusive and exhaustive ways. We let $s _ { 1 } , s _ { 2 } , \ldots , s _ { n }$ denote these states. We suppose it possible to examine the system at times $t _ { 0 } < t _ { 1 } < t _ { 2 } < \cdots$ and to observe the state of the system at each of these times. We suppose further that there exist absolute probabilities $p _ { i } ( t _ { r } )$ of finding the system in state $s _ { i }$ at time $t _ { r }$ for $i = 1 , 2 , \ldots , n$ and $r = 0 , 1 , 2 , \ldots$ . Since the system must be in one of the n states at time $t _ { r }$ we have

$$
\sum _ { i = 1 } ^ { n } p _ { i } ( t _ { r } ) = 1 , \qquad r = 0 , 1 , 2 , \ldots .\tag{1}
$$

It is assumed that we can determine the probability that state $s _ { i }$ is attained at time $t _ { r }$ after having been in state $s _ { j }$ at time $t _ { r - 1 } ,$ for all i and j. Thus, we assume a knowledge of the conditional probability

$$
q _ { i j } ( t _ { r } | t _ { r - 1 } ) , \qquad i , j = 1 , 2 , \ldots , n ,
$$

of being in state $\pmb { s _ { i } }$ at time $t _ { r } ,$ given that the system is in state s, at time $s _ { j }$ $t _ { r - 1 }$ The laws of probability then imply

$$
p _ { i } ( t _ { r } ) = \sum _ { j = 1 } ^ { n } q _ { i j } ( t _ { r } | t _ { r - 1 } ) p _ { j } ( t _ { r - 1 } ) ,
$$

$\mathbf { o r } ,$ in matrix-vector form,

$$
\pmb { p } _ { r } = Q ( t _ { r } , t _ { r - 1 } ) \pmb { p } _ { r - 1 } , \qquad r = 1 , 2 , \ldots ,\tag{2}
$$

where we define

$$
\pmb { p } _ { s } = [ p _ { 1 } ( t _ { s } ) \quad p _ { 2 } ( t _ { s } ) \quad \cdots \quad p _ { n } ( t _ { s } ) ] ^ { \mathrm { T } } , \qquad s = 0 , 1 , 2 , \ldots ,
$$

and $Q ( t _ { r } , t _ { r - 1 } )$ to be the matrix in $\mathbb { R } ^ { n \times n }$ with elements $q _ { i j } ( t _ { r } | t _ { r - 1 } )$ , called the transition matrix

Since the system must go to one of the n states at time $t _ { r }$ after being in state j at time $t _ { r - 1 }$ , it follows that

$$
\sum _ { i = 1 } ^ { n } q _ { i j } ( t _ { r } | t _ { r - 1 } ) = 1 .\tag{3}
$$

Finally, it is assumed that the initial state of the system is known. Thus, if the initial state is $\pmb { S _ { i } }$ then we have $\begin{array} { r } { p _ { 0 } = e _ { i } , } \end{array}$ , the vector with 1 in the ith place and zeros elsewhere. We deduce from Eq. (2) that at time $t _ { r }$ we have

$$
\pmb { p } _ { r } = Q ( t _ { r } , t _ { r - 1 } ) Q ( t _ { r - 1 } , t _ { r - 2 } ) \cdots Q ( t _ { 1 } , t _ { 0 } ) \pmb { p } _ { 0 } .\tag{4}
$$

The process we have just described is known as a Markov chain. If the conditional probabilities $q _ { i j } ( t _ { r } | t _ { r - 1 } )$ are independent of t or are the same at each instant $t _ { 0 } , t _ { 1 } , t _ { 2 } , \ldots ,$ then the process is described as a homogeneous Markov chain. We shall confine our attention to this relatively simple problem. Observe that we may now write

$$
Q ( t _ { r } , t _ { r - 1 } ) = Q , \qquad r = 1 , 2 , \ldots .
$$

Equation (4) becomes

$$
p _ { r } = Q ^ { r } p _ { 0 } ,
$$

and Eq. (3) implies that the transition matrix $Q$ associated with a homogenous Markov chain is such that $Q ^ { \mathbf { r } }$ is stochastic. For convenience, we define $\pmb { P } = \pmb { Q } ^ { \pmb { \mathsf { T } } }$

In many problems involving Markov chains, we are interested in the limiting behavior of the sequence $\pmb { p } _ { 0 } , \pmb { p } _ { 1 } , \pmb { p } _ { 2 } , \dots$ . This leads us to examine the existence of $\operatorname* { l i m } _ { r \to \infty } Q ^ { r } ,$ or $\mathrm { l i m } _ { r \to \infty } P ^ { r } .$ If P (or Q) is irreducible, then according to Theorem 15.7.3, the limits exist if and only if P is primitive. Since ${ \pmb P } = { \pmb Q } ^ { \pmb r }$ it follows that $Q$ has an eigenvalue 1, and the associated right and left eigenvectors x, y of Eq. (15.7.4) are left and right eigenvectors of $Q ,$ respectively. Thus, there are positive right and left eigenvectors ${ \boldsymbol { \xi } } \ ( = y )$ and ${ \pmb \eta } \left( = { \pmb x } \right)$ associated with the eigenvalue 1 of $\varrho$ for which $\pmb { \eta } ^ { \tt T } \pmb { \zeta } = 1$ and

$$
Q ^ { \infty } = \xi \eta ^ { \mathrm { \pmb { r } } } .
$$

We then have

$$
\pmb { p } _ { \infty } = \xi ( \pmb { \eta } ^ { \mathrm { T } } \pmb { p } _ { 0 } ) = ( \pmb { \eta } ^ { \mathrm { T } } \pmb { p } _ { 0 } ) \xi ,
$$

since $\pmb { \eta } ^ { \mathrm { { T } } } \pmb { p } _ { 0 }$ is a scalar. So, whatever the starting vector ${ \pmb { p } } _ { 0 }$ , the limiting vector is proportional to $\pmb { \xi } .$ However, ${ \pmb { p } } ,$ satisfies the condition (1) for every r and so ${ \pmb { p _ { 0 } } }$ satisfies the same condition. Thus, if we define the positive vector $\pmb { \xi } = [ \xi _ { 1 } \quad \xi _ { 2 } \quad \ldots \quad \xi _ { n } ] ^ { \mathbf { T } }$ so that $\sum _ { i = 1 } ^ { n } \xi _ { i } = 1$ , then $\pmb { p _ { \infty } } = \pmb { \xi }$ for every possible choice of ${ \pmb { p _ { 0 } } }$

The fact that $\xi > \theta$ means that it is possible to end up in any of the n states $s _ { 1 } , s _ { 2 } , \ldots , s _ { n }$ . We have proved the following result.

Theorem 1. If Q is the transition matrix of a homogeneous Markov chain and $Q$ is irreducible, then the limiting absolute probabilities $p _ { i } ( t _ { \infty } )$ exist if and only if Q is primitive. Furthermore, when $\boldsymbol { Q }$ is primitive, $p _ { i } ( t _ { \infty } ) > 0$ for $i = 1 , 2 , \ldots , n$ and these probabilities are the components of the (properly normalized) right eigenvector of $Q$ associated with the eigenvalue 1.

# A Survey of Scalar Polynomials

The expression

$$
p ( \lambda ) = p _ { 0 } + p _ { 1 } \lambda + p _ { 2 } \lambda ^ { 2 } + \cdot \cdot \cdot + p _ { l } \lambda ^ { l } ,\tag{1}
$$

with coefficients $p _ { 0 } , p _ { 1 } , \ldots , p _ { l }$ in a field $\mathcal { F }$ and $p _ { l } \neq 0 ,$ is referred to as a polynomial of degree l over $\mathcal { F } .$ Nonzero scalars from $\mathcal { F }$ are considered polynomials of zero degree, while $p ( \lambda ) \equiv 0$ is written for polynomials with all zero coefficients.

In this appendix we give a brief survey of some of the fundamental properties of such polynomials. An accessible and complete account can be found in Chapter 6 of “The Theory of Matrices" by Sam Perlis (Addison Wesley, 1958), for example

Theorem 1. For any two polynomials $p ( \lambda )$ and $q ( \lambda )$ over $\mathcal { F }$ (with $q ( \lambda ) \not \equiv 0 )$ 5 there exist polynomials $d ( \lambda )$ and $r ( \lambda )$ over $\mathcal { F }$ such that

$$
\begin{array} { r } { p ( \lambda ) = q ( \lambda ) d ( \lambda ) + r ( \lambda ) , } \end{array}\tag{2}
$$

where deg $r ( \lambda ) < \deg { q ( \lambda ) } o r r ( \lambda ) \equiv 0$ . The polynomials $d ( \lambda )$ and $r ( \lambda )$ satisfying Eq. (2) are uniquely defined

The polynomial $d ( \lambda )$ in Eq. (2) is called the quotient on division of $p ( \lambda )$ by $q ( \lambda )$ and $r ( \lambda )$ is the remainder of this division. If the remainder $r ( \lambda )$ in Eq. (2) is the zero polynomial, then $d ( \lambda )$ (or $q ( \lambda ) )$ is referred to as a divisor of $p ( \lambda )$ In this event, we also say that $d ( \lambda )$ (or $q ( \lambda ) )$ divides $p ( \lambda )$ , or that $p ( \lambda )$ is divisible by $d ( \lambda )$ . A divisor of degree 1 is called linear.

Exercise 1. Find the quotient and the remainder on division of $p ( \lambda )$ $= \lambda ^ { 3 } + \lambda + 2  { \mathbf { b } }  { \mathbf { y } } q ( \lambda ) = \lambda ^ { 2 } + \lambda + 1$

Answer. $d ( \lambda ) = \lambda - 1 , r ( \lambda ) = \lambda + 3 .$

Exercise 2. Show that $p ( \lambda )$ divides $q ( \lambda )$ and simultaneously $q ( \lambda )$ divides $p ( \lambda )$ if and only if $p ( \lambda ) = c q ( \lambda )$ for some $c \in { \mathcal { F } } , \ \sqsupset$

Given polynomials $p _ { 1 } ( \lambda ) , p _ { 2 } ( \lambda ) , \ldots , p _ { k } ( \lambda ) .$ q(λ) over ${ \mathcal { F } } ,$ the polynomial $q ( \lambda )$ is called a common divisor of $p _ { i } ( \lambda ) ( i = 1 , 2 , \ldots , k )$ if it divides each of the polynomials $p _ { i } ( \lambda )$ . A greatest common divisor $d ( \lambda )$ of $p _ { i } ( \lambda ) ( i = 1 , 2 , \ldots , k )$ abbreviated ${ \bf g . c . d . } \{ p _ { i } ( \lambda ) \}$ , is defined to be a common divisor of these polynomials that is divisible by any other common divisor. To avoid unnecessary complications, we shall assume in the remainder of this section (if not indicated otherwise) that the leading coefficient, that is, the coefficient of the highest power of the polynomial being considered, is equal to 1. Such polynomials are said to be monic.

Theorem 2. For any set of nonzero polynomials over $\mathcal { F } ,$ there exists a unique greatest common divisor.

This result follows immediately from the definition of a greatest common divisor. If the greatest common divisor of a set of polynomials is 1, then they are said to be relatively prime.

Exercise 3. Check that the polynomials $p ( \lambda ) = \lambda ^ { 2 } + 1$ and $q ( \lambda ) = \lambda ^ { 3 } + 1$ are relatively prime.

Exercise 4. Construct a set of three relatively prime polynomials, no two of which are relatively prime. □

Theorem 3. If $d ( \lambda )$ is the greatest common divisor of $p _ { 1 } ( \lambda )$ and $p _ { 2 } ( \lambda ) _ { : }$ then there exist polynomials $c _ { 1 } ( \lambda )$ and $c _ { 2 } ( \lambda )$ such that

$$
c _ { 1 } ( \lambda ) p _ { 1 } ( \lambda ) + c _ { 2 } ( \lambda ) p _ { 2 } ( \lambda ) = d ( \lambda ) .
$$

In particular, if $p _ { 1 } ( \lambda )$ and $p _ { 2 } ( \lambda )$ are relatively prime, then

$$
c _ { 1 } ( \lambda ) p _ { 1 } ( \lambda ) + c _ { 2 } ( \lambda ) p _ { 2 } ( \lambda ) = 1\tag{3}
$$

for some polynomials $c _ { 1 } ( \lambda )$ and $c _ { 2 } ( \lambda )$

This important theorem requires more proof. The argument is omitted in the interest of brevity.

Let $\begin{array} { r } { \lambda _ { 1 } \in \mathcal { F } . \mathrm { ~ H f ~ } p ( \lambda _ { 1 } ) = \sum _ { i = 0 } ^ { l } p _ { i } \lambda _ { 1 } ^ { i } = 0 , } \end{array}$ then $\lambda _ { 1 }$ is a zero of $p ( \lambda )$ or a root of the equation $\begin{array} { r } { p ( \lambda ) = 0 . } \end{array}$ The fundamental theorem of algebra concerns the zeros of a polynomial over C.

Theorem 4. Any polynomial over C of nonzero degree has at least one zero in C.

Dividing $p ( \lambda )$ by $( \lambda - \lambda _ { 1 } )$ with the use of Theorem 1, the next exercise is easily established.

Exercise 5. Show that $\lambda _ { 1 }$ is a zero of $p ( \lambda )$ if and only if $\lambda - \lambda _ { 1 }$ is a (linear) divisor of $p ( \lambda )$ . In other words, for some polynomial $p _ { 1 } ( \lambda )$ over ${ \mathcal { F } } ,$

$$
p ( \lambda ) = p _ { 1 } ( \lambda ) ( \lambda - \lambda _ { 1 } ) . ~ \varTheta\tag{4}
$$

Let λ, be a zero of p(λ). It may happen that, along with $\lambda _ { 1 }$ $p ( \lambda )$ $\lambda - \lambda _ { 1 }$ , higher powers, $( \lambda - \lambda _ { 1 } ) ^ { 2 } , ( \lambda - \lambda _ { 1 } ) ^ { 3 } , \ldots ,$ are also divisors of $p ( \lambda )$ . The scalar $\lambda _ { 1 } \in \mathcal { F }$ is referred to as a zero of $p ( \lambda )$ of multiplicity k if $( \lambda - \lambda _ { 1 } ) ^ { k }$ divides $p ( \lambda )$ but $( \lambda - \lambda _ { 1 } ) ^ { k + 1 }$ does not. Zeros of multiplicity 1 are said to be simple. Óther zeros are called multiple zeros of the polynomial.

Exercise 6. Check that λ1 is a zero of multiplicity k of p(λ) if and only if $\lambda _ { 1 }$ $p ( \lambda )$ $p ( \lambda _ { 1 } ) = p ^ { \prime } ( \lambda _ { 1 } ) = \cdot \cdot \cdot = p ^ { ( k - 1 ) } ( \lambda _ { 1 } ) = 0$ but $p ^ { ( k ) } ( \bar { \lambda } _ { 1 } ) \neq 0$ □

Consider again the equality (4) and suppose $p _ { 1 } ( \lambda )$ has nonzero degree. By virtue of Theorem 4 the polynomial $p _ { 1 } ( \lambda )$ has a zero $\lambda _ { 2 }$ . Using Exercise 5, we obtain $p ( \lambda ) = p _ { 2 } ( \lambda ) ( \lambda - \lambda _ { 2 } ) ( \lambda - \lambda _ { 1 } )$ . Proceeding to factorize ${ \pmb p } _ { 2 } ( \lambda )$ and continuing this process, the following theorem is obtained.

Theorem 5. Any polynomial over C of degree $l \ ( l \geq 1 )$ has exactly l zeros $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { l }$ in C (which may include repetitions). Furthermore, there is a representation

$$
p ( \lambda ) = p _ { l } ( \lambda - \lambda _ { l } ) ( \lambda - \lambda _ { l - 1 } ) \cdots ( \lambda - \lambda _ { 1 } ) ,\tag{5}
$$

where $p _ { l } = 1$ in the case of a monic polynomial $p ( \lambda )$

Collecting the equal zeros in Eq. (5) and renumbering them, we obtain

$$
p ( \lambda ) = p _ { l } ( \lambda - \lambda _ { 1 } ) ^ { k _ { 1 } } ( \lambda - \lambda _ { 2 } ) ^ { k _ { 2 } } \cdot \cdot \cdot ( \lambda - \lambda _ { s } ) ^ { k _ { s } } ,\tag{6}
$$

where $\lambda _ { i } \neq \lambda _ { j } ( i \neq j )$ and $k _ { 1 } + k _ { 2 } + \cdots + k _ { s } = l .$

Given $p _ { 1 } ( \lambda ) , p _ { 2 } ( \lambda ) , \ldots , p _ { k } ( \lambda )$ , the polynomial $p ( \lambda )$ is said to be a common multiple of the given polynomials if each of them divides $p ( \lambda )$

$$
p ( \lambda ) = q _ { i } ( \lambda ) p _ { i } ( \lambda ) , \quad \quad 1 \leq i \leq k ,\tag{7}
$$

for some polynomials $q _ { i } ( \lambda )$ over the same field. A common multiple that is a divisor of any other common multiple is called a least common multiple of the polynomials.

Theorem 6. For any set of monic polynomials, there exists a unique monic least common multiple.

Exercise 7. Show that the product $\prod _ { i = 1 } ^ { k } p _ { i } ( \lambda )$ is a least common multiple of the polynomials $p _ { 1 } ( \lambda ) , p _ { 2 } ( \lambda ) , \ldots , p _ { k } ( \lambda )$ if and only if any two of the given polynomials are relatively prime.

Exercise 7 can now be used to complete the next exercise.

Exercise 8. Check that if $p ( \lambda )$ is the least common multiple of $p _ { 1 } ( \lambda )$ $p _ { 2 } ( \lambda ) , \ldots , p _ { k } ( \lambda )$ , then the polynomials $q _ { i } ( \lambda ) ~ ( i = 1 , 2 , \ldots , k )$ in Eq. (7) are relatively prime. □

Note that the condition in Exercise 7 is stronger than requiring that the set of polynomials be relatively prime.

Exercise 9. Prove that if $\tilde { p } ( \lambda )$ is the least common multiple of $p _ { 1 } ( \lambda ) _ { : }$ $p _ { 2 } ( \lambda ) , \ldots , p _ { k - 1 } ( \lambda )$ , then the least common multiple of $p _ { 1 } ( \lambda ) , p _ { 2 } ( \lambda ) , \ldots , p _ { k } ( \lambda )$ coincides with the least common multiple of $\tilde { p } ( \lambda )$ and $p _ { \pmb { k } } ( \lambda )$ □

A field $\mathcal { F }$ that contains the zeros of every polynomial over $\mathcal { F }$ is said to be algebraically closed. Thus Theorem 4 asserts, in particular, that the field C of complex numbers is algebraically closed. Note that the polynomial $p ( \lambda ) = \lambda ^ { 2 } + 1$ viewed as a polynomial over the field R of real numbers shows that R fails to be algebraically closed.

If $p ( \lambda )$ is a polynomial over $\mathcal { F }$ of degree l, and 1 is the only monic polynomial over $\mathcal { F }$ of degree less than l that divides $p ( \lambda )$ , then $p ( \lambda )$ is said to be irreducible over $\mathcal { F } .$ Otherwise, $p ( \lambda )$ is reducible over $\mathcal { F } .$ Obviously, in view of Exercise ${ \mathfrak { s } } ,$ every polynomial of degree greater than 1 over an algebraically closed field is reducible. In fact, if $p ( \lambda )$ is a monic polynomial over an algebraically closed field $\mathcal { F }$ and $p ( \lambda )$ has degree $l ,$ then $p ( \lambda )$ has a factorization $p ( \lambda ) = \prod _ { j = 1 } ^ { l } ( \lambda - \lambda _ { j } )$ into linear factors, where $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { l } \in \mathcal { F }$ and are not necessarily distinct. If the field fails to be algebraically closed, then polynomials of degree higher than 1 may be irreducible.

Exercise 10. Check that the polynomial $p ( \lambda ) = \lambda ^ { 2 } + 1$ is irreducible over R and over the field of rational numbers but is reducible over $\mathbb { C } . \ \sqcap$

Note that all real polynomials of degree greater than 2 are reducible over $\mathbb { R } ,$ while for any positive integer l there exists a polynomial of degree l with rational coefficients that is irreducible over the field of rational numbers.

# Some Theorems and Notions from Analysis

In this appendix we discuss without proof some important theorems of analysis that are used several times in the main body of the book. We present the results in a setting sufficiently general for our applications, although they can be proved just as readily in a more general context. We first need some definitions.

Recall that in $\mathbb { C } ^ { n }$ any vector norm may be used as a measure of magnitude of distance (Section 10.2). Given a vector norm $\parallel \parallel$ on $\mathbb { C } ^ { n }$ and a real number $\varepsilon > 0 _ { ; }$ , we define a neighbourhood $\mathcal { N } _ { \varepsilon } ( \mathbf { x } _ { 0 } )$ of $\ b { x _ { 0 } } \in \mathbb { C } ^ { n }$ to be the set of vectors (also called points in this context) x in $\mathbb { C } ^ { n }$ for which $\| \pmb { x } - \pmb { x _ { 0 } } \| < \varepsilon$ (that is, it is the interior of a ball with centre $\pmb { x } _ { 0 }$ and radius ε; see Section 10.2). If $\mathcal { S }$ is a set of points of $\mathbb { C } ^ { n } ,$ then $\pmb { x } \in \mathbb { C } ^ { n }$ is a limit point of $\mathcal { S }$ if every neighbourhood of x contains some point $\pmb { y } \in \mathcal { S }$ with ${ \pmb y } \neq { \pmb x } .$ The set $\mathcal { S }$ is said to be open if it is a union of neighbourhoods, and closed if every limit point of $\mathcal { S }$ is in S. A set $\mathcal { S }$ is bounded if there is a real number $K \geq 0$ and an $\boldsymbol { \mathbf { \mathit { x } } } \in \mathbb { C } ^ { n }$ such that $\| { \boldsymbol { y } } - { \boldsymbol { x } } \| < K$ for all $\pmb { y } \in \mathcal { S } .$

Clearly, these definitions can be applied to sets in C or in R. We have only to replace the norm by the absolute value function. We can now state the first result.

Theorem 1. Let X be a closed and bounded set of real numbers and let M and m be the least upper bound and greatest lower bound, respectively, of the numbers x in X. Then M, $m \in { X }$

The proof is a straightforward deduction from the definitions.

Now consider a function $f$ with values in $\mathbb { C } ^ { m }$ and defined on an open set ${ \mathcal { S } } \subseteq \mathbb { C } ^ { n }$ We say that $f$ is continuous at a point $\pmb { x } \in \mathcal { S }$ if, given $\varepsilon > 0 ,$ there is a $\delta > 0$ such that $\mathbf { \boldsymbol { y } } \in \mathcal { N } _ { \delta } ( \mathbf { \boldsymbol { x } } )$ implies

$$
\| f ( \mathbf { y } ) - f ( \mathbf { x } ) \| < \varepsilon .
$$

We say that $f$ is continuous on $\mathcal { S }$ if f is continuous at every point of ${ \mathcal { S } } .$ $\mathbf { I f } \mathbf { \mathcal { S } }$ is closed, then $f$ is continuous on $\mathcal { S }$ if it is continuous on some open set containing $\mathcal { S } .$ The range $f ( \mathcal S )$ of the function $f$ is a subset of $\mathbb { C } ^ { m }$ defined by saying that ${ \pmb a } \in f ( { \mathcal { S } } )$ if and only if there is a vector $\pmb { b } \in \mathbb { C } ^ { n }$ such that $a = f ( b )$

Theorem 2. Let f be defined as above. $I f { \mathcal { S } }$ is a closed and bounded set in $\mathbb { C } ^ { n }$ and f is continuous on ${ \mathcal { S } } ,$ then $f ( \mathcal S )$ is a closed and bounded subset $o f \mathbb { C } ^ { m } ,$

ln Theorem 2 and the next theorem we may replace $\mathbb { C } ^ { n }$ by $\mathbb { R } ^ { n }$ or $\mathbb { C } ^ { m }$ by $\mathbb { R } ^ { m }$ , or both. The next theorem is obtained by combining Theorems 1 and 2.

Theorem 3. Let f be a continuous real-valued function defined on a closed and bounded subset $\mathcal { S }$ of C". If

$$
M = \operatorname* { s u p } _ { \mathbf { x } \in \mathcal { S } } f ( \mathbf { x } ) , \qquad m = \operatorname* { i n f } _ { \mathbf { x } \in \mathcal { S } } f ( \mathbf { x } ) ,
$$

then there are vectors y, $\pmb { z } \in \mathcal { S }$ such that

$$
M = f ( { \pmb y } ) , ~ { \pmb m } = f ( { \pmb z } ) .
$$

In this statement $\operatorname { s u p } _ { x \in \mathcal { S } } f ( x )$ is read, “the supremum, or least upper bound, of the numbers $f ( x )$ , where $\pmb { x } \in \mathcal { S } . ^ { \pmb { \mathscr { s } } }$ Similarly, $\operatorname { i n f } _ { x \in \mathcal { S } } f ( x )$ denotes an infimum or greatest lower bound.

Theorem 2 tells us that, under the hypotheses of Theorem 3, $f ( \mathcal S )$ is a closed and bounded set of real numbers and the result then follows from Theorem 1. It may be said that, under the hypotheses of Theorem 3, f has a maximum and a minimum on $\mathcal { S }$ and we may write

$$
\operatorname* { s u p } _ { x \in \mathcal { S } } f ( { \pmb x } ) = \operatorname* { m a x } _ { { \pmb x } \in \mathcal { S } } f ( { \pmb x } ) , \qquad \operatorname* { i n f } _ { { \pmb x } \in \mathcal { S } } f ( { \pmb x } ) = \operatorname* { m i n } _ { { \pmb x } \in \mathcal { S } } f ( { \pmb x } ) .
$$

We now show in the following example that the three conditions of Theorem $3 - f$ continuous on ${ \mathcal { S } } , { \mathcal { S } }$ bounded, and $\mathcal { S }$ closed—are all necessary.

Exercise 1. (a) Let $f ( x ) = x ,$ and let $\mathcal { S }$ be the open interval $( 0 , 1 )$ Here $\mathcal { S }$ is bounded but not closed and $f$ is continuous on $\mathcal { S } .$ Clearly $M = 1$ $m = 0 ,$ , and $f$ does not attain these values on ${ \mathcal { S } } .$

(b) With $f ( x ) = 1 / x$ and $\mathcal { S }$ the set of all real numbers not less than 1, we have $f$ continuous on $\mathcal { S }$ and $\mathcal { S }$ closed but unbounded. In this case $f ( \mathcal S )$ is the half-open interval $( 0 , 1 ]$ and in $\operatorname { f } _ { x \in { \mathcal { S } } } f ( x ) = 0$ is not attained.

(c) With

$$
f ( x ) = \left\{ { x , \atop D , \qquad x = 1 , } \right.
$$

we have $\mathcal { S } = [ 0 , 1 ]$ , which is closed and bounded, but $f$ is not continuous on ${ \mathcal { S } } .$ Now $f ( \mathcal { S } ) = [ 0 , 1 ]$ and $\mathbf { s u p } _ { x \in \mathcal { S } } f ( x ) = 1$ is not attained. □

A set $\mathcal { S }$ in the complex plane C is said to be convex if for any ${ \mathfrak { X } } _ { 1 } , { \mathfrak { X } } _ { 2 } \in { \mathcal { S } }$ and any $\theta \in [ 0 , 1 ]$

$$
( 1 - \theta ) { \alpha } _ { 1 } + \theta { \alpha } _ { 2 } \in \mathcal { S } .
$$

The convex set that contains the points $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { k }$ and is included in any other convex set containing them is called the convex hull of $\alpha _ { 1 } , \alpha _ { 2 }$ $\dots , \alpha _ { k }$ . In other words, the convex hull is the minimal convex set containing the given points.

Exercise 2. Prove that the convex hull of $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { k }$ in $\mathbb { C }$ is the set of all linear combinations of the form

$$
\theta _ { 1 } \alpha _ { 1 } + \theta _ { 2 } \alpha _ { 2 } + \cdot \cdot \cdot + \theta _ { k } \alpha _ { k } , \qquad \theta _ { i } \geq 0 \quad \mathrm { a n d } \quad \sum _ { i = 1 } ^ { k } \theta _ { i } = 1 .\tag{1}
$$

(Such sums are called convex linear combinations.)

Hint. First show that the set of elements given by (1) is convex, and then check its minimality (in the previous sense) by use of an induction argument.

The notion of convexity can be extended to linear spaces in a natural way. Thus, let $\mathcal { X }$ be a linear space over $\mathcal { F }$ (where $\mathcal { F }$ is R or C). The line segment joining members x and $\pmb { y }$ of $\mathcal { X }$ is the set of elements of the form $( 1 - \theta ) { \mathbf x } + \theta { \mathbf y }$ where $\theta \in [ 0 , 1 ]$ . Then a subset $\mathcal { S }$ of $\mathcal { X }$ is said to be convex if, for each pair x and y in ${ \mathcal { S } } ,$ the line segment joining x and $\pmb { y }$ is also in $\mathcal { S } .$ For example, it is easily seen that any subspace of $\mathcal { X }$ is convex.

Exercise 3. Show that any ball in $\mathbb { C } ^ { n }$ is a convex set.

Exercise 4. Let $A \in \mathbb { C } ^ { m \times n }$ and $\pmb { b } \in \mathbb { C } ^ { m }$ . Show that the solution set of $A \pmb { x } = \pmb { b }$ is a convex set (when it is not empty).

# Suggestions for Further Reading

In this appendix, references to several books and papers are collected that cast more light on the subject matter of the book. They may extend the (finite-dimensional) theory further, or go more deeply into it, or contain interesting applications. Some of them have also provided sources of information and stimulation for the authors.

The list is prepared alphabetically by author, and the numbers in square brackets after each reference indicate the chapters of this book to which the reference is mainly related.

Barnett, S. Polynomials and Linear Control Systems. New York: Marcel Dekker, 1983. [13]

Barnett, S., and Storey, C. Matrix Methods in Stability Theory. London: Nelson, 1970. [13]

Baumgärtel, H. Endlich-dimensionale Analytishe Störungstheory. Berlin: Academie-Verlag, 1972. [11] To appear in English translation by Birkhäuser Verlag.

Bellman, R. Introduction to Matrix Analysis. New York: McGraw-Hill, 1960. [1–15]

Ben-Israel, A., and Greville, T. N. E. Generalized Inverses: Theory and Applications. New York: Wiley, 1974. [12]

Berman, A., and Plemmons, R. J. Nonnegative Matrices in the Mathematical Sciences. New York: Academic Press, 1979.[15]

Boullion, T., and Odell, P. Generalized Inverse Matrices. New York: Wiley (Interscience), 1971. [12]

Campbell, S. L., and Meyer, C. D. Jr., Generalized Inverses of Linear Transformations. London : Pitman, 1979. [12]

Daleckii, J. L., and Krein, M. G. Stability of Solutions of Differential Equations in Banach Space. Providence, R. Is.: Trans. Amer. Math. Soc. Monographs, vol. 43, 1974. [12, 14]

Dunford, N., and Schwartz, J. T. Linear Operators, Part I: General Theory. New York: Wiley (Interscience), 5, 9, 10]

Gantmacher, F. R. The Theory of Matrices, vols. 1 and 2. New York: Chelsea, 1959. [1–15]

Glazman, I. M., and Liubich, J. I. Finite-Dimensional Linear Analysis. Cambridge, Mass.: M.I.T. Press, 1974. [3–10]

Gohberg, I., Lancaster, P., and Rodman, L. Matrix Polynomials. New York: Academic Press, 1982. [14]

Golub, G. H., and Van Loan, C. F. Matrix Computations. Baltimore, Md.: Johns Hopkins Univ. Press, 1983. [3, 4, 10].

Halmos, P. R. Finite-Dimensional Vector Spaces. New York: Van Nostrand, 1958. [3–6]

Hamburger, M. L., and Grimshaw, M. E. Linear Transformations in n-Dimensional Vector Spaces. London: Cambridge Univ., 1956. [3–6]

Heinig, G., and Rost, K. Algebraic Methods for Toeplitz-like Matrices and Operators. Berlin: Akademie Verlag, 1984. [13].

Householder, A. S. The Theory of Matrices in Numerical Analysis. Boston: Ginn (Blaisdell), 1964. [10, 15]

Kato, T. Perturbation Theory for Linear Operators. Berlin: Springer-Verlag, 1966 (2nd ed., 1976). [11]

Krein, M. G., and Naimark, M. A.The Method of Symmetric and Hermitian Forms in the Theory of the Separation of the Roots of Algebraic Equations." Lin. and Multilin. Alg. 10 (1981): 265–308. [13]

Lancaster, P. Lambda Matrices and Vibrating Systems. Oxford: Pergamon Press, 1966. [14]

Lerer, L., and Tismenetsky, M. “The Bezoutian and the Eigenvalue-Separation Problem for Matrix Polynomials."Integral Eq. and Operator Theory 5 (1982): 386–445. [13]

MacDuffee, C. C. The Theory of Matrices. New York: Chelsea, 1946. [12]

Marcus, M., and Minc, H. A Survey of Matrix Theory and Matrix Inequalities. Boston: Allyn and Bacon, 1964. [1–10, 12, 15]

Mirsky, L. An Introduction to Linear Algebra. Oxford: Oxford Univ. (Clarendon), 1955. [1–7]

Ortega, J. M., and Rheinboldt, W. C. Iterative Solution of Nonlinear Equations in Several Variables. New York: Academic Press, 1970. [15]

Rellich, F. Perturbation Theory of Eigenvalue Problems. New York: Gordon and Breach, 1969.[11]

Russell, D. L. Mathematics of Finite-Dimensional Control Systems. New York: Marcel Dekker, 1979.[9]

Varga, R. S. Matrix Iterative Analysis. Englewood Cliffs, N.J.: Prentice-Hall, 1962. [15]

Wilkinson, J. H. The Algebraic Eigenvalue Problem. Oxford: Oxford Univ. (Clarendon), 1965. [10]

Wonham, W. M. Linear Multivariable Control: A Geometric Approach. Berlin: Springer-Verlag, 1979. [9]

## Index

## A

Abel's formula, 346   
Absolute norm, 367–370, 387   
Adjoint matrix, 42, 274   
reduced, 272   
Adjoint transformation, 169–174   
Admissible pairs, 212-217   
Admissible triple, for a matrix polynomial,   
494,519   
Algebra, of linear transformations, 121   
Algebraic multiplicity, 159, 239, 279, 349   
Algebraically closed field, 556   
Analytic perturbations, 391–405   
Analytic function, 331   
Angle, 106   
Annihilating polynomial, 223–229   
Appollonius's Theorem, 107   
Approximate solutions of Ax = b, 436–438   
Augmented matrix, 57

## B

Ball, 355, 356, 557   
Barnett factorization, 458   
Barnett, S., 560   
Basis, 83   
standard, 84   
elements, 84   
Bauer, F. L., 368, 387   
Baumgärtel, H., 560   
Bellman, R., 560   
Bendixson, I., 379   
Ben-Israel, A., 560   
Berman, A., 560   
Bessel's inequality, 109   
Bezout matrix, 454–466   
Bezoutian, 454–466   
Bilinear, 104   
Bilinear forms, 202   
Binary operation, 72   
closed, 72   
Binet-Cauchy formula, 39, 97   
Biorthogonal systems, 113, 154, 195   
Block matrix, 17, 55   
Boolean sum of projectors, 199   
Borhardt, C., 487   
Bouillon, T., 560   
Bounded set, 557

## C

Campbell, S. L., 560   
Canonical set of Jordan chains, 502   
Cardinal polynomials, 308   
Carlson, D., 448   
Cartesian decomposition, 179, 219   
Cauchy index, 482   
theorem, 332   
Cauchy-Schwarz inequality, 42, 106, 114,   
381   
Cayley transform, 219   
Cayley-Hamilton theorem, 165, 228, 252   
Characteristic polynomial, 155–159, 228, 240,   
271, 490   
Chebyshev polynomial, 166   
Chen, C. T., 449

Cholesky factorization, 63, 180   
Chrystal's theorem, 276   
Circulant matrix, 66, 146, 166 generalized, 66   
Closed set, 557   
Cofactor, 33, 42   
Col, 457   
Column space, 80, 93   
Common divisor, 554 multiple, 555   
Commuting linear transformations, 143   
Commuting matrices, 166, 416–420 normal, 420 simple, 420   
Companion matrix, 32, 36, 68, 69, 157, 262, 455 of a matrix polynomial, 280, 490, 493 second, 461, 490, 493, 497   
Compatible norms, 360, 363, 367   
Complementary subspace, 91 orthogonal, 111   
Complexification, 200   
Component matrices, 314-322, 332–334, 347 analyticity of, 393–395   
Composition of transformations, 121   
Condition number, 385–387 spectral, 386   
Conformable matrices, 9   
Congruent matrices, 184–188, 203   
Conjugate bilinear forms, 202   
Consistent equations, 100   
Constituent matrix, 164   
Constrained eigenvalues, 291–294   
Constrained eigenvectors, 291–294   
Continuous function, 558   
Control function, 342   
Controllable pair, 216, 448–450, 470   
Controllable subspace, 216, 342   
Controllable system, 342–345   
Convergence in a normed linear space, 356, 357 in Cm×n, 325, 361   
Convex hull, 559   
Convex linear combination, 559   
Convex set, 356   
Courant-Fischer theorem, 289, 300   
Courant, R., 288   
Cramer's rule, 24, 60   
Cyclic subspace, 231

## D

Daleckii, J. L., 445, 560   
Decomposable matrix, 273   
Defect, of a linear transformation, 135–138, 172   
Definite matrix, 179   
Degree of a λ-matrix, 247 of nilpotency, 12   
Derivative of a matrix, 330   
Derogatory matrix, 240   
Determinant, 23 et seq., 157, 184, 373, 379 bordered, 65 derivative of, 65 of a linear transformation, 141   
Diagonal, of a matrix, 25 main, 2 secondary, 2   
Diagonal matrix, 2   
Diagonally dominant matrix, 373, 531   
Difference equations, 277–278, 340, 512–516   
Differential equations, 161–163, 274–277, 334–340, 348, 506–612, 525 inhomogeneous, 162, 338–340, 348, 509-512 initial-value problem, 336–340, 510–512 matrix, 346, 348 steady-state solution, 340   
Dimension, 86   
Direct sum of linear transformations, 144 of matrices, 146   
Directed graph of a matrix, 528   
Distance, 354   
Divisor (right and left), of a matrix polynomial, 249–253, 518   
Doubly stochastic matrix, 21   
Dual norm, 381   
Dual system, 345   
Dunford, N., 560

## E

Eigenbasis, 151, 173 orthonormal, 174, 190, 193   
Eigenspace, 149, 159, 175   
Eigenvalue dominant, 361 of a linear transformation, 148 of a matrix, 152   
Eigenvectors left, 154 linear independence of, 150, 153 of a linear transformation, 148 of a matrix, 152   
Elementary divisors, 266–271 of a function of a matrix, 313 linear and nonlinear, 266   
Elementary matrices, 48, 255   
Elementary operations, 47, 253   
Equivalence relation, 52, 130, 184, 220, 255, 354,494   
Equivalence transformation on matrix polynomials, 255, 491   
Equivalent matrices, 52   
Equivalent matrix polynomials, 255, 261, 279   
Equivalent norms, 353   
Euclidean norm, 351, 352, 358, 378   
Euclidean space, 105   
Exponential function, 308, 313, 323, 329, 382   
Extension of a linear transformation, 142 of a nonnegative irreducible matrix, 535

## F

Fibonacci matrix, 35   
Field of values, 283–286   
Fischer, E., 288   
Flanders, H., 422   
Flockerzi, D., 537   
Fractional powers of a matrix, 323   
Fredholm alternative, 174, 219   
Fredholm theorem, 115   
Frobenius, G., 295, 299, 415, 481, 482, 538   
Fujiwara, M., 462   
Full rank, 96, 111, 139, 140, 180   
Function defined on the spectrum, 305   
Function of a matrix, 308   
composite, 324   
Fundamental polynomials, 308

## G

Gantmacher, F. R., 561   
Gauss reduction, 49, 56   
Generalized eigenspace, 229, 232–236, 239 order of, 229

Generalized eigenvector, 229   
order of, 229–231   
Generalized inverse, 428–438   
Geometric multiplicity, 159, 239, 279   
Geršgorin disks, 372   
Geršgorin theorem, 371–377   
Glazman, I. M., 561   
Gohberg, I., 489, 561   
Golub, G. H., 561   
Gram matrix, 110, 218   
Gramian, 110   
Gram-Schmidt process, 108   
Greatest common divisor, 460, 554   
Greville, T. N. E., 560   
Grimshaw, M. E., 561   
Gundelfinger's criterion, for inertia of a   
Hermitian matrix, 298, 481, 482

## H

Hadamard's inequality, 65   
Hahn, W., 450   
Halmos, P. R., 561   
Hamburger, M. L., 561   
Hankel matrix, 66   
Heinig, G., 561   
Hermite, C., 462   
Hermite interpolation, 306   
Hermitian forms, 203   
Hermitian matrix, 3, 15, 63, 178–180,   
184-188, 284-302   
Hill, D. R., 452   
Hirsch, A., 378   
Hölder inequality, 359, 381   
Hölder norms, 351, 358, 381   
Homogeneous equations, 61   
Householder, A. S., 387, 561   
Householder transformation, 190   
Hurwitz, A., 478   
Hurwitz matrix, 478

## I

Idempotent matrix, 11, 13, 133, 158, 164, 166, 194–199, 244, 279, 426   
Image of a linear transformation, 133 of a matrix, 77, 80 of a subspace, 86, 133 of a transformation, 116   
Imaginary part of a matrix, 179   
Imprimitive matrices, 544–547   
Inconsistent equations, 56   
Indecomposable matrix, 273   
Index of an eigenvalue, 226, 228, 240, 269 of imprimitivity, 544 of stabilization, 214   
Induced matrix norms, 363–367   
Inertia of a matrix, 186–188, 296–300 with respect to the real axis, 450   
Inertia of a polynomial, 462–466 with respect to the real axis, 462 with respect to the unit circle, 466   
Inf, 558   
Inner product, 7, 104, 180, 186 standard, 104   
Integral of a matrix, 330   
Interpolatory polynomials, 306-308   
Invariant polynomials, of a matrix polynomial, 261   
Invariant subspace, 143, 155, 172, 197, 201, 374 trivial, 143   
Inverse left, 45, 138 of a linear transformation, 141 of a matrix, 44, 53 right, 45, 139   
lnvertible λ-matrix, 247   
Invertible linear transformation, 140, 151   
Invertible matrix, 44, 53, 425   
Involutory matrix, 12, 44   
lrreducible matrix, 374–377, 528–542   
Isomorphic spaces, 113, 124, 126   
Isomorphism of algebras, 126

## J

Jacobi criteron, for inertia of a Hermitian matrix, 296   
Jacobi, G., 487   
Jacobi identity, 346   
Jacobi matrix, 35   
Jordan basis, 232, 234   
Jordan block, 237, 244, 268, 274, 311   
Jordan canonical form, 237, 239, 270, 311 for real matrices, 242–243   
Jordan chain, 230, 235 for a matrix polynomial, 501–505, 519 length of, 230

Jordan decomposition, 236   
Jordan pair, 500–505   
Jordan subspace, 230, 231   
Jordan triple, 500–505

## K

Kato, T., 400, 561   
Kernel of a linear transformation, 135 of a matrix, 77   
Krein, M. G., 445, 560, 561   
Kronecker delta, 79   
Kronecker product, 407–413, 438, 439 eigenvalues of, 412 for rectangular matrices, 413, 438, 440   
Kronecker sum, 412

## L

λ-matrix, 246 et seq. See also Matrix   
polynomial   
L-C splitting of a polynomial, 470, 485   
LU decomposition, 61   
Lagrange interpolating polynomial, 307   
Lancaster, P., 468, 489, 561   
Langer, H., 521   
Laplace's theorem, 37   
Latent roots, 265, 280, 281, 491   
Latent vectors, 280, 501   
Laurent expansion, 333   
Leading principal minors, 36   
Leading vector of a Jordan chain, 501   
Least squares solution, 436   
Left invertible linear transformation, 138   
Left invertible matrices, 140, 425–427, 439   
Legendre polynomials, 114   
Length of a vector, 4, 105, 106   
Lerer, L., 561   
Lévy-Desplanques-Hadamard theorem, 373   
Liénard–Chipart criterion, 470–474, 455, 486   
Limit point, 557   
Line segment, 559   
Linear combination, 78   
Linear dependence, 81   
Linear hull, 79   
Linear independence, 82   
Linear spáce, 73   
finite dimensional, 84, 86   
infinite dimensional, 84, 86

## INDEX

Linear transformation, 117   
invertible, 140   
Linearization, 492 et seq., 520, 524   
Liouville's formula, 346   
Liubich, J. I., 561   
Logarithmic function, 312, 313, 317   
Lower bound, 369, 370, 387   
Lyapunov equation, 416, 443–450   
Lyapunov stability criterion, 443

## M

M-matrices, 531, 532   
MacDuffee, C. C., 415, 561   
Marcus, M., 561   
Markov, A. A., 476   
Markov chains, 550–552   
Markov criterion, 475–477, 486   
Markov parameters, 474, 477, 478, 483   
Matrix, 1   
Matrix equations, 413–424   
Matrix norm, 358, 381, 382   
induced, 363–367   
Matrix polynomial, 246 et seq., 489 et seq.   
monic, 248   
Metric, 355   
Meyer, C. D., 560   
Minc, H., 561   
Minimal polynomial, 224, 240, 245, 271–273   
Minkowski inequality, 351   
Minor of a matrix, 32, 36   
Mirsky, L., 561   
Monotone matrices, 531   
Monotonic norm, 367   
Moore, E. H., 432   
Moore-Penrose inverse, 432-440   
Multiples of matrix polynomials, 518–520   
Multiplicity   
of a latent root, 279. See also Algebraic   
multiplicity, Geometric multiplicity   
of a zero of a polynomial, 555

## N

Naimark, M. A., 561   
Natural frequencies, 210   
Natural normal form (first and second), 264,   
269   
Negative definite matrix, 179   
Negative semidefinite matrix, 179

Neighborhood, 356, 557   
Newton sums, 487   
Nilpotent matrix, 11, 133, 158, 244   
Nonderogatory matrix, 240, 273   
Nonnegative matrix, 527   
Nonsingular matrix, 43, 375   
Norm euclidean, 351, 352, 358, 378 Frobenius, 358 Hölder, 351, 358, 381 infinity, 351, 352 of a linear transformation, 363 of a matrix, 358 of a vector, 105, 106, 350 et seq. submultiplicative, 358   
Normal coordinates, 210   
Normal linear transformation, 174–177   
Normal matrices, 174–177, 183, 284, 365, 390 analytic perturbation of, 404 commuting, 420   
Normal modes, 210   
Normalized vector, 106   
Normed linear space, 351   
Nullspace of a matrix, 77

## 0

Observable pair, 214-217, 341, 497   
Observable system, 340   
Odell, P., 560   
Open set, 557   
Ortega, J. M., 530, 561   
Orthogonal complement, 111, 195   
Orthogonal matrix, 46, 175, 201, 219, 346   
Orthogonal projection of a vector, 112   
Orthogonal projector, 195, 380, 431   
Orthogonal similarity, 175   
Orthogonal subspaces, 111   
complementary, 111   
Orthogonal system, 107   
Orthogonal vectors, 107   
Orthonormal basis, 108   
Orthonormal system, 108   
Ostrowski, A., 445   
Outer product, 9

## P

Parallelogram theorem, 107   
Parseval's relation, 109, 112, 113   
Partition of a matrix, 16   
Penrose, R., 432   
Perlis, S., 553   
Permutation matrix, 64   
Perron, O., 538, 542   
Perron–Frobenius theorem, 536   
Perturbation coefficients, 397-399   
Perturbation of eigenvalues, 387-405   
Plemmons, R. J., 560   
Polar decomposition, 190, 380, 439   
Polynomial in a matrix, 19   
Polynomials, 553–556   
Position vector, 4, 72   
Positive definite matrices, 179–182, 185, 218,   
219, 309, 373, 382   
Kronecker product of, 413   
Positive matrix, 527   
Positive semidefinite matrices, 179–182, 185,   
218   
Power method, 361   
Preimage of a vector, 137   
Primitive matrices, 544–548   
Principal minors, 36   
Projectors, 164, 194–199, 315, 321, 333,   
426, 430   
commuting, 199   
Puiseux series, 392, 401   
Pythagoras's theorem, 107

## Q

QR decomposition, 111, 184   
Quadratic forms, 203   
Quotient (right and left), 249–253

## R

Range of a function, 558   
Range of a matrix, 77   
Rank decomposition, 97, 433   
Rank of a linear transformation, 133–136, 172 of a matrix, 53 et seq., 93, 114, 115, 129 of a matrix polynomial, 259–262   
Rayleigh quotient, 282, 286–294, 363   
Rayleigh theorem, 294   
Reachable vector, 342, 345   
Real part of a matrix, 179   
Reduced adjoint, 272, 274, 334   
Reducible matrices, 374–377, 543, 544 normal form for, 544   
Reducing subspaces, 197–198   
Regular λ-matrix, 247, 259, 489   
Relative perturbation, 383   
Relatively prime polynomials, 554   
Rellich, F., 400, 405, 561   
Remainder (right and left), 249–253   
Remainder theorem, 251-253   
Representation of a linear transformation, 122, 140, 145 of a set of vectors, 92, 95 of a vector, 85 standard, 123 theorem for matrix polynomials, 516   
Resolution of the identity, 315   
Resolvent, 164, 315, 321, 322, 330–333, 505 of a matrix polynomial, 493, 505   
Resolvent condition, 386   
Resonance, 212   
Restriction of a linear transformation, 142   
Resultant matrix, 460, 461   
Rheinboldt, W. C., 530, 561   
Right-invertible linear transformation, 139   
Right-invertible matrices, 140, 425–427, 439   
Rodman, L., 489, 561   
Rost, K., 561   
Rotation matrix, 455   
Roth, W. E., 422   
Routh-Hurwitz problem, 464–466   
Routh-Hurwitz stability test, 480–482   
Row echelon form, 50, 57   
Row space, 80, 94   
Russell, D. L., 561

## S

Scalar matrix, 2, 133   
Scalar multiplication, 6, 72   
Scalar product, 7   
Schneider, H., 445, 448   
Schur-Cohn problem, 466–468   
Schur complement, 46, 56   
Schur, I., 165, 176, 377   
Schwartz, J. T., 560   
Schwarz matrix, 450   
Segre characteristic, 241, 492   
Semi-definite matrix, 179   
Sequences of matrices, 325–327   
Series of matrices, 327–329   
Sherman-Morison formula, 64

Shift operator, 277   
Signature, 187 Similar admissible triples, 494 Similar matrices, 130–133, 175, 262-271 Simple linear transformation, 146, 151, 164, 173,177   
Simple matrices, 143, 146, 147, 153, 154, 160, 239, 271, 273, 419- eigenvalues of, 387–390 Kronecker product of, 413   
Singular bases, 435, 437   
Singular matrix, 43, 94, 155   
Singular-value decomposition, 192   
Singular values, of a matrix, 182–184. 192–193, 380, 386, 435   
Size of a matrix, 1   
Skew-Hermitian matrix, 16, 180   
Skew-symmetric matrix, 14, 219, 346   
Small oscillations, 208–212, 302, 303   
Smith canonical form, 261, 262   
Solvents of matrix polynomials, 252, 280, 520-526 complete set of, 524   
Span, 79   
Spectral norm, 365, 366, 367, 381   
Spectral radius, 359, 365, 377, 530–532, 539 540   
Spectral resolution, 314-320   
Spectral theorem, 154, 164, 175   
Spectrum, 150, 152, 178, 188, 331 of a matrix polynomial, 281, 491   
Sphere, 355   
Square root of a positive (semi-) definite matrix, 180, 309, 324   
Stable matrix, 414, 416, 441 with respect to the unit circle, 451–453   
Stable polynomial, 462, 465   
Standard pair, 497   
Standard triple, 494, 519, 520   
State vector, 340   
Stein equation, 451–453   
Stephanos, C., 411   
Stieltjes matrices, 532   
Stochastic matrices, 21, 547–552 doubly, 550   
Stoer, J., 368   
Storey, C., 560   
Strongly connected directed graph, 528   
Submatrix, 16   
Subspace, 75, 105 complementary, 91 trivial, 76   
Sum of subspaces, 87 direct, 89, 112 orthogonal, 112   
Sup, 558   
Sylvester, J. J., 450, 460   
Sylvester's law of inertia, 188, 204   
Symmetric matrix, 3, 14   
Symmetric partition, 17   
Symmetrizer of a matrix polynomial, 493 of a polynomial, 455   
Systems of algebraic equations, 56

## T

Taussky, O., 375, 376, 445, 452   
Tensor product, 407   
Tismenetsky, M., 468, 561   
Toeplitz matrix, 68, 69, 79   
Toeplitz, O., 176   
Trace of a matrix, 22, 107, 132, 157, 166   
Transfer function, 70   
Transformation, 116   
addition and scalar multiplication, 120   
zero, 120   
Transition matrix, 98   
Transposed matrix, 13   
Triangle inequality, 351   
Triangular matrix, 2, 44, 176   
Tridiagonal matrix, 35

## U

Unimodular λ-matrix, 247, 255, 268   
Union of bases, 89   
Unit sphere, 283   
Unit vectors, 79   
Unitarily similar matrices, 175   
Unitary equivalence, 193   
Unitary matrix, 47, 115, 174, 184, 188–190,   
219, 346, 348   
Unitary similarity, 175, 176, 365   
Unitary space, 105, 351   
Unobservable subspace, 214

## V

Van Loan, C. F., 561

Vandermonde matrix, 35, 66, 69, 307, 524 generalized, 70, 281, 307

Varga, R. S., 530, 561

Vec-function, 409, 410

Vector, 3 position, 4

Vibrating systems, 208, 302

W

Well-conditioned equations, 383

Wielandt, H., 450, 539

Wilkinson, J. H., 561

Wimmer, H. K., 422, 452

Witzgall, C., 368

Wonham, M., 561

![](images/d371ee32735056a28486ed2ea90decab5b3d2efe873059dd53282b43da5b8374.jpg)