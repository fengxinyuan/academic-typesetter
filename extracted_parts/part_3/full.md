## 8.1 Field of Values. Extremal Eigenvalues of a Hermitian Matrix

The eigenvalues of a matrix $A \in \mathbb { C } ^ { n \times n }$ form a set of n (not necessarily distinct) points in the complex plane. Some useful ideas concerning the distribution of these points can be developed from the concept of the field of values of $A ,$ defined as the set $F ( A )$ of complex numbers $( A { \bf { x } } , { \bf { x } } )$ , where x ranges over all vectors in $\mathbb { C } ^ { n }$ that are normalized so that $( x , x ) = x ^ { * } x = 1 . ^ { \dagger }$

Observe that the quadratic form

$$
f ( { \pmb x } ) = ( { \pmb A } { \pmb x } , { \pmb x } ) = \sum _ { i , j = 1 } ^ { n } a _ { i j } x _ { i } \bar { x } _ { j } , \qquad { \pmb x } = [ { \pmb x } _ { 1 } \quad x _ { 2 } \quad \cdots \quad x _ { n } ] ^ { \mathrm { T } } ,
$$

is a continuous function in n variables on the unit sphere in $\mathbb { C } ^ { n } ,$ ,that is, the set of vectors for which

$$
( \mathbf { x } , \mathbf { x } ) = \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { 2 } = 1 .
$$

Hence it follows (see Theorem 2 in Appendix 2) that $F ( A )$ is a closed and bounded set in the complex plane. It can also be proved that $F ( A )$ is a convex set (see Appendix 2 for the definition), but we omit this proof.

Theorem 1. The field of values of a matrix $A \in \mathbb { C } ^ { n \times n }$ is invariant under unitary similarity transformations. Thus, if $U \in \mathbb { C } ^ { n \times n }$ is unitary, then

$$
F ( A ) = F ( U A U ^ { * } ) .
$$

PROOF. We have

$$
( U A U ^ { * } x , \pmb { x } ) = ( A U ^ { * } x , U ^ { * } \pmb { x } ) = ( A y , \pmb { y } ) ,
$$

where $y = U ^ { * } x$ If $( { \pmb x } , { \pmb x } ) = 1$ , then $( y , y ) = ( U U ^ { * } x , \pmb { x } ) = ( \pmb { x } , \pmb { x } ) = 1$ . Hence a number α is equal to $( U A U ^ { * } { \pmb x } , { \pmb x } )$ for some $\mathbf { x } \in \mathbb { C } ^ { n }$ with $( { \pmb x } , { \pmb x } ) = 1$ if and only if $\alpha = ( A \mathbf { y } , \mathbf { y } )$ for some normalized $\ b { y } \in \mathbb { C } ^ { n }$ ; that is, α belongs to $F ( U A U ^ { * } )$ if and only if $\alpha \in F ( A )$

This result admits an elegant geometrical description of the field of values of a normal matrix in terms of its eigenvalues. First note that all eigenvalues of an arbitrary matrix $A \in \mathbb { C } ^ { n \times n }$ are in $F ( A )$ . For, if $\lambda \in \sigma ( A )$ , then there is an eigenvector x of A corresponding to this eigenvalue for which $A { \boldsymbol { x } } = \lambda { \boldsymbol { x } }$ and $( { \pmb x } , { \pmb x } ) = 1$ . Hence

$$
( A x , x ) = ( \lambda \mathbf { x } , \mathbf { x } ) = \lambda ( x , x ) = \lambda ,
$$

and so $\lambda \in F ( A )$ . Thus, $\sigma ( A ) \subset F ( A )$

For normal matrices, the geometry of the field of values is now easily characterized. The notion of the convex hull appearing in the next theorem is defined and discussed in Appendix 2.

Theorem 2. The field of values of a normal matrix $\ b { A } \in \mathbb { C } ^ { n \times n }$ coincides with the convex hull of its eigenvalues.

ProOF. If A is normal and its eigenvalues are $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n } ,$ then by Theorem 5.2.1 there is a unitary $n \times n$ matrix U such that $A = U D U ^ { * }$ , where $D = \mathrm { d i a g } [ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { n } ]$ . Theorem 1 now asserts that $F ( A ) = F ( D )$ and so it suffices to show that the field of values of the diagonal matrix D coincides with the convex hull of the entries on its main diagonal.

Indeed, $F ( D )$ is the set of numbers

$$
\alpha = ( D \mathbf { x } , \mathbf { x } ) = \sum _ { i = 1 } ^ { n } \lambda _ { i } | x _ { i } | ^ { 2 } ,
$$

where $\begin{array} { r } { ( { \bf x } , { \bf x } ) = \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { 2 } = 1 . } \end{array}$

On the other hand, the convex hull of the points $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ is, according to Exercise 2 in Appendix 2 the set

$$
\left\{ \sum _ { i = 1 } ^ { n } \theta _ { i } \lambda _ { i } \colon \theta _ { i } \geq 0 , \quad \sum _ { i = 1 } ^ { n } \theta _ { i } = 1 \right\} .
$$

Putting $\theta _ { i } = | x _ { i } | ^ { 2 } ( i = 1 , 2 , \dots , n )$ and noting that, as x runs over all vectors satisfying $( { \pmb x } , { \pmb x } ) = { \ o 1 } ,$ , the $\theta _ { i }$ run over all possible choices such that $\theta _ { i } \geq 0 ,$ $\sum _ { i } ^ { n } { \theta _ { i } } = 1$ , we obtain the desired result.

For a general n × n matrix A, the convex hull of the points of the spectrum of a matrix A is a subset of $F ( A )$ (see Appendix 2). But for the special case of Hermitian matrices, the geometry simplifies beautifully.

Theorem 3. The field of values of the matrix $\ b { A } \in \mathbb { C } ^ { n \times n }$ is an interval of the real line if and only if A is Hermitian.

ProoF. First, if A is Hermitian then A is normal and, by Theorem 2, F(A) is the convex hull of the eigenvalues of A, which are all real (Theorem 5.3.1). Since the only convex sets on the real line are intervals, the required result follows.

Conversely, if $\ b { A } \in \mathbb { C } ^ { n \times n }$ and $F ( A )$ is an interval of the real line, then, writing

$$
B = \mathcal { H }  A = \frac 1 2 ( A + A ^ { * } ) , \ ~ C = \mathcal { I } _ { m } \ A = \frac 1 { 2 i } ( A - A ^ { * } ) ,
$$

we obtain

$$
( A { \pmb x } , { \pmb x } ) = ( ( B + i C ) { \pmb x } , { \pmb x } ) = ( B { \pmb x } , { \pmb x } ) + i ( C { \pmb x } , { \pmb x } ) ,
$$

where $( B { \pmb x } , { \pmb x } )$ and $( C { \pmb x } , { \pmb x } )$ are real since B and C are Hermitian (see Section 5.10). But $F ( A )$ consists only of real numbers, therefore $( C \pmb { x } , \pmb { x } ) = 0$ for all

x such that $( { \pmb x } , { \pmb x } ) = 1$ . Hence, $C = O$ (see Exercise 3.13.2) and $A = A ^ { * }$ , that $\mathbf { i s } , A$ is Hermitian.■

Corollary 1. If H is Hermitian with the eigenvalues $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n }$ , then

$$
F ( H ) = [ \lambda _ { 1 } , \lambda _ { n } ] .\tag{1}
$$

Conversely, if $F ( A ) = \left[ \lambda _ { 1 } , \lambda _ { n } \right]$ , then A is Hermitian and $\lambda _ { 1 } , \lambda _ { n }$ are the minimal and maximal eigenvalues of A, respectively.

This result is an immediate consequence of Theorems 2 and 3.

Recalling the definition of $F ( H )$ , we deduce from Eq. (1) the existence of vectors $\mathbf { x } _ { 1 }$ and ${ \pmb x } _ { n }$ on the unit sphere such that $( H \pmb { x } _ { 1 } , \pmb { x } _ { 1 } ) = \lambda _ { 1 }$ and $( H \pmb { x } _ { n } , \pmb { x } _ { n } ) =$ $\lambda _ { n }$ . Obviously,

$$
\lambda _ { 1 } = ( H x _ { 1 } , x _ { 1 } ) = \operatorname* { m i n } _ { ( \pmb { x } , \pmb { x } ) = 1 } ( H \pmb { x } , \pmb { x } ) ,\tag{2}
$$

and

$$
\lambda _ { n } = ( H \mathbf { x } _ { n } , \mathbf { x } _ { n } ) = \operatorname* { m a x } _ { ( \pmb { x } , \pmb { x } ) = 1 } ( H \pmb { x } , \pmb { x } ) .\tag{3}
$$

Moreover, the vectors $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { n }$ are eigenvectors of H corresponding to $\lambda _ { 1 }$ and $\lambda _ { n }$ , respectively. In fact, it follows from Eq. (2) that if x is any vector with $( { \pmb x } , { \pmb x } ) = 1$ , then

$$
( H \mathbf { x } , \mathbf { x } ) \geq \lambda _ { 1 } = \lambda _ { 1 } ( \mathbf { x } , \mathbf { x } ) .
$$

Hence

$$
( ( H - \lambda _ { 1 } I ) \mathbf { x } , \mathbf { x } ) \geq 0 ,
$$

and this implies that $H - \lambda _ { 1 } I$ is positive semidefinite. But Eq. (2) also implies that

$$
( ( H - \lambda _ { 1 } I ) x _ { 1 } , x _ { 1 } ) = 0 ,
$$

and it follows (as in Exercise 5.4.1) that $( H - \lambda _ { 1 } I ) \pmb { x } _ { 1 } = \pmb { \mathscr { 0 } } .$ Since $( { \pmb x } _ { 1 } , { \pmb x } _ { 1 } ) = 1$ it follows that $\ b x _ { 1 } \neq \ b \theta$ and $\mathbf { x } _ { 1 }$ is therefore an eigenvector of H corresponding to $\lambda _ { 1 }$

Similarly, $x _ { n }$ is an eigenvector of H corresponding to the maximal eigenvalue $\lambda _ { n }$ . Thus, we have proved the following:

Theorem 4. If $\lambda _ { 1 }$ and $\lambda _ { n }$ denote the minimal and maximal eigenvalues of a Hermitian matrix $H \in \mathbb { C } ^ { n \times n }$ , respectively, then

$$
\lambda _ { 1 } = \operatorname* { m i n } _ { ( \mathbf { x } , \mathbf { x } ) = 1 } ( H \mathbf { x } , \mathbf { x } ) , \qquad \lambda _ { n } = \operatorname* { m a x } _ { ( \mathbf { x } , \mathbf { x } ) = 1 } ( H \pmb { x } , \pmb { x } ) .
$$

Moreover, the extremal values of (Hx, x) are attained at corresponding eigenvectors of H.

This result is the first step in the development of a min-max theory of eigenvalues of Hermitian matrices, one of the main topics in this chapter.

Exercise 1. Let $H = [ h _ { i j } ] _ { i , j = 1 } ^ { n }$ denote a Hermitian matrix. Prove that, preserving the notation of this section,

(a) $\lambda _ { 1 } \leq h _ { j j } \leq \lambda _ { n } { \mathrm { f o r } } j = 1 , 2 , \ldots , n ;$

(b) $\begin{array} { r } { \mathrm { { I f } } \propto = n ^ { - 1 } \sum _ { i , j = 1 } ^ { n } h _ { i j } , \mathrm { { t h e n } } \lambda _ { 1 } \le \alpha \le \lambda _ { n } . } \end{array}$

Hint. For part (a) put $\mathbf { \boldsymbol { x } } _ { j } = \mathbf { \boldsymbol { e } } _ { j }$ , (a unit vector in C") in $( H \pmb { x } , \pmb { x } )$ and use Theorem 4. For part (b) use the vector $n ^ { - 1 / 2 } [ 1 \quad 1 \quad \cdots \quad 1 ] ^ { \mathbf { \dot { T } } } . \quad \square$

## 8.2 Courant-Fischer Theory and the Rayleigh Quotient

In this section, the variational description of extremal eigenvalues of a Hermitian matrix achieved in the preceding section will be extended to all of the eigenvalues. For this and other purposes the notion of the Rayleigh quotient for an $n \times n$ Hermitian matrix H is useful. We define it to bel

$$
R _ { H } ( { \pmb x } ) \equiv R ( { \pmb x } ) \triangleq \frac { ( H { \pmb x } , { \pmb x } ) } { ( { \pmb x } , { \pmb x } ) } , ~ { \pmb x } \neq \pmb \theta .
$$

Thus, R is a real-valued function defined by H, whose domain is the nonzero vectors of $\mathbb { C } ^ { n } .$

It is clear that, replacing x by αx, the Rayleigh quotient remains invariant. Hence, in particular,

$$
\begin{array} { c } { \operatorname* { m i n } _ { \mathbf { \eta } ( { \pmb { k } } , { \pmb { x } } ) } \left( H { \pmb { x } } , { \pmb { x } } \right) = \displaystyle \operatorname* { m i n } _ { { \pmb { x } } \neq { \pmb { \theta } } } R ( { \pmb { x } } ) } \\ { \displaystyle \operatorname* { m a x } _ { { \pmb { x } } \neq { \pmb { \theta } } } \left( H { \pmb { x } } , { \pmb { x } } \right) = \displaystyle \operatorname* { m a x } _ { { \pmb { x } } \neq { \pmb { \theta } } } R ( { \pmb { x } } ) , } \end{array}
$$

and the result of Theorem 8.1.4 can be rewritten in the form

$$
\lambda _ { 1 } = \operatorname* { m i n } _ { \stackrel { x \neq 0 } { x \neq \theta } } R ( \stackrel { x } { x } ) , \qquad \lambda _ { n } = \operatorname* { m a x } _ { \stackrel { x \neq 0 } { x \neq \theta } } R ( \stackrel { x } { x } ) .
$$

and these extrema are attained on eigenvectors of H.

Now let $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n }$ be the eigenvalues of an $n \times n$ Hermitian matrix H and suppose that ${ \mathfrak { x } } _ { 1 } , { \mathfrak { x } } _ { 2 } , \ldots , { \mathfrak { x } } _ { n }$ are associated eigenvectors forming an orthonormal basis. Denote by $\mathscr { C } _ { p }$ the subspace of $\mathbb { C } ^ { n }$ generated by the vectors $\mathbf { x } _ { p } , \mathbf { x } _ { p + 1 } , \dots , \mathbf { x } _ { n } \big ( 1 \leq p \leq n \big )$ . Obviously, $\mathscr { C } _ { p }$ has dimension $n - p + 1$ we have the chain of inclusions

$$
\mathbb { C } ^ { n } = \mathcal { C } _ { 1 } \supset \mathcal { C } _ { 2 } \supset \cdot \cdot \cdot \supset \mathcal { C } _ { n } ,
$$

and the subspace $\mathscr { C } _ { p }$ is orthogonal to the space generated by $\pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \ldots , \pmb { x } _ { p ^ { - 1 } }$ It has already been shown that

$$
\lambda _ { 1 } = \operatorname* { m i n } _ { \pmb { \theta } \neq \pmb { x } \in \mathcal { C } _ { 1 } } R ( \pmb { x } ) ,\tag{1}
$$

and it will now be shown that the other eigenvalues of H can be characterized in a way that generalizes statement (1)

Theorem 1. Let $R ( x )$ be the Rayleigh quotient defined by a Hermitian matrix H, and let the subspaces $\mathcal { C } _ { 1 } , \ldots , \mathcal { C } _ { n }$ (associated with H) be as defined in the previous paragraph. Then, for $i = 1 , 2 , \dots , n .$ the numbers

$$
\lambda _ { i } = \operatorname* { m i n } _ { \pmb { \theta } \neq \pmb { x } \in \mathscr { C } _ { i } } R ( \pmb { x } )\tag{2}
$$

are the eigenvalues of H. Moreover, the minima in Eq. (2) are attained on eigenvectors $x _ { i } o f H$

ProOF. Observe first that the case $i = 1$ is just that of Theorem 8.1.4 written in the form (1). Let $U = [ { \pmb x } _ { 1 } \quad { \pmb x } _ { 2 } \quad \cdots \quad { \pmb x } _ { n } ]$ be the matrix formed by the set of orthonormal eigenvectors of H (as in Theorem 5.2.1), and recall that $\mathscr { C } _ { i }$ is spanned by $\pmb { x } _ { i } , \pmb { x } _ { i + 1 } , \ldots , \pmb { x } _ { n }$ . Then for any $\pmb { x } \in \mathcal { C } _ { i }$ there are numbers $\alpha _ { i } , \alpha _ { i + 1 } , \ldots , \alpha _ { n }$ such that $\begin{array} { r } { \pmb { x } = \sum _ { j = i } ^ { n } \pmb { \alpha } _ { j } \pmb { x } _ { j } } \end{array}$ . Introduce the vector $\pmb { \mathscr { a } } \in \mathbb { C } ^ { n }$ defined by

$$
\pmb { \alpha } = [ 0 \quad \ldots \quad 0 \quad \alpha _ { i } \quad \alpha _ { i + 1 } \quad \cdots \quad \alpha _ { n } ] ^ { \mathrm { T } } ,\tag{3}
$$

so that $\begin{array} { r } { \pmb { x } = U \pmb { \alpha } , } \end{array}$ and observe that, using Theorem 5.2.1,

$$
( H \pmb { x } , \pmb { x } ) = \pmb { x } ^ { * } H \pmb { x } = \pmb { \alpha } ^ { * } U ^ { * } H U \pmb { \alpha } = \pmb { \alpha } ^ { * } D \pmb { \alpha } = \sum _ { j = i } ^ { n } \lambda _ { j } | \alpha _ { j } | ^ { 2 } .\tag{4}
$$

Also we have $\textstyle ( { \pmb x } , { \pmb x } ) = \sum _ { j = 1 } ^ { n } | { \boldsymbol \alpha } _ { j } | ^ { 2 }$ and so

$$
R ( \pmb { x } ) = \bigg ( \sum _ { j = i } ^ { n } \lambda _ { j } | \alpha _ { j } | ^ { 2 } \bigg ) \bigg / \bigg ( \sum _ { j = 1 } ^ { n } | \alpha _ { j } | ^ { 2 } \bigg ) .\tag{5}
$$

Since $\lambda _ { i } \leq \lambda _ { i + 1 } \leq \cdots \leq \lambda _ { n }$ , it is clear that $R ( { \pmb x } ) \geq \lambda _ { i }$ for all $\alpha _ { i } , \alpha _ { i + 1 } , \ldots , \alpha _ { n }$ (not all zero, and hence for all nonzero $\pmb { x } \in \mathcal { C } _ { i } )$ and that $R ( \mathbf { x } ) = \lambda _ { i }$ when $\alpha _ { i } \neq 0$ and $\alpha _ { i + 1 } = \alpha _ { i + 2 } = \cdot \cdot \cdot = \alpha _ { n } = 0$ . Thus relation (2) is established. Note that the minimizing vector of $\mathscr { C } _ { i }$ is just $\alpha _ { i } { \pmb x } _ { i }$ , an eigenvector associated with $\lambda _ { i }$ .

The following dual result is proved similarly.

Exercise 1. In the notation of Theorem 1, prove that

$$
\lambda _ { i } = \operatorname* { m a x } _ { \substack { 0 \neq x \in \mathcal { C } _ { n - i + 1 } } } R ( { \pmb x } ) , \qquad i = 1 , 2 , \ldots , n ,
$$

where the maxima are attained on eigenvectors of H. □

The result of Exercise 1, like that of Theorem 1, suffers from the disadvantage that $\lambda _ { j } \ ( j > 1 )$ is characterized with the aid of the eigenvectors $\pmb { x } _ { n - j + 1 } , \ldots , \pmb { x } _ { n }$ . Thus in employing Theorem 1 we must compute the eigenvalues in nondecreasing order together with orthonormal bases for their eigenspaces. The next theorem is a remarkable result allowing us to characterize each eigenvalue with no reference to other eigenvalues or eigenvectors. This is the famous Courant-Fischer theorem, which originated with E. Fischer† in 1905 but was rediscovered by R. Courant in 1920. It was Courant who saw, and made clear, the great importance of the result for problems in mathematical physics. We start with a preliminary result.

Proposition 1. Let $\mathcal { S } _ { j } \ ( 1 \leq j \leq n )$ denote an arbitrary $( n - j + 1 ) – d i m e n .$ sional subspace of C", and let H be a Hermitian matrix with eigenvalues $\lambda _ { 1 } \leq$ $\lambda _ { 2 } \leq \cdots \leq \lambda _ { n }$ and Rayleigh quotient R(x). Then

$$
\operatorname* { m i n } _ { \pmb { 0 } \neq \pmb { x } \in \mathcal { S } _ { j } } R ( \pmb { x } ) \le \lambda _ { j } , \qquad \operatorname* { m a x } _ { \pmb { 0 } \neq \pmb { x } \in \mathcal { S } _ { j } } R ( \pmb { x } ) \ge \lambda _ { n - j + 1 } .\tag{6}
$$

PROOF. Let ${ \mathfrak { x } } _ { 1 } , { \mathfrak { x } } _ { 2 } , \ldots , { \mathfrak { x } } _ { n }$ be an orthonormal system of eigenvectors for H corresponding to the eigenvalues $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n }$ of H, and let $\hat { \mathcal { S } } _ { j } =$ span $\{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \ldots , \pmb { x } _ { j } \}$ for $j = 1 , 2 , \dots , n .$ Fix j and observe that, since dim $\mathcal { S } _ { j } +$ dim $\begin{array} { r } { \hat { \mathcal { S } } _ { j } = ( n ^ { ' } - j + 1 ) + j > n , } \end{array}$ there exists a nonzero vector $\pmb { x } _ { 0 } \in \mathbb { C } ^ { n }$ belonging to both of these subspaces (see Exercise 3.14.3). In particular since $\pmb { x } _ { 0 } \in \hat { \mathcal { S } } _ { j }$ it follows that $\begin{array} { r } { \pmb { x } _ { 0 } = \sum _ { k = 1 } ^ { j } \pmb { \alpha } _ { k } \pmb { x } _ { k } } \end{array}$ and hence

$$
( H x _ { 0 } , x _ { 0 } ) = \left( \sum _ { k = 1 } ^ { j } \lambda _ { k } \alpha _ { k } x _ { k } , \sum _ { k = 1 } ^ { j } \alpha _ { k } x _ { k } \right) = \sum _ { k = 1 } ^ { j } \lambda _ { k } | \alpha _ { k } | ^ { 2 } .
$$

Thus obviously

$$
\lambda _ { 1 } \sum _ { k = 1 } ^ { j } | \alpha _ { k } | ^ { 2 } \leq ( H \mathbf { x } _ { 0 } , \pmb { x } _ { 0 } ) \leq \lambda _ { j } \sum _ { k = 1 } ^ { j } | \alpha _ { k } | ^ { 2 }
$$

and, dividing by $\sum _ { k = 1 } ^ { j } | { \alpha _ { k } } | ^ { 2 } = ( { \pmb x } _ { 0 } , { \pmb x } _ { 0 } )$ , we obtain

$$
\lambda _ { 1 } \leq R ( \mathbf { x } _ { 0 } ) \leq \lambda _ { j } .\tag{7}
$$

Recall now that xo also belongs to S; and that our immediate purpose $\mathbf { \delta x } _ { 0 }$ $\mathcal { S } _ { j }$ is to establish the first relation in (6). But this follows readily from (7) since

$$
\operatorname* { m i n } _ { \theta \neq \pmb { x } \in \mathcal { S } _ { j } } R ( \pmb { x } ) \leq R ( \pmb { x } _ { 0 } ) \leq \lambda _ { j } .
$$

The second statement of the proposition is proved similarly on replacing $\hat { \mathcal { S } } _ { j }$ by $\mathcal { C } _ { n - j + 1 }$

Theorem 2. (Courant-Fischer). In the previous notation,

$$
\lambda _ { j } = \operatorname* { m a x } _ { \mathcal { S } _ { j } } \operatorname* { m i n } _ { \mathfrak { p } \neq \pmb { x } \in \mathcal { S } _ { j } } R ( \pmb { x } )\tag{8}
$$

for j = 1, 2, . . . , n, or, in dual form,

$$
\lambda _ { n - j + 1 } = \operatorname* { m i n } _ { \mathcal { S } _ { j } } \operatorname* { m a x } _ { \mathfrak { v } \in \mathcal { S } _ { j } } R ( \mathfrak { x } ) .\tag{9}
$$

In other words, Eq. (8) says that by taking the minimum of $R ( x )$ over all nonzero vectors from an $( n - j + 1 )$ -dimensional subspace of $\mathbb { C } ^ { n } ;$ and then the maximum of these minima over all subspaces of this dimension in $\mathbb { C } ^ { n }$ , we obtain the jth eigenvalue of H.

PRooF . To establish Eq. (8) it suffices, in view of the first statement of Eq (6), to show the existence of an $( n - j + 1 )$ -dimensional subspace such that min $R ( x )$ , where x varies over all nonzero vectors of this subspace, is equal to $\lambda _ { j }$ Taking $\mathcal { C } _ { j } = \operatorname { s p a n } \{ \boldsymbol { x } _ { j } , \boldsymbol { x } _ { j + 1 } , \ldots , \boldsymbol { x } _ { n } \}$ , we obtain such a subspace. In fact, by (6),

$$
\operatorname* { m i n } _ { \mathbf { \theta } _ { 0 } \neq x \in \mathcal { C } _ { j } } R ( \pmb { x } ) \leq \lambda _ { j } ,
$$

while by Theorem 1,

$$
\operatorname* { m i n } _ { \mathbf { \theta } _ { 0 } \neq x \in \mathcal { C } _ { j } } R ( \pmb { x } ) = \lambda _ { j } .
$$

This means that the equality (8) holds. Equation (9) is established similarly.

Exercise 2. Check that for $H \in \mathbb { R } ^ { 3 \times 3 } , H > 0 ,$ and $j = 2 ,$ the geometrical interpretation of Eq. (8) (as developed in Exercises 5.10.5 and 5.10.6) is the following: the length of the major axis of any central cross section of an ellipsoid (which is an ellipse) is not less than the length of the second axis of the ellipsoid, and there is a cross section with the major axis equal to the second axis of the ellipsoid.

## 8.3 The Stationary Property of the Rayleigh Quotient

The eigenvalues of a real symmetric matrix can be described in terms of the Rayleigh quotient in another way. Let A denote a real symmetric matrix acting in $\textstyle \mathbb { R } ^ { n }$ We may then view $R ( { \pmb x } )$ associated with A as a real-valued function of the n independent real variables $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ that make up the components of x. We write $R ( \pmb { x } ) = R ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$

Theorem 1. If A is a real symmetric matrix with an eigenvalue $\lambda _ { 0 }$ and associated eigenvector $\scriptstyle { \pmb { x } } _ { 0 }$ , then $R ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ has a stationary value with respect to $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ at $\mathbf { x } _ { 0 } = [ x _ { 1 } ^ { 0 } x _ { 2 } ^ { 0 } \cdots x _ { n } ^ { 0 } ] ^ { \mathbf { T } }$ and $R ( \mathbf { x } _ { 0 } ) = \lambda _ { 0 }$

PRoOF. We have to show that for $k = 1 , 2 , \ldots , n ,$ the derivatives $\partial R / \partial { x _ { k } }$ vanish when evaluated at $\scriptstyle { \pmb { x } } _ { 0 }$ . Indeed, representing $( A \pmb { x } , \pmb { x } )$ as a quadratic form, and writing $\pmb { x } = [ x _ { 1 } \quad x _ { 2 } \quad \cdots \quad x _ { n } ] ^ { \mathbf { T } }$ , we have

$$
( A x , x ) = x ^ { \operatorname { T } } A x = \sum _ { i , j = 1 } ^ { n } a _ { i j } x _ { i } x _ { j } .
$$

Since $a _ { i j } = a _ { j i }$ , it follows that

$$
{ \frac { \hat { \partial } } { \hat { \partial } { x _ { k } } } } \left( A x , x \right) = 2 \sum _ { j = 1 } ^ { n } a _ { k j } x _ { j }
$$

or, equivalently,

$$
\frac { \partial } { \partial x _ { k } } ( A x , x ) = 2 A _ { k * } x ,\tag{1}
$$

where $A _ { k * }$ denotes the kth row of A.

In particular, setting $A = I$ in Eq. (1), we obtain

$$
\frac { \hat { \sigma } } { \hat { \sigma } x _ { k } } ( \pmb { x } , \pmb { x } ) = 2 x _ { k }
$$

and hence

$$
\frac { \partial R } { \partial x _ { k } } = \frac { \partial } { \partial x _ { k } } \frac { ( A x , x ) } { ( x , x ) } = \frac { ( { \bf x } , { \bf x } ) ( 2 A _ { k * } x ) - ( A x , x ) 2 x _ { k } } { ( { \bf x } , x ) ^ { 2 } } .\tag{2}
$$

Evaluating this at $\mathbf { x } _ { 0 } = [ x _ { 1 } ^ { 0 } x _ { 2 } ^ { 0 } \cdots x _ { n } ^ { 0 } ] ^ { \mathbf { T } }$ , where $A \pmb { x } _ { 0 } = \lambda _ { 0 } \pmb { x } _ { 0 }$ and thus $\begin{array} { r } { A _ { k * } \pmb { x } _ { 0 } = \lambda _ { 0 } x _ { k } ^ { 0 } . } \end{array}$ we deduce that the numerator in Eq. (2) is equal to zero:

$$
( { \pmb x } _ { 0 } , { \pmb x } _ { 0 } ) ( 2 A _ { k _ { 4 } } { \pmb x } _ { 0 } ) - ( A { \pmb x } _ { 0 } , { \pmb x } _ { 0 } ) 2 x _ { k } ^ { 0 } = ( { \pmb x } _ { 0 } , { \pmb x } _ { 0 } ) 2 \lambda _ { 0 } x _ { k } ^ { 0 } - \lambda _ { 0 } ( { \pmb x } _ { 0 } , { \pmb x } _ { 0 } ) 2 x _ { k } ^ { 0 } = 0 .
$$

This completes the proof.

## 8.4 Problems with Constraints

Long before the formulation and proof of the Courant-Fischer theorem, mathematicians were faced with eigenvalue computations that arose from maximization problems subject to a constraint. In the variational approach, this means that we seek the stationary values of $R _ { H } ( x )$ where x varies over those nonzero members of $\mathbb { C } ^ { n }$ that satisfy an equation (or constraint) of the form ${ \pmb a } ^ { * } { \pmb x } = 0$ where $\pmb { a } ^ { * } = [ \alpha _ { 1 } \alpha _ { 2 } \cdots \alpha _ { n } ]$ , or

$$
\alpha _ { 1 } x _ { 1 } + \alpha _ { 2 } x _ { 2 } + \cdot \cdot \cdot + \alpha _ { n } x _ { n } = 0 ,
$$

where not all the $a _ { j }$ are zero. Clearly, if $\alpha _ { j } \neq 0$ we can use the constraint to express $x _ { j }$ as a linear combination of the other $\pmb { x } ^ { \prime } \mathbf { s } ,$ substitute it into $R ( { \pmb x } )$ and obtain a new quotient in $n - 1$ variables whose stationary values (and $n - 1$ associated eigenvalues) can be examined directly without reference to constraints. As it happens, this obvious line of attack is not the most profitable and if we already know the properties of the unconstrained system, we can say quite a lot about the constrained one. We shall call eigenvalues and eigenvectors of a problem with constraints constrained eigenvalues and constrained eigenvectors.

More generally, consider the eigenvalue problem subject to r constraints:

$$
( \mathbf { x } , \pmb { a } _ { i } ) = \pmb { a } _ { i } ^ { * } \mathbf { x } = 0 , \qquad i = 1 , 2 , \ldots , r ,\tag{1}
$$

where ${ \mathfrak { a } } _ { 1 } , { \mathfrak { a } } _ { 2 } , \ldots , { \mathfrak { a } } _ { r }$ are linearly independent vectors in $\mathbb { C } ^ { n } .$ Given a Hermitian matrix $H \in \mathbb { C } ^ { n \times n }$ , we wish to find the constrained eigenvalues and constrained eigenvectors of H, that is, the scalars $\lambda \in \mathbb { C }$ and vectors $\pmb { x } \in \mathbb { C } ^ { n }$ such that

$$
H \mathbf { x } = \lambda x , \quad x \neq 0 , \quad \quad { \mathrm { a n d } } \quad \quad ( \mathbf { x } , \mathbf { a } _ { i } ) = a _ { i } ^ { * } x = 0 , i = 1 , 2 , \ldots , r .\tag{2}
$$

Let $\mathcal { A } _ { r }$ be the subspace generated by ${ \mathfrak { a } } _ { 1 } , { \mathfrak { a } } _ { 2 } , \ldots , { \mathfrak { a } } _ { \mathfrak { i } }$ . appearing in Eq. (1) and let $\boldsymbol { \mathcal { C } } _ { n - r }$ denote the orthogonal complement to $\mathcal { A } _ { r }$ in $\mathbb { C } ^ { n }$

$$
\mathcal { A } _ { r } \oplus \mathcal { C } _ { n - r } = \mathbb { C } ^ { n } .
$$

If $b _ { 1 } , b _ { 2 } , \ldots , b _ { n - r }$ is an orthonormal basis in $\boldsymbol { \mathcal { C } } _ { n - r }$ and

$$
B = [ { \pmb b } _ { 1 } \quad { \pmb b } _ { 2 } \quad \cdots \quad { \pmb b } _ { n - r } ] ,
$$

then, obviously, $\begin{array} { r } { B \in \mathbb { C } ^ { n \times ( n - r ) } , B ^ { * } B = I _ { n - r } , } \end{array}$ and $B B ^ { * }$ is an orthogonal projector onto $\boldsymbol { \mathcal { C } } _ { n - r }$ (see Section 5.8).

The vector $\pmb { x } \in \mathbb { C } ^ { n }$ satisfies the constraints of Eq. (1) if and only if $\pmb { x } \in \mathcal { C } _ { n - r }$ That is, $B B ^ { * } x = x$ and the vector $\mathbf { y } = B ^ { * } \mathbf { x } \in \mathbb { C } ^ { n - r }$ satisfies $x = B y , \mathrm { S o }$ , for $\qquad x \neq \theta ,$

$$
R _ { H } ( { \pmb x } ) = \frac { ( H { \pmb x } , { \pmb x } ) } { ( { \pmb x } , { \pmb x } ) } = \frac { ( H B { \pmb y } , B { \pmb y } ) } { ( B { \pmb y } , B { \pmb y } ) } = \frac { ( B ^ { \ast } H B { \pmb y } , { \pmb y } ) } { ( B ^ { \ast } B { \pmb y } , { \pmb y } ) } .
$$

Since $B ^ { * } B = I _ { n - r } ,$ we obtain

$$
R ( \pmb { x } ) \equiv R _ { H } ( \pmb { x } ) = R _ { B ^ { * } H B } ( \pmb { y } )\tag{3}
$$

and the problem in Eq. (2) is reduced to the standard form of finding the stationary values of the Rayleigh quotient for the $( n - r ) \times ( n - r )$ Hermitian matrix $B ^ { * } H B$ (Section 8.3). We have seen that these occur only at the eigenvalues of $B ^ { * } H B$ . Thus λ is a constrained eigenvalue of H with associated eigenvector x if and only if λ is an eigenvalue of $B ^ { * } H B$ with eigenvector y, where $\boldsymbol { x } = B \boldsymbol { y }$

Let the constrained eigenvalues be $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n - }$ , and let

$$
y _ { 1 } , y _ { 2 } , \ldots , y _ { n - r }
$$

be associated orthonormal eigenvectors of $B ^ { * } H B$ Then $\pmb { x } _ { 1 } = B \pmb { y } _ { 1 } , \dots , \pmb { x } _ { n - r } =$ $B y _ { n - 1 }$ , are the corresponding constrained eigenvectors. They are also orthonormal since, for $i , j = 1 , 2 , \dots , n - r ,$

$$
\delta _ { i j } = ( \pmb { x _ { i } } , \pmb { x _ { j } } ) = ( B \pmb { y _ { i } } , B \pmb { y _ { j } } ) = ( B ^ { * } B \pmb { y _ { i } } , \pmb { y _ { j } } ) = ( \pmb { y _ { i } } , \pmb { y _ { j } } ) .
$$

For $i = 1 , 2 , \ldots , n - r ,$ let $X _ { i }$ be the subspace in $\mathbb { C } ^ { n }$ generated by the vectors $\mathbf { { x } } _ { i } , { \mathbf { { x } } } _ { i + 1 } , \ldots , { \mathbf { { x } } } _ { n - r }$ .By first applying Theorem 8.2.1 to $B ^ { * } H B$ in $\mathbb { C } ^ { n - r }$ and then transforming the result to $\mathbb { C } ^ { n }$ and using Eq. (3), we easily derive the following result.

Proposition 1. If $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n - }$ are the eigenvalues of the constrained eigenvalue problem (2) with associated orthonormal eigenvectors $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { n - r } ,$ then for $i = 1 , 2 , \ldots , n - r ,$

$$
\lambda _ { i } = \operatorname* { m i n } _ { \pmb { \theta } \neq \pmb { x } \in X _ { i } } R ( \pmb { x } ) ,
$$

where $X _ { i }$ is the subspace generated by $\mathbf { x } _ { i } , \mathbf { x } _ { i + 1 } , \ldots , \mathbf { x } _ { n - r }$

Similarly, using Exercise 8.2.1, we have another result.

Proposition 2. With the notation of Proposition 1,

$$
\lambda _ { i } = \operatorname* { m a x } _ { \substack { \theta \neq x \in X _ { n - r - i + 1 } } } R ( { \pmb x } ) , \qquad i = 1 , 2 , \ldots , n - r ,
$$

where $X _ { n - r - i + 1 }$ is the space generated by $\pmb { x } _ { n - r - i + 1 } , \ldots , \pmb { x } _ { n - r } .$

We consider now the relationships between the eigenvalues of a constrained eigenvalue problem and those of the initial unconstrained problem. The main result in this direction is sometimes known as Rayleigh's theorem,† although Rayleigh himself attributes it to Routh and it had been used even earlier by Cauchy. It is easily proved with the aid of the Courant-Fischer theorem.

Theorem 1. If $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n - r }$ are the eigenvalues of the eigenvalue problem (2) for a Hermitian $H \in \mathbb { C } ^ { n \times n }$ with r constraints, then

$$
\mu _ { i } \leq \lambda _ { i } \leq \mu _ { i + r } , \qquad i = 1 , 2 , \ldots , n - r ,
$$

where $\mu _ { 1 } \leq \mu _ { 2 } \leq \cdots \leq \mu _ { n }$ are the eigenvalues of the corresponding unconstrained problem $H \mathbf { x } = \mu \mathbf { x } , \mathbf { x } \neq \pmb { \theta } .$

ProOF. First recall the definition of the space $X _ { i }$ in Proposition 1 and observe that dim $X _ { i } = n - r - i + 1$ . It follows from Theorem 8.2.2 that

$$
\mu _ { i + r } = \operatorname* { m a x } _ { \mathcal { S } _ { i + r } } \operatorname* { m i n } _ { \pmb { \mathscr { S } } \neq \pmb { x } \in \mathcal { S } _ { i + r } } R ( \pmb { x } ) \geq \operatorname* { m i n } _ { \pmb { \mathscr { S } } \neq \pmb { x } \in X _ { i } } R ( \pmb { x } ) .
$$

By virtue of Proposition 1,

$$
\mu _ { i + r } \geq \operatorname* { m i n } _ { \theta \neq x \in X _ { i } } R ( { \pmb x } ) = \lambda _ { i } ,
$$

and the first inequality is established.

For the other inequality we consider the eigenvalues $\nu _ { 1 } \leq \nu _ { 2 } \leq \cdots \leq \nu _ { n }$ of the matrix - H. Obviously, $\nu _ { i } = - \mu _ { n + 1 - i }$ . Similarly, let the eigenvalues of — H under the given r constraints in (1) be $\omega _ { 1 } \leq \omega _ { 2 } \leq \cdot \cdot \cdot \leq \omega _ { n - r } ,$ where

$$
\omega _ { i } = - \lambda _ { n - r + 1 - i } \qquad \mathrm { f o r } \quad i = 1 , 2 , \ldots , n - r .
$$

Applying the result just proved for H to the matrix — H, we obtain

$$
\nu _ { i + r } \geq \omega _ { i } ,
$$

for $i = 1 , 2 , \ldots , n - r ,$ and hence

$$
- \mu _ { n + 1 - i - r } \geq - \lambda _ { n - r + 1 - i } .
$$

Writing $j = n + 1 - r - i ,$ we finally have $\mu _ { j } \leq \lambda _ { j }$ for $j = 1 , 2 , \dots , n - r ,$ and the theorem is proved.■

Note the following particular case of this theorem in which the “interlacing" of the constrained and unconstrained eigenvalues is most obvious.

Corollary 1. If $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n - 1 }$ are the eigenvalues of H with one constraint and $\mu _ { 1 } \leq \mu _ { 2 } \leq \cdot \cdot \cdot \leq \mu _ { n }$ are eigenvalues of H, then

$$
\mu _ { 1 } \leq \lambda _ { 1 } \leq \mu _ { 2 } \leq \cdot \cdot \cdot \leq \mu _ { n - 1 } \leq \lambda _ { n - 1 } \leq \mu _ { n } .
$$

Note also that the eigenvalue problem for H with linear constraints (1) can be interpreted as an unconstrained problem for a leading principal submatrix of a matrix congruent to H.

More precisely, let $H \in \mathbb { C } ^ { n \times n }$ be a Hermitian matrix generating the Rayleigh quotient $R ( x )$ and let B denote the matrix introduced at the beginning of the section, that is, $B = [ \pmb { b } _ { 1 } \quad \pmb { b } _ { 2 } \quad \cdots \quad \pmb { b } _ { n - r } ]$ , where $\{ \pmb { b } _ { j } \} _ { j = 1 } ^ { n - r }$ forms an orthonormal basis in $\mathcal { C } _ { n - r }$ the orthogonal complement of $\mathcal { A } _ { r }$ in C". Consider the matrix $C = [ B A ]$ , where the columns of A form an orthonormal basis in $\mathcal { A } _ { r }$ , and note that C is unitary and, therefore, the matrix $C ^ { * } H C$ has the same eigenvalues as H. Since

$$
\begin{array} { r } { C ^ { * } H C = \left[ \begin{array} { l } { B ^ { * } } \\ { A ^ { * } } \end{array} \right] H \left[ B \quad A \right] = \left[ \begin{array} { l l } { B ^ { * } H B } & { B ^ { * } H A } \\ { A ^ { * } H B } & { A ^ { * } H A } \end{array} \right] , } \end{array}
$$

$B ^ { * } H B$ is the $( n - r ) \times ( n - r )$ leading principal submatrix of $C ^ { * } H C$ . Thus, the constrained eigenvalue problem for H described above is reduced to finding the eigenvalues of a leading principal submatrix of a matrix congruent to H. This last problem is interesting in its own right and will be considered in the next section.

Exercise 1. Consider the matrix A of Exercise 5.2.8. Examine the constrained eigenvalues under one constraint for each of the following constraint equations and verify Corollary 1 in each case:

$$
\begin{array} { r l } { \mathrm { ( a ) } } & { { } x _ { 1 } = 0 ; } \\ { \mathrm { ( b ) } } & { { } x _ { 1 } - x _ { 2 } = 0 ; } \\ { \mathrm { ( c ) } } & { { } x _ { 1 } - x _ { 3 } = 0 . \quad \bigtriangledown } \end{array}
$$

## 8.5 The Rayleigh Theorem and Definite Matrices

Let H be an $n \times n$ Hermitian matrix and let $H _ { n - r }$ be an $( n - r ) \times ( n - r )$ principal submatrix of H, and $1 \leq r < n$ . The following result can be viewed as a special case of Theorem 8.4.1.

Theorem 1 (Rayleigh). If $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n }$ -r are the eigenvalues of $H _ { n - r }$ and $\mu _ { 1 } \leq \mu _ { 2 } \leq \cdot \cdot \cdot \leq \mu _ { n }$ are the eigenvalues of H, then for $i =$ $1 , 2 , \ldots , n - r ,$

$$
\mu _ { i } \leq \lambda _ { i } \leq \mu _ { i + r } .\tag{1}
$$

PROOF. If $H _ { n - r }$ is not the $( n - r ) \times ( n - r )$ leading principal submatrix of H we apply a permutation matrix P so that it is in this position in the transformed matrix $P ^ { \boldsymbol { \mathsf { T } } } H P$ Since $P ^ { - 1 } = P ^ { \mathsf { T } }$ , the matrix $P ^ { \boldsymbol { \mathsf { T } } } H P$ has the same spectrum as H, so without loss of generality we may assume that $H _ { n - r }$ is the $( n - r ) \times ( n - r )$ leading principal submatrix of H.

In view of the concluding remarks of the previous section, the eigenvalues of $H _ { n - r }$ are those of an eigenvalue problem for $C H C ^ { * }$ with r constraints, where C is some unitary matrix. This also follows from the easily checked relation $B ^ { * } ( C H C ^ { * } ) ~ B = H _ { n - r }$ . Appealing to Theorem 8.4.1, we obtain

$$
\tilde { \mu } _ { i } \leq \lambda _ { i } \leq \tilde { \mu } _ { i + r } , \qquad i = 1 , 2 , \ldots , n - r ,
$$

where $\tilde { \mu } _ { 1 } , \tilde { \mu } _ { 2 } , \ldots , \tilde { \mu } _ { n }$ are the eigenvalues of $C H C ^ { * }$ . It remains now to observe that, because C is unitary, $\tilde { \mu } _ { j } = \mu _ { j } \mathrm { f o r } j = 1 , 2 , \ldots , n$ and this completes the proof.

Exercise 1. All principal minors of a positive definite matrix are positive.

SOLUTION. For the eigenvalues $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n - 1 }$ , of a principal submatrix $H _ { n } .$ -, of H we have, using Eq. (1)

$$
0 < \mu _ { 1 } \leq \lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdot \cdot \cdot \leq \lambda _ { n - r } ,
$$

where $\mu _ { 1 }$ denotes the smallest eigenvalue of the positive definite matrix H. But then det $H _ { n - r } = \lambda _ { 1 } \lambda _ { 2 } \dotsm \lambda _ { n - r }$ is positive and the assertion follows.□

We can now develop a different approach to definite matrices, one in which they are characterized by determinantal properties.

Theorem 2 (G. Frobenius†). An $n \times n$ Hermitian matrix H is positive defnite if and only if all of its leading principal minors,

$$
H { \binom { 1 } { 1 } } , \qquad H { \binom { 1 } { 1 } } , \quad 2 \biggr ) , \qquad \ldots , \qquad H { \binom { 1 } { 1 } } \quad 2 \quad \cdots \quad n \biggr ) ,\tag{2}
$$

are positive.

PROOF. If $H > 0$ then, by Exercise 1, all of its principal minors and, in particular, the leading principal minors of H are positive.

Conversely, let the minors (2) be positive. Denote by $H _ { k } \left( 1 \leq k \leq n \right)$ the $k \times k$ leading principal submatrix of H; we prove by induction on k that the matrix $H _ { n } = H$ is positive definite.

First, for $k = 1$ the $1 \times 1$ matrix $H _ { 1 }$ is obviously positive definite. Then suppose that the matrix $H _ { k } \ ( 1 \leq k \leq n - 1 )$ is positive definite and let us show that $H _ { k + 1 }$ is also positive definite. Note that the assumption $H _ { k } > 0$ means the positivity of the eigenvalues $\lambda _ { 1 } ^ { ( k ) } \leq \lambda _ { 2 } ^ { ( k ) } \leq \cdots \leq \lambda _ { k } ^ { ( k ) }$ of $H _ { k }$ . If now $\hat { \nearrow } _ { \times _ { 1 } } ^ { ( k + 1 ) } \le \lambda _ { 2 } ^ { ( k ^ { - } + 1 ) } \le \cdots \le \lambda _ { k + 1 } ^ { ( k + 1 ) }$ are the eigenvalues of $H _ { k + 1 }$ , then Theorem 1 yields

$$
\lambda _ { 1 } ^ { ( k + 1 ) } \leq \lambda _ { 1 } ^ { ( k ) } \leq \lambda _ { 2 } ^ { ( k + 1 ) } \leq \cdots \leq \lambda _ { k } ^ { ( k + 1 ) } \leq \lambda _ { k } ^ { ( k ) } \leq \lambda _ { k + 1 } ^ { ( k + 1 ) } ,
$$

and the positivity of the eigenvalues $\lambda _ { i } ^ { ( k ) } \left( i = 1 , 2 , \ldots , k \right)$ implies positivity of the numbers $\lambda _ { 2 } ^ { ( k + 1 ) } , \ \lambda _ { 3 } ^ { ( k \mp 1 ) } , \ \dots , \ \lambda _ { k + 1 } ^ { ( k + 1 ) }$ . But also $\lambda _ { 1 } ^ { ( k + 1 ) }$ is positive since the positivity of the minors in (2) implies

$$
\operatorname* { d e t } H _ { k + 1 } = \lambda _ { 1 } ^ { ( k + 1 ) } \lambda _ { 2 } ^ { ( k + 1 ) } \dots \lambda _ { k + 1 } ^ { ( k + 1 ) } > 0 .
$$

Thus, all the eigenvalues of $H _ { k + 1 }$ are positive, that is, $H _ { k + 1 }$ is positive definite.

Note that, in fact, all the leading principal submatrices of a positive definite matrix are positive definite.

Exercise 2. Confirm the following criterion for negative definiteness of an n × n Hermitian matrix: $H < 0$ if and only if the leading principal minors det $H _ { k } \left( k = 1 , 2 , \ldots , n \right)$ of H satisfy the conditions det $H _ { 1 } < 0$ and

$$
( \operatorname* { d e t } H _ { k } ) ( \operatorname* { d e t } H _ { k + 1 } ) < 0
$$

for $k = 1 , 2 , \ldots , n - 1 . \quad \bigsqcup$

Thus, a Hermitian matrix $H = [ h _ { i j } ] _ { i , j = 1 } ^ { n }$ is negative definite if and only if $h _ { 1 1 } < 0$ and the signs of its leading principal minors alternate.

The tests for positive and negative definiteness presented in this section are often used in practice since they are readily implemented from a computational point of view. Some generalizations of these results will be considered in the next section.

## 8.6 The Jacobi-Gundelfinger-Frobenius Method

The following result is a generalization of the Sylvester theorem. For a general Hermitian matrix H, it gives a criterion for finding the inertia of H, as defined in Section 5.5.

Theorem 1 (G. Jacobi†). Let $H _ { 1 } , \ H _ { 2 } , \ldots , H _ { n }$ be the leading principal submatrices of a Hermitian matrix $H \in \mathbb { C } ^ { n \times n }$ of rank r, and assume that $d _ { k } = \operatorname* { d e t } H _ { k } \neq 0 , k = 1 , 2 , \ldots , r .$ Then the number of negative (respectively, positive) eigenvalues of H is equal to the number of alterations (respectively constancies) of sign in the sequence

$$
1 , d _ { 1 } , d _ { 2 } , \ldots , d _ { r } .\tag{1}
$$

ProoF. We prove this result by induction. If $k = 1$ , then $d _ { 1 }$ is the (unique) eigenvalue of $H _ { 1 }$ and obviously $d _ { 1 }$ is negative or positive according as there is an alteration or constancy of sign in the sequence $1 , d _ { 1 }$

Suppose that the statement holds for the leading principal submatrix $H _ { k }$ , that is, the number of negative (respectively, positive) eigenvalues of $H _ { k }$ is equal to the number of alterations (respectively, constancies) of sign in the sequence 1, $d _ { 1 } , d _ { 2 } , \ldots , d _ { k }$ . The transition to $H _ { k + 1 }$ adds to this sequence the nonzero number $d _ { k + 1 } =$ det $H _ { k + 1 }$ . If $d _ { k + 1 } > 0$ , then (see Eq. (4.11.3)) the product of all the eigenvalues

$$
\lambda _ { 1 } ^ { ( k + 1 ) } \leq \lambda _ { 2 } ^ { ( k + 1 ) } \leq \cdot \cdot \cdot \leq \lambda _ { k + 1 } ^ { ( k + 1 ) }
$$

of $H _ { k + 1 }$ is positive. Furthermore, $d _ { k } = \lambda _ { 1 } ^ { ( k ) } \lambda _ { 2 } ^ { ( k ) } \cdot \cdot \cdot \lambda _ { k } ^ { ( k ) }$ . Consider the case $d _ { k } > 0 .$ Then in the sequence 1, $d _ { 1 } , \ldots , d _ { k } , d _ { k + 1 }$ the sign is changed the same number of times as in the sequence 1, $d _ { 1 } , \ldots , d _ { k }$ , and hence our aim is to show that $H _ { k + 1 }$ has the same number of negative eigenvalues and one more positive eigenvalue than $H _ { k }$

Indeed, let $H _ { k }$ have m $( 1 \leq m \leq k )$ negative and $k - m$ positive eigenvalues:

$$
\lambda _ { 1 } ^ { ( k ) } \leq \cdot \cdot \cdot \leq \lambda _ { m } ^ { ( k ) } < 0 < \lambda _ { m + 1 } ^ { ( k ) } \leq \cdot \cdot \cdot \leq \lambda _ { k } ^ { ( k ) } .
$$

By Theorem 8.5.1, $\lambda _ { m } ^ { ( k ) } \leq \lambda _ { m + 1 } ^ { ( k + 1 ) } \leq \lambda _ { m + 1 } ^ { ( k ) }$ and two cases can occur:

$$
\lambda _ { m + 1 } ^ { ( k + 1 ) } < 0 \qquad \mathrm { o r } \qquad \lambda _ { m + 1 } ^ { ( k + 1 ) } > 0 .
$$

The first inequality is impossible in the case $d _ { k } > 0$ and $d _ { k + 1 } > 0$ presently being considered. In fact, if

$$
\lambda _ { 1 } ^ { ( k + 1 ) } \leq \lambda _ { 1 } ^ { ( k ) } \leq \cdot \cdot \cdot \leq \lambda _ { m } ^ { ( k ) } \leq \lambda _ { m + 1 } ^ { ( k + 1 ) } < 0 < \lambda _ { m + 1 } ^ { ( k ) } \leq \cdot \cdot \cdot \leq \lambda _ { k + 1 } ^ { ( k + 1 ) } ,
$$

we have

$$
\begin{array} { r l } & { \mathrm { s i g n } d _ { k + 1 } = \mathrm { s i g n } ( \lambda _ { 1 } ^ { ( k + 1 ) } \lambda _ { 2 } ^ { ( k + 1 ) } \cdot \cdot \cdot \lambda _ { k + 1 } ^ { ( k + 1 ) } ) = ( - 1 ) ^ { m + 1 } , } \\ & { \quad \quad \mathrm { s i g n } d _ { k } = \mathrm { s i g n } ( \lambda _ { 1 } ^ { ( k ) } \lambda _ { 2 } ^ { ( k ) } \cdot \cdot \cdot \lambda _ { k } ^ { ( k ) } ) = ( - 1 ) ^ { m } , } \end{array}
$$

a contradiction with the assumption sign $d _ { k + 1 } = \sin d _ { k } = 1$ . Thus, $\lambda _ { m + 1 } ^ { ( k + 1 ) } > 0$ and $H _ { k + 1 }$ has one more positive eigenvalue than $H _ { k }$

Other cases are proved similarly to complete an inductive proof of the theorem.

Exercise 1. Consider the matrix

$$
H = { \left[ \begin{array} { l l l } { 2 } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { { \frac { 1 } { 2 } } } & { 0 } & { - 1 } \end{array} \right] }
$$

associated with the real Hermitian form discussed in Exercise 5.11.2(a). Since

$$
\begin{array} { r } { d _ { 1 } = 2 , \qquad d _ { 2 } = \operatorname* { d e t } { \left[ \begin{array} { l l } { 2 } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 2 } } } & { 0 } \end{array} \right] } = - { \frac { 1 } { 4 } } , \qquad d _ { 3 } = \operatorname* { d e t } H = { \frac { 1 } { 4 } } , } \end{array}
$$

the number of alterations of sign in the sequence $1 , 2 , - { \textstyle { \frac { 1 } { 4 } } } , { \textstyle { \frac { 1 } { 4 } } } \mathrm { o r } $ , what is equivalent, in the sequence of signs $+ , + , - , +$ is equal to $^ { 2 , }$ while the number of constancies of sign is 1. Thus, $\pi ( H ) = 1 , \nu ( H ) = 2 ;$ , and the first canonical form of the corresponding Hermitian form contains one positive and two negative squares.

It is clear that this method of finding the inertia (if it works) is simpler than the Lagrange method described in Section 5.11. However, the latter also supplies the transforming matrix.

A disadvantage of the Jacobi method is the strong hypothesis that the leading principal minors be nonzero. This condition is relaxed in the generalizations due to Gundelfinger and Frobenius.

Theorem 2 (S. Gundelfinger†). With the notation of Theorem 1, suppose that the sequence (1) contains no two successive zeros. If det $H _ { r } \neq 0 ;$ then the assertion of Jacobi's theorem remains valid if any sign is assigned to each (isolated) zero $d _ { i } = 0$ in (1).

In other words, for computing the number v(H), single zeros in the sequence (1) can be omitted.

ProoF. Assume inductively that the hypothesis holds for $H _ { 1 } , H _ { 2 } , \dots , H _ { k }$ If det $H _ { k + 1 } \neq 0 ;$ then the appropriate part of the proof of Jacobi's theorem can be repeated to show that the transition from 1, $d _ { 1 } , \ldots , d _ { k }$ (with signs instead of zeros) to $1 , d _ { 1 } , \dotsc , d _ { k + 1 }$ adds an alteration or a constancy of sign (between $d _ { k }$ and $d _ { k + 1 } )$ according as $H _ { k + }$ ,has one more negative or positive eigenvalue than $H _ { k }$

Suppose that dk+1 = det $H _ { k + 1 } = 0$ . Then at least one eigenvalue $\lambda _ { i } ^ { ( k + 1 ) }$ $( 1 \leq i \leq k + 1 )$ must be zero. Since $d _ { k } \neq 0$ and $d _ { k + 2 } \neq 0$ there is exactly one zero eigenvalue of $H _ { k + 1 }$ . Indeed, if $\lambda _ { i } ^ { ( k + 1 ) } = \lambda _ { s } ^ { ( k + 1 ) } = 0 ( i < s ) ,$ then by applying Theorem 8.5.1 there are zero eigenvalues of $H _ { k }$ and $H _ { k + 2 }$ , which yields $d _ { k } = d _ { k + 2 } = 0$

Let $\lambda _ { m + 1 } ^ { ( k + 1 ) } = 0 \left( 1 \leq m \leq k - 1 \right)$ . Then it follows from

$$
\lambda _ { m } ^ { ( k ) } < \lambda _ { m + 1 } ^ { ( k + 1 ) } = 0 < \lambda _ { m + 1 } ^ { ( k ) }
$$

and

$$
\lambda _ { m + 1 } ^ { ( k + 2 ) } < \lambda _ { m + 1 } ^ { ( k + 1 ) } = 0 < \lambda _ { m + 2 } ^ { ( k + 2 ) }\tag{2}
$$

that the number of negative eigenvalues of $H _ { k }$ is m and the number of negative eigenvalues of $H _ { k + 2 }$ is m + 1. Hence sign $d _ { k } = ( - 1 ) ^ { m }$ , sign $d _ { k + 2 } = ( - 1 ) ^ { m + 1 }$ and therefore $d _ { k } d _ { k + 2 } < 0$

If $\lambda _ { 1 } ^ { ( k + 1 ) } = 0$ , then all eigenvalues of $H _ { k }$ are positive and so sign $d _ { k } = 1$ Also, we may put m = 0 in (2) and find that sign $d _ { k + 2 } = - 1$ . Thus $d _ { k } d _ { k + 2 } < 0$ once more. A similar argument gives the same inequality when $\lambda _ { k + 1 } ^ { ( k + 1 } = 0$

It is now clear that, by assigning any sign to $d _ { k + 1 } = 0$ or omitting it, we obtain one alteration of sign from $d _ { k }$ to $d _ { k + 2 }$ . This proves the theorem.

Example 2. Consider the matrix

$$
H = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 1 } \end{array} \right] }
$$

associated with the quadratic form in Exercise 5.11.1. Compute the number of alterations and constancies of sign in the sequence

$$
\begin{array} { r } { 1 , d _ { 1 } = 0 , d _ { 2 } = - 1 , d _ { 3 } = - 1 , } \end{array}
$$

or equivalently, in the sign sequences

$$
+ , + , - , - \mathrm { ~ o r ~ } + , - , - , - .
$$

Using the Gundelfinger rule, we deduce $\nu ( H ) = 1 , \pi ( H ) = 2 . \quad \varsquare$

Theorem 3 (G. Frobenius†). If, in the notation of Theorem 1, det $H _ { r } \neq 0$ and the sequence (1) contains no three successive zeros, then Jacobi's method can be applied by assigning the same sign to the zeros $d _ { i + 1 } = d _ { i + 2 } = 0$ if $d _ { i } d _ { i + 3 } < 0 ,$ and different signs if $d _ { i } d _ { i + 3 } > 0$

ProoF. We only sketch the proof, because it relies on the same argument as that of the previous theorem.

Let $d _ { k + 1 } = d _ { k + 2 } = 0 , d _ { k } \neq 0 , d _ { k + 3 } \neq 0 .$ As before, there is exactly one zero eigenvalue of $H _ { k + 1 } , \ \mathrm { s a y } , \ \lambda _ { m + 1 } ^ { ( k + 1 ) }$ .Similarly, it follows from $\lambda _ { i } ^ { ( k + 3 ) } \neq 0$ $( i = 1 , 2 , \ldots , k + 3 )$ and Theorem 8.5.1 that there exists exactly one zero, $\lambda _ { s + 1 } ^ { ( k + 2 ) } = 0 ( 0 \leq s \leq k + 1 )$ , of $H _ { k + 2 }$ . Using Theorem 8.5.1 to compare the eigenvalues of $H _ { k + 1 }$ and $H _ { k + 2 }$ , it is easily seen that either $s = m \operatorname { o r } s = m + 1$

The distribution of eigenvalues in the case $s = m$ looks as follows:

$$
\begin{array} { r l } & { \lambda _ { m } ^ { ( k ) } < \lambda _ { m + 1 } ^ { ( k + 1 ) } = 0 , \qquad \lambda _ { m } ^ { ( k + 1 ) } < \lambda _ { m + 1 } ^ { ( k + 2 ) } = 0 = \lambda _ { m + 1 } ^ { ( k + 1 ) } , } \\ & { \qquad \lambda _ { m } ^ { ( k + 2 ) } \leq \lambda _ { m + 1 } ^ { ( k + 3 ) } < \lambda _ { m + 1 } ^ { ( k + 2 ) } = 0 < \lambda _ { m + 2 } ^ { ( k + 3 ) } . } \end{array}
$$

Hence the matrices $H _ { k } , H _ { k + 1 } , H _ { k + 2 }$ , and $H _ { k + 3 }$ have, respectively, m, m, m, and $m + 1$ negative eigenvalues.

Thus, for $s = m$ we have $d _ { k } d _ { k + 3 } < 0$ and, in this case, $H _ { k + 3 }$ has one more negative eigenvalue than $H _ { k }$ . Assigning to the zeros $d _ { k + 1 } , d _ { k + 2 }$ the same sign, we obtain only one alteration of sign in the sequence $d _ { k } , d _ { k + 1 } , d _ { k + 2 } , d _ { k + 3 }$ 2 which proves the theorem in this case.

It is similarly found that if $s = m + 1$ , then $d _ { k } d _ { k + 3 } > 0 _ { : }$ and the assertion of the theorem is valid.

It should be emphasized that, as illustrated in the next exercise, a further improvement of Jacobi's theorem is impossible. In other words, if the sequence (1) contains three or more successive zeros, then the signs of the leading principal minors do not uniquely determine the inertia characteristics of the matrix.

Example 3. The leading principal minors of the Hermitian matrix

$$
H = { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { b } \\ { 0 } & { a } & { 0 } & { 0 } \\ { 0 } & { 0 } & { a } & { 0 } \\ { b } & { 0 } & { 0 } & { 0 } \end{array} \right] } , \qquad a , b \neq 0 ,
$$

are

$$
d _ { 1 } = d _ { 2 } = d _ { 3 } = 0 , d _ { 4 } = a ^ { 2 } b ^ { 2 } < 0 .
$$

On the other hand, the characteristic polynomial of H is $( \lambda ^ { 2 } - b ^ { 2 } ) ( \lambda - a ) ^ { 2 }$ and hence $\sigma ( H ) = \{ b , - b , a , a \}$ . Thus for $a > 0$ we have $\pi ( H ) = 3 , \nu ( H ) = 1$ while for $a < 0$ we have $\pi ( H ) = 1 , \nu ( H ) = 3$ , and the inertia of H is not uniquely determined by the signs of its leading principal minors. □

Note also that if the rank r of H fails to be attained on the leading principal submatrix $H _ { r }$ of H that is, $d _ { r } = 0 ,$ then the Jacobi theorem cannot be applied.

Exercise 4. Observe that the Hermitian matrix

$$
H = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { a } \end{array} \right] }
$$

with $a \neq 1$ has rank 2, while $d _ { 2 } = \operatorname* { d e t } \ H _ { 2 } = 0 .$ Furthermore, the leading principal minors $d _ { 1 } = 1 , d _ { 2 } = d _ { 3 } = 0$ do not depend on the values assigned to $^ { a , }$ whereas the inertia of H does:

$$
\operatorname* { d e t } ( \lambda I - H ) = \lambda [ \lambda ^ { 2 } - ( a + 2 ) \lambda + ( 2 a - 2 ) ] .
$$

Since for the nonzero eigenvalues $\lambda _ { 1 } , \lambda _ { 2 }$ of H we have $\lambda _ { 1 } \lambda _ { 2 } = 2 a - 2$ and $\lambda _ { 1 } + \dot { \iota } _ { 2 } = a + 2$ , it follows that $\pi ( H ) = 2 \mathrm { i f } a > 1$ and $\pi ( H ) = 1$ for $a < 1$ . □

## 8.7 An Application of the Courant-Fischer Theory

Consider two $n \times n$ Hermitian matrices $H _ { 1 }$ and $H _ { 2 }$ . We say that $H _ { 2 }$ is not greater than $H _ { 1 : }$ written $H _ { 1 } \geq H _ { 2 }$ or $H _ { 2 } \leq H _ { 1 } ,$ , if the difference $H _ { 1 } \mathrm { ~ - ~ } H _ { 2 }$ is a positive semi-definite matrix. Similarly, we write $H _ { 1 } > H _ { 2 }$ or $H _ { 2 } < H _ { 1 }$ if $H _ { 1 } - H _ { 2 } > 0$ These relations preserve some properties of the natural ordering of real numbers (see Exercise 5.14.21). However, there are properties of numerical inequalities that fail to be true for Hermitian matrices. For instance, from $H _ { 1 } \geq H _ { 2 } \geq 0$ the inequality $H _ { 1 } ^ { 2 } \geq H _ { 2 } ^ { 2 }$ does not follow in general.

Exercise 1. Check that $H _ { 1 } \geq H _ { 2 } \geq 0$ if

$$
H _ { 1 } = { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 2 } \end{array} \right] } , \qquad H _ { 2 } = { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] } ,
$$

while $H _ { 1 } ^ { 2 } - H _ { 2 } ^ { 2 }$ fails to be a positive semi-definite matrix. □

Applying the Courant-Fischer theory, a relation between the eigenvalues of matrices $H _ { 1 }$ and $H _ { 2 }$ satisfying the condition $H _ { 1 } \geq H _ { 2 }$ can be derived. This can also be viewed as a perturbation result: What can be said about the perturbations of eigenvalues of $H _ { 2 }$ under addition of the positive semidefinite matrix $H _ { 1 } \mathrm { ~ - ~ } H _ { 2 } ?$

Theorem 1. Let $H _ { 1 } , H _ { 2 } \in \mathcal { F } ^ { n \times n }$ be Hermitian matrices for which $H _ { 1 } \geq H _ { 2 }$ $I f \mu _ { 1 } ^ { ( k ) } \leq \mu _ { 2 } ^ { ( k ) } \leq \cdots \leq \mu _ { n } ^ { ( k ) }$ denote the eigenvalues of $H _ { k } \left( k = 1 , 2 \right)$ and the rank of the matrix $H = H _ { 1 } - H _ { 2 }$ is r, then

$$
\begin{array} { r l } { ( a ) } & { \mu _ { i } ^ { ( 1 ) } \geq \mu _ { i } ^ { ( 2 ) } f o r i = 1 , 2 , \ldots , n ; } \\ { ( b ) } & { \mu _ { j } ^ { ( 1 ) } \leq \mu _ { j + r } ^ { ( 2 ) } f o r j = 1 , 2 , \ldots , n - r . } \end{array}
$$

ProOF. Observe that the condition $H \geq 0$ implies, by Theorem 5.3.3, that

$$
( H _ { 1 } \pmb { x } , \pmb { x } ) = ( ( H _ { 2 } + H ) \pmb { x } , \pmb { x } ) = ( H _ { 2 } \pmb { x } , \pmb { x } ) + ( H \pmb { x } , \pmb { x } ) \geq ( H _ { 2 } \pmb { x } , \pmb { x } )
$$

for any $\boldsymbol { x } \in \mathcal { F } ^ { n }$ . Thus, if $\mathcal { S }$ is any subspace in ${ \mathcal { F } } ^ { n }$ , then

$$
\operatorname* { m i n } ( H _ { 1 } x , x ) \geq \operatorname* { m i n } ( H _ { 2 } x , x ) ,\tag{1}
$$

where the minima are over all vectors $\pmb { x } \in \mathcal S$ such that $( { \pmb x } , { \pmb x } ) = 1$ . In particular, considering all the subspaces $\mathcal { S } _ { i }$ of dimension $n - i + 1$ , where $1 \leq i \leq n ,$ we deduce from (1) and Theorem 8.2.2 that

$$
\mu _ { i } ^ { ( 1 ) } = \operatorname* { m a x } _ { \scriptstyle \mathscr { S } _ { i } \atop \scriptstyle \mathscr { S } _ { i } \atop \scriptstyle \mathscr { S } _ { i } \atop \scriptstyle \mathscr { S } _ { i } \mathscr { L } _ { i } } \operatorname* { m i n } _ { \scriptstyle \mathscr { S } _ { i } \atop \scriptstyle \mathscr { S } _ { i } \atop \scriptstyle \mathscr { S } _ { i } \atop \scriptstyle \mathscr { S } _ { i } \mathscr { L } _ { i } } \operatorname* { m i n } _ { \scriptstyle \mathscr { S } _ { i } \atop \scriptstyle \mathscr { S } _ { i } \atop \scriptstyle \mathscr { S } _ { i } \mathscr { L } _ { i } } ( H _ { 2 } \pmb { x } , \pmb { x } ) = \mu _ { i } ^ { ( 2 ) }
$$

for $i = 1 , 2 , \dots , n .$ This proves part (a) of the theorem.

For the second part, assume that H has positive eigenvalues $\nu _ { 1 } , \ldots , \nu _ { r }$ and eigenvalues $\nu _ { r + 1 } = \cdot \cdot \cdot = \nu _ { n } = 0$ , together with an associated orthonormal basis of eigenvectors ${ \mathfrak { x } } _ { 1 } , { \mathfrak { x } } _ { 2 } , \ldots , { \mathfrak { x } } _ { n }$ . For any $\boldsymbol { x } \in \mathbb { C } ^ { n }$ write ${ \pmb x } =$ $\sum \limits _ { j = 1 } ^ { n } \alpha _ { j } \bf { x } _ { j }$ . Then we have [see also Eq. (5.10.9)]

$$
( H \pmb { x } , \pmb { x } ) = \sum _ { j = 1 } ^ { r } \nu _ { j } | \alpha _ { j } | ^ { 2 } .
$$

Write ${ \bf y } _ { j } = \nu _ { j } ^ { 1 / 2 } x _ { j } \mathrm { f o r } j = 1 , 2 , \ldots , r$ and use the fact that $\boldsymbol { \alpha } _ { j } = ( \mathbf { x } , \mathbf { x } _ { j } )$ (Exercise 3.12.3) to obtain

$$
\sum _ { j = 1 } ^ { r } \nu _ { j } | \alpha _ { j } | ^ { 2 } = \sum _ { j = 1 } ^ { r } | ( x , y _ { j } ) | ^ { 2 } ,
$$

and note that $y _ { 1 } , \ldots , y _ { r }$ are obviously linearly independent. Since $H _ { 1 } =$ $H _ { 2 } + H$ , we now have

$$
( H _ { 1 } \mathbf { x } , \pmb { x } ) = ( H _ { 2 } \pmb { x } , \pmb { x } ) + \sum _ { i = 1 } ^ { r } | ( \pmb { x } , \pmb { y } _ { i } ) | ^ { 2 } ,\tag{2}
$$

and we consider the eigenvalue problems for $H _ { 1 }$ and $H _ { 2 }$ both with constraints $( \pmb { x } , \pmb { y } _ { i } ) = 0 , i = 1 . 2 , . . . , r .$ Obviously, in view of Eq. (2), the two problems coincide and have the same eigenvalues $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n - r }$ . Applying Theorem 8.4.1 to both problems, we obtain

$$
\mu _ { j } ^ { ( k ) } \le \lambda _ { j } \le \mu _ { j + r } ^ { ( k ) } , \qquad k = 1 , 2 ; \quad j = 1 , 2 , \ldots , n - r ,
$$

which implies the desired result :

$$
\mu _ { j } ^ { ( 1 ) } \le \lambda _ { j } \le \mu _ { j + r } ^ { ( 2 ) } . \quad \equiv
$$

## 8.8 Applications to the Theory of Small Vibrations

We return now to the problem discussed in Section 5.12. In that section we reduced a physical vibration problem to the problem of solving the matrix differential equation $A { \ddot { p } } + C p = 0$ , where A is positive definite and C is either positive definite or semi-definite. This then reduced to the purely algebraic problem of using a congruence transformation to reduce A and C simultaneously to diagonal matrices. This, in turn, was seen to depend on the reduction of the matrix $B = A ^ { - 1 / 2 } C A ^ { - 1 / 2 }$ to diagonal form by means of an orthogonal congruence transformation.

The natural frequencies of vibration of the system are given by the nonnegative square roots of the zeros of det $( A \lambda - C )$ , which are also the eigenvalues of B. We know now, therefore, that the largest natural frequency, $\omega _ { n } = \lambda _ { n } ^ { 1 / 2 }$ , is given by $\lambda _ { n } = \operatorname* { m a x } R _ { 1 } ( { \pmb x } )$ , where $R _ { 1 }$ is the Rayleigh quotient for B and $\pmb { x } \neq \pmb { \theta }$ ranges over $\mathbb { R } ^ { n }$ (see Exercise 8.2.1). Theorems 8.2.1 and 8.2.2 imply that all the natural frequencies can be deined in terms of extreme values of $R _ { 1 }$ . However, observe that if we write $\pmb { x } = A ^ { 1 / 2 } \pmb { q }$ , then

$$
R _ { 1 } ( { \pmb x } ) = \frac { { \pmb x } ^ { \mathrm { T } } A ^ { - 1 / 2 } C A ^ { - 1 / 2 } { \pmb x } } { { \pmb x } ^ { \mathrm { T } } { \pmb x } } = \frac { { \pmb q } ^ { \mathrm { T } } C { \pmb q } } { { \pmb q } ^ { \mathrm { T } } A { \pmb q } } .
$$

The Rayleigh quotient appropriate to this problem is therefore chosen to be

$$
R ( { \pmb q } ) = \frac { { \pmb q } ^ { \operatorname { T } } C { \pmb q } } { { \pmb q } ^ { \operatorname { T } } A { \pmb q } } .
$$

Notice also that if $\boldsymbol { x } _ { j }$ is an eigenvector of $B ,$ then $\pmb q _ { j } = A ^ { - 1 / 2 } \pmb x _ { j }$ is a normalmode vector for the vibration problem and, as in Eqs. (5.12.5),

$$
\begin{array} { r } { \pmb q _ { j } ^ { \operatorname { T } } A \pmb q _ { k } = \delta _ { j k } , \qquad \pmb q _ { j } ^ { \operatorname { T } } C \pmb q _ { k } = \omega _ { j } ^ { 2 } \delta _ { j k } . } \end{array}
$$

On applying each theorem of this chapter to $B ,$ it is easily seen that a generalization is obtained that is applicable to the zeros of det $( A \lambda - C )$ . As an example, we merely state the generalized form of the Courant-Fischer theorem of Section 8.2.

Theorem 1. Given any linearly independent vectors ${ \pmb a } _ { 1 } , { \pmb a } _ { 2 } , \dots , { \pmb a } _ { i - 1 }$ in $\mathbb { R } ^ { n } ;$ let $\mathcal { S } _ { i }$ be the subspace consisting of all vectors in $\mathbb { R } ^ { n }$ that are orthogonal to ${ \pmb a } _ { 1 } , \ldots , { \pmb a } _ { i - 1 }$ . Then

$$
\lambda _ { i } = \operatorname* { m a x } _ { \stackrel { } { \mathcal { S } _ { i } } } \operatorname* { m i n } _ { { \pmb x } \in { \mathcal { S } _ { i } } } \left( \frac { { \pmb x } ^ { \operatorname { T } } C { \pmb x } } { { \pmb x } ^ { \operatorname { T } } A { \pmb x } } \right) .
$$

The minimum is attained when $a _ { j } = q _ { j } , j = 1 , 2 , \ldots , i - 1$

The physical interpretations of Theorems 8.4.1 and 8.7.1 are more obvious in this setting. The addition of a constraint may correspond to holding one point of the system so that there is no vibration at this point. The perturbation considered in Theorem 8.7.1 corresponds to an increase in the stiffness of the system. The theorem tells us that this can only result in an increase in the natural frequencies

## Functions of Matrices

In this chapter we consider matrices A from $C ^ { n \times n }$ (including those of $\mathbb { R } ^ { n \times n }$ as a special case) and the possibility of giving a meaning to $f ( A )$ where $f ( \lambda )$ is a complex-valued function of a complex variable. We would like the definition of $f ( A )$ to hold for as wide a class of functions $f ( \lambda )$ as possible. We have seen that the question is easily resolved if $f ( \lambda ) = p ( \lambda )$ is a polynomial over the complex numbers; thus,

$$
p ( A ) \triangleq \sum _ { i = 1 } ^ { l } p _ { i } A ^ { i } \qquad { \mathrm { i f } } \qquad p ( \lambda ) = \sum _ { i = 0 } ^ { l } p _ { i } \lambda ^ { i } .
$$

Moreover, if $m ( \lambda )$ is the minimal polynomial for $A ,$ then for a polynomial $p ( \lambda )$ there are polynomials $q ( \lambda )$ and $r ( \lambda )$ such that

$$
\begin{array} { r } { p ( \lambda ) = m ( \lambda ) q ( \lambda ) + r ( \lambda ) , } \end{array}
$$

where $r ( \lambda )$ is the zero polynomial or has degree less than that of $m ( \lambda )$ . Thus, since $m ( A ) = O ,$ we have $p ( A ) = r ( A )$

The more general functions $f ( \lambda )$ that we shall consider will retain this property; that is to say, given $f ( \lambda )$ and A, there is a polynomial $r ( \lambda )$ (with degree less than that of the minimal polynomial of A) such that $A )$ $f ( A ) = r ( A )$ It is surprising but true that this constraint still leaves considerable freedom in the nature of the functions $f ( \lambda )$ that can be accommodated.

## 9.1 Functions Defined on the Spectrum of a Matrix

Let $A \in \mathbb { C } ^ { n \times n }$ and suppose that $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ are the distinct eigenvalues of A, so that

$$
m ( \lambda ) = ( \lambda - \lambda _ { 1 } ) ^ { m _ { 1 } } ( \lambda - \lambda _ { 2 } ) ^ { m _ { 2 } } \cdot \cdot \cdot ( \lambda - \lambda _ { s } ) ^ { m _ { s } }\tag{1}
$$

is the minimal polynomial of A with degree $m = m _ { 1 } + m _ { 2 } + \cdot \cdot \cdot + m _ { s }$ Recall that the multiplicity $m _ { k }$ of $\lambda _ { k }$ as a zero of the minimal polynomial is referred to as the index of the eigenvalue $\lambda _ { k }$ (Section 6.2) and is equal to the maximal degree of the elementary divisors associated with $\lambda _ { k } \left( 1 \leq k \leq s \right)$

Given a function $f ( \lambda )$ , we say that it is defined on the spectrum of A if the numbers

$$
f ( \lambda _ { k } ) , f ^ { \prime } ( \lambda _ { k } ) , \ldots , f ^ { ( m _ { k } - 1 ) } ( \lambda _ { k } ) , \qquad k = 1 , 2 , \ldots , s ,\tag{2}
$$

called the values of f(λ) on the spectrum of A, exist. Clearly, every polynomial over C is defined on the spectrum of any matrix from Cⁿ\*". More can be said $\mathbb { C } ^ { n \times n }$ about minimal polynomials.

Exercise 1. Check that the values of the minimal polynomial of A on the spectrum of A are all zeros.

The next result provides a criterion for two scalar polynomials $p _ { 1 } ( \lambda )$ and $p _ { 2 } ( \lambda )$ to produce the same matrix $p _ { 1 } ( A ) = p _ { 2 } ( A )$ . These matrices are defined as described in Section 1.7.

Proposition 1. If $p _ { 1 } ( \lambda )$ and $p _ { 2 } ( \lambda )$ are polynomials over C and $\ b { A } \in \mathbb { C } ^ { n \times n }$ then $p _ { 1 } ( A ) = p _ { 2 } ( A )$ if and only if the polynomials $p _ { 1 } ( \lambda )$ and $p _ { 2 } ( \lambda )$ have the same values on the spectrum of A.

PROOF. If $p _ { 1 } ( A ) = p _ { 2 } ( A )$ and $p _ { 0 } ( \lambda ) = p _ { 1 } ( \lambda ) - p _ { 2 } ( \lambda )$ , then obviously, $p _ { 0 } ( A )$ $= 0$ and hence $p _ { 0 } ( \lambda )$ is an annihilating polynomial for A. Thus (Theorem $6 . 2 . 1 ) p _ { 0 } ( \lambda )$ is divisible by the minimal polynomial m(λ) of A given by (1) and there exists a polynomial $q ( \lambda )$ such that $p _ { 0 } ( \lambda ) = q ( \lambda ) m ( \lambda )$ . Computing the values of $p _ { 0 } ( \lambda )$ on the spectrum of A and using Exercise 1, it is easily seen that

$$
p _ { 1 } ^ { ( j ) } ( \lambda _ { k } ) - p _ { 2 } ^ { ( j ) } ( \lambda _ { k } ) = p _ { 0 } ^ { ( j ) } ( \lambda _ { k } ) = 0\tag{3}
$$

for $j = 0 , 1 , \ldots , m _ { k } - 1 , 1 \leq k \leq s$ Thus, the two polynomials $p _ { 1 } ( \lambda )$ and $p _ { 2 } ( \lambda )$ have the same values on the spectrum of A provided $p _ { 1 } ( A ) = p _ { 2 } ( A )$

Conversely, if (3) holds, then $p _ { 0 } ( \lambda )$ has a zero of multiplicity $m _ { k }$ at the point $\dot { \iota } _ { \ast k }$ for each $k = 1 , 2 , \ldots , s .$ Hence $p _ { 0 } ( \lambda )$ must be divisible by $m ( \lambda )$ in (1) and it follows that $p _ { 0 } ( A ) = 0$ (see Corollary 1 of Theorem 6.2.2) or, equivalently, $p _ { 1 } ( A ) = p _ { 2 } ( A )$

It is this property of polynomials with matrix arguments that we now use to extend the definition of $f ( A )$ to more general functions $f ( \lambda )$ . Thus, we shall demand that all functions that are defined on the spectrum of A and that take on the same values there should yield the same matrix $f ( A )$ . In particular, for any $f ( \lambda )$ defined on the spectrum of A we shall be able to write $f ( A ) =$ $p ( A )$ , where $p ( \lambda )$ is a polynomial with the same values on the spectrum of A. The existence of such a polynomial $p ( \lambda )$ with the prescribed properties follows from the solution of the problem of general Hermite interpolation, which we must now consider.

## 9.2 Interpolatory Polynomials

Proposition 1. Given distinct numbers $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ , positive integers $m _ { 1 }$ $m _ { 2 } , \ldots , m _ { s }$ with $\begin{array} { r } { m = \sum _ { k = 1 } ^ { s } m _ { k } } \end{array}$ , and a set of numbers

$$
f _ { k , 0 } , \quad f _ { k , 1 } , \ldots , \quad f _ { k , m _ { k } - 1 } , \qquad k = 1 , 2 , \ldots , s ,
$$

there exists a polynomial $p ( \lambda )$ of degree less than m such that

$$
p ( \lambda _ { k } ) = f _ { k , 0 } , \qquad p ^ { ( 1 ) } ( \lambda _ { k } ) = f _ { k , 1 } , \ldots , \qquad p ^ { ( m _ { k } - 1 ) } ( \lambda _ { k } ) = f _ { k , m _ { k } - 1 }\tag{1}
$$

for $k = 1 , 2 , \ldots , s .$

ProOF. It is easily seen that the polynomial $p _ { k } ( \lambda ) = \alpha _ { k } ( \lambda ) \psi _ { k } ( \lambda ) , ^ { \dagger }$ where $1 \leq k \leq s$ and

$$
\alpha _ { k } ( \lambda ) = \alpha _ { k , 0 } + \alpha _ { k , \scriptscriptstyle 1 } ( \lambda - \lambda _ { k } ) + \cdot \cdot \cdot + \alpha _ { k , m _ { k } - \scriptscriptstyle 1 } ( \lambda - \lambda _ { k } ) ^ { m _ { k } - 1 } ,
$$

$$
\psi _ { k } ( \lambda ) = \prod _ { j = 1 , j \neq k } ^ { s } ( \lambda - \lambda _ { j } ) ^ { m _ { j } } ,
$$

has degree less than m and satisfies the conditions

$$
p _ { k } ( \lambda _ { i } ) = p _ { k } ^ { ( 1 ) } ( \lambda _ { i } ) = \cdot \cdot \cdot = p _ { k } ^ { ( m _ { i } - 1 ) } ( \lambda _ { i } ) = 0
$$

for $i \neq k$ and arbitrary $\alpha _ { k , 0 } , \alpha _ { k , 1 } , \ldots \alpha _ { k , m _ { k } - 1 }$ . Hence the polynomial

$$
p ( \lambda ) = p _ { 1 } ( \lambda ) + p _ { 2 } ( \lambda ) + \cdot \cdot \cdot + p _ { s } ( \lambda )\tag{2}
$$

satisfies conditions (1) if and only if

$$
p _ { k } ( \lambda _ { k } ) = f _ { k , 0 } , \qquad p _ { k } ^ { ( 1 ) } ( \lambda _ { k } ) = f _ { k , 1 } , \ldots , \qquad p _ { k } ^ { ( m _ { k } - 1 ) } ( \lambda _ { k } ) = f _ { k , m _ { k } - 1 }\tag{3}
$$

for each $1 \leq k \leq s .$ By differentiation,

$$
p _ { k } ^ { ( j ) } ( \lambda _ { k } ) = \sum _ { i = 0 } ^ { j } \binom { j } { i } \alpha _ { k } ^ { ( i ) } ( \lambda _ { k } ) \psi _ { k } ^ { ( j - i ) } ( \lambda _ { k } )
$$

for $1 \leq k \leq s , 0 \leq j \leq m _ { k } - 1$ . Using Eqs. (3) and recalling the definition of $\alpha _ { k } ( \lambda )$ , we have for $k = 1 , 2 , . . . , s , j = 0 , 1 , . . . , m _ { k } - 1$

$$
f _ { k , j } = \sum _ { i = 0 } ^ { j } { \binom { j } { i } } i ! \alpha _ { k , i } \psi _ { k } ^ { ( j - i ) } ( \lambda _ { k } ) .\tag{4}
$$

Since $\psi _ { k } ( \lambda _ { k } ) \neq 0$ for each fixed k, Eqs. (4) can now be solved successively (beginning with $j = 0 )$ to find the coefficients $\alpha _ { k , 0 } , \ldots , \alpha _ { k , m _ { k } - 1 }$ for which (3) holds. Thus, a polynomial $p ( \lambda )$ of the form given in (2) satisfies the required conditions.

Proposition 2. The polynomial p(λ) of Proposition 1 is unique.

The unique polynomial of degree less than m that satisfies conditions (1) is known as the Hermite interpolating polynomial.

This is an important step in our argument but the proof is cumbersome and is therefore omitted. It can be made to depend on the nonsingularity of a generalized Vandermonde matrix (see Exercise 2.11.22).

Exercise 1. If $m _ { 1 } = m _ { 2 } = \cdot \cdot \cdot = m _ { s } = 1$ , then conditions (1) reduce to the simple “point wise" conditions of interpolation : $p ( \lambda _ { k } ) = f _ { k , 0 } \mathrm { f o r } k = 1 , 2 , . . . , s .$ Show that these conditions are satisfied by the Lagrange interpolating polynomial:

$$
p ( \lambda ) = \sum _ { k = 1 } ^ { s } f _ { k , 0 } { \frac { ( \lambda - \lambda _ { 1 } ) \cdot \cdot \cdot ( \lambda - \lambda _ { k - 1 } ) ( \lambda - \lambda _ { k + 1 } ) \cdot \cdot \cdot ( \lambda - \lambda _ { s } ) } { ( \lambda _ { k } - \lambda _ { 1 } ) \cdot \cdot \cdot ( \lambda _ { k } - \lambda _ { k - 1 } ) ( \lambda _ { k } - \lambda _ { k + 1 } ) \cdot \cdot \cdot ( \lambda _ { k } - \lambda _ { s } ) } } .\tag{5}
$$

Exercise 2. Prove the result of Proposition 2 in the case described in Exercise 1, that is, when $m _ { 1 } = m _ { 2 } = \cdot \cdot \cdot = m _ { s } = 1$

Hint. First show that a polynomial of degree less than m that vanishes at m distinct points is necessarily the zero polynomial. This can be done using the nonsingularity of a certain Vandermonde matrix (see Exercise 2.3.6). □

A useful role is played by those polynomials for which numbers $f _ { k , i }$ in (1) are all zero except one, and the nonzero number, say $f _ { k , j }$ is equal to 1. Thus Propositions 1 and 2 guarantee the existence of a unique polynomial $\varphi _ { k j } ( \lambda )$ of degree less than m (with $1 \leq k \leq s$ and $0 \le j \le m _ { k } - 1 )$ such that

$$
\varphi _ { k j } ^ { ( r ) } ( \lambda _ { k } ) = \delta _ { j r } , \qquad r = 0 , 1 , \ldots , m _ { k } - 1 ;\tag{6}
$$

and when $i \neq k ,$

$$
\varphi _ { k j } ^ { ( r ) } ( \lambda _ { i } ) = 0 , \qquad r = 0 , 1 , \ldots , m _ { i } - 1 .\tag{7}
$$

These m polynomials are called the fundamental or cardinal polynomials of the interpolation problem.

Once these polynomials are known, the solution to every problem with the general conditions (1) can be expressed as a linear combination of them. $\mathbf { F o r } _ { \mathbf { \alpha } }$ if $p ( \lambda )$ satisfies (1) then, as is easily verified,

$$
p ( \boldsymbol { \lambda } ) = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } f _ { k , j } \varphi _ { k j } ( \boldsymbol { \lambda } ) .\tag{8}
$$

Exercise 3. Verify that the m polynomials $\varphi _ { k j } ( \lambda ) \left( 1 \leq k \leq s \right.$ and $0 \leq j \leq$ $m _ { k } \mathrm { ~ - ~ } 1 )$ just defined are linearly independent and hence form a basis for the space $\mathcal { P } _ { m - 1 }$ of all polynomials of degree less than $m .$

Exercise 4. Show that, with the hypothesis of Exercise 1, the fundamental interpolatory polynomials are given by

$$
\varphi _ { k 0 } ( \lambda ) \equiv \varphi _ { k } ( \lambda ) = \prod _ { j = 1 , j \ne k } ^ { s } ( \lambda - \lambda _ { j } ) \Biggl \langle \prod _ { j = 1 , j \ne k } ^ { s } ( \lambda _ { k } - \lambda _ { j } )
$$

for $k = 1 , 2 , \ldots , s .$ □

## 9.3 Definition of a Function of a Matrix

Using the concepts and results of the two preceding sections, a general definition of the matrix $f ( A )$ in terms of matrix A and the function f can be made, provided $f ( \lambda )$ is defined on the spectrum of A. If $p ( \lambda )$ is any polynomial that assumes the same values as $f ( \lambda )$ on the spectrum of A, we simply define $f ( A ) \triangleq p ( A )$ . Proposition 9.2.1 assures us that such a polynomial exists, while Proposition 9.1.1 shows that, for the purpose of the formal definition, the choice of $p ( \lambda )$ is not important. Moreover, Eq. (9.2.8) indicates how $p ( \lambda )$ might be chosen with the least possible degree.

Exercise 1. If A is a simple matrix with distinct eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { s }$ and $f ( \lambda )$ is any function that is well defined at the eigenvalues of A, show that

$$
f ( A ) = \sum _ { k = 1 } ^ { s } f ( \lambda _ { k } ) \Biggl [ \prod _ { j = 1 , j \neq k } ^ { s } ( A - \lambda _ { j } / I ) \Biggl / \prod _ { j = 1 , j \neq k } ^ { s } ( \lambda _ { k } - \lambda _ { j } ) \Biggr ] .
$$

Exercise 2. Calculate $f ( A )$ , where $f ( \lambda ) = e ^ { 2 \lambda }$ and

$$
A = { \binom { 7 6 } { 3 } } \quad { \overset { - 1 } { 2 } } { \overset { 1 } { \mathrm { J } } } .
$$

SoLUTION. The eigenvalues of A are found to be $\lambda _ { 1 } = 3 , \lambda _ { 2 } = 5 ,$ so that the minimal polynomial $m ( \lambda )$ of A is $( \lambda - 3 ) ( \lambda - 5 )$ . The Lagrange interpolatory polynomial is

$$
\begin{array} { c } { { p ( \lambda ) = f ( \lambda _ { 1 } ) \displaystyle \frac { \lambda - \lambda _ { 2 } } { \lambda _ { 1 } - \lambda _ { 2 } } + f ( \lambda _ { 2 } ) \displaystyle \frac { \lambda - \lambda _ { 1 } } { \lambda _ { 2 } - \lambda _ { 1 } } } } \\ { { = - \frac { 1 } { 2 } e ^ { 6 } ( \lambda - 5 ) + \frac { 1 } { 2 } e ^ { 1 0 } ( \lambda - 3 ) . } } \end{array}
$$

Hence, by definition,

$$
{ \begin{array} { r l } & { e ^ { 2 A } = - { \frac { 1 } { 2 } } e ^ { 6 } ( A - 5 I ) + { \frac { 1 } { 2 } } e ^ { 1 0 } ( A - 3 I ) } \\ & { } \\ & { = { \frac { 1 } { 2 } } { \left[ \begin{array} { l l l } { 3 e ^ { 1 0 } - e ^ { 6 } } & { - e ^ { 1 0 } + e ^ { 6 } } \\ { 3 e ^ { 1 0 } - 3 e ^ { 6 } } & { - e ^ { 1 0 } + 3 e ^ { 6 } } \end{array} \right] } . } \end{array} }
$$

Exercise 3. If

$$
A = { \frac { \pi } { 2 } } { \left[ \begin{array} { l l l } { 2 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } ,
$$

prove that

$$
\sin { A } = { \frac { 4 } { \pi } } { \cal A } - { \frac { 4 } { \pi ^ { 2 } } } { \cal A } ^ { 2 } = { \Bigg [ } 0 { \pmod { 0 } } { \Bigg ] } .
$$

Exercise 4. If $f ( \lambda )$ and $g ( \lambda )$ are defined on the spectrum of A and $h ( \lambda )$ $= \alpha f ( \lambda ) + \beta g ( \lambda )$ , where $\alpha , \beta \in \mathbb { C } ,$ and $k ( \lambda ) = f ( \lambda ) g ( \lambda )$ , show that $h ( \lambda )$ and $k ( \lambda )$ are defined on the spectrum of A, and

$$
\begin{array} { l } { { h ( A ) = \alpha f ( A ) + \beta g ( A ) , } } \\ { { k ( A ) = f ( A ) g ( A ) = g ( A ) f ( A ) . } } \end{array}
$$

Exercise 5. If $f _ { 1 } ( \lambda ) = \lambda ^ { - 1 }$ and det $A \neq 0 ,$ , show that $f _ { 1 } ( A ) = A ^ { - 1 }$ . Show also that if $f _ { 2 } ( \lambda ) = ( \stackrel { . } { a } - \lambda ) ^ { - 1 }$ and $a \not \in \sigma ( A )$ , then $f _ { 2 } ( A ) = ( a I - A ) ^ { - 1 }$

Hint: For the first part observe that if $p ( \lambda )$ is an interpolatory polynomial for $f _ { 1 } ( \lambda )$ , then the values of $\lambda p ( \lambda )$ and $\lambda f _ { 1 } ( \lambda ) = 1$ coincide on the spectrum of A and hence $A p ( A ) = A f _ { 1 } ( A ) = I$

Exercise 6. Use the ideas of this section to determine a positive definite square root for a positive definite matrix (see Theorem 5.4.1). Observe that there are, in general, many square roots.

We conclude this section with the important observation that if $f ( \lambda )$ is a polynomial, then the matrix $f ( A )$ determined by the definition of Section 1.7 coincides with that obtained from the more general definition introduced in this section.

## 9.4 Properties of Functions of Matrices

In this section we obtain some important properties of $f ( A )$ , which, in particular, allow us to compute $f ( A )$ very easily, provided the Jordan decomposition of A is known. These properties will also establish important relationships between Jordan forms for A and $f ( A )$

Theorem 1. If $A \in C ^ { n \times n }$ is a block-diagonal matrix,

$$
A = \mathrm { d i a g } [ A _ { 1 } , A _ { 2 } , . . . , A _ { t } ] ,
$$

and the function $f ( \lambda )$ is defined on the spectrum of A, then

$$
f ( A ) = \mathrm { d i a g } [ f ( A _ { 1 } ) , f ( A _ { 2 } ) , \ldots , f ( A _ { t } ) ] .\tag{1}
$$

PRooF. First, it is clear that for any polynomial q(λ),

$$
q ( A ) = \mathrm { d i a g } [ q ( A _ { 1 } ) , q ( A _ { 2 } ) , \ldots , q ( A _ { t } ) ] .
$$

Hence, if $p ( \lambda )$ is the interpolatory polynomial for $f ( \lambda )$ on the spectrum of A, we have

$$
f ( A ) = p ( A ) = \operatorname { d i a g } [ p ( A _ { 1 } ) , p ( A _ { 2 } ) , \ldots , p ( A _ { t } ) ] .
$$

Second, since the spectrum of $A _ { j } \ ( 1 \leq j \leq t )$ is obviously a subset of the spectrum of $A ,$ the function $f ( \lambda )$ is defined on the spectrum of $A _ { j }$ for each $j = 1 , 2 , \dots , t .$ (Note also that the index of an eigenvalue of $A _ { j }$ cannot exceed the index of the same eigenvalue of $A . )$ Furthermore, since $f ( \lambda )$ and $p ( \lambda )$ assume the same values on the spectrum of $A ,$ they must also have the same values on the spectrum of $A _ { j } \ ( j = 1 , 2 , \ldots , t )$ . Hence $f ( A _ { j } ) = p ( A _ { j } )$ and we obtain Eq. (1).

The next result provides a relation between $f ( A )$ and $f ( B )$ when A and B are similar matrices.

Theorem 2. If $A , B , P \in \mathbb { C } ^ { n \times n }$ , where $B = P A P ^ { - 1 }$ , and $f ( \lambda )$ is dened on the spectrum of A, then

$$
f ( B ) = P f ( A ) P ^ { - 1 } .\tag{2}
$$

ProoF. Since A and B are similar, they have the same minimal polynomial (Section 6.2). Thus, if $p ( \lambda )$ is the interpolatory polynomial for $f ( \lambda )$ on the spectrum of A, then it is also the interpolatory polynomial for f(λ) on the spectrum of B. Thus we have $f ( A ) = p ( A ) , f ( B ) = p ( B ) , p ( B ) = P p ( A ) P ^ { - 1 }$ and so the relation (2) follows.

In view of the Jordan theorem, Theorems 1 and 2 imply a related theorem about functions of matrices.

Theorem 3. Let $A \in \mathbb { C } ^ { n \times n }$ and let $J = \mathrm { d i a g } [ J _ { j } ] _ { j = 1 } ^ { t }$ be the Jordan canonical form of A, where $A = P J P ^ { - 1 }$ and $J _ { j }$ is the jth Jordan block of J. Then

$$
f ( A ) = P \mathrm { d i a g } [ f ( J _ { 1 } ) , f ( J _ { 2 } ) , \ldots , f ( J _ { t } ) ] P ^ { - 1 } .\tag{3}
$$

The last step in computing $f ( A )$ by use of the Jordan form of A consists, therefore, of the following formula.

Theorem 4. Let $J _ { 0 }$ be a Jordan block of size l associated with $\lambda _ { 0 }$

$$
J _ { 0 } = \left[ \begin{array} { c c c c c } { { \lambda _ { 0 } } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { \lambda _ { 0 } } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { } } & { { \lambda _ { 0 } } } \end{array} \right] .
$$

$H f ( \lambda )$ is an $( l - 1 )$ -times differentiable function in a neighborhood of $\lambda _ { 0 }$ then

$$
f ( J _ { 0 } ) = \left[ \begin{array} { c c c c } { { f ( \lambda _ { 0 } ) } } & { { \displaystyle { \frac { 1 } { 1 ! } } f ^ { \prime } ( \lambda _ { 0 } ) } } & { { \cdots } } & { { \displaystyle { \frac { 1 } { ( l - 1 ) ! } } f ^ { ( l - 1 ) } ( \lambda _ { 0 } ) } } \\ { { 0 } } & { { f ( \lambda _ { 0 } ) } } & { { \ddots } } & { { \vdots } } \\ { { \vdots } } & { { \ddots } } & { { \ddots } } & { { \displaystyle { \frac { 1 } { 1 ! } } f ^ { \prime } ( \lambda _ { 0 } ) } } \\ { { 0 } } & { { \cdots } } & { { 0 } } & { { f ( \lambda _ { 0 } ) } } \end{array} \right] .\tag{4}
$$

PRoOF. The minimal polynomial of $J _ { 0 }$ is $( \lambda - \lambda _ { 0 } ) ^ { l }$ (see Exercise 7.7.4) and the values of $f ( \lambda )$ on the spectrum of $J _ { 0 }$ are therefore $f ( \lambda _ { 0 } ) , f ^ { \prime } ( \lambda _ { 0 } ) , \dots , f ^ { ( l - 1 ) } ( \lambda _ { 0 } )$ The interpolatory polynomial p(λ), defined by the values of $p ( \lambda )$ $f ( \lambda )$ on the spectrum $\{ \lambda _ { 0 } \}$ of $J _ { 0 }$ , is found by putting $s = 1 , m _ { k } = l , \lambda _ { 1 } = \lambda _ { 0 }$ , and $\psi _ { 1 } ( \lambda ) \equiv 1$ in Eqs. (9.2.2) through (9.2.4). One obtains

$$
p ( \lambda ) = \sum _ { i = 0 } ^ { l - 1 } \frac { 1 } { i ! } f ^ { ( i ) } ( \lambda _ { 0 } ) ( \lambda - \lambda _ { 0 } ) ^ { i } .
$$

The fact that the polynomial $p ( \lambda )$ solves the interpolation problem $p ^ { ( j ) } ( \lambda _ { 0 } )$ $= f ^ { ( j ) } ( \lambda _ { 0 } ) , 1 \le j \le l - 1$ , can also be easily checked by a straightforward calculation.

We then have $f ( J _ { 0 } ) = p ( J _ { 0 } )$ and hence

$$
f ( J _ { 0 } ) = \sum _ { i = 0 } ^ { l - 1 } { \frac { 1 } { i ! } } f ^ { ( i ) } ( \lambda _ { 0 } ) ( J _ { 0 } - \lambda _ { 0 } I ) ^ { i } .
$$

Computing the powers of $J _ { 0 } - \lambda _ { 0 } I _ { : }$ , we obtain

$$
\left( J _ { 0 } - \dot { x } _ { 0 } I \right) ^ { i } = \left[ \begin{array} { c c c } { { 0 } } & { { 1 } } & { { } } \\ { { } } & { { } } & { { } } \\ { { } } & { { 0 } } & { { \ddots } } \\ { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { 0 } } \end{array} \right] ^ { i } = \left[ \begin{array} { c c c c c } { { \dot { i } } } & { { } } & { { } } & { { } } & { { 0 } } & { { \cdots } } & { { 0 \dot { } } } \\ { { } } & { { \cdots } } & { { 0 } } & { { 1 } } & { { 0 } } & { { \cdots } } & { { \dot { \zeta } } } \\ { { } } & { { } } & { { } } & { { \ddots } } & { { \vdots \dot { } } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { 0 } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { 0 } } \\ { { } } & { { } } & { { } } & { { } } & { { \vdots \dot { } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } \end{array} \right]
$$

and Eq. (4) follows.

Thus, given a Jordan decomposition of the matrix A, the matrix $f ( A )$ is easily found by combining Theorems 3 and 4.

Theorem 5. With the notation of Theorem 3,

$$
f ( A ) = P \mathrm { d i a g } [ f ( J _ { 1 } ) , f ( J _ { 2 } ) , \ldots , f ( J _ { t } ) ] P ^ { - 1 } ,
$$

where $f ( J _ { i } ) \ ( i = 1 . 2 . \ldots , t )$ are upper-triangular matrices of the form given in Eq. (4).

Exercise 1. Verify (using the real natural logarithm) that

$$
\ln ( { [ \begin{array} { l l l } { 6 } & { 2 } & { 2 } \\ { - 2 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 2 } \end{array} ] } ) = [ { \begin{array} { r r r } { 0 } & { 2 } & { 1 } \\ { - 1 } & { - 2 } & { 0 } \\ { 1 } & { 0 } & { 0 } \end{array} } { [ \begin{array} { l l l } { \ln 2 } & { 0 } & { 0 } \\ { 0 } & { \ln 4 } & { { \frac { 1 } { 4 } } } \\ { 0 } & { 0 } & { \ln 4 } \end{array} ] } [ { \begin{array} { r r r } { 0 } & { 2 } & { 1 } \\ { - 1 } & { - 2 } & { 0 } \\ { 1 } & { 0 } & { 0 } \end{array} } ] ^ { - 1 }
$$

Hint. Use Example 6.5.2. □

We observe that if J, is associated with the eigenvalue λ, then the diagonal $J _ { i }$ $\lambda _ { i }$ elements of $f ( J _ { i } )$ are all equal to $f ( \lambda _ { i } )$ , and since the eigenvalues of a triangular matrix are just its diagonal elements, it follows that the eigenvalues of $f ( A )$ possibly multiple. are $f ( \lambda _ { 1 } ) , f ( \lambda _ { 2 } ) , \ldots , f ( \lambda _ { s } )$ . Compare the next result with Theorem 4.11.3.

Theorem 6. If $i _ { 1 } , i _ { 2 } , \ldots , i _ { n }$ are the eigenvalues of the matrix $A \in \mathbb { C } ^ { n \times 1 }$ a and $f ( \lambda )$ is defined on the spectrum of $A ,$ then the eigenvalues of $f ( A )$ are $f ( \lambda _ { 1 } ) , f ( \lambda _ { 2 } ) , \ldots , f ( \lambda _ { n } )$

Exercise 2. Check that $e ^ { A }$ is nonsingular for any $A \in \mathbb { C } ^ { n \times n }$

Exercise 3. Show that, if all the eigenvalues of the matrix $A \in \mathbb { C } ^ { n \times n }$ lie in the open unit disk, then $A + I$ is nonsingular.

Exercise 4. If the eigenvalues of $A \in \mathbb { C } ^ { n \times n }$ lie in the open unit disk, show that Re $\lambda < 0$ for any $\lambda \in \sigma ( C )$ , where $C = ( A + I ) ^ { - 1 } ( A - I )$ □

The elementary divisors associated with a particular eigenvalue are not necessarily preserved under the transformation determined by $f ( \lambda )$ , in that an elementary divisor $( \lambda - \lambda _ { i } ) ^ { r }$ of $\lambda I - A$ is not necessarily carried over to an elementary divisor $( \lambda - f ( \lambda _ { i } ) ) ^ { r }$ for $\lambda I - f ( A )$ . Exercise 9.3.3 illustrates this fact by showing that the nonlinear elementary divisor associated with the eigenvalue $\pi / 2$ of A splits into two linear elementary divisors of the eigenvalue $f ( \pi / 2 ) = 1$ of $f ( A )$ . A description of the elementary divisors of $\lambda I - f ( A )$ in terms of those of $\lambda I - A$ is given in the following theorem.

Theorem 7. Let $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ be the distinct eigenvalues of $A \in \mathbb { C } ^ { n \times n }$ , and let the function $f ( \lambda )$ be deined on the spectrum of A.

(a) $I f f ^ { \prime } ( \lambda _ { k } ) \ne 0 .$ , the elementary divisors of $\lambda I - f ( A )$ associated with the eigenvalue $f ( \lambda _ { k } )$ are obtained by replacing each elementary divisor $( 1 - \lambda _ { k } ) ^ { r }$ $o f \lambda I - A$ associated with $\lambda _ { k } b y ( \lambda - f ( \lambda _ { k } ) ) ^ { r }$

(b) $I f f ^ { \prime } ( \lambda _ { k } ) = f ^ { \prime \prime } ( \lambda _ { k } ) = \cdot \cdot \cdot = f ^ { ( l - 1 ) } ( \lambda _ { k } ) = 0 ,$ but $f ^ { ( l ) } ( \lambda _ { k } ) \neq 0 .$ where $l \geq r ,$ then an elementary divisor $( \lambda - \lambda _ { k } ) ^ { r }$ of λI — A splits into r linear elementary divisors of $\lambda I - f ( A )$ of the form $\lambda - f ( \lambda _ { k } )$

(c) $I f f ^ { \prime } ( \lambda _ { k } ) = f ^ { \prime \prime } ( \lambda _ { k } ) = \cdots = f ^ { ( l - 1 ) } ( \lambda _ { k } ) = 0$ but $f ^ { ( l ) } ( \lambda _ { k } ) \neq 0$ , where $2 \leq l$ $\leq r - 1 .$ , the elementary divisors of $\lambda I - f ( A )$ associated with $f ( \lambda _ { k } )$ are obtained by replacing each elementary divisor $( \lambda - \lambda _ { k } ) ^ { r }$ of $\lambda I - A$ associated with $\lambda _ { k } b y$ l elementary divisors $( \lambda - \lambda _ { k } ) ^ { p }$ (taken $l - q t i m e s )$ and $( \lambda - \lambda _ { k } ) ^ { p + 1 }$ (taken q times), where the integers p and q satisfy the condition $r = l p + q$ $( 0 \leq q \leq l - 1 , p > 0 )$

Note that the cases (a) and (b) can be viewed as extreme cases of (c)

ProoF. In view of Theorems 5 and 7.7.1, since each elementary divisor $( \lambda - \lambda _ { k } ) ^ { r }$ of $\lambda I - A$ generates a Jordan block $J _ { k }$ of size r associated with $\lambda _ { k }$ , it suffices to determine the elementary divisors of $\lambda I - f ( J _ { k } )$

If $f ^ { \prime } ( \lambda _ { k } ) \neq 0$ in Eq. (4), then by Exercise 7.7.7 the unique elementary divisor of $f ( J _ { k } ) \operatorname { i s } { ( \lambda - f ( \lambda _ { k } ) ) ^ { r } }$ , which proves part (a). Part (b) is checked by observing that $f ( J _ { k } )$ is in this case a diagonal matrix and applying Exercise 7.7.6. The result of Exercise 7.7.8 readily implies the required statement in (c).

Exercise 5. If B is positive definite, show that there is a unique Hermitian matrix H such that $B = e ^ { H } .$ (This matrix is, of course, a natural choice for ln B.) Give an example of a non-Hermitian matrix A such that $e ^ { A }$ is positive definite.□

## 9.5 Spectral Resolution of f(A)

The following decomposition, or spectral resolution, of $f ( A )$ is important and is obviously closely related to the spectral theorem for simple matrices, which we have already discussed in Theorem 4.10.3 and Exercise 4.14.3. It gives a useful explicit representation of $f ( A )$ in terms of fundamental properties of A.

Theorem 1. If $A \in \mathbb { C } ^ { n \times n } , \ f ( \lambda )$ is defined on the spectrum $\{ \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s } \}$ $o f A , f _ { k , j }$ is the value of the jth derivative of $f ( \lambda )$ at the eigenvalue $\lambda _ { k } \left( k = 1 , 2 , \right.$ $\dots , s , j = 0 , 1 , \dots , m _ { k } - 1 )$ , and $m _ { k }$ is the index of $\lambda _ { k }$ , then there exist matrices $Z _ { k j }$ independent of f(λ) such that

$$
f ( A ) = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } f _ { k , j } Z _ { k j } .\tag{1}
$$

Moreover, the matrices $Z _ { k j }$ are linearly independent members of $\mathbb { C } ^ { n \times n }$ and commute with A and with each other.

PROOF. Recall that the function $f ( \lambda )$ and the polynomial $p ( \lambda )$ defined by Eq. (9.2.8) take the same values on the spectrum of A. Hence $f ( A ) = p ( A )$ and Eq. (1) is obtained on putting $Z _ { k j } = \varphi _ { k j } ( A )$ . It also follows immediately that A and all of the $Z _ { k j }$ are mutually commutative.

It remains only to prove that these matrices are linearly independent. Suppose that

$$
\sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } c _ { k j } Z _ { k j } = O
$$

and define $\begin{array} { r } { h ( \lambda ) = \sum _ { k , j } c _ { k j } \varphi _ { k j } ( \lambda ) } \end{array}$ ; then $h ( \lambda )$ is a polynomial of the space $\mathcal { P } _ { m - 1 }$ ; that is, the degree of $h ( \lambda )$ does not exceed $m - 1$ . Then $Z _ { k j } = \varphi _ { k j } ( A )$ implies that $h ( A ) = 0$ But m is the degree of the minimal polynomial of A and, since h annihilates A, it follows from Theorem 6.2.1 that h is the zero polynomial. Hence, since the $\varphi _ { k j } \mathbf { \bar { s } }$ are independent by Exercise 9.2.3, we have $c _ { k j } = 0$ for each k and $j .$ Thus, the matrices $Z _ { k j }$ are linearly independent.

We shall call the matrices $Z _ { k j }$ the components of $A ;$ note that, because they are linearly independent, none of them can be a zero-matrix.

Let us investigate the case of simple matrices more closely. We now have $m _ { 1 } = m _ { 2 } = \cdot \cdot \cdot = m _ { s } = 1$ in (1) and so, for a simple matrix A,

$$
f ( A ) = \sum _ { k = 1 } ^ { s } f _ { k } Z _ { k 0 } , \qquad f _ { k } = f _ { k , 0 } , ~ k = 1 , 2 , \ldots , s .
$$

Recall that, by definition, $Z _ { k 0 } = \varphi _ { k 0 } ( A )$ . If we apply the result of Exercise 4.14.3 to the polynomials $\varphi _ { k 0 } ( \lambda ) , k = 1 , 2 , \ldots , s ,$ we see that $Z _ { k 0 }$ is the sum of the constituent matrices associated with the eigenvalue $\lambda _ { k }$ . It is then easily seen that $Z _ { k 0 }$ is idempotent, and the range of $Z _ { k 0 }$ is the (right) eigenspace associated with $\lambda _ { k }$ (that is, the kernel of $\lambda _ { k } I - A )$ . Thus, the result of Exercise 4.14.3 is seen to be a special case of Theorem 1. We deduce from it that for a simple matrix A

$$
\sum _ { k = 1 } ^ { s } Z _ { k 0 } = I { \qquad \mathrm { a n d } \qquad } Z _ { k 0 } Z _ { j 0 } = \delta _ { k j } Z _ { k 0 } ,
$$

although the first of these results is easily seen to be true for all matrices $A \in \mathbb { C } ^ { n \times n }$ (see Exercise 1). We shall show in Theorem 2 that the second result is also generally true.

Finally, we note that, in view of Exercise 9.2.4,

$$
Z _ { k 0 } = \varphi _ { k 0 } ( A ) = \prod _ { j = 1 , j \neq k } ^ { s } ( A - \lambda _ { j } I ) \Bigg / \prod _ { j = 1 , j \neq k } ^ { s } ( \lambda _ { k } - \lambda _ { j } ) .
$$

Exercise 1. If $A \in \mathbb { C } ^ { n \times n }$ prove that, in the previous notation,

$$
( \mathfrak { a } ) \ I = \sum _ { k = 1 } ^ { s } Z _ { k 0 } \qquad \mathrm { a n d } \qquad ( \mathfrak { b } ) \ A = \sum _ { k = 1 } ^ { s } ( \lambda _ { k } Z _ { k 0 } + Z _ { k 1 } ) .
$$

Hint. Put $f ( \lambda ) = 1$ in Eq. (1) for part (a) and $f ( \lambda ) = \lambda$ for part (b).

Exercise 2. If $A \in \mathbb { C } ^ { n \times n }$ and $\lambda \not \in \sigma ( A )$ , show that

$$
R _ { \lambda } ( { \cal A } ) \triangleq ( \lambda I - { \cal A } ) ^ { - 1 } = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } \frac { j ! } { ( \lambda - \lambda _ { k } ) ^ { j + 1 } } Z _ { k j } .
$$

Hint. Use Exercise 9.3.5.

Let us examine more closely the properties of the components of a general matrix $\ b { A } \in \mathbb { C } ^ { n \times n }$ . Note particularly that part (c) of the next theorem shows that the components $Z _ { 1 0 } , \ldots , Z _ { s 0 }$ of any matrix are projectors and, by part (a), their sum is the identity. A formula like that in part (a) is sometimes known as a resolution of the identity.

Theorem 2. The components $Z _ { k j } \ ( j = 0 , 1 , . . . , m _ { k } - 1 ; k = 1 , 2 , . . . , s )$ of the matrix $A \in \mathbb { C } ^ { n \times n }$ satisfy the conditions

(a) $\sum _ { k = 1 } ^ { s } Z _ { k 0 } = I ;$

(b) $Z _ { k p } Z _ { l } =  { \left. \begin{array} { l } {  { \left( \boldsymbol { \imath } \right. \kern - delimiterspace } k \ne l } \right. } \end{array}$

(c) $Z _ { k j } ^ { 2 } = Z _ { k j }$ if and only if j = 0;

(d) $Z _ { k 0 } Z _ { k r } = Z _ { k r } , r = 0 , 1 , \ldots , m _ { k } - 1 .$

PRooF. The relation (a) was established in Exercise 1. However, this and the other properties readily follow from the structure of the components $Z _ { k j }$ which we discuss next

First observe that if $A = P J P ^ { - 1 }$ , where $\boldsymbol { J } = \operatorname { d i a g } [ J _ { 1 } , J _ { 2 } , \dots , J _ { t } ]$ is a Jordan form for A, then, by Theorem 9.4.5,

$$
Z _ { k j } = \varphi _ { k j } ( A ) = { \cal P } \mathrm { d i a g } [ \varphi _ { k j } ( J _ { 1 } ) , \dots , \varphi _ { k j } ( J _ { t } ) ] { \cal P } ^ { - 1 } ,\tag{2}
$$

where $\varphi _ { k j } ( J _ { i } ) ( 1 \leq i \leq t , 1 \leq k \leq s , 0 \leq j \leq m _ { k } - 1 )$ is a matrix of the form (9.4.4). The structure of $\varphi _ { k j } ( J _ { i } )$ is now studied by considering two possibilities.

Case 1. The Jordan block $J _ { i }$ (of size $n _ { i } )$ is associated with the eigenvalue $\lambda _ { k }$ . Since (see Eq. (9.2.6)) $\varphi _ { k j } ^ { ( r ) } ( \lambda _ { k } ) = \delta _ { j r } ~ ( r , j = 0 , 1 , \ldots , m _ { k } - 1 )$ , it follows from Eq. (9.4.4) that

$$
\varphi _ { k j } ( J _ { i } ) = \frac { 1 } { j ! } N _ { n _ { i } } ^ { j } ,\tag{3}
$$

where $N _ { n _ { i } }$ is the $n _ { i } \times n _ { i }$ Jordan block associated with the zero eigenvalue, and it is assumed that for $j = 0$ the expression on the right in Eq. (3) is the $n _ { i } \times n _ { i }$ identity matrix. Note also that $n _ { i } \le m _ { k }$ (see Exercises 7.7.4 and 7.7.9).

Case 2. The Jordan block $J _ { i }$ (of order $n _ { i } )$ is associated with an eigenvalue $\lambda _ { 1 } \neq \lambda _ { k }$ . Then again $n _ { i } \le m _ { l }$ and [as in Eq. (9.2.7)] we observe that $\varphi _ { k j } ( \lambda )$ along with its first $m _ { l } - 1$ derivatives, is zero at $\lambda = \lambda _ { l }$ . Using (9.4.4) again, we see that

$$
\varphi _ { k j } ( J _ { i } ) = 0 .\tag{4}
$$

To simplify the notation, consider the case $k = 1$ . Substituting Eqs. (3) and (4) into (2) it is easily seen that

$$
Z _ { 1 j } = \frac { 1 } { j ! } P \mathrm { d i a g } [ N _ { n _ { 1 } } ^ { j } , N _ { n _ { 2 } } ^ { j } , . . . , N _ { n _ { q } } ^ { j } , 0 , . . . , 0 ] P ^ { - 1 }\tag{5}
$$

for $j = 0 , 1 , . . . , m _ { 1 } - 1$ , provided $J _ { 1 } , J _ { 2 } , \ldots , J _ { q }$ are the only Jordan blocks of J associated with $\lambda _ { 1 }$ . More specifically, Eq. (5) implies

$$
Z _ { 1 0 } = { \cal P } \mathrm { d i a g } [ I _ { r } , { \cal O } ] { \cal P } ^ { - 1 } ,\tag{6}
$$

where $r = n _ { 1 } + n _ { 2 } + \cdot \cdot \cdot + n _ { q }$

The nature of the results for general $\lambda _ { k }$ should now be quite clear, and the required statements follow.

The results of Theorems 1 and 2 should be regarded as generalizations of Exercise 4.14.3. They may help in computing $f ( A )$ and especially in simultaneously finding several functions of the same matrix. In the last case each function can be represented as in Eq. (1); only the coefficients $f _ { k , j }$ differ from one function to another.

When faced with the problem of finding the matrices $Z _ { k j }$ , the obvious technique is first to find the interpolatory polynomials $\varphi _ { k j } ( \lambda )$ and then to put $Z _ { k j } = \varphi _ { k j } ( A )$ . However, the computation of the polynomials $\varphi _ { k j } ( \lambda )$ may be a very laborious task, and the following exercise suggests how this can be avoided.

Example 3 (see Exercises 6.2.4, 6.5.2, and 9.4.1). We want to find the component matrices of the matrix

$$
A = { \left[ \begin{array} { l l l } { 6 } & { 2 } & { 2 } \\ { - 2 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 2 } \end{array} \right] } .
$$

We also want to find ln A using Theorem 1. We have seen that the minimal polynomial of A is $( \lambda - 2 ) ( \lambda - 4 ) ^ { 2 }$ and so, for any f defined on the spectrum of A, Theorem 1 gives

$$
f ( A ) = f ( 2 ) Z _ { 1 0 } + f ( 4 ) Z _ { 2 0 } + f ^ { ( 1 ) } ( 4 ) Z _ { 2 1 } .\tag{7}
$$

We substitute for f(λ) three judiciously chosen linearly independent polynomials and solve the resulting simultaneous equations for $Z _ { 1 0 } , Z _ { 2 0 }$ 2 and $Z _ { 2 1 }$ . Thus, putting $f ( \lambda ) = 1 , f ( \lambda ) = \lambda - 4$ and $f ( \lambda ) = ( \lambda - 4 ) ^ { 2 }$ in turn, we obtain

$$
Z _ { 1 0 } + Z _ { 2 0 } = I ,
$$

$$
- 2 Z _ { 1 0 } + Z _ { 2 1 } = A - 4 I = { \left[ \begin{array} { r r r } { 2 } & { 2 } & { 2 } \\ { - 2 } & { - 2 } & { 0 } \\ { 0 } & { 0 } & { - 2 } \end{array} \right] } ,
$$

$$
4 Z _ { 1 0 } = ( A - 4 I ) ^ { 2 } = { \left[ 0 \begin{array} { l l l } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 4 } \\ { 0 } & { 0 } & { 4 } \end{array} \right] } .
$$

These equations are easily solved to give

$$
Z _ { 1 0 } = { \left[ \begin{array} { l l l } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 1 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } , \qquad Z _ { 2 0 } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] } , \qquad Z _ { 2 1 } = { \left[ \begin{array} { l l l } { 2 } & { 2 } & { 2 } \\ { - 2 } & { - 2 } & { - 2 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] } .
$$

By comparison, the straightforward calculation of a component matrix, say $Z _ { 2 0 }$ , using its definition, $Z _ { 2 0 } = \varphi _ { 2 0 } ( A )$ , is more complicated. Seeking a polynomial $\varphi _ { 2 0 } ( \lambda )$ of degree not exceeding 2 and such that

$$
\varphi _ { 2 0 } ( 2 ) = 0 , \qquad \varphi _ { 2 0 } ( 4 ) = 1 , \qquad \varphi _ { 2 0 } ^ { \prime } ( 4 ) = 0 ,\tag{8}
$$

we write (see the proof of Proposition 9.2.1)

$$
\varphi _ { 2 0 } ( \lambda ) = [ \alpha _ { 0 } + \alpha _ { 1 } ( \lambda - 4 ) ] ( \lambda - 2 )
$$

and observe that the conditions (8) give $\begin{array} { r } { \alpha _ { 0 } = \frac { 1 } { 2 } , \alpha _ { 1 } = - \frac { 1 } { 4 } } \end{array}$ . Hence

$$
\begin{array} { r } { Z _ { 2 0 } = - \frac { 1 } { 4 } A ^ { 2 } + 2 A - 3 I = \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] , } \end{array}
$$

as required.

Note that formula (7) for $f ( \lambda ) = \ln \lambda$ provides another method for finding In A (compare with that used in Exercise 9.4.1):

$$
\begin{array} { r } { \ln A = ( \ln 2 ) Z _ { 1 0 } + ( \ln 4 ) Z _ { 2 0 } + \frac { 1 } { 4 } Z _ { 2 1 } = \left[ \begin{array} { c c c } { \ln 4 + \frac { 1 } { 2 } } & { \frac { 1 } { 2 } } & { \frac { 1 } { 2 } } \\ { - \frac { 1 } { 2 } } & { \ln 4 - \frac { 1 } { 2 } } & { \ln 2 - \frac { 1 } { 2 } } \\ { 0 } & { 0 } & { \ln 2 } \end{array} \right] , } \end{array}
$$

which coincides with the result of Exercise 9.4.1.

Exercise 4. Check formulas (3) through (6) and the statement of Theorem 2 for the matrix A considered in Exercise 3. □

Note that, in general, the results of Theorem 2 may help in solving the equations for the component matrices.

Exercise 5. Show that the component matrices of

$$
A = \left[ { \begin{array} { r r r r } { - 1 } & { 1 } & { 2 } & { 1 } \\ { 0 } & { - 1 } & { 0 } & { - 3 } \\ { 0 } & { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} } \right]
$$

are (taking $\lambda _ { 1 } = 0 , \lambda _ { 2 } = 1 , \lambda _ { 3 } = - 1 )$

$$
Z _ { 1 0 } = { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { - 4 } \\ { 0 } & { 0 } & { 0 } & { - 3 } \\ { 0 } & { 0 } & { 0 } & { - 1 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] } , \qquad Z _ { 2 0 } = { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } ,
$$

$$
Z _ { 3 0 } = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { - 1 } & { 3 } \\ { 0 } & { 1 } & { 0 } & { 3 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } ,
$$

$$
Z _ { 3 1 } = { \left[ \begin{array} { l l l l } { 0 } & { 1 } & { 0 } & { 3 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } . \quad \boxed { 1 }
$$

The next result allows us to find all component matrices very easily once the projectors $Z _ { k 0 } , k = 1 , 2 , \ldots , s ,$ are known.

Theorem 3. For $k = 1 , 2 , . . . , s a n d j = 0 , 1 , . . . , m _ { k } - 1$

$$
Z _ { k j } = \frac { 1 } { j ! } ( A - \lambda _ { k } I ) ^ { j } Z _ { k 0 } .\tag{9}
$$

ProoF. Observe first that the result is trivial for $j = 0 .$ Without loss of generality, we will again suppose $k = 1$ and use the associated notations introduced above. Since $A \bar { \bf \Phi } - \bar { \lambda } _ { 1 } I = P ( J - \lambda _ { 1 } I ) P ^ { - 1 }$ , it follows that

$$
J - \lambda _ { 1 } I = P ^ { - 1 } ( A - \lambda _ { 1 } I ) P = \mathrm { d i a g } [ N _ { n _ { 1 } } , \ldots , N _ { n _ { q } } , J _ { q + 1 } - \lambda _ { 1 } I , \ldots , J _ { t } - \lambda _ { 1 } I ] ,\tag{10}
$$

where $J _ { 1 } , J _ { 2 } , \ldots , J _ { q }$ are the only Jordan blocks of J associated with $\lambda _ { 1 }$ Multiplying Eq. (10) on the right by $P ^ { - 1 } Z _ { 1 j } P$ and using Eq. (5), we obtain

$$
j ! P ^ { - 1 } ( A - \lambda _ { 1 } I ) Z _ { 1 j } P = \mathrm { d i a g } [ N _ { n _ { 1 } } ^ { j + 1 } , \ldots , N _ { n _ { q } } ^ { j + 1 } , 0 , \ldots , 0 ] .
$$

Using Eq. (5) again, we thus have

$$
j ! P ^ { - 1 } ( A - \lambda _ { 1 } I ) Z _ { 1 j } P = ( j + 1 ) ! P ^ { - 1 } Z _ { 1 , j + 1 } P
$$

and

$$
Z _ { 1 , j + 1 } = \frac { 1 } { j + 1 } ( A - \lambda _ { 1 } I ) Z _ { 1 j }
$$

for $j = 0 , 1 , \ldots , m _ { k } - 1$ . Applying this result repeatedly, we obtain Eq. (9) for k = 1. ■

Theorem 3 should now be complemented with some description of the projectors $Z _ { k 0 } , k = 1 , 2 , \ldots , s$ (see also Section 9.6).

Theorem 4. With the previous notation,

$$
\operatorname { I m } Z _ { k 0 } = \operatorname { K e r } ( A - \lambda _ { k } I ) ^ { m _ { k } } .
$$

ProoF. We will again consider only the case $k = 1$ . If J is the Jordan form of A used in the above discussion, then (see Eq. (10))

$$
( J - \lambda _ { 1 } I ) ^ { m _ { 1 } } = \mathrm { { d i a g } } [ 0 , \ldots , 0 , ( J _ { q + 1 } - \lambda _ { 1 } I ) ^ { m _ { 1 } } , \ldots , ( J _ { t } - \lambda _ { 1 } I ) ^ { m _ { 1 } } ] ,
$$

since $n _ { 1 } , n _ { 2 } , \ldots , n _ { q } \leq m _ { 1 }$ . The blocks $( J _ { r } - \lambda _ { 1 } I ) ^ { m _ { 1 } }$ are easily seen to be nonsingular for $r = q + 1 , \ldots , t ,$ and it follows that the kernel of $( J - \lambda _ { 1 } I ) ^ { m _ { 1 } }$ is spanned by the unit vectors $e _ { 1 } , e _ { 2 } , \ldots , e _ { r }$ , where $r = n _ { 1 } + n _ { 2 } + \cdots + n _ { q }$ Let $\mathcal { S }$ denote this space.

We also have $( A \bar { \bf { \Psi } } - \lambda _ { 1 } I ) ^ { m _ { 1 } } = P ( J - \lambda _ { 1 } I ) ^ { m _ { 1 } } P ^ { - 1 }$ , and it follows immediately that $\pmb { x } \in \mathbf { K e r } ( A - \lambda _ { 1 } I ) ^ { m _ { 1 } }$ if and only if $P ^ { - 1 } { \pmb x } \in { \mathcal { S } } .$

Using Eq. (6) we see that x ∈ Im $Z _ { 1 0 }$ if and only if

$$
P ^ { - 1 } \pmb { x } \in \operatorname { I m } [ I _ { r } \quad 0 ] P ^ { - 1 } = \mathcal { S } ,
$$

and hence $\mathrm { K e r } ( A - \lambda _ { 1 } I ) ^ { m _ { 1 } } = \mathrm { I m } Z _ { 1 0 }$ .■

It turns out that the result of the theorem cannot be extended to give an equally simple description of Im $Z _ { k j }$ for $j \geq 1$ . However, a partial result for Im $Z _ { k , m _ { k } - 1 }$ is given in Exercise 7.

Exercise 6. Prove that $( A - \lambda _ { k } I ) ^ { m _ { k } } Z _ { k 0 } = 0 .$

Exercise 7. Prove that Im $Z _ { k 0 } =$ Im $Z _ { k 1 } = \cdots \supset$ Im $Z _ { k , m _ { k } - 1 }$ and that Im $Z _ { k , m _ { k } - 1 }$ is a subspace $\mathcal { S } _ { k }$ of $\operatorname { K e r } ( A - \lambda _ { k } I )$ . Show that the dimension of $\mathcal { S } _ { k }$ is equal to the number of Jordan blocks associated with $\lambda _ { k }$ having order $m _ { k }$

Exercise 8. If x, y are, respectively, right and left eigenvectors (see Section 4.10) associated with $\lambda _ { 1 }$ , prove that $Z _ { 1 0 } { \pmb x } = { \pmb x }$ and $\mathbf { y } ^ { \mathrm { { T } } } Z _ { 1 0 } = \mathbf { y } ^ { \mathrm { { T } } }$

Exercise 9. If A is Hermitian, prove that $Z _ { k 0 }$ is an orthogonal projector onto the (right) eigenspace of $\lambda _ { k }$

Exercise 10. Consider the $n \times n$ matrix A with all diagonal elements equal to a number a and all off-diagonal elements equal to 1. Show that the eigenvalues of A are $\lambda _ { 1 } = n + a - 1$ and $\lambda _ { 2 } = a - 1$ with $\lambda _ { 2 }$ repeated $n - 1$ times. Show also that

$$
Z _ { 1 0 } = { \frac { 1 } { n } } { \left[ \begin{array} { l l l l } { 1 } & { 1 } & { \cdots } & { 1 } \\ { 1 } & { 1 } & { \cdots } & { 1 } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 1 } & { 1 } & { \cdots } & { 1 } \end{array} \right] } , \quad Z _ { 2 0 } = { \frac { 1 } { n } } { \left[ \begin{array} { l l l l l } { n - 1 } & { - 1 } & { - 1 } & { \cdots } & { - 1 } \\ { - 1 } & { n - 1 } & { - 1 } & { \cdots } & { - 1 } \\ { \vdots } & { \vdots } & & { } & { \vdots } \\ { - 1 } & { - 1 } & { \cdots } & { n - 1 } \end{array} \right] } .
$$

## 9.6 Component Matrices and Invariant Subspaces

It was shown in Chapter 6 (see especially Theorem 6.2.3 and Section 6.3) that, given an arbitrary matrix $\ b { A } \in \mathbb { C } ^ { n \times n }$ , the space $\mathbb { C } ^ { n }$ is a direct sum of the generalized eigenspaces of A. Now, Theorem 9.5.4 states that each component matrix $Z _ { k 0 }$ is a projector onto the generalized eigenspace associated with eigenvalue $\lambda _ { k } , k = 1 , 2 , \ldots , s .$ .Furthermore, the result of Theorem 9.5.2(a), the resolution of the identity, shows that the complementary projector $I - Z _ { k 0 }$ can be expressed in the form

$$
I - Z _ { k 0 } = \sum _ { j = 0 , j \neq k } ^ { s } Z _ { j 0 }
$$

and, since Im $Z _ { i 0 } \cap$ Im ${ \cal Z } _ { j 0 } = \{ \pmb { \theta } \}$ when $i \neq j ,$

$$
\mathrm { K e r } Z _ { k 0 } = \mathrm { I m } ( I - Z _ { k 0 } ) = \sum _ { j = 0 , j \neq k } ^ { s } \cdot \mathrm { I m } Z _ { j 0 } .\tag{1}
$$

Thus, both Im $Z _ { k 0 }$ and Ker $Z _ { k 0 }$ are A-invariant and the following result holds.

Theorem 1. The component matrix $Z _ { k 0 }$ associated with an eigenvalue $\lambda _ { k }$ of $A \in \mathbb { C } ^ { n \times n }$ is a projector onto the generalized eigenspace of $\lambda _ { k }$ and along the sum of generalized eigenspaces associated with all eigenvalues of A different from $\lambda _ { k }$

The discussion of Section 4.8 shows that if we choose bases in Im $Z _ { k 0 }$ and Ker $Z _ { k 0 }$ , they will determine a basis for $\mathbb { C } ^ { n }$ in which A has a representation diagl $\left[ A _ { 1 } , A _ { 2 } \right]$ , where the sizes of $A _ { 1 }$ and $A _ { 2 }$ are just the dimensions of Im $Z _ { k 0 }$ and Ker $Z _ { k 0 }$ , respectively. In particular, if these bases are made up of Jordan chains for A, as in Section 6.4, then $A _ { 1 }$ and $A _ { 2 }$ both have Jordan form

For any $A \in \mathbb { C } ^ { n \times n }$ and any $z \not \in \sigma ( A )$ , the function $f ( \lambda ) = ( z - \lambda ) ^ { - 1 }$ is defined on $\sigma ( A )$ ; hence the resolvent of $A , ( z I - A ) ^ { - 1 }$ , exists. Holding A fixed, the resolvent can be considered to be a function of z on any domain in C not containing points of $\sigma ( A )$ , and this point of view plays an important role in matrix analysis. Indeed, we shall develop it further in Section 9.9 and make substantial use of it in Chapter 11, in our introduction to perturbation theory.

A representation for the resolvent was obtained in Exercise 9.5.2:

$$
( z I - A ) ^ { - 1 } = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } \frac { j ! } { ( z - \lambda _ { k } ) ^ { j + 1 } } Z _ { k j } .
$$

Using the orthogonality properties of the matrices $Z _ { k j }$ , it is easily deduced that

$$
( z I - { \cal A } ) ^ { - 1 } ( I - { \cal Z } _ { 1 0 } ) = \sum _ { k = 2 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } \frac { j ! } { ( z - \lambda _ { k } ) ^ { j + 1 } } { \cal Z } _ { k j }
$$

and, using Eq. (1) and Exercise 9.5.6, the resolvent has Im $( I - Z _ { 1 0 } )$ as its range. Now as $z  \lambda _ { 1 }$ , elements of $( z I - A ) ^ { - 1 }$ will become unbounded. But, since the limit on the right of the equation exists, we see that multiplication of the resolvent by $I - Z _ { 1 0 }$ has the effect of eliminating the singular part of $( z I - A ) ^ { - 1 }$ at $z = \lambda _ { 1 }$ . In other words, the restriction of the resolvent to the subspace

$$
\mathrm { I m } ( I - Z _ { 1 0 } ) = \sum _ { j = 2 } ^ { s } \mathrm { I m } Z _ { j 0 }
$$

has no singularity at $z = \lambda _ { 1 }$

Define the matrix

$$
E _ { 1 } = \operatorname * { l i m } _ { z  \lambda _ { 1 } } ( z I - A ) ^ { - 1 } ( I - Z _ { 1 0 } ) = \sum _ { k = 2 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } { \frac { j ! } { ( \lambda _ { 1 } - \lambda _ { k } ) ^ { j + 1 } } } Z _ { k j } .\tag{2}
$$

The next proposition expresses $\begin{array} { r } { I - Z _ { 1 0 } = \sum _ { k = 2 } ^ { s } Z _ { k 0 } } \end{array}$ in terms of $E _ { 1 }$ and will be used in Chapter 11.

Theorem 2. In the notation of the previous paragraphs,

$$
I - Z _ { 1 0 } = E _ { 1 } ( \lambda _ { 1 } I - A ) .
$$

PROOF. The simple statement $\lambda _ { 1 } I - A = ( \lambda _ { 1 } - z ) I + ( z I - A )$ implies

$$
( z I - A ) ^ { - 1 } ( \lambda _ { 1 } I - A ) = ( \lambda _ { 1 } - z ) ( z I - A ) ^ { - 1 } + I .
$$

Multiply on the left by $I - Z _ { 1 0 }$ , take the limit as $z  \lambda _ { 1 }$ , and take advantage of Eq. (2) to obtain the result.

Exercise 1. Let $A \in \mathbb { C } ^ { n \times n }$ and $\sigma ( A ) = \{ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { s } \}$ . Define a function $f _ { k } ( \lambda )$ on the spectrum of A by setting $f _ { k } ( \lambda ) \equiv 1$ in an arbitrarily small neighborhood of $\lambda _ { k }$ and $f _ { k } ( \lambda ) \equiv 0$ in an arbitrarily small neighborhood of each $\lambda _ { j } \in \sigma ( A )$ with $\lambda _ { j } \neq \lambda _ { k }$ . Show that $f _ { k } ( A ) = Z _ { k 0 }$ and use Exercise 9.3.4 to show that $Z _ { k 0 }$ is idempotent.

Exercise 2. If $\lambda = \lambda _ { 1 }$ is an eigenvalue of A and $\lambda _ { 1 } , \ldots , \lambda _ { s }$ are the distinct eigenvalues of A, show that, for any $z \not \in \sigma ( A )$ 2

$$
( z I - A ) ^ { - 1 } = \sum _ { j = 0 } ^ { m _ { 1 } - 1 } \frac { j ! Z _ { 1 j } } { ( z - \lambda ) ^ { j + 1 } } + E ( z ) ,
$$

where $E ( z )$ is a matrix that is analytic on a neighborhood of λ and $Z _ { 1 1 } E ( z )$ $= E ( z ) Z _ { 1 1 } = 0 .$ Write $E = E ( \lambda )$ and use this representation to obtain Theorem $2 . \sqsupset$

## 9.7 Further Properties of Functions of Matrices

In this section we obtain some additional properties of functions of matrices, which, in particular, allow us to extend some familiar identities for scalar functions to their matrix-valued counterparts. For example, we ask whether the identity sir $1 ^ { 2 } \alpha + \cos ^ { 2 } \alpha = 1$ implies that si $\mathbf { n } ^ { 2 } \mathbf { \nabla } A + \cos ^ { 2 } \mathbf { \nabla } A = I ,$ and does $e ^ { \alpha } e ^ { - \alpha } = 1$ imply $e ^ { A } e ^ { - A } = I ?$ We answer these questions (and a whole class of such questions) in the following theorems.

Theorem 1. Let $P ( u _ { 1 } , u _ { 2 } , \ldots , u _ { t } )$ be a scalar polynomial in $u _ { 1 } , u _ { 2 } , \ldots , u _ { t }$ and let $f _ { 1 } ( \lambda ) , f _ { 2 } ( \lambda ) , \ldots , f _ { t } ( \lambda )$ be functions defned on the spectrum of $A \in \mathbb { C } ^ { n ^ { \times n } } .$ If the function $f ( \lambda ) = P ( f _ { 1 } ( \lambda ) , f _ { 2 } ( \lambda ) , . . . , f _ { t } ( \lambda ) )$ assumes zero values on the spectrum of A, then

$$
f ( A ) = P ( f _ { 1 } ( A ) , f _ { 2 } ( A ) , \ldots , f _ { t } ( A ) ) = 0 .
$$

PROOF. Let $p _ { 1 } ( \lambda ) , \ p _ { 2 } ( \lambda ) , \ldots , p _ { t } ( \lambda )$ be interpolatory polynomials on the spectrum of A for $f _ { 1 } ( \lambda ) , f _ { 2 } ( \lambda ) , \ldots , f _ { t } ( \lambda )$ , respectively. Then by definition of the $p _ { i }$ , we have $f _ { i } ( A ) = p _ { i } ( A )$ for $i = 1 , 2 , \dots , t .$ Denote the polynomial $P ( p _ { 1 } ( \lambda ) , p _ { 2 } ( \lambda ) , \dots , p _ { t } ( \lambda ) )$ by $p ( \lambda )$ and observe that since $p _ { i } ( \lambda )$ and $f _ { i } ( \lambda )$ have the same values on the spectrum of A $( 1 \leq i \leq t )$ , so do $p ( \lambda )$ and $f ( \lambda )$ Hence our assumption that $f ( \lambda )$ is zero on the spectrum of A implies the same for $P ( \lambda )$ and therefore $f ( A ) = p ( A ) = 0 .$

For the particular cases mentioned above, we first choose $f _ { 1 } ( \lambda ) =$ sin λ, $f _ { 2 } ( \lambda ) = \cos \lambda ,$ and $P ( u _ { 1 } , u _ { 2 } ) = u _ { 1 } ^ { 2 } + u _ { 2 } ^ { 2 } - 1$ to prove that, for every $A \in \mathbb { C } ^ { n \times n } .$ , it is true that $\sin ^ { 2 } A + \cos ^ { 2 } A = I$ Next, taking $f _ { 1 } ( \lambda ) = e ^ { \lambda } ,$ $f _ { 2 } ( \lambda ) = e ^ { - \lambda }$ , and $P ( u _ { 1 } , u _ { 2 } ) = u _ { 1 } u _ { 2 } - 1$ , we obtain $e ^ { \boldsymbol { A } } e ^ { \boldsymbol { - A } } = \boldsymbol { I }$ Thus, $e ^ { - A }$ $\boldsymbol { \mathbf { \mathit { \sigma } } } = ( e ^ { \boldsymbol { \mathbf { \mathit { A } } } } ) ^ { - 1 }$

Exercise 1. If $\ b { A } \in \mathbb { C } ^ { n \times n }$ and the functions $f _ { 1 } ( \lambda )$ and $f _ { 2 } ( \lambda )$ are defined on the spectrum of A, show that the functions $F _ { 1 } ( \lambda ) = f _ { 1 } ( \lambda ) + f _ { 2 } ( \lambda ) , \ F _ { 2 } ( \lambda ) =$ $f _ { 1 } ( \lambda ) f _ { 2 } ( \lambda )$ are also defined on the spectrum of A, and $F _ { 1 } ( A ) = f _ { 1 } ( A ) + f _ { 2 } ( A ) .$ $F _ { 2 } ( A ) = f _ { 1 } ( A ) f _ { 2 } ( A )$

Exercise 2. If $p ( \lambda )$ and $q ( \lambda )$ are relatively prime polynomials, det $q ( A ) \neq 0 ,$ and $r ( \lambda )$ denotes the rational function $p ( \lambda ) / q ( \lambda )$ , prove that

$$
r ( A ) = p ( A ) [ q ( A ) ] ^ { - 1 } = [ q ( A ) ] ^ { - 1 } p ( A ) .
$$

Exercise 3. Prove that for any $A \in \mathbb { C } ^ { n \times n }$

$$
e ^ { i A } = \cos A + i \sin A .
$$

(Note that, in general, the cosine and sine functions must be considered as defined on $\mathbb { C } . ) \ \sqcap$

We can also discuss the possibility of taking pth roots of a matrix with the aid of Theorem 1. Suppose that p is a positive integer and let $f _ { 1 } ( \lambda ) = \lambda ^ { 1 / p }$ $f _ { 2 } ( \lambda ) = \lambda ,$ and $P ( u _ { 1 } , u _ { 2 } ) = u _ { 1 } ^ { p } - u _ { 2 }$ . We would normally choose a singlevalued branch of the function $\lambda ^ { 1 / p }$ for $f _ { 1 } ( \lambda )$ , but this is not essential. If, however, the matrix A has a zero eigenvalue with index greater than 1, then, since derivatives of $f _ { 1 } ( \lambda )$ at the origin are needed, $f _ { 1 } ( \lambda )$ would not be defined on the spectrum of A. Thus, if A is nonsingular, or is singular with a zero eigenvalue of index one, we define $f _ { 1 } ( \lambda ) = \lambda ^ { 1 / p }$ (with a known convention concerning the choice of branches at the eigenvalues), and

$$
A ^ { 1 / p } = f _ { 1 } ( A ) = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } f _ { 1 } ^ { ( j ) } ( \lambda _ { k } ) Z _ { k j } .
$$

Then, by Theorem 1 applied to the functions $f _ { 1 } ( \lambda ) , f _ { 2 } ( \lambda )$ ,and $P ( u _ { 1 } , u _ { 2 } )$ defined above,

$$
( A ^ { 1 / p } ) ^ { p } = A .
$$

This discussion should be compared with the definition of the square root of a positive definite matrix made in Section 5.4.

It should be noted that our definition of $A ^ { 1 / 2 }$ , for example, does not include all possible matrices B for which $B ^ { 2 } = A$ . To illustrate this point, any real symmetric orthogonal matrix B has the property that $B ^ { 2 } = I ,$ but B will not necessarily be generated by applying our definitions to find $I ^ { 1 / 2 }$ .A particular example is the set of matrices defined by

$$
B ( \theta ) = { \left[ \begin{array} { l l } { \cos \theta } & { \sin \theta } \\ { \sin \theta } & { - \cos \theta } \end{array} \right] }
$$

(see Exercise 2.6.16).

Theorem 2. Let $h ( \lambda ) = g ( f ( \lambda ) )$ , where $f ( \lambda )$ is defined on the spectrum of $\ b { A } \in \mathbb { C } ^ { n \times n }$ and $g ( \mu )$ is defined on the spectrum of $B = f ( A )$ . Then $h ( \lambda )$ is defined on the spectrum of A and $h ( A ) = g ( f ( A ) )$

PROOF. Let $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ be the distinct eigenvalues of A with indices $m _ { 1 } , m _ { 2 } , \ldots , m _ { s }$ , respectively. Denote $f ( \lambda _ { k } ) = \mu _ { k } \operatorname { f o r } k = 1 , 2 , \ldots , s .$ Since

$$
\begin{array} { c } { { h ( \lambda _ { k } ) = g ( \mu _ { k } ) , } } \\ { { h ^ { \prime } ( \lambda _ { k } ) = g ^ { \prime } ( \mu _ { k } ) f ^ { \prime } ( \lambda _ { k } ) , } } \\ { { \vdots } } \\ { { h ^ { ( m _ { k } - 1 ) } ( \lambda _ { k } ) = g ^ { ( m _ { k } - 1 ) } ( \mu _ { k } ) [ f ^ { \prime } ( \lambda _ { k } ) ] ^ { m _ { k } - 1 } + \cdots + g ^ { \prime } ( \mu _ { k } ) f ^ { ( m _ { k } - 1 ) } ( \lambda _ { k } ) , } } \end{array}\tag{1}
$$

it follows that $h ( \lambda )$ is defined on the spectrum of A and assigns values given by the formulas in (1). Let $r ( \mu )$ denote any polynomial that has the same values as $g ( \mu )$ on the spectrum of B and consider the function $r ( f ( \lambda ) )$ . If the values of $h ( \lambda )$ and $r ( f ( \lambda ) )$ coincide on the spectrum of $A _ { i }$ then $h ( \lambda ) -$ $r ( f ( \lambda ) )$ assigns zero values on the spectrum of A and, by Theorem 1,

$$
h ( A ) = r ( f ( A ) ) = r ( B ) = g ( B ) = g ( f ( A ) ) ,
$$

and the result is established.

Now observe that in view of (1) the values of $h ( \lambda )$ and $r ( f ( \lambda ) )$ coincide on the spectrum of A if

$$
r ^ { ( i ) } ( \mu _ { k } ) = g ^ { ( i ) } ( \mu _ { k } )\tag{2}
$$

for $i = 0 , 1 , \ldots , m _ { k } - 1 , k = 1 , 2 , \ldots , s .$

Let us show that $\{ g ( \mu _ { k } ) , g ^ { \prime } ( \mu _ { k } ) , \ldots , g ^ { ( m _ { k } - 1 ) } ( \mu _ { k } ) \}$ contains all the values of $g ( \mu )$ on the spectrum of B. This fact is equivalent to saying that the index $n _ { k }$ of the eigenvalue $\mu _ { k }$ of B does not exceed $m _ { k }$ or that the polynomial $p ( \mu ) = ( \mu - \mu _ { 1 } ) ^ { m _ { 1 } } ( \mu - \mu _ { 2 } ) ^ { m _ { 2 } } \cdot \cdot \cdot ( \mu - \mu _ { s } ) ^ { m _ { k } }$ annihilates B $( 1 \leq k \leq s )$ . To see this, observe that $q ( \lambda ) = p ( f ( \lambda ) ) = ( f ( \lambda ) - f ( \lambda _ { 1 } ) ) ^ { m _ { 1 } } \cdot \cdot \cdot ( f ( \lambda ) - f ( \lambda _ { s } ) ) ^ { m _ { s } }$ has zeros $\lambda _ { k }$ with multiplicity at least $m _ { k } \ ( k = 1 , 2 , . . . , s )$ and therefore $q ( \lambda )$ assigns zero values on the spectrum of A. Thus, by Theorem 1 with $t = 1 , p ( B ) = p ( f ( A ) ) = 0$ and $p ( \lambda )$ is an annihilating polynomial for B. Now defining the polynomial $r ( \mu )$ as satisfying the conditions (2), we obtain a polynomial with the same values as $g ( \mu )$ on the spectrum of B and the proof is completed. Note that $r ( \mu )$ is not necessarily the interpolatory polynomial for $g ( \mu )$ on the spectrum of B of least possible degree.■

Exercise 4. Prove that for any $A \in \mathbb { C } ^ { n \times n }$

$$
\sin 2 A = 2 \sin A \cos A . \quad \bigsqcup
$$

## 9.8 Sequences and Series of Matrices

In this section we show how other concepts of analysis can be applied to matrices and particularly to functions of matrices as we have defined them. We first consider sets of matrices defined on the nonnegative integers, that is, sequences of matrices.

Let $A _ { 1 } , A _ { 2 } , \ldots$ be a sequence of matrices belonging to $\mathbb { C } ^ { m \times n }$ and let $a _ { i j } ^ { ( p ) }$ be the $i , j \mathrm { t h }$ element of $A _ { p } , p = 1 , 2 , \ldots .$ The sequence $A _ { 1 } , A _ { 2 } , \ldots$ is said to converge to the matrix $\ b { A } \in \mathbb { C } ^ { m \times n }$ if there exist numbers $a _ { i j }$ (the elements of A) such that $a _ { i j } ^ { ( p ) }  a _ { i j }$ as $p  \infty$ for each pair of subscripts i, j. A sequence that does not converge is said to diverge. Thus the convergence of sequences of matrices is defined as elementwise convergence. The definition also includes the convergence of column and row vectors as special cases.

Exercise 1. Let $\left\{ A _ { p } \right\} _ { p } ^ { \infty } = 1 , \left\{ B _ { p } \right\} _ { p } ^ { \infty } = 1$ be convergent sequences of matrices from $\mathbb { C } ^ { m \times n }$ and assume that $A _ { p }  A , B _ { p }  B$ as $p  \infty$ . Prove that as $p  \infty$

(a) $A _ { p } + B _ { p } \to A + B$

(b) $A _ { p } B _ { p }  A B$ and, in particular, $\alpha _ { p } B _ { p }  \alpha B$ for any sequence $\alpha _ { p }  \alpha$ in C;

(c) $Q A _ { v } Q ^ { - 1 }  Q A Q ^ { - 1 }$

(d) $\mathrm { d i a g } [ A _ { p } , B _ { p } ] \to \mathrm { d i a g } [ A , B ]$

Hint. These results follow from fundamental properties of sequences of complex numbers. For part (b), if $\alpha _ { p }  \alpha$ and $\beta _ { p }  \beta$ as $p  \infty$ , write

$$
\alpha _ { p } \beta _ { p } - \alpha \beta = ( \alpha _ { p } - \alpha ) \beta + ( \beta _ { p } - \beta ) \alpha + ( \alpha _ { p } - \alpha ) ( \beta _ { p } - \beta ) . \quad \bigsqcup
$$

We now consider the case in which the members of a sequence of matrices are defined as functions of $A \in \mathbb { C } ^ { n \times n }$ . Thus, let the sequence of functions $f _ { 1 } ( \lambda ) , f _ { 2 } ( \lambda ) , \dots$ be defined on the spectrum of A, and define $A _ { p } \triangleq f _ { p } ( A )$ $p = 1 , 2 , \ldots { } .$ or each term of the sequence $A _ { 1 } , A _ { 2 } , \ldots$ , Theorem 9.5.1 yields

$$
f _ { p } ( A ) = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } f _ { p } ^ { ( j ) } ( \lambda _ { k } ) Z _ { k j } .\tag{1}
$$

Now the component matrices $Z _ { k j }$ depend only on A and not on $p ,$ so that each term of the sequence is defined by the m numbers $f _ { p } ^ { ( j ) } ( \lambda _ { k } )$ for $k =$ $1 , 2 , \ldots , s$ and $j = 0 , 1 , \ldots , m _ { k } - 1$ . We might therefore expect that the convergence of $A _ { 1 } , A _ { 2 } , \ldots$ can be made to depend on the convergence of the m scalar sequences $f _ { 1 } ^ { ( j ) } ( \lambda _ { k } ) , f _ { 2 } ^ { ( j ) } ( \lambda _ { k } ) , . .$ . rather than the $n ^ { 2 }$ scalar sequences of the elements of $A _ { 1 } , A _ { 2 } , \ldots .$

Theorem 1. Let the functions $f _ { 1 } , f _ { 2 } , \ldots$ be defined on the spectrum of $A \in \mathbb { C } ^ { n \times n }$ and let $A _ { p } = f _ { p } ( A ) , p = 1 , 2 , . . .$ Then the sequence $A _ { 1 } , A _ { 2 } , \ldots ,$ $A _ { p } , \ldots$ converges as $p  \infty$ if and only if the m scalar sequences $f _ { 1 } ^ { ( j ) } ( \lambda _ { k } ) ,$ $f _ { 2 } ^ { ( j ) } ( \lambda _ { k } ) , \ldots , f _ { p } ^ { ( j ) } ( \lambda _ { k } ) , \ldots ( k = 1 , 2 , \ldots , s , j = 0 , 1 , \ldots , m _ { k } - 1 , m = m _ { 1 } + m _ { 2 }$ $+ \cdots + m _ { s } )$ converge as $p  \infty$

Moreover, if $f _ { p } ^ { ( j ) } ( \lambda _ { k } )  f ^ { ( j ) } ( \lambda _ { k } )$ as $p  \infty$ for each j and k and for some function $f ( \lambda )$ , then $A _ { p } \to f ( A )$ as $p  \infty$ . Conversely, if lim $A _ { p }$ exists as $p  \infty$ , then there is a function f(λ) defined on the spectrum of A such that lim $A _ { p } = f ( A )$ as $p  \infty$

PROOF. If $f _ { p } ^ { ( j ) } ( \lambda _ { k } ) \to f ^ { ( j ) } ( \lambda _ { k } )$ as $p  \infty$ for each j and k and some $f ( \lambda )$ then Eq. (1) and Exercise 1 imply that

$$
\operatorname* { l i m } _ { p  \infty } { \cal A } _ { p } = \operatorname* { l i m } _ { p  \infty } f _ { p } ( A ) = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } \bigg ( \operatorname* { l i m } _ { p  \infty } f _ { p } ^ { ( j ) } ( \lambda _ { k } ) \bigg ) Z _ { k j }\tag{2}
$$

and

$$
\operatorname* { l i m } _ { p \to \infty } { \cal A } _ { p } = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } f ^ { ( j ) } ( \lambda _ { k } ) Z _ { k j } = f ( A ) .\tag{3}
$$

Conversely, suppose that lim $A _ { p }$ exists as $p  \infty$ and denote the elements of $A _ { p } = f _ { p } ( A )$ by $a _ { i r } ^ { ( p ) } , i , r = 1 , 2 , \cdot \cdot \cdot , n , p = 1 , 2 , \cdot \cdot \cdot .$ Viewing Eq. (1) as a set of $n ^ { 2 }$ equations for the $m = m _ { 1 } + m _ { 2 } + \cdot \cdot \cdot + m _ { s }$ unknowns $f _ { p } ^ { ( j ) } ( \lambda _ { k } ) _ { i }$ where p is fixed, and recalling the linear independence (Theorem 9.5.1) of the component matrices $Z _ { k j }$ as members of $\mathbb { C } ^ { n \times n }$ , we deduce that the $n ^ { 2 } \times m$ coefficient matrix of this system has rank m. Since the degree m of the minimal polynomial of A does not exceed the degree of the characteristic polynomial for $A ,$ it follows that $m \leq n \leq n ^ { 2 }$ and therefore (see Exercise 3.10.7) the system in (1) has a unique solution of the form

$$
f _ { p } ^ { ( j ) } ( \lambda _ { k } ) = \sum _ { i , r = 1 } ^ { n } \gamma _ { i r } a _ { i r } ^ { ( p ) } ,\tag{4}
$$

where the $\gamma _ { i r } \ ( i , r = 1 , 2 , \ldots , n )$ depend on j and k but not on p. Now if lim $A _ { p }$ exists as $p  \infty$ , then so does lim $a _ { i r } ^ { ( p ) }$ and it follows from Eq. (4) that lim $f _ { p } ^ { ( j ) } ( \lambda _ { k } )$ also exists as $p  \infty$ for each j and k. This completes the first part of the theorem.

If $\overline { { f } } _ { p } ^ { ( j ) } ( \lambda _ { k } )  f ^ { ( j ) } ( \lambda _ { k } )$ as p → ∞ for each j and k and for some $f ( \lambda )$ then Eq. (3) shows that $A _ { p } \to f ( A )$ as $p  \infty$ . Conversely, the existence of lim $A _ { p }$ as $p  \infty$ provides the existence of lim $f _ { p } ^ { ( j ) } ( \lambda _ { k } )$ as $p  \infty$ and hence the equality (2). Thus, we may choose for $f ( \bar { \lambda } )$ the interpolatory polynomial whose values on the spectrum of A are the numbers lim $\cdot _ { p } \to _ { \infty } f _ { p } ^ { ( j ) } ( \lambda _ { k } )$ $k = 1 , 2 , . . . , s , j = 0 , 1 , . . . , m _ { k } - 1$ . The proof is complete.

We now wish to develop a similar theorem for series of matrices. First, the series of matrices $\sum _ { p = 0 } ^ { \infty } A _ { p }$ is said to converge to the matrix A (the sum of the series) if the sequence of partial sums $\begin{array} { r } { B _ { \nu } = \sum _ { p = 1 } ^ { \nu } A _ { p } } \end{array}$ converges to A as $\nu  \infty$ . A series that does not converge is said to diverge.

The following theorem is immediately obtained by applying Theorem 1 to a sequence of partial sums.

Theorem 2. If the functions $u _ { 1 } , u _ { 2 } , \ldots$ are defined on the spectrum of $\ b { A } \in \mathbb { C } ^ { n \times n }$ , then $\sum _ { p = 1 } ^ { \infty } u _ { p } ( A )$ converges if and only if the series $\sum _ { p } \sp { \infty } = { 1 } u _ { p } \sp { ( j ) } ( \lambda _ { k } )$ convergé for $k = 1 , 2 , \ldots , s$ and $j = 0 , 1 , \ldots , m _ { k } - 1$

Moreover, if

$$
\sum _ { p = 1 } ^ { \infty } u _ { p } ^ { ( j ) } ( \lambda _ { k } ) = f ^ { ( j ) } ( \lambda _ { k } )
$$

for each j and k, then

$$
\sum _ { p \mathop { = } 1 } ^ { \infty } u _ { p } ( A ) = f ( A ) ,
$$

and vice versa.

We can now apply this theorem to obtain an important result that helps to justify our development of the theory of functions of matrices. The next theorem shows the generality of the definition made in Section 9.3, which may have seemed rather arbitrary at first reading. Indeed, the properties described in the next theorem are often used as a (more restrictive) definition of a function of a matrix.

Theorem 3. Let the function f(λ) have a Taylor series about $\lambda _ { 0 } \in \mathbb { C }$

$$
f ( \lambda ) = \sum _ { p = 0 } ^ { \infty } \alpha _ { p } ( \lambda - \lambda _ { 0 } ) ^ { p } ,\tag{5}
$$

with radius of convergence r. If $\ b { A } \in \mathbb { C } ^ { n \times n }$ , then f (A) is defined and is given by

$$
f ( A ) = \sum _ { p = 0 } ^ { \infty } \alpha _ { p } ( A - \lambda _ { 0 } I ) ^ { p }\tag{6}
$$

if and only if each of the distinct eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ of A satisfies one of the following conditions:

(a) $| \lambda _ { k } - \lambda _ { 0 } | < r ;$

(b) $| \lambda _ { k } - \lambda _ { 0 } | = r$ and the series for $f ^ { ( m _ { k } - 1 ) } ( \lambda )$ (where $m _ { k }$ is the index of $\lambda _ { k } )$ is convergent at the point $\lambda = \lambda _ { k } , 1 \leq k \leq s$

PROOF. First we recall that $f ( A )$ exists if and only if $f ^ { ( j ) } ( \lambda _ { k } )$ exists for $j = 0 , 1 , \ldots , m _ { k } - 1$ and $k = 1 , 2 , \ldots , s .$ Furthermore, the function $f ( \lambda )$ given by Eq. (5) has derivatives of all orders at any point inside the circle of convergence and these derivatives can be obtained by differentiating the series for $f ( \lambda )$ term by term. Hence $f ( \lambda )$ is obviously defined on the spectrum of A if $| \lambda _ { k } - \lambda _ { 0 } | < r$ for $k = 1 , 2 , \ldots , s .$ Also, if $\vert \lambda _ { k } - \lambda _ { 0 } \vert = r$ for some k and the series obtained by $m _ { k } \mathrm { ~ - ~ } 1$ differentiations of the series in (5) is convergent at the point $\lambda = \lambda _ { k }$ then $f ( \lambda _ { k } ) , f ^ { \prime } ( \lambda _ { k } ) , \ldots , f ^ { ( m _ { k } - 1 ) } ( \lambda _ { k } )$ exist and, consequently, $f ( A )$ is defined. Note that, starting with the existence of $f ( A )$ , the above argument can be reversed.

If we now write $u _ { p } ( \lambda ) = \alpha _ { p } ( \lambda - \lambda _ { 0 } ) ^ { p }$ for $\begin{array} { r } { p = 0 , 1 , 2 , \ldots } \end{array}$ then $u _ { p } ( \lambda )$ is certainly defined on the spectrum of A and under the hypotheses (a) or (b), the series $\begin{array} { r } { \sum _ { p = 1 } ^ { \infty } u _ { p } ^ { ( j ) } ( \lambda _ { k } ) , k = 1 , 2 , \ldots , s , j = 0 , 1 , \ldots , \ldots 1 } \end{array}$ , all converge. It now follows from Theorem 2 that $\sum _ { p = 0 } ^ { \infty } u _ { p } ( A )$ converges and has sum $f ( A )$ and vice versa.

Note that for functions of the form (5), a function $f ( A )$ of A can be defined by formula (6). Clearly, this definition cannot be applied for functions having only a finite number of derivatives at the points $\lambda _ { k } \in \sigma ( A )$ , as assumed in Section 9.3.

If the Taylor series for $f ( \lambda )$ about the origin converges for all points in the complex plane (the radius of convergence is infinite), then $f ( \lambda )$ is said to be an entire function and the power series representation for $f ( A )$ will converge for all $A \in \mathbb { C } ^ { n \times n }$ . Among the most important functions of this kind are the trigonometric and exponential functions. Thus, from the corresponding results for (complex) scalar functions, we deduce that for all $\ b { A } \in \mathbb { C } ^ { n \times n }$

$$
\sin { A } = \sum _ { p = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { p } } { ( 2 p + 1 ) ! } } A ^ { 2 p + 1 } , \qquad \cos { A } = \sum _ { p = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { p } } { ( 2 p ) ! } } A ^ { 2 p } ,
$$

$$
e ^ { A } = \sum _ { p = 0 } ^ { \infty } \frac { A ^ { p } } { p ! } , \sinh A = \sum _ { p = 0 } ^ { \infty } \frac { A ^ { 2 p + 1 } } { ( 2 p + 1 ) ! } , \cosh A = \sum _ { p = 0 } ^ { \infty } \frac { A ^ { 2 p } } { ( 2 p ) ! } .
$$

If the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ of A satisfy the conditions $| \lambda _ { j } | < 1$ for $j = 1 , 2 , \dots , n _ { \cdot }$ then we deduce from the binomial theorem and the logarithmic series that

$$
( I - A ) ^ { - 1 } = \sum _ { p = 0 } ^ { \infty } A ^ { p } , \log ( I + A ) = \sum _ { p = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { p - 1 } } { p } } A ^ { p } .\tag{7}
$$

Exercise 2. Prove that if $A \in \mathbb { C } ^ { n \times n } ,$ , then $e ^ { A ( s + t ) } = e ^ { A s } e ^ { A t }$ for any complex numbers s and t.

Exercise 3. Prove that if A and B commute, then $e ^ { \boldsymbol { A } + \boldsymbol { B } } = e ^ { \boldsymbol { A } } e ^ { \boldsymbol { B } }$ , and if $e ^ { ( A + B ) t } = e ^ { A t } e ^ { B t }$ for all t, then A and B commute.

## Exercise 4. Show that if

$$
A = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } , \qquad B = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { \varepsilon } \end{array} \right] } , \qquad C = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right] } ,
$$

then

$$
e ^ { \boldsymbol { A } t } = \left[ \begin{array} { c c } { \boldsymbol { e } ^ { t } - t } & { t } \\ { t } & { \boldsymbol { e } ^ { t } - t } \end{array} \right] , \qquad e ^ { \boldsymbol { B } t } = \left[ \begin{array} { c c } { 1 } & { \boldsymbol { \varepsilon } ^ { - 1 } ( \boldsymbol { e } ^ { s t } - 1 ) } \\ { 0 } & { \boldsymbol { e } ^ { s t } } \end{array} \right] ,
$$

$$
e ^ { C t } = { \left[ \begin{array} { l l } { \cos t } & { \sin t } \\ { - \sin t } & { \cos t } \end{array} \right] } .
$$

Exercise 5. Show that the sequence $A , A ^ { 2 } , A ^ { 3 } , \ldots$ . converges to the zeromatrix if and only $\mathrm { i f } | \lambda | < 1$ for every $\lambda \in \sigma ( A )$ □

## 9.9 The Resolvent and the Cauchy Theorem for Matrices

The theory of (scalar) functions of a complex variable provides a third approach to the definition of $f ( A )$ that is applicable when $f ( \lambda )$ is an analytic unction. This approach is also consistent with the general definition of Section 9.3.

Consider a matrix $A ( \lambda )$ whose elements are functions of a complex variable λ and define the derivative (or integral) of the matrix to be the matrix obtained by differentiating (or integrating) each element of $A ( \lambda )$ . For $r = 0 , 1 , 2 , \ldots$ , we write

$$
\frac { d ^ { r } } { d \lambda ^ { r } } A ( \lambda ) \qquad \mathrm { o r } \qquad A ^ { ( r ) } ( \lambda )
$$

for the derivative of $A ( \lambda )$ of order r.

Exercise 1. Prove that

$$
{ \frac { d } { d t } } \left( e ^ { A t } \right) = A e ^ { A t } = e ^ { A t } A .
$$

Hint. Use the series representation of $e ^ { A t }$

Exercise 2. Prove that (with the variable t omitted from the right-hand expressions)

$$
\frac { d } { d t } \left( A ( t ) \right) ^ { 2 } = A ^ { ( 1 ) } A + A A ^ { ( 1 ) } ,
$$

and construct an example to show that, in general,

$$
\frac { d } { d t } \left( A ( t ) \right) ^ { 2 } \neq 2 A A ^ { ( 1 ) } .
$$

Exercise 3. Prove that, when p is a positive integer and the matrices exist,

$$
\frac { d } { d t } \left( A ( t ) \right) ^ { p } = \sum _ { j = 1 } ^ { p } \ A ^ { j - 1 } A ^ { ( 1 ) } A ^ { p - j } ,
$$

$$
\frac { d } { d t } \left( A ( t ) \right) ^ { - p } = - A ^ { - p } \frac { d A ^ { p } } { d t } A ^ { - p } . \quad \varTheta
$$

The notation

$$
\int _ { L } A ( \lambda ) d \lambda
$$

will be used for the integral of $A ( \lambda )$ taken in the positive direction along a path L in the complex plane, which, for our purposes, will always be a simple piecewise smooth closed contour, or a finite system of such contours, without points of intersection.

Let $A \in \mathbb { C } ^ { n \times n }$ The matrix $( \lambda I - A ) ^ { - 1 }$ is known as the resolvent of A and it has already played an important part in our analysis. Viewed as a function of a complex variable λ, the resolvent is defined only at those points λ that do not belong to the spectrum of A. Since the matrix A is fixed in this section, we use the notation $R _ { \lambda } = ( \lambda I - A ) ^ { - 1 }$ for the resolvent of A.

Exercise 4. Verify that for λ ∉ σ(A),

$$
\frac { d } { d \lambda } R _ { \lambda } = - R _ { \lambda } ^ { 2 } ,
$$

and, more generally,

$$
\frac { d ^ { j } } { d \lambda ^ { j } } R _ { \lambda } = ( - 1 ) ^ { j } j ! R ^ { j + 1 } \mathrm { f o r } j = 1 , 2 , \ldots .
$$

Hint. Use Exercise 4.14.4(a). □

Theorem 1. The resolvent $R _ { \lambda }$ of $\ b { A } \in \mathbb { C } ^ { n \times n }$ is a rational function of λ with poles at the points of the spectrum of A and $R _ { \infty } = O .$ Moreover, each $\lambda _ { k } \in \sigma ( A )$ is a pole of $R _ { \lambda } o f$ order $m _ { k }$ , where $m _ { k }$ is the index of the eigenvalue $\lambda _ { k }$

PROOF. Let $\begin{array} { r } { m ( \lambda ) = \sum _ { i = 0 } ^ { m } \alpha _ { i } \lambda ^ { i } } \end{array}$ be the minimal polynomial of A. It is easily seen that

$$
\frac { m ( \lambda ) - m ( \mu ) } { \lambda - \mu } = \sum _ { i , j = 0 } ^ { m - 1 } \gamma _ { i j } \lambda ^ { i } \mu ^ { j } , \qquad \lambda \ne \mu ,
$$

for some $\gamma _ { i j } ( 1 \leq i , j \leq m - 1 )$ and therefore, substituting A for $\mu ,$ we have for $\lambda \not \in \sigma ( A )$

$$
( m ( \lambda ) I - m ( A ) ) R _ { \lambda } = \sum _ { j = 0 } ^ { m - 1 } { \binom { m - 1 } { i = 0 } } \lambda _ { i j } \lambda ^ { i } \Biggr ) A ^ { j } .
$$

Since $m ( A ) = 0 ;$ , it follows that, for the values of $\lambda$ for which $m ( \lambda ) \neq 0 ;$

$$
R _ { \lambda } = \frac { 1 } { m ( \lambda ) } \sum _ { j = 0 } ^ { m - 1 } m _ { j } ( \lambda ) A ^ { j } ,\tag{1}
$$

where $m _ { j } ( \lambda ) ( 0 \le j \le m - 1 )$ is a polynomial of degree not exceeding $m - 1$ The required results now follow from the representation (1).

Thus, using the terminology of complex analysis, the spectrum of a matrix can be described in terms of its resolvent. This suggests the application of results from complex analysis to the theory of matrices and vice versa. In the next theorem we use the classical Cauchy integral theorem to obtain its generalization for a matrix case, and this turns out to be an important and useful result in matrix theory.

First, let us agree to call a function $f ( \lambda )$ of the complex variable λ analytic on an open set of points D of the complex plane $\mathbf { i f } f ( \lambda )$ is continuously differentiable at every point of $D , \mathbf { O r } ,$ what is equivalent, $f ( \lambda )$ is analytic if it has a convergent Taylor series expansion about each point of $D . \operatorname { I f } f ( \lambda )$ is analytic within an open domain D bounded by a contour L and continuous on the closure ${ \overline { { D } } } ,$ then the Cauchy theorem asserts that

$$
f ^ { ( j ) } ( \lambda _ { 0 } ) = { \frac { j ! } { 2 \pi i } } \int _ { L } { \frac { f ( \lambda _ { 0 } ) } { ( \lambda - \lambda _ { 0 } ) ^ { j + 1 } } } d \lambda\tag{2}
$$

for any $\lambda _ { 0 } \in D$ and $j = 0 , 1 , \ldots$

Theorem 2. If $A \in \mathbb { C } ^ { n \times n }$ has distinct eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { s } .$ , the path L is a closed contour having $\lambda _ { 1 } , \ldots , \lambda _ { s }$ in its interior, and $f ( \lambda )$ is continuous in and on L and analytic within L, then

$$
f ( A ) = { \frac { 1 } { 2 \pi i } } \int _ { L } f ( \lambda ) ( \lambda I - A ) ^ { - 1 } ~ d \lambda = { \frac { 1 } { 2 \pi i } } \int _ { L } f ( \lambda ) R _ { \lambda } ~ d \lambda .\tag{3}
$$

PRooF. Use the representation of Exercise 9.5.2 for the resolvent and multiply both sides by $f ( \lambda ) ( 2 \pi i ) ^ { - 1 }$ . Applying formula (2) with $\lambda _ { 0 } = \lambda _ { k }$ $( 1 \leq k \leq s )$ and integrating along L, we obtain

$$
\frac { 1 } { 2 \pi i } \int _ { L } f ( \lambda ) ( \lambda I - A ) ^ { - 1 } ~ d \lambda = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } f ^ { ( j ) } ( \lambda _ { k } ) Z _ { k j } ,
$$

and the result follows from the spectral resolution of Theorem 9.5.1.■

Note that the relation (3) is an exact analog of (2) in the case $j = 0$ $( \lambda - \lambda _ { 0 } ) ^ { - 1 }$ is simply replaced by $( \lambda I - A ) ^ { - 1 }$ . It should also be remarked that (3) is frequently used as a definition of $f ( A )$ for analytic functions f(λ).

Corollary 1. With the notation of Theorem 2,

$$
I = \frac { 1 } { 2 \pi i } \int _ { L } R _ { \lambda } d \lambda , \quad \quad A = \frac { 1 } { 2 \pi i } \int _ { L } \lambda R _ { \lambda } d \lambda .
$$

The component matrices Zk of A can also be described in terms of the $Z _ { k j }$ resolvent of A.

Theorem 3. Preserving the previous notation, let $L _ { k }$ be a simple piecewise smooth closed contour that contains $\lambda _ { k } \in \sigma ( A )$ in its interior, and assume that no other points of the spectrum of A are inside or on $L _ { k }$ . Then

$$
Z _ { k j } = { \frac { 1 } { j ! 2 \pi i } } \int _ { L _ { k } } ( \lambda - \lambda _ { k } ) ^ { j } R _ { \lambda } d \lambda\tag{4}
$$

$$
f o r j = 0 , 1 , \ldots , m _ { k } - 1 ; k = 1 , 2 , \ldots , s .
$$

PRooF. Multiplying both sides of the equation in Exercise 9.5.2 by $( \lambda - \lambda _ { p } ) ^ { r }$ $( 1 \leq p \leq s , 0 \leq r \leq m _ { p } - 1 )$ and integrating around $L _ { p }$ , we obtain

$$
\int _ { L _ { p } } ( \lambda - \lambda _ { p } ) ^ { r } R _ { \lambda } d \lambda = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } j ! Z _ { k j } \int _ { L _ { p } } { \frac { ( \lambda - \lambda _ { p } ) ^ { r } } { ( \lambda - \lambda _ { k } ) ^ { j + 1 } } } d \lambda .\tag{5}
$$

The functions $( \lambda - \lambda _ { p } ) ^ { r } ( \lambda - \lambda _ { k } ) ^ { - j - 1 }$ with $k \neq p$ or with $k = p$ and $j \le r - 1$ are analytic in the domain bounded by $L _ { p }$ . Therefore the integrals of these functions around $L _ { p }$ are equal to zero. Now observe that for the remaining cases we have, in view of Eq. (2) for $f ( \lambda ) \equiv 1$

$$
\int _ { L _ { p } } ( \lambda - \lambda _ { p } ) ^ { r - j - 1 } d \lambda = { \left\{ \begin{array} { l l } { 2 \pi i } & { { \mathrm { i f } } \quad j = r , } \\ { 0 } & { { \mathrm { i f } } \quad j > r . } \end{array} \right. }
$$

Hence Eq. (5) implies

$$
\int _ { L _ { p } } ( \lambda - \lambda _ { p } ) ^ { r } R _ { \lambda } d \lambda = r ! Z _ { p r } ( 2 \pi i ) ,
$$

which is equivalent to (4).

We remark that, for those familiar with Laurent expansions, Eq. (4) expresses $Z _ { k j }$ as a coefficient of the Laurent expansion for the resolvent $R _ { \lambda }$ about the point $\lambda _ { k }$

Using the results of Theorems 9.5.2 and 9.5.4, and that of Theorem 3 for $j = 0$ , the following useful result is obtained (see also Theorem 9.6.1).

Theorem 4. With the previous notation, the integral

$$
P _ { k } = Z _ { k 0 } = { \frac { 1 } { 2 \pi i } } \int _ { L _ { k } } R _ { \lambda } d \lambda , \quad \quad 1 \leq k \leq s ,
$$

called the Riesz projector, is a projector. The system $\lbrace P _ { k } \rbrace _ { k = 1 } ^ { s }$ is an orthogonal system of projectors in the sense that $P _ { k } P _ { j } = 0$ for $k \neq j ,$ giving a spectral resolution of the identity matrix (with respect to A):

$$
I = \sum _ { k = 1 } ^ { s } P _ { k } \qquad a n d \qquad \mathrm { I m } P _ { k } = \mathrm { K e r } ( A - \lambda _ { k } I ) ^ { m _ { k } } ,
$$

where $m _ { k }$ is the index of the eigenvalue $\lambda _ { k }$ of A.

Exercise 5. Let $A \in \mathbb { C } ^ { n \times n }$ and $L _ { 0 }$ be a simple piecewise smooth closed contour. Show that

$$
\int _ { L _ { 0 } } R _ { \lambda } d \lambda = \sum _ { k = 1 } ^ { r } Z _ { k 0 }
$$

if $L _ { 0 }$ contains in its interior only the points $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { r }$ from the spectrum of A, and that the integral is the zero-matrix if there are no points of $\sigma ( A )$ inside $L _ { 0 }$

Exercise 6. Prove that, with the notation of Theorems 3 and 4,

$$
\lambda _ { k } Z _ { k 0 } + Z _ { k 1 } = A Z _ { k 0 } = \frac { 1 } { 2 \pi i } \int _ { L _ { k } } \lambda R _ { \lambda } d \lambda . \quad \sqcup
$$

Exercise 7 shows that, when $\lambda _ { k }$ is an eigenvalue of A of index 1, the projector $Z _ { k 0 }$ can easily be described in terms of the reduced adjoint $C ( \lambda )$ of A and the minimal polynomial $m ( \lambda )$ of A.

Exercise 7. Show that, if $\lambda _ { k }$ is an eigenvalue of A of index 1, then

$$
Z _ { k 0 } = \frac { 1 } { m ^ { ( 1 ) } ( \lambda _ { k } ) } C ( \lambda _ { k } ) .
$$

SoLUTION. Use Theorem 3 to write

$$
Z _ { k 0 } = { \frac { 1 } { 2 \pi i } } \int _ { L _ { k } } ( \lambda I - A ) ^ { - 1 } ~ d \lambda .
$$

Then use Exercise 7.9.1 to obtain

$$
Z _ { k 0 } = { \frac { 1 } { 2 \pi i } } \int _ { L _ { k } } { \frac { 1 } { m ( \lambda ) } } C ( \lambda ) d \lambda .
$$

Since the index of $\lambda _ { k }$ is 1, we have $m ( \lambda ) = ( \lambda - \lambda _ { j } ) m _ { 1 } ( \lambda )$ , where $m _ { 1 } ( \lambda _ { j } ) =$ $m ^ { ( 1 ) } ( \lambda _ { j } ) \neq 0$ Substitute this into the last displayed equation and use the theorem of residues to obtain the result.

Exercise 8. Let J be a matrix in Jordan normal form. Use Theorem 4 to show that the projectors $Z _ { k 0 }$ for J have the form diag $[ d _ { k 1 } , d _ { k 2 } , \ldots , d _ { k n } ]$ where $d _ { k i }$ is equal to 0 or 1 for $1 \leq k \leq s$ and $1 \leq i \leq n$ □

## 9.10 Applications to Differential Equations

Consider again the systems of differential equations with constant coefficients introduced in Section 4.13. We wish to find functions of time, x(t), with values in $\mathbb { C } ^ { n }$ satisfying the homogeneous equation

$$
\dot { { \mathbf { x } } } ( t ) = A { \mathbf { x } } ( t )\tag{1}
$$

or the nonhomogeneous equation

$$
{ \dot { \mathbf { x } } } ( t ) = A \mathbf { x } ( t ) + f ( t ) ,\tag{2}
$$

where $A \in \mathbb { C } ^ { n \times n }$ and $f ( t )$ is a prescribed function of time. We will now analyse these problems with no hypotheses on $A \in \mathbb { C } ^ { n \times n }$

It was seen in Section 4.13 that primitive solutions of the form $\pmb { x _ { 0 } } e ^ { \lambda _ { 0 } t }$ , where $\lambda _ { 0 }$ is an eigenvalue and $\mathbf { \boldsymbol { x } } _ { 0 }$ an associated eigenvector, play an important part.

More generally, we look for a solution of Eq. (1) in the form

$$
\begin{array} { r } { \pmb { x } ( t ) = \pmb { x } _ { 0 } ( t ) e ^ { \lambda _ { 0 } t } , \qquad \lambda _ { 0 } \in \mathbb { C } , } \end{array}\tag{3}
$$

where ${ \pmb x } _ { 0 } ( t )$ is a vector of order n whose coordinates are polynomials in t. For convenience we write ${ \pmb x } _ { 0 } ( t )$ in the form

$$
\pmb { x } _ { 0 } ( t ) = \frac { t ^ { k - 1 } } { ( k - 1 ) ! } \pmb { x } _ { 1 } + \cdots + \frac { t } { 1 ! } \pmb { x } _ { k - 1 } + \pmb { x } _ { k } ,\tag{4}
$$

where $\pmb { x } _ { i } \in \mathbb { C } ^ { n } , i = 1 , 2 , \ldots , k _ { 2 }$ and $\mathbf { x _ { 1 } }$ is assumed to be nonzero.

It is easily seen that x(t) in the form (3) is a solution of (1) if and only if

$$
\dot { { \mathbf x } } _ { 0 } ( t ) = ( A - \lambda _ { 0 } I ) { \mathbf x } _ { 0 } ( t ) ,
$$

where ${ \bf { x } } _ { 0 } ( t )$ is given by Eq. (4). By differentiation, we then have

$$
\begin{array} { r } { { \pmb x } _ { 0 } ^ { ( i ) } ( t ) = ( A - \lambda _ { 0 } I ) ^ { i } { \pmb x } _ { 0 } ( t ) , \qquad i = 1 , 2 , \ldots , } \end{array}\tag{5}
$$

and since ${ \bf { x } } _ { 0 } ( t )$ is a vector-valued polynomial of degree $k \mathrm { ~ - ~ } 1$ , it follows that $\pmb { \theta } = ( A - \lambda _ { 0 } I ) ^ { k } \pmb { x } _ { 0 } ( t )$

Now we find from Eq. (4) that $x _ { 0 } ^ { ( k - 1 ) } ( t ) = x _ { 1 }$ , and comparing this with Eq. (5), $x _ { 1 } = ( A - \lambda _ { 0 } I ) ^ { k - 1 } x _ { 0 } ( t )$ . Multiplying on the left by $( A - \lambda _ { 0 } I )$ we obtain $( A - \lambda _ { 0 } I ) { \pmb x } _ { 1 } = { \pmb \theta } ,$ and since $\pmb { x } _ { 1 } \neq \pmb { \theta }$ by hypothesis, $\bf { x _ { 1 } }$ is an eigenvector of A corresponding to the eigenvalue $\lambda _ { 0 }$

Now compare the (k - 2)nd derivative of ${ \pmb x } _ { 0 } ( t )$ calculated from Eqs. (4) and (5) to get

$$
t x _ { 1 } + x _ { 2 } = ( A - \lambda _ { 0 } I ) ^ { k - 2 } x _ { 0 } ( t ) .
$$

Multiply on the left by $( A - \lambda _ { 0 } I )$ , and use the results of the preceding paragraph to get $( A - \lambda _ { 0 } I ) \mathbf { x } _ { 2 } = \mathbf { x } _ { 1 }$ . Thus, (see Eqs. (6.3.3)) $\mathbf { \delta x } _ { 1 } , \mathbf { \delta x } _ { 2 }$ form a Jordan chain of length 2.

Proceeding in the same way, it is found that $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { k }$ form a Jordan chain for A associated with $\lambda _ { 0 }$ . A similar argument shows that if $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { k }$ generate a Jordan chain for A corresponding to the eigenvalue $\lambda _ { 0 }$ , then Eq. (3) along with Eq. (4) gives a solution of Eq. (1). Thus, we have proved the following.

Proposition 1. The function x(t) defined by Eqs. (3) and (4) is a solution of Eq. (1) if and only if $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { k }$ constitute a Jordan chain for A associated with the eigenvalue $\lambda _ { 0 }$ of A.

Now recall that, by Theorem 7.10.1, the dimension of the solution space $\mathcal { f }$ of Eq. (1) is n and by the Jordan theorem, there is a basis in $\mathbb { C } ^ { n }$ consisting entirely ofeigenvectors and generalized eigenvectors of A. Hence the following result is clear.

Theorem 1. Let $A \in \mathbb { C } ^ { n \times n }$ and let $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ be the distinct eigenvalues of A of algebraic multiplicity $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { s } .$ , respectively. If the Jordan chains for $\lambda _ { k } \left( 1 \leq k \leq s \right)$ are

$$
\begin{array} { c c c c c } { { \pmb x _ { 1 1 } ^ { ( k ) } , } } & { { { \pmb x _ { 1 2 } ^ { ( k ) } } , } } & { { \ldots , } } & { { { \pmb x _ { 1 v _ { k 1 } } ^ { ( k ) } } , } } \\ { { \pmb x _ { 2 1 } ^ { ( k ) } , } } & { { { \pmb x _ { 2 2 } ^ { ( k ) } } , } } & { { \ldots , } } & { { { \pmb x _ { 2 v _ { k 2 } } ^ { ( k ) } } , } } \\ { { \vdots } } & { { } } & { { } } & { { } } \\ { { \pmb x _ { r _ { k , 1 } } ^ { ( k ) } } } & { { { \pmb x _ { r _ { k , 2 } } ^ { ( k ) } } } } & { { \ldots , } } & { { { \pmb x _ { r _ { k , \mathrm { r } _ { k , r _ { k } } } } ^ { ( k ) } } } } \end{array}
$$

where $\sum _ { i = 1 } ^ { r _ { k } } \nu _ { k i } = \alpha _ { k }$ , then any solution ${ \pmb x } ( t ) o f ( l )$ is a linear combination of the n vector-valued functions

$$
\bigg [ \frac { t ^ { j - 1 } } { ( j - 1 ) ! } \pmb { x } _ { i 1 } ^ { ( k ) } + \cdots + \frac { t } { 1 ! } \pmb { x } _ { i , j - 1 } ^ { ( k ) } + \pmb { x } _ { i j } ^ { ( k ) } \bigg ] e ^ { \lambda _ { k } t } ,\tag{6}
$$

where $j = 1 , 2 , \ldots , \nu _ { k i } , i = 1 , 2 , \ldots r _ { k } , k = 1 , 2 , \ldots , s .$

In other words, the expressions in (6) form a basis in the solution space S of $\mathcal { S }$ (1) and therefore are referred to as the fundamental solutions of (1). Note also that $\lambda _ { k }$ has geometric multiplicity $r _ { k }$ and $\mathbf { \boldsymbol { x } } _ { 1 1 } ^ { ( k ) } , \mathbf { \boldsymbol { x } } _ { 2 1 } ^ { ( k ) } , \ldots , \mathbf { \boldsymbol { x } } _ { r _ { k } 1 } ^ { ( k ) }$ span Ker $( A - \lambda _ { k } I )$

Exercise 1. Find the general form of the solutions (the general solution) of the system

$$
\dot { { \pmb x } } ( t ) = \left[ \dot { { \dot { \boldsymbol x } } } _ { 1 } \right] = \left[ \begin{array} { c c c } { 6 } & { 2 } & { 2 } \\ { - 2 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 2 } \end{array} \right] \left[ \begin{array} { c } { { \boldsymbol x } _ { 1 } } \\ { { \boldsymbol x } _ { 2 } } \\ { { \boldsymbol x } _ { 3 } } \end{array} \right] = { \pmb A } { \pmb x } ( t ) .
$$

SoLUTION. It was found in Exercise 6.5.2 that the matrix A has an eigenvalue $\lambda _ { 1 } = 2$ with an associated eigenvector $[ 0 \ - 1 \ \mathrm { ~ \ } 1 ] ^ { \mathfrak { r } }$ and an eigenvalue $\lambda _ { 2 } = 4$ associated with the eigenvector $[ 2 \ - 2 0 ] ^ { \mathbf { r } }$ and generalised eigenvector ${ \begin{array} { l l l } { [ 1 } & { 0 } & { 0 ] ^ { \mathbf { T } } } \end{array} }$ , Hence the general solution, according to (6), is given by

$$
{ \pmb x } ( t ) = \beta _ { 1 } \left[ - 1 \right] e ^ { 2 t } + \beta _ { 2 } \left[ - 2 \right] e ^ { 4 t } + \beta _ { 3 } \left( \left[ - 2 \right] t + \left[ 0 \right] \right) e ^ { 4 t } . \bigstar \square\tag{7}
$$

It is frequently the case that a particular solution of (1) is required that is specified by additional conditions. The initial-value problems are of this kind, in which a vector $\ b { x _ { 0 } } \in \mathbb { C } ^ { n }$ is given and a solution ${ \boldsymbol x } ( t )$ of (1) is to be found, where ${ \boldsymbol x } ( t )$ takes the value $\mathbf { \delta x } _ { 0 }$ at $t = 0$

Theorem 2. Let $A \in \mathbb { C } ^ { n \times n }$ . There is a unique $\mathbf { \boldsymbol { x } } ( t )$ such that

$$
{ \dot { \pmb { x } } } ( t ) = { \pmb { A } } { \pmb { x } } ( t ) \qquad { \pmb { a n d } } \qquad { \pmb { x } } ( 0 ) = { \pmb { x } } _ { 0 }\tag{8}
$$

for any given vector $\pmb { x } _ { 0 } \in \mathbb { C } ^ { n }$

PRooF. By Theorem 1 any solution x(t) of (1) is a linear combination of the n expressions $\mathbf { x } _ { p } ( t ) ( p = 1 , 2 , \ldots , n )$ of the form (6);

$$
{ \bf x } ( t ) = \sum _ { p = 1 } ^ { n } \beta _ { p } { \bf x } _ { p } ( t ) .
$$

Observe that $\mathbf { \boldsymbol { x } } _ { p } ( 0 ) , p = 1 , 2 , \ldots , n ,$ gives the vectors of the Jordan basis of A in $\mathbb { C } ^ { n } { } _ { i }$ , and therefore the matrix $B = [ { \pmb x } _ { 1 } ( 0 ) \mathrm { ~ } { \pmb x } _ { 2 } ( 0 ) \mathrm { ~ } \cdot \cdot \cdot \mathrm { ~ } { \pmb x } _ { n } ( 0 ) ]$ is nonsingular. Thus, the system

$$
\sum _ { p = 1 } ^ { n } \beta _ { p } { \bf x } _ { p } ( 0 ) = { \bf x } _ { 0 }
$$

or in matrix form $B { \boldsymbol { \mathbf { \beta } } } = { \boldsymbol { \mathbf { \nu } } } _ { 0 }$ with $\mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta \beta } \mathbf \mathbf { \beta } \mathbf { \beta } \mathbf { \beta \mathbf } \mathbf { \beta \beta } \mathbf \mathbf { \beta } \mathbf { \beta \mathbf } \mathbf  \beta \mathbf { \beta } \mathbf \mathbf { \beta } \mathbf \mathbf { \beta } \mathbf \mathbf { \beta \beta } \mathbf \mathbf \mathbf { \beta } \mathbf \mathbf \mathbf { \beta \beta \mathbf } \mathbf \mathbf  \beta \mathbf \mathbf \beta \mathbf { } \mathbf \mathbf \mathbf \mathbf { \beta } \mathbf \mathbf \mathbf \mathbf { \beta \beta \mathbf \mathbf } \mathbf \mathbf \mathbf \mathbf { \mathbf \beta \mathbf \mathbf \mathbf \mathbf \beta \mathbf } $ , has a unique solution for every $\pmb { x } _ { 0 } \in \mathbb { C } ^ { n } .$

Exercise 2. Find the solution of the system considered in Exercise 1 that satisfies the condition $\mathbf { x } ( 0 ) = [ 0 \quad 1 \quad 1 ] ^ { \mathbf { T } }$

SOLUTION. It is easily seen that by putting $t = 0$ in Eq. (7) we obtain a linear system

$$
{ \begin{array} { r r r } { { \left[ \begin{array} { l l l } { 0 } & { 2 } & { 1 } \\ { - 1 } & { - 2 } & { 0 } \\ { 1 } & { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l } { \beta _ { 1 } } \\ { \beta _ { 2 } } \\ { \beta _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 1 } \end{array} \right] } } \end{array} }
$$

with an invertible coefficient matrix. The vector $\begin{array} { r l } { [ \beta _ { 1 } } & { { } \beta _ { 2 } \quad \beta _ { 3 } ] ^ { \mathtt { T } } } \end{array}$ is found to be $[ 1 ~ - 1 ~ 2 ] ^ { \mathtt { T } }$ and therefore the required solution is

$$
{ \pmb x } ( t ) = \left[ - 1 _ { 1 } ^ { 0 } \right] e ^ { 2 t } + \left( \left[ 2 _ { 2 } \right] + \left[ - 4 _ { 0 } ^ { 4 } \right] t \right) e ^ { 4 t } . \quad \sqcup _ { 0 }
$$

Now we show how the solution of (8) can be found by use of the notion of a function of A. Start by using the idea in the beginning of the section but applying it directly to the matrix differential equation $\dot { \pmb { x } } = \pmb { A } \pmb { x }$ . We look for solutions in the form $e ^ { A t } z$ with $z \in \mathbb { C } ^ { n }$ . Exercise 9.9.1 clearly shows that the vector-valued function ${ \bf x } ( t ) = e ^ { { \bf A } t } { \bf z }$ is a solution of (1) for any $z \in \mathbb { C } ^ { n }$

$$
{ \dot { \pmb { x } } } ( t ) = { \frac { d } { d t } } e ^ { { \pmb { A } } t } { \pmb { z } } = { \pmb { A } } e ^ { { \pmb { A } } t } { \pmb { z } } = { \pmb { A } } { \pmb { x } } ( t ) .
$$

Obviously ${ \bf { x } } ( t ) = e ^ { { \bf { A } } t } { \bf { z } }$ satisfies the initial condition ${ \pmb x } ( 0 ) = { \pmb x } _ { 0 }$ if and only if $\mathbf { \mu } _ { z } = \mathbf { \mu } _ { \mathbf { x _ { 0 } } }$ . Thus, using Theorem 2, we find the following.

Theorem 3. The unique solution of the problem (8) can be written in the form

$$
\begin{array} { r } { { \bf x } ( t ) = e ^ { \boldsymbol { A } t } { \bf x } _ { 0 } . } \end{array}\tag{9}
$$

Let $\mathbf { \boldsymbol { x } } ( t )$ be a solution of (1). Computing $\mathbf { \boldsymbol { x } } ( 0 )$ , we see from Theorem 3 that ${ \bf x } ( t ) = e ^ { A t } { \bf x } ( 0 )$ . Hence we have a further refinement.

Theorem 4. Any solution x(t) of (1) can be represented in the form ${ \bf \boldsymbol { x } } ( t ) = e ^ { \boldsymbol { A } t } { \bf \boldsymbol { z } }$ for some $z \in \mathbb { C } ^ { n }$

It is a remarkable and noteworthy fact that all the complications of Theorem 1 can be streamlined into the simple statement of Theorem 4. This demonstrates the power of the “functional calculus" developed in this chapter.

Another representation for solutions of (1) is derived on putting $f ( \lambda ) = e ^ { \lambda }$ in Theorem 9.5.1 and using the spectral resolution for $e ^ { A t }$ . Hence, denoting ${ \bf { x } } ( 0 ) = { \bf { x } } _ { 0 }$ , we use Theorem 3 to derive

$$
\qquad \mathbf { x } ( t ) = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } Z _ { k j } t ^ { j } e ^ { \lambda _ { k } t } \pmb { x } _ { 0 } = \sum _ { k = 1 } ^ { s } ( z _ { k 0 } + z _ { k 1 } t + \cdot \cdot \cdot + z _ { k , m _ { k } - 1 } t ^ { m _ { k } - 1 } ) e ^ { \lambda _ { k } t } ,
$$

where $z _ { k j } = Z _ { k j } \mathbf { x } _ { 0 }$ and is independent of t. Thus, we see again that the solution is a combination of polynomials in t with exponential functions. If A is a simple matrix, the solution reduces to

$$
{ \bf { x } } ( t ) = \sum _ { k = 1 } ^ { s } z _ { k 0 } e ^ { \lambda _ { k } t } ,
$$

and we see that each element of $x ( t )$ is a linear combination of exponential functions with no polynomial contributions (see Section 4.13).

Exercise 3. By means of component matrices, find the solution of the initialvalue problem discussed in Exercise 2. □

Finally, consider the inhomogeneous Eq. (2) in which the elements of fare prescribed piecewise-continuous functions $f _ { 1 } ( t ) , \ldots , f _ { n } ( t )$ of t that are not all identically zero. Let $\mathcal { S }$ be the space of all solutions of the associated homogeneous problem ${ \dot { \pmb { x } } } = A { \pmb { x } }$ and let $\mathcal { T }$ be the set of all solutions of ${ \dot { \pmb { x } } } = { \boldsymbol { A } } { \pmb { x } } + { \pmb { f } } .$ If we are given just one solution ${ \boldsymbol { \mathbf { \mathit { y } } } } \in { \mathcal { T } } ,$ then (compare with Theorem $3 . 1 0 . 2 ) \ z \in \mathcal { T }$ if and only if ${ \pmb z } = { \pmb y } + { \pmb w }$ for some ${ \pmb w } \in \mathcal { S }$ The verification of this result is left as an exercise. Thus, to obtain $\mathcal { T }$ we need to know just one solution of the inhomogeneous equation, known as a particular integral, and add to it all the solutions of the homogeneous equation, each of which we express in the form $e ^ { A t } { \bf x }$ for some $\ b { x } \in C ^ { n }$

We look for a solution of ${ \dot { \pmb { x } } } = { \boldsymbol { A } } { \pmb { x } } + { \pmb { f } }$ in the form

$$
\pmb { x } ( t ) = e ^ { A t } \pmb { z } ( t ) .
$$

If there is such a solution, then $\dot { \pmb { x } } = A \pmb { x } + e ^ { A t } \dot { \pmb { z } }$ and so $e ^ { A t } \dot { \bar { z } } = f ,$ hence

$$
z ( t ) = e ^ { - A t _ { 0 } } \mathbf { x } _ { 0 } + \int _ { t _ { 0 } } ^ { t } e ^ { - A \tau } f ( \tau ) d \tau ,
$$

where $\mathbf { x } _ { 0 } = e ^ { \mathbf { A } t _ { 0 } } \mathbf { z } ( t _ { 0 } ) = \mathbf { x } ( t _ { 0 } )$ . This suggests that

$$
\begin{array} { l } { { \displaystyle { \pmb x } ( t ) = e ^ { A t } \bigg ( e ^ { - A t _ { 0 } } { \pmb x } _ { 0 } + \int _ { t _ { 0 } } ^ { t } e ^ { - A \tau } { \pmb f } ( \tau ) d \tau \bigg ) } } \\ { { \displaystyle ~ = e ^ { A ( t - t _ { 0 } ) } { \pmb x } _ { 0 } + \int _ { t _ { 0 } } ^ { t } e ^ { A ( t - \tau ) } { \pmb f } ( \tau ) d \tau } } \end{array}
$$

is the solution of ${ \dot { \pmb { x } } } = { \boldsymbol { A } } { \pmb { x } } + { \pmb { f } } ,$ where ${ \pmb x } ( t _ { 0 } ) = { \pmb x } _ { 0 }$ . This is easily verified.

Theorem 5. If $\pmb { f } ( t )$ is a piecewise-continuous function of t with values in $\mathbb { C } ^ { n } , t _ { 0 } \in R ,$ and $A \in \mathbb { C } ^ { n \times n }$ , then every solution of the differential equation

$$
{ \dot { \mathbf { x } } } ( t ) = A \mathbf { x } ( t ) + \mathbf { \nabla } f ( t )
$$

has the form

$$
{ \pmb x } ( t ) = e ^ { { \pmb A } ( t - t _ { 0 } ) } { \pmb x } _ { 0 } + \int _ { t _ { 0 } } ^ { t } e ^ { { \pmb A } ( t - \tau ) } { \pmb f } ( \tau ) d \tau ,\tag{10}
$$

and ${ \boldsymbol x } _ { 0 } = { \boldsymbol x } ( t _ { 0 } )$

Exercise 4. Find the solution of ${ \dot { \pmb { x } } } = { \boldsymbol { A } } { \pmb { x } } + { \pmb { f } } ,$ with ${ \pmb x } ( 0 ) = { \pmb x } _ { 0 }$ , if A and $\bf { { x _ { 0 } } }$ are as defined in Exercises 1 and 2 and

$$
\begin{array} { r } { f = \left[ \begin{array} { c } { a e ^ { 4 t } } \\ { 0 } \\ { 0 } \end{array} \right] = a e ^ { 4 t } e _ { 1 } . } \end{array}
$$

SOLUTION. The vector $e ^ { \boldsymbol { A } t } \mathbf { x } _ { 0 }$ is known from Exercise 1. Using Eq. (9.5.1) to find the particular integral, we have

$$
y ( t ) = \int _ { 0 } ^ { t } e ^ { A ( t - \tau ) } f ( \tau ) d \tau = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } Z _ { k j } \int _ { 0 } ^ { t } ( t - \tau ) ^ { j - 1 } e ^ { \lambda _ { k } ( t - \tau ) } f ( \tau ) d \tau .
$$

The integrals

$$
a \int _ { 0 } ^ { t } e ^ { 4 ( t - \tau ) } e ^ { 4 \tau } d \tau , \qquad a \int _ { 0 } ^ { t } ( t - \tau ) e ^ { 4 ( t - \tau ) } e ^ { 4 \tau } d \tau , \qquad a \int _ { 0 } ^ { t } e ^ { 2 ( t - \tau ) } e ^ { 4 \tau } d \tau
$$

are easily found to be $a t e ^ { 4 t } , { \textstyle \frac { 1 } { 2 } } a t ^ { 2 } e ^ { 4 t }$ , and $\scriptstyle { \frac { 1 } { 2 } } a e ^ { 2 t } ( e ^ { 2 t } - 1 )$ , respectively. Hence

$$
\begin{array} { l } { { y ( t ) = a t e ^ { 4 t } Z _ { 1 0 } e _ { 1 } + \frac { 1 } { 2 } a t ^ { 2 } e ^ { 4 t } Z _ { 1 1 } e _ { 1 } + \frac { 1 } { 2 } a e ^ { 2 t } ( e ^ { 2 t } - 1 ) Z _ { 2 0 } e _ { 1 } } } \\ { { \ } } \\ { { = \frac { 1 } { 2 } a t e ^ { 4 t } \left( 2 \left[ \begin{array} { c } { { 1 } } \\ { { 0 } } \\ { { 0 } } \end{array} \right] + t \left[ \begin{array} { c } { { 2 } } \\ { { - 2 } } \\ { { 0 } } \end{array} \right] \right) = \left[ \begin{array} { c } { { a ( 1 + t ) t e ^ { 4 t } } } \\ { { - a t ^ { 2 } e ^ { 4 t } } } \\ { { 0 } } \end{array} \right] . } } \end{array}
$$

The solutionis then given by $\mathbf { } \mathbf { x } ( t ) = e ^ { \mathbf { A } t } \mathbf { x } _ { 0 } + \mathbf { y } ( t )$

Exercise 5. Let A be nonsingular and $\pmb { \beta } = \pmb { A } ^ { - 1 } \pmb { b }$ , where $\pmb { b } \in \mathbb { C } ^ { n }$ Show that if $\mathbf { \boldsymbol { x } } ( t )$ is a solution of ${ \dot { \mathbf { x } } } ( t ) = A { \mathbf { x } } ( t ) - b ,$ then

$$
\displaystyle \mathbf { \boldsymbol { x } } ( t ) - \mathbf { \boldsymbol { \beta } } = e ^ { A t } ( \mathbf { \boldsymbol { x } } ( 0 ) - \mathbf { \boldsymbol { \beta } } ) .
$$

(Here $\beta$ is the steady-state solution of the differential equation.)

Exercise 6. Let $A \in \mathbb { C } ^ { n \times n }$ and let a sequence of vectors $f _ { 0 } , f _ { 1 } , \ldots$ in $\mathbb { C } ^ { n }$ be given. Show that any solution of the difference equation

$$
{ \pmb x } _ { r + 1 } = A { \pmb x } _ { r } + { \pmb f } _ { r } , \qquad r = 0 , 1 , 2 , \ldots ,
$$

can be expressed in the form $\mathbf { \delta x } _ { 0 } = \mathbf { \delta z }$ and, for $j = 1 , 2 , \dots$

$$
{ \bf x } _ { j + 1 } = A ^ { j } z + \sum _ { k = 0 } ^ { j - 1 } A ^ { j - k - 1 } f _ { k } ,
$$

for some $\pmb { z } \in \mathbb { C } ^ { n } . \quad \square$

## 9.11 Observable and Controllable Systems

In this section we bring together several important results developed in this and earlier chapters. This will allow us to present some interesting ideas and results from the theory of systems and control.

Let $A \in \mathbb { C } ^ { n \times n }$ and $C \in \mathbb { C } ^ { r \times n }$ and consider the system of equations

$$
\begin{array} { r l } { \dot { \mathbf { x } } ( t ) = A \mathbf { x } ( t ) , \quad } & { { } \mathbf { x } ( 0 ) = \mathbf { x } _ { 0 } , } \\ { \mathbf { y } ( t ) = C \mathbf { x } ( t ) . } \end{array}\tag{1}
$$

Thus $\mathbf { \boldsymbol { x } } ( t )$ has values in $\mathbb { C } ^ { n }$ determined by the initial-value problem (supposing $\mathbf { x } _ { 0 } \in \mathbb { C } ^ { n }$ is given) and is called the state vector. Then $\mathbf { y } ( t ) \in \mathbb { C } ^ { r }$ for each $t \geq 0$ and is the observed or output vector. It represents the information about the state of the system that can be recorded after “filtering" through the matrix C. The system (1) is said to be observable if $\boldsymbol { y } ( t ) \equiv \boldsymbol { \theta }$ occurs only when $\mathbf { \boldsymbol { x } } _ { 0 } = \mathbf { \boldsymbol { \theta } }$ Thus, for the system to be observable all nonzero initial vectors must give rise to a solution which can be observed, in the sense that the output vector is not identically zero.

The connection with observable pairs, as introduced in Section 5.13, is established by the first theorem. For convenience, write

$$
Q = Q ( C , A ) = \left[ \begin{array} { c } { { C } } \\ { { C A } } \\ { { \vdots } } \\ { { C A ^ { n - 1 } } } \end{array} \right] ,
$$

a matrix of size $n r \times n .$

Theorem 1. The system (1) is observable if and only if Ker $Q ( C , A ) = \{ \pmb { 0 } \}$ that is, if and only if the pair $( C , A )$ is observable.

Before proving the theorem we establish a technical lemma that will simplify subsequent arguments involving limiting processes. An entire function is one that is analytic in the whole complex plane; the only possible singularity is at infinity.

Lemma 1. For any matrix $A \in \mathbb { C } ^ { n \times n }$ there exist entire functions $\psi _ { 1 } ( t )$ $\ldots , \psi _ { n } ( t )$ such that

$$
e ^ { A t } = \sum _ { j = 1 } ^ { n } \psi _ { j } ( t ) A ^ { j - 1 } .\tag{2}
$$

PRoOF. Let $f ( \lambda ) = e ^ { \lambda t }$ ; then f is an entire function of λ that is defined on the spectrum of any n × n matrix A. Since $f ^ { ( j ) } ( \lambda ) = t ^ { j } e ^ { \lambda t }$ , it follows from Theorem 9.5.1 that

$$
f ( A ) = e ^ { A t } = \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } t ^ { j } e ^ { \lambda _ { k } t } Z _ { k j } .\tag{3}
$$

Since $Z _ { k j } = \varphi _ { k j } ( A )$ for each $k , j$ and $\varphi _ { k j }$ is a polynomial whose degree does not exceed n [see the discussion preceding Eqs. (9.2.6) and (9.2.7)], and because the ø: depend only on A, the right-hand term in Eq. (3) can be rearranged $\varphi _ { k j }$ as in Éq. (2). Furthermore, each coefficient ψ (t) is just a linear combination $\psi _ { j } ( t )$ of functions of the form $t ^ { j } e ^ { \lambda _ { k } t }$ and is therefore entire.■

PROOF OF THEOREM 1. If Ker $Q ( C , A ) \neq \{ \pmb { 0 } \}$ then there is a nonzero $\mathbf { \boldsymbol { x } } _ { 0 }$ such that $C A ^ { j } \mathbf { x } _ { 0 } = \pmb { 0 }$ for $j = 0 , 1 , \ldots , n - 1$ . It follows from Lemma 1 that $C e ^ { 4 t } \pmb { x } _ { 0 } = \pmb { 0 }$ for any real t. But then Theorem 9.10.3 and Eqs. (1) yield

$$
\mathbf { y } ( t ) = C e ^ { A t } \mathbf { x } _ { 0 } \equiv \pmb { \theta }
$$

and the system is not observable. Thus, if the system is observable, the pair $( C , A )$ must be observable.

Conversely, if the system is not observable, there is an $\mathbf { \boldsymbol { x } } _ { 0 } \neq \mathbf { \boldsymbol { \theta } }$ such that $\mathbf { y } ( t ) = C e ^ { A t } \mathbf { x } _ { 0 } \equiv \pmb { \theta }$ . Differentiating repeatedly with respect to t, it is found that

$$
Q ( C , A ) e ^ { A t } x _ { 0 } \equiv \pmb { \theta }
$$

and Ker $Q ( C , A ) \neq \{ \pmb { 0 } \}$ . Consequently, observability of the pair $( C , A )$ must imply observability of the system.

It has been seen in Section 5.13 that there is a notion of “controllability" of matrix pairs that is dual to that of observability. We now develop this

notion in the context of systems theory. Let $A \in \mathbb { C } ^ { n \times n }$ and $B \in \mathbb { C } ^ { n \times m }$ and consider a differential equation with initial condition

$$
{ \dot { \mathbf { x } } } ( t ) = A { \mathbf { x } } ( t ) + B u ( t ) , \qquad { \mathbf { x } } ( 0 ) = { \mathbf { x } } _ { 0 } .\tag{4}
$$

Consistency demands that $\ b { x } ( t ) \in \mathbb { C } ^ { n }$ and $\pmb { u } ( t ) \in \mathbb { C } ^ { m }$ for each t. We adopt the point of view that $\pmb { u } ( t )$ is a vector function, called the control, that can be used to guide, or control, the solution ${ \boldsymbol x } ( t )$ of the resulting initial-value problem to meet some objective. The objective that we consider is that of controlling the solution ${ \boldsymbol x } ( t )$ in such a way that after some time t, the function $\pmb { x } ( t )$ takes some preassigned vector value in $\mathbb { C } ^ { n } .$

To make these ideas precise we first define a class of admissible control functions $\pmb { u } ( t )$ . We define ${ \mathcal { U } } _ { m }$ to be the linear space of all $\mathbb { C } ^ { m } .$ -valued functions that are defined and piecewise continuous on the domain $t \geq 0 ,$ and we assume that $\pmb { u } ( t ) \in \mathcal { U } _ { m }$ . Then observe that, using Eq. (9.10.10), when $\pmb { u } ( t ) \in \mathcal { U } _ { m }$ is chosen, the solution of our initial-value problem can be written explicitly in the form

$$
x ( t ; x _ { 0 } , u ) = e ^ { A t } x _ { 0 } + \int _ { 0 } ^ { t } e ^ { ( t - s ) A } B u ( s ) d s .\tag{5}
$$

The purpose of the complicated notation on the left is to emphasize the dependence of the solution x on the control function u and the initial value $\pmb { x } _ { 0 }$ , as well as on the independent variable t.

A vector $\boldsymbol { y } \in \mathbb { C } ^ { n }$ is said to be reachable from the initial vector $\mathbf { \boldsymbol { x } } _ { 0 }$ if there is a $\pmb { u } ( t ) \in \mathcal { U } _ { m }$ such that $\mathbf { x } ( t ; \mathbf { x } _ { 0 } , { \pmb u } ) = \mathbf { y }$ for some positive time t. Under the same condition we may say that y is reachable from $\mathbf { \delta x } _ { 0 }$ in time t.

The system of Eq. (4) is said to be controllable (in contrast to controllability of a matrix pair) if every vector in $\mathbb { C } ^ { n }$ is reachable from every other vector in $\mathbb { C } ^ { n } .$ Our next major objective is to show that the system (4) is controllable if and only if the pair (A, B) is controllable, and this will follow easily from the next result.

Recall first that the controllable subspace of (A, B), which we will denote $\mathcal { C } _ { A , B }$ , is given by

$$
\mathcal { C } _ { A , B } = \sum _ { r = 0 } ^ { n - 1 } \operatorname { I m } ( A ^ { r } B ) .\tag{6}
$$

(See Corollary 1(d) of Theorem 5.13.1.)

Theorem 2. The vector $z \in \mathbb { C } ^ { n }$ is reachable from $\pmb { y } \in \mathbb { C } ^ { n }$ in time t if and only if

$$
{ \boldsymbol { z } } \mathbin { - } e ^ { A t } \mathbf { y } \in \mathcal { C } _ { A , B } .
$$

The proof will be broken down with the help of another lemma, which provides a useful description of the controllable subspace of $( A , B )$

Lemma 2. The matrix-valued function $W ( t )$ defned by

$$
W ( t ) = \int _ { 0 } ^ { t } e ^ { A s } B B ^ { * } e ^ { A ^ { * } s } d s\tag{7}
$$

has the property that, for any $t > 0 ,$ Im $W ( t ) = { \mathcal { C } } _ { A , B }$

PROOF. Clearly, $W ( t )$ is Hermitian for each $t > 0$ and hence [see Eq. (5.8.5)]

$$
\operatorname { I m } W ( t ) = ( \operatorname { K e r } W ( t ) ) ^ { \perp } .
$$

Also (see Eq. 5.13.5), if $\mathcal { K } _ { A , B }$ denotes the unobservable subspace of $( B ^ { * } , A ^ { * } )$ then

$$
\mathcal { C } _ { A , B } = ( \mathcal { K } _ { A , B } ) ^ { \perp } .
$$

Thus, the conclusion of the lemma is equivalent to the statement Ker W(t) $= \mathcal { K } _ { A , B }$ and we shall prove it in this form.

If $\mathbf { \boldsymbol { x } } \in \mathbf { \mathbb { K } }$ er W(t) then

$$
x ^ { * } W ( t ) x = \int _ { 0 } ^ { t } \lVert B ^ { * } e ^ { A ^ { * } s } x \rVert ^ { 2 } d s = 0 ;
$$

here the Euclidean vector norm is used. Hence, for all $s \in [ 0 , t ]$

$$
B ^ { * } e ^ { A ^ { * } s } x = 0 .
$$

Differentiate this relation with respect to s repeatedly and take the limit as $s \to 0 _ { + }$ to obtain

$$
B ^ { * } ( A ^ { * } ) ^ { j - 1 } x = 0 \qquad \mathrm { f o r } \quad j = 1 , 2 , \ldots , n .
$$

In other words,

$$
\pmb { x } \in \bigcap _ { j = 1 } ^ { n } \operatorname { K e r } ( B ^ { * } ( A ^ { * } ) ^ { j - 1 } ) = \pmb { \mathcal { M } } _ { A , B } .
$$

Thus Ker $W ( t ) \subset \mathcal { K } _ { A , B }$ . It is easy to verify that, reversing the argument and using Lemma 1, the opposite inclusion is obtained. So Ker $W ( t ) = \mathcal { K } _ { A , B }$ and the lemma is proved.■

This lemma yields another criterion for controllability of the pair $( A , B )$

Corollary 1. The pair $( A , B )$ is controllable if and only if the matrix W(t) of Eq. (7) is positive definite for all $t > 0$

ProoF. It is clear from definition (7) that $W ( t )$ is at least positive semidefinite. However, for $( A , B )$ to be controllable means that $\mathcal { C } _ { A , B } = \mathbb { C } ^ { n } ;$ and so Lemma 2 implies that Im $W ( t ) = \mathbb { C } ^ { n }$ . Hence $W ( t )$ has rank n and is therefore positive definite.■

PROOF OF THEOREM 2. If z is reachable from y in time t, then, using $t ,$ Eq. (5),

$$
z - e ^ { A t } y = \int _ { 0 } ^ { t } e ^ { ( t - s ) A } B u ( s ) d s
$$

for some $\pmb { u } \in \mathcal { U } _ { m }$ . Use Lemma 1 to write

$$
z - e ^ { A t } y = \sum _ { j = 1 } ^ { n } A ^ { j - 1 } B \int _ { 0 } ^ { t } \psi _ { j } ( t - s ) u ( s ) d s ,
$$

and, using definition (6), it is seen immediately that $\mathbf { \delta } \mathbf { z } \mathrm { ~ - ~ } e ^ { \boldsymbol { A } t } \mathbf { y } \in \mathcal { C } _ { \boldsymbol { A } , \boldsymbol { B } }$

For the converse, let $\mathbf { \delta } \mathbf { z } \mathrm { ~ - ~ } e ^ { \boldsymbol { A } t } \mathbf { y } \in \mathcal { C } _ { \boldsymbol { A } , \boldsymbol { B } }$ . We are to construct an input, or control, u(t) that will “steer" the system from y to z. Use Lemma 2 to write ${ \pmb u } ( t )$

$$
z - e ^ { A t } y = W ( t ) w = \int _ { 0 } ^ { t } e ^ { A s } B B ^ { * } e ^ { A ^ { * } s } w ~ d s
$$

for some $\pmb { w } \in \mathbb { C } ^ { n } ,$ Put $s = t - \tau$ to obtain

$$
z - e ^ { A t } y = \int _ { 0 } ^ { t } e ^ { A ( t - \tau ) } B B ^ { * } e ^ { A ^ { * } ( t - \tau ) } w d \tau = \int _ { 0 } ^ { t } e ^ { A ( t - \tau ) } B u ( \tau ) d \tau ,
$$

where we define $u ( \tau ) = B ^ { * } e ^ { A ^ { * } ( t - \tau ) } w \in \mathcal { U } _ { m }$ . Comparing this with Eq. (5), we see that z is reachable from y in time t.

Corollary 1. The pair $( A , B )$ is controllable if and only if the system ${ \dot { \mathbf { x } } } = A { \mathbf { x } } + B { \mathbf { \mathfrak { u } } } , { \mathbf { \mathfrak { x } } } ( 0 ) = { \mathbf { \mathfrak { x } } } _ { 0 }$ , is controllable.

PROOF. If the pair $( A , B )$ is controllable then $\mathcal { C } _ { A , B } = \mathbb { C } ^ { n }$ Thus, for any $y , z \in \mathbb { C } ^ { n } ,$ , it follows trivially that $\mathbf { \delta } \mathbf { z } \mathrm { ~ - ~ } e ^ { \mathbf { { \cal A } } t } \mathbf { y } \in \mathcal { C } _ { { \cal A } , { \cal B } }$ . Then Theorem 2 asserts that the system is controllable.

Conversely, if the system is controllable then, in particular, every vector $z \in \mathcal { C } ^ { n }$ is reachable from the zero vector and, by Theorem 2, $\mathcal { C } _ { A , B } = \mathbb { C } ^ { n }$ Thus, the pair $( A , B )$ is controllable.

When the system is controllable, it turns out that any $z \in \mathbb { C } ^ { n }$ is reachable from any $\pmb { y } \in \mathbb { C } ^ { n }$ at any time $t > 0$ To see this, we construct an explicit control function $u ( s )$ that will take the solution from y to z in any prescribed time t Thus, in the controllable case, $W ( t )$ of Lemma 2 is positive definite and we may define a function

$$
\pmb { u } ( s ) = B ^ { * } e ^ { \pmb { A } ^ { * } ( t - s ) } W ( t ) ^ { - 1 } ( \pmb { z } - e ^ { \pmb { A } t } \pmb { y } ) .\tag{8}
$$

Then Eq. (5) gives

$$
x ( t ; y , u ) = e ^ { A t } y + \left( \int _ { 0 } ^ { t } e ^ { A ( t - s ) } B B ^ { * } e ^ { A ^ { * } ( t - s ) } d s \right) W ( t ) ^ { - 1 } ( z - e ^ { A t } y ) .
$$

Using definition (7) of $W ( t )$ , this equation reduces to

$$
\pmb { x } ( t ; \pmb { y } , \pmb { u } ) = e ^ { A t } \pmb { y } + \pmb { z } - e ^ { A t } \pmb { y } = \pmb { z } ,
$$

as required.

Exercise 1. Show that if z is reachable from y and $\boldsymbol { y } \in \mathcal { C } _ { A , B }$ , then $z \in \mathcal { C } _ { A , B }$

Exercise 2. The system dual to that of Eqs. (4) is defined to be a system of the type in Eqs. (1), given in terms of A and B by

$$
\dot { \boldsymbol { y } } ( t ) = - \boldsymbol { A } ^ { * } \boldsymbol { y } ( t ) ,
$$

$$
z ( t ) = B ^ { * } y ( t ) .
$$

Show that the system (4) is controllable if and only if its dual system is observable.

Exercise 3. Let $\mathcal { C } _ { A , B }$ have dimension k. Use the ideas of Section 4.8 to form a matrix P such that, if $\hat { \boldsymbol { A } } = \boldsymbol { P } ^ { - 1 } \boldsymbol { A } \boldsymbol { P }$ and $\hat { B } = P ^ { - 1 } B ,$ then

$$
{ \widehat { A } } = { \left[ \begin{array} { l l } { A _ { 1 } } & { A _ { 3 } } \\ { 0 } & { A _ { 2 } } \end{array} \right] } \qquad { \mathrm { a n d } } \qquad { \widehat { B } } = { \left[ \begin{array} { l } { B _ { 1 } } \\ { 0 } \end{array} \right] } ,
$$

where $A _ { 1 }$ is $k \times k , B _ { 1 }$ is $k \times m ,$ and the pair $( A _ { 1 } , B _ { 1 } )$ is controllable.

Hint. Recall that $\mathcal { C } _ { A , B }$ is A-invariant and Im $B \subset \mathcal { C } _ { A , B }$ . Use the transformation of variables $\mathbf { x } = P z$ to transform ${ \dot { \mathbf { x } } } ( t ) = A { \mathbf { x } } ( t ) + B ( t )$ to the form $\dot { z } ( t ) = \widehat { A } z ( t ) + \widehat { B } \pmb { u } ( t )$ and show that if

$$
z ( t ) = { \biggl [ } { \begin{array} { l } { z _ { 1 } ( t ) { \biggl ] } } \\ { z _ { 2 } ( t ) { \biggl ] } } \end{array} } ,
$$

where ${ \boldsymbol z } _ { 1 } ( t )$ takes values in $\mathbb { C } ^ { k } ;$ , then $\dot { z } _ { 1 } ( t ) = A _ { 1 } z _ { 1 } ( t ) + B _ { 1 } \pmb { u } ( t )$ is a controllable system.

Exercise 4. Establish the following analogue of Lemma 1. If $\ b { A } \in \mathbb { C } ^ { n \times n }$ then there are functions $\varphi _ { 1 } ( \lambda ) , \ldots , \varphi _ { n } ( \lambda )$ analytic in any neighborhood not containing points of $\sigma ( A )$ such that

$$
( \lambda I - A ) ^ { - 1 } = \sum _ { j = 1 } ^ { n } \varphi _ { j } ( \lambda ) A ^ { j - 1 } . \quad \bigsqcup
$$

## 9.12 Miscellaneous Exercises

1. If $f ( \lambda )$ is defined on the spectrum of $A \in \mathbb { C } ^ { n \times n }$ , prove that $f ( A ^ { \boldsymbol { \mathsf { T } } } ) =$ $[ f ( A ) ] ^ { \boldsymbol { \mathsf { T } } }$

Hint. Observe that the interpolatory polynomials for A and $A ^ { \boldsymbol { \mathsf { T } } }$ coincide.

2. If $A \in \mathbb { C } ^ { n \times n }$ . show that $\begin{array} { r } { A ^ { 2 } = \sum _ { k = 1 } ^ { s } { ( \lambda _ { k } ^ { 2 } Z _ { k 0 } + 2 \lambda _ { k } Z _ { k 1 } + 2 Z _ { k 2 } ) } } \end{array}$ by use of Theorems 9.5.1 and 9.5.2 and Exercise 9.5.1(b).

3. Prove that the series $I + A + A ^ { 2 } + \cdots$ converges if and only if all the eigenvalues of A have modulus less than 1.

Hint. See Exercise 9.8.5.

4. Show that a unitary matrix U can be expressed in the form $U = e ^ { i H }$ where H is Hermitian. Observe the analogy between this and the representation $u = e ^ { \mathrm { i } \alpha }$ (α real) of any point on the unit circle.

Hint. Show that $U = V \mathrm { d i a g } [ e ^ { i \alpha _ { 1 } } , e ^ { i \alpha _ { 2 } } , . . . , e ^ { i \alpha _ { n } } ] V ^ { * }$ for some unitary V and real scalars $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { n }$ and define $H = V \mathrm { d i a g } [ \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { n } ] V ^ { * }$

5. If $A \in \mathbb { C } ^ { n \times n }$ , prove that there is a real skew-symmetric matrix S such that $A = e ^ { S }$ if and only if A is a real orthogonal matrix with det $A = 1$

6. Determine $A ^ { n } ( \lambda )$ , where

$$
A ( \lambda ) = { \left[ \begin{array} { l l l } { 1 - \lambda + \lambda ^ { 2 } } & { 1 - \lambda } \\ { \lambda - \lambda ^ { 2 } } & { \lambda } \end{array} \right] } ,
$$

for all integers n and all λ by use of Eq. (9.5.1).

7. If the elements of the square matrix D(λ) are differentiable and $\Delta ( \lambda ) =$ det D(λ), show that

$$
\Delta ^ { ( 1 ) } ( \lambda ) = \mathrm { t r } ( ( \mathrm { a d j } D ( \lambda ) ) D ^ { ( 1 ) } ( \lambda ) )
$$

and if $\Delta ( \lambda ) \neq 0 ,$

$$
\frac { \Delta ^ { ( 1 ) } ( \lambda ) } { \Delta ( \lambda ) } = \mathrm { t r } ( D ^ { - 1 } ( \lambda ) D ^ { ( 1 ) } ( \lambda ) ) .
$$

8. Suppose that λ is a real variable. Let D(λ), defined in Exercise 7, be a solution of the matrix differential equation $\dot { X } ( \lambda ) = X ( \lambda ) A ( \lambda )$ , where A(λ) exists for all λ. Prove that if $\Delta ( \lambda ) = \operatorname * { d e t } D ( \lambda )$ , and if there is a $\lambda _ { 0 }$ for which $\Delta ( \lambda _ { 0 } ) \neq 0$ , then

$$
\Delta ( \lambda ) = \Delta ( \lambda _ { 0 } ) \exp \int _ { \lambda _ { 0 } } ^ { \lambda } \mathrm { t r } ( A ( \mu ) ) d \mu ,
$$

and hence $\Delta ( \lambda ) \neq 0$ for all λ. (This relation is variously known as the Jacobi identity, Liouville's formula, or Abel's formula.)

9. If all the eigenvalues of A have negative real parts, prove that

$$
A ^ { - 1 } = - \int _ { 0 } ^ { \infty } e ^ { A t } d t ,
$$

and hence that if all eigenvalues of A are in the half-plane given by $\{ \lambda \in \mathbb { C } : \mathcal { R } \boldsymbol { \mathscr { e } } \lambda < \mathcal { R } \boldsymbol { \mathscr { e } } \lambda _ { 0 } \}$ , then

$$
( I \lambda _ { 0 } - A ) ^ { - 1 } = \int _ { 0 } ^ { \infty } e ^ { - ( I \lambda _ { 0 } - A ) t } d t .
$$

Hint. Apply the result of Exercise 9.5.2.

10. Prove that for any $A \in \mathbb { C } ^ { n \times n } ,$ , the component matrices $Z _ { k j } ~ ( j = 0 , 1$ $\ldots , m _ { k } - 1 , k = 1 , 2 , \ldots , s )$ satisfy

$$
Z _ { k j } Z _ { k t } = { \binom { j + t } { j } } Z _ { k , j + t } , 0 \leq j , t \leq m _ { k } - 1 ,
$$

with the convention that $Z _ { k l } = 0 { \mathrm { ~ i f ~ } } l \geq m _ { k }$

Hint. Use Eq. (9.5.9).

11. Let $\begin{array} { r } { L ( \lambda ) = \sum _ { i = 0 } ^ { l } \lambda ^ { i } L _ { i } } \end{array}$ be an n × n λ-matrix over $\mathbb { C } ,$ let $A \in \mathbb { C } ^ { n \times n } ,$ , and let $\begin{array} { r } { L ( A ) = \sum _ { i = 0 } ^ { l } { L _ { i } A ^ { i } } } \end{array}$ Prove that

$$
\begin{array} { r l } { \mathrm { ( a ) } } & { { } L ( A ) = \displaystyle \sum _ { k = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } L ^ { ( j ) } ( \lambda _ { k } ) Z _ { k j } , } \end{array}
$$

where $Z _ { k j } ( 1 \leq k \leq s , 0 \leq j \leq m _ { k } - 1 )$ are the component matrices for A.

$$
{ \cal L } ( A ) = { \frac { 1 } { 2 \pi i } } \int _ { \cal L } L ( \lambda ) R _ { \lambda } d \lambda ,
$$

where $R _ { \lambda } = ( \lambda I - A ) ^ { - 1 } , \lambda \notin \sigma ( A )$ , and L is a contour like that described in Theorem 9.9.2.

Hint. For part (a) first find $\boldsymbol { A } ^ { i } \ ( i = 0 , 1 , \ldots , l )$ by Eq. (9.5.1); for part (b) use Eq. (9.8.4) and part (a)

12. With the notation of Exercise 11, prove that

$$
L ( A ) Z _ { k t } = \sum _ { j = 0 } ^ { m _ { k } - 1 } L ^ { ( j ) } ( \lambda _ { k } ) \binom { j + t } { j } Z _ { k , j + t }
$$

for $k = 1 , 2 , \ldots , s$ and $t = 0 , 1 , \ldots , m _ { k } - 1$ , where $Z _ { k , j + t } = O$ for $j + t \ge m _ { k }$

Hint. Use Exercises 10 and 11 and Theorem 9.5.2(b).

13. Prove that Ker $Z _ { k 0 } \subset \operatorname { I m } ( A - \lambda _ { k } I )$ and that $m _ { k } = 1$ implies Ker $Z _ { k 0 }$ $= \operatorname { I m } ( A - \lambda _ { k } I )$ for $k = 1 , 2 , \ldots , s .$

Hint. Represent $\varphi _ { k 0 } ( \lambda ) - 1 = ( \lambda - \lambda _ { k } ) q ( \lambda )$ , where $\varphi _ { k j } ( \lambda )$ are defined in Section 9.2, and substitute A for λ. For the second part use Exercise 9.5.1(b).

14. If A, $\ b { B } \in \mathbb { C } ^ { n \times n }$ and $X = X ( t )$ is an $n \times n$ matrix dependent on t, check that a solution of

$$
{ \dot { X } } = A X + X B , \qquad X ( 0 ) = C ,
$$

is given by $X = e ^ { A t } C e ^ { B t }$

15. Consider the matrix differential equations

$$
{ \bf ( a ) } \dot { X } = A X , ( { \bf b } ) \dot { X } = A X + X B ,
$$

in which A, $\ b { B } \in \mathbb { C } ^ { n \times n }$ are skew-Hermitian matrices and $X = X ( t )$ Show that in each case there is a solution matrix $X ( t )$ that is unitary for each t.

Hint. Use Exercise 14 with $C = I$ for part (b).

16. Let $A ( t ) , B ( t ) \in \mathbb { C } ^ { n \times n }$ for each $t \in [ t _ { 1 } , t _ { 2 } ]$ and suppose that any solution of ${ \dot { X } } + A X + X B X = 0$ is nonsingular for each $t \in \left[ t _ { 1 } , t _ { 2 } \right]$ . Show the following.

(a) The matrix-valued function $Y = X ^ { - 1 }$ satisfies the linear equation

$$
\dot { Y } - Y A = B ,\tag{1}
$$

(b) If A is independent of t, then the solution of Eq. (1) with $Y ( t _ { 0 } )$ $= C ^ { - 1 } \left( t _ { 1 } \leq t _ { 0 } \leq t _ { 2 } \right)$ is given by

$$
Y ( t ) = C ^ { - 1 } e ^ { A ( t - t _ { 0 } ) } + \int _ { t _ { 0 } } ^ { t } B ( \tau ) e ^ { A ( t - \tau ) } d \tau .
$$

17. Find the solution of ${ \ddot { \pmb x } } = A { \pmb x } + { \pmb f } , { \pmb x } ( 0 ) = { \pmb x } _ { 0 } , { \dot { \pmb x } } ( 0 ) = { \dot { \pmb x } } _ { 0 }$

18. Verify that if A is nonsingular, then

$$
{ \pmb x } ( t ) = ( \cos A ^ { 1 / 2 } t ) { \pmb x } _ { 0 } + ( A ^ { 1 / 2 } ) ^ { - 1 } ( \sin A ^ { 1 / 2 } t ) \dot { { \pmb x } } _ { 0 }
$$

is the solution of ${ \ddot { \mathbf { x } } } = { } - A \mathbf { x } , { \mathbf { x } } ( 0 ) = \mathbf { x } _ { 0 } , { \dot { \mathbf { x } } } ( 0 ) = { \dot { \mathbf { x } } } _ { 0 }$ . How can the result be extended to include a singular matrix A?

19. If $A \in \mathbb { C } ^ { n \times n }$ and $\dot { \mathbf { y } } ( t ) = A \mathbf { y } ( t )$ has a nonzero solution ${ \bf y } ( t )$ for which $y ( t + \tau ) = \lambda y ( t )$ for all t and some fixed $\tau > 0 ,$ prove that $\lambda = e ^ { \mu \tau }$ for some $\mu \in \sigma ( A )$ . Hence show that a periodic solution exists only if A is singular.

20. Show that the controllable subspace of the pair $( A , B )$ is the smallest A-invariant subspace containing Im B.

Hint. Note Exercise 9.11.3.

21. Let $f ( \lambda )$ be a function defined on the spectrum of a Hermitian matrix H with the property $| f ( \lambda ) | = 1$ whenever λ is real. Show that $f ( H )$ is unitary.

22. (a) Let $\lambda _ { 0 }$ be an eigenvalue of $\boldsymbol { A } \in \mathbb { C } ^ { n \times n }$ with algebraic multiplicity $\mu .$ Show that

$$
\mu = \operatorname * { l i m } _ { \lambda  \lambda _ { 0 } } [ ( \lambda - \lambda _ { 0 } ) \operatorname { t r } ( \lambda I - A ) ^ { - 1 } ] .
$$

Hint. Use Ex. 7 above with $D ( \lambda ) = \lambda I - A$

(b) If A has component matrices $Z _ { 0 } , Z _ { 1 } , \dots , Z _ { m - 1 }$ corresponding to $\lambda _ { 0 }$ , show that

$$
\operatorname { t r } ( Z _ { j } ) = \left\{ { \begin{array} { l l } { \mu } & { \quad { \mathrm { f o r } } \quad j = 0 } \\ { 0 } & { \quad { \mathrm { f o r } } \quad j = 1 , 2 , \ldots , m - 1 . } \end{array} } \right.
$$

(c) Check the above properties in Exs. 9.5.3 and 9.5.5.

# Norms and Bounds for Eigenvalues

In many situations it is useful to be able to assign a single nonnegative number to a vector or a matrix as a measure of its magnitude. We already have such a measure of magnitude for a complex number, namely, its modulus; and for a vector x of $\mathbb { C } ^ { n } ;$ the magnitude can be measured by the length $( { \pmb x } , { \pmb x } ) ^ { 1 / 2 }$ , introduced in Section 3.11. We will take an axiomatic approach to the formulation of measures of magnitude or norms of elements of an arbitrary linear space and begin by setting down the properties we demand of such a measure. We shall see that there are many possible choices for norms.

A study of norms of matrices and vectors is the first topic of this chapter, while different results concerning bounds for eigenvalues (some of which are expressed in terms of a norm of a matrix) are studied in the second part of the chapter.

## 10.1 The Notion of a Norm

Consider a linear space $\mathcal { S }$ over the field of complex or real numbers. A real-valued function defined on all elements x from $\mathcal { S }$ is called a norm (on S); usually written , if it satisfies the following axioms:

(1) $\| { \pmb x } \| \geq 0$ for all $\pmb { x } \in \mathcal { S }$ and $\| \pmb { x } \| = 0$ if and only if ${ \pmb x } = { \pmb \theta }$

(2) $\| { \pmb { \alpha } } { \pmb { x } } \| = | { \pmb { \alpha } } | \ \| { \pmb { x } } \|$ for all $\pmb { x } \in \mathcal { S }$ and $\alpha \in \mathbb { C }$

(3) $\| { \pmb x } + { \pmb y } \| \leq \| { \pmb x } \| + \| { \pmb y } \|$ for all $\pmb { x } , \pmb { y } \in \mathcal { S } .$

It is helpful to bear in mind the analogy of a norm with the modulus of a complex number or with the familiar length of a vector in $\mathbb { R } _ { 3 }$ . The axioms 1–3 are immediate generalizations for these ideas and therefore, in particular, axiom 3 is called the triangle inequality.

Note first of all that in a unitary space $\boldsymbol { \mathcal U }$ (see Section 3.11) the inner product generates a norm. Thus, one defines $\| { \pmb x } \| = ( { \pmb x } , { \pmb x } ) ^ { 1 / 2 }$ for any $\pmb { x } \in \mathcal { U }$ and the norm axioms above follow readily from the inner product axioms. It can be shown, however, that not all norm functions are generated by an inner product and, since several such norms are widely useful, much of the analysis of this chapter is completed without reference to inner products.

The next set of exercises is important. The first points out some immediate and frequently used consequences of the norm axioms. The second introduces the most important norms on the spaces $\textstyle \mathbb { R } ^ { n }$ and $\mathbb { C } ^ { n }$ of n-tuples. The third exercise shows, in particular, that norms can always be defined on an abstract finite-dimensional linear space. A linear space together with a norm defined on it is called a normed linear space.

Exercise 1. (a) For any $\mathbf { \delta x } , \mathbf { \delta y }$ in a normed linear space ${ \mathcal { S } } ,$ prove that

$$
| \| { \pmb x } \| - \| { \pmb y } \| | \leq \| { \pmb x } + { \pmb y } \| \leq \| { \pmb x } \| + \| { \pmb y } \| .
$$

(b) For any $\pmb { x } \in \mathcal { S }$ , show that $\lVert - { \pmb x } \rVert = \lVert { \pmb x } \rVert .$

(c) For any $\pmb { x } \in \mathcal S$ with $x \neq \theta ,$ show that there is a member of $\mathcal { S }$ of the form αx with norm equal to 1. (For example, take $\pmb { \alpha } = \| \pmb { x } \| ^ { - 1 } . )$

Exercise 2. Let x be a typical vector of $\mathbb { C } ^ { n } ( \mathrm { o r } \mathbb { R } ^ { n } ) , \boldsymbol { x } = [ x _ { 1 } \quad x _ { 2 } \quad \cdot \cdot \cdot \quad x _ { n } ] . ^ { \mathrm { \bf T } }$ Show that the functions $\| \big \| _ { \infty } , \big \| \big \| _ { 1 } , \big \| \big \| _ { 2 } , \big \| \big \| _ { p }$ defined on $\mathbb { C } ^ { n } \left( \mathrm { o r } \ \mathbb { R } ^ { n } \right)$ as follows are all norms on $\mathbb { C } ^ { n } \left( \mathrm { o r } \mathbb { R } ^ { n } \right)$

(a)

$$
\| { \pmb x } \| _ { \infty } = \operatorname* { m a x } _ { 1 \leq j \leq n } | x _ { j } | \qquad ( \mathrm { t h e } i n f i n i t y \mathrm { n o r m } ) ;\tag{b}
$$

$$
\| { \pmb x } \| _ { 1 } = \sum _ { j = 1 } ^ { n } | x _ { j } | ;
$$

$$
( \mathbf { c } ) \quad \| \mathbf { x } \| _ { 2 } = \left( \sum _ { j = 1 } ^ { n } | x _ { j } | ^ { 2 } \right) ^ { 1 / 2 } = ( \mathbf { x } ^ { * } \mathbf { x } ) ^ { 1 / 2 } \qquad ( \mathrm { t h e } \ e u c l i d e a n \ \mathrm { n o r m } ) ;
$$

$$
( \mathbf { d } ) \quad \| \pmb { x } \| _ { p } = \bigg ( \sum _ { j = 1 } ^ { n } | x _ { j } | ^ { p } \bigg ) ^ { 1 / p } , \quad p \geq 1 \qquad ( \mathrm { t h e } ~ H \ddot { \sigma } l d e r \mathrm { n o r m s } ) .
$$

Hint. For part (d) the Minkowski inequality should be assumed, that is, for any $p \geq 1$ and any complex n-tuples $( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ and $( y _ { 1 } , y _ { 2 } , \ldots , y _ { n } )$

$$
\left( \sum _ { j = 1 } ^ { n } | x _ { j } + y _ { j } | ^ { p } \right) ^ { 1 / p } \leq \left( \sum _ { j = 1 } ^ { n } | x _ { j } | ^ { p } \right) ^ { 1 / p } + \left( \sum _ { j = 1 } ^ { n } | y _ { j } | ^ { p } \right) ^ { 1 / p } .
$$

Exercise 3. Let $\{ b _ { 1 } , b _ { 2 } , . . . , b _ { n } \}$ be a fxed basis for a linear space ${ \mathcal { S } } ,$ and for any $\pmb { x } \in \mathcal { S }$ , write $\begin{array} { r } { \pmb { x } = \sum _ { j = 1 } ^ { n } \pmb { \alpha } _ { j } \pmb { b } _ { j } } \end{array}$

(a) Show that $\left\| \pmb { x } \right\| _ { \infty } = \operatorname* { m a x } _ { 1 \leq j \leq n } | \alpha _ { j } |$ defines a norm on ${ \mathcal { S } } .$

(b) If $p \geq 1$ , show that $\begin{array} { r } { \| { \pmb x } \| _ { p } = ( \sum _ { j = 1 } ^ { n } \big | \alpha _ { j } \big | ^ { p } ) ^ { 1 / p } } \end{array}$ defines a norm on ${ \mathcal { S } } .$ □

The euclidean norm of Exercise $2 ( \mathrm { c } )$ is often denoted by $\Vert \big | \big | \big | \big | \big | \big | \big | \big | \big | \big | \big |$ and is just one of the Hölder norms of part (d). It is clear from these exercises that many different norms can be defined on a given finite-dimensional linear space, and a linear space combined with one norm produces a different “normed linear space" from the same linear space combined with a different norm. For example, $\mathbb { C } ^ { n }$ with $\parallel \parallel _ { \infty }$ is not the same normed linear space as $\mathbb { C } ^ { n }$ with $\left. \begin{array} { r l } \end{array} \right. \begin{array} { r l } { ~ } & { { } \parallel _ { 2 } } \end{array}$ For this reason it is sometimes useful to denote a normed linear space by a pair, $\mathcal { S } , \Vert \dag \Vert$

It is also instructive to consider the examples of Exercise 2 as special cases of Exercise 3. This is done by introducing the basis of unit coordinate vectors into $\mathbb { C } ^ { n } .$ , or $\mathbb { R } ^ { n } ,$ in the role of the general basis $\{ b _ { 1 } , \ldots , b _ { n } \}$ of Exercise 3.

The notation $\bigstar \bigstar \bigstar | \bigstar \bigstar \bigstar | _ { \infty }$ used for the norm in Exercise $3 ( \mathbf { a } )$ suggests that it might be interpreted as a norm of the type introduced in Exercise $2 ( \mathrm { d } )$ with $p = \infty$ This can be justified in a limiting sense in the following way: If $\begin{array} { r } { { \pmb x } = \sum _ { j = 1 } ^ { n } { \pmb \alpha } _ { j } { \pmb b } _ { j } } \end{array}$ and there are v components $\alpha _ { i } \ ( 1 \leq i \leq n )$ of absolute value $\| \mathbf { \boldsymbol { x } } \| _ { \infty } = \rho$ $= \operatorname* { m a x } _ { 1 \leq i \leq n } | \alpha _ { i } |$ , then

$$
\| { \pmb x } \| _ { p } = ( | \alpha _ { 1 } | ^ { p } + | \alpha _ { 2 } | ^ { p } + \cdot \cdot \cdot + | \alpha _ { n } | ^ { p } ) ^ { 1 / p } = \rho ( \nu + \varepsilon _ { 1 } ^ { p } + \cdot \cdot \cdot + \varepsilon _ { n - v } ^ { p } ) ^ { 1 / p } ,
$$

where for some $k$ depending on $j , \varepsilon _ { j } = | \alpha _ { k } | / \rho < 1 ( j = 1 , 2 , \ldots , n - \nu )$ . Now it is easily seen that $\left\| { \pmb x } \right\| _ { \infty } = \rho = \operatorname* { l i m } _ { p \to \infty } \left\| { \pmb x } \right\| _ { p } ,$

Exercise 4. $\mathbf { I f } \parallel \mathbf { \Sigma } \parallel$ denotes a norm on a linear space $\mathcal { S }$ and $k > 0 ,$ , show that $k \parallel \parallel$ is also a norm on ${ \mathcal { S } } .$

Exercise 5. Let $\boldsymbol { \mathcal U }$ be a unitary space with inner product $( \mathbf { \epsilon } , \mathbf { \epsilon } ) ,$ as defined in Section 3.11. Show that $\| { \pmb x } \| = ( { \pmb x } , { \pmb x } ) ^ { 1 / 2 }$ defines a norm on $\mathcal { U } .$ (Thus, the natural definition of a norm on a unitary space makes it a normed linear space.)

Exercise 6. Show that the euclidean vector norm on $\mathbb { C } ^ { n }$ is invariant under unitary transformations. In other words, if $\pmb { x } \in \mathbb { C } ^ { n }$ and $U \in \mathbb { C } ^ { n \times n }$ is a unitary matrix, then $\| U \pmb { x } \| _ { 2 } = \| \pmb { x } \| _ { 2 }$ . Formulate an abstract generalization of this result concerning an arbitrary unitary space $\mathcal { U } .$

Exercise 7. If H is a positive definite matrix, show that

$$
\| { \pmb x } \| = ( H { \pmb x } , { \pmb x } ) ^ { 1 / 2 } = ( { \pmb x } ^ { * } H { \pmb x } ) ^ { 1 / 2 }
$$

is a norm on $\mathbb { C } ^ { n } .$ What is the generalization appropriate for an abstract unitary space?

The remainder of this section is devoted to two important results concerning norms in general. The first tells us that a norm is necessarily a “smooth" function of the coordinates of a vector $\pmb { x } \in \mathcal { S }$ with respect to a fixed basis in ${ \mathcal { S } } .$ Thus, “small" variations in the coordinates of x give rise to small variations in the size of the norm. Observe first that in a normed linear space $\| \pmb { x } \|$ depends continuously on x itself. This follows immediately from Exercise 1(a), which implies that, in any normed linear space ${ \mathcal { S } } .$

$$
| \| { \mathbf { x } } \| - \| { \mathbf { y } } \| | \leq \| { \mathbf { x } } - { \mathbf { y } } \| .
$$

for all $\pmb { x } , \pmb { y } \in \mathcal { S } .$

Theorem 1. Let $\{ b _ { 1 } , b _ { 2 } , \ldots , b _ { n } \}$ be a fxed basis in a linear space ${ \mathcal { S } } .$ Then any norm deined on S depends continuously on the coordinates of members of $\mathcal { S }$ with respect to $\boldsymbol { b } _ { 1 } , \ldots , \boldsymbol { b } _ { n }$ . In other words, $\begin{array} { r } { i f x = \sum _ { j = 1 } ^ { n } x _ { j } b _ { j } , y = \sum _ { j = 1 } ^ { n } y _ { j } b _ { j } } \end{array}$ denote arbitrary members of $\mathcal { S }$ and $\parallel \parallel$ is a norm on ${ \mathcal { S } } ,$ then given $\varepsilon > 0$ there is a $\delta > 0$ depending on ε such that

$$
| \| { \pmb x } \| - \| { \pmb y } \| | < \varepsilon
$$

whenever $| x _ { j } - y _ { j } | < \delta f o r j = 1 , 2 , \ldots , n .$

PROOF. Let $M = \operatorname* { m a x } _ { 1 \leq j \leq n } \| \boldsymbol { b } _ { j } \|$ . By the first norm axiom, $M > 0 _ { : }$ , so we may choose a $\delta$ satisfying $0 < \delta \leq \varepsilon / M n$

Then for any $\pmb { x } , \pmb { y } \in \mathcal { S }$ for which $| x _ { j } - y _ { j } | < \delta$ for each j we have, using the second and third norm axioms,

$$
\| x - y \| \leq \sum _ { j = 1 } ^ { n } | x _ { j } - y _ { j } | \| b _ { j } \| \leq M \sum _ { j = 1 } ^ { n } | x _ { j } - y _ { j } | < M n \delta \leq \varepsilon .
$$

The next result is a comparison theorem between different norms defined on the same space. If any two norms, $\parallel \parallel _ { 1 }$ and $\| \quad \| _ { 2 } , \mathsf { o n } { \mathcal { S } }$ satisfy $\left\| { \pmb x } \right\| _ { 1 } \le \left\| { \pmb x } \right\| _ { 2 }$ for all $\pmb { x } \in \mathcal { S }$ , we say that $\begin{array}{c} \left. \begin{array} { l } { } \end{array} \right. \begin{array} { l } { } \\ { 2 } \end{array}  \end{array}$ dominates $\begin{array}{c} \left. \begin{array} { r l } \end{array} \right. \begin{array} { r l } { \mathbf { \Sigma } } & { { } } \end{array}  \end{array}$ . Now, we have noted in Exercise 4 that a positive multiple of a norm is a norm. The next result says that all norms are equivalent in the sense that for any two norms $\parallel \parallel _ { 1 }$ and $\Vert \bigstar \bigstar \bigstar | | _ { 2 }$ on ${ \mathcal { S } } , \emptyset \ \emptyset \ 1$ is dominated by a positive multiple of $\left. \begin{array} { r l } \end{array} \right. \left. \begin{array} { r l } \end{array} \right. _ { 2 }$ and, at the same time, $\left. \begin{array} { r l } \end{array} \right. \left. \begin{array} { r l } \end{array} \right. _ { 2 }$ is dominated by a positive multiple of $\parallel \big \parallel _ { 1 }$ . It should be noted that the proof depends on the fact that $\mathcal { S }$ is finite-dimensional.

First we make a formal definition: two norms $\bigstar \bigstar \bigstar | | _ { 1 }$ and $\Vert \bigstar \bigstar \bigstar | | _ { 2 }$ defined on a linear space $\mathcal { S }$ are said to be equivalent if there exist positive numbers $r _ { 1 }$ and $r _ { 2 }$ depending only on the choice of norms such that, for any nonzero $\pmb { x } \in \mathcal { S } .$

$$
r _ { 1 } \leq \| \mathbf { x } \| _ { 1 } / \| \mathbf { x } \| _ { 2 } \leq r _ { 2 } .\tag{1}
$$

Theorem 2. Any two norms on a finite-dimensional linear space are equivalent

PROOF. Let $\begin{array}{c} \left. \begin{array} { r l } \end{array} \right. \begin{array} { r l } { \mathbf { \Sigma } } & { { } } \end{array}  \end{array}$ and $\left. \begin{array} { r l } \end{array} \right. \left. \begin{array} { r l } \end{array} \right. _ { 2 }$ be any two norms defined on $\mathcal { S }$ We have observed that the functions $f _ { 1 }$ and $f _ { 2 }$ defined on $\mathcal { S }$ by $f _ { 1 } ( { \pmb x } ) = \| { \pmb x } \| _ { 1 }$ and $f _ { 2 } ( \pmb { x } ) = \| \pmb { x } \| _ { 2 }$ are continuous. Then it is easily verified that the sets

$$
C _ { 1 } = \{ \pmb { x } \in \mathcal { S } \colon \| \pmb { x } \| _ { 1 } = 1 \} , \qquad C _ { 2 } = \{ \pmb { x } \in \mathcal { S } \colon \| \pmb { x } \| _ { 2 } = 1 \}
$$

are bounded and closed in $\mathcal { S }$ (see Appendix 2). It follows that the greatest lower bounds

$$
\gamma _ { 1 } = \operatorname* { i n f } _ { \pmb { x } \in C _ { 1 } } \| \pmb { x } \| _ { 2 } , \qquad \gamma _ { 2 } = \operatorname* { i n f } _ { \pmb { x } \in C _ { 2 } } \| \pmb { x } \| _ { 1 }\tag{2}
$$

are attained on members of $C _ { 1 }$ and $C _ { 2 }$ , respectively. Hence $\gamma _ { 1 } = \| \pmb { x } _ { 0 } \| _ { 2 }$ for some $\pmb { x } _ { 0 } \in C _ { 1 }$ and so $\gamma _ { 1 } > 0$ . Similarly, $\gamma _ { 2 } > 0$ and for any nonzero $\pmb { x } \in \mathcal { S } ,$ it follows from (2) and the second norm axiom that

$$
\gamma _ { 1 } \leq { \bigg \| } { \frac { \mathbf { x } } { \| \mathbf { x } \| _ { 1 } } } { \bigg \| } _ { 2 } = { \frac { \| \mathbf { x } \| _ { 2 } } { \| \mathbf { x } \| _ { 1 } } }
$$

and

$$
\gamma _ { 2 } \leq { \bigg \| } { \frac { \mathbf { x } } { \| \mathbf { x } \| _ { 2 } } } { \bigg \| } _ { 1 } = { \frac { \| \mathbf { x } \| _ { 1 } } { \| \mathbf { x } \| _ { 2 } } }
$$

Taking $r _ { 1 } = \gamma _ { 2 }$ and $r _ { 2 } = 1 / \gamma _ { 1 }$ , inequalities (1) are obtained and the theorem is proved.

Exercise 8. Verify that equivalence of norms on $\mathcal { S }$ is an equivalence relation on the set of all norms on $\mathcal { S } . \sqsupset$

Theorem 2 can be useful since it can be applied to reduce the study of properties of a general norm to those of a relatively simple norm. The strong candidates for the choice of $\textbf { a } ^ { 6 6 }$ relatively simple" norm are generally $\left. \begin{array} { r l } { \mathbf { \Phi } } & { { } \right. _ { \infty } , \left. \mathbf { \Phi } \right.} \end{array}  _ { 1 }$ , or most frequently, $\Vert \bigstar \bigstar \bigstar | | _ { 2 }$ of Exercises 2 and 3.

## 10.2 A Vector Norm as a Metric: Convergence

In Section 10.1 the emphasis placed on a norm was its usefulness as a measure of the size of members of a normed linear space. It is also very important as a measure of distance. Thus, if $\mathcal { S } , \Vert \mathbf { \Sigma } \Vert$ is a normed linear space then for any $\mathbf { \Delta } _ { \mathbf { { x } } , \mathbf { \Delta } \mathbf { { y } } \in \mathcal { S } }$ , the quantity $\| { \pmb x } - { \pmb y } \|$ is thought of as a measure of the distance between x and y. The special case of $\mathbb { R } _ { 3 } \left( \mathrm { o r } \mathbb { R } _ { 2 } \right)$ with the euclidean norm produces the most familiar physical measure of distance.

The following properties are easily verified from the norm axioms for any $\mathbf { \delta x } , \mathbf { y } , \mathbf { z }$ in a normed linear space:

(a) $\| { \pmb x } - { \pmb y } \| \geq 0$ with equality if and only if ${ \bf y } = { \bf x }$

(b) $\| { \pmb x } - { \pmb y } \| = \| { \pmb y } - { \pmb x } \| ;$

$$
( \operatorname { c } ) \quad \| { \boldsymbol { x } } - { \boldsymbol { y } } \| \leq \| { \boldsymbol { x } } - { \boldsymbol { z } } \| + \| { \boldsymbol { z } } - { \boldsymbol { y } } \| .
$$

They correspond to the axioms for a metric, that is, a function defined on pairs of elements of the set $\mathcal { S }$ that is a mathematically sensible measure of distance.

The set of all vectors in a normed linear space whose distance from a fixed point $\scriptstyle { \mathbf { x } _ { 0 } }$ is $r > 0$ is known as the sphere with center $\scriptstyle { \mathbf { x } } _ { 0 }$ and radius r. Thus written explicitly in terms of the norm, this sphere is

$$
\{ \pmb { x } \in \mathcal { S } : \| \pmb { x } - \pmb { x } _ { 0 } \| = r \} .
$$

The set of $\pmb { x } \in \mathcal { S }$ for which $\| { \pmb x } - { \pmb x } _ { 0 } \| \le r$ is the ball with centre $\scriptstyle { \mathbf { 1 } } _ { 0 }$ and radius $r .$ The sphere with centre $\theta$ and radius $r = 1$ is called the unit sphere and plays an important part in the analysis of normed linear spaces, as it did in the proof of Theorem 10.1.2. The unit ball is, of course, $\{ { \pmb x } \in { \mathcal { S } } { : } \| { \pmb x } \| \leq 1 \}$

It is instructive to examine the unit sphere in $\mathbb { R } _ { 2 }$ with the norms $\bigstar \bigstar \bigstar | \bigstar \bigstar \bigstar | | _ { \infty }$ ${ \big \updownarrow } \quad { \big \updownarrow } _ { 2 }$ , and $\parallel \parallel .$ introduced in Exercise 10.1.2. It is easy to verify that the portions of the unit spheres in the first quadrant for these norms (described by $p = \infty , 2 , 1$ , respectively) are as sketched in Fig. 10.1. It is also instructive to examine the nature of the unit spheres for Hölder norms with intermediate values of $p$ and to try to visualize corresponding unit spheres in $\mathbb { R } _ { 3 }$

Exercise 1. Show that the function $\parallel \parallel$ defined on $\mathbb { C } ^ { n }$ by

$$
\| \pmb { x } \| = | x _ { 1 } | + \dotsb { + } | x _ { n - 1 } | + n ^ { - 1 } | x _ { n } | ,
$$

where $\mathbf { x } = [ x _ { 1 } \quad x _ { 2 } \quad \cdots \quad x _ { n } ] ^ { \mathrm { { T } } }$ , is a norm on $\mathbb { C } ^ { n }$ (or R"). Sketch the unit spheres in $\mathbb { R } ^ { 2 }$ and $\mathbb { R } ^ { 3 }$ . □

![](images/f9b33a3d4add67c6d81b93f63ed2a4e393b8cf00bfbc55ad588f56b6c23c41da.jpg)  
Fig. 10.1 Unit spheres in $R _ { 2 }$ for p-norms.

Norms can be defined on a linear space in a great variety of ways and give rise to unit balls with varied geometries. A property that all unit balls have in common, however, is that of convexity. (See Appendix 2 for a general discussion of convexity.)

Theorem 1. The unit ball in a normed linear space is a convex set.

PROOF. Let $\mathcal { S } , \Vert \mathbf { \Sigma } \Vert$ be a normed linear space with unit ball B. If $x , y \in B ,$ then for any $t \in [ 0 , 1 ]$ , the vector $z = t { \pmb x } + ( 1 - t ) { \pmb y }$ is a member of the line segment joining x and y. We have only to prove that $z \in B .$ .But the second and third norm axioms immediately give

$$
\| z \| \leq t \| x \| + ( 1 - t ) \| y \| ,
$$

and since $\| { \boldsymbol { \mathbf { x } } } \| \leq 1$ and $\| \mathbf { y } \| \leq 1$ we get $\| z \| \leq 1$ , so that $z \in B .$

Exercise 2. Show that any ball in a normed linear space is a convex set.

A primitive open set in a normed linear space is a neighborhood, which is simply the interior of a ball. More formally, if $\mathcal { S } , \parallel \mathbf { \Sigma } \parallel$ is a normed linear space, the neighborhood with centre $\scriptstyle { \pmb { x } } _ { 0 }$ and radius $r$ is the set

$$
N ( \pmb { x } _ { 0 } , r ) = \{ \pmb { x } \in \mathcal { S } ; \lVert \pmb { x } - \pmb { x } _ { 0 } \rVert < r \} .\tag{1}
$$

Neighborhoods are frequently useful in analysis. For example, if $\mathcal { S } , \parallel \mathbf { \Sigma } \parallel$ 1 and $\mathcal { R } , \parallel \mathbf { \epsilon } \parallel _ { 2 }$ are two normed linear spaces and $f$ is a function defined on $\mathcal { S }$ with values in ${ \mathcal R } ,$ then $f$ is continuous at $\pmb { x } _ { 0 } \in \mathcal { S }$ if given $\varepsilon > 0$ there is a $\delta > 0 _ { : }$ depending on $\delta ,$ such that ${ \pmb x } \in N ( { \pmb x } _ { 0 } , \delta )$ implies $f ( { \pmb x } ) \in N ( f ( { \pmb x } _ { 0 } )$ , ε). Note that $N ( \pmb { x } _ { 0 } , \delta )$ is a neighborhood in $\mathcal { S }$ defined via the norm $\parallel \parallel _ { 1 }$ and $N ( f ( \pmb { x } _ { 0 } ) , \pmb { \varepsilon } )$ is a neighborhood in $\mathcal { R }$ defined using the norm $\Vert \bigstar \bigstar \bigstar | | _ { 2 }$

A basic concept of analysis is convergence, and we have already considered the convergence of sequences and series in $\mathbb { C } ^ { n }$ and $\mathbb { R } ^ { n }$ in Section 9.8. For a general finite-dimensional linear space ${ \mathcal { S } } ,$ ,the approach adopted there can be generalized by first introducing a basis into ${ \mathcal { S } } .$ say $\left\{ b _ { 1 } , b _ { 2 } , \ldots , b _ { n } \right\}$ If $\{ \pmb { x } _ { k } \} _ { k = 1 } ^ { \infty }$ is a sequence in $\mathcal { S }$ then each member has a representation

$$
{ \bf x } _ { k } = \sum _ { j = 1 } ^ { n } \mathrm { ~ } \alpha _ { j } ^ { ( k ) } b _ { j } , \mathrm { ~ } k = 1 , 2 , \ldots ,\tag{2}
$$

and the sequence is said to converge coordinatewise to an element $\begin{array} { r } { \mathbf { x } _ { 0 } = \sum _ { j = 1 } ^ { n } \alpha _ { j } ^ { ( 0 ) } \pmb { b } _ { j } } \end{array}$ if ${ \alpha } _ { j } ^ { ( k ) }  { \alpha } _ { j } ^ { ( 0 ) }$ as $k \to \infty$ for each of the n scalar sequences obtained by putting $j = 1 , 2 , \dots , n .$ Thus, the convergence of sequences of vectors considered in section 9.8 is just coordinatewise convergence in the linear space $\mathbb { C } ^ { n }$ with respect to its standard basis.

However, this process is cumbersome and appears to depend on the choice of basis for $\mathcal { S }$ (although, in fact, it does not). Furthermore it turns out to be equivalent to a notion of convergence defined by a norm and, indeed, any norm, as we shall soon verify.

A sequence $\{ x _ { k } \} _ { k = 1 } ^ { \infty }$ in a normed linear space $\mathcal { S } , \Vert \mathbf { \Sigma } \Vert$ is said to be convergent in norm (or simply convergent) to $\pmb { x } _ { 0 } \in \mathcal { S } \mathrm { { i f } } \| \pmb { x } _ { k } - \pmb { x } _ { 0 } \|  0 \mathrm { { a s } } k  \infty$ . We will write, informally, ${ \pmb x } _ { k }  { \pmb x } _ { 0 }$ as $k \to \infty$

Exercise 3. Show that, if ${ \pmb x } _ { k }  { \pmb x } _ { 0 } , { \pmb y } _ { k }  { \pmb y } _ { 0 }$ , and $\mathfrak { X } _ { k } \to \mathfrak { X } _ { 0 }$ as $k \to \infty$ , where $\alpha _ { 0 }$ and the $\alpha _ { k }$ are scalars, then $\| \pmb { x } _ { k } - \pmb { x } _ { 0 } \|  0$ and $\alpha _ { k } x _ { k } + y _ { k } \to \alpha _ { 0 } x _ { 0 } + y _ { 0 }$ as $k \to \infty$

Exercise 4. Show that if $\left\{ x _ { k } \right\} _ { k = 1 } ^ { \infty }$ converges in one norm to $\scriptstyle { \mathbf { r } _ { 0 } }$ , then it converges to $\scriptstyle { \mathbf { x } _ { 0 } }$ in any other norm.

Hint. Use Theorem 10.1.2.

The next theorem shows that coordinatewise convergence and convergence in norm for infinite sequences (and hence series) in a finite-dimensional space are equivalent. However, the result is not true if the space is not of fnite dimension. Indeed, the possibility of different forms of convergence is a major issue in the study of infinite-dimensional linear spaces.

Theorem 2. Let $\{ \pmb { x } _ { k } \} _ { k = 1 } ^ { \infty }$ be a sequence in a finite-dimensional linear space ${ \mathcal { S } } .$ The sequence converges coordinatewise to $\pmb { x } _ { 0 } \in \mathcal { S }$ if and only if it converges to $\pmb { x _ { 0 } }$ in (any) norm.

PROOF. Let $\{ b _ { 1 } , b _ { 2 } , \ldots , b _ { n } \}$ be a basis in the linear space $\mathcal { S }$ and write $\begin{array} { r } { \mathbf { x } _ { k } = \sum _ { j = 1 } ^ { n } \alpha _ { j } ^ { ( k ) } \pmb { b } _ { j } } \end{array}$ for $k = 0 , 1 , 2 , \ldots$ . Given coordinatewise convergence to $\mathbf { \boldsymbol { x } } _ { 0 } \in \mathcal { S }$ we have, for any norm $\parallel \parallel$ defined on ${ \mathcal { S } } ,$

$$
\| x _ { k } - x _ { 0 } \| = \left\| \sum _ { j = 1 } ^ { n } ( \alpha _ { j } ^ { ( k ) } - \alpha _ { j } ^ { ( 0 ) } ) b _ { j } \right\| \leq \sum _ { j = 1 } ^ { n } | \alpha _ { j } ^ { ( k ) } - \alpha _ { j } ^ { ( 0 ) } | \| b _ { j } \| \to 0
$$

as $k \to \infty$ , since n and the basis are fixed. Hence, we have convergence in norm. Conversely, given that $\mathbf { \boldsymbol { x } } _ { k } \to \mathbf { \boldsymbol { x } } _ { 0 }$ in any norm we can, using the equivalence of norms (as in Exercise $4 ) _ { \cdot }$ , replace the norm by $\bigstar \bigstar \bigstar \bigstar \bigstar \bigstar \bigstar$ of Exercise 10.1.3(a). Then

$$
\| \mathbf { \boldsymbol { x } } _ { k } - \mathbf { \boldsymbol { x } } _ { 0 } \| _ { \infty } = \Bigg | \Bigg | \sum _ { j = 1 } ^ { n } ( \alpha _ { j } ^ { ( k ) } - \alpha _ { j } ^ { ( 0 ) } ) \pmb { \dot { b } } _ { j } \Bigg | \Bigg | _ { \infty } = \operatorname* { m a x } _ { 1 \leq j \leq n } | \alpha _ { j } ^ { ( k ) } - \alpha _ { j } ^ { ( 0 ) } | .
$$

Thus, $\| { \pmb x } _ { k } - { \pmb x } _ { 0 } \|  0$ implies $\| { \pmb x } _ { k } - { \pmb x } _ { 0 } \| _ { \infty } \to 0$ and hence

$$
\operatorname* { m a x } _ { 1 \leq j \leq n } \vert \alpha _ { j } ^ { ( k ) } - \alpha _ { j } ^ { ( 0 ) } \vert  0
$$

as ${ \bf k } \to \infty$ . This clearly implies coordinatewise convergence.

## 10.3 Matrix Norms

We start this section by confining our attention to norms on the linear space $\mathbb { C } ^ { n \times n }$ , that is, to norms of square matrices. Obviously, all properties of a general norm discussed in Sections 1 and 2 remain valid for this particular case. For instance, we have the following.

Exercise I. Verify that any norm on $\mathbb { C } ^ { n \times n }$ depends continuously on the matrix elements.

Hint. Consider the standard basis $\{ E _ { i j } \} _ { i , j = 1 } ^ { n }$ for $\mathbb { C } ^ { n \times n }$ (see Exercise 3.5.1) and use Theorem 10.1.1.

The possibility of multiplying any two matrices A, $\boldsymbol { B } \in \mathbb { C } ^ { n \times n }$ gives rise to an important question about the relation between the norms $\| A \| , \| B \|$ and the norm $\| A B \|$ of their product. We say that the norm ∥ ∥ on $\mathbb { C } ^ { n \times n }$ is a matrix norm or is submultiplicative (in contrast to a norm of a matrix as a member of the normed space $\mathbb { C } ^ { n \times n } )$ if

$$
\| A B \| \leq \| A \| \ \| B \|\tag{1}
$$

for all A, $\boldsymbol { B } \in \mathbb { C } ^ { n \times n }$ . Before examining some matrix norms note first that not all norms on $\mathbb { C } ^ { n \times n }$ are matrix norms.

Exercise 2. Verify that the real-valued function max $_ { 1 \leq i , j \leq n } | a _ { i j } | ,$ where $a _ { i j }$ is the $i , j \mathrm { t h }$ element of $A \in \mathbb { C } ^ { n \times n }$ , defines a norm on $\mathbb { C } ^ { n \times n }$ but is not a matrix norm.

Exercise 3. (The euclidean or Frobenius norm.) Prove that

$$
\| A \| _ { \mathrm { E } } = \biggl ( \sum _ { i , j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \biggr ) ^ { 1 / 2 } , \qquad A = [ a _ { i j } ] _ { i , j = 1 } ^ { n } ,
$$

defines a matrix norm on $\mathbb { C } ^ { n \times n }$

Hint. For the norm axioms the argument is that of Exercise 10.1.2(c), which requires the use of the Cauchy-Schwarz inequality (Exercise 2.5.4). For property (1) use the Cauchy-Schwarz inequality again.

Exercise 4. This generalizes Exercise 3. Show that the Hölder norm,

$$
\| A \| _ { p } = \bigg ( \sum _ { i , j = 1 } ^ { n } | a _ { i j } | ^ { p } \bigg ) ^ { 1 / p } , \qquad p \ge 1 ,\tag{2}
$$

is a matrix norm on $\mathbb { C } ^ { n \times n }$ if and only if $1 \leq p \leq 2$

Hint. Use the Hölder inequality:

$$
\sum _ { j = 1 } ^ { n } | x _ { j } y _ { j } | \leq { \biggl ( } \sum _ { j = 1 } ^ { n } | x _ { j } | ^ { p } { \biggr ) } ^ { 1 / p } { \biggl ( } \sum _ { j = 1 } ^ { n } | y _ { j } | ^ { q } { \biggr ) } ^ { 1 / q } ,\tag{3}
$$

where $p \ge 1 , q \ge 1$ , and $p ^ { - 1 } + q ^ { - 1 } = 1$

Exercise 5. Prove that, for any matrix norm  ,

$$
\| I \| \geq 1 , \qquad \| A ^ { n } \| \leq \| A \| ^ { n } , \qquad \| A ^ { - 1 } \| \geq { \frac { 1 } { \| A \| } } \quad ( \det A \neq 0 ) .
$$

Exercise 6. If S is nonsingular and $\parallel \parallel$ is a matrix norm, then the realvalued function f defined by $f ( A ) = \| S A S ^ { - 1 }$ is a matrix norm.

Exercise 7. Check that the following are true.

(a) The function $\left\| A \right\| = n \operatorname* { m a x } _ { 1 \leq i , j \leq n } | a _ { i j } |$ is a matrix norm. (Compare with Exercises 2 and 10.1.4.)

(b) $\operatorname { I f } \parallel \operatorname { \big \| } _ { \mathbf { E } }$ denotes the euclidean matrix norm (see Exercise 3) and   is defined as in part (a), then $\left\| A \right\| _ { \mathbf { E } } \leq \left\| A \right\|$

(c) $\| A \| _ { \mathrm { E } } ^ { 2 } = \operatorname { t r } ( A ^ { * } A ) .$

Exercise 8. If $p \geq 2$ and $( 1 / p ) + ( 1 / q ) = 1$ , then in the notation of Eq. (2),

$$
\begin{array} { r } { \| A B \| _ { p } \leq \operatorname* { m i n } ( \| A \| _ { p } \| B \| _ { q } , \| A \| _ { q } \| B \| _ { p } ) . } \end{array}
$$

Hint. Use Eq. (3).

The most useful matrix norms are often those that are easily defined in terms of the elements of the matrix argument. It is conceivable that a measure of magnitude for matrices could be based on the magnitudes of the eigenvalues, although this may turn out to be of no great practical utility, since the eigenvalues are often hard to compute. However, $\mathrm { i f } \lambda _ { 1 } , \ldots , \lambda _ { n }$ arethe eigenvalues of $A ,$ then $\mu _ { A } = \mathrm { m a x } _ { 1 \leq j \leq n } | \lambda _ { j } |$ is such a measure of magnitude and is known as the spectral radius of A.

Consider the matrix N of Exercise 6.8.6. It is easily seen that all of its eigenvalues are zero and hence the spectral radius of N is zero. Since N is not the zero-matrix, we see immediately that the spectral radius does not satisfy the first norm axiom. However, although the spectral radius is not a norm, it is intimately connected with the magnitude of matrix norms. Indeed, matrix norms are often used to obtain bounds for the spectral radius. The next theorem is a result of this kind.

Theorem 1. If $A \in \mathbb { C } ^ { n \times n }$ and $\mu _ { A }$ is the spectral radius of A then, for any matrix norm,

$$
\| A \| \geq \mu _ { A } .
$$

ProOF. Let λ be an eigenvalue of A such that $\mu _ { A } = | \lambda |$ Then there is a vector $\pmb { x } \neq \pmb { \theta }$ such that $A { \boldsymbol { \mathbf { x } } } = \lambda { \boldsymbol { \mathbf { x } } }$ . Define the $n \times n$ matrix

$$
A _ { x } = [ { \pmb x } \quad { \pmb \theta } \quad { \pmb \theta } \quad \cdots \quad { \pmb \theta } ]
$$

and observe that

$$
A A _ { x } = \lambda A _ { x } .
$$

Using the second norm axiom and property (1) of the matrix norm, we deduce that

$$
| \lambda | \ \| A _ { x } \| \leq \| A \| \ \| A _ { x } \| ,
$$

Since $A _ { x } \neq \theta ,$ it follows that $\| A _ { x } \| \neq 0$ and hence

$$
| \lambda | = \mu _ { A } \leq \| A \| . \quad \overline { { \mathbb { I } } }
$$

We are very often faced with the problem of finding the norm of a vector that is given in the form $A { \boldsymbol { \mathbf { \mathit { x } } } } ,$ where $A \in \mathbb { C } ^ { n \times n }$ and $\boldsymbol { x } \in \mathbb { C } ^ { n }$ .Given our experience with property (1) for a matrix norm, we might expect that there will be matrix norms $\parallel \parallel$ and vector norms ∥ ∥ (that is, norms on $\mathbb { C } ^ { n } )$ for which

$$
\left\| A \pmb { x } \right\| _ { \mathbf { v } } \leq \left\| A \right\| \left\| \pmb { x } \right\| _ { \mathbf { v } } .\tag{4}
$$

When Eq. (4) holds for all $\boldsymbol { x } \in \mathbb { C } ^ { n }$ and all $A \in \mathbb { C } ^ { n \times n }$ , then the vector norm  ∥lv and the matrix norm   are said to be compatible.

Exercise 9. Prove that the euclidean matrix and vector norms are compatible.

SoLUTION. For arbitrary $\pmb { x } = [ { \alpha } _ { 1 } \quad { \alpha } _ { 2 } \quad \cdots \quad { \alpha } _ { n } ] ^ { \mathsf { T } } \in \mathbb { C } ^ { n }$ and

$$
\begin{array} { r } { A = [ \boldsymbol { a } _ { i j } ] _ { i , j = 1 } ^ { n } \in \mathbb { C } ^ { n \times n } , } \end{array}
$$

compute $A { \bf x } = [ \beta _ { 1 } \mathrm { ~  ~ \nabla ~ } \beta _ { 2 } \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \nabla ~ } \beta _ { n } ] ^ { \bf T }$ , where $\begin{array} { r } { \beta _ { i } = \sum _ { j = 1 } ^ { n } a _ { i j } \alpha _ { j } , i = 1 , 2 , . . . , n . } \end{array}$ Hence by Eq. (3) for $p = 2 , q = 2 ,$

$$
\| A \pmb { x } \| _ { \mathbb { V } } ^ { 2 } = \sum _ { i = 1 } ^ { n } | \beta _ { i } | ^ { 2 } = \sum _ { i = 1 } ^ { n } \bigg | \sum _ { j = 1 } ^ { n } a _ { i j } \alpha _ { j } \bigg | ^ { 2 } \leq \sum _ { i = 1 } ^ { n } \bigg ( \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \bigg ) \bigg ( \sum _ { j = 1 } ^ { n } | \alpha _ { j } | ^ { 2 } \bigg ) .
$$

Finally, since $\textstyle \| A \| _ { \mathrm { E } } ^ { 2 } = \sum _ { i , j = 1 } ^ { n } | a _ { i j } | ^ { 2 }$ and $\begin{array} { r } { \| \mathbf { x } \| _ { \mathrm { v } } ^ { 2 } = \sum _ { j = 1 } ^ { n } | \alpha _ { j } | ^ { 2 } } \end{array}$ , we have

$$
\begin{array} { r } { \| A { \mathbf { x } } \| ^ { 2 } \leq \| A \| _ { \mathrm { E } } ^ { 2 } \| { \mathbf { x } } \| ^ { 2 } , } \end{array}
$$

which is equivalent to Eq. (4).

Exercise 10. Prove that the matrix norm defined in Exercise $7 ( \mathbf { a } )$ is compatible with the Hölder norms on $\mathbb { C } ^ { n }$ for $p = 1 , 2 , \infty$

Exercise 11. Let $\parallel \parallel _ { \mathbf { v } }$ be a norm on $\mathbb { C } ^ { n }$ and let $S \in \mathbb { C } ^ { n \times n }$ be nonsingular. Show that $\| { \pmb x } \| _ { S } = \| { \pmb S } { \pmb x } \| _ { \pmb \nu }$ is also a norm on $\mathbb { C } ^ { n }$ . Then show that $\parallel \parallel _ { s }$ and the matrix norm of Exercise 6 are compatible if and only if  ∥ and ∥  are $\parallel \parallel ,$ $\parallel \parallel$ compatible.□

As with column vectors and their norms, norms applied to matrices provide a useful vehicle for the study of convergence of sequences and series of matrices. Indeed, comparing the discussions of sections 9.8 and 10.2 it is easily seen that the following proposition is just a special case of Theorem 10.2.2.

Proposition 1. Let $\left\{ A _ { k } \right\} _ { k = 1 } ^ { \infty }$ be a sequence in $\mathbb { C } ^ { m \times n }$ n. The sequence converges coordinatewise to A if and only if $\| A _ { \pmb { k } } - A \|  0$ as $k \to \infty$ in any norm.

Here, the norm needs to have only the three basic properties of a vector norm, and the sub-multiplicative property plays no part.

The next exercises illustrate the use of norms in the analysis of an important numerical procedure.

Exercise 12. Suppose that $A \in \mathbb { C } ^ { n \times n }$ has an eigenvalue $\lambda _ { 1 }$ with the properties that $| \lambda _ { 1 } |$ exceeds the absolute value of all other eigenvalues of A and the index of λ1 is one. (Then λ, is called the dominant eigenvalue of A.) Show that, $\lambda _ { 1 }$ $\lambda _ { 1 }$ $A . )$ as $r \to \infty$

$$
\left( { \frac { 1 } { \lambda _ { 1 } } } A \right) ^ { r } \to Z _ { 1 0 } .\tag{5}
$$

Hint. Let $f ( z ) = z ^ { r }$ and use Theorem 9.5.1. (The hypothesis that $\lambda _ { 1 }$ has index one is made for convenience. Otherwise, the limit on the right of (5) is a little more complicated.)

Exercise 13. (The power method for calculating eigenvalues). Let $A \in \mathbb { C } ^ { n \times n }$ and have a dominant eigenvalue $\lambda _ { 1 }$ of index one (as in Exercise 12). Let $\scriptstyle { \mathbf { x } } _ { 0 }$ be any vector for which $\scriptstyle { \mathbf { 1 } } _ { 0 }$ ∉Ker $A ^ { n } , \| \pmb { x _ { 0 } } \| = 1$ in the euclidean norm, and $Z _ { 1 0 } x _ { 0 } \neq \theta .$ Define a sequence of vectors $\mathbf { x } _ { 0 } , \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots$ . of norm one by

$$
{ \pmb x } _ { r } = \frac { 1 } { k _ { r } } A { \pmb x } _ { r - 1 } , \qquad r = 1 , 2 , \ldots ,
$$

where $k _ { r } = \| A \pmb { x } _ { r - 1 } \|$ . Show that:

(a) The sequence is well-defined $( \mathrm { i } . \mathsf { e } . , k _ { r } \neq 0$ for any r).

(b) As $r  \infty , k _ { r }  \vert \lambda _ { 1 } \vert$

(c) There is a sequence $\{ \beta _ { r } \} _ { r = 1 } ^ { \infty }$ of complex numbers such that as $r  \infty$ $\beta _ { r + 1 } / \beta _ { r } \to | \lambda _ { 1 } | / \lambda _ { 1 }$ and

$$
\beta _ { r } x _ { r }  p _ { 1 } ,\tag{6}
$$

where p₁ is an eigenvector of A of norm one determined by the choice of ${ \pmb p } _ { 1 }$ $\scriptstyle \mathbf { x } _ { 0 }$ (Note that by normalizing the vectors $\mathbf { x } _ { r }$ to have euclidean norm equal to one, they are not defined to within a unimodular scalar multiple. Thus, the presence of $\beta _ { r }$ in (6) is to be expected. In numerical practice a different normalization is likely to be used, with $\bigstar \bigstar \bigstar | \bigstar \bigstar \bigstar$ for example. But as in so many cases, the euclidean norm is the most convenient for analysis.)

OUTLINE OF THE SOLUTION. Assume inductively that $k _ { 1 } , k _ { 2 } , \ldots , k _ { r - 1 }$ are nonzero. Then show that

$$
A x _ { r - 1 } = { \frac { 1 } { k _ { r - 1 } \cdot \cdot \cdot k _ { 2 } k _ { 1 } } } A ^ { r } x _ { 0 } .
$$

Since Ker $A ^ { r } = \mathbf { K }$ er $A ^ { n }$ for all $r \geq n$ (ref. Ex. 4.5.14), $\pmb { x } _ { 0 } \notin \pmb { \mathscr { x } }$ Ker $A ^ { \boldsymbol { r } } ,$ and so $A x _ { r - 1 } \neq \theta .$ Hence $k _ { r } \neq 0$ and (a) follows by induction.

Then observe

$$
k _ { r } = \| A ^ { r } { \bf x } _ { 0 } \| / \| A ^ { r - 1 } { \bf x } _ { 0 } \| .\tag{7}
$$

Define $p _ { 1 } = \alpha ^ { - 1 } Z _ { 1 0 } \pmb { x } _ { 0 }$ , where $\alpha = \| Z _ { 1 0 } \pmb { x } _ { 0 } \| \neq 0$ , and use the preceding exercise to show that $| \lambda _ { 1 } | ^ { - r } \| A ^ { r } { \pmb x } _ { 0 } \|  \alpha .$ Combine with (7) to obtain part (b). Ise the fact that Use the fact that

$$
\pmb { x } _ { r } = \frac { 1 } { k _ { r } \cdot \cdot \cdot k _ { 2 } k _ { 1 } } A ^ { r } \pmb { x } _ { 0 }
$$

together with Theorem 9.5.1 to show that

$$
\frac { k _ { r } \cdot \cdot \cdot k _ { 2 } k _ { 1 } } { \lambda _ { \mathrm { { I } } } ^ { r } } x _ { r }  \alpha p _ { 1 } ,
$$

and define $\beta _ { r } = ( k _ { r } \cdot \cdot \cdot k _ { 2 } k _ { 1 } ) / ( \alpha \lambda _ { 1 } ^ { r } )$ to obtain (c). □

## 10.4 Induced Matrix Norms

We now investigate a method for obtaining a matrix norm from any given vector norm. If  ∥, is a vector norm in $\mathbb { C } ^ { n }$ and $\ b { A } \in \mathbb { C } ^ { n \times n }$ , we consider the quotient $\| A \mathbf { x } \| _ { \mathbf { v } } / \| \mathbf { x } \| ,$ , defined for each nonzero $\pmb { x } \in \mathbb { C } ^ { n }$ . The quotient is obviously nonnegative; we consider the set of all numbers obtained when x takes all possible nonzero values in $\mathbb { C } ^ { n }$ and deine

$$
f ( A ) = \operatorname* { s u p } _ { \substack { \mathbf { x } \in \mathbb { C } ^ { n } , \mathbf { x } \neq \mathbf { 0 } } } \frac { \Vert A \mathbf { x } \Vert _ { \mathbf { v } } } { \Vert \mathbf { x } \Vert _ { \mathbf { v } } } .\tag{1}
$$

We shall prove that, for a fixed matrix A, this is a well-defined nonnegative number, and the resulting function $f ( A )$ is a matrix norm. We shall call it the matrix norm induced by the vector norm $\parallel \parallel _ { \mathbf { v } }$ . Note that there is a close analogy with the Rayleigh quotient (for Hermitian matrices), as discussed in Chapter 8. Also, observe that the definition can be applied to the definition of a norm for any linear transformation acting on a normed linear space.

To begin our investigation of the quotient in (1), we first note some important properties:

Exercise 1. Show that, for the function $f ( A )$ defined on $\mathbb { C } ^ { n \times n }$ by Eq. (1),

(a) $f ( A ) = \operatorname* { s u p } _ { x \in \mathbb { C } ^ { n } , \| x \| _ { \mathbf { v } } = 1 } \| A x \| _ { \mathbf { v } }$

(b) There is a vector $\pmb { x _ { 0 } } \in \mathbb { C } ^ { n }$ , depending on $A ,$ such that $\| \pmb { x _ { 0 } } \| _ { \mathbf { v } } = 1$ and $f ( A ) = \| A \pmb { x } _ { 0 } \| _ { \mathbf { v } }$ . Thus

$$
f ( A ) = \operatorname* { m a x } _ { \| { \pmb x } \| _ { \mathbb { V } } = 1 } \| A { \pmb x } \| _ { \mathbb { V } } , \qquad { \pmb x } \in \mathbb { C } ^ { n } .\tag{2}
$$

Hint. Observe first that replacing x by αx does not alter the quotient in Eq. (1). For part (b) take advantage of the technique used in the proof of Theorem 10.1.2.

The importance of the induced norms is partly explained by part (c) of the following theorem.

Theorem 1. Let ∥ , denote any vector norm on C". $\parallel \parallel .$ $\mathbb { C } ^ { n } .$

(a) The function f defined on $\mathbb { C } ^ { n \times n }$ by

$$
f ( A ) = \operatorname* { s u p } _ { \mathbf { x } \in \mathbb { C } ^ { n } , \mathbf { x } \neq \mathbf { 0 } } { \frac { \| A \mathbf { x } \| _ { \mathbf { v } } } { \| \mathbf { x } \| _ { \mathbf { v } } } } = \operatorname* { m a x } _ { \mathbf { x } \in \mathbb { C } ^ { n } , \| \mathbf { x } \| _ { \mathbf { \nu } } = 1 } \| A \mathbf { x } \| _ { \mathbf { v } }
$$

is a matrix norm and is denoted by $\parallel \parallel$

(b) The norms $\parallel \parallel$ and $\parallel \parallel ,$ are compatible.

(c) $I f \parallel \mathbf { \parallel _ { 1 } }$ is any matrix norm compatible with $\parallel \parallel _ { \mathbf { v } }$ then, for all $A \in \mathbb { C } ^ { n \times 1 }$ 3

$$
\| A \| \leq \| A \| _ { 1 } .
$$

ProoF. We set out to establish the axioms for a matrix norm. For axiom 1 it is clear that $f ( A ) \geq 0 .$ , and that $f ( A ) = 0$ if $A = \theta .$ If $A \neq \theta ,$ then there is an $\boldsymbol { x } \in \mathbb { C } ^ { n }$ such that $A x \neq \theta$ and $\| \pmb { x } \| _ { \mathbf { v } } = 1$ . Hence $f ( A ) > 0 .$ Axiom 1 is therefore satisfied.

Using axiom 2 for the vector norm and Eq. (2), we obtain

$$
f ( \lambda A ) = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { \mathbf { v } } = 1 } \| \lambda A \mathbf { x } \| _ { \mathbf { v } } = | \lambda | \operatorname* { m a x } _ { \| \mathbf { x } \| _ { \mathbf { v } } = 1 } \| A \mathbf { x } \| _ { \mathbf { v } } = | \lambda | f ( A ) ,
$$

and so axiom 2 for the matrix norm is also satisfied. Furthermore,

$$
\left\| ( A + B ) \pmb { x } \right\| _ { \mathbf { v } } = \left\| A \pmb { x } + B \pmb { x } \right\| _ { \mathbf { v } } \leq \left\| A \pmb { x } \right\| _ { \mathbf { v } } + \left\| B \pmb { x } \right\| _ { \mathbf { v } } ,
$$

hence

$$
\operatorname* { m a x } _ { \| \pmb { x } \| _ { \mathbb { v } } = 1 } \| ( A + B ) \pmb { x } \| _ { \mathbb { v } } \leq \operatorname* { m a x } _ { \| \pmb { x } \| _ { \mathbb { v } } = 1 } \| A \pmb { x } \| _ { \mathbb { v } } + \operatorname* { m a x } _ { \| \pmb { x } \| _ { \mathbb { v } } = 1 } \| B \pmb { x } \| _ { \mathbb { v } } .
$$

Thus, $f ( A + B ) \leq f ( A ) + f ( B )$ and we have axiom 3 for the matrix norm.

Proceeding finally to the submultiplicative property (10.3.1) of a matrix norm, we infer from Exercise 1(b) the existence of an $\pmb { x } _ { 0 } \in \mathbb { C } ^ { n }$ with $\| \pmb { x } _ { 0 } \| _ { \mathbf { v } } = 1$ such that $f ( A B ) = \| A B \pmb { x } _ { 0 } \| ,$ for given A, $\boldsymbol { B } \in \mathbb { C } ^ { n \times n }$ . Then

$$
f ( A B ) = \| A B \mathbf { x } _ { 0 } \| _ { \mathbf { v } } = \| A ( B \mathbf { x } _ { 0 } ) \| _ { \mathbf { v } } \leq f ( A ) \| B \mathbf { x } _ { 0 } \| _ { \mathbf { v } } ,
$$

because it follows from Eq. (1) that

$$
\| A x \| _ { \mathbf { v } } \leq f ( A ) \| x \| _ { \mathbf { v } }\tag{3}
$$

for all nonzero $\pmb { x } \in \mathbb { C } ^ { n }$ and any $A \in \mathbb { C } ^ { n \times n }$ . Using Eq. (3) once more (with respect to B), we have

$$
f ( A B ) \leq f ( A ) \| B \mathbf { x } _ { 0 } \| _ { \mathbf { v } } \leq f ( A ) f ( B ) \| \mathbf { x } _ { 0 } \| _ { \mathbf { v } } = f ( A ) f ( B ) ,
$$

and the property (10.3.1) holds. Part (a) of the theorem is thus proved and we may write $f ( A ) = \left\| A \right\|$

Observe that part (b) of the theorem is just the relation (3). For part (c) we have, with an element $\pmb { x } _ { 0 }$ defined as in Exercise 1(b),

$$
\| A \| = f ( A ) = \| A \pmb { x } _ { 0 } \| _ { \mathbf { v } } \leq \| A \| _ { 1 } \| \pmb { x } _ { 0 } \| _ { \mathbf { v } } = \| A \| _ { 1 } ,
$$

for any matrix norm compatible with $\Vert \begin{array} { r l } { \Vert } & { { } \Vert _ { \mathbf { v } } . \quad \mathbf { U } } \end{array}$

Exercise 2. Verify that $\| I \| = 1$ for any induced matrix norm.

Exercise 3. Let $N _ { n } \in \mathbb { C } ^ { n \times n }$ denote a matrix with ones in the i, i + 1st positions $( 1 \leq i \leq n - 1 )$ and zeros elsewhere. Check that there are induced matrix norms such that

$$
\mathrm { ( a ) } \quad \| N _ { n } \| = n ; \qquad \mathrm { ( b ) } \quad \| N _ { n } \| = 1 ; \qquad \mathrm { ( c ) } \quad \| N _ { n } \| < 1 .
$$

Hint. Consider the vector norm of Exercise 10.2.1 for part (a) and the norms

$$
\| { \pmb x } \| _ { \mathfrak { v } } = \biggl ( \frac { 1 } { k } \biggr ) ^ { n - 1 } | x _ { 1 } | + \biggl ( \frac { 1 } { k } \biggr ) ^ { n - 2 } | x _ { 2 } | + \cdots + \frac { 1 } { k } | x _ { n - 1 } | + | x _ { n } |
$$

with $k = 1$ and $k > 1$ for parts (b) and (c), respectively. □

Some of the most important and useful matrix norms are the induced norms discussed in the next exercises. In particular, the matrix norm induced by the euclidean vector norm is known as the spectral norm, and it is probably the most widely used norm in matrix analysis.

Exercise 4. If A is a unitary matrix, show that the spectral norm of A is 1.

Exercise 5. Let $A \in \mathbb { C } ^ { n \times n }$ and let $\lambda _ { A }$ be the spectral radius of $A ^ { * } A$ If $\big \| \bigstar \bigstar \bigstar$ denotes the spectral norm, show that $\| A \| _ { s } = \lambda _ { A } ^ { 1 / 2 }$ . (In other words, $\left. A \right. _ { s }$ is just the largest singular value of A.)

SOLUTION. The matrix $A ^ { * } A$ is positive semi-definite and therefore its eigenvalues are nonnegative numbers. Hence $\lambda _ { A }$ is actually an eigenvalue of $A ^ { * } A$

Let $\pmb { x } _ { 1 } , \ \pmb { x } _ { 2 } , \ldots , \ \pmb { x } _ { n }$ be a set of orthonormal eigenvectors of $A ^ { * } A$ with associated eigenvalues $0 \leq \lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n }$ . Note that $\lambda _ { 1 } = \lambda _ { n }$ and if $\begin{array} { r } { { \pmb x } = \sum _ { i = 1 } ^ { n } \alpha _ { i } { \pmb x } _ { i } } \end{array}$ , then $\begin{array} { r } { A ^ { * } A { \bf x } = \sum _ { i = 1 } ^ { n } \alpha _ { i } \lambda _ { i } \pmb { x } _ { i } } \end{array}$ . Let $\Vert \big \Vert \big \Vert \big \Vert _ { \mathrm { ~ E ~ } }$ denote the euclidean vector norm on C". Then

$$
\| A { \pmb x } \| _ { \mathrm { E } } ^ { 2 } = ( A { \pmb x } , A { \pmb x } ) = ( { \pmb x } , A ^ { * } A { \pmb x } ) = \sum _ { i = 1 } ^ { n } | \alpha _ { i } | ^ { 2 } \lambda _ { i } .
$$

For $\pmb { x } \in \mathbb { C } ^ { n }$ such that $\| { \pmb x } \| _ { \mathbf { E } } = 1$ , that is, $\sum _ { i = 1 } ^ { n } \vert \alpha _ { i } \vert ^ { 2 } = 1$ , the expression above does not exceed $\lambda _ { n }$ and attains this value if $\alpha _ { 1 } = \alpha _ { 2 } = \cdot \cdot \cdot = \alpha _ { n - 1 } = 0$ and $\mathfrak { X } _ { n } = 1$ . Thus

$$
\left\| A \right\| _ { \mathrm { s } } = \operatorname* { m a x } _ { \left\| \mathbf { x } \right\| _ { \mathrm { E } } = 1 } \left\| A \mathbf { x } \right\| _ { \mathrm { E } } = \lambda _ { n } ^ { 1 / 2 } = \lambda _ { A } ^ { 1 / 2 } .
$$

Exercise 6. If $A = \mathrm { d i a g } [ d _ { 1 } , d _ { 2 } , \dots , d _ { n } ]$ and $\parallel \parallel$ is a matrix norm induced by one of the Hölder norms of Exercise 10.1.2(d), show that

$$
\| A \| = \operatorname* { m a x } _ { 1 \leq j \leq n } | d _ { j } | .
$$

Exercise 7. If $A , U \in \mathbb { C } ^ { n \times n }$ and U is unitary, prove that, for both the euclidean matrix and spectral norms $\| A \| = \| U A \| = \| A U \|$ and hence that, for these two norms, $\| A \|$ is invariant under unitary similarity transformations.

Hint. For the euclidean norm use Exercise 10.3.7(c); for the spectral norm use Exercises 4 and 10.1.6.

Exercise 8. If A is a normal matrix in $\mathbb { C } ^ { n \times n }$ and $\parallel \parallel _ { \mathbf { s } }$ denotes the spectral norm, prove that $\left\| A \right\| _ { \mathbf { s } } = \mu _ { A }$ , the spectral radius of A. (Compare this result with Theorem 10.3.1.) If f is a complex-valued function defined on the spectrum of A, prove that $\| f ( A ) \|$ is equal to the spectral radius of $f ( A )$

Hint. Use Theorem 5.2.1.

Exercise 9. Show that the matrix norm $\| \bigstar \bigstar \| _ { \rho }$ induced by the vector norm $\bigstar \bigstar \bigstar \bigstar | _ { \bigstar \bigstar }$ of Exercise 10.1.2 is given by

$$
\| A \| _ { \rho } = \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } | a _ { i j } | .
$$

(Note that we form the row sums of the absolute values of the matrix elements, and then take the greatest of these sums.)

SOLUTION. Let $\pmb { x } = [ x _ { 1 } \quad x _ { 2 } \quad \cdot \cdot \cdot \quad x _ { n } ] ^ { \mathrm { \bf T } }$ be a vector in $\mathbb { C } ^ { n }$ with $\| \pmb { x } \| _ { \infty } = 1$ Then

$$
\left\| A x \right\| _ { \infty } = \operatorname* { m a x } _ { 1 \leq i \leq n } \left| \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } \right| \leq \operatorname* { m a x } _ { 1 \leq i \leq n } \sum _ { j = 1 } ^ { n } \left| a _ { i j } \right| \left| x _ { j } \right| \leq \left\| x \right\| _ { \infty } \left\| A \right\| _ { \rho } = \left\| A \right\| _ { \rho } .
$$

Thus,

$$
\operatorname* { m a x } _ { \| \mathbf { x } \| _ { \infty } = 1 } \| A \mathbf { x } \| _ { \infty } \leq \| A \| _ { p } ,
$$

and so the norm induced by $\bigstar \bigstar \bigstar \bigstar | | _ { \infty }$ cannot exceed $\| A \| _ { \rho }$ . To prove that they are equal we have only to show that there is an $\pmb { x } _ { 0 } \in \mathbb { C } ^ { n }$ with $\| \pmb { x } _ { 0 } \| _ { \infty } = 1$ and $\| A \mathbf { x } _ { 0 } \| _ { \infty } \geq \| A \| _ { \rho }$ . It is easy to see that if $\begin{array} { r } { \left. A \right. _ { \rho } = \sum _ { j = 1 } ^ { n } \left. a _ { k j } \right. } \end{array}$ , then the vector $\begin{array} { r } { \pmb { x } _ { 0 } = [ { \pmb { \alpha } } _ { 1 } \quad { \pmb { \alpha } } _ { 2 } \quad \cdot \cdot \cdot \quad { \pmb { \alpha } } _ { n } ] ^ { \mathbf { T } } } \end{array}$ , where

$$
\alpha _ { j } = \left\{ \begin{array} { l l } { \displaystyle \frac { | a _ { k j } | } { a _ { k j } } \quad } & { \mathrm { i f } \quad a _ { k j } \neq 0 , } \\ { \quad } & { } \\ { 0 \quad } & { \mathrm { i f } \quad a _ { k j } = 0 , } \end{array} \right.
$$

$j = 1 , 2 , \dots , n ,$ satisfies the above conditions.

Exercise 10. Show that the matrix norm induced by the vector norm ∥ i of Exercise 10.1.2 is given by

$$
\| A \| _ { \gamma } = \operatorname* { m a x } _ { 1 \leq j \leq n } \ \sum _ { i = 1 } ^ { n } | a _ { i j } | .
$$

(Note that we form the column sums of the absolute values of the matrix elements, and then take the greatest of these sums.)

Hint. Use the fact that $\left\| A \right\| _ { \gamma } = \left\| A ^ { * } \right\| _ { \rho }$

Exercise 11. $\mathbf { I f } \parallel \mathbf { \Sigma } \parallel _ { \mathbf { s } }$ denotes the spectral norm and $\| \bigstar \bigstar \| _ { \rho }$ and $\parallel \parallel _ { \chi }$ are as defined in Exercises 9 and 10, prove that

$$
\begin{array} { r } { \| A \| _ { s } ^ { 2 } \leq \| A \| _ { \rho } \| A \| _ { \gamma } . } \end{array}
$$

SoLUTION. Using the result of Exercise 5, we have $\| A \| _ { \mathsf { s } } = \lambda _ { A } ^ { 1 / 2 }$ , where $\lambda _ { A }$ is the maximum eigenvalue of $A ^ { * } A$ . Since $A ^ { * } A$ is positive semidefinite, $\lambda _ { A }$ is just the spectral radius of $A ^ { * } A$ By Theorem 10.3.1, $\lambda _ { A } \leq \| A ^ { * } A \| _ { \gamma }$ . Thus

$$
\begin{array} { r } { \| A \| _ { \ L ^ { 2 } } ^ { 2 } \leq \| A ^ { * } A \| _ { \ L ^ { \gamma } } \leq \| A ^ { * } \| _ { \ L ^ { \gamma } } \| A \| _ { \ L ^ { \gamma } } = \| A \| _ { \ L _ { \rho } } \| A \| _ { \ L _ { \gamma } } \relax \prod } \end{array}
$$

Before leaving the idea of inducing matrix norms from vector norms, we ask the converse question: Given a matrix norm $\parallel \parallel .$ , can we use it to induce a compatible vector norm? This can be done by defining∥ l, by

$$
\| \pmb { x } \| _ { \mathbf { v } } = \| \pmb { x } \pmb { a } ^ { \top } \|\tag{4}
$$

for some fixed nonzero vector a.

Exercise 12. Let

$$
A = \left[ { 3 / 2 \ - 1 / 2 } \atop { - 1 / 2 \ } \right] .
$$

Use Exercise 11 to show that $\left\| A \right\| _ { s } \leq 2$ and Exercise 8 to show that $\| A \| _ { s } = ( 5 + { \sqrt { 5 } } ) / 4 \simeq 1 . 8$

Exercise 13. Consider an $n \times n$ matrix with block diagonal form, $A = \mathrm { d i a g } [ A _ { 1 } \quad A _ { 2 } ]$ , where $A _ { 1 }$ and $A _ { 2 }$ are square matrices. Show that, in the spectral norm,

$$
\| A \| = \operatorname* { m a x } ( \| A _ { 1 } \| , \| A _ { 2 } \| ) .
$$

Exercise 14. Let $A \in \mathbb { C } ^ { n \times n }$ and consider a Hermitian matrix of the form

$$
H = \biggl [ \begin{array} { c c } { { 0 } } & { { i A \biggr ] } } \\ { { - i A ^ { * } } } & { { \theta \biggr ] . } } \end{array}
$$

Show that $\| H \| = \| A \|$ , in the spectral norm. □

## 10.5 Absolute Vector Norms and Lower Bounds of a Matrix

Almost all the vector norms we have introduced in the exercises depend only on the absolute values of the elements of the vector argument. Such norms are called absolute vector norms. The general theory of norms that we have developed up to now does not assume that this is necessarily the case. We shall devote the first part of this section to proving two properties of absolute vector norms.

One of the properties of an absolute vector norm that we shall establish is called the monotonic property. Let us denote by $| { \pmb x } |$ the vector whose elements are the absolute values of the components of $\mathbf { \delta x } ,$ and if $\pmb { x } _ { 1 } , \pmb { x } _ { 2 } \in \mathbb { R } ^ { n }$ we shall say that ${ \pmb x } _ { 1 } \leq { \pmb x } _ { 2 } \left( \mathrm { o r } { \pmb x } _ { 2 } \geq { \pmb x } _ { 1 } \right)$ if this relation holds for corresponding components of $\mathbf { x } _ { 1 }$ and $\pmb { x } _ { 2 } . \mathbf { A }$ vector norm $\Vert \ \Vert _ { \textbf { v } }$ on $\mathbb { C } ^ { n }$ is said to be monotonic if $| x _ { 1 } | \leq | x _ { 2 } |$ implies $\left\| { \pmb x } _ { 1 } \right\| _ { \mathbf { v } } \leq \left\| { \pmb x } _ { 2 } \right\| _ { \mathbf { v } }$ for any $\pmb { x } _ { 1 } , \pmb { x } _ { 2 } \in \mathbb { C } ^ { n }$

The second property we will develop concerns the induced matrix norm. When a matrix norm is evaluated at a diagonal matrix

$$
D = \mathrm { d i a g } [ d _ { 1 } , d _ { 2 } , \ldots , d _ { n } ] ,
$$

we think highly of the norm if it has the property $\| D \| = \operatorname* { m a x } _ { j } | d _ { j } |$ We will show that $\parallel \parallel$ has this property if and only if it is a norm induced by an absolute vector norm.

Theorem 1 (F. L. Bauer, J. Stoer, and C. Witzgall†). $I f \ \parallel \mathbf { \Sigma } \parallel _ { \mathbf { v } }$ is a vector norm in $\mathbb { C } ^ { n }$ and $\bigstar \bigstar \bigstar | \bigstar \bigstar | |$ denotes the matrix norm induced $b y \parallel \mathbf { \parallel } _ { \mathbf { v } } ,$ then the following conditions are equivalent :

(a) $\Vert \big | \big | \big | _ { \mathbf { v } }$ is an absolute vector norm;

(b) $\Vert \mathbf { \Omega } \Vert _ { \mathbf { v } }$ is monotonic;

(c) $\| D \| = \operatorname* { m a x } _ { 1 \leq j \leq n } | d _ { j } |$ for any diagonal matrix

$$
D = \mathrm { d i a g } [ d _ { 1 } , d _ { 2 } , \dots , d _ { n } ]
$$

from $\mathbb { C } ^ { n \times n }$

PROOF. $( a ) \Rightarrow ( b )$ We shall prove that if $\parallel \parallel _ { \mathbf { v } }$ is an absolute vector norm and $\| \pmb { x } \| _ { \mathbf { v } } = F ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ , where $\mathbf { x } = [ x _ { 1 } \quad x _ { 2 } \quad \cdots \quad x _ { n } ] ^ { \mathrm { { T } } } $ then F is a nondecreasing function of the absolute values of $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ . Let us focus attention on $F$ as a function of the first component, $x _ { 1 }$ . The same argument will apply to each of the n variables. Thus, we suppose that $x _ { 2 } , x _ { 3 } , \ldots , x _ { n }$ are fixed, define

$$
f ( x ) = F ( x , x _ { 2 } , x _ { 3 } , \ldots , x _ { n } )
$$

and consider the behaviour of $f ( x )$ as x varies through the real numbers.

If the statement in part (b) is false, there exist nonnegative numbers $p , q$ for which $p < q$ and $f ( p ) > f ( q )$ . Now since $f ( x ) = f ( | x | )$ , we have $f ( - q ) = f ( q ) ,$ and so the vectors $\pmb { x } _ { 1 } = [ - q \quad x _ { 2 } \quad \cdot \cdot \cdot \quad x _ { n } ] ^ { \mathbf { T } }$ and $\mathbf { x } _ { 2 } = [ q \quad x _ { 2 } \quad \ldots \quad x _ { n } ] ^ { \mathrm { T } }$ belong to the ball consisting of vectors x for which $\| { \pmb x } \| _ { \mathbf { v } } \le f ( q )$ . This ball is convex (Exercise 10.2.2) and since the vector $\mathbf { x } _ { 0 } = [ p \quad x _ { 2 } \quad \cdots \quad x _ { n } ] ^ { \mathrm { T } }$ can be written in the form ${ \pmb x } _ { 0 } = t { \pmb x } _ { 1 } + ( 1 - t ) { \pmb x } _ { 2 }$ for some $t \in [ 0 , 1 ]$ , then $\mathbf { \delta x } _ { 0 }$ also belongs to the ball. Thus $\| \ b { x } _ { 0 } \| _ { \mathbf { v } } \leq f ( q )$ . But $\| \mathbf { x } _ { 0 } \| _ { \mathbf { v } } = f ( p ) > f ( q )$ , so we arrive at a contradiction and the implication $( a ) \Rightarrow ( b )$ is proved.

$( b ) \Rightarrow ( c )$ Suppose without loss of generality that $D \neq O$ and define $d = \operatorname* { m a x } _ { 1 \leq j \leq n } | d _ { j } |$ . Clearly, $| D \pmb { x } | \leq | d \pmb { x } |$ for all $\pmb { x } \in \mathbb { C } ^ { n }$ and so condition (b) implies that $\left\| D \mathbf { x } \right\| _ { \mathbf { v } } \leq \| d \mathbf { x } \| _ { \mathbf { v } } = d \| \mathbf { x } \| _ { \mathbf { v } }$ . Thus

$$
\left\| D \right\| = \operatorname* { s u p } _ { x \neq 0 } { \frac { \left\| D x \right\| _ { v } } { \left\| x \right\| _ { v } } } \leq d .
$$

If we can show that there is an $\pmb { x } _ { 0 } \in \mathbb { C } ^ { n }$ for which $\| D \pmb { x } _ { 0 } \| _ { \mathbf { v } } / \| \pmb { x } _ { 0 } \| _ { \mathbf { v } } = d _ { 2 }$ the proof will be complete. Suppose that m is an integer for which $d = | d _ { m } |$ . Then

$$
{ \frac { \| D e _ { m } \| _ { \mathrm { v } } } { \| e _ { m } \| _ { \mathrm { v } } } } = { \frac { \| d _ { m } e _ { m } \| _ { \mathrm { v } } } { \| e _ { m } \| _ { \mathrm { v } } } } = | d _ { m } | = d ,
$$

where $e _ { m }$ is the mth unit vector in $\mathbb { C } ^ { n } .$ Hence

$$
\left\| D \right\| = \operatorname* { m a x } _ { \mathbf { x } \neq \mathbf { 0 } } { \frac { \| D \mathbf { x } \| _ { \mathbf { v } } } { \| \mathbf { x } \| _ { \mathbf { v } } } } = d ,
$$

and (c) follows from (b).

$( c ) \Rightarrow ( a )$ Suppose that the condition (c) holds; let $\mathbf { x } = [ x _ { 1 } \quad x _ { 2 } \quad \cdots \quad x _ { n } ] ^ { \mathrm { T } }$ Choosing $d _ { j } = 1 \mathrm { i f } x _ { j } = 0$ and $d _ { j } = | x _ { j } | / x _ { j } \mathrm { i f } x _ { j } \neq 0 .$ , we see that for any $\boldsymbol { x } \in \mathbb { C } ^ { n }$ there is a diagonal matrix $D = \dot { \mathrm { d i a g } } [ d _ { 1 } , d _ { 2 } , \dots , d _ { n } ]$ such that $| { \pmb x } | = D { \pmb x }$ Hence property (c) yields $\| D \| = \| D ^ { - 1 } \| = 1$ . We then have

$$
\left\| ~ | ~ \mathbf { x } | ~ \right\| _ { \mathbf { v } } = ~ \left\| D \mathbf { x } \right\| _ { \mathbf { v } } \leq ~ \left\| D \right\| ~ \left\| \mathbf { x } \right\| _ { \mathbf { v } } = ~ \left\| \mathbf { x } \right\| _ { \mathbf { v } }
$$

and since ${ \pmb x } = D ^ { - 1 } | { \pmb x } |$ , it follows that

$$
\| { \boldsymbol { \mathbf { x } } } \| _ { \mathbf { \check { v } } } \leq \| { \boldsymbol { D } } ^ { - 1 } \| \mathbf { \check { \phi } } \| | { \boldsymbol { \mathbf { \mathit { x } } } } | \| _ { \mathbf { \check { v } } } = \| \mathbf { \phi } | { \boldsymbol { \mathbf { \mathit { x } } } } | \| _ { \mathbf { \check { v } } }
$$

Thus $\| { \pmb x } \| _ { \mathbf { v } } = \| { \mathbf \alpha } \| { \pmb x } \| \| ,$ for any $\pmb { x } \in \mathbb { C } ^ { n }$ , and so (c) implies (a). This completes the proof.

Exercise 1. $\mathbf { I f } \parallel \parallel$ is a matrix norm induced by an absolute vector norm and $\left| A \right|$ is the matrix with elements $| a _ { i j } | ,$ show that $\| A \| < \| \left| A \right| \|$

Hint. Use Eq. (10.4.2).

Proceeding to the second topic of this section, recall that our discussion of norms was started by looking for a measure of magnitude or a measure of the departure of an element from the zero element. Confining our attention to matrix norms, a measure of departure of a matrix from singularity (rather than the zero-matrix) would also be useful. Thus we seek a nonnegative function that is defined on all square matrices A and that is zero if and only if det $A = 0$ . At first sight, it is surprising that such a measure should be obtained from a definition complementary to that of the induced norm given in Eq. (10.4.1). At second sight it is less surprising, because we know that there is an $\pmb { x } \neq \pmb { \theta }$ with $A \pmb { x } = \pmb { \theta }$ if and only if det $A = 0$ . We define the lower bound of A, written l(A), with respect to the vector norm $\Vert \bigstar \bigstar \Vert _ { \mathbf { v } } .$ by

$$
l ( A ) = \operatorname* { i n f } _ { \mathbf { x } \in \mathbb { C } ^ { n } , \mathbf { x } \neq \mathbf { 0 } } \frac { \| A \mathbf { x } \| _ { \mathrm { v } } } { \| \mathbf { x } \| _ { \mathrm { v } } } .\tag{1}
$$

If we accept the idea that $\| A ^ { - 1 } \|$ increases indefinitely in magnitude as A approaches a singular matrix, then the next theorem justifies our claim that the lower bound is a measure of departure from singularity.

Theorem 2. $I f \ \sharp \ \sharp$ is the matrix norm induced by the vector norm l  and l is the corresponding lower bound, then

$$
I ( A ) = { \left\{ \begin{array} { l l } { 1 / \| A ^ { - 1 } \| } & { i f \quad { \operatorname* { d e t } } \ A \neq 0 , } \\ { 0 } & { i f \quad { \operatorname* { d e t } } \ A = 0 . } \end{array} \right. }
$$

PROOF. If det $A \neq 0 .$ , define a vector y in terms of a vector x by ${ \mathfrak { y } } = A { \mathfrak { x } } .$ Then for any ${ \pmb x } \neq { \pmb 0 } , { \pmb y } \neq { \pmb 0 } ,$

$$
l ( A ) = \operatorname* { i n f } \frac { \lvert A \mathbf { x } \rvert | _ { \mathbf { v } } } { \lvert | \mathbf { x } \rvert | _ { \mathbf { v } } } = \operatorname* { i n f } \frac { \lvert | \mathbf { y } \rvert | _ { \mathbf { v } } } { \lvert | A ^ { - 1 } \mathbf { y } \rvert | _ { \mathbf { v } } } = \left( \operatorname* { s u p } \frac { \lvert | A ^ { - 1 } \mathbf { y } \rvert | _ { \mathbf { v } } } { \lvert | \mathbf { y } \rvert | _ { \mathbf { v } } } \right) ^ { - 1 } = \frac { 1 } { \lvert | A ^ { - 1 } \rvert | } .
$$

If det $A = 0 ,$ there is an $\pmb { x } _ { 0 } \in \mathbb { C } ^ { n }$ such that $A \pmb { x } _ { 0 } = \pmb { \theta }$ and $\| \pmb { x } _ { 0 } \| _ { \mathbf { v } } = 1$ . Then obviously $l ( A ) = 0$ by the definition of l(A).■

Corollary 1. If A, $\boldsymbol { B } \in \mathbb { C } ^ { n \times n }$ , then

$$
l ( A B ) \geq l ( A ) l ( B ) .
$$

Corollary 2. $I f \parallel \mathbf { \Sigma } \parallel _ { \mathbf { v } }$ is an absolute norm and

$$
D = \mathrm { d i a g } [ d _ { 1 } , d _ { 2 } , \dotsc , d _ { n } ] \in \mathbb { C } ^ { n \times n } ,
$$

then

$$
l ( D ) = \operatorname* { m i n } _ { 1 \leq j \leq n } | d _ { j } | .
$$

PrOOF. If D is nonsingular, then $d _ { j } \neq 0$ for each j and, using Theorems 2 and 1,

$$
l ( D ) = \frac { 1 } { \Vert D \Vert ^ { - 1 } } = \frac { 1 } { \underset { 1 \leq j \leq n } { \operatorname* { m a x } } \ ( 1 / \Vert d _ { j } \vert ) } = \ \underset { 1 \leq j \leq n } { \operatorname* { m i n } } \ \vert d _ { j } \vert .
$$

If det $D = 0 ;$ , then $l ( D ) = 0$ and obviously min $\mid _ { 1 \leq j \leq n } \mid d _ { j } \mid = 0$ also.■

Exercise 2. Let $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ be the eigenvalues of $A \in \mathbb { C } ^ { n \times n }$ . Prove that, with respect to any vector norm ∥ lv ,

$$
l ( A ) \leq \operatorname* { m i n } _ { 1 \leq j \leq n } | \lambda _ { j } | .
$$

Prove also that equality obtains if A is normal and $\parallel \parallel _ { \mathbf { v } }$ is the euclidean vector norm. □

Note that by combining the result of Exercise 2 with Theorem 10.3.1, we can define an annular region of the complex plane within which the eigenvalues of A must lie.

Exercise 3. Show that if A is nonsingular then, in the notation of Theorem 2,

$$
\| A \mathbf { x } \| _ { \mathrm { v } } \geq l ( A ) \| \mathbf { x } \| _ { \mathrm { v } } . \quad \bigtriangledown
$$

## 10.6 The Geršgorin Theorem

A description of regions of the complex plane containing the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ of a matrix $A \in \mathbb { C } ^ { n \times n }$ is presented in this section. Recall that a first result of this kind was obtained in Theorem 10.3.1 (see also Exercise 10.5.2).

Before entering into further details, let us point out the essential fact that the eigenvalues of matrix A depend continuously on the elements of A. Since the eigenvalues are just the zeros of the characteristic polynomial, this result follows immediately once it is known that the zeros of a polynomial depend continuously on its coefficients. This is a result of the elementary theory of algebraic functions and will not be pursued here.

We now prove one of the most useful and easily applied theorems that give bounds for eigenvalues. This is known as Geršgorin's theorem and was first published as recently as 1931†

Theorem 1. If $A \in \mathbb { C } ^ { n \times n }$ and $a _ { j k }$ denotes the elements of $A , j , k = 1 , \ldots , n ,$ and

$$
\rho _ { j } = \sum _ { k } | a _ { j k } | ,
$$

where $\sum \limits _ { k } ^ { \prime }$ denotes the sum from k = 1 to n, $k \neq j ,$ then every eigenvalue of A lies in at least one of the disks

$$
\{ z : | z - a _ { j j } | \leq \rho _ { j } \} , ~ j = 1 , 2 , \ldots , n ,\tag{1}
$$

in the complex z-plane.

Furthermore, a set of m disks having no point in common with the remaining n – m disks contains m and only m eigenvalues of A.

ProoF. Let λ be an eigenvalue of A with the associated eigenvector x. Then $A { \boldsymbol { \mathbf { x } } } = \lambda { \boldsymbol { \mathbf { x } } }$ or, writing this relation out as n scalar equations,

$$
\sum _ { k = 1 } ^ { n } a _ { j k } x _ { k } = \lambda x _ { j } , \qquad j = 1 , 2 , \ldots , n .
$$

Let $\vert x _ { p } \vert = \mathrm { m a x } _ { j } \vert x _ { j } \vert$ ; then the pth equation gives

$$
| \lambda - a _ { p p } | | x _ { p } | = \left| \sum _ { k = 1 } ^ { n } a _ { p k } x _ { k } \right| \leq \sum _ { k = 1 } ^ { n } | a _ { p k } | | x _ { k } | \leq | x _ { p } | \sum _ { k = 1 } ^ { n } | a _ { p k } | .
$$

Now since $\pmb { x } \neq \pmb { \theta }$ it must be that $| x _ { p } | \neq 0 .$ , and so we have $| \lambda - a _ { p p } | \leq \rho _ { p }$ The first result is proved.

Suppose now that $A = D + C$ where $D = \mathrm { d i a g } [ a _ { 1 1 } , \dotsc , a _ { n n } ]$ , and let $B ( t ) = D + t C$ Then $B ( 0 ) = D$ and $B ( 1 ) = A$ We consider the behaviour of the eigenvalues of B(t) as t varies in the interval [0, 1] and use the continuity of the eigenvalues as functions of t. Thus, for any t in this interval, the eigenvalues of $B ( t )$ lie in the disks with centers $a _ { j j }$ and radii $t \rho _ { j } , j = 1 , 2 , \ldots , n ,$

Now suppose that the jth disk of $A = B ( 1 )$ has no point in common with the remaining $n - 1$ disks. Then it is obviously true that the jth disk of B(t) is isolated from the rest for all t in [0, 1]. Now when $t = 0 ,$ the eigenvalues of $B ( 0 )$ are $a _ { 1 1 } , \ldots , a _ { n n }$ and, of these, $a _ { j j }$ is the only one in the jth (degenerate) disk. Since the eigenvalues of $B ( t )$ are continuous functions of $t ,$ and the jth disk is always isolated from the rest, it follows that there is one and only one eigenvalue of $B ( t )$ in the jth disk for all $t \in [ 0 , 1 ]$ . In particular, this is the case when $t = 1$ and $B ( 1 ) = A$

This proves the second part of the theorem for $m = 1$ . The completion of the proof for any $m \leq n$ is left as an exercise.

Note that by applying the theorem to $A ^ { \boldsymbol { \mathsf { T } } } ,$ , a similar result is obtained using column sums of A, rather than row sums, to define the radii of the new disks. The n disks in (1) are often referred to as the Geršgorin disks.

Exercise 1. Sketch the Geršgorin disks for the following matrix and for its transpose:

$$
A = { \left[ \begin{array} { l l l l } { 0 } & { 1 } & { 0 } & { i } \\ { 1 } & { 6 } & { 1 } & { 1 } \\ { { \frac { 1 } { 2 } } i } & { i } & { 5 i } & { 0 } \\ { 0 } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { - 2 } \end{array} \right] } .
$$

$\mathrm { I f } \ S = \mathrm { d i a g } [ 1 , 1 , 1 , 4 ]$ , compute $S A S ^ { - 1 }$ and deduce that A has an eigenvalue in the disk $| z + 2 | \leq { \frac { 1 } { 2 } }$

Exercise 2. If $A \in \mathbb { C } ^ { n \times n }$ , show that the eigenvalues of A lie in the disk $\left\{ z \in \mathbb { C } { : } | z | \leq \operatorname* { m i n } ( \rho , \nu ) \right\}$ , where

$$
\rho = \operatorname* { m a x } _ { 1 \leq j \leq n } \sum _ { k = 1 } ^ { n } | a _ { j k } | , \qquad \nu = \operatorname* { m a x } _ { 1 \leq k \leq n } \sum _ { j = 1 } ^ { n } | a _ { j k } | .\tag{2}
$$

SOLUTION. For any eigenvalue $\lambda _ { i }$ of $A \left( 1 \leq i \leq n \right)$

$$
| \lambda _ { i } | - | a _ { j j } | \leq | \lambda - a _ { j j } | \leq \rho _ { j } .
$$

Therefore

$$
| \lambda _ { i } | \leq \rho _ { j } + | a _ { j j } | = \sum _ { k = 1 } ^ { n } | a _ { j k } | \leq \rho .
$$

A similar proof can be performed for column sums, and the result follows.□

Note that $\rho$ in Eq. (2) can be viewed as the matrix norm induced by the vector norm $\| \pmb { x } \| _ { \infty }$ (Exercise 10.4.9) and similarly for v (Exercise 10.4.10). This shows that the result of Exercise 2 is a particular case of Theorem 10.3.1 (for a special norm).

Exercise 3. With the notation of Eq. (2), prove that

$$
| \mathbf { d e t } \ A | \leq \operatorname* { m i n } ( \rho ^ { n } , \nu ^ { n } )
$$

for any $A \in \mathbb { C } ^ { n \times n } , \quad \bigsqcup$

A matrix $\ b { A } = [ a _ { j k } ] _ { j , k = 1 } ^ { n } \in \mathbb { C } ^ { n \times n }$ is said to be diagonally dominant if

$$
| a _ { j j } | > \sum _ { k = 1 } ^ { n } \left| a _ { j k } \right| = \rho _ { j }
$$

for all $j = 1 , 2 , \dots , n .$ In other words, if

$$
\begin{array} { c } { d _ { j } = \vert a _ { j j } \vert - \rho _ { j } , \qquad j = 1 , 2 , \dotsc , n , } \\ { d = \underset { 1 \leq j \leq n } { \operatorname* { m i n } } d _ { j } , } \end{array}\tag{3}
$$

then A is diagonally dominant if and only if $d > 0$

Exercise 4. Let A be diagonally dominant and $\lambda _ { i }$ be an eigenvalue of A. With the previous notation, show that $| \lambda _ { i } | \geq d , i = 1 , 2 , \ldots , n ,$ and hence that |det $A | \geq d ^ { n } .$ In particular, confirm the nonsingularity of any diagonally dominant matrix, and illustrate with the matrix of Exercise 4.11.10. (The nonsingularity of a diagonally dominant matrix is sometimes referred to as the Lévy-Desplanques-Hadamard theorem.)

Hint. Consider the matrix $B = ( 1 / d ) A$ and apply Theorem 1 to show that $| \mu _ { j } | \geq 1$ for any $\mu _ { j } \in \sigma ( B )$

Exercise 5. Prove that an Hermitian matrix that is diagonally dominant and has all positive diagonal elements is positive definite.

Exercise 6. If $A = B + C$ , where B = diag[1, 2, 2] and $\begin{array} { r } { | c _ { j k } | \le \varepsilon < \frac { 1 } { 6 } } \end{array}$ for $j , k = 1 , 2 , 3$ , prove that there is an eigenvalue of A in the disk

$$
| z - 1 - c _ { 1 1 } | \leq 1 2 \varepsilon ^ { 2 } .
$$

Exercise 7. This is a generalization of Exercise 6. If $A = B + C ,$ where $\begin{array} { r } { B = \mathrm { d i a g } [ b _ { 1 } , \dotsc , b _ { n } ] , \rho _ { j } = \operatorname* { m i n } _ { k \neq j } | b _ { j } - b _ { k } | > 0 , } \end{array}$ and $| c _ { j k } | \le \varepsilon < \beta _ { j } / 2 n$ for $j , k = 1 , 2 , \ldots , n ,$ prove that there is an eigenvalue of A in the disk

$$
| z - b _ { j } - c _ { j j } | \leq 2 n ( n - 1 ) \varepsilon ^ { 2 } / \beta _ { j } .
$$

Exercise 8. If $f ( z ) = a _ { 0 } + a _ { 1 } z + \cdots + a _ { l } z ^ { l } , a _ { l } \neq 0 $ and $z _ { 0 }$ is a zero of $f ,$ prove that

$$
| z _ { 0 } | \leq 1 + \operatorname* { m a x } _ { k } | a _ { k } / a _ { l } | . \quad \bigsqcup
$$

The localization of eigenvalues of a simple matrix will be discussed in Section 11.2.

## 10.7 Geršgorin Disks and Irreducible Matrices

In this section two useful results are presented that can be seen as refinements of Geršgorin's theorem. However, they both involve the further hypothesis that the matrix in question be “irreducible." This is a property that is easily seen to hold in many practical problems. We make a formal definition here and return for further discussion of the concept in Chapter 15.

If $n \geq 2 ,$ , the matrix $A \in \mathbb { C } ^ { n \times n }$ is said to be reducible if there is an $n \times n$ permutation matrix P such that

$$
P ^ { \mathrm { T } } A P = { \left[ \begin{array} { l l } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} \right] } ,\tag{1}
$$

where $A _ { 1 1 }$ and $A _ { 2 2 }$ are square matrices of order less than n. If no such P exists then A is irreducible.

If A is considered to be a representation of a linear transformation $T$ on an n-dimensional space ${ \mathcal { S } } _ { : }$ the fact that A is irreducible simply means that, among the basis vectors for $\mathcal { S }$ chosen for this representation, there is no proper subset that spans an invariant subspace of A (see Section 4.8 and Eq. (4.8.3) in particular).

Exercise 1. If $A \in \mathbb { R } ^ { n \times n }$ is reducible, prove that for any positive integer ${ p , }$ the matrix $A ^ { p }$ is reducible. Also, show that any polynomial in A is a reducible matrix.

Exercise 2. Check that the square matrices A and $A ^ { \boldsymbol { \mathsf { T } } }$ are both reducible or both irreducible. □

The first result concerns a test for a matrix $A \in \mathbb { C } ^ { n \times n }$ to be nonsingular. Clearly, Theorem 10.6.1 provides a test (or class of tests) for nonsingularity (see Exercise 10.6.4): A is certainly nonsingular if it is diagonally dominant. In other words, if $\begin{array} { r } { | a _ { j j } | > \sum _ { k \neq j } | a _ { j k } | \mathrm { f o r } j = 1 , 2 , \ldots , n } \end{array}$ , then the origin of the complex plane is excluded from the union of the Geršgorin disks in which $\pmb { \sigma } ( A )$ must lie. These inequalities can be weakened at the expense of the irreducibility hypothesis.

Theorem 1 (O. Taussky†). If $A = [ a _ { j k } ] _ { j , k = 1 } ^ { n }$ is irreducible and

$$
| a _ { j j } | \geq \sum _ { k = 1 , k \neq j } ^ { n } | a _ { j k } | , \qquad j = 1 , 2 , \ldots , n ,\tag{2}
$$

with strict inequality for at least one j, then A is nonsingular.

ProoF. Suppose, on the contrary, that $A \pmb { x } = \pmb { \theta }$ for some

$$
\begin{array} { r } { \mathbf { \boldsymbol { x } } = [ \mathbf { \boldsymbol { x } } _ { 1 } \quad \mathbf { \boldsymbol { x } } _ { 2 } \quad \cdots \quad \mathbf { \boldsymbol { x } } _ { n } ] ^ { \mathrm { { T } } } \neq \mathbf { \boldsymbol { 0 } } . } \end{array}
$$

Clearly, there is a permutation matrix $P \in \mathbb { R } ^ { n \times n }$ such that $P { \bf { x } } = \tilde { { \bf { x } } } ,$ where $\tilde { \mathbf { x } } = [ \dot { \tilde { x } } _ { 1 } \quad \tilde { x } _ { 2 } \quad \cdots \quad \tilde { x } _ { n } ] ^ { \mathrm { T } }$ and either

$$
| \tilde { x } _ { 1 } | = | \tilde { x } _ { 2 } | = \cdot \cdot \cdot = | \tilde { x } _ { n } |\tag{3}
$$

or

$$
| \tilde { x } _ { 1 } | = \cdots = | \tilde { x } _ { r } | > | \tilde { x } _ { r + 1 } | \geq \cdots \geq | \tilde { x } _ { n } | .\tag{4}
$$

Denote $\widetilde { A } = P A P ^ { \mathrm { T } } = [ \widetilde { a } _ { j k } ] _ { j , k = 1 } ^ { n }$ and observe that this simultaneous permutation of rows and columns of A allows us to rewrite Eq. (2) in the form

$$
| \tilde { a } _ { j j } | \geq \sum _ { k = 1 , k \neq j } ^ { n } | \tilde { a } _ { j k } | , \qquad j = 1 , 2 , \ldots , n .\tag{5}
$$

We also have $\widetilde { A } \widetilde { \pmb { x } } = \pmb { \theta }$ and so $\begin{array} { r } { \sum _ { \mathtt { k } = 1 } ^ { n } \tilde { a } _ { j k } \tilde { x } _ { k } = 0 } \end{array}$ for $j = 1 , 2 , \dots , n$ Therefore we obtain, in the case of Eq. (3),

$$
| \widetilde { a } _ { j j } | \left\| x \right\| _ { \infty } = | \widetilde { a } _ { j j } | \left| \widetilde { x } _ { j } \right| = \left| \sum _ { k = 1 , k \neq j } ^ { n } \widetilde { a } _ { j k } \widetilde { x } _ { k } \right| \leq \left( \sum _ { k = 1 , k \neq j } ^ { n } | \widetilde { a } _ { j k } | \right) \left\| x \right\| _ { \infty } , \qquad 1 \leq j \leq n .
$$

Dividing by $\| \mathbf { x } \| _ { \infty } \neq 0 .$ , we then have

$$
| \tilde { a } _ { j j } | \leq \sum _ { k = 1 , k \neq j } ^ { n } | \tilde { a } _ { j k } | , \qquad 1 \leq j \leq n ,
$$

and comparison with (5) gives equalities throughout (5), a contradiction that proves the theorem in this case.

In the case of Eq. (4) we have, for $1 \leq j \leq r .$

$$
\begin{array} { r l r } {  { \vert \tilde { a } _ { j j } \vert  x  _ { \infty } = \vert \tilde { a } _ { j j } \vert  \tilde { x } _ { j }  } } \\ & { } & { =  \displaystyle \sum _ { k = 1 , k \neq j } ^ { n } \tilde { a } _ { j k } \tilde { x } _ { k }  } \\ & { } & { \leq ( \displaystyle \sum _ { k = 1 , k \neq j } ^ { \ell } \vert \tilde { a } _ { j k } \vert ) \Vert x \Vert _ { \infty } + \displaystyle \sum _ { k = r + 1 } ^ { n } \vert \tilde { a } _ { j k } \vert \vert \tilde { x } _ { k } \vert } \\ & { } & { \leq ( \displaystyle \sum _ { k = 1 , k \neq j } ^ { n } \vert \tilde { a } _ { j k } \vert ) \Vert x \Vert _ { \infty } . } \end{array}\tag{6}
$$

Dividing by $\| \mathbf { x } \| _ { \infty } \neq 0$ , we see that

$$
| \tilde { a } _ { j j } | \leq \sum _ { k = 1 , k \neq j } ^ { n } | \tilde { a } _ { j k } | , \qquad 1 \leq j \leq r ,
$$

and comparing with Eq. (5), we obtain equalities in (5) for $j = 1 , 2 , \dots , r .$ Hence it follows from Eq. (6) that

$$
\sum _ { k = r + 1 } ^ { n } | \widetilde { a } _ { j k } | = 0 , \qquad j = 1 , 2 , \ldots , r ,
$$

or, what is equivalent, the matrix A is lower block-triangular. Thus $\tilde { A }$ $A = P ^ { \mathrm { T } } \tilde { A } P$ is reducible and a contradiction is obtained. This proves the theorem.

Exercise 3. Check that the $n \times n$ matrices

$$
{ \left[ \begin{array} { l l l l l } { n } & { 1 } & { 1 } & { \cdots } & { 1 } \\ { 1 } & { 2 } & { 0 } & { \cdots } & { 0 } \\ { 1 } & { 0 } & { 3 } & { \ddots } & { \vdots } \\ { \vdots } & { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 1 } & { 0 } & { \cdots } & { 0 } & { n } \end{array} \right] } ,
$$

$$
\begin{array} { r } { \left[ \begin{array} { l l l l l } { 2 - 1 } & { 0 } & { \cdots } & { 0 } \\ { - 1 } & { 2 } & { - 1 } & { \ddots } & { \vdots } \\ { 0 } & { } & { \ddots } & { \ddots } & { \ddots } \\ { \vdots } & { \ddots } & { } & { } & { - 1 } \\ { 0 } & { \cdots } & { 0 } & { - 1 } & { 2 } \end{array} \right] } \end{array}
$$

are nonsingular.

The next result shows that either all eigenvalues of an irreducible matrix A lie in the interior of the union of Geršgorin's disks or an eigenvalue of A is a common boundary point of all n disks.

Theorem 2 (O. Taussky). Let $\begin{array} { r } { A = [ a _ { j k } ] _ { j , k = 1 } ^ { n } } \end{array}$ be a complex irreducible matrix and let λ be an eigenvalue of A lying on the boundary of the union of the Geršgorin disks. Then λ is on the boundary of each of the n Geršgorin disks.

ProoF. Given the hypotheses of the theorem, let $| \lambda - a _ { i i } | = \rho _ { i }$ for some i, $1 \leq i \leq n .$ . If λ lies outside the remaining n - 1 Geršgorin disks, then $| \lambda - a _ { j j } | > \rho _ { j }$ for all $j \neq i .$ Therefore by Theorem 1 the matrix $\lambda I - A$ must be nonsingular. This contradicts the assumption that λ is an eigenvalue of A. Thus, since λ must lie on the boundary of the union of the disks, it must be a point of intersection of m circumferences where $2 \leq m \leq n$ . Thus there are m equalities in the system

$$
| \lambda - a _ { j j } | \geq \sum _ { k = 1 , k \neq j } ^ { n } | a _ { j k } | , \qquad 1 \leq j \leq n ,
$$

and $n - m$ strict inequalities. In view of Theorem 1, this conflicts again with the definition of λ unless $m = n ,$ Hence the assertion of the theorem.

In the study of iterative processes it is often useful to have criteria (sharper than that of Theorem 10.3.1) for deciding when the spectral radius of a matrix is less than 1 (see Exercise 9.8.5). Theorem 2 yields such a criterion as a corollary.

Corollary 1. Let $A = [ a _ { i j } ] _ { i , j = 1 } ^ { n }$ be irreducible and satisfy

$$
\sum _ { j = 1 } ^ { n } | a _ { i j } | \leq 1 \qquad f o r \quad i = 1 , 2 , \ldots , n ,\tag{5}
$$

with strict inequality for at least one i. Then $\mu _ { A } < 1$

ProoF. Note first that the hypothesis (5) implies at once that all Geršgorin disks are in the unit disk. So Theorem 10.6.1 immediately gives $\mu _ { A } \leq 1$

The fact that there is strict inequality in (5) for at least one i means that there is at least one Geršgorin disk that is entirely in the interior of the unit disk. Since points on the unit circle can only be on the circumference of the Geršgorin disks, it follows from Theorem 2 that an eigenvalue of A on the unit circle would have to be a common boundary point of all n disks, and this is impossible. Hence the result.

## 10.8 The Schur Theorem

We present next a rather different result that originates with I. Schur.' Let us recall the decomposition of a matrix $A \in \mathbb { R } ^ { n \times n }$ into the sum of a Hermitian matrix B and a skew-Hermitian matrix C. We write $\begin{array} { r } { B = \frac { 1 } { 2 } ( A + A ^ { * } ) } \end{array}$ 7 $\begin{array} { r } { C = \frac { 1 } { 2 } ( A - A ^ { * } ) } \end{array}$ , and observe that $A = B + C , B ^ { * } = B ,$ and $C ^ { * } = - C$ . Now if $A ^ { * } = A$ , then $C = O$ and all the eigenvalues of A are real. This suggests that a norm of C may give an upper bound for the magnitudes of the imaginary parts of the eigenvalues of A. Similarly, if $A ^ { * } = - A$ , then $B = o$ and all the eigenvalues of A have zero real parts, so a norm of B might be expected to give an upper bound for the magnitudes of the real parts of the eigenvalues of A. Schur's theorem contains results of this kind. In the following statement $\mathcal { R } e \ \lambda$ and $\mathcal { I } _ { M } ~ \lambda$ will denote the real and imaginary parts of the complex number λ.

Theorem 1. If $A \in \mathbb { C } ^ { n \times n } , \Vert \big | \Vert$ denotes the euclidean matrix norm, and $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ are the eigenvalues of A, then

$$
\sum _ { i = 1 } ^ { n } | \lambda _ { i } | ^ { 2 } \leq \| A \| ^ { 2 } ,
$$

$$
\sum _ { i = 1 } ^ { n } \mid { \mathcal { R } } _ { { \boldsymbol { \imath } } } \lambda _ { i } | ^ { 2 } \leq \| { \boldsymbol { B } } \| ^ { 2 } ,
$$

$$
\sum _ { i = 1 } ^ { n } \mid { \mathcal { I } } _ { { \mathcal { M } } } \lambda _ { i } \mid ^ { 2 } \leq \| C \| ^ { 2 } ,
$$

where $B = { \textstyle \frac { 1 } { 2 } } ( A + A ^ { * } )$ and $\begin{array} { r } { C = \frac { 1 } { 2 } ( A - A ^ { * } ) } \end{array}$ . Equality in any one of these relations implies equality in all three and occurs if and only if A is normal.

ProoF. Theorem 5.2.2 informs us that there is a unitary matrix U and an upper-triangular matrix $\Delta$ such that $A = U \Delta U ^ { * }$ , and the eigenvalues of A are the diagonal elements of $\Delta .$ Now the euclidean norm is invariant under unitary similarity transformations (Exercise 10.4.7) and so $\| A \| ^ { 2 } = \| \Delta \| ^ { 2 }$ If the elements of $\Delta$ are written $d _ { r s } \left( r , s = 1 , 2 , \ldots , n \right)$ , then

$$
\| A \| ^ { 2 } = \sum _ { i = 1 } ^ { n } | \lambda _ { i } | ^ { 2 } + \sum _ { r < s } | d _ { r s } | ^ { 2 } \geq \sum _ { i = 1 } ^ { n } | \lambda _ { i } | ^ { 2 } ,
$$

and the first inequality is proved.

We also have $B = { \textstyle { \frac { 1 } { 2 } } } U ( \Delta + \Delta ^ { * } ) U ^ { * }$ so that, as before,

$$
\begin{array} { l } { \displaystyle \| B \| ^ { 2 } = \sum _ { i = 1 } ^ { n } \bigg | \frac { \lambda _ { i } + \bar { \lambda } _ { i } } { 2 } \bigg | ^ { 2 } + \sum _ { r \neq s } \bigg | \frac { { d _ { r s } + \bar { d } _ { s r } } } { 2 } \bigg | ^ { 2 } } \\ { \displaystyle = \sum _ { i = 1 } ^ { n } | \mathscr { R } _ { \ell } \lambda _ { i } | ^ { 2 } + \sum _ { r \neq s } \frac { | { d _ { r s } } | ^ { 2 } } { 2 } \geq \sum _ { i = 1 } ^ { n } | \mathscr { R } _ { \ell } \lambda _ { i } | ^ { 2 } . } \end{array}
$$

A similar proof also yields the third inequality.

It is clear that equality obtains in each of the three relations if and only if $d _ { r s } = 0$ for all $r \neq s ,$ and $r , s = 1 , 2 , \ldots , n$ ; that is, if and only if A is unitarily similar to a diagonal matrix of its eigenvalues. The result now follows from Theorem 5.2.1.

Corollary 1 (A. Hirsch†). If we define

$$
\rho = \underset { r , s } { \operatorname* { m a x } } ~ | a _ { r s } | , \qquad \sigma = \underset { r , s } { \operatorname* { m a x } } ~ | b _ { r s } | , \qquad \tau = \underset { r , s } { \operatorname* { m a x } } ~ | c _ { r s } | ,
$$

and if λ is any eigenvalue of A, then

$$
| \lambda | \leq n \rho , | \mathcal { R } e \lambda | \leq n \sigma , | \mathcal { I } _ { \partial \mathcal { W } } \lambda | \leq n \tau .
$$

† Acta Math. 25 (1902), 367–370.

PROOF. Clearly, $\begin{array} { r } { \| A \| _ { \mathrm { E } } ^ { 2 } \le \sum _ { r , s } \rho ^ { 2 } = n ^ { 2 } \rho ^ { 2 } } \end{array}$ . The first inequality of Theorem 1 then gives $\begin{array} { r } { | \lambda | \leq ( \sum _ { i } | \lambda _ { i } | ^ { 2 } ) ^ { { \overline { { 1 / 2 } } } } \leq \| A \| \leq n \rho } \end{array}$ , which is the first result of the corollary. The two remaining results follow similarly.

Note that the particular case $\tau = 0$ provides another (high-powered) proof that the eigenvalues of a Hermitian matrix are real. Similarly the case $\sigma = 0$ yields the result that the eigenvalues of a skew-Hermitian matrix have their real parts zero.

Finally, we should note that $n \rho$ is the norm defined in Exercise 10.3.7a. The result $| \lambda | \leq n \rho$ is then a special case of Theorem 10.3.1.

Corollary 2 (I. Bendixson†). If $A \in \mathbb { R } ^ { n \times n }$ and $\begin{array} { r } { \tau = { \frac { 1 } { 2 } } \operatorname* { m a x } _ { r , s } | a _ { r s } - a _ { s r } | } \end{array}$ then for any eigenvalue λ of A,

$$
| { \mathcal I } _ { \mathcal M } \lambda | \leq \tau \sqrt { n ( n - 1 ) / 2 } .
$$

PRooF. When A is real, the third inequality of Theorem 1 implies that

$$
\sum _ { i = 1 } ^ { n } \mid \mathcal { I } _ { \mathcal { M } } \lambda _ { i } \mid ^ { 2 } \leq \sum _ { r , s = 1 , r \neq s } ^ { n } \left| \frac { a _ { r s } - a _ { s r } } { 2 } \right| ^ { 2 } \leq \tau ^ { 2 } n ( n - 1 ) .
$$

Since A is real, all of its complex eigenvalues arise in complex conjugate pairs, so that every nonzero term in the sum on the left appears at least twice. Hence 2| Im $\lambda _ { i } | ^ { 2 } \leq \tau ^ { 2 } n ( n - 1 )$ and the result follows.

Before leaving these results, we should remark that the bounds obtained in the corollaries are frequently less sharp than the corresponding bounds obtained from Geršgorin's theorem. This is well illustrated on applying Corollary 1 to Exercise 10.6.1.

Exercise 1. Prove that |det $A | \leq n ^ { n / 2 } \rho ^ { n }$ where $\rho = \operatorname* { m a x } _ { r , s } | a _ { r s } | .$

SoLUTION. First of all note the inequality of the arithmetic and geometric means: namely, for any nonnegative numbers $a _ { 1 } , a _ { 2 } , \ldots , a _ { n } .$

$$
( a _ { 1 } a _ { 2 } \cdots a _ { n } ) ^ { 1 / n } \leq { \frac { a _ { 1 } + a _ { 2 } + \cdots + a _ { n } } { n } } .
$$

If $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ are the eigenvalues of A, we have, by Theorem 1,

$$
\begin{array} { r l } & { | \det A | ^ { 2 } = | \lambda _ { 1 } | ^ { 2 } | \lambda _ { 2 } | ^ { 2 } \cdot \cdot \cdot | \lambda _ { n } | ^ { 2 } } \\ & { \qquad \leq \left( \frac { | \lambda _ { 1 } | ^ { 2 } + \cdot \cdot \cdot + | \lambda _ { n } | ^ { 2 } } { n } \right) ^ { n } } \\ & { \qquad \leq \left( \frac { 1 } { n } \| A \| _ { \mathbf { E } } ^ { 2 } \right) ^ { n } \leq \left( \frac { 1 } { n } n ^ { 2 } \rho ^ { 2 } \right) ^ { n } , } \end{array}
$$

and the result follows on taking square roots.

Exercise 2. If $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ are the eigenvalues of A and $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n }$ are those of $A ^ { * } A$ , show that

$$
\sum _ { i \mathop { = } 1 } ^ { n } | \lambda _ { i } | ^ { 2 } \leq \sum _ { i \mathop { = } 1 } ^ { n } \mu _ { i } ,
$$

with equality if and only if A is normal

Exercise 3. With the notation of Exercise $^ { 2 , }$ show that A is normal if and only if, for some ordering of the eigenvalues, $\mu _ { i } = | \lambda _ { i } | ^ { 2 } , i = 1 , 2 , \ldots , n .$ □

## 10.9 Miscellaneous Exercises

1. Prove that for any $A \in \mathbb { C } ^ { n \times n }$

$$
\| A \| _ { \mathrm { E } } ^ { 2 } = s _ { 1 } ^ { 2 } + s _ { 2 } ^ { 2 } + \cdot \cdot \cdot + s _ { n } ^ { 2 } ,
$$

where $s _ { 1 } , s _ { 2 } , \ldots , s _ { n }$ are the singular values of A.

Hint. Use Theorem 5.7.2 and Exercise 10.4.7.

2. Let $\ b { P } \in \mathbb { C } ^ { n \times n }$ be an orthogonal projector on $\mathcal { S } \subset \mathbb { C } ^ { n }$ . Prove that

$$
\| { \pmb x } - P { \pmb x } \| _ { \mathrm { E } } \le \| { \pmb x } - Q { \pmb x } \| _ { \mathrm { E } }
$$

for any projector $Q$ on $\mathcal { S }$ and any $\mathbf { x } \in \mathbb { C } ^ { n } .$ Interpret the result geometrically (in terms of a distance) in the case of $\mathbb { R } ^ { 3 }$ and dim $\mathcal { S } = 1$

3. Let $A = H _ { 1 } + i H _ { 2 } , H _ { 1 } ^ { * } = H _ { 1 } , H _ { 2 } ^ { * } = H _ { 2 }$

(a) show that $\| A \| _ { \mathrm { E } } ^ { 2 } = \| H _ { 1 } \| _ { \mathrm { E } } ^ { 2 } + \| H _ { 2 } \| _ { \mathrm { E } } ^ { 2 } \|$

(b) For any Hermitian matrix $H \in \mathbb { C } ^ { n \times n }$ , show that

$$
\| A - H _ { 1 } \| _ { \mathrm { E } } \leq \| A - H \| _ { \mathrm { E } }
$$

and

$$
\begin{array} { r } { \| A - i H _ { 2 } \| _ { \mathrm { E } } \leq \| A - i H \| _ { \mathrm { E } } . } \end{array}
$$

Interpret the result geometrically.

4. If $A = H U$ is the polar decomposition of $A ,$ prove that $\| A \| _ { \mathbf { E } } = \| H \| _ { \mathbf { E } }$ Indicate the corresponding property of complex numbers.

5. Define a vector norm $\parallel \parallel _ { \mathbf { v } }$ by Eq. (10.4.4) and prove that $\| \mathbf { x } \| _ { \mathbf { v } } \geq | \pmb { a } ^ { \mathrm { T } } \pmb { x } | .$ Also, if $\parallel \parallel _ { 1 }$ is the matrix norm induced by $\parallel \parallel _ { \mathbf { v } }$ , then $\left\| A \right\| _ { 1 } \leq \left\| A \right\|$ for all $A \in \mathbb { C } ^ { n \times n }$ , where $\parallel \parallel$ is the matrix norm in Eq. (10.4.4)

Hint. Start with $\parallel ( y \pmb { a } ^ { \operatorname { T } } ) ( \mathbf { x } \pmb { a } ^ { \operatorname { T } } ) \parallel ( \mathbf { y } \neq \pmb { 0 } )$ to obtain the first result.

6. $\operatorname { I f } \parallel \operatorname { \nabla } \parallel _ { \mathbf { v } }$ is the vector norm of Exercise 10.1.7, and $\parallel \parallel$ and $\bigstar \bigstar | | _ { \mathrm { ~ \scriptsize ~ s ~ } }$ denote the matrix norms induced by | l and  |le, respectively, prove that for $\parallel \parallel ,$ $\Vert \big | \big | \big | \big | \big | \big | \big | \big | \big | \big | \big | \big | \big |$ any $\ b { A } \in \mathbb { C } ^ { n \times n }$

$$
\| A \| = \| H ^ { 1 / 2 } A H ^ { 1 / 2 } \| _ { s } ,
$$

where $H ^ { 1 / 2 }$ denotes the positive definite square root of $H . \ \sqsubset$

If $\parallel \big | \big | _ { \pmb { v } }$ is a vector norm in $\mathbb { C } ^ { n } .$ , then the function $\parallel \parallel _ { \mathbf { d } }$ defined by

$$
\| \mathbf { y } \| _ { \mathbf { d } } \triangleq \operatorname* { s u p } _ { \mathbf { x } \neq 0 } \frac { | \mathbf { y } ^ { * } \mathbf { x } | } { \| \mathbf { x } \| _ { \mathbf { v } } } , \qquad \mathbf { y } \in \mathbb { C } ^ { n } ,\tag{1}
$$

is called the dual norm of $\bigstar \bigstar \bigstar \bigstar$

## 7. Prove that

(a) $\parallel \parallel _ { \mathbf { d } }$ is a vector norm;

(b) $| \mathbf { y } ^ { * } \pmb { x } | \leq \| \pmb { x } \| _ { \mathbf { v } } \| \mathbf { y } \| _ { \mathbf { d } }$ for all $x , \ y \in \mathbb { C } ^ { n }$ (the generalized Cauchy-Schwarz inequality);

(c) If $\begin{array} { r } { \| \pmb { x } \| _ { p } = ( \sum _ { i = 1 } ^ { n } | \pmb { x } _ { i } | ^ { p } ) ^ { 1 / p } } \end{array}$ is a Hölder vector norm, then the corresponding dual norm of x is

$$
\| { \bf x } \| _ { q } = \biggl ( \sum _ { i = 1 } ^ { n } | { \bf x } _ { i } | ^ { q } \biggr ) ^ { 1 / q } ,
$$

where $( 1 / q ) + ( 1 / p ) = 1$ . By use of part (b) for these norms, obtain the Hölder inequality.

8. If $A = a b ^ { * }$ and $\parallel \parallel$ is the matrix norm induced by a vector norm $\begin{array}{c} \Vert \big | \big | _ { \begin{array} { l } { \big | } \end{array} } \end{array}$ prove that $\lVert A \rVert = \lVert a \rVert _ { \mathbf { v } } \lVert b \rVert _ { \mathbf { d } }$ , where $\big \| \big \| \big \| _ { \mathrm { ~ \bf ~ d ~ } }$ is defined in Eq. (1).

9. If $\begin{array} { r } { \mathbf { x } \neq \pmb { \theta } , } \end{array}$ prove that there is a $\ b { y } \in \mathbb { C } ^ { n }$ such that $\mathbf { y } ^ { * } \mathbf { x } = \| \mathbf { x } \| _ { \mathbf { v } } \| \mathbf { y } \| _ { \mathbf { d } } = 1$

10. Prove that if $\| \big \updownarrow \big \| _ { \mathbf { d d } }$ is the dual norm of $\parallel \parallel _ { \mathbf { d } }$ , then $\| { \pmb x } \| _ { { \bf d d } } = \| { \pmb x } \| ,$ , for all $\pmb { x } \in \mathbb { C } ^ { n }$ . The norm $\parallel \parallel _ { \mathbf { d } }$ is defined in Eq. (1).

11. Let $\Vert \bigstar \bigstar \bigstar \bigstar | \bigstar$ be a norm in $\mathbb { C } ^ { n \times n }$ (not necessarily a matrix norm). Define

$$
N ( A ) = \operatorname* { s u p } _ { \substack { 0 \neq X \in \mathbb { C } ^ { n \times \ n } } } \frac { \| A X \| } { \| X \| }
$$

and prove that

(a) N is a matrix norm;

(b) $\operatorname { I f } \ \left\| \begin{array} { l l } \end{array} \right\|$ is a matrix norm, then $N ( A ) \leq \| A \|$ for all $A \in \mathbb { C } ^ { n \times n }$

(c) $N ( A ) = \left\| A \right\|$ for all $A \in \mathbb { C } ^ { n \times n }$ if and only $\mathrm { i f } \parallel \parallel$ is a matrix norm and $\| I \| = 1$

12. If $\parallel \parallel$ is a norm in $\mathbb { C } ^ { n \times n }$ (not necessarily a matrix norm), then there exists a number $c > 0$ such that the function

$$
M ( A ) = c \| A \| , \qquad A \in \mathbb { C } ^ { n \times n } ,
$$

is a matrix norm.

13. Use Exercise 1.8.5 to show that if, for any matrix norm $\| X \| \leq M$ and $\| Y \| \leq M$ (where X, $Y \in \mathbb { C } ^ { n \times n } )$ , then for $r = 1 , 2 , \ldots { } $

$$
\| X ^ { r } - Y ^ { r } \| \leq r M ^ { r - 1 } \| X - Y \| .
$$

14. (a) Let Î be a Jordan block of size p with eigenvalue λ. Let $\mu = \mathcal { R } e ( \lambda )$ and $f ( t ) = t ^ { p - 1 } e ^ { \mu t }$ . Using Theorem 9.4.4 show that there are positive constants $k _ { 1 } , k _ { 2 }$ , and $t _ { 0 }$ such that

$$
k _ { 1 } f ( t ) \leq \| e ^ { \hat { J } t } \| _ { s } \leq k _ { 2 } f ( t ) , \qquad t \geq t _ { 0 } .
$$

(b) Let $A \in \mathbb { C } ^ { n \times n } , \mu = \operatorname* { m a x } _ { \lambda \in \sigma ( A ) } { \mathcal { R } } e ( \lambda )$ and let $p$ be the largest index of any eigenvalue for which $\mu = \mathcal { R } e ( \lambda )$ . Show that there are positive constants $K _ { 1 } , K _ { 2 } ,$ and $t _ { 0 }$ such that

$$
K _ { 1 } f ( t ) \leq \| e ^ { A t } \| _ { s } \leq K _ { 2 } f ( t ) , \qquad t \geq t _ { 0 } .
$$

(c) Use the result of part (b) to show that

(i) $\| e ^ { A t } \| _ { s } \to 0 \mathrm { a s } t \to \infty$ if and only if $\mu < 0$

(ii) If $\mu \leq 0$ and p = 1, then $\| e ^ { \boldsymbol { A } t } \| _ { s } \le K _ { 2 }$ for all $t \geq t _ { 0 }$

(iii) $\textstyle \operatorname { I f } \mu < 0$ there are positive constants K and α such that $\| e ^ { \ b { A } t } \| _ { s } \le K e ^ { - \alpha t }$ for all $t \geq 0 .$

## 15. Let $\ b { F } \in \mathbb { C } ^ { n \times n }$ and

$$
A = { \binom { I } { F ^ { * } } } \quad F \Biggr ] .
$$

Prove that A is positive definite if and only if $\| F \| _ { s } < 1$

Hint. Use the factorization

$$
{ \left[ \begin{array} { l l } { I } & { F } \\ { F ^ { * } } & { I } \end{array} \right] } = { \left[ \begin{array} { l l } { I } & { \ O } \\ { F ^ { * } } & { I } \end{array} \right] } { \left[ \begin{array} { l l } { I } & { \ O } \\ { O } & { I - F ^ { * } F } \end{array} \right] } { \left[ \begin{array} { l l } { I } & { \ F } \\ { O } & { I } \end{array} \right] }
$$

together with Exercise 10.4.5.

16. Let $A \in \mathbb { C } ^ { n \times n } , B \in \mathbb { C } ^ { r \times r }$ and $U \in \mathbb { C } ^ { n \times r }$ with orthonormal columns, i.e. $U ^ { * U }$ $\mathbf { \delta } = I _ { r ^ { \star } } \mathbf { I f } A = U B U ^ { * }$ show that $\left. \left. A \right. \right. _ { \mathrm { s } } = \left. \left. B \right. \right. _ { \mathrm { s } }$

## Perturbation Theory

The greater part of this chapter is devoted to investigations of the behavior of matrix eigenvalues under perturbations of the elements of the matrix. Before starting on this subject it is instructive (and particularly important for the numerical analyst) to examine the effects of perturbations of A and $\pmb { b }$ on a solution x of the linear equation $A { \boldsymbol { \mathbf { x } } } = \mathbf { \boldsymbol { b } }$

## 11.1 Perturbations in the Solution of Linear Equations

Given $A \in \mathbb { C } ^ { n \times n }$ , consider the equation $A { \pmb x } = b \left( { \pmb x } , { \pmb b } \in \mathbb { C } ^ { n } \right)$ and assume that det $A \neq 0 ,$ , so that x is the unique solution of the equation.

In general terms, a problem is said to be stable, or well conditioned, if “small" causes (perturbations in A or b) give rise to “small” effects (perturbations in x). The degree of smallness of the quantities in question is usually measured in relation to their magnitudes in the unperturbed state. Thus if $x + y$ is the solution of the problem after the perturbation, we measure the magnitude of the perturbation in the solution vector by $\| \mathbf { y } \| _ { \mathbf { v } } / \| \mathbf { x } \| ,$ for some vector norm $\Vert \big | \big | \big | _ { \mathbf { v } }$ . We call this quotient the relative perturbation of x.

Before investigating the problem with a general coefficient matrix A, it is very useful to examine the prototype problem of variations in the coefficients of the equation ${ \pmb x } = { \pmb b } .$ Thus, we are led to investigate solutions of $( I + M ) \xi = b$ , where M is “small" compared to I. The departure of ${ \pmb \xi }$ from x will obviously depend on the nature of $( I + M ) ^ { - 1 }$ , if this inverse exists. In this connection we have one of the most useful results of linear analysis:

Theorem 1. $H \| \| \|$ denotes any matrix norm for which $\| I \| = 1$ and $i f \parallel M \parallel <$ 1, then $( I + M ) ^ { - 1 }$ exists,

$$
( I + M ) ^ { - 1 } = I - M + M ^ { 2 } - \cdot \cdot \cdot
$$

and

$$
\lVert ( I + M ) ^ { - 1 } \rVert \leq \frac { 1 } { 1 - \lVert M \rVert } .
$$

Note that in view of Theorem 10.3.1, the hypotheses of the theorem can be replaced by a condition on the spectral radius: $\mu _ { M } < 1$

ProOF. Theorem 10.3.1 implies that for any eigenvalue $\lambda _ { 0 }$ of $M , \vert \lambda _ { 0 } \vert \leq$ $\| M \| < 1$ . Moreover, the function f defined by $f ( \lambda ) = ( 1 + \lambda ) ^ { - 1 }$ has a power series expansion about $\lambda = 0$ with radius of convergence equal to 1. Hence (see Theorem 9.8.3), $f ( M ) = ( I + M ) ^ { - 1 }$ exists and

$$
( I + M ) ^ { - 1 } = I - M + M ^ { 2 } - \cdots .
$$

If we write $S _ { v } = I - M + M ^ { 2 } - \cdot \cdot \cdot \pm M ^ { p - 1 }$ for the pth partial sum and note that $\| M ^ { r } \| \leq \| M \| ^ { r }$ , we obtain

$$
\| S _ { p } \| \leq \sum _ { k = 1 } ^ { p - 1 } \| M ^ { k } \| \leq \sum _ { k = 1 } ^ { p - 1 } \| M \| ^ { k } = \frac { 1 - \| M \| ^ { p } } { 1 - \| M \| } \leq \frac { 1 } { 1 - \| M \| } .
$$

As this bound is independent of $p ,$ the result follows on taking the limit as $p  \infty$

Let us return now to our original problem. We have

$$
A \mathbf { x } = \mathbf { b } ,
$$

with det $A \neq 0 ,$ and we suppose that b is changed to $\mathbf { \delta } \mathbf { b } + \mathbf { \delta } \mathbf { k } ,$ that A is changed to $A + F _ { \mathrm { { i } } }$ , and that $x + y$ satisfies

$$
( A + F ) ( { \pmb x } + { \pmb y } ) = { \pmb b } + { \pmb k } .\tag{1}
$$

We will compute an upper bound for the relative perturbation $\| \mathbf { y } \| _ { \mathbf { v } } / \| \mathbf { x } \| _ { \mathbf { v } }$ Subtracting the first equation from the second, we have

$$
( A + F ) { \pmb y } + F { \pmb x } = { \pmb k } ,
$$

or

$$
\begin{array} { r } { A ( I + A ^ { - 1 } F ) y = k - F { \pmb { x } } . } \end{array}
$$

We assume now that $\delta = \lVert A ^ { - 1 } \rVert \ \lVert F \rVert < 1$ , and that $\| I \| = 1$ . Then, since $\| A ^ { - 1 } F \| \le \| A ^ { - 1 } \| \| F \| < 1$ , Theorem 1 implies that $( \dot { I } + A ^ { - 1 } F ) ^ { - 1 }$ exists, and that $\lVert ( I + A ^ { - 1 } F ) ^ { - 1 } \rVert < ( 1 - \delta ) ^ { - 1 }$ . Thus

$$
\pmb { y } = ( \pmb { I } + \pmb { A } ^ { - 1 } \pmb { F } ) ^ { - 1 } \pmb { A } ^ { - 1 } \pmb { k } - ( \pmb { I } + \pmb { A } ^ { - 1 } \pmb { F } ) ^ { - 1 } \pmb { A } ^ { - 1 } \pmb { F } \pmb { x } ,
$$

and, ${ \dot { \mathbf { i f } } } \parallel \mathbf { \nabla } \parallel _ { \mathbf { v } }$ is any vector norm compatible with $\parallel \parallel$

$$
\left\| \mathbf { y } \right\| _ { \mathbf { v } } \leq { \frac { \left\| A ^ { - 1 } \right\| } { 1 - \delta } } \left\| \pmb { k } \right\| _ { \mathbf { v } } + { \frac { \delta } { 1 - \delta } } \left\| \pmb { x } \right\| _ { \mathbf { v } } .
$$

To obtain a convenient expression for our measure, $\| { \bf y } \| _ { \bf v } / \| { \bf x } \| ,$ , of the magnitude of the perturbation, we use the fact that $A \mathbf { x } = \mathbf { b }$ implies $\| \pmb { b _ { \mathrm { \pmb { v } } } } \| \leq$ $\| A \| \ \| \mathbf { x } \| _ { \cdot }$ , hence $1 / \| \mathbf { x } \| _ { \mathbf { v } } \leq \| A \| / \| \pmb { \mathit { b } } \| _ { \mathbf { v } } , \pmb { \mathit { b } } \neq \pmb { \mathit { 0 } } .$ Thus

$$
\frac { \left\| \pmb { y } \right\| _ { \mathbf { v } } } { \left\| \pmb { x } \right\| _ { \mathbf { v } } } \leq \frac { \left\| \pmb { A } \right\| \left\| \pmb { A } ^ { - 1 } \right\| } { 1 - \delta } \frac { \left\| \pmb { k } \right\| _ { \mathbf { v } } } { \left\| \pmb { b } \right\| _ { \mathbf { v } } } + \frac { \delta } { 1 - \delta } .
$$

The first term on the right contains the relative perturbation of $\mathbf { \delta } _ { \mathbf { \delta } }$ and the last term is independent of the right-hand side of the original equation. We now define $\kappa ( A ) = \| A \| \ \| A ^ { - 1 } \|$ to be the condition number of A (with respect to ∥ ∥) and note that

$$
\delta = \| A ^ { - 1 } \| \ \| F \| = { \frac { \kappa ( A ) \left\| F \right\| } { \left\| A \right\| } } .
$$

Thus, we obtain finally

$$
\frac { \Vert \pmb { y } \Vert _ { \mathbf { v } } } { \Vert \pmb { x } \Vert _ { \mathbf { v } } } \leq \frac { \kappa ( A ) } { 1 - ( \kappa ( A ) \Vert \boldsymbol { F } \Vert / \Vert A \Vert ) } \left( \frac { \Vert \pmb { k } \Vert _ { \mathbf { v } } } { \Vert \pmb { b } \Vert _ { \mathbf { v } } } + \frac { \Vert \boldsymbol { F } \Vert } { \Vert A \Vert } \right) .\tag{2}
$$

This gives us an upper bound for the relative perturbation of x in terms of the relative perturbations of b and A and the condition number $\kappa ( A )$ . In particular, the decisive part played by the condition number should be noted. This is the case whether perturbations occur in b alone, in A alone, or in b and A simultaneously. The condition number will also play an important part in the investigation of perturbations of eigenvalues (Section 2).

Exercise 1. Prove that if $\| A ^ { - 1 } \| \ \| F \| < 1$ , then $\| F \| < \| A \|$

Exercise 2. If A = diag[1, 2, 3, .. . , 10] and $\| \pmb { b } \| _ { \infty } = 1$ , and it is known only that the elements of F and k are bounded in absolute value by $\varepsilon ,$ where $\varepsilon < 0 . 1$ , then

$$
\frac { \| \pmb { y } \| _ { \infty } } { \| \pmb { x } \| _ { \infty } } \le \frac { 2 0 \varepsilon } { 1 - 1 0 \varepsilon } .
$$

If, in addition,

$$
\pmb { b } = \left[ \begin{array} { c } { 0 . 1 } \\ { 0 . 2 } \\ { \vdots } \\ { 1 . 0 } \end{array} \right] , \qquad \pmb { k } = \left[ \begin{array} { c } { - \varepsilon } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right] , \qquad \boldsymbol { F } = \left[ \begin{array} { l l l l } { \varepsilon } & { \varepsilon } & { \cdots } & { \varepsilon } \\ { 0 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { 0 } \end{array} \right] ,
$$

show that

$$
{ \frac { \| { \mathbf { y } } \| _ { \infty } } { \| { \mathbf { x } } \| _ { \infty } } } = { \frac { 2 0 \varepsilon } { 1 + \varepsilon } } .
$$

Exercise 3. Prove that for any $A \in \mathbb { C } ^ { n \times n }$ and any matrix norm, the condition number $\kappa ( A )$ satisfies the inequality $\kappa ( A ) \geq 1$

Exercise 4. If $\kappa ( A )$ is the spectral condition number of A, that is, the condition number obtained using the spectral norm, and $s _ { 1 }$ and $s _ { n }$ are the largest and smallest singular values of $A ,$ respectively, prove that $\kappa ( A ) = s _ { 1 } / s _ { n }$

Exercise 5. If $\kappa ( A )$ is the spectral condition number of a normal nonsingular matrix $A \in \mathbb { C } ^ { n \times n }$ , and $\lambda _ { 1 }$ and $\lambda _ { n }$ are (in absolute value) the largest and smallest eigenvalues of A, respectively, prove that $\kappa ( A ) = \vert \lambda _ { 1 } \vert / \vert \lambda _ { n } \vert$

Exercise 6. Prove that the spectral condition number $\kappa ( A )$ is equal to 1 if and only if $\alpha A$ is a unitary matrix for some $\alpha \neq 0$

Exercise 7. If the linear equation $A \mathbf { x } = \mathbf { b } $ det $A \neq 0 ,$ , is replaced by the equivalent equation $B x = A ^ { * } b$ , where $B = A ^ { * } A$ , prove that this may be done at the expense of the condition number; that is, that $\kappa ( B ) \geq \kappa ( A )$

Exercise 8. Use Theorem 1 to prove that $M ^ { p }  0$ as $p  \infty$ . More precisely, prove that $M ^ { p }  0$ as $p  \infty$ if and only if the spectral radius of M is less than 1

Exercise 9. If $A \in \mathbb { C } ^ { n \times n }$ satisfies the condition $\| A \| ^ { p } < k$ for some matrix norm  |, all nonnegative integers $p ,$ and some constant k independent of $p ,$ show that A also satisfies the resolvent condition: for all complex z with $| z | > 1$ , the matrix $z I - A$ is nonsingular and

$$
\lVert ( z I - A ) ^ { - 1 } \rVert \leq { \frac { k } { | z | - 1 } } .
$$

Exercise 10. Let $A \in \mathbb { C } ^ { n \times n }$ be an invertible normal matrix with eigenvalues $\lambda _ { \operatorname* { m a x } }$ and $\lambda _ { \operatorname* { m i n } }$ of largest and smallest absolute values, respectively. Let $A v = \lambda _ { \operatorname* { m a x } } v , A u = \lambda _ { \operatorname* { m i n } } u$ with $\| { \pmb v } \| = \| { \pmb u } \| = 1$ in the euclidean norm. Write $\pmb { b } = \pmb { v } , \pmb { k } = \pmb { \varepsilon } \pmb { u } _ { 1 }$ with $\varepsilon > 0$ . Show that if $A \mathbf { x } = \mathbf { b }$ and $A ( { \mathfrak { x } } + { \mathfrak { y } } ) = { \pmb { b } } + { \pmb { k } }$ [cf. Eq. (1)], then

$$
{ \frac { \| { \mathbf { y } } \| } { \| { \mathbf { x } } \| } } = \varepsilon \kappa ( { \boldsymbol { A } } ) .
$$

(This is a “worst case" in which the general error bound of (2) is actually attained. Note the result of Ex. 10.4.8)

## 11.2 Perturbations of the Eigenvalues of a Simple Matrix

We now take up the question of the dependence of the eigenvalues of a simple matrix A on the elements of A. The results of this section are essentially due to F. L. Bauer and A. S. Householder.†

Let A be a simple matrix with eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ . Then if $D =$ diag $[ \lambda _ { 1 } , . . . , \lambda _ { n } ]$ , there is a nonsingular matrix P such that $A = P D P ^ { - 1 }$ In Theorem 10.5.1 we have been able to characterize a class of matrix norms with favorable properties when applied to diagonal matrices, and so we are led to the idea of using $\| D \|$ to estimate $\| A \|$ for such a norm. Thus, if is a matrix norm induced by an absolute vector norm, the equation $A =$ $P D P ^ { - 1 }$ and Theorem 10.5.1 imply that

$$
\| A \| \leq \kappa ( P ) \operatorname* { m a x } _ { 1 \leq j \leq n } | \lambda _ { j } | ,
$$

where $\kappa ( P ) = \| P \| \ \| P ^ { - 1 } \|$ is the condition number of P with respect to $\parallel \parallel .$ as defined in Section 1. However, as Exercise 6.5.4 shows, the matrix P is not uniquely defined by the equation $A = P D P ^ { - 1 }$ . In particular, $A = Q D Q ^ { - 1 }$ for any matrix $Q = P D _ { 1 }$ , where $D _ { 1 }$ is a nonsingular diagonal matrix. We therefore obtain the best possible bound,

$$
\| A \| \leq \nu ( A ) \operatorname* { m a x } _ { 1 \leq j \leq n } | \lambda _ { j } | ,
$$

if we define $\begin{array} { r } { \nu ( A ) = \operatorname* { i n f } _ { P } \kappa ( P ) } \end{array}$ the infimum being taken with respect to all matrices P for which $P ^ { - 1 } A P$ is diagonal. This result may be viewed as a lower bound for the spectral radius of $A$ ; coupled with Theorem 10.3.1, it yields the first half of the following result.

Theorem 1. If A is a simple matrix,   is a matrix norm induced by an absolute vector norm, and $\begin{array} { r } { \nu ( A ) = \operatorname* { i n f } _ { P } \kappa ( P ) } \end{array}$ , where $P ^ { - 1 } A P$ is diagonal, then

$$
{ \frac { \| A \| } { \nu ( A ) } } \leq \operatorname* { m a x } _ { 1 \leq j \leq n } | \lambda _ { j } | \leq \| A \| ,
$$

and

$$
l ( A ) \leq \operatorname* { m i n } _ { 1 \leq j \leq n } | \lambda _ { j } | \leq \nu ( A ) l ( A ) ,\tag{1}
$$

where l(A) is deined in $E q .$ (10.5.1).

PRoOF. The first inequality in (1) is just the result of Exercise 10.5.2. For the second inequality, the equation $A = P D P ^ { - 1 }$ and Corollaries 10.5.1 and 10.5.2 imply that

$$
l ( A ) \geq l ( P ) l ( P ^ { - 1 } ) \operatorname* { m i n } _ { 1 \leq j \leq n } | \lambda _ { j } | .
$$

Theorem 10.5.2 then gives

$$
l ( A ) \geq ( \kappa ( P ) ) ^ { - 1 } \operatorname* { m i n } _ { 1 \leq j \leq n } | \lambda _ { j } | ,
$$

and the second inequality in (1) follows.

For a general simple matrix A this theorem is of doubtful computational value because the quantity $\nu ( A )$ is so difficult to estimate. However, we should observe that $P P ^ { - 1 } = I$ implies that $\kappa ( P ) = \| P \| \ \| P ^ { - 1 } \| \geq 1$ (see also Exercise 11.1.3), and hence that $\nu ( A ) \geq 1$

If A is a normal matrix then we know that P may be chosen to be a unitary matrix. If, in addition, we use the euclidean vector norm, and hence the spectral matrix norm ∥ ∥, then $\| P \| = \| P ^ { - 1 } \| = 1$ . Thus, for a normal matrix and spectral norm we have $\nu ( A ) = 1$ and the theorem reduces to the known cases:

$$
\| A \| = \operatorname* { m a x } _ { 1 \leq j \leq n } | \lambda _ { j } | , \qquad l ( A ) = \operatorname* { m i n } _ { 1 \leq j \leq n } | \lambda _ { j } | .
$$

Our next theorem demonstrates the significance of $\nu ( A )$ as a condition number for A reflecting the stability of the eigenvalues under perturbation of the matrix elements.

Theorem 2. Let $A , B \in \mathbb { C } ^ { n \times n } ,$ , with A simple. If A has eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ and $\mu$ is an eigenvalue of $| A + B ,$ and if for a matrix norm induced by an absolute vector norm $\parallel \parallel ,$ , we have

$$
r = \| B \| \nu ( A ) ,
$$

then $\mu$ lies in at least one of the disks

$$
\{ z : | z - \lambda _ { j } | \leq r \} , \qquad j = 1 , 2 , \ldots , n ,
$$

of the complex z-plane.

PROOF. Since $\mu$ is an eigenvalue of $A + B ,$ there is $\mathbf { a } \ \mathbf { y } \neq \mathbf { 0 }$ for which

$$
( A + B ) y = \mu { \bf y } .
$$

If $A = P D P ^ { - 1 }$ , where $D = \mathrm { d i a g } [ \lambda _ { 1 } , . . . , \lambda _ { n } ] ,$ then

$$
( D + P ^ { - 1 } B P ) { \bf x } = \mu { \bf x } ,
$$

where $\pmb { x } = P ^ { - 1 } \pmb { y } \neq \pmb { 0 } .$ Thus,

$$
( \mu I - D ) { \pmb x } = P ^ { - 1 } B P { \pmb x }\tag{2}
$$

and hence

$$
l ( \mu I - D ) \leq \frac { \| ( \mu I - D ) \pmb x \| _ { \mathbf { v } } } { \| \pmb x \| _ { \mathbf { v } } } = \frac { \| P ^ { - 1 } B P \pmb x \| _ { \mathbf { v } } } { \| \pmb x \| _ { \mathbf { v } } } \leq \| P ^ { - 1 } B P \| \leq \kappa ( P ) \ \| B \| .
$$

Therefore we have

$$
\operatorname* { m i n } _ { 1 \leq j \leq n } | \mu - \lambda _ { j } | \leq \kappa ( P ) \| B \| .
$$

Since this is true for every P diagonalizing A, we have

$$
\operatorname* { m i n } _ { 1 \leq j \leq n } | \mu - \lambda _ { j } | \leq \nu ( A ) \| B \| = r .
$$

Hence, μ lies in at least one of the disks $| z - \lambda _ { j } | \leq r , j = 1 , 2 , \ldots , n .$ ■

Exercise 1. Show that the eigenvalues in Exercise 10.6.1 lie in the disks with radius 2 and centers at $3 \doteq { \sqrt { 1 0 } } , 5 i$ , and −2.

Hint. Use Exercise 10.4.11 to estimate ∥B∥. □

If the perturbation matrix B of Theorem 2 is also known to be simple, then the radius of the disks obtained in that theorem can be reformulated, as indicated in the next theorem.

Theorem 3. If, in addition to the hypotheses of Theorem 2, the matrix B is simple with eigenvalues $\mu _ { 1 } , \ldots , \mu _ { n }$ , then μ lies in at least one of the disks

$$
\{ z \colon | z - \lambda _ { j } | \leq \nu ( A , B ) \operatorname* { m a x } _ { j } | \mu _ { j } | \} , \qquad j = 1 , 2 , \ldots , n ,
$$

where

$$
\displaystyle \nu ( A , B ) = \operatorname* { i n f } _ { P , Q } \kappa ( P ^ { - 1 } Q )
$$

and P and Q diagonalize A and B, respectively.

ProoF. We may now write Eq. (2) in the form

$$
( \mu I - D ) { \pmb x } = ( P ^ { - 1 } Q ) D _ { 1 } ( P ^ { - 1 } Q ) ^ { - 1 } { \pmb x } ,
$$

where $D _ { 1 } = \mathrm { d i a g } [ \mu _ { 1 } , . . . , \mu _ { n } ]$ Hence

$$
l ( \mu I - D ) \leq \kappa ( P ^ { - 1 } Q ) \| D _ { 1 } \| ,
$$

and the result follows from Theorem 10.5.1.

We can easily obtain a stronger form of this theorem. Observe that P will diagonalize A if and only if P will diagonalize αI + A for any complex number $\alpha ,$ and similarly for $Q , B ,$ and $- \alpha I + B .$ Since

$$
( \alpha I + A ) + ( - \alpha I + B ) = A + B ,
$$

we can now apply Theorem 3 to αI $+ \ A$ and $- \alpha I + B .$

Corollary 1. Under the hypotheses of Theorem 3, the eigenvalue $\mu$ lies in at least one of the disks

$$
\{ z \colon | z - ( \alpha + \lambda _ { j } ) | \leq \nu ( A , B ) \operatorname * { m a x } _ { 1 \leq j \leq n } | \mu _ { j } - \alpha | \} , \ j = 1 , 2 , \ldots , n ,
$$

for any fixed complex number α.

The advantage of this result lies in the fact that α may now be chosen to minimize max ${ \bf \nabla } _ { j } | \mu _ { j } - \alpha |$ and hence minimize the area of the disks containing the eigenvalues.

The case in which A and B are normal is important enough to warrant a separate statement

Corollary 2. If, in the hypotheses of Theorem 3, the matrices A and B are normal, then the eigenvalues of $A + B$ are contained in the disks

$$
\{ z : | z - ( \alpha + \lambda _ { j } ) | \leq \operatorname* { m a x } _ { j } \lvert \mu _ { j } - \alpha \rvert \} , \qquad j = 1 , 2 , \ldots , n ,
$$

for any xed complex number α.

PRooF. Observe that P and Q may be supposed to be unitary. This implies that $P ^ { - 1 } Q$ is unitary and hence, if we use the spectral matrix norm, $\nu ( A , B ) =$ $\begin{array} { r } { \operatorname* { i n f } _ { P , Q } \kappa ( P ^ { - 1 } Q ) = 1 } \end{array}$ . The result now follows from the first corollary.

Exercise 2. If A is a normal matrix with eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ , and B has all its elements equal to $\mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } }$ prove that the eigenvalues of $A + B$ lie in the disks

$$
\left\{ z colon \left| z - \left( { \frac { n \varepsilon } { 2 } } + \lambda _ { j } \right) \right| \leq { \frac { n } { 2 } } \left| \varepsilon \right| \right\} , \qquad j = 1 , 2 , \ldots , n .
$$

Exercise 3. If A is a normal matrix and $B = \operatorname { d i a g } [ b _ { 1 } , \dotsc , b _ { n } ]$ is real, prove that the eigenvalues of $A + B$ lie in the disks

$$
\{ z : | z - ( \alpha + \lambda _ { j } ) | \leq \beta \} , \qquad j = 1 , 2 , \ldots , n ,
$$

where $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ are the eigenvalues of A and

$$
2 \alpha = \operatorname* { m a x } _ { 1 \leq j \leq n } b _ { j } + \operatorname* { m i n } _ { 1 \leq j \leq n } b _ { j } \qquad { \mathrm { a n d } } \qquad 2 \beta = \operatorname* { m a x } _ { 1 \leq j \leq n } b _ { j } - \operatorname* { m i n } _ { 1 \leq j \leq n } b _ { j } .
$$

Exercise 4. Let $A \in \mathbb { R } ^ { n \times n }$ , and let $\mu _ { 1 } , \ldots , \mu _ { n }$ be the eigenvalues of ${ \textstyle \frac { 1 } { 2 } } ( A + A ^ { \boldsymbol { \mathsf { T } } } )$ \_ If k is the spectral radius of ${ \scriptstyle { \frac { 1 } { 2 } } } ( A - A ^ { \mathsf { T } } )$ and

$$
\operatorname* { m i n } _ { j \neq k } | \mu _ { j } - \mu _ { k } | \geq 2 k ,
$$

prove that the eigenvalues of A are real.

Exercise 5. Suppose that A, $B \in \mathbb { R } ^ { n \times n } , ~ A ^ { \mathrm { T } } = A$ and $| b _ { j k } | \leq b$ for j, $k =$ 1, 2, . . . , n. If $\mu _ { 1 } , \ldots , \mu _ { n }$ are the eigenvalues of A and

$$
\operatorname* { m i n } _ { j \neq k } | \mu _ { j } - \mu _ { k } | > 2 n b ,
$$

prove that the eigenvalues of $A + B$ are real.

Exercise 6. Let A and $A + E$ be $n \times n$ matrices with eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ and $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n }$ , respectively. Show that the eigenvalues can be ordered in such a way that

$$
| \lambda _ { j } - \mu _ { j } | \leq \| E \| _ { s } ,
$$

for $j = 1 , 2 , \dots , n . \quad \bigsqcup$

## 11.3 Analytic Perturbations

We now take quite a different approach to the perturbation problem. Suppose that $A \in \mathbb { C } ^ { n \times n }$ is the unperturbed matrix and has eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { n }$ . We then suppose that $A ( \zeta )$ is an $n \times n$ matrix whose elements are analytic functions of $\zeta$ in a neighborhood of $\zeta _ { 0 }$ and that $A ( \zeta _ { 0 } ) = A$ . For convenience, and without loss of generality, we may suppose that $\zeta _ { 0 } = 0 ,$ so $A ( 0 ) = A$ . We write $\lambda _ { 1 } ( \zeta ) , \ldots , \lambda _ { n } ( \zeta )$ for the eigenvalues of $A ( \zeta )$ and then (Section 10.6), since the eigenvalues of $A ( \zeta )$ depend continuously on the elements of $A ( \zeta )$ , we may suppose that $\lambda _ { j } ( \zeta ) \to \lambda _ { j } \mathrm { a s } \zeta \to 0 \mathrm { f o r } j = 1 , 2 , \ldots , n .$

The following exercise illustrates the fact that, though the eigenvalues depend continuously on the matrix elements, they may nevertheless vary quite rapidly in pathological circumstances.

Exercise 1. Consider the $1 0 \times 1 0$ matrix $A ( \zeta )$ defined as a function of the real variable $\zeta$ by

$$
A ( \zeta ) = \left[ \begin{array} { l l l l l } { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \ddots } & { \ddots } & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \\ { \zeta } & { 0 } & { \cdots } & { 0 } & { 0 } \end{array} \right] .
$$

Prove that the eigenvalues at $\zeta = 0$ and those at $\zeta = 1 0 ^ { - 1 0 }$ differ in absolute value by 0.1.

Note that the difference between $A ( 0 )$ and $A ( 1 0 ^ { - 1 0 } )$ is so small that they may not be distinguishable on a computer with too short a word length.

What can we say about the nature of the functions $\lambda _ { j } ( \zeta )$ for sufficiently small $| \zeta | 2$ We shall see that in certain important special cases, the functions $\lambda _ { j } ( \zeta )$ are also analytic in a neighborhood of $\zeta = 0$ . That this is not generally the case is illustrated by the next example.

Example 2. The eigenvalues of the matrix

$$
A ( \zeta ) = { \left[ \begin{array} { l l } { 0 } & { \zeta } \\ { \zeta ^ { 2 } } & { 0 } \end{array} \right] }
$$

are the zeros of the polynomial

$$
\operatorname* { d e t } ( \lambda I - A ( \zeta ) ) = \lambda ^ { 2 } - \zeta ^ { 3 } ,
$$

that is, $\lambda _ { 1 } ( \zeta ) = \zeta ^ { 3 / 2 }$ (defined by a particular branch of the function $\zeta ^ { 1 / 2 } )$ and $\lambda _ { 2 } ( \zeta ) = - \lambda _ { 1 } ( \zeta )$ . Thus, we see that the eigenvalues are certainly not analytic in a neighbourhood of $\zeta = 0 . \ \bigcirc$

It should be noted that det $( \lambda I - A ( \zeta ) )$ is a polynomial in λ whose coefficients are analytic functions of ζ. It then follows from the theory of algebraic functions that

(a) If $\lambda _ { j }$ is an unrepeated eigenvalue of A, then $\lambda _ { j } ( \zeta )$ is analytic in a neighbourhood of $\zeta = 0$

(b) If $\lambda _ { j }$ has algebraic multiplicity m and $\lambda _ { k } ( \zeta ) \to \lambda _ { j }$ for $k = \mathfrak { x } _ { 1 } , \ldots , \mathfrak { x } _ { m } .$ then $\lambda _ { k } ( \zeta )$ is an analytic function of $\dot { \zeta } ^ { 1 / l }$ in a neighborhood of $\zeta = 0 _ { : }$ where $l \leq m$ and $\zeta ^ { 1 / l }$ is one of the l branches of the function $\zeta ^ { 1 / l }$ Thus $\lambda _ { k } ( \zeta )$ has a power-series expansion in $\zeta ^ { 1 / l }$

We shall prove result (a) together with a result concerning the associated eigenvectors. Note that, in result (b), we may have $l = 1$ and $m > 1$ , in which case $\lambda _ { k } ( \zeta )$ could be analytic. As might be expected it is case (b) with $m > 1$ that gives rise to difficulties in the analysis. The expansions in fractional powers of $\zeta$ described in (b) are known as Puiseux series, and their validity will be assumed in the discussions of Section 11.7.

It is when we try to follow the behavior of eigenvectors that the situation becomes more complicated. The matrix

$$
A ( \zeta ) = { \left[ \begin{array} { l l } { 0 } & { \zeta } \\ { 0 } & { 0 } \end{array} \right] }
$$

serves to show that even though the eigenvalues may be analytic, the eigenvectors need not be continuous at $\zeta = 0$

Nevertheless, we shall approach the perturbation problem by analysis of the spaces generated by eigenvectors, insofar as these are determined by the component matrices of $A ( \zeta )$ (see Section 9.5). The reason for this is that, first, the resolvent $R _ { z } ( \zeta ) = ( z I - A ( \zeta ) ) ^ { - 1 }$ is expressed directly in terms of $A ( \zeta )$ and, second, by means of Eq. (9.9.4) we can then examine the component matrices of $A ( \zeta )$ . In particular, we shall be able to infer properties of vectors in the range of a component matrix.

## 11.4 Perturbation of the Component Matrices

Suppose that an unperturbed eigenvalue λ “splits" into distinct eigenvalues $\lambda _ { 1 } ( \zeta ) , \ldots , \lambda _ { p } ( \zeta )$ under the perturbation determined by $A ( \zeta )$ . We can prove that the sum of the first component matrices for each of these eigenvalues is analytic near $\zeta = 0 .$ This theorem is the peg on which we hang all our subsequent analysis of the perturbation problem.

Theorem 1. Let $A ( \zeta )$ be analytic in a neighborhood of $\zeta = 0$ and $A ( 0 ) = A$ Suppose that $\lambda _ { 1 } ( \zeta ) , \ldots , \lambda _ { p } ( \zeta )$ are the distinct eigenvalues of $A ( \zeta )$ for which $\lambda _ { k } ( \zeta ) \to \lambda a s \zeta \to 0 , k = 1 , 2 , \ldots , p .$ and let $Z _ { k 0 } ( \zeta )$ be the idempotent component matrix of $A ( \zeta )$ associated with $\lambda _ { k } ( \zeta )$ . If Z is the idempotent component matrix of A associated with λ and we define

$$
Y ( \zeta ) = \sum _ { k = 1 } ^ { p } Z _ { k 0 } ( \zeta ) ,
$$

then there is a neighborhood $o f \zeta = 0$ in which the following developments hold:

$$
Y ( \zeta ) = Z + \zeta C _ { 1 } + \zeta ^ { 2 } C _ { 2 } + \cdots ,
$$

$$
A ( \zeta ) Y ( \zeta ) = A Z + \zeta B _ { 1 } + \zeta ^ { 2 } B _ { 2 } + \cdots ,
$$

for matrices $C _ { r } , B _ { r }$ independent of ζ, $r = 1 , 2 , \ldots$

PRoOF. Consider a fixed $\zeta \neq 0$ for which $| \zeta |$ is small enough to admit the construction of a simple closed contour L that encircles $\lambda , \lambda _ { 1 } ( \zeta ) , \ldots , \lambda _ { p } ( \zeta )$ and no other eigenvalues of A or of $A ( \zeta )$ . Then writing $R _ { z } = ( z I - \dot { A } ) ^ { - 1 }$ and $R _ { z } ( \zeta ) = ( z I - A ( \zeta ) ) ^ { - 1 }$ , we have

$$
Z = \frac { 1 } { 2 \pi i } \int _ { L } R _ { z } d z , \qquad Y ( \zeta ) = \frac { 1 } { 2 \pi i } \int _ { L } R _ { z } ( \zeta ) d z .\tag{1}
$$

We note that the elements of $R _ { z } ( \zeta )$ are rational expressions in functions of $\zeta$ that are analytic in a neighborhood of $\zeta = 0$ for z on the contour L. Thus, there exist matrices $R _ { z } ^ { ( r ) } , r = 1 , 2 , \ldots$ , independent of $\zeta$ such that

$$
R _ { z } ( \zeta ) = R _ { z } + \zeta R _ { z } ^ { ( 1 ) } + \zeta ^ { 2 } R _ { z } ^ { ( 2 ) } + \cdots .\tag{2}
$$

Using (1) we have only to integrate this series term by term around the contour to obtain the first result of the theorem. This is permissible provided only that each coefficient $R _ { z } ^ { ( r ) } ~ ( r = 0 , 1 , 2 , . . . )$ is integrable on L. Using Exercise 9.9.3 we see that, for a fixed $z ,$

$$
R _ { z } ^ { ( 1 ) } ( \zeta ) = R _ { z } ( \zeta ) A ^ { ( 1 ) } ( \zeta ) R _ { z } ( \zeta ) ,\tag{3}
$$

and hence that, for each r, the matrix $R _ { z } ^ { ( r ) }$ is a linear combination of matrices $R _ { z } ( A ^ { ( p ) } R _ { z } ) ^ { s }$ for certain integers $p ,$ s with $p \leq r$ Now, $A ^ { ( p ) } ( 0 )$ is independent of z and $R _ { z }$ is certainly continuous in $z$ on $L$ Hence $R _ { z } ^ { ( r ) }$ is continuous on L. Integrating the series for $R _ { z } ( \zeta )$ around $L ,$ we now obtain

$$
{ \cal { Y } } ( \zeta ) = Z + \zeta C _ { 1 } + \zeta ^ { 2 } C _ { 2 } + \cdots ,
$$

where

$$
C _ { r } = \frac { 1 } { 2 \pi i } \int _ { L } R _ { z } ^ { ( r ) } d z , \qquad r = 1 , 2 , \ldots { . }
$$

Now both $Y ( \zeta )$ and $A ( \zeta )$ are analytic on a neighborhood of $\zeta = 0$ It follows that their product $A ( \zeta ) Y ( \zeta )$ is also analytic there and has a Taylor expansion given by the product of the expansions for $A ( \zeta )$ and $Y ( \zeta ) _ { : }$ , so the theorem is proved.

A similar theorem can be proved showing that the continuity of $A ( \zeta )$ at $\zeta = 0$ implies that of $Y ( \zeta )$ $\zeta = 0$ B

Now we show that the individual first component matrices do not necessarily have the property of being analytic near $\zeta = 0$

Exercise 1. Find the matrices $Z , Z _ { 1 0 } ( \zeta ) , Z _ { 2 0 } ( \zeta )$ , and $Y ( \zeta )$ for the matrix

$$
A ( \zeta ) = \left[ { \begin{array} { c c } { 0 } & { \zeta } \\ { \zeta ^ { 2 } } & { 0 } \end{array} } \right] .
$$

SOLUTION. $\mathbf { A } \mathbf { t } \zeta = 0 $ , the matrix A is the zero-matrix and it is easily seen that $Z = I$ The eigenvalues of $A ( \zeta )$ are $\mu _ { 1 } ( \zeta ) = \zeta ^ { 3 / 2 }$ and $\mu _ { 2 } ( \zeta ) = - \mu _ { 1 } ( \zeta )$ . We then have

$$
R _ { z } ( \zeta ) = \left[ \begin{array} { c c } { z } & { - \zeta } \\ { - \zeta ^ { 2 } } & { z } \end{array} \right] ^ { - 1 } = \frac { 1 } { z ^ { 2 } - \zeta ^ { 3 } } \left[ \begin{array} { c c } { z } & { \zeta } \\ { \zeta ^ { 2 } } & { z } \end{array} \right] .
$$

Partial fraction expansions now give

$$
R _ { z } ( \zeta ) = \frac { 1 } { 2 } \left[ \frac { 1 } { z - \zeta ^ { 3 / 2 } } + \frac { 1 } { z + \zeta ^ { 3 / 2 } } \frac { \zeta ^ { - 1 / 2 } } { z - \zeta ^ { 3 / 2 } } - \frac { \zeta ^ { - 1 / 2 } } { z + \zeta ^ { 3 / 2 } } \right] .
$$

Using Eq. (9.9.4) we obtain

$$
\begin{array} { r } { Z _ { 1 0 } ( \zeta ) = \frac { 1 } { 2 } \left[ \begin{array} { c c } { 1 } & { \zeta ^ { - 1 / 2 } } \\ { \zeta ^ { 1 / 2 } } & { 1 } \end{array} \right] \qquad \mathrm { a n d } \qquad Z _ { 2 0 } ( \zeta ) = \frac { 1 } { 2 } \left[ \begin{array} { c c } { 1 } & { - \zeta ^ { - 1 / 2 } } \\ { - \zeta ^ { 1 / 2 } } & { 1 } \end{array} \right] . } \end{array}
$$

Hence $Y ( \zeta ) = Z _ { 1 0 } ( \zeta ) + Z _ { 2 0 } ( \zeta ) = I .$ This example emphasizes the fact that although $Y ( \zeta )$ may be analytic in ζ, the component matrices (of which it is the sum) need not be analytic. Indeed, in this example the component matrices have a singularity at $\zeta = 0 .$ It should also be noted that although the eigenvalues are not analytic in a neighborhood containing $\zeta = 0 ,$ yet they are “better behaved" than the component matrices.

Exercise 2. If the matrix

$$
A ( \zeta ) = { \left[ \begin{array} { l l l } { 0 } & { \zeta } & { 0 } \\ { 0 } & { 0 } & { \zeta } \\ { \zeta } & { 0 } & { 1 } \end{array} \right] }
$$

has eigenvalues $\lambda _ { 1 } ( \zeta ) , \lambda _ { 2 } ( \zeta )$ , and $\lambda _ { 3 } ( \zeta )$ and $\lambda _ { j } ( \zeta ) \to 0 \mathrm { ~ a s ~ } \zeta \to 0 , j = 1 .$ ,2, show that we may write

$$
\lambda _ { j } ( \zeta ) = ( - 1 ) ^ { j + 1 } i \zeta ^ { 3 / 2 } - \textstyle { \frac { 1 } { 2 } } \zeta ^ { 3 } + \cdots , \qquad j = 1 , 2 .
$$

If $\lambda = 0$ is the unperturbed eigenvalue under investigation, find $Z , Z _ { \mathbf { 1 0 } } ( \zeta )$ $Z _ { 2 0 } ( \zeta )$ , and $Y ( \zeta )$ , and verify that $Y ( \zeta )$ is analytic in a neighbourhood of $\zeta = 0 .$

Exercise 3. Consider eigenvectors $e _ { 1 } , e _ { 2 } , e _ { 3 }$ (unit coordinate vectors) of $A ( 0 )$ in Exercise 2. Consider the possibility of extending these, as eigenvectors of $A ( \zeta ) .$ , into a neighbourhood of $\zeta = 0 .$ Show that $\pmb { e _ { 3 } }$ can be extended analytically, $e _ { \mathrm { I } }$ has two continuous extensions, and $\pmb { e } _ { 2 }$ has no such extension.

## 11.5 Perturbation of an Unrepeated Eigenvalue

We are now in a position to prove a perturbation theorem of the greatest practical importance. The notation is that developed in the two preceding sections.

Theorem 1. If λ is an eigenvalue of A of multiplicity 1, then, for sufficiently small |ζ|, there is an eigenvalue $\lambda ( \zeta )$ of $A ( \zeta )$ such that

$$
\lambda ( \zeta ) = \lambda + \zeta \lambda ^ { ( 1 ) } + \zeta ^ { 2 } \lambda ^ { ( 2 ) } + \cdot \cdot \cdot .\tag{1}
$$

Also, there are right and left eigenvectors $\pmb { x } ( \zeta )$ and $y ( \zeta )$ , respectively, associated with $\lambda ( \zeta )$ for which

$$
\mathbf { y } ^ { \mathbf { T } } ( \zeta ) \mathbf { x } ( \zeta ) = 1
$$

and

$$
\pmb { x } ( \zeta ) = \pmb { x } + \zeta \pmb { x } ^ { ( 1 ) } + \zeta ^ { 2 } \pmb { x } ^ { ( 2 ) } + \cdots ,\tag{2}
$$

$$
\begin{array} { r } { \pmb { y } ( \zeta ) = \pmb { y } + \zeta \pmb { y } ^ { ( 1 ) } + \zeta ^ { 2 } \pmb { y } ^ { ( 2 ) } + \cdots . } \end{array}\tag{3}
$$

ProOF. We suppose throughout that ζ| is so small that λ(ζ) $| \zeta |$ $\lambda ( \zeta )$ has multiplicity 1. It then follows that $Y ( \zeta ) = Z _ { 1 0 } ( \zeta )$ , a component matrix. Furthermore (see Theorem 4.10.3) we may write

$$
Z = { \bf x } { \bf y } ^ { \mathrm { T } } , \qquad Y ( \zeta ) = { \bf x } ( \zeta ) { \bf y } ^ { \mathrm { T } } ( \zeta ) ,\tag{4}
$$

where

$$
\mathbf { y } ^ { \mathsf { T } } \mathbf { x } = \mathbf { y } ^ { \mathsf { T } } ( \boldsymbol { \zeta } ) \mathbf { x } ( \boldsymbol { \zeta } ) = \mathbf { l } .
$$

In this case we obviously have

$$
A ( \zeta ) Y ( \zeta ) = \lambda ( \zeta ) Y ( \zeta ) ,
$$

so premultiplying by $\mathbf { y } ^ { \mathsf { T } }$ and postmultiplying by x we obtain

$$
\lambda ( \zeta ) = { \frac { y ^ { \operatorname { T } } A ( \zeta ) Y ( \zeta ) { \mathbf { x } } } { y ^ { \operatorname { T } } Y ( \zeta ) { \mathbf { x } } } } = { \frac { \lambda + \zeta b _ { 1 } + \zeta ^ { 2 } b _ { 2 } + \cdot \cdot \cdot } { 1 + \zeta c _ { 1 } + \zeta ^ { 2 } c _ { 2 } + \cdot \cdot \cdot \cdot } }
$$

after making use of Theorem 11.4.1. The coefficients on the right are given by

$$
b _ { r } = y ^ { \operatorname { T } } B _ { r } \mathbf { x } , \qquad c _ { r } = y ^ { \operatorname { T } } C _ { r } \mathbf { x } , \qquad r = 1 , 2 , \ldots .
$$

It follows that $\lambda ( \zeta )$ is analytic in a neighbourhood of $\zeta = 0 ,$ , which is the first part of the theorem.

It is clear that, in the statement of the theorem, $\pmb { x } ( \zeta )$ is not defined to within a nonzero multiplicative constant (which may vary with ζ). We define $\pmb { x } ( \zeta )$ more precisely by noting first of all that there is no ambiguity in the definition of Y(ζ). We then choose the eigenvectors x, y with $\mathbf { y } ^ { \mathbf { T } } \mathbf { x } = 1$ , and hence $\mathbf { x } \mathbf { y } ^ { \mathbf { T } } = Z$

Then $Y ( \zeta ) = { \mathbf { x } } ( \zeta ) { \mathbf { y } } ^ { { \mathsf { T } } } ( \zeta )$ implies

$$
\begin{array} { r } { \mathbf { y } ^ { \mathsf { T } } Y ( \zeta ) \mathbf { x } = ( \mathbf { y } ^ { \mathsf { T } } \mathbf { x } ( \zeta ) ) ( \mathbf { y } ^ { \mathsf { T } } ( \zeta ) \mathbf { x } ) , } \end{array}
$$

and since $Y ( \zeta ) \to x y ^ { \mathsf { T } }$ as $\zeta  0 ,$ it follows that $( \mathbf { y } ^ { \mathrm { { T } } } \mathbf { x } ( \zeta ) ) ( \mathbf { y } ^ { \mathrm { { T } } } ( \zeta ) \mathbf { x } ) \to 1$ as $\zeta \to 0$ Thus we may suppose that $\mathbf { y } ^ { \mathsf { T } } \mathbf { x } ( \zeta )$ and $\mathbf { y } ^ { \mathsf { T } } ( \zeta )$ are nonzero for small enough $| \zeta |$ . Now we can define $\pmb { x } ( \zeta )$ by normalizing in such a way that

$$
y ^ { \mathsf { T } } x ( \zeta ) = 1 .\tag{5}
$$

Since $Y ( \zeta ) \mathbf { x } = \mathbf { x } ( \zeta ) ( \mathbf { y } ^ { \mathrm { { T } } } ( \zeta ) \mathbf { x } )$ , we have $\mathbf { y } ^ { \mathsf { T } } Y ( \zeta ) \mathbf { x } = \mathbf { y } ^ { \mathsf { T } } ( \zeta ) \mathbf { x } .$ Hence $Y ( \zeta ) =$ $x ( \zeta ) { \mathfrak { p } } ^ { \mathsf { T } } ( \zeta )$ implies

$$
\pmb { x } ( \zeta ) = \frac { 1 } { \mathbf { y } ^ { \mathsf { T } } Y ( \zeta ) \pmb { x } } Y ( \zeta ) \pmb { x } .
$$

Since $Y ( \zeta )$ is analytic in a neighborhood of $\zeta = 0$ and $y ^ { \mathsf { T } } Y ( 0 ) x = 1$ , it follows that $\pmb { x } ( \zeta )$ is analytic in a neighborhood of $\zeta = 0$

Finally, Eq. (5) also implies $\mathbf { x } ^ { \mathrm { T } } ( \zeta ) \mathbf { y } = 1$ , so the relation $\mathbf { \mathfrak { y } } ( \zeta ) \mathbf { \mathfrak { x } } ^ { \mathrm { T } } ( \zeta ) = Y ^ { \mathrm { T } } ( \zeta )$ implies $\mathbf { \boldsymbol { y } } ( \zeta ) = \mathbf { \boldsymbol { Y } } ^ { \mathrm { { r } } } ( \zeta ) \mathbf { \boldsymbol { y } }$ , which is also analytic in a neighborhood of $\zeta = 0$

We have now proved the existence of power series expansions in ζ for an unrepeated eigenvalue and its eigenvectors. The next step in the analysis is the discussion of methods for computing the coefficients of these expansions.

## 11.6 Evaluation of the Perturbation Coefficients

We shall first discuss a particular problem that will arise repeatedly later on. If λ is an eigenvalue of the matrix $A \in \mathbb { C } ^ { n \times n }$ and $\qquad b \neq 0 ,$ we want to solve the equation

$$
( \lambda I - A ) \mathbf { x } = \pmb { b } .\tag{1}
$$

Given that a solution exists (i.e., $\pmb { b } \in \operatorname { I m } ( \lambda I - A ) )$ , we aim to express a solution x of (1) in terms of the spectral properties of A. $\mathbf { I f } \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ are the distinct eigenvalues of A and $\lambda = \lambda _ { 1 }$ we first define the matrix

$$
E = \sum _ { k = 2 } ^ { s } \sum _ { j = 0 } ^ { m _ { k } - 1 } \frac { j ! } { ( \lambda - \lambda _ { k } ) ^ { j + 1 } } Z _ { k j } ,\tag{2}
$$

just as in Eq. (9.6.2) but replacing $\lambda _ { 1 }$ and $E _ { 1 }$ by λ and E. Multiply Eq. (1) on the left by $E$ and use Theorem 9.6.2 to obtain

$$
( I - Z ) { \pmb x } = E { \pmb b } .\tag{3}
$$

With the convention of Sections 4 and 5 we write Z for $Z _ { 1 0 } . )$ Since $Z E = O$ it is easily seen that the vector ${ \pmb x } = E { \pmb b }$ satisfies Eq. (3), and we would like to assert that it is also a solution of Eq. (1). However, we need an additional hypothesis to guarantee this.

Proposition 1. If λ is an eigenvalue of A of index 1, then Eqs. (1) and (3) have the same solution set $\mathcal { S }$ Furthermore, ${ \pmb x } = E { \pmb b }$ is a common solution (when ${ \mathcal { S } } \neq { \mathcal { O } } )$

ProoF. In view of the argument above, we have only to show that the solution sets coincide. But $I - Z = E ( \lambda I - A )$ and so, using Exercise 3.10.8, we need to check that rank $( I - Z ) = \mathrm { r a n k } ( \lambda I - A )$ . To do this, observe that ${ I - Z }$ and $\lambda I - A$ have the same kernel, namely, the eigenspace of A associated with λ.

Suppose now that the hypotheses of Theorem 11.5.1 are fulfilled. Then λ has multiplicity 1 and for small enough $| \zeta | ,$ we use the results of that theorem to write

$$
\begin{array} { c } { { ( A + \zeta A ^ { ( 1 ) } + \zeta ^ { 2 } A ^ { ( 2 ) } + \cdots ) ( x + \zeta x ^ { ( 1 ) } + \zeta ^ { 2 } x ^ { ( 2 ) } + \cdots ) } } \\ { { { } } } \\ { { = ( \lambda + \zeta \lambda ^ { ( 1 ) } + \cdots ) ( x + \zeta x ^ { ( 1 ) } + \cdots ) . } } \end{array}\tag{4}
$$

We can equate the coefficients of $\zeta ^ { n }$ obtained by multiplying these series for $\pmb { n = 0 } , 1 , 2 , \ldots$ The coefficient of $\zeta ^ { 0 }$ gives the equation for the unperturbed eigenvalue: $A \pmb { x } = \lambda \pmb { x }$ . The coefficient of $\zeta$ gives

$$
( \lambda I - A ) { \bf x } ^ { ( 1 ) } = ( A ^ { ( 1 ) } - \lambda ^ { ( 1 ) } I ) { \bf x } .\tag{5}
$$

Since y (of Eq. 11.5.4) is a left eigenvector of $\lambda ,$ we deduce that ${ \bf y } ^ { \tt T } ( A ^ { ( 1 ) } -$ $\lambda ^ { ( 1 ) } I ) \mathbf { x } = 0 .$ Since $\mathbf { y } ^ { \mathsf { T } } \mathbf { x } = 1$ , this condition yields

$$
\lambda ^ { ( 1 ) } = { \bf y } ^ { \mathsf { T } } A ^ { ( 1 ) } x .\tag{6}
$$

We also know that, with our definition of $\pmb { x } ( \zeta )$ , the relation (11.5.5) gives us

$$
y ^ { \operatorname { T } } ( x + \zeta x ^ { ( 1 ) } + \zeta ^ { 2 } x ^ { ( 2 ) } + \cdot \cdot \cdot ) = 1 ,
$$

and this implies that

$$
y ^ { \mathrm { T } } x ^ { ( r ) } = 0 , \qquad r = 1 , 2 , \ldots { } .\tag{7}
$$

To obtain an expression for $\mathbf { x } ^ { ( 1 ) }$ from Eq. (5), we use Proposition 1. Thus, we know that $\begin{array} { r } { \hat { \mathbf { x } } ^ { ( 1 ) } = E ( A ^ { ( 1 ) } - \lambda ^ { ( 1 ) } I ) \mathbf { x } } \end{array}$ is a solution. Since $\boldsymbol { Z } = \mathbf { x } \mathbf { y } ^ { \boldsymbol { \mathsf { T } } }$ and $E Z = O ;$ , it follows that $E { \pmb x } = E Z { \pmb x } = { \pmb 0 }$ , so the expression for $\mathbf { x } ^ { ( 1 ) }$ simplifies to give $\mathbf { x } ^ { ( 1 ) } = E A ^ { ( 1 ) } \mathbf { x }$

We should confirm that this choice of solution is consistent with (7), that is, that $\begin{array} { r } { \mathbf { y ^ { \mathsf { T } } } \mathbf { x ^ { ( 1 ) } } = 0 } \end{array}$ Since $\mathbf { y } ^ { \mathsf { T } } Z = \mathbf { y } ^ { \mathsf { T } }$ we have

$$
\mathbf { y } ^ { \mathrm { T } } \mathbf { x } ^ { ( 1 ) } = \mathbf { y } ^ { \mathrm { T } } Z E A ^ { ( 1 ) } \mathbf { x } .
$$

But then $\begin{array} { r } { Z E = E Z = 0 . } \end{array}$ sO $\mathbf { y } ^ { \mathsf { T } } \mathbf { x } ^ { ( 1 ) } = 0$ , as required.

Thus, we complete the solution for the first-order perturbation coefficients as follows:

$$
\lambda ^ { ( 1 ) } = y ^ { \mathrm { T } } A ^ { ( 1 ) } x , \quad x ^ { ( 1 ) } = E A ^ { ( 1 ) } x\tag{8}
$$

The argument can easily be extended to admit the recursive calculation of $\lambda ^ { ( r ) }$ and $\boldsymbol { x } ^ { ( r ) }$ for any r. The coefficients of $\zeta ^ { r }$ in $\mathbf { E q . } \left( 4 \right)$ yield

$$
A x ^ { ( r ) } + A ^ { ( 1 ) } x ^ { ( r - 1 ) } + \cdot \cdot \cdot + A ^ { ( r ) } x = \lambda x ^ { ( r ) } + \lambda ^ { ( 1 ) } x ^ { ( r - 1 ) } + \cdot \cdot \cdot + \lambda ^ { ( r ) } x ,
$$

or

$$
( \lambda I - A ) { \pmb x } ^ { ( r ) } = \big ( A ^ { ( 1 ) } - \lambda ^ { ( 1 ) } I \big ) { \pmb x } ^ { ( r - 1 ) } + \dots + \big ( A ^ { ( r ) } - \lambda ^ { ( r ) } I \big ) { \pmb x } .
$$

If we now assume that $\lambda ^ { ( 1 ) } , \ldots , \lambda ^ { ( r - 1 ) }$ and $\mathbf { x } ^ { ( 1 ) } , \ldots , \mathbf { x } ^ { ( r - 1 ) }$ are known, then multiplying on the left by $\mathbf { y } ^ { \mathsf { T } }$ gives

$$
\lambda ^ { ( r ) } = y ^ { \operatorname { T } } A ^ { ( r ) } x + y ^ { \operatorname { T } } A ^ { ( r - 1 ) } x ^ { ( 1 ) } + \cdots + y ^ { \operatorname { T } } A ^ { ( 1 ) } x ^ { ( r - 1 ) } ,\tag{9}
$$

for $r = 1 , 2 , \ldots$ , and ${ \pmb x } ^ { ( 0 ) } = { \pmb x } .$ Proposition 1 then yields the result

$$
\pmb { x } ^ { ( r ) } = E [ ( A ^ { ( 1 ) } - \lambda ^ { ( 1 ) } I ) \pmb { x } ^ { ( r - 1 ) } + \cdots + ( A ^ { ( r - 1 ) } - \lambda ^ { ( r - 1 ) } I ) \pmb { x } ^ { ( 1 ) } + A ^ { ( r ) } \pmb { x } ] .\tag{10}
$$

In many applications the perturbations of A are linear in $\zeta .$ Thus we have $A ( \zeta ) = A + \zeta B$ for a matrix B independent of $\zeta .$ In this case we have $A ^ { ( 1 ) } =$ B and $A ^ { ( 2 ) } = A ^ { ( 3 ) } = \cdots = O$ . Equations (9) and (10) now reduce to

$$
\boldsymbol { \lambda } ^ { ( r ) } = \boldsymbol { y } ^ { \top } \boldsymbol { B } \boldsymbol { x } ^ { ( r - 1 ) } , \qquad \boldsymbol { x } ^ { ( r ) } = \boldsymbol { E } \left( \boldsymbol { B } \boldsymbol { x } ^ { ( r - 1 ) } - \sum _ { j = 1 } ^ { r - 1 } \boldsymbol { \lambda } ^ { ( j ) } \boldsymbol { x } ^ { ( r - j ) } \right) ,
$$

for $r = 1 , 2 , \ldots$ . Recall that in these formulas the superscripts do not denote derivatives but are defined by the expansions (11.5.1) and (11.5.2).

Exercise 1. Show that Eq. (9) in the case $r = 2$ may be written

$$
\lambda ^ { ( 2 ) } = \mathrm { t r } ( A ^ { ( 2 ) } Z _ { 1 0 } ) + \mathrm { t r } ( A ^ { ( 1 ) } E A ^ { ( 1 ) } Z _ { 1 0 } ) . ~ \bigtriangledown
$$

## 11.7 Perturbation of a Multiple Eigenvalue

We can now consider the problem of analytic perturbations of an unrepeated eigenvalue to be solved. In particular, the result (a) of Section 11.3 has been established. If λ is an iegenvalue of A of multiplicity $m > 1$ , then we must return to the Puiseux series representation of a perturbed eigenvalue $\lambda ( \zeta )$ that tends to $\lambda$ as $\zeta \to 0$ (result (b) of Section 11.3). In Section 11.4 we gained some further insight into the behavior of the component matrices of the perturbed eigenvalues and saw that although their sum $Y ( \zeta )$ is analytic for small enough $| \zeta |$ (Theorem 11.4.1), the separate component matrices may have singularities at $\zeta = 0$ (Exercise 11.4.1)

Suppose now that we impose the further condition that $A ( \zeta )$ be Hermitian and analytic on a neighborhood $\mathcal { N }$ of $\zeta = \zeta _ { 0 }$ in the complex plane. Let $a _ { j k } ( \zeta )$ be an element of $A ( \zeta )$ with $j \neq k$ , and let $z = x + i y$ with x and y real Then define $a _ { j k } ( x + i y ) = u ( x , y ) + i v ( x , y )$ , where u and v are real-valued functions.

With these definitions, the Cauchy-Riemann equations imply that

$$
{ \frac { { \hat { c } } u } { { \hat { \partial } } x } } = { \frac { { \hat { \partial } } v } { \partial y } } \qquad { \mathrm { a n d } } \qquad { \frac { { \hat { c } } u } { \partial y } } = - { \frac { { \hat { c } } v } { \partial x } } .
$$

But $a _ { k j } ( \zeta ) = a _ { j k } ( \zeta ) = u ( x , y ) - i v ( x , y )$ , which is also analytic on $\mathcal { N }$ Hence

$$
\frac { \hat { c } \pmb { u } } { \hat { c } \pmb { x } } = - \frac { \hat { c } \pmb { v } } { \hat { \partial } \pmb { y } } \quad \mathrm { a n d } \quad \frac { \hat { c } \pmb { u } } { \hat { \partial } \pmb { y } } = \frac { \hat { c } \pmb { v } } { \hat { \partial } \pmb { x } } .
$$

These equations together imply that $a _ { j k } ( \zeta )$ is a constant on ${ \mathcal { N } } ,$ and the parameter dependence has been lost. This means that analytic dependence in the sense of complex variables is too strong a hypothesis, and for the analysis of matrices that are both analytic and Hermitian we must confine attention to a real parameter $\zeta$ and assume that for each $j$ and k the real and imaginary parts of $a _ { j k }$ are real analytic functions of the real variable $\zeta .$

For this reason the final theorem of this chapter (concerning normal matrices) must be stated in terms of a real parameter $\zeta .$ When applied to Hermitian matrices this means that the perturbed eigenvalues remain real and the component matrices (as studied in Theorem 11.4.1) will be Hermitian. It can also be shown that in this case the perturbed eigenvalues are analytic in $\zeta ,$ whatever the multiplicity of the unperturbed eigenvalue may be. The perturbed component matrices are also analytic and hence the eigenvectors of $A ( \zeta )$ can be supposed to be analytic and orthonormal throughout a neighborhood of $\zeta = 0$ These important results were first proved by F. Rellich in the early 1930s. Rellich's first proof depends primarily on the fact that the perturbed eigenvalues are real. We shall prove a result (Theorem 2) that contains these results by means of a more recent technique due to Kato. (See the references in Appendix 3.)

With this preamble, we now return to a perturbation problem, making no assumption with regard to symmetry of the matrix $A ( \zeta )$ . Until we make some hypothesis concerning the symmetry of $A ( \zeta )$ , we retain the assumption of dependence on a complex parameter $\zeta .$ The formulation of corresponding results for the case of a real variable $\zeta$ is left as an exercise. We first prove that if $\lambda$ is an eigenvalue of A of index 1 and $\lambda _ { j } ( \zeta )$ is an eigenvalue of $A ( \zeta )$ for which $\lambda ( \zeta )  \lambda$ as $\zeta \to 0 ,$ then, as $\zeta \to 0$

$$
\lambda _ { j } ( \zeta ) = \lambda + \alpha _ { j } \zeta + O ( | \zeta | ^ { 1 + ( 1 / l ) } ) .
$$

Thus, in the Puiseux expansion for $\lambda _ { j } ( \zeta )$ described in result (b) of Section 11.3, the coefficients of $\zeta ^ { j / l }$ are zero for $j = 1 , 2 , \dots , l - 1$

As in Section 11.4, the eigenvalue λ of $A = A ( 0 )$ is supposed to “split” into eigenvalues $\lambda _ { 1 } ( \zeta ) , \ldots , \lambda _ { p } ( \zeta )$ for $| \zeta |$ sufficiently small. Also $A ( \zeta ) =$ $\sum _ { n = 0 } ^ { \infty } \zeta ^ { n } A ^ { ( n ) }$ , the matrix $Z$ is the component matrix of $\lambda ,$ and $Y ( \zeta )$ is the sum of component matrices $Z _ { k 0 } ( \zeta )$ of $A ( \zeta )$ for $1 \leq k \leq p .$ Thus, $Y ( \zeta ) \to Z$ as $| \zeta |  0$

Lemma 1. With the conventions and hypotheses of the previous paragraphs, the function

$$
B ( \zeta ) \overset { \triangle } { = } \zeta ^ { - 1 } ( \lambda I - A ( \zeta ) ) Y ( \zeta )\tag{1}
$$

has a Taylor expansion about $\zeta = 0$ of the form

$$
B ( \zeta ) = - Z A ^ { ( 1 ) } Z + \sum _ { n = 1 } ^ { \infty } \zeta ^ { n } B ^ { ( n ) } .
$$

PRoOF. Using Eq. (11.4.1) and Exercise 9.9.6, we may write

$$
Y ( \zeta ) = \frac { 1 } { 2 \pi i } \int _ { L } R _ { z } ( \zeta ) d z , \qquad A ( \zeta ) Y ( \zeta ) = \frac { 1 } { 2 \pi i } \int _ { L } z R _ { z } ( \zeta ) d z ,
$$

where, as in the proof of Theorem 11.4.1, the contour L is simple and closed and contains $\lambda , \lambda _ { 1 } ( \zeta ) , \ldots , \lambda _ { p } ( \zeta )$ and no other eigenvalues of $A$ or $A ( \zeta )$ Here, $\zeta$ is fixed and $| \zeta |$ is assumed to be small enough to complete this (and subsequent) constructions. Using Eq. (11.4.2) it follows that

$$
\begin{array} { c } { { ( \lambda I - A ( \zeta ) ) Y ( \zeta ) = \displaystyle - \frac { 1 } { 2 \pi i } \int _ { L } ( z - \lambda ) R _ { z } ( \zeta ) d z } } \\ { { = \displaystyle - \frac { 1 } { 2 \pi i } \int _ { L } ( z - \lambda ) \sum _ { r = 0 } ^ { \infty } \zeta ^ { r } R _ { z } ^ { ( r ) } d z . } } \end{array}
$$

Now, $Y ( 0 ) = Z$ and, since λ has index 1, $( \lambda I - A ) Z = O$ . Hence the coefficient of $\zeta ^ { 0 }$ on both sides of the last equation must vanish and we find that

$$
B ( \zeta ) = \zeta ^ { - 1 } ( \lambda I - A ( \zeta ) ) Y ( \zeta ) = \sum _ { r = 0 } ^ { \infty } \zeta ^ { r } B ^ { ( r ) } ,
$$

where, for $r = 0 , 1 , 2 , \ldots$

$$
B ^ { ( r ) } = - \ \frac { 1 } { 2 \pi i } \int _ { L } { ( z - \lambda ) R _ { z } ^ { ( r + 1 ) } d z }
$$

and is independent of $\zeta .$ This confirms the existence of the Taylor expansion for $B ( \zeta )$

To examine the leading coefficient we first take advantage of Eq. (11.4.3) and Exercise 9.5.2 to write

$$
\begin{array} { l } { { \displaystyle R _ { z } ^ { ( 1 ) } = ( z I - A ) ^ { - 1 } A ^ { ( 1 ) } ( z I - A ) ^ { - 1 } } } \\ { { \displaystyle ~ = \biggl ( \frac { Z } { z - \lambda } + E ( z ) \biggr ) A ^ { ( 1 ) } \biggl ( \frac { Z } { z - \lambda } + E ( z ) \biggr ) . } } \end{array}
$$

Hence, using Cauchy's theorem of residues,

$$
{ \cal B } ^ { ( 0 ) } = - \frac { 1 } { 2 \pi i } \int _ { L } \left\{ \frac { Z A ^ { ( 1 ) } Z } { z - \lambda } + ( \mathrm { f u n c t i o n ~ a n a l y t i c ~ n e a r ~ } z = \lambda ) \right\} d z .
$$

Let $\pmb { x } _ { j } ( \zeta )$ be a right eigenvector of $A ( \zeta )$ associated with one of the eigenvalues $\bar { \lambda _ { j } } ( \zeta ) , 1 \le j \le p$ Then $Y ( \zeta ) \pmb { x } _ { j } ( \zeta ) = \pmb { x } _ { j } ( \zeta )$ and we see immediately from Eq. (1) that

$$
\begin{array} { r } { B ( \zeta ) { \bf x } _ { j } ( \zeta ) = \zeta ^ { - 1 } ( \lambda - \lambda _ { j } ( \zeta ) ) { \bf x } _ { j } ( \zeta ) . } \end{array}\tag{2}
$$

Thus, $\zeta ^ { - 1 } ( \lambda - \lambda _ { j } ( \zeta ) )$ is an eigenvalue of $B ( \zeta ) _ { : }$ say $\beta ( \zeta )$ . But, since $B ( \zeta )$ has a Taylor expansion at $\zeta = 0 , \beta ( \zeta )$ also has an expansion in fractional powers of ζ. Consequently, for small enough |ζ| and some integer l,

$$
\zeta ^ { - 1 } ( \lambda - \lambda _ { j } ( \zeta ) ) = \beta _ { 0 } + \beta _ { 1 } \zeta ^ { 1 / l } + \beta _ { 2 } \zeta ^ { 2 / l } + \cdots ,
$$

and $\beta _ { 0 }$ is an eigenvalue of the unperturbed matrix $- Z A ^ { ( 1 ) } Z$ This implies

$$
\lambda _ { j } ( \zeta ) = \lambda - \beta _ { 0 } \zeta - \beta _ { 1 } \zeta ^ { 1 + ( 1 / l ) } - \beta _ { 2 } \zeta ^ { 1 + ( 2 / l ) } - \cdot \cdot \cdot .\tag{3}
$$

In other words,

$$
\lambda _ { j } ( \zeta ) = \lambda + a _ { j } \zeta + O ( | \zeta | ^ { 1 + ( 1 / l ) } )
$$

as $| \zeta |  0 ,$ and $a _ { j }$ is an eigenvalue of $Z A ^ { ( 1 ) } Z$

We have proved the first part of the following theorem.

Theorem 1. Let $A ( \zeta )$ be a matrix that is analytic in ζ on a neighborhood of $\zeta = 0 ,$ and suppose $A ( 0 ) = A$ . Let λ be an eigenvalue of A of index 1 and multiplicity m, and let $\lambda _ { j } ( \zeta )$ be an eigenvalue of A(ζ) for which $\lambda _ { j } ( 0 ) = \lambda$ Then there is a number $a _ { j }$ and a positive integer $l \leq m$ such that

$$
\begin{array} { r } { \lambda _ { j } ( \zeta ) = \lambda + a _ { j } \zeta + { \cal O } ( | \zeta | ^ { 1 + ( 1 / l ) } ) } \end{array}\tag{4}
$$

as $| \zeta |  0 ,$ and $a _ { j }$ is an eigenvalue of ${ Z A ^ { ( 1 ) } Z }$

Moreover, to each $\lambda _ { j } ( \zeta )$ corresponds at least one eigenvector $\pmb { x } _ { j } ( \zeta )$ such that, for small enough |ζ|

$$
\pmb { x } _ { j } ( \zeta ) = \pmb { x } + \zeta ^ { 1 / l } \pmb { x } _ { 1 } + \zeta ^ { 2 / l } \pmb { x } _ { 2 } + \cdots ,\tag{5}
$$

where $\begin{array} { r } { { \pmb x } , { \pmb x } _ { 1 } , \ldots , { \pmb x } _ { l - 1 } \in \bf K e r ( \pmb { A } - \lambda I ) a n d a _ { j } { \pmb x } = Z A ^ { ( 1 ) } Z { \pmb x } . } \end{array}$

ProoF. It remains to prove only the statements concerning eigenvectors. But these follow immediately on writing down $A ( \zeta ) \mathbf { x } _ { j } ( \zeta ) = \lambda _ { j } ( \zeta ) \mathbf { x } _ { j } ( \zeta )$ and comparing coefficients of powers of $\zeta ^ { 1 / l }$ B

Now it is important to observe that if $a _ { j }$ is an eigenvalue of ${ \cal Z } A ^ { ( 1 ) } { \cal Z }$ with index 1, then the process can be repeated, that is, we can apply the above analysis to $B ( \zeta )$ instead of $A ( \zeta )$ and find that in expansions (3), the coefficients $\beta _ { 1 } , \beta _ { 2 } , \dots , \beta _ { l - 1 }$ all vanish. This observation will be exploited in Exercise 3 below.

Exercise 1. Find $Z A ^ { ( 1 ) } Z$ for the matrix $A ( \zeta )$ given in Exercise 11.4.2 and show that the result of Theorem 1 is consistent with the expansions for $\hat { \lambda } _ { 1 } ( \zeta )$ and $\lambda _ { 2 } ( \zeta )$ given in that example.

Exercise 2. Verify the results of Theorem 1 for the matrix $A ( \zeta )$ of Exercise 11.4.1 and for the matrix

$$
\begin{array} { r } { \left[ \begin{array} { c c } { 0 } & { \zeta - 1 } \\ { \zeta ( \zeta - 1 ) } & { 0 } \end{array} \right] . } \end{array}
$$

Exercise 3. Prove that if $a _ { j }$ is an eigenvalue of ${ Z A ^ { ( 1 ) } Z }$ of index 1, then there is a number $b _ { j }$ such that

$$
\lambda _ { j } ( \zeta ) = \lambda + a _ { j } \zeta + b _ { j } \zeta ^ { 2 } + { \cal O } ( | \zeta | ^ { 2 + ( 1 / l ) } ) ,\tag{6}
$$

and that $b _ { j }$ is an eigenvalue of ${ \cal Z } ( A ^ { ( 1 ) } E A ^ { ( 1 ) } + A ^ { ( 2 ) } ) { \cal Z }$ with right eigenvector $\pmb { x } . \sqsupset$

Consider the matrix function $B ( \zeta )$ of Lemma 1 once more. Since $Y ( \zeta )$ is just a function of $A ( \zeta )$ (for a fixed $\zeta , A ( \zeta )$ and $Y ( \zeta )$ commute. Also $Y ( \zeta ) ^ { 2 } =$ $Y ( \zeta )$ so we can write, instead of Eq. (1),

$$
B ( \zeta ) = \zeta ^ { - 1 } Y ( \zeta ) ( \lambda I - A ( \zeta ) ) Y ( \zeta ) ,\tag{7}
$$

and this representation has a clear symmetry. In particular, if A and $A ^ { ( 1 ) }$ happen to be Hermitian, then $Y ( 0 ) = Z$ and hence B(0) is also Hermitian. Thus, $B ( 0 )$ has all eigenvalues of index one and repetition of the process described above is legitimate, thus guaranteeing dependence of the perturbed eigenvalues on $S$ like that described by Eq. (6). Furthermore, it looks as though we can repeat the process indefinitely, if all the derivatives of $A ( \zeta )$ at $\zeta = 0$ are Hermitian, and we conclude that $\lambda _ { j } ( \zeta )$ has a Taylor expansion about $\zeta = 0$

But once we bring symmetry into the problem, the considerations of the preamble to this section come into play. Thus, it will now be assumed that $\zeta$ is a real parameter, and that $A ( \zeta )$ is normal for every real $\zeta$ in some open interval containing $\zeta = 0$ Now it follows that whenever $A ( \zeta )$ is normal, $Y ( \zeta )$ and Z are Hermitian (i.e., they are orthogonal projectors), and $B ( \zeta )$

is also normal. In particular, $B ( 0 ) = - Z A ^ { ( 1 ) } Z$ is normal and all eigenvalues of $B ( 0 )$ have index 1. So a second step of the reduction process can be taken and, in fact, repeated indefinitely. This leads to the following conclusion.

Theorem 2. Let $A ( \zeta )$ be analytic and normal throughout a real neighborhood $o f \zeta = 0$ ; then the eigenvalues of $A ( \zeta )$ are analytic in some real neighborhood $o f \zeta = 0$

Moreover, to each eigenvalue $\lambda _ { j } ( \zeta )$ analytic on a real neighborhood of $\zeta = 0$ corresponds at least one eigenvector $\pmb { x } _ { j } ( \zeta )$ that is analytic on the same neighborhood.

Exercise 4. Show that if ζ is real and $A ( \zeta )$ is normal, then $B ( \zeta )$ is normal.

Exercise 5. Let $A ( \zeta )$ be analytic and Hermitian throughout a real neighborhood of $\zeta = 0$ , and suppose that all eigenvalues $\lambda _ { 1 } ( 0 ) , \ldots , \lambda _ { n } ( 0 )$ of $\boldsymbol { A } ( 0 )$ are distinct. Show that there is a real neighborhood $\mathcal { N }$ of $\zeta = 0 ,$ real functions $\lambda _ { 1 } ( \zeta ) , \ldots , \lambda _ { n } ( \zeta )$ that are analytic on $\mathcal { N } ,$ and a matrix-valued function $U ( \zeta )$ that is analytic on $\mathcal { N }$ such that, for $\zeta \in \mathcal { N }$

$$
A ( \zeta ) = U ( \zeta ) ^ { - 1 } \mathrm { d i a g } [ \lambda _ { 1 } ( \zeta ) , \ldots , \lambda _ { n } ( \zeta ) ] U ( \zeta )
$$

and

$$
U ( \zeta ) U ( \zeta ) ^ { * } = I .
$$

(This result also holds without the hypothesis of distinct unperturbed eigenvalues.) □

There are expansions of the form (5) for eigenvectors even when the unperturbed eigenvalue has index greater than 1. Indeed, Exercise 6 demonstrates the existence of a continuous eigenvector. However, even this cannot be guaranteed if the hypothesis of analytic dependence on the parameter is removed. This is illustrated in Exercise 7, due to F. Rellich, in which the matrix is infinitely differentiable at $\zeta = 0$ but not analytic, and it has no eigenvector at $\zeta = 0$ that can be extended in a continuous way to eigenvectors for nonzero values of $\zeta .$

Exercise 6. Adopt the notation and hypotheses of Theorem 1, except that the eigenvalue λ of A may have any index m. Show that there is an eigenvector $\pmb { x } _ { j } ( \zeta )$ of $\pmb { \mathcal { A } } ( \zeta )$ such that the expansion (5) holds for $1 \leq 1$ small enough.

SoLUTiON. Using statement (b) of Section 11.3, we may assume that there is an eigenvalue $\lambda _ { j } ( \zeta )$ of $A ( \zeta )$ that has a power series expansion in powers of $\zeta ^ { 1 / l }$ for $1 5 1$ small enough. Then the matrix $D ( \zeta ) = \lambda _ { i } ( \zeta ) I - A ( \zeta )$ has elements with power series expansions of the same kind.

Suppose that $D ( \zeta )$ has rank r in a deleted neighborhood $\mathcal { N }$ of $\zeta = 0$ (i.e., excluding the point $\zeta = 0$ itself). For simplicity, and without loss of generality, assume that the rth-order minor

$$
D { \left( \begin{array} { l l l l } { 1 } & { 2 } & { \cdots } & { r } \\ { 1 } & { 2 } & { \cdots } & { r } \end{array} \right) }
$$

is nonzero in ${ \mathcal { N } } .$ Then expand the minor

$$
D { \binom { 1 } { 1 } } ^ { 2 } \quad { \stackrel { . . . } { \dots } } \quad r \quad r + 1 \atop r + 1 \wedge
$$

by its last row, and write $l _ { 1 } , \ldots , l _ { r + 1 }$ for the cofactors of $d _ { r + 1 , 1 } , \dotsc , d _ { r + 1 , r + 1 } .$ Thus

$$
D { \binom { 1 } { 1 } } \quad 2 \quad \cdots \quad r + 1 \atop r + 1  \qquad = \sum _ { j = 1 } ^ { r + 1 } d _ { r + 1 , j } l _ { j } = 0 .
$$

Define $l _ { r + 2 } = \dots = l _ { n } = 0$ (for any $\zeta$ in $\mathcal { N } )$ and then write the vector $\pmb { l } =$ $[ { \pmb l } _ { 1 } \quad { \pmb l } _ { 2 } \quad \cdots \quad { \pmb l } _ { n } ] ^ { \pmb \tau }$

Obviously, l is a function of ζ with a power series expansion in ζ¹/ for $\zeta$ $\zeta ^ { 1 / l }$ $| \zeta |$ small enough. Furthermore, $D ( \zeta ) l ( \zeta ) = \pmb { \theta } ,$ so that $l ( \zeta )$ is an eigenvector with the required property. To see this, let D be the jth row of D(ζ). Then $D _ { j * }$ $D ( \zeta )$

$$
D _ { j * } l = \sum _ { k = 1 } ^ { n } d _ { j k } l _ { k } = D { \binom { 1 } { 1 } } 2 \cdots r _ { \phantom { j } } j _ { \phantom { j } } \qquad j \qquad 
$$

This is zero for each j because if $1 \le j \le r$ we have a determinant with two equal rows, and if $j \ge r + 1$ we have a minor of $D$ of order $r + 1$

Exercise 7 (Rellich). Verify that the matrix $A ( x )$ defined for all real x by

$$
A ( 0 ) = 0 , \qquad A ( x ) = e ^ { - 1 / x ^ { 2 } } \left[ \cos ( 2 / x ) \ : \ : \ : \ : \sin ( 2 / x ) \right]
$$

is continuous (even infinitely differentiable) at $x = 0$ and that there is no eigenvector ${ \pmb v } ( { \pmb x } )$ continuous near $x = 0 \mathrm { w i t h } \ v ( 0 ) \neq \pm \ 0 . \quad \bigsqcup$

# Linear Matrix Equations and Generalized Inverses

In this chapter we consider the general linear matrix equation

$$
A _ { 1 } X B _ { 1 } + A _ { 2 } X B _ { 2 } + \cdots + A _ { p } X B _ { p } = C ,
$$

for the unknown matrix X; we will also consider its particular cases, especially the equation of great theoretical and practical importance:

$$
A X + X B = C .
$$

Our investigation of these matrix equations will depend on the idea of the "Kronecker product" of two matrices, a useful notion that has several important applications.

In the second half of the chapter some generalizations of the notion of the inverse of a square matrix are developed. Beginning with “one-sided" inverses, we go on to a widely useful definition of a generalized inverse that is applicable to any matrix, whether square or rectangular. The Moore-Penrose inverse appears as a special case of this analysis, and the chapter concludes with the application of the Moore-Penrose inverse to the solution of $A \mathbf { x } = \pmb { b } ,$ , where A and b are an arbitrary (rectangular) matrix and vector, respectively.

## 12.1 The Notion of a Kronecker Product

In this section we introduce and examine a new operation that, in full generality, is a binary operation from $\mathcal { F } ^ { m \times l } \times \mathcal { F } ^ { n \times k }$ to $\mathcal { F } ^ { m n } \times l k$ , although we shall confine our attention to the case $l = m , k = n .$ This is the most useful case in applications and yields beautiful results concerning the eigenvalues of the product matrix in terms of the factors. The idea of the Kronecker product arises naturally in group theory and, as a result, has important applications in particle physics.

if $A = [ a _ { i j } ] _ { i , j = 1 } ^ { m } \in \mathcal { F } ^ { m \times m } , B = [ b _ { i j } ] _ { i , j = 1 } ^ { n } \in \mathcal { F } ^ { n \times n }$ , then the right Kronecker (or direct, or tensor) product of A and $B ,$ written ${ \cal A } \otimes { \cal B } ,$ is defined to be the partitioned matrix

$$
A \otimes B = \left[ \begin{array} { c c c c } { a _ { 1 1 } B } & { a _ { 1 2 } B } & { \cdots } & { a _ { 1 m } B } \\ { a _ { 2 1 } B } & { a _ { 2 2 } B } & { \cdots } & { a _ { 2 m } B } \\ { \vdots } & { \vdots } & { } & { \vdots } \\ { a _ { m 1 } B } & { a _ { m 2 } B } & { \cdots } & { a _ { m m } B } \end{array} \right] = [ a _ { i j } B ] _ { i , j = 1 } ^ { m } \in \mathcal { F } ^ { m n \times m n } .
$$

For example, if

$$
A = { \left[ \begin{array} { l l } { a _ { 1 1 } } & { a _ { 1 2 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } \end{array} \right] } , \qquad B = { \left[ \begin{array} { l l } { b _ { 1 1 } } & { b _ { 1 2 } } \\ { b _ { 2 1 } } & { b _ { 2 2 } } \end{array} \right] } ,
$$

then

$$
A \otimes B = { \left[ \begin{array} { l l l l } { a _ { 1 1 } b _ { 1 1 } } & { a _ { 1 1 } b _ { 1 2 } } & { a _ { 1 2 } b _ { 1 1 } } & { a _ { 1 2 } b _ { 1 2 } } \\ { a _ { 1 1 } b _ { 2 1 } } & { a _ { 1 1 } b _ { 2 2 } } & { a _ { 1 2 } b _ { 2 1 } } & { a _ { 1 2 } b _ { 2 2 } } \\ { a _ { 2 1 } b _ { 1 1 } } & { a _ { 2 1 } b _ { 1 2 } } & { a _ { 2 2 } b _ { 1 1 } } & { a _ { 2 2 } b _ { 1 2 } } \\ { a _ { 2 1 } b _ { 2 1 } } & { a _ { 2 1 } b _ { 2 2 } } & { a _ { 2 2 } b _ { 2 1 } } & { a _ { 2 2 } b _ { 2 2 } } \end{array} \right] } .
$$

It should be noted that the left Kronecker product of A and $B ,$ defined to be the matrix

$$
{ \left[ \begin{array} { l l l } { A b _ { 1 1 } } & { \cdots } & { A b _ { 1 n } } \\ { \vdots } & { } & { \vdots } \\ { A b _ { n 1 } } & { \cdots } & { A b _ { n n } } \end{array} \right] } ,
$$

has similar properties to those of ${ \cal A } \otimes { \cal B } ,$ but to avoid unnecessary duplication, only the right Kronecker product, called merely the Kronecker product, will be discussed.

Exercise 1. Verify that for any square matrix $A = [ a _ { i j } ] _ { i , j = 1 } ^ { m }$

$$
\begin{array} { r l } { \mathrm { ( a ) } } & { { } I _ { n } \otimes A = \mathrm { d i a g } [ A , A , \ldots , A ] , } \\ { \mathrm { ( b ) } } & { { } A \otimes I _ { n } = { \left[ \begin{array} { l l l l } { a _ { 1 1 } I _ { n } } & { a _ { 1 2 } I _ { n } } & { \cdots } & { a _ { 1 m } I _ { n } } \\ { \vdots } & { } & { \vdots } & { } \\ { a _ { m 1 } I _ { n } } & { a _ { m 2 } I _ { n } } & { \cdots } & { a _ { m m } I _ { n } } \end{array} \right] } ; } \\ { \mathrm { ( c ) } } & { { } I _ { m } \otimes I _ { n } = I _ { m n } . \quad \bigcup } \end{array}
$$

The properties of the Kronecker product incorporated in Proposition 1 follow immediately from the definition.

Proposition 1. If the orders of the matrices involved are such that all the operations below are defined, then

(a) $I f \mu \in { \mathcal { F } } , ( \mu A ) \otimes B = A \otimes ( \mu B ) = \mu ( A \otimes B )$

(b) $( A + B ) \otimes C = ( A \otimes C ) + ( B \otimes C )$ ;

(c) $A \otimes ( B + C ) = ( A \otimes B ) + ( A \otimes C )$ );

(d) $A \otimes ( B \otimes C ) = ( A \otimes B ) \otimes C ;$

(e) $( A \otimes B ) ^ { \boldsymbol { \mathsf { T } } } = A ^ { \boldsymbol { \mathsf { T } } } \otimes B ^ { \boldsymbol { \mathsf { T } } } .$

We need a further property that is less obvious and will be found very useful.

Proposition 2. $I f A , C \in { \mathcal { F } } ^ { m \times m }$ and B, $D \in \mathcal { F } ^ { n \times n }$ , then

$$
( A \otimes B ) ( C \otimes D ) = A C \otimes B D .\tag{1}
$$

PROOF. Write A ⊗ $B = [ a _ { i j } B ] _ { i , j = 1 } ^ { m } , C \otimes D = [ c _ { i j } D ] _ { i , j = 1 } ^ { m }$ . The i, jth block of $( A \otimes B ) ( C \otimes D )$ is

$$
F _ { i j } = \sum _ { k = 1 } ^ { m } ( a _ { i k } B ) ( c _ { k j } D ) = \sum _ { k = 1 } ^ { m } a _ { i k } c _ { k j } B D , \qquad { \mathrm { f o r } } \quad 1 \leq i , j \leq m .
$$

On the other hand, by the definition of the Kronecker product, $A C \otimes B D =$ $[ \gamma _ { i j } B D ] _ { i , j = 1 } ^ { m }$ , where $\gamma _ { i j }$ is the $i , j \mathbf { t }$ h element of $A C$ and is given by the formula $\begin{array} { r } { \gamma _ { i j } = \sum _ { k = 1 } ^ { m } a _ { i k } c _ { k j } } \end{array}$ . Thus $F _ { i j } = \gamma _ { i j } B D$ for each possible pair $( i , j ) ,$ and the result follows.

Proposition 2 has some important consequences, which we list in the following corollaries.

Corollary 1. If $A \in \mathcal { F } ^ { m \times m } , B \in \mathcal { F } ^ { n \times n } ,$ then

(a) $A \otimes B = ( A \otimes I _ { n } ) ( I _ { m } \otimes B ) = ( I _ { m } \otimes B ) ( A \otimes I _ { n } ) .$

(b) $( A \otimes B ) ^ { - 1 } = A ^ { - 1 } \otimes B ^ { - 1 }$ , provided that $A ^ { - 1 }$ and $B ^ { - 1 }$ exist.

Note that the assertion of Corollary 1(a) states the commutativity of $A \otimes I _ { n }$ and $I _ { m } \otimes B _ { \ l }$

Corollary 2. If $A _ { 1 } , A _ { 2 } , \ldots , A _ { p } \in { \mathcal { F } } ^ { m \times m }$ and $B _ { 1 } , B _ { 2 } , \ldots , B _ { p } \in { \mathcal { F } } ^ { n \times n }$ , then

$$
( A _ { 1 } \otimes B _ { 1 } ) ( A _ { 2 } \otimes B _ { 2 } ) \cdot \cdot \cdot ( A _ { p } \otimes B _ { p } ) = ( A _ { 1 } A _ { 2 } \cdot \cdot \cdot A _ { p } ) \otimes ( B _ { 1 } B _ { 2 } \cdot \cdot \cdot B _ { p } ) .
$$

The Kronecker product is, in general, not commutative. However, the next Proposition shows that $A \otimes B$ and B ⊗ A are intimately connected.

Proposition 3. If $A \in { \mathcal { F } } ^ { m \times m } , B \in { \mathcal { F } } ^ { n \times n }$ , then there exists a permutation matrix $P \in \mathbb { R } ^ { m n \times m n }$ such that

$$
P ^ { \mathrm { \scriptscriptstyle T } } ( A \otimes B ) P = B \otimes A .
$$

ProoF. First observe that by a simultaneous interchange of rows and columns with the same number, the matrix $A \otimes I _ { n }$ can be reduced to the matrix $I _ { n } \otimes A$ Thus, there exists a permutation matrix P such that $P ^ { \mathrm { T } } ( A \otimes I _ { n } ) P = I _ { n } \otimes A$ . In fact, if the permutation of 1, 2, 3, . .. , mn, which is equal to

$$
\begin{array} { c } { { 1 , n + 1 , 2 n + 1 , \ldots , ( m - 1 ) n + 1 , 2 , n + 2 , 2 n + 2 , \ldots , ( m - 1 ) n + 2 , } } \\ { { \ldots , n , 2 n , 3 n , \ldots , ( m - 1 ) n , m n , } } \end{array}
$$

is denoted by $i _ { 1 } , i _ { 2 } , \ldots , i _ { m n }$ , then the permutation P has the unit coordinate vectors $e _ { i _ { 1 } } , e _ { i _ { 2 } } , \ldots , e _ { i _ { m n } }$ for its columns. Now observe that the same matrix P performs the transformation $P ^ { \mathrm { { T } } } ( I _ { m } \otimes B ) P = B \otimes I _ { m }$ . Since $P P ^ { \boldsymbol { \mathsf { T } } } = I ,$ then by a repeated use of Corollary 1(a), it is found that

$$
\begin{array} { r } { P ^ { \mathrm { T } } ( A \otimes B ) P = P ^ { \mathrm { T } } ( A \otimes I _ { n } ) P P ^ { \mathrm { T } } ( I _ { m } \otimes B ) P ~ } \\ { = ( I _ { n } \otimes A ) ( B \otimes I _ { m } ) = B \otimes A , } \end{array}
$$

and the proposition is established.

Exercise 2. If $A \in \mathcal { F } ^ { m \times m } , B \in \mathcal { F } ^ { n \times n }$ , prove that

$$
\operatorname * { d e t } ( A \otimes B ) = ( \operatorname * { d e t } A ) ^ { n } ( \operatorname * { d e t } B ) ^ { m } .
$$

SoLUTION. In view of Corollary 1(a), it is sufficient to find the determinants of the matrices $A \otimes I _ { n }$ and $I _ { m } \otimes B .$ By Exercise $1 ( \mathsf { a } ) , \mathsf { d e t } ( I _ { m } \otimes B ) = ( \mathsf { d e t } \ : B ) ^ { m }$ Using Proposition 3 and the property det $P = \pm 1$ , we have

$$
\operatorname* { d e t } ( A \otimes I _ { n } ) = ( \operatorname* { d e t } P ^ { \mathtt { T } } ) \mathrm { d e t } ( I _ { n } \otimes A ) ( \operatorname* { d e t } P ) = ( \operatorname* { d e t } A ) ^ { n } ,
$$

and the result follows. □

Now we define a vector-valued function associated with a matrix and closely related to the Kronecker product. For a matrix $A \in \mathcal { F } ^ { m \times n }$ write $A = [ A _ { * 1 } \quad A _ { * 2 } \quad \cdots \quad A _ { * n } ]$ , where $A _ { * j } \in \mathcal { F } ^ { m } , j = 1 , 2 , \dotsc , n .$ Then the vector

$$
\left[ \begin{array} { c } { A _ { * 1 } } \\ { A _ { * 2 } } \\ { \vdots } \\ { A _ { * n } } \end{array} \right] \in \mathcal { F } ^ { m n }
$$

is said to be the vec-function of A and is written vec A. It is the vector formed by “stacking" the columns of A into one long vector. Note that the vecfunction is linear:

$$
\operatorname { v e c } ( \alpha A + \beta B ) = \alpha \operatorname { v e c } A + \beta \operatorname { v e c } B ,
$$

for any A, $B \in \mathcal { F } ^ { m \times n }$ and $\alpha , \beta \in { \mathcal { F } } .$ Also, the matrices $A _ { 1 } , A _ { 2 } , \ldots , A _ { k }$ from $\mathbb { C } ^ { m \times n }$ are linearly independent as members of ${ \mathcal { F } } ^ { m \times n }$ if and only if vec $A _ { 1 }$

vec $A _ { 2 } , \ldots$ , vec $A _ { k }$ are linearly independent members of ${ \mathcal { F } } ^ { m n }$ The next result indicates a close relationship between the vec-function and the Kronecker product.

Proposition 4. If $A \in \mathcal { F } ^ { m \times m } , B \in \mathcal { F } ^ { n \times n } , X \in \mathcal { F } ^ { m \times n }$ , then

$$
\operatorname { v e c } ( A X B ) = ( B ^ { \mathrm { { T } } } \otimes A ) \operatorname { v e c } X .
$$

PROOF. For $j = 1 , 2 , \dots , n ,$ , the j-column $( A X B ) _ { * j }$ can be expressed

$$
( A X B ) _ { * j } = A X B _ { * j } = \sum _ { k = 1 } ^ { n } b _ { k j } ( A X ) _ { * k } = \sum _ { k = 1 } ^ { m } ( b _ { k j } A ) X _ { * k } ,
$$

where $b _ { k j }$ is the element of B in the k, jth position. Consequently,

$$
( A X B ) _ { * j } = [ b _ { 1 j } A b _ { 2 j } A \quad \cdot \cdot b _ { n j } A ] \mathrm { v e c } X ,
$$

and it remains to observe that the expression in brackets is the jth block-row in $B ^ { \mathrm { T } } \otimes A .$

## Corollary 1. With the previous notation,

(a) ${ \mathfrak { v e c } } ( A X ) = ( I _ { n } \otimes A )$ vec X;

(b) ${ \mathsf { v e c } } ( X B ) = ( B ^ { \mathsf { T } } \otimes I _ { m } )$ vec X;

(c) ${ \mathrm { v e c } } ( A X + X B ) = ( ( I _ { n } \otimes A ) + ( B ^ { \operatorname { T } } \otimes I _ { m } ) )$ vec X.

Important applications of these results will be considered in Section 3. We conclude with a few more properties of the Kronecker product.

Exercise 3. If $A \in \mathcal { F } ^ { m \times m } , B \in \mathcal { F } ^ { n \times n } ,$ , prove that

(a) $\operatorname { t r } ( A \otimes B ) = ( \operatorname { t r } A ) ( \operatorname { t r } B )$

(b) ran $\mathbf { k } ( A \otimes B ) = ( \operatorname { r a n k } A ) ( \operatorname { r a n k } B ) .$

Hint. For part (a) use the representation $A \circledast B = [ a _ { i j } B ] _ { i , j = 1 } ^ { m }$ . Use Proposition 2 for part (b).

Exercise 4. Write $A ^ { [ 1 ] } = A$ and define ${ \cal A } ^ { [ k + 1 ] } = { \cal A } \otimes { \cal A } ^ { [ k ] } , k = 1 , 2 , \ldots .$ Prove that

(a) $A ^ { [ k + l ] } = A ^ { [ k ] } A ^ { [ l ] }$ :’

(b) If $A , B \in { \mathcal { F } } ^ { n \times n }$ , then $( A B ) ^ { [ k ] } = A ^ { [ k ] } B ^ { [ k ] }$

Note the contrast with $( A B ) ^ { k }$

Exercise 5. Verify that

(a) The Kronecker product of diagonal matrices is a diagonal matrix;

(b) The Kronecker product of upper- (respectively, lower-) triangular matrices is an upper- (respectively, lower-) triangular matrix.

Exercise 6. Prove that, if $A _ { 1 } , B _ { 1 }$ are similar to the matrices $A _ { 2 } , B _ { 2 }$ , respectively, then $A _ { 1 } \otimes B _ { 1 }$ is similar to $A _ { 2 } \otimes B _ { 2 }$ . In particular, if $A _ { 1 }$ and $B _ { 1 }$ are simple, then so is $A _ { 1 } \otimes B _ { 1 }$

Exercise 7. If $A \in \mathcal { F } ^ { m \times m }$ , prove that, for any function $f ( \lambda )$ defined on the spectrum of A,

(a) $f ( I _ { n } \otimes A ) = I _ { n } \otimes f ( A )$ );

(b) $f ( A \otimes I _ { n } ) = f ( A ) \otimes I _ { n }$ □

## 12.2 Eigenvalues of Kronecker Products and Composite Matrices

One of the main reasons for interest in the Kronecker product is a beautifully simple connection between the eigenvalues of the matrices A and B and A © B. We obtain this relation from a more general result concerning composite matrices of Kronecker products.

Consider a polynomial p in two variables, x and $y ,$ with complex coefficients. Thus, for certain complex numbers $c _ { i j }$ and a positive integer l,

$$
p ( x , y ) = \sum _ { i , j = 0 } ^ { l } c _ { i j } x ^ { i } y ^ { j } .
$$

If $A \in \mathbb { C } ^ { m \times m }$ and $\pmb { { \cal B } } \in \mathbb { C } ^ { n \times n }$ , we consider matrices in $\mathbb { C } ^ { m n \times m n }$ of the form

$$
p ( A ; B ) = \sum _ { i , j = 0 } ^ { l } c _ { i j } A ^ { i } \otimes B ^ { j } .
$$

For example, if $p ( x , y ) = 2 x + x y ^ { 3 }$ , we write 2x $+ \ x y ^ { 3 } = 2 x ^ { 1 } y ^ { 0 } + x ^ { 1 } y ^ { 3 }$ and

$$
p ( A ; B ) = 2 A \otimes I _ { n } + A \otimes B ^ { 3 } .
$$

The next theorem gives a connection between the eigenvalues of A and B and those of $p ( A ; B )$

Theorem 1 (C. Stephanos†). $I f \lambda _ { 1 } , \ldots , \lambda _ { m }$ are the eigenvalues of $A \in \mathbb { C } ^ { m \times m }$ and $\mu _ { 1 } , \ldots , \mu _ { n }$ are the eigenvalues of $\ b { B } \in \mathbb { C } ^ { n \times n }$ , then the eigenvalues of $p ( A ; B )$ are the mn numbers $p ( \lambda _ { r } , \mu _ { s } )$ , where $r = 1 , 2 , \ldots , m$ and $s = 1 , 2 , \ldots , n .$

PROOF. Let matrices $P \in \mathbb { C } ^ { m \times m }$ and $Q \in \mathbb { C } ^ { n \times n }$ be defined so that

$$
P A P ^ { - 1 } = J _ { 1 } , \qquad Q B Q ^ { - 1 } = J _ { 2 } ,
$$

where $J _ { 1 }$ and $J _ { 2 }$ are matrices in Jordan normal form (Section 6.5). It is clear that $J _ { 1 } ^ { i }$ is an upper-triangular matrix having $\lambda _ { 1 } ^ { i } , \ldots , \lambda _ { m } ^ { i }$ as its main diagonal elements and similarly, $\mu _ { 1 } ^ { j } , \ldots , \mu _ { n } ^ { j }$ are the main diagonal elements of the upper-triangular matrix $J _ { 2 } ^ { j }$

Furthermore, from Exercise 12.1.5 it follows that $J _ { \textbf { 1 } } ^ { i } \otimes J _ { 2 } ^ { j }$ is also an uppertriangular matrix. It is easily checked that its diagonal elements are $\lambda _ { r } ^ { i } \mu _ { s } ^ { j }$ for $r = 1 , 2 , \ldots , m , s = 1 , 2 , \ldots , n .$ Hence the matrix $p ( J _ { 1 } ; J _ { 2 } )$ is uppertriangular and has diagonal elements $p ( \lambda _ { r } , \mu _ { s } )$ . But the diagonal elements of an upper-triangular matrix are its eigenvalues; hence $p ( J _ { 1 } ; J _ { 2 } )$ has eigenvalues $p ( \lambda _ { r } , \mu _ { s } )$ for $r = 1 , 2 , \ldots , m , s = 1 , 2 , \ldots , n .$

Now we have only to show that $p ( J _ { 1 } ; J _ { 2 } )$ and $p ( A ; B )$ have the same eigenvalues. On applying Corollary 2 to Proposition 12.1.2, we find that

$$
\begin{array} { c } { { J _ { 1 } ^ { i } \otimes J _ { 2 } ^ { j } = P A ^ { i } P ^ { - 1 } \otimes Q B ^ { j } Q ^ { - 1 } } } \\ { { = ( P \otimes Q ) ( A ^ { i } \otimes B ^ { j } ) ( P ^ { - 1 } \otimes Q ^ { - 1 } ) , } } \end{array}
$$

and by Corollary 1 to Proposition 12.1.2, $P ^ { - 1 } \otimes Q ^ { - 1 } = ( P \otimes Q ) ^ { - 1 }$ . Thus,

$$
J _ { 1 } ^ { i } \otimes J _ { 2 } ^ { j } = ( P \otimes Q ) ( A ^ { i } \otimes B ^ { j } ) ( P \otimes Q ) ^ { - 1 } ,
$$

and hence

$$
p ( J _ { 1 } ; J _ { 2 } ) = ( P \otimes Q ) p ( A ; B ) ( P \otimes Q ) ^ { - 1 } .
$$

This shows that $p ( J _ { 1 } ; J _ { 2 } )$ and $p ( A ; B )$ are similar and so they must have the same eigenvalues (Section 4.10).■

The two following special cases (for $p ( x , y ) = x y$ and $p ( x , y ) = x + y )$ are probably the most frequently used.

Corollary 1. The eigenvalues of $A \otimes B$ are the mn numbers $\lambda _ { r } \mu _ { s } , r = 1$ $2 , \ldots , m , s = 1 , 2 , \ldots , n .$

Corollary 2. The eigenvalues of $( I _ { n } \otimes A ) + ( B \otimes I _ { m } )$ (or, what is equivalent in view of Exercise 4.11.9, of $( I _ { n } \otimes A ^ { \mathsf { T } } ) + ( B ^ { \mathsf { T } } \otimes I _ { m } ) )$ are the mn numbers $\lambda _ { r } + \mu _ { s } , r = 1 , 2 , \ldots , m , s = 1 , 2 , \ldots , n .$

The matrix $( I _ { n } \otimes A ) + ( B \otimes I _ { m } )$ is often called the Kronecker sum of A and B.

Exercise 1. If $C \in \mathcal { F } ^ { m n \times m n }$ is the Kronecker sum of $A \in \mathcal { F } ^ { m \times m }$ and $B \in \mathcal { F } ^ { n \times n }$ prove that $e ^ { C } = e ^ { A } \otimes e ^ { B }$ and indicate a corresponding result in numbers.

Hint. Use Exercise 12.1.7 for $f ( \lambda ) = e ^ { \lambda } .$

Exercise 2. Let $A \in \mathbb { C } ^ { n \times n }$ and let $\pmb { { \cal B } } \in \mathbb { C } ^ { m n \times m n }$ be the partitioned matrix with each of its $m ^ { 2 }$ blocks equal to A. If A has eigenvalues $\mu _ { 1 } , \ldots , \mu _ { n }$ (not necessarily distinct), prove that the eigenvalues of B are $m \mu _ { 1 } , \ldots , m \mu _ { n }$ and $m ( n - 1 )$ zeros.

Hint. Express B as a Kronecker product.

Exercise 3. If $\pmb { x } = [ \alpha _ { 1 } \quad \alpha _ { 2 } \quad \cdot \cdot \cdot \quad \alpha _ { m } ] ^ { \mathsf { T } } \in \mathbb { C } ^ { m }$ is an eigenvector of $A \in \mathbb { C } ^ { m ^ { \times } }$ m corresponding to the eigenvalue λ, and $\pmb { y } \in \mathbb { C } ^ { n }$ is an eigenvector of $\pmb { { \cal B } } \in \mathbb { C } ^ { n \times n }$ corresponding to the eigenvalue $\mu ,$ show that an eigenvector z of A ⊗ B associated with $\lambda \mu$ is

$$
\boldsymbol { z } = [ { \alpha _ { 1 } } { y } ^ { \mathrm { T } } \quad { \alpha _ { 2 } } { y } ^ { \mathrm { T } } \quad \cdot \cdot \cdot \quad { \alpha _ { m } } { y } ^ { \mathrm { T } } ] ^ { \mathrm { T } } .\tag{1}
$$

Exercise 4. Show that if A and B are positive definite matrices, then $A \otimes B$ is positive definite.

Define the (right) Kronecker product of two rectangular matrices $A = [ a _ { i j } ] _ { i , j = 1 } ^ { m , l } \in \mathcal { F } ^ { m \times l }$ and $B \in \mathcal { F } ^ { n \times k }$ to be the matrix

$$
A \otimes B \triangleq [ a _ { i j } B ] _ { i , j = 1 } ^ { m , l } \in \mathcal { F } ^ { m n \times l k } .\tag{2}
$$

Exercise 5. Establish the assertions of Propositions 12.1.1 and 12.1.2 for rectangular matrices.

Exercise 6. Let x, $y \in \mathbb { C } ^ { m }$ and u, $\pmb { v } \in \mathbb { C } ^ { n }$ . Show that the equation $\pmb { x } \circledast$ u $= \textbf { y } \otimes$ v implies that $\boldsymbol { y } = \lambda \boldsymbol { x }$ and ${ \mathfrak { v } } = \lambda { \mathfrak { u } }$ for some $\lambda \in \mathbb { C }$ □

Observe that, using the general definition of a Kronecker product of rectangular matrices (see Eq. (2)), we may write z in Eq. (1) as ${ \pmb z } = { \pmb x } \otimes { \pmb y }$ and use the generalized Proposition 12.1.1 (see Exercise 5) for proving Exercise 3. Furthermore, if A and B are simple, so is $A \otimes B$ (Exercise 12.1.6) and hence there is an eigenbasis for $\mathbb { C } ^ { m n \times m n }$ with respect to A © B consisting entirely of the Kronecker products $x _ { i } \otimes y _ { j }$ , where $\left\{ x _ { i } \right\} _ { i = 1 } ^ { m } , \left\{ y _ { j } \right\} _ { j = 1 } ^ { n }$ are the eigenbases in $\mathbb { C } ^ { m }$ and $\mathbb { C } ^ { n }$ for A and B, respectively. In the general case the situation is more complicated.

## 12.3 Applications of the Kronecker Product to Matrix Equations

We start by studying the general linear matrix equation

$$
A _ { 1 } X B _ { 1 } + A _ { 2 } X B _ { 2 } + \cdots + A _ { p } X B _ { p } = C ,\tag{1}
$$

where $A _ { j } \in \mathbb { C } ^ { m \times m } , B _ { j } \in \mathbb { C } ^ { n \times n } ( j = 1 , 2 , . . . , p ) , X , C \in \mathbb { C } ^ { m \times n }$ , and its particular cases. The method we use relies on the assertion of Proposition 12.1.4 and reduces Eq. (1) to a matrix-vector equation of the form $G x = \pmb { c } ,$ where $G \in \mathbb { C } ^ { m n \times m n }$ and $\pmb { x } , \pmb { c } \in \mathbb { C } ^ { m n }$

Theorem 1. A matrix $\pmb { X } \in \mathbb { C } ^ { m \times n }$ is a solution of Eq. (1) if and only if the vector x = vec X defined in Section 12.1 is a solution of the equation

$$
G \pmb { x } = \pmb { c } ,\tag{2}
$$

with $\begin{array} { r } { G = \sum _ { j = 1 } ^ { p } ( B _ { j } ^ { \operatorname { T } } \circledast A _ { j } ) } \end{array}$ and c = vec C.

ProoF. By Proposition 12.1.4, vec $( A _ { j } X B _ { j } ) = ( B _ { j } ^ { \operatorname { T } } \otimes A _ { j } )$ vec X for each $j = 1 , 2 , \ldots , p .$ Since the function vec A is linear, then

$$
\mathrm { v e c } ~ C = \sum _ { j = 1 } ^ { p } ~ ( B _ { j } ^ { \mathrm { T } } \otimes A _ { j } ) \mathrm { v e c } ~ X
$$

and the result follows.

Having transformed the linear matrix equation to an equation of the form $G { \pmb x } = { \pmb c } .$ we may now apply the results developed in Section 3.10 to determine criteria for the existence and uniqueness of a solution (see also Theorem 12.6.7 to follow).

Corollary 1. Equation (1) has a solution X if and only if rank[G c] = rank G.

Corollary 2. Equation (1) has a unique solution if and only if the matrix G in Eq. (2) is nonsingular.

We now consider an important particular case of Eq. (1); the matrix equation

$$
A X + X B = C .\tag{3}
$$

Theorem 2. Equation (3) has a unique solution if and only if the matrices A and — B have no eigenvalues in common

PRooF. In the case being considered, the matrix G in Eq. (2) is $\left( { { I } _ { n } } \otimes A \right) +$ $( B ^ { \boldsymbol { \mathsf { T } } } \otimes I _ { m } )$ and its eigenvalues are, by Corollary 12.2.2, the numbers $\lambda _ { r } + \mu _ { s }$ $r = 1 , 2 , \ldots , m , s = 1 , 2 , \ldots , n .$ It remains now to apply Corollary 2 and recall that a matrix is nonsingular if and only if all its eigenvalues are nonzero.■

There is a special case in which we can obtain an explicit form for the solution matrix X of Eq. (3).

Theorem 3. If all eigenvalues of the matrices $A \in C ^ { m \times m }$ and $B \in C ^ { n \times n }$ have negative real parts (that is, A and B are stable), then the unique solution X of Eq. (3) is given by

$$
X = \mathrm { ~ - ~ } \int _ { 0 } ^ { \infty } e ^ { A t } C e ^ { B t } d t .\tag{4}
$$

ProoF. First observe that the conditions of the theorem imply that A and — B have no eigenvalue in common, and hence there is a unique solution X of Eq. (3).

Consider a matrix-valued function Z(t) defined as the solution of the initial-value problem

$$
d Z / d t = A Z + Z B , \qquad Z ( 0 ) = C .\tag{5}
$$

As indicated in Exercise 9.12.14, the solution of Eq. (5) is

$$
Z ( t ) = e ^ { A t } C e ^ { B t } .
$$

Now observe that, integrating the differential equation in (5) from $t = 0$ to $t = \infty$ under the hypothesis that the matrix (4) exists, we obtain

$$
Z ( \infty ) - Z ( 0 ) = A \int _ { 0 } ^ { \infty } Z ( t ) d t + \left( \int _ { 0 } ^ { \infty } Z ( t ) d t \right) B .
$$

Hence assuming, in addition, that

$$
Z ( \infty ) = \operatorname* { l i m } _ { t ^ {  } \infty } e ^ { A t } C e ^ { B t } = 0 ,\tag{6}
$$

it is found that the matrix given by Eq. (4) is the (unique) solution of Eq. (3). Thus it suffices to check that, for stable A and B, the assumptions we have had to make are valid. To this end, write the spectral resolution (Eq. (9.5.1)) for the function $e ^ { A t } \left( 0 < t < \infty \right)$

$$
e ^ { \boldsymbol { A } t } = \sum _ { \boldsymbol { k } = 1 } ^ { s } \sum _ { j = 0 } ^ { m _ { \boldsymbol { k } } - 1 } t ^ { j } e ^ { \lambda _ { \boldsymbol { k } } t } Z _ { \boldsymbol { k } j } ,\tag{7}
$$

where $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ are the distinct eigenvalues of A with indices $m _ { 1 } , m _ { 2 } , \ldots , m _ { s }$ , respectively. Consider the Cartesian decomposition of the eigenvalues, $\lambda _ { k } = \alpha _ { k } + i \beta _ { k }$ , and write

$$
e ^ { \lambda _ { k } t } = e ^ { \alpha _ { k } t } e ^ { i \beta _ { k } t } = e ^ { \alpha _ { k } t } ( \cos \beta _ { k } t + i \sin \beta _ { k } t ) ,
$$

for each $k = 1 , 2 , \ldots , s .$ Since $\alpha _ { k } < 0 \ ( k = 1 , 2 , \ldots , s ) _ { }$ , it follows that, for each k, $\mathrm { e x p } ( \lambda _ { k } t ) \to 0$ as $t  \infty$ . Hence (see Eq. (7)) $\begin{array} { r } { \operatorname* { l i m } _ { t \to \infty } e ^ { A t } = O } \end{array}$ and, similarly, $\quad \operatorname* { l i m } _ { t \to \infty } e ^ { B t } = O$ . Thus, the relation (6) as well as the existence of the integral in (4) follow.

Now consider the case in which A and — B have eigenvalues in common. Then the matrix $G = ( I _ { n } \otimes A ) + ( B ^ { \boldsymbol { \mathsf { T } } } \otimes I _ { m } )$ is singular and solutions exist, provided rank[G c] = rank G (Corollary 1). The number of linearly independent solutions is then determined by the dimension of the kernel of G. The direct determination of dim(Ker G) poses a relatively difficult question and can be found in the standard reference book by MacDuffee (1946) where the Frobenius proof is presented; this proof dates back to 1910.

However, we prefer at this moment to abandon the idea of using the Kronecker product in investigating the solvability and the number of linearly independent solutions of Eq. (3). Our line of attack will restart with a study of the particular cases $A X = X A$ in Section 12.4 and then $A X +$ $X B = O$ in Section 12.5, where the problems mentioned regarding the general equation $A X + X B = C$ will be resolved.

Exercise 1. Let A be a stable matrix and suppose $W \geq 0 .$ Show that the Lyapunov equation $A X + X A ^ { * } = - W$ has a unique solution X and that $X \geq O$ (See also Section 13.1.)

Exercise 2. Let $A \in \mathbb { C } ^ { m \times m } , B \in \mathbb { C } ^ { n \times n }$ , and $C \in \mathbb { C } ^ { m \times n }$ . If A and B have spectral radii $\mu _ { A }$ and $\mu _ { B }$ , respectively, and $\mu _ { A } \mu _ { B } < 1$ , show that the equation

$$
X = A X B + C\tag{8}
$$

has a unique solution X and that this solution is given by

$$
X = \sum _ { j = 0 } ^ { \infty } A ^ { j } C B ^ { j } .
$$

Exercise 3. Show that Eq. (8) has a unique solution if $\lambda \mu \neq 1$ for all $\lambda \in \sigma ( A )$ and $\mu \in \sigma ( B )$

Exercise 4. Let A, $C \in \mathbb { C } ^ { n \times n }$ and $C ^ { * } = C$ If the equation

$$
X = \leavevmode { A ^ { * } X A + C }
$$

has a unique solution X, show that X is Hermitian. Also, if $\mu _ { A } < 1$ , show that $( X - C ) \geq 0$ . In particular, if $C \geq 0 ,$ then $X \geq 0$

Exercise 5. If $A > 0 , C > 0 .$ and $X = A X A + C$ , show that $\mu _ { A } < 1$ □

## 12.4 Commuting Matrices

An important special case of Eq. (12.3.3) arises when $C = O$ and $B = - A$

$$
A X = X A , \quad \ A , X \in \mathbb { C } ^ { n \times n } .\tag{1}
$$

Clearly, finding all the solutions X of Eq. (1) is equivalent to determining all matrices that commute with the given matrix A. To this end, we first observe that if $A = P J P ^ { - 1 }$ , where J is a Jordan normal form for A, then Eq. (1) is equivalent to the equation

$$
J Y = Y J ,\tag{2}
$$

where $Y = P ^ { - 1 } X P $

Proceeding to the analysis of the reduced Eq. (2) we write $J = \mathrm { d i a g } [ J _ { 1 } , J _ { 2 } , . . . , J _ { p } ]$ , where $J _ { s } = \lambda _ { s } I _ { k _ { s } } + N _ { k _ { s } }$ is a $k _ { s } \times k _ { s }$ Jordan block associated with an eigenvalue $\lambda _ { s } ( 1 \le s \bar { \le } p )$ . Hence, performing a corresponding partition of Y in Eq. (2),

$$
\begin{array} { r } { Y = [ Y _ { s t } ] _ { s , t = 1 } ^ { p } , \qquad Y _ { s t } \in \mathbb { C } ^ { k _ { s } \times k _ { t } } , } \end{array}
$$

Eq. (2) is reduced to the following system:

$$
J _ { s } Y _ { s t } = Y _ { s t } J _ { t } , \qquad s , t = 1 , 2 , \ldots , p ,
$$

or, exploiting the structure of Jordan blocks,

$$
( \lambda _ { s } - \lambda _ { t } ) Y _ { s t } = Y _ { s t } N _ { k _ { t } } - N _ { k _ { s } } Y _ { s t } , \qquad s , t = 1 , 2 , \ldots , p .\tag{3}
$$

We now consider two possible cases.

Case (1) $\lambda _ { s } \neq \lambda _ { t }$ . Multiplying Eq. (3) by $\lambda _ { s } - \lambda _ { t }$ and using Eq. (3) again, we obtain

$$
( \lambda _ { s } - \lambda _ { t } ) ^ { 2 } Y _ { s t } = ( Y _ { s t } N _ { k _ { t } } - N _ { k _ { s } } Y _ { s t } ) N _ { k _ { t } } - N _ { k _ { s } } ( Y _ { s t } N _ { k _ { t } } - N _ { k _ { s } } Y _ { s t } ) .
$$

Simplifying the right-hand expression and multiplying successively by $\lambda _ { s } - \lambda _ { t }$ , it is found that, for $r = 1 , 2 , \ldots$

$$
( \lambda _ { s } - \lambda _ { r } ) ^ { r } Y _ { s t } = \underset { j = 0 } { \overset { r } { \sum } } ( - 1 ) ^ { j } \binom { r } { j } N _ { k _ { s } } ^ { j } Y _ { s t } N _ { k _ { t } } ^ { r - j } ,\tag{4}
$$

where it is assumed that $N _ { k _ { s } } ^ { 0 } = I _ { k _ { s } } , N _ { k _ { t } } ^ { 0 } = I _ { k _ { t } }$

Now recall that the matrices $N _ { k _ { s } }$ are nilpotent and therefore $N _ { k _ { s } } ^ { m } = O$ for sufficiently large m. Hence if r in Eq. (4) is large enough, then $( \lambda _ { s } - \bar { \lambda _ { t } } ) ^ { r } Y _ { s t } = O$ and the assumption $\lambda _ { s } \neq \lambda _ { t }$ yields $Y _ { s t } = 0 .$

Case (2) $\lambda _ { s } = \lambda _ { t }$ . In this case Eq. (3) becomes

$$
Y _ { s t } N _ { k _ { s } } = N _ { k _ { t } } Y _ { s t } , \qquad 1 \leq s , t \leq p ,\tag{5}
$$

and if $Y _ { s t } = [ \gamma _ { i j } ] _ { i , j = 1 } ^ { k _ { s } , k _ { t } }$ , comparing the corresponding elements of the matrices on the right and left in Eq. (5), it is not difficult to see that

$$
\gamma _ { i + 1 , j } = \gamma _ { i , j - 1 } , \qquad i = 1 , 2 , \ldots , k _ { s } , \ : \ : j = 1 , 2 , \ldots , k _ { t } ,\tag{6}
$$

where it is supposed that $\gamma _ { i 0 } = \gamma _ { k _ { s } + 1 , j } = 0$

The equalities (6) show that the $k _ { s } \times k _ { t }$ matrix $Y _ { s t } \left( 1 \leq s , t \leq p \right)$ is in one of the following forms, depending on the relation between $k _ { s }$ and $k _ { t }$

(a) if $k _ { s } = k _ { t }$ , then $Y _ { s t }$ is an upper-triangular Toeplitz matrix;

(b) $\mathrm { i f } k _ { s } < k _ { t }$ , then $Y _ { s t } = [ 0 \mathrm { ~ } Y _ { k _ { s } } ]$

(c) if $k _ { s } > k _ { t }$ , then $Y _ { s t } = { \left[ \begin{array} { l } { Y _ { k _ { t } } } \\ { 0 } \end{array} \right] }$

in which $Y _ { k _ { s } }$ and $Y _ { k _ { t } }$ denote (square) upper-triangular Toeplitz matrices of orders $k _ { s }$ and $k _ { t } ,$ , respectively.

Thus, we may state the following.

Theorem 1. If $\ b { A } \in \mathbb { C } ^ { n \times n }$ and $A = P J P ^ { - 1 }$ , where J is a Jordan canonical form of A, then a matrix X commutes with A if and only if it is of the form $\overset { \cdot } { X } = \mathop { P Y P ^ { - 1 } }$ , where $Y = [ Y _ { s t } ] _ { s , t = 1 } ^ { p }$ is the partition of Y consistent with the partition of J into Jordan blocks, and where $Y _ { s t } = 0$ for $\lambda _ { s } \neq \lambda _ { t }$ and $Y _ { s t }$ is in one of the forms (a), (b), or (c) $i f \lambda _ { s } = \lambda _ { t }$

Exercise 1. Check that the set of matrices commuting with the matrix

$$
A = P { \left( \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 0 } & { 2 } \end{array} \right] \right)} + \left[ \begin{array} { l l l } { 2 } & { 1 } & { 0 } \\ { 0 } & { 2 } & { 1 } \\ { 0 } & { 0 } & { 2 } \end{array} \right] + { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] }  P ^ { - 1 }
$$

consists entirely of the matrices

$$
X = P ( [ \begin{array} { l l l l l } { \gamma _ { 0 } } & { \gamma _ { 1 } } & { \vdots } & { 0 } & { \alpha _ { 0 } } & { \alpha _ { 1 } } \\ { 0 } & { \gamma _ { 0 } } & { \vdots } & { 0 } & { 0 } & { \alpha _ { 0 } } \\ { . . . . . . . . . } & { . . . . . . . . . . . } & { . . . . } \\ { \beta _ { 0 } } & { \beta _ { 1 } } & { | \begin{array} { l l l l } { \delta _ { 0 } } & { \delta _ { 1 } } & { \delta _ { 1 } } & { \delta _ { 2 } } \\ { 0 } & { \beta _ { 0 } } & { | } & { 0 } & { \delta _ { 0 } } & { \delta _ { 1 } } \\ { 0 } & { 0 } & { | } & { 0 } & { 0 } & { \delta _ { 0 } } \end{array} | } & { + [ \begin{array} { l l } { \varepsilon _ { 0 } } & { \varepsilon _ { 1 } } \\ { 0 } & { \varepsilon _ { 0 } } \end{array} ] ) P ^ { - 1 } , } \end{array} 
$$

where the letters denote arbitrary complex numbers.

The number of arbitrary parameters in the general solution X of Eq. (1) is obviously greater than or equal to n.

Exercise 2. If αs denotes the degree of the greatest common divisor of the $\alpha _ { s t }$ elementary divisors $( \lambda - \lambda _ { s } ) ^ { k _ { s } }$ and $( \lambda - \lambda _ { t } ) ^ { k _ { t } } ( 1 \leq s , t \leq p )$ , prove that X in Eq. (1) has

$$
\alpha = \sum _ { s , t = 1 } ^ { p } \alpha _ { s t }\tag{7}
$$

undefined elements.

Hint. Observe that if $\lambda _ { s } = \lambda _ { t }$ , then $\alpha _ { s t } = \operatorname* { m i n } ( k _ { s } , k _ { t } )$ 口

Rephrasing the result of Exercise 2, the dimension of the linear space of solutions X of $A X = X .$ 4 is the number α given by Eq. (7). To see this, denote the α parameters of X by $\gamma _ { 1 } , \gamma _ { 2 } , \ldots , \gamma _ { \alpha }$ , and denote by $X _ { i }$ the solution of Eq. (1) obtained by putting $\gamma _ { i } = 1 , \gamma _ { i } = 0 ( j = 1 , 2 , \ldots , \alpha , j \ne i )$ . Clearly, the matrices $X _ { i } ( i = 1 , 2 , \ldots , \alpha )$ are linearly independent and any solution X of Eq. (1) can be written

$$
X = \sum _ { i = 1 } ^ { \alpha } \gamma _ { i } X _ { i } .\tag{8}
$$

Thus, $X _ { 1 } , X _ { 2 } , \ldots , X _ { \alpha }$ constitute a basis in the solution space of $A X = X A$

We have seen that, quite obviously, any polynomial $p ( A )$ in $A \in \mathbb { C } ^ { n \times n }$ commutes with $A ;$ ; we now ask about conditions on A such that, conversely each matrix commuting with A is a polynomial in A.

Proposition 1. Every matrix commuting with $A \in \mathbb { C } ^ { n \times n }$ is a polynomial in A if and only if no two Jordan blocks in the Jordan canonical form of A are associated with the same eigenvalue. $O r ,$ equivalently, the elementary divisors of A are pairwise relatively prime.

ProoF. First recall that in view of the Cayley-Hamilton theorem the number of linearly independent powers of A does not exceed n. Thus, if $A X = X A$ implies that X is a polynomial of A, then X can be rewritten as $X = p ( A )$ , where $l = \deg p ( \lambda ) \leq n$ and all powers $I , A , A ^ { 2 } , \ldots , A ^ { \prime - 1 }$ are linearly independent. Hence the dimension α of the solution set of Eq. (1) is in this case $\alpha = l \leq n$ . But Eq. (7) shows that $\alpha \geq n ,$ therefore ${ \mathfrak { X } } = n$ and the result follows from Eq. (7).

Conversely, if $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ are the distinct eigenvalues of A with indices $m _ { 1 } , m _ { 2 } , \ldots , m _ { s }$ , respectively, then the Jordan form J of A consists of exactly s blocks $J _ { i }$ . As we have seen, the solution X of $A X = X A$ is then similar to a direct sum of upper-triangular Toeplitz matrices:

$$
Y _ { i } = \left[ \begin{array} { c c c c } { \gamma _ { 0 } ^ { ( i ) } } & { \gamma _ { 1 } ^ { ( i ) } } & { \cdot \cdot \cdot } & { \gamma _ { m _ { i } - 1 } ^ { ( i ) } } \\ & { \gamma _ { 0 } ^ { ( i ) } } & { \cdot \cdot } & { \vdots } \\ & & { \cdot \cdot } & { \gamma _ { 1 } ^ { ( i ) } } \\ & & & { \gamma _ { 0 } ^ { ( i ) } } \end{array} \right] ,
$$

for $i = 1 , 2 , \ldots , s .$ In view of Eq. (9.2.4) it is clear that a polynomial $p ( \lambda )$ satisfying the conditions

$$
p ( \lambda _ { i } ) = \gamma _ { 0 } ^ { ( i ) } , \qquad \frac { 1 } { 1 ! } p ^ { \prime } ( \lambda _ { i } ) = \gamma _ { 1 } ^ { ( i ) } , \ldots , \frac { 1 } { ( m _ { i } - 1 ) ! } p ^ { ( m _ { i } - 1 ) } ( \lambda _ { i } ) = \gamma _ { m _ { i } - 1 } ^ { ( i ) } ,
$$

$i = 1 , 2 , \dots , s ,$ gives the required result :

$$
\begin{array} { r l } & { X = P \mathrm { d i a g } [ Y _ { 1 } , Y _ { 2 } , \dotsc , Y _ { s } ] P ^ { - 1 } } \\ & { \quad = P \mathrm { d i a g } [ p ( J _ { 1 } ) , \dotsc , p ( J _ { s } ) ] P ^ { - 1 } } \\ & { \quad = P p ( J ) P ^ { - 1 } = p ( P J P ^ { - 1 } ) = p ( A ) . } \end{array}
$$

Note that $p ( \lambda )$ can be chosen with degree not exceeding n – 1. ■

We now confine our attention to matrices commuting with a simple matrix. First, observe that Theorem 1 implies the result of Exercise 3.

Exercise 3. If A is simple and $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ are the distinct eigenvalues of $A ,$ show that the linear space of solutions of $A X = X A$ has dimension $\beta _ { 1 } ^ { 2 } + \beta _ { 2 } ^ { 2 } + \cdots + \beta _ { s } ^ { 2 }$ , where $\beta _ { i } ( 1 \leq i \leq s )$ is the algebraic multiplicity of $\lambda _ { i }$

Exercise 4. Show that if $A \in \mathbb { C } ^ { n \times n }$ has all its eigenvalues distinct, then every matrix that commutes with A is simple. □

$$
\lim \limits _ { n  \infty } \int \limits _ { 0 } ^ { 1 } d x + e ^ { n \beta } = \int \limits _ { 0 } ^ { 1 } \int \limits _ { 0 } ^ { 1 } \int \limits _ { 0 } ^ { 1 } \int e ^ { n }
$$

Proposition 2. Simple matrices A, $\pmb { X } \in \mathbb { C } ^ { n \times n }$ commute if and only if they have a set of n linearly independent eigenvectors in common.

In other words, if A and X are simple and $A X = X A .$ , then there exists a basis in $\mathbb { C } ^ { n }$ consisting entirely of common eigenvectors of A and X.

PROOF. Let $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ be the distinct eigenvalues of A with indices $m _ { 1 } , m _ { 2 } , \ldots , m _ { s } .$ , respectively, and let $A = P J P ^ { - 1 }$ , where the diagonal matrix J is a Jordan canonical form of A. By Theorem 1, the general form of matrices commuting with A is

$$
X = P Y P ^ { - 1 } = P \mathrm { d i a g } [ Y _ { 1 } , Y _ { 2 } , . . . , Y _ { s } ] P ^ { - 1 }
$$

where $Y _ { j } \in \mathbb { C } ^ { m _ { j } \times m _ { j } } , j = 1 , 2 , \ldots , s$ Reducing each $Y _ { j }$ to a Jordan canonical form, $Y _ { j } ^ { ' } = Q _ { j } J _ { j } Q _ { j } ^ { - 1 }$ , we obtain

$$
X = ( P Q ) \mathrm { d i a g } [ J _ { 1 } , J _ { 2 } , . . . , J _ { s } ] ( P Q ) ^ { - 1 } ,
$$

where $Q = \mathrm { d i a g } [ Q _ { 1 } , Q _ { 2 } , \dots , Q _ { s } ] .$

Since X is simple so is diag[ $\cdot J _ { 1 } , J _ { 2 } , \ldots , J _ { s } ]$ , and therefore the columns of PQ give n linearly independent eigenvectors of X. The same is true for A, because

$$
( P Q ) J ( P Q ) ^ { - 1 } = { \cal P } \mathrm { d i a g } [ \lambda _ { 1 } Q _ { 1 } Q _ { 1 } ^ { - 1 } , \ldots , \lambda _ { s } Q _ { s } Q _ { s } ^ { - 1 } ] P ^ { - 1 } = { \cal P } J P ^ { - 1 } = A .
$$

Conversely, if A and X have a set of n linearly independent eigenvectors in common, then A and X are obviously simple, and the eigenvectors determine a matrix P for which $A = P D _ { 1 } P ^ { - 1 } , X = ^ { \bullet } P D _ { 2 } P ^ { - 1 }$ , and $D _ { 1 } , D _ { 2 }$ are diagonal matrices. Then A and X commute, for

$$
A X = P D _ { 1 } D _ { 2 } P ^ { - 1 } = P D _ { 2 } D _ { 1 } P ^ { - 1 } = X A . \quad =
$$

Exercise 5. If A is a normal matrix with all its eigenvalues distinct, prove that every matrix that commutes with A is normal.

Exercise 6. Prove that normal matrices commute if and only if they have a common set of orthonormal eigenvectors.

Exercise 7. If A is a simple matrix with s distinct eigenvalues, prove that every matrix that commutes with A has at least s linearly independent eigenvectors in common with A.

## 12.5 Solutions of AX + XB = C

In the previous section we described the form of solutions of the equation $A X = X A$ Now observe that a matrix $\pmb { X } \in \mathbb { C } ^ { m \times n }$ is a solution of the equation $A X + X B = 0$ where $A \in \mathbb { C } ^ { m \times m } , \ B \in \mathbb { C } ^ { n \times n } ,$ , if and only if the $( m + n ) \times$ (m + n) matrices

$$
\begin{array}{c} \begin{array}{c} { \begin{array} { r l } { { \boldsymbol { \left[ { I _ { m } } & { X } \\ { 0 } & { I _ { n } } \end{array} \right]}  } , \qquad { \boldsymbol { \left[ { A } & { 0 } \\ { 0 } & { - B } \end{array} \right]}  } } \end{array} }\tag{1}
$$

commute. Thus, applying Theorem 12.4.1 to these two matrices, the next result readily follows

Theorem 1. Let $A \in \mathbb { C } ^ { m \times m } , B \in \mathbb { C } ^ { n \times n }$ and let $A = P J _ { 1 } P ^ { - 1 } , B = Q J _ { 2 } Q ^ { - 1 }$ where

$$
J _ { 1 } = \mathrm { d i a g } [ \lambda _ { 1 } I _ { k _ { 1 } } + N _ { k _ { 1 } } , \ldots , \lambda _ { p } I _ { k _ { p } } + N _ { k _ { p } } ]
$$

and

$$
J _ { 2 } = \mathrm { d i a g } [ \mu _ { 1 } I _ { r _ { 1 } } + N _ { r _ { 1 } } , \ldots , \mu _ { q } I _ { r _ { q } } + N _ { r _ { q } } ]
$$

are Jordan canonical forms of A and B, respectively. Then any solution X of

$$
A X + X B = 0\tag{2}
$$

is of the form $X = P Y Q ^ { - 1 }$ , where $Y = [ Y _ { s t } ] _ { s , t } ^ { p , q } = 1$ is the general solution of $J _ { 1 } Y + Y J _ { 2 } = 0 .$ with $Y _ { s t } \in \mathbb { C } ^ { k _ { s } \times r _ { t } } , s = 1 , 2 , \ldots , p , t = 1 , 2 , \ldots , q .$ Therefore Y has the properties $Y _ { s t } = 0 \ i f \ \lambda _ { s } \neq - \mu _ { t }$ , and $Y _ { s t }$ is a matrix of the form described in Theorem 12.4.1 for $\lambda _ { s } = - \mu _ { t }$

The argument used in Section 12.4 can also be exploited here.

Corollary 1. The general form of solutions of Eq. (2) is given by the formula

$$
X = \sum _ { i = 1 } ^ { \alpha } \gamma _ { i } X _ { i } ,\tag{3}
$$

where $X _ { 1 } , X _ { 2 } , \ldots , X _ { \alpha }$ are linearly independent solutions of Eq. (2) and

$$
\alpha = \sum _ { s = 1 } ^ { p } \ \sum _ { t = 1 } ^ { q } \alpha _ { s t } ,\tag{4}
$$

where $\alpha _ { s t } ( 1 \leq s \leq p , 1 \leq t \leq q )$ is the degree of the greatest common divisor of the elementary divisors $( \lambda - \lambda _ { s } ) ^ { k _ { s } }$ and $( \lambda + \mu _ { t } ) ^ { r _ { t } }$ of A and B, respectively.

Note that the number α in Eq. (4) is equal to dim(Ker G), where $G = I _ { n } \otimes$ $A + B ^ { \boldsymbol { \mathsf { T } } } \otimes I _ { m }$

The next exercise indicates a second approach to equation (2) based on the observation that Im X is A-invariant.

Exercise 1. Show that the equation $A X = X B$ has a solution X of rank r if and only if A and B have r eigenvalues in common with corresponding partial multiplicities in A and B.

OUTLINE OF SOLUTION. Observe first that Im X is A-invariant. Then use Ex. 6.5.3 to show that X has a factorization $X = E X _ { 0 }$ where E is m $\times \ r , \ X _ { 0 }$ is $r \times n ,$ both have full rank, and the columns of E are made up of Jordan chains of A. Thus $A E = E J$ and J is an $r \times r$ matrix in Jordan normal form. Then show that $X _ { 0 } B = J X _ { 0 }$ , and conclude that the eigenvalues of J (and their partial multiplicities) are common to both A and B.

Conversely, define E and $X _ { 0 }$ of full rank so that

$$
A E = E J , \qquad X _ { 0 } B = J X _ { 0 } ,
$$

and show that $X = E X _ { 0 }$ satisfies $A X = X B . \quad \sqcup$

Proceeding to the general equation

$$
A X + X B = C ,\tag{5}
$$

where $A \in \mathbb { C } ^ { m \times m } , B \in \mathbb { C } ^ { n \times n } , X , C \in \mathbb { C } ^ { m \times n }$ , it is easily seen, after rewriting this as a system of mn linear (scalar) equations, that Eq. (2) (also rewritten as such a system) is the corresponding homogeneous equation. Thus we can combine the results of Section 3.10 with the foregoing discussion.

Theorem 2. If Eq. (5) is solvable, then either it has a unique solution (when $\sigma ( A ) \cap \sigma ( - B ) = \emptyset )$ or it has infinitely many solutions given by the formula

$$
X = X _ { 0 } + \tilde { X } ,
$$

where $X _ { 0 }$ is a fixed particular solution of Eq. (5) and ${ \tilde { X } } ,$ being the general solution of the homogeneous equation, Eq. (2), is of the form (3).

Thus, to complete an investigation of Eq. (5), it remains to obtain a criterion for its solvability in terms of the matrices A, B, and C. This criterion is due to W. E. Roth† and the proof presented here is that of H. Flanders and H. K. Wimmer.

Theorem 3. Equation (5) has a solution if and only if the matrices

$$
{ \begin{array} { r l } { \left[ A \quad \quad 0 \right] \quad } & { { \mathrm { } a n d } \quad } \\ { \left[ 0 \quad - B \right] \quad } & { { \mathrm { } a n d } \quad } \end{array} } \quad { \begin{array} { r l } { \left[ A \quad c \right] } \\ { \left[ 0 \quad - B \right] } \end{array} }\tag{6}
$$

are similar.

ProoF. If Eq. (5) has a solution $X ,$ it is easily checked that the matrices in (6) are similar, with the transforming matrix

$$
{ \left[ \begin{array} { l l } { I } & { X } \\ { 0 } & { I } \end{array} \right] } .
$$

Conversely, let

$$
{ \left[ \begin{array} { l l } { A } & { \quad 0 } \\ { 0 } & { - B } \end{array} \right] } = P ^ { - 1 } { \left[ \begin{array} { l l } { A } & { \quad C } \\ { 0 } & { - B } \end{array} \right] } P\tag{7}
$$

for some nonsingular matrix $P \in \mathbb { C } ^ { ( m + n ) \times ( m + n ) }$ . Define linear transformations $T _ { 1 } , T _ { 2 } \in \mathcal { L } ( \mathbb { C } ^ { ( m + n ) \times ( m + n ) } )$ by the rule

$$
T _ { 1 } ( Z ) = \left[ \begin{array} { c c } { { A } } & { { 0 } } \\ { { 0 } } & { { - B } } \end{array} \right] Z - Z \biggl [ \begin{array} { c c } { { A } } & { { 0 } } \\ { { 0 } } & { { - B } } \end{array} \biggr ] ,
$$

$$
T _ { 2 } ( Z ) = \left[ \begin{array} { c c } { { A } } & { { C } } \\ { { 0 } } & { { - B } } \end{array} \right] Z - Z \biggl [ \begin{array} { c c } { { A } } & { { 0 } } \\ { { 0 } } & { { - B } } \end{array} \biggr ] ,
$$

where $Z \in \mathbb { C } ^ { ( m + n ) \times ( m + n ) }$ , and observe that it suffices to find a matrix in Ker $T _ { 2 }$ of the form

$$
{ \begin{array} { r } { { \left[ { R \atop 0 } \right. } ^ { U } } \\ { \left. { \begin{array} { r l } { 0 } & { - I } \end{array} } \right] } \end{array} } .\tag{8}
$$

Indeed, in this case a straightforward calculation shows that the matrix U in (8) is a solution of (5).

Eq. (7) implies that

$$
T _ { 1 } ( Z ) = P ^ { - 1 } T _ { 2 } ( P Z ) ,
$$

and hence

$$
\operatorname { K e r } T _ { 2 } = \{ P Z : Z \in \mathbb { C } ^ { ( m + n ) \times ( m + n ) } \quad { \mathrm { a n d } } \quad Z \in \operatorname { K e r } T _ { 1 } \} .
$$

Consequently,

$$
\dim ( \mathrm { K e r } \ T _ { 1 } ) = \dim ( \mathrm { K e r } \ T _ { 2 } ) .\tag{9}
$$

Let us consider the set $\mathcal { S }$ consisting of all pairs $( V , W )$ , where $V \in \mathbb { C } ^ { n \times m }$ $\ b { W } \in \mathbb { C } ^ { n \times n }$ , and such that $B V + V A = 0$ and $B W = W B$ Then $\mathcal { S }$ is a linear space with respect to the natural operations

$$
\begin{array} { r } { \alpha ( V , W ) = ( \alpha V , \alpha W ) , \qquad \alpha \in \mathbb { C } , } \\ { ( V _ { 1 } , W _ { 1 } ) + ( V _ { 2 } , W _ { 2 } ) = ( V _ { 1 } + V _ { 2 } , W _ { 1 } + W _ { 2 } ) . } \end{array}
$$

Define the transformations $\varphi _ { i } \in { \mathcal { L } } ( \mathbb { K } \operatorname { e r } T _ { i } , { \mathcal { S } } ) , i = 1 , 2$ , by the formula

$$
\varphi _ { i } \left( { \left[ \begin{array} { l l } { R } & { U } \\ { V } & { W } \end{array} \right] } \right) = ( V , W )
$$

and observe that

$$
\mathrm { K e r } \varphi _ { 1 } = \mathrm { K e r } \varphi _ { 2 } = \left\{ \left[ { \cal R } { \cal U } \right] : { \cal A } { \cal R } = { \cal R } { \cal A } , { \cal A } { \cal U } + { \cal U } { \cal B } = 0 \right\} .\tag{10}
$$

Furthermore, Im $\varphi _ { 1 } = { \mathcal { S } } .$ This is because $( V , W ) \in \mathcal { S }$ implies $B V + V A = 0$ and $B W = W B .$ Hence

$$
\begin{array} { r } { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { V } & { W } \end{array} \right] \in  { \mathbf { K e r } } \ T _ { 1 } , \qquad \mathrm { a n d } \qquad \varphi _ { 1 } \biggl ( \ b { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { V } & { W } \end{array} \right] } \biggr ) = ( V , W ) . } \end{array}
$$

Thus, $\mathcal { S } \subset \mathrm { I m } \ \varphi _ { 1 }$ . Since the reverse inclusion is obvious, Im $\varphi _ { 1 } = { \mathcal { S } } .$ Now we have Im $\varphi _ { 2 } \subset \mathcal { S } = \mathrm { I m } \varphi _ { 1 }$ . But, on the other hand (see Eq. (4.5.2)),

$$
\dim ( \mathrm { K e r } \ \varphi _ { i } ) + \dim ( \mathrm { I m } \ \varphi _ { i } ) = \dim ( \mathrm { K e r } \ T _ { i } ) , \qquad i = 1 , 2 ,
$$

and therefore Eqs. (9) and (10) imply that dim(Im $\varphi _ { 1 } ) = \dim ( \operatorname { I m } \varphi _ { 2 } )$ and, consequently, that

$$
\mathbf { I m } \varphi _ { 1 } = \mathbf { I m } \varphi _ { 2 } = \mathcal { S } .\tag{11}
$$

Now observe that

$$
\begin{array} { r } { \left[ \begin{array} { c c } { I } & { 0 } \\ { 0 } & { - I } \end{array} \right] \in \mathrm { K e r } \ T _ { 1 } \qquad \mathrm { a n d } \qquad \varphi _ { 1 } \left( \left[ \begin{array} { c c } { I } & { 0 } \\ { 0 } & { - I } \end{array} \right] \right) = ( 0 , - I ) . } \end{array}
$$

Thus, in view of Eq. (11), there is a matrix

$$
{ \left[ \begin{array} { l l } { R _ { 0 } } & { U _ { 0 } } \\ { V _ { 0 } } & { W _ { 0 } } \end{array} \right] } \in \mathbf { K e r } \ T _ { 2 }
$$

such that

$$
( 0 , - I ) = \varphi _ { 2 } \biggl ( \left[ { \begin{array} { c c } { R _ { 0 } } & { U _ { 0 } } \\ { V _ { 0 } } & { W _ { 0 } } \end{array} } \right] \biggr ) .
$$

This means that $V _ { \mathbf { 0 } } = 0$ and $W _ { 0 } = - I .$ Thus we have found a matrix in Ker $T _ { 2 }$ of the desired form (8). This completes the proof.■

## 12.6 One-Sided Inverses

In this and the following sections we shall introduce some generalizations of the inverse matrix. These generalized inverses retain some of the important properties of the inverse but are defined not only for nonsingular (square) matrices but for singular square and rectangular matrices, as well. We devote this section to a study of the notion of one-sided invertibility of matrices, but first recall the corresponding ideas for linear transformations studied in Section 4.6.

A matrix $A \in \mathcal { F } ^ { m \times n }$ is said to be left (respectively, right) invertible if there exists a matrix $A _ { \mathbf { L } } ^ { - 1 }$ (respectively, $A _ { \tt R } ^ { - 1 } )$ from $\mathcal { F } ^ { n \times m }$ such that

$$
A _ { \bf L } ^ { - 1 } A = I _ { n } \qquad \mathrm { ( r e s p e c t i v e l y , } \quad A A _ { \bf R } ^ { - 1 } = I _ { m } \mathrm { ) . }\tag{1}
$$

A matrix $A _ { \mathbf { L } } ^ { - 1 }$ (respectively, $A _ { \mathbb { R } } ^ { - 1 } )$ satisfying Eq. (1) is called a left (respectively, $r i g h t )$ inverse of A. Clearly, if $m = n$ and A is nonsingular, then the one-sided inverses of A coincide with the regular inverse $A ^ { - 1 }$

The first results are obtained directly from Theorems 4.6.1 and 4.6.2 on interpreting members of ${ \mathcal { F } } ^ { m \times n }$ as linear transformations from $\mathbb { C } ^ { n }$ to $\mathbb { C } ^ { m }$

Theorem 1. The following statements are equivalent for any matrix $\pmb { A } \in \mathcal { F } ^ { m \times n }$

(a) the matrix A is left invertible;

(b) $m \geq n$ and rank $A = n$

(c) The columns of A are linearly independent as members of ${ \mathcal { F } } ^ { m }$

(d) Ker $A = \{ \pmb { \theta } \}$

Theorem 2. The following statements are equivalent for any matrix $\pmb { A } \in \mathcal { F } ^ { m \times n }$

(a) the matrix A is right invertible;

(b) $m \leq n$ and rank $A = m ;$

(c) The rows of A are linearly independent as members of ${ \mathcal { F } } ^ { n }$

(d) Im $A = { \mathcal { F } } ^ { m } .$

Thus, m × n matrices of full rank (see Section 3.8) and only they are one-sided invertible. They are invertible from the left if $m \geq n$ and from the right if $m \leq n$ In the case $m = n \textbf { a }$ matrix of full rank is (both-sided) invertible.

Exercise 1. Let

$$
A = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { - 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] } , \qquad B = { \left[ \begin{array} { l l } { 1 } & { - 2 } \\ { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] } .
$$

Verify that $B = A _ { \mathbf { R } } ^ { - 1 }$ and that $A = B _ { \mathrm { L } } ^ { - 1 }$ . Find other right inverses of A and left inverses of B. □

Let $A \in \mathcal { F } ^ { m \times n } , m \geq n .$ and rank $A = n$ Then A is left invertible (Theorem 1) and hence the equation

$$
X A = I _ { n }\tag{2}
$$

is solvable. To describe all solutions of Eq. (2), that is, the set of all left inverses of A, we first apply a permutation matrix $P \in \mathcal { F } ^ { m \times m }$ such that the $n \times n$ nonsingular submatrix $A _ { 1 }$ in $P A$ occupies the top n rows, that is,

$$
P A = \binom { A _ { 1 } } { A _ { 2 } } , \qquad A _ { 1 } \in \mathcal { F } ^ { n \times n } , \quad \operatorname* { d e t } A _ { 1 } \not = 0 .
$$

It is easily verified that matrices of the form

$$
[ A _ { 1 } ^ { - 1 } - B A _ { 2 } A _ { 1 } ^ { - 1 } B ] P\tag{3}
$$

for any $B \in \mathcal { F } ^ { n \times ( m - n ) }$ satisfy Eq. (2), that is, are left inverses of A. Conversely, if $A _ { \mathrm { L } } ^ { - 1 }$ is a left inverse of A, then, representing $A _ { \mathrm { L } } ^ { - 1 } = [ C B ] P _ { \mathrm { : } }$ where $C \in \mathcal { F } ^ { n \times n } , B \in \mathcal { F } ^ { n \times ( m - n ) }$ , and substituting it in Eq. (2), we obtain $C A _ { 1 } + B A _ { 2 }$ $= I _ { n }$ . Hence $C = A _ { 1 } ^ { - 1 } - B A _ { 2 } A _ { 1 } ^ { - 1 }$ and the following result is proved.

Theorem 3. If $A \in \mathcal { F } ^ { m \times n }$ is left invertible, then all left inverses of A are given by formula (3), where B is an arbitrary $n \times ( m - n )$ matrix.

A similar result is easily proved for right inverses.

Theorem 4. Let $A \in \mathcal { F } ^ { m \times n }$ be right invertible. Then all right inverses of A are given by the formula

$$
A _ { \tt R } ^ { - 1 } = \ Q { \left[ \begin{array} { l l } { A _ { 3 } ^ { - 1 } - A _ { 3 } ^ { - 1 } A _ { 4 } C } \\ { \qquad \quad } C \right]} \end{array}   ,\tag{4}
$$

for any $( n - m ) \times$ m matrix C. Here $Q \in \mathcal { F } ^ { n \times n }$ is a permutation matrix such that $A Q = [ A _ { 3 } \quad A _ { 4 } ]$ and the m × m matrix $A _ { 3 }$ is nonsingular.

It should also be noted that the matrices $A A _ { \mathrm { L } } ^ { - 1 }$ and $A _ { \tt R } ^ { - 1 } A$ are idempotents:

$$
( A A _ { \mathrm { L } } ^ { - 1 } ) ( A A _ { \mathrm { L } } ^ { - 1 } ) = A ( A _ { \mathrm { L } } ^ { - 1 } A ) A _ { \mathrm { L } } ^ { - 1 } = A A _ { \mathrm { L } } ^ { - 1 } .
$$

Similarly, ${ A } _ { \tt R } ^ { - 1 } A$ is also idempotent.

Exercise 2. If A is left invertible, prove that

(a) $A A _ { \mathrm { L } } ^ { - 1 }$ is a projector onto Im A;

(b) dim(Ker $A _ { \mathrm { L } } ^ { - 1 } ) = m - \mathrm { d i m } ( \mathrm { I m } \ { \cal A } ) .$

Exercise 3. If A is right invertible, prove that

(a) $I - A _ { \mathbb { R } } ^ { - 1 } A$ is a projector onto Ker A;

(b) $\operatorname { l i m } ( \operatorname { I m } A _ { \mathrm { R } } ^ { - 1 } ) = n - \dim ( \operatorname { K e r } A ) . \quad \bigsqcup$

We now consider the equation

$$
A x = b , \qquad A \in { \mathcal { F } } ^ { m \times n } , \quad x \in { \mathcal { F } } ^ { n } , \quad b \in { \mathcal { F } } ^ { m } ,\tag{5}
$$

with a one-sided invertible matrix A.

Theorem 5. If A is left invertible, then the equation $A { \pmb x } = { \pmb b }$ is solvable if and only if

$$
( I _ { m } - A A _ { \mathrm { L } } ^ { - 1 } ) \pmb { b } = \pmb { 0 } .\tag{6}
$$

Furthermore, if Eq. (6) holds, then the solution of $E q . \ ( 5 )$ is unique and is given by the formula

$$
\begin{array} { r } { \pmb { x } = A _ { \mathbf { L } } ^ { - 1 } \pmb { b } . } \end{array}
$$

PRooF. Let x be a solution of Eq. (5). Then the multiplication of Eq. (5) by $A A _ { \mathrm { L } } ^ { - 1 }$ from the left gives

$$
A A _ { \mathrm { L } } ^ { - 1 } b = A ( A _ { \mathrm { L } } ^ { - 1 } A ) x = A x = b ,
$$

and the condition (6) follows. Conversely, if Eq. (6) holds, then the vector $\begin{array} { r } { \pmb { x } = A _ { \mathbf { L } } ^ { - 1 } \pmb { b } } \end{array}$ is a solution of Eq. (5). If $\mathbf { x _ { 1 } }$ is another solution of (5), then $A ( { \pmb x } - { \pmb x } _ { 1 } ) = { \pmb 0 }$ and the assertion (d) of Theorem 1 yields the required result, $\mathbf { x } = { \mathbf { x } } _ { 1 }$

Theorem 6. If A is right invertible, then Eq. (5) is solvable for any $\ b { b } \in \mathcal { F } ^ { m }$ and if $\qquad \neq \theta ,$ every solution x is of the form

$$
\begin{array} { r } { \pmb { x } = A _ { \mathbb { R } } ^ { - 1 } \pmb { b } , } \end{array}\tag{7}
$$

for some right inverse $A _ { \mathbb { R } } ^ { - 1 }$ of A.

ProoF. The solvability of Eq. (5) for any vector $\pmb { b } \in \mathcal { F } ^ { m }$ is obvious since $A ( A _ { \mathbb { R } } ^ { - 1 } \pmb { b } ) = \pmb { b } ,$ and x in Eq. (7) is a solution of Eq. (5). Suppose now that x is a solution of Eq. (5). Decompose A as in Theorem 4: $A = [ \bar { A } _ { 3 } \quad A _ { 4 } ] Q ^ { \bar { \bf T } }$ , where det $A _ { 3 } \neq 0$ and Q is a permutation matrix. Perform a consistent decomposition of $\begin{array} { r } { { \pmb x } \colon { \pmb x } = Q [ { \pmb x } _ { 1 } ^ { \sf T } \quad { \pmb x } _ { 2 } ^ { \sf T } ] ^ { \sf T } } \end{array}$ . Then Eq. (5) can be rewritten $A _ { 3 } x _ { 1 } + A _ { 4 } x _ { 2 } = b ,$ hence $x _ { 1 } = A _ { 3 } ^ { - 1 } b - A _ { 3 } ^ { - 1 } A _ { 4 } x _ { 2 }$ . Now compute $A _ { \mathbb { R } } ^ { - 1 } b$ using Eq. (4) and use the fact that (since $b \neq \pmb { \mathbb { \mathbb { 0 } } } )$ a matrix $C \in \mathcal { F } ^ { ( n - m ) \times m }$ exists such that $C b = x _ { 2 }$

$$
\begin{array} { r } { A _ { \mathrm { R } } ^ { - 1 } \pmb { b } = Q \bigg [ \frac { A _ { \mathrm { 3 } } ^ { - 1 } \pmb { b } - A _ { \mathrm { 3 } } ^ { - 1 } A _ { \mathrm { 4 } } C \pmb { b } } { C \pmb { b } } \bigg ] = Q \bigg [ \pmb { x } _ { 1 } \bigg ] = \pmb { x } , } \end{array}
$$

and the assertion follows.

Theorems 5 and 6 are easily included in a single more general statement that will also serve to introduce an idea developed in the next section. Comparison should also be made with Theorem 3.10.2. Let $A \in \mathcal { F } ^ { m \times n }$ , and let $\pmb { X } \in \mathcal { F } ^ { n \pmb { \times } m }$ be any matrix for which

$$
A X A = A .\tag{8}
$$

If A is left (or right) invertible, we may choose for X a left (or right) inverse of A, of course, but as we shall see in the next section, such matrices X exist even if X has no one-sided inverse.

Theorem 7. Let $A \in \mathcal { F } ^ { m \times n } , b \in \mathcal { F } ^ { m }$ , and let X be a solution of $E q . ( 8 )$ . Then the equation $A { \boldsymbol { \mathbf { x } } } = \mathbf { \boldsymbol { \ b } }$ has a solution if and only if $A X b = b ;$ and then any solution has the form

$$
{ \pmb x } = { \pmb X } { \pmb b } + ( { \pmb I } - { \pmb X } { \pmb A } ) { \pmb y } ,
$$

for some $\boldsymbol { y } \in \mathcal { F } ^ { n } ,$

Exercise 4. With the assumptions of Theorem 7, prove that $\pmb { A } \pmb { x } = \pmb { 0 }$ has the general solution ${ \pmb x } = ( J - X A ) { \pmb y }$ for any $y \in \mathcal { F } ^ { n }$ . In other words, if x satisfies (8) then $I _ { m } ( I - X A ) = \operatorname { K e r } A$ . Then prove Theorem 7. □

## 12.7 Generalized Inverses

In the preceding section we introduced the notion of a one-sided inverse for $A \in \mathcal { F } ^ { m \times n }$ , and we showed that such an inverse exists if and only if the matrix A is of full rank. Our purpose is now to define a generalization of the concept of a one-sided inverse that will apply to any m × n matrix A. To this end, we first observe that a one-sided inverse X of A (if it exists) satisfies the equations

$$
A X A = A ,\tag{1}
$$

$$
X A X = X .\tag{2}
$$

Therefore we define a generalized inverse of $A \in \mathcal { F } ^ { m \times n }$ to be a matrix $\pmb { X } \in \mathcal { F } ^ { n \pmb { \times } m }$ for which Eq. (1) and (2) hold, and we write $X = A ^ { I }$ for such a matrix.

Proposition 1. A generalized inverse $A ^ { \parallel }$ exists for any matrix $A \in \mathcal { F } ^ { m \times n }$

ProoF. Observe first that the m × n zero matrix has the n × m zero matrix as its generalized inverse. Then let $r \neq 0$ be the rank of A. Then (see Section 2.7)

$$
A = R { \binom { I _ { r } } { 0 } } V ,\tag{3}
$$

for some nonsingular matrices $R \in \mathcal { F } ^ { m \times m } , V \in \mathcal { F } ^ { n \times n }$ It is easily checked that matrices of the form

$$
A ^ { \mathrm { I } } = V ^ { - 1 } { \binom { I _ { r } } { B _ { 2 } } } B _ { 1 } \biggr ] { R ^ { - 1 } } ,\tag{4}
$$

for any $B _ { 1 } \in \mathcal { F } ^ { r \times ( n - r ) } , B _ { 2 } \in \mathcal { F } ^ { ( m - r ) \times r }$ , satisfy the conditions (1) and (2).■

Thus, a generalized inverse always exists and is, generally, not unique. Bearing in mind the decomposition (3), it is easy to deduce the following criterion for uniqueness of the generalized inverse.

Exercise 1. Prove that the generalized inverse of A is unique if and only if $A = 0$ or A is a square and nonsingular matrix.

The following properties of generalized inverses follow readily from the defining relations (1) and (2).

Proposition 2. If $A \in { \mathcal { F } } ^ { m \times n }$ and $A ^ { \boldsymbol { \mathsf { I } } }$ denotes one of its generalized inverses, then

(a) $A ^ { 1 } A$ and $A A ^ { \boldsymbol { \mathsf { I } } }$ are idempotent matrices.

(b) rank A¹ = rank A.

(c) the matrix $( A ^ { 1 } ) ^ { * }$ is one of the generalized inverses of $A ^ { * } .$

ProoF. Parts (a) and (c) follow immediately from the defining properties (1) and (2) as applied to $A ^ { 1 } .$ Part (b) follows on applying the result of Exercise 3.8.5 to the same relations.■

If $A \in { \mathcal { F } } ^ { \mathfrak { n } \times n }$ is a nonsingular matrix, so is $A ^ { - 1 }$ and obviously

$$
\mathbf { I m } ~ A \ + ~ \mathbf { K e r } ~ A ^ { - 1 } = { \mathcal { F } } ^ { n } + \{ \pmb { \theta } \} = { \mathcal { F } } ^ { n } ,
$$

$$
\operatorname { K e r } A + \operatorname { I m } A ^ { - 1 } = \{ \pmb { \theta } \} + \mathcal { F } ^ { n } = \mathcal { F } ^ { n } .
$$

The next result generalizes these statements for an arbitrary matrix A and its generalized inverses.

Proposition 3. If $A \in \mathcal { F } ^ { m \times n }$ and $A ^ { \parallel }$ denotes one of the generalized inverses of A, then

$$
\operatorname { I m } A + \operatorname { K e r } A ^ { \operatorname { I } } = { \mathcal { F } } ^ { m }\tag{5}
$$

$$
\operatorname { K e r } A + \operatorname { I m } A ^ { \mathbf { I } } = { \mathcal { F } } ^ { n } .\tag{6}
$$

ProoF. It has been noted in Proposition $2 ( \mathsf { a } )$ that $A A ^ { \boldsymbol { \mathsf { I } } }$ is a projector and it is clear that Im $( A A ^ { \mathsf { I } } ) \subset \operatorname { I m } A$ .We show that, in fact, $A A ^ { \boldsymbol { \mathsf { I } } }$ projects onto Im A. If $\mathbf { y } = A \mathbf { x } \in \operatorname { I m } A$ , then since $A = A A ^ { 1 } A , \ y = ( A A ^ { 1 } ) ( A x ) \in \operatorname { I m } ( A A ^ { 1 } )$ So Im $A \subset \operatorname { I m } ( A A ^ { \operatorname { I } } )$ and hence $\operatorname { I m } ( A A ^ { \mathrm { I } } ) = \operatorname { I m } A$

It is deduced from this, and Proposition 2(b), that

$$
\operatorname { r a n k } A = \operatorname { r a n k } ( A A ^ { \mathrm { I } } ) = \operatorname { r a n k } A ^ { \mathrm { I } } ,
$$

and then that Ker $A ^ { \boldsymbol { \mathsf { I } } } = \mathbf { K e r } ( A A ^ { \boldsymbol { \mathsf { I } } } )$ . For Ker $A ^ { \mathsf { I } } \subset \mathsf { K e r } ( A A ^ { \iota } )$ , obviously. But also, by Theorem 4.5.5

$$
\dim ( \operatorname { K e r } A ^ { \operatorname { I } } ) = m - \operatorname { r a n k } A ^ { \operatorname { I } } = m - \operatorname { r a n k } ( A A ^ { \operatorname { I } } ) = \dim \operatorname { K e r } ( A A ^ { \operatorname { I } } ) .
$$

Consequently, Ker $A ^ { \boldsymbol { \mathsf { I } } } = \mathbf { K e r } ( A A ^ { \boldsymbol { \mathsf { I } } } )$

Finally, combining these results with the fact that $A A ^ { \mathbf { I } }$ is a projector it is found that

$$
\mathcal { F } ^ { m } = \mathrm { I m } ( A A ^ { \mathrm { I } } ) \dotplus \mathrm { K e r } ( A A ^ { \mathrm { I } } ) = \mathrm { I m } ~ A \dotplus \mathrm { K e r } ~ A ^ { \mathrm { I } } ,
$$

which is equation (5).

Since the defining equations for $A ^ { \boldsymbol { \mathsf { I } } }$ are symmetric in $A , A ^ { l }$ we can replace $A , A ^ { \mathfrak { I } }$ in (5) by $A ^ { \mathbb { I } } , A ,$ respectively, and obtain (6).■

Corollary 1. $I f A ^ { \mathbf { I } }$ is a generalized inverse of A, then $A A ^ { \boldsymbol { \mathsf { I } } }$ is a projector onto Im A along Ker $A ^ { \underline { { { t } } } } ,$ and $A ^ { \mathbf { I } } A$ is a projector onto Im $A ^ { \boldsymbol { \mathsf { I } } }$ along Ker A.

Note also the following property of the generalized inverse of A that follows immediately from the Corollary, and develops further the relationship with properties of the ordinary inverse.

Exercise 2. If $A \in \mathcal { F } ^ { m \times n }$ , prove that

$$
A ^ { l } A x = x \qquad \mathrm { a n d } \qquad A A ^ { \mathrm { I } } y = y
$$

for any $\pmb { x \in }$ Im $A ^ { \mathfrak { I } }$ and $y \in$ Im A. In other words, considered as linear transformations, A and $A ^ { \boldsymbol { \mathsf { I } } }$ are mutual inverses on the pairs of subspaces Im $A ^ { \mathbb { I } }$ and Im $A ,$ respectively.□

Proposition 3 shows that a generalized inverse for an $m \times n$ matrix determines a complementary subspace for Im A in ${ \mathcal { F } } ^ { m }$ and another complementary subspace for Ker A in ${ \mathcal { F } } ^ { n }$ . The next results shows that a converse statement also holds.

Proposition 4. Given a matrix $A \in \mathcal { F } ^ { m \times n }$ , let $\mathcal { S } _ { 1 } , \mathcal { S } _ { 2 }$ be subspaces of ${ \mathcal { F } } ^ { m }$ and ${ \mathcal { F } } ^ { n } .$ respectively, such that

$$
\operatorname { I m } A + { \mathcal { S } } _ { 1 } = { \mathcal { F } } ^ { m } \qquad a n d \qquad \operatorname { K e r } A + { \mathcal { S } } _ { 2 } = { \mathcal { F } } ^ { n } .\tag{7}
$$

Then there is a generalized inverse $A ^ { \boldsymbol { \mathsf { I } } }$ of A such that Ker $A ^ { \mathbf { I } } = { \mathcal { S } } _ { 1 }$ and Im $A ^ { \mathbf { I } } = \mathcal { S } _ { 2 }$

ProoF. Let A have rank r and write A in the form (3). It is easily seen that

$$
V ( \mathbf { K e r ~ } A ) = \mathbf { K e r } { \left[ \begin{array} { l l } { I _ { r } } & { O } \\ { O } & { O } \end{array} \right] } , \qquad R ^ { - 1 } ( \mathbf { I m ~ } A ) = \mathbf { I m } { \left[ \begin{array} { l l } { I _ { r } } & { O } \\ { O } & { O } \end{array} \right] }
$$

and then, using (7), that

$$
\begin{array} { r } { \mathrm { I m } \left[ \begin{array} { l l } { I _ { r } } & { \boldsymbol { 0 } } \\ { \boldsymbol { 0 } } & { \boldsymbol { 0 } } \end{array} \right] + R ^ { - 1 } ( \mathcal { S } _ { 1 } ) = \mathscr { F } ^ { m } , \qquad \mathrm { K e r } \left[ \begin{array} { l l } { I _ { r } } & { \boldsymbol { 0 } } \\ { \boldsymbol { 0 } } & { \boldsymbol { 0 } } \end{array} \right] + V ( \mathcal { S } _ { 2 } ) = \mathscr { F } ^ { n } . } \end{array}
$$

Consequently, for some $r \times ( m - r )$ matrix X and $( n - r ) \times r$ matrix Y,

$$
{ \mathcal { S } } _ { 1 } = R \operatorname { I m } { \left[ { \begin{array} { l } { X } \\ { I _ { m - r } } \end{array} } \right] } , \qquad { \mathcal { S } } _ { 2 } = V ^ { - 1 } \operatorname { I m } { \left[ { \begin{array} { l } { I _ { r } } \\ { Y } \end{array} } \right] } .
$$

Now define $A ^ { \mathfrak { I } }$ by

$$
\begin{array} { r } { A ^ { \mathbf { I } } = V ^ { - 1 } \biggl [ \begin{array} { l l } { I _ { r } } & { - X } \\ { Y } & { - Y X } \end{array} \biggr ] R ^ { - 1 } , } \end{array}
$$

and it is easily verified that $A ^ { \boldsymbol { \mathsf { I } } }$ is a generalized inverse of A with the required properties.■

This section is to be concluded with a result showing how any generalized inverse can be used to construct the orthogonal projector onto Im $A ;$ this should be compared with Corollary 1 above in which $A A ^ { \boldsymbol { \mathsf { I } } }$ is shown to be a projector onto Im $A ,$ but not necessarily an orthogonal projector, and also with a construction of Section 5.8. The following exercise will be useful in the proof. It concerns situations in which left, or right, cancellation of matrices is permissible.

Exercise 3. Prove that whenever the matrix products exist,

(a) $A ^ { * } A B = A ^ { * } A C$ implies $A B = A C$

(b) $B A ^ { * } A = C A ^ { * } A$ implies $B A ^ { * } = C A ^ { * } .$

Hint. Use Exercise 5.3.6 to establish part (a) and then obtain part (b) from (a). □

Proposition 5. If $A \in \mathcal { F } ^ { m \times n }$ and $( A ^ { * } A ) ^ { \mathbf { I } }$ is any generalized inverse of $A ^ { * } A$ then $P = A ( A ^ { * } A ) ^ { \mathbf { I } } A ^ { * }$ is the orthogonal projector of $\mathcal { F } ^ { m }$ onto Im A.

PRoOF. Equation (1) yields

$$
A ^ { * } A ( A ^ { * } A ) ^ { \mathrm { I } } A ^ { * } A = A ^ { * } A ,
$$

and the results of Exercise 3 above show that

$$
A ( A ^ { * } A ) ^ { \mathrm { I } } A ^ { * } A = A , \qquad A ^ { * } A ( A ^ { * } A ) ^ { \mathrm { I } } A ^ { * } = A ^ { * } .\tag{8}
$$

Using either equation it is seen immediately that $P ^ { 2 } = P .$

Using Proposition 2(c) one may write

$$
P ^ { * } = A ( ( A ^ { * } A ) ^ { \mathrm { I } } ) ^ { * } A ^ { * } = A ( A ^ { * } A ) ^ { J } A ^ { * } ,
$$

where $( A ^ { * } A ) ^ { J }$ is (possibly) another generalized inverse of $A ^ { * } A$ It can be shown that $P ^ { * } = P$ by proving $( P - P ^ { * } ) ( P - P ^ { * } ) ^ { * } = 0$ Write

$$
( P - P ^ { * } ) ( P - P ^ { * } ) ^ { * } = P P ^ { * } + P ^ { * } P - P ^ { 2 } - ( P ^ { * } ) ^ { 2 } ,
$$

and use equation (8) (for either inverse) to show that the sum on the right reduces to zero.

Obviously, P is a projector of ${ \mathcal { F } } ^ { m }$ into Im A. To show that the projection is onto Im $A ,$ let $y \in$ Im A. Then ${ \boldsymbol { y } } = A { \boldsymbol { x } }$ for some $\pmb { x } \in \mathcal { F } ^ { m }$ and, using the first equality in (8), we obtain

$$
\begin{array} { r } { \mathbf { y } = A ( A ^ { * } A ) ^ { \mathrm { I } } A ^ { * } ( A { \boldsymbol { x } } ) = P z , } \end{array}
$$

where $z = A x ,$ , and the result follows.

## 12.8 The Moore-Penrose Inverse

It has been shown in Propositions 12.7.3 and 12.7.4 that a generalized inverse of an $m \times n$ matrix determines and is determined by a pair of direct complements to Im A in ${ \mathcal { F } } ^ { m }$ and Ker A in ${ \mathcal { F } } ^ { n } .$ An important case arises when orthogonal complements are chosen. To ensure this, it suffices to require the projectors $A A ^ { 1 }$ and $A ^ { 1 } A$ to be Hermitian (see Section 5.8). Indeed, in this case $A A ^ { \boldsymbol { \mathsf { I } } }$ is an orthogonal projector onto Im A along Ker $A ^ { \mathbf { I } }$ (Corollary 12.7.1) and then

$$
\mathrm { I m } ~ { \cal A } \oplus \mathrm { K e r } ~ { \cal A } ^ { \mathrm { I } } = \mathcal { F } ^ { m } ,\tag{1}
$$

and similarly,

$$
\ker A \oplus \operatorname { I m } A ^ { \mathbf { I } } = { \mathcal { F } } ^ { n } .\tag{2}
$$

Thus, we define the Moore-Penrose inverse† of $A \in \mathcal { F } ^ { m \times n }$ , written $A ^ { + }$ as a generalized inverse of A satisfying the additional conditions

$$
( A A ^ { \mathrm { I } } ) ^ { * } = A A ^ { \mathrm { I } }
$$

$$
( A ^ { \mathbf { I } } A ) ^ { * } = { \mathfrak { A } } ^ { \mathbf { I } } A .
$$

Obviously, the existence of an orthogonal complement to a subspace and Proposition 12.7.4 together guarantee the existence of $A ^ { + }$ for any matrix A. It turns out, moreover, that the Moore-Penrose inverse is unique.

Proposition 1. Let $A \in \mathcal { F } ^ { m \times n }$ . There exists a unique matrix $\pmb { X } \in \mathcal { F } ^ { n \times m }$ for which

$$
A X A = A ,\tag{3}
$$

$$
X A X = X ,\tag{4}
$$

$$
( A X ) ^ { * } = A X ,\tag{5}
$$

$$
( X A ) ^ { * } = X A .\tag{6}
$$

†E. H. Moore, Bull. Amer. Math. Soc. 26 (1920), 394–395, and R. Penrose, Proc. Cambridge Phil. Soc. 51 (1955), 406–413.