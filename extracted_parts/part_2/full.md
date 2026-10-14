Exercise 7. Check that the matrices

$$
A = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } \qquad { \mathrm { a n d } } \qquad I = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] }
$$

are not similar, although they have the same rank, determinant, and trace. □

The similarity relation preserves some other properties of matrices.

Exercise 8. Show that if ${ \cal A } \approx { \cal B } ,$ then

(a) if B is idempotent, so is A;

(b) if B is nilpotent of degree k, so is A.

Exercise 9. Show that the scalar matrices are similar to themselves using any transforming matrix P. Conversely, prove that a matrix having this property must be scalar.

Hint. Consider first diagonal transforming matrices. □

## 4.5 Image and Kernel of a Linear Transformation

Theorem 1. Let $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ . If $\mathcal { S }$ is a subspace in $\mathcal { S } _ { 1 }$ , then $T ( \mathcal S )$ is a subspace in $\mathcal { S } _ { 2 }$

PROOF.'Let ${ \pmb y } _ { 1 } , { \pmb y } _ { 2 } \in T ( { \mathcal { S } } )$ . Then there are elements ${ \pmb x } _ { 1 } , { \pmb x } _ { 2 } \in \mathcal { S }$ such that ${ \bf y } _ { i } = T ( { \bf x } _ { i } ) ( i = 1 , 2 )$ . Since T is linear, it follows that

$$
\alpha y _ { 1 } + \beta y _ { 2 } = \alpha T ( x _ { 1 } ) + \beta T ( x _ { 2 } ) = \mathrm { T } ( \alpha x _ { 1 } + \beta x _ { 2 } ) .
$$

Hence for any $\alpha , \beta \in { \mathcal { F } } ,$ the element $\alpha { \bf y } _ { 1 } + \beta { \bf y } _ { 2 }$ is the image of a ${ \bf x } _ { 1 } + \beta { \bf x } _ { 2 } \in \mathcal { S } ,$ that is, it belongs to $T ( \mathcal { S } )$ . This proves that the image $T ( \mathcal S )$ is a linear subspace in $\mathcal { S } _ { 2 }$ .■

In particular, the image $T ( \mathcal { S } _ { 1 } )$ of the whole space $\mathcal { S } _ { 1 }$ , called the image of the transformation T and usually denoted by Im T, is a subspace in $T$ $\mathcal { S } _ { 2 }$ Its dimension is called the rank of the transformation T and is written rank T. Thus,

$$
\operatorname { r a n k } T \triangleq \mathrm { d i m } ( \operatorname { I m } T ) .
$$

We have seen in Exercise 4.13 that an m × n matrix A over $\mathcal { F }$ determines a linear transformation $T _ { A }$ from ${ \mathcal { F } } ^ { n }$ to ${ \mathcal { F } } ^ { m }$ in a natural way. Observe that Im $T _ { A }$ as defined here is just the subspace Im A of ${ \mathcal { F } } ^ { m }$ , as introduced in Section 3.2.

Exercise 1. Describe the image of the transformation $T \in \mathcal { L } ( \mathbb { R } ^ { 3 } , \mathbb { R } ^ { 4 } )$ defined in Exercise 4.2.1 and determine its rank.

SOLUTION. Representing $_ T$ as

$$
{ \begin{array} { r } { \left[ x _ { 2 } + x _ { 3 } \right] } \\ { x _ { 1 } + x _ { 2 } } \\ { x _ { 1 } } \\ { x _ { 1 } - x _ { 2 } } \end{array} } = x _ { 1 } { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 1 } \\ { 1 } \\ { 1 } \end{array} \right] } + x _ { 2 } { \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 0 } \\ { - 1 } \end{array} \right] } + x _ { 3 } { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { 0 } \\ { 0 } \end{array} \right] } ,
$$

it is not difficult to see that Im $T$ coincides with span $\{ \mathfrak { v } _ { 1 } , \mathfrak { v } _ { 2 } , \mathfrak { v } _ { 3 } \}$ , where $\mathfrak { v } _ { 3 } = [ 0 \mathrm { ~  ~ \mathsf ~ { ~ 1 ~ } ~ } 1 \mathrm { ~  ~ \mathsf ~ { ~ 1 ~ } ~ } ] ^ { \mathrm { T } } , \ \mathfrak { v } _ { 2 } = [ 1 \mathrm { ~  ~ \mathsf ~ { ~ 1 ~ } ~ } 0 \mathrm { ~  ~ \mathsf ~ { ~ - ~ 1 ~ } ~ } ] ^ { \mathrm { T } } , \ \mathfrak { v } _ { 3 } = [ 1 \mathrm { ~  ~ \mathsf ~ { ~ 0 ~ } ~ } 0 \mathrm { ~  ~ \mathsf ~ { ~ 0 ~ } ~ } ] ^ { \mathrm { T } } .$ The vectors ${ \mathfrak { v } } _ { i } ( i = 1 , 2 , 3 )$ are linearly independent and, therefore, rank $T = 3$

Exercise 2. Show that, for any linear subspace $\mathcal { S }$ of $\mathcal { S } _ { 1 }$

$$
\mathrm { d i m } \ T ( { \mathcal { S } } ) \leq \mathrm { d i m } { \mathcal { S } }\tag{1}
$$

and hence, that rank $T \leq$ dim $\mathcal { S } _ { 1 }$

Hint. Use Exercise 4.1.5. Compare this result with that of Exercise 3.5.6.

Exercise 3. Check that for any $T _ { 1 } , T _ { 2 } \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } ) .$

$$
\mathrm { I m } ( T _ { 1 } + T _ { 2 } ) \subset \mathrm { I m } T _ { 1 } + \mathrm { I m } T _ { 2 } .
$$

Then prove the inequalities

$$
\lvert \mathrm { r a n k } \ T _ { 1 } - \mathrm { r a n k } \ T _ { 2 } \rvert \leq \mathrm { r a n k } ( T _ { 1 } + { T _ { 2 } } ) \leq \mathrm { r a n k } \ T _ { 1 } + \mathrm { r a n k } \ T _ { 2 } .
$$

Hint. Use Exercise 3.6.2; compare this with the assertion of Proposition 3.8.2.

Exercise 4. Let $T _ { 1 } \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ and $T _ { 2 } \in \mathcal { L } ( \mathcal { S } _ { 2 } , \mathcal { S } _ { 3 } )$ . Show that

$$
\mathrm { I m } ( T _ { 2 } T _ { 1 } ) = T _ { 2 } ( \mathrm { I m } T _ { 1 } )
$$

and that

$$
\mathrm { r a n k } ( T _ { 2 } T _ { 1 } ) \leq \mathrm { m i n } ( \mathrm { r a n k } T _ { 1 } , \mathrm { r a n k } T _ { 2 } ) .
$$

Hint. Use Eq. (1). Compare this with the result of Exercise 3.8.5.

The notion of the rank of a transformation can be defined in a different way. Recall (Section 4.3) that all matrices from the equivalence class $\mathcal { A } _ { T }$ have the same rank and so this can be viewed as a characteristic of the transformation T itself. It is thus natural to consider this characteristic as the rank of T. Note that both definitions are equivalent.

## Theorem 2. With the previous notation,

$$
\operatorname { r a n k } T = \operatorname { r a n k } A
$$

for any $A \in \mathcal { A } _ { T }$

ProoF. Let A be the representation of $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ with respect to the bases $\mathcal { E } = \{ \mathbf { y } _ { j } \} _ { j = 1 } ^ { n }$ and $\mathcal { G } = \{ y _ { i } \} _ { i = 1 } ^ { m }$ for $\mathcal { S } _ { 1 }$ and $\mathcal { S } _ { 2 }$ , respectively. Since rank $T = \mathrm { d i m } ( \operatorname { s p a n } \{ T ( \pmb { x } _ { j } ) _ { j = 1 } ^ { n } ) ,$ it follows from Proposition 3.7.1 that rank $T = \mathrm { d i m } ( \operatorname { s p a n } \{ \boldsymbol { \mathfrak { p } } _ { j } \} _ { j = 1 } ^ { n } )$ , where $\beta _ { j } \ ( 1 \leq j \leq n )$ is the representation of the element $T ( \mathbf { x } _ { j } )$ with respect to the basis G. Recalling that $A =$ $[ { \pmb { \beta } } _ { 1 } \quad { \pmb { \beta } } _ { 2 } \quad \cdots \quad { \pmb { \beta } } _ { n } ]$ and using the result of Theorem 3.7.2, the proof is completed.

Generalizing the definition of the kernel of a matrix, as introduced in Section 3.2, we now define the kernel of any transformation $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ by

$$
\operatorname { K e r } T \triangleq \{ \pmb { x } \in \mathcal { S } _ { 1 } : T ( \pmb { x } ) = \pmb { \theta } \} .
$$

In the notation of Exercise 4.1.3 we see that for any matrix A, Ker $A =$ Ker $T _ { A }$

Theorem 3. Let $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ . The set Ker T is a linear subspace in $\mathcal { S } _ { 1 }$

PROOF. For any ${ \pmb x } _ { 1 } , { \pmb x } _ { 2 } \in { \bf K }$ er T and any α, $\beta \in { \mathcal { F } } ,$ the element $\alpha { \pmb x } _ { 1 } + \beta { \pmb x } _ { 2 }$ also belongs to the kernel of $T$

$$
T ( \alpha { \pmb x } _ { 1 } + \beta { \pmb x } _ { 2 } ) = \alpha T ( { \pmb x } _ { 1 } ) + \beta T ( { \pmb x } _ { 2 } ) = \alpha { \pmb \theta } + \beta { \pmb \theta } = { \pmb \theta } .
$$

This copletes the proof.

The dimension of the subspace Ker $T$ is referred to as the defect of the transformation and is denoted by def T.

Exercise 5. Describe the kernel of the transformation defined in Exercise 4.2.1 and determine its defect.

SOLUTION. To find the elements $\pmb { x } \in \mathcal { S } _ { 1 }$ such that $T ( \mathbf { x } ) = \pmb { \theta } ;$ we solve the system

$$
{ \begin{array} { r } { \left[ x _ { 2 } + x _ { 3 } \right] } \\ { x _ { 1 } + x _ { 2 } } \\ { x _ { 1 } } \\ { x _ { 1 } - x _ { 2 } } \end{array} } = \mathbf { 0 } ,
$$

which gives $x _ { 1 } = x _ { 2 } = x _ { 3 } = 0$ and Ker ${ \pmb T } = \{ { \pmb \theta } \}$ . Thus, def $T = 0$

Exercise 6. Describe the kernel and determine the defect of the transformation considered in Exercise 4.1.6.

Answer. Ker $T = \operatorname { s p a n } \{ [ 0 \quad \begin{array} { l l l l l l } { 1 } & { 1 } & { 1 } & { 0 ] ^ { \mathrm { T } } , [ 1 } & { 1 } & { 0 } & { - 1 ] ^ { \mathrm { T } } \} } \end{array}$ ; def T = 2. □

Theorem 4. For any matrix representation A of a linear transformation T,

$$
\dim ( \operatorname { K e r } T ) = \dim ( \operatorname { K e r } A ) .
$$

ProoF. Let us use the notations introduced in the proof of Theorem 2. An element x belongs to Ker T if and only if its representation $\pmb { \alpha } = [ \alpha _ { 1 } \quad \alpha _ { 2 } \quad \cdots \quad \alpha _ { n } ] ^ { \mathbf { T } }$ with respect to a basis $\pmb { \delta }$ belongs to the kernel of $A _ { \delta , \mathcal { G } } ,$ Indeed, if $\begin{array} { r } { { \bf x } = \sum _ { j = 1 } ^ { n } \alpha _ { j } { \bf x } _ { j } , } \end{array}$ then x ∈ Ker T if and only if $\begin{array} { r } { \sum _ { j = 1 } ^ { n } \dot { \alpha _ { j } } T ( \pmb { x } _ { j } ) = \pmb { \theta } } \end{array}$ or, what is equivalent,

$$
\sum _ { j = 1 } ^ { n } \alpha _ { j } \sum _ { i = 1 } ^ { m } a _ { i j } y _ { i } = \sum _ { i = 1 } ^ { m } \bigg ( \sum _ { j = 1 } ^ { n } \alpha _ { j } a _ { i j } \bigg ) y _ { i } = \pmb { \theta } .
$$

The linear independence of the elements $y _ { 1 } , y _ { 2 } , \ldots , y _ { m }$ from the basis $\mathscr { G }$ implies that $A _ { \mathcal { E } , \mathcal { G } } \alpha = \pmb { \theta } ;$ where $A _ { \mathcal { E } , \mathcal { G } } = [ a _ { i j } ] _ { i , j = 1 } ^ { m , n }$ . It remains only to apply Proposition 3.7.1.

Using the notion of the defect for matrices, we say that def T = def A for any A that is a representation of T. It should be emphasized that, in general, the subspaces Im T and Im A, as well as Ker T and Ker A, lie in different spaces and are essentially different.

Theorems 2 and 4, combined with the relation (3.8.1), yield the following useful result:

Theorem 5. For any $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$

$$
\operatorname { r a n k } T + \operatorname { d e f } T = \dim { \mathcal { S } } _ { 1 } .\tag{2}
$$

This result is in fact a particular case of the next theorem, which is inspired by the observation that Ker T consists of all elements of $\mathcal { S } _ { 1 }$ that are carried by T onto the zero element of $\mathcal { S } _ { 2 }$ . Hence, it is reasonable to expect that Im T is spanned by images of the basis elements in a complement to Ker T.

Theorem 6. Let $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ and let $\mathcal { S } _ { \mathfrak { d } }$ be a direct complement to Ker $T$ in $\mathcal { S } _ { 1 }$

$$
\mathcal { S } _ { 1 } = \mathrm { K e r } \ T + \mathcal { S } _ { 0 } .\tag{3}
$$

If $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { r }$ form a basis for $\mathcal { S } _ { 0 }$ , then $T ( \mathbf { x } _ { 1 } ) , T ( \mathbf { x } _ { 2 } ) , \ldots , T ( \mathbf { x } _ { r } )$ form a basis for Im T.

ProOF. We first observe that the elements $T ( \mathbf { x } _ { 1 } ) , \dots , T ( \mathbf { x } _ { r } )$ are linearly independent. Indeed, if

$$
\sum _ { i = 1 } ^ { r } \alpha _ { i } T ( \mathbf { x } _ { i } ) = T \bigg ( \sum _ { i = 1 } ^ { r } \alpha _ { i } \mathbf { x } _ { i } \bigg ) = \pmb { \mathscr { 0 } } ,
$$

then the element $\sum _ { i = 1 } ^ { r } \alpha _ { i } x _ { i }$ is in $( \mathsf { K e r } T ) \cap \mathcal { S } _ { 0 }$ and hence is the zero element of $\mathcal { S } _ { 1 }$ . Now the linear independence of $\{ { \pmb x } _ { i } \} _ { i = 1 } ^ { r }$ yields $\alpha _ { i } = 0 ( i = 1 , 2 , . . . , r )$ and the linear independence of $T ( \mathbf { x } _ { 1 } ) , \dots , T ( \mathbf { x } _ { r } )$

Furthermore, every element $y \in$ Im T can be represented as a linear combination of $T ( \pmb { x } ) , \dots , T ( \pmb { x } _ { r } )$ .To see this, we first write ${ \bf y } = T ( { \bf x } )$ for some $\pmb { x } \in \mathcal { S } _ { 1 }$ . Let $\left\{ { \bf { x } } _ { i } ^ { \prime } \right\} _ { i = 1 } ^ { k }$ be a basis for Ker $T ,$ where k = def T. If the basis representation of x is

$$
{ \pmb x } = \sum _ { i = 1 } ^ { k } \beta _ { i } { \pmb x } _ { i } ^ { \prime } + \sum _ { i = 1 } ^ { r } \gamma _ { i } { \pmb x } _ { i } ,
$$

we obtain $\begin{array} { r } { T ( \pmb { x } ) = \sum _ { i = 1 } ^ { r } \gamma _ { i } T ( \pmb { x } _ { i } ) } \end{array}$ , which completes the proof.

Exercise 7. Deduce Eq. (2) from Theorem 6. □

The assertion of Theorem 6 is seen from a different point of view in the next exercise.

Exercise 8. $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ and let Im $T = \operatorname { s p a n } \{ y _ { 1 } , y _ { 2 } , \dots , y _ { r } \}$ , where $y _ { i } = T ( \pmb { x } _ { i } )$ for $i = 1 , 2 , \ldots , r .$ (We say $\pmb { x } _ { i }$ is the preimage of $y _ { i } . )$ Confirm that $\mathcal { S } _ { 0 } = \operatorname { s p a n } \{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \dots , \pmb { x } _ { r } )$ satisfies Eq. (3). □

Using the same technique as in the proof of Theorem $\begin{array} { r } { { \bf 6 , } } \end{array}$ it is not difficult to prove the next exercise.

Exercise 9. If $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ and $\mathcal { S }$ is a linear subspace in $\mathcal { S } _ { 1 }$ , show that

$$
\dim T ( { \mathcal { S } } ) = \dim { \mathcal { S } } - \dim ( { \mathcal { S } } \cap \operatorname { K e r } T ) .\tag{4}
$$

Hint. Extend a basis in $\mathcal { S } \cap \mathbb { K }$ er T to a basis in $\mathcal { S } \sqcap$

Note that Eq. (4) implies Eqs. (1) and (2) (for $\mathcal { S } = \mathcal { S } _ { 1 } )$ and also the inequality

$$
\dim T ( { \mathcal { S } } ) \geq \dim { \mathcal { S } } - \deg T .\tag{5}
$$

The next exercises concern properties of sums and compositions of linear transformations.

Exercise 10. Let $T _ { 1 } , T _ { 2 } \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ . Check that

$$
\mathrm { K e r } \ T _ { 1 } \cap \mathrm { K e r } \ T _ { 2 } \subset \mathrm { K e r } ( T _ { 1 } + { T _ { 2 } } ) .
$$

Exercise 11. Let $T _ { 1 } \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ and $T _ { 2 } \in \mathcal { L } ( \mathcal { S } _ { 2 } , \mathcal { S } _ { 3 } )$

(a) Show that

$$
\begin{array} { r } { \mathsf { K e r } \ T _ { 1 } \subset \mathsf { K e r } ( T _ { 2 } T _ { 1 } ) = \{ \mathbf { x } \in \mathcal { S } _ { 1 } : T _ { 1 } ( \mathbf { x } ) \in \mathsf { K e r } \ T _ { 2 } \} . } \end{array}
$$

(b) Show that $T _ { 1 } ( \mathrm { K e r } \ T _ { 2 } T _ { 1 } ) \subset \mathrm { K e r }$ $T _ { 2 }$ with equality if Ker $T _ { 2 } \subset \mathrm { I m } \ T _ { 1 }$

(c) Apply the inequality (5) with ${ \mathcal { S } } = \mathop { \mathrm { K e r } } ( T _ { 2 } T _ { 1 } )$ and $T = T _ { 1 }$ to show that

$$
\begin{array} { r } { \operatorname* { d e f } ( T _ { 2 } T _ { 1 } ) \leq \operatorname* { d e f } T _ { 1 } + \operatorname* { d e f } T _ { 2 } . } \end{array}\tag{6}
$$

Exercise 12. Check that for any $T \in { \mathcal { L } } ( { \mathcal { S } } )$

$$
\begin{array} { r } { \mathrm { K e r } \ T \subset \mathrm { K e r } \ T ^ { 2 } \subset \mathrm { K e r } \ T ^ { 3 } \subset \cdots , } \\ { \mathrm { I m } \ T \supset \mathrm { I m } \ T ^ { 2 } \supset \mathrm { I m } \ T ^ { 3 } \supset \cdots . } \end{array}
$$

Exercise 13. Show that if

$$
\begin{array} { r } { \mathrm { K e r \ } T ^ { k } = \mathrm { K e r \ } T ^ { k + 1 } , } \end{array}\tag{7}
$$

then Ker $T ^ { j } = \mathsf { K e r } \ T ^ { j + 1 }$ for all $j \geq k .$

SoLUTIoN. Suppose on the contrary that for some $j > k ,$ we have Ker $T ^ { j }$ $\neq \mathsf { K e r } \ T ^ { j + 1 }$ . In other words, $T ^ { j + 1 } ( { \boldsymbol { \mathsf { x } } } ) = { \pmb { \theta } }$ but $T ^ { j } ( { \pmb x } ) \neq { \pmb \theta }$ for some $\pmb { x } \in \mathcal { S } _ { 1 }$ Writing $j = k + i ,$ we obtain $T ^ { k + 1 } ( T ^ { i } ( { \pmb x } ) ) = { \pmb \theta }$ while $T ^ { k } ( T ^ { i } ( x ) ) \neq 0 .$ This contradicts the assumption that Ker $T ^ { k } = \mathsf { K e r } \ T ^ { k + 1 }$ □

Since strict inclusion between subspaces, $\mathcal { S } _ { 0 } \subset \mathcal { S } _ { 1 }$ , implies dim $\mathcal { S } _ { 0 }$ $<$ dim $\mathcal { S } _ { 1 }$ , then, in a chain of subspaces of a finite-dimensional space $\mathcal { S }$ such that

$$
\mathcal { S } _ { 0 } \subset \mathcal { S } _ { 1 } \subset \cdots \subset \mathcal { S } _ { k } \subset \cdots \subset \mathcal { S } ,
$$

there exists a positive integer $k \leq \dim { \mathcal { S } }$ such that $\mathcal { S } _ { k } = \mathcal { S } _ { k + 1 } = \cdots$ . Using this observation and combining Exercises 12 and 13 will yield the conclusion of the next exercise.

Exercise 14. Check that for any $T \in { \mathcal { L } } ( { \mathcal { S } } )$

$$
\mathrm { K e r } \ T \subset \mathrm { K e r } \ T ^ { 2 } \subset \cdots \subset \mathrm { K e r } \ T ^ { k } = \mathrm { K e r } \ T ^ { k + 1 } = \cdots \subset { \mathcal { S } } ,
$$

where k denotes a positive integer between 1 and $n , n = \dim { \mathcal { S } } ,$ and the inclusions are strict. □

## 4.6 Invertible Transformations

A transformation $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ is said to be left invertible if there exists a transformation $T _ { 1 } \in \mathcal { L } ( \mathcal { S } _ { 2 } , \mathcal { S } _ { 1 } )$ such that

$$
T _ { 1 } T = I _ { 1 } ,\tag{1}
$$

where $I _ { 1 }$ denotes the identity transformation in $\mathcal { S } _ { 1 }$ . If Eq. (1) holds, then the transformation $T _ { 1 }$ is called a left inverse of T.

Theorem 1. Let $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ and let dim $\mathcal { S } _ { 1 } = n ,$ dim ${ \mathcal { S } } _ { 2 } = m .$ The following statements are equivalent:

(a) T is left invertible;

(b) Ker $T = \left\{ \pmb { \theta } \right\}$ n

(c) T defines an isomorphism between $\mathcal { S } _ { 1 }$ and Im $T ;$

(d) $n \leq$ m and rank $T = n ;$

(e) Every representation of T is an $m \times n$ matrix with $n \leq m$ and full rank.

ProOF. If Eq. (1) holds and $T ( { \bf { x } } ) = \bf { 0 } ,$ then ${ \bf { x } } = I _ { 1 } ( { \bf { x } } ) = T _ { 1 } ( T ( { \bf { x } } ) ) = \bf { 0 }$ hence Ker $T = \{ \pmb { \theta } \}$ and $( a ) \Rightarrow ( b )$ . To deduce (c) from (b) it suffices, in view of the linearity of $T ,$ to establish a one-to-one correspondence between $\mathcal { S } _ { 1 }$ and Im T. Let $\mathbf { y } = T ( \mathbf { x } _ { 1 } ) = T ( \mathbf { x } _ { 2 } )$ where $\mathbf { x } _ { i } \in \mathcal { S } _ { 1 } ( i = 1 , 2 )$ . Then $T ( \mathfrak { x } _ { 1 } - \mathfrak { x } _ { 2 } ) = \pmb { \mathscr { 0 } }$ and the condition Ker $T = \{ \pmb { \theta } \}$ yields ${ \pmb x } _ { 1 } = { \pmb x } _ { 2 }$ and, consequently, the required uniqueness of x. To prove the implication $( c ) \Rightarrow ( a )$ 2 we observe that the existence of a one-to-one map (namely, T) from $\mathcal { S } _ { 1 }$ onto Im $T$ permits the definition of the transformation $T _ { 1 } \in \mathcal { L } ( \mathrm { I m } \ T , \mathcal { S } _ { 1 } )$ by the rule: If $y = T ( x )$ then $T _ { 1 } ( y ) = x$ Obviously $T _ { 1 } ( T ( \mathbf { x } ) ) = T _ { 1 } ( \mathbf { y } ) = \mathbf { x }$ for all $\pmb { x } \in \mathcal { S } _ { 1 }$ , or, what is equivalent, $T _ { 1 } T = I _ { 1 }$ . Thus, $( c ) \Rightarrow ( a )$ . We have shown that $( a ) , ( b )$ and (c) are equivalent.

Now we note that the equivalence $( b ) \Leftrightarrow ( d )$ follows from Eq. (4.5.2), and Theorem 4.5.2 gives the equivalence $( d ) \Leftrightarrow ( e )$ . This completes the proof.

Exercise 1. Check the equivalence of the following statements:

(a) $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ is left invertible.

(b) For any linear subspace $\mathcal { S } \subset \mathcal { S } _ { 1 }$

$$
\dim T ( { \mathcal { S } } ) = \dim { \mathcal { S } } ,
$$

(c) Any linearly independent system in $\mathcal { S } _ { 1 }$ is carried by T into another linearly independent system in $\mathcal { S } _ { 2 }$ . □

The notion of right invertibility of a transformation is defined similarly by saying that $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ is right invertible if one can find a transformation $T _ { 2 } \in \mathcal { L } ( \mathcal { S } _ { 2 } , \mathcal { S } _ { 1 } )$ such that

$$
T T _ { 2 } = I _ { 2 } ,\tag{2}
$$

where $I _ { 2 }$ denotes the identity transformation in $\mathcal { S } _ { 2 }$ . The transformation $T _ { 2 }$ in Eq. (2) is referred to as a right inverse of T.

Theorem 2. Let $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ and let dim $\mathcal { S } _ { 1 } = n ,$ dim $\mathcal { S } _ { 2 } = m$ The following statements are equivalent :

(a) T is right invertible;

(b) rank $T = m ;$

(c) T defines an isomorphism between any direct complement to Ker T and $\mathcal { S } _ { 2 }$

(d) n ≥ m and def $T = n - m$

(e) Every representation of T is an m × n matrix with $n \geq$ m and full rank.

PROOF. $( a ) \Rightarrow ( b )$ Let Eq. (2) hold and let $\boldsymbol { y } \in \mathcal { S } _ { 2 }$ . Then $\begin{array} { r } { { \bf y } = T T _ { 2 } ( { \bf y } ) = } \end{array}$ $T ( T _ { 2 } ( y ) )$ and the element ${ \pmb x } = T _ { 2 } ( { \pmb y } ) \in \mathcal { S } _ { 1 }$ is a pre-image of y. Thus $\mathcal { S } _ { 2 } =$ Im T and part (b) follows from part (a). To prove the implication $( b ) \Rightarrow ( c )$ we consider a subspace $\mathcal { S } _ { 0 }$ such that $\mathcal { S } _ { 1 } \stackrel {  } { = } \mathsf { K e r } \ T + \mathcal { S } _ { 0 }$ and show that T provides a one-to-one correspondence between $\mathcal { S } _ { 0 }$ and $\mathcal { S } _ { 2 }$ . Indeed, if $\mathbf { y } = T ( \mathbf { x } _ { 1 } ) = T ( \mathbf { x } _ { 2 } )$ , where $\pmb { x } _ { i } \in \mathcal { S } _ { 0 } \left( i = 1 , 2 \right)$ , then ${ \pmb x } _ { 1 } - { \pmb x } _ { 2 } = \mathcal { S } _ { 0 } \cap$ Ker T ${ \bf \mu } = \{ { \pmb \theta } \}$ . Hence ${ \pmb x } _ { 1 } = { \pmb x } _ { 2 }$ and the required isomorphism between $\mathcal { S } _ { 0 }$ and $\mathcal { S } _ { 2 }$ follows from the linearity of T. Now observe that this isomorphism guarantees the existence of a transformation $T _ { 2 } \in \mathcal { L } ( \mathcal { S } _ { 2 } , \mathcal { S } _ { 0 } )$ defined by the rule:

$$
{ \mathrm { I f ~ } } y = T ( \mathbf { x } ) { \mathrm { ~ w h e r e ~ } } x \in \mathcal { S } _ { 0 } { \mathrm { , ~ t h e n ~ } } T _ { 2 } ( y ) = \mathbf { x } .
$$

Clearly, $T ( T _ { 2 } ( y ) ) = T ( x ) = y$ for all $\boldsymbol { y } \in \mathcal { S } _ { 2 }$ and the relation (2) holds.   
Thus, the equivalence of $( a ) , ( b )$ , and (c) is established.

Note that the equivalences $( b ) \Leftrightarrow ( d )$ and $( d ) \Leftrightarrow ( e )$ are immediate consequences of Theorems 4.5.5 and 4.5.2, respectively.

The notions of left (or right) invertible matrices and their one-sided inverses are defined similarly to those for transformations. As pointed out in Section 2.6, a one-sided inverse of a square matrix is necessarily an inverse matrix, that is, both a left and right inverse.

Exercise 2. Show that a transformation $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ is left (respectively, right) invertible if and only if any representation A is a left (respectively, right) invertible matrix.

Hint. Use the correspondence (4.2.4). □

Theorems 1 and 2 applied to matrices state, in particular, that a rectangular m × n matrix of full rank is left invertible if $m \geq n ,$ and it is right invertible if $m \leq n$ n. The treatment of one-sided invertible matrices will be continued in the chapter on generalized inverses, while the invertibility properties of square matrices are discussed later in this section after some further preparations.

Let $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ . The transformation T is said to be invertible if it is both left and right invertible. We combine Theorems 1 and 2 and the corollary to Theorem 3.7.1 to derive the next theorem.

Theorem 3. Let $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } { \mathcal { S } } _ { 2 } )$ and let dim $\mathcal { S } _ { 1 } = n ,$ dim $\mathcal { S } _ { 2 } = m .$ The following statements are equivalent:

(a) T is invertible;

(b) Ker $T = \{ \pmb { \theta } \}$ , rank $T = m = n$

(c) T defines an isomorphism between $\mathcal { S } _ { 1 }$ and $\mathcal { S } _ { 2 }$

(d) Every representation of T is an n × n nonsingular matrix.

Using Theorem 4.5.5, we deduce three corollaries.

Corollary 1. Let $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ be left invertible. Then T is invertible if and only if dim $\mathcal { S } _ { 1 } = \dim \mathcal { S } _ { 2 }$ . In particular, a left invertible transformation acting on $\mathcal { S }$ is invertible and defines a one-to-one map of $\mathcal { S }$ onto itself.

Corollary 2. Let $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ be right invertible. Then $T$ is invertible if and only if def $T = 0$ . In particular, a right invertible transformation acting on $\mathcal { S }$ is invertible and produces a one-to-one map of $\mathcal { S }$ onto itself.

Corollary 3. Any representation of an invertible transformation is an invertible matrix.

Consider an invertible transformation $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ . By definition there are transformations $T _ { 1 } , T _ { 2 } \in \mathcal { L } ( \mathcal { S } _ { 2 } , \mathcal { S } _ { 1 } )$ such that simultaneously Eqs. (1) and (2) hold. In this case, the equalities

$$
T _ { 1 } = T _ { 1 } I _ { 2 } = T _ { 1 } ( T T _ { 2 } ) = ( T _ { 1 } T ) T _ { 2 } = I _ { 1 } T _ { 2 } = T _ { 2 }
$$

show that the one-sided inverses of T coincide. Hence there is a transformation $T ^ { \prime 1 } \in \mathcal { L } ( \mathcal { S } _ { 2 } , \mathcal { S } _ { 1 } )$ satisfying the conditions

$$
T ^ { - 1 } T = I _ { 1 } \qquad \mathrm { a n d } \qquad T T ^ { - 1 } = I _ { 2 } .\tag{3}
$$

The transformation $T ^ { - 1 }$ is called the inverse of $T$ and is easily seen to be unique. It is clear, comparing Eq. (4.2.4) with Eq. (3), that if $A$ is a representation of an invertible transformation $T \in { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ with respect to the bases $( \mathcal { E } , \mathcal { G } )$ , then $A ^ { - 1 }$ is the representation of $T ^ { - 1 }$ with respect to $( \mathcal { G } , \mathcal { E } )$ In particular, if T, $T ^ { - 1 } \in { \mathcal { L } } ( { \mathcal { S } } )$ , then their representations with respect to a fixed basis in $\mathcal { S }$ are correspondingly A and $\overset { \cdot } { A } ^ { - 1 }$

Note that part (d) of Theorem 3 asserts that a transformation Tis invertible if and only if det $A \neq 0$ for every $A \in \mathcal { A } _ { T }$ . When $T$ acts on a space ${ \mathcal { S } } ,$ then by Exercise 4.4.1(b) all its representations have the same determinant. In this case it is then reasonable to define the determinant of the transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ , written det $T ,$ as the determinant of any of its representations $\mathcal { A } _ { T } ^ { 0 }$ . Hence we now conclude that a transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ is invertible if and only if det $T \neq 0 .$ This result for matrices was established in Section 2.6.

Exercise 3. Let $T _ { i } \colon \mathcal { S } _ { i } \stackrel { \mathrm { o n t o } } { \longrightarrow } \mathcal { S } _ { i + 1 } ( i = 1 , 2 , \ldots , k )$ be invertible linear transformations. Show that $T = T _ { k } T _ { k - 1 } \cdot \cdot \cdot T _ { 1 } \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { k + 1 } )$ is also invertible and that $T ^ { - 1 } = T _ { 1 } ^ { - 1 } T _ { 2 } ^ { - 1 } \cdot \cdot \cdot T _ { k } ^ { - 1 } . \stackrel { \cdot } { \bigsqcup }$

The result in Exercise 3 can be reversed in the following sense.

Exercise 4. Let $T _ { i } \in \mathcal { L } ( \mathcal { S } ) , i = 1 , 2 , \ldots , k .$ Check that all $T _ { i }$ are invertible if and only if, for any permutation $( j _ { 1 } , j _ { 2 } , \ldots , j _ { k } )$ of $( 1 , 2 , \ldots , k )$ , the transformation $T _ { j _ { 1 } } T _ { j _ { 2 } } \cdots T _ { j _ { k } }$ is invertible.

Exercise 5. Check that if $\sum _ { i \mathop { = } 0 } ^ { k } p _ { i } T ^ { i } = 0 , \ p _ { 0 } \not = 0 ;$ and $T \in { \mathcal { L } } ( { \mathcal { S } } )$ , then T is invertible. □

## 4.7 Restrictions, Invariant Subspaces, and Direct Sums of Transformations

Let $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ and let $\mathcal { S } _ { 0 }$ be a linear subspace in $\mathcal { S } _ { 1 }$ . The transformation $\tilde { T } : \mathcal { S } _ { 0 }  \bar { \mathcal { S } } _ { 2 }$ defined by $\tilde { T } ( \mathbf { x } ) = T ( \mathbf { x } )$ for every $\boldsymbol { x } \in \mathcal { S } _ { 0 }$ is referred to as the restriction of T to $\mathcal { S } _ { \mathbf { 0 } }$ and is denoted by $T \vert _ { \mathcal { S } _ { 0 } }$ . Obviously, $T | _ { \mathcal { S } _ { 0 } } \in \mathcal { L } ( \mathcal { S } _ { 0 } , \mathcal { S } _ { 2 } )$ In contrast, a transformation $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ coinciding with $\widetilde { T }$ on $\mathcal { S } _ { 0 } \subset \mathcal { S } _ { 1 }$ is called an extension of $\tilde { \cal T } .$

Exercise 1. Let $T { \in } { \mathcal { L } } ( { \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } )$ . Check that for any linear subspace $\mathcal { S } _ { 0 } \subset \mathcal { S } _ { 1 }$

$$
\mathrm { I m } ( T | _ { \mathcal { S } _ { 0 } } ) = T ( \mathcal { S } _ { 0 } ) , \qquad \mathrm { K e r } ( T | _ { \mathcal { S } _ { 0 } } ) = \mathcal { S } _ { 0 } \cap \mathrm { K e r } \ T ; \quad \bigtriangledown
$$

The second relation of Exercise 1 shows that if $\mathcal { S } _ { 0 }$ is any direct complement to Ker T in $\mathcal { S } _ { 1 }$ (thus $\mathcal { S } _ { 0 } \dot { + } \operatorname { K e r } T = \mathcal { S } _ { 1 } )$ , then $T \mid _ { \mathcal { S } _ { 0 } }$ has the trivial subspace {0} as its kernel. In this case, we deduce from Theorem 4.5.6 that Im $T = T ( \mathcal { S } _ { 0 } )$ . So the action of a linear transformation T is completely determined by its action on a direct complement to Ker T, that is, by the restriction of T to such a subspace.

We now consider an arbitrary decomposition of the domain into a direct sum of subspaces (as defined in Section 3.6).

Exercise 2. Let $T \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } )$ and let ${ \mathcal { S } } _ { 1 } = { \mathcal { S } } _ { 0 } { \dot { + } } { \tilde { \mathcal { S } } } .$ Write ${ \pmb x } = { \pmb x } _ { 1 } + { \pmb x } _ { 2 }$ where $\mathbf { { x } } _ { 1 } \in \mathcal { S } _ { 0 } , \mathbf { { x } } _ { 2 } \in \tilde { \mathcal { S } } .$ and show that, if $T _ { 1 } \in \mathcal { L } ( \mathcal { S } _ { 0 } , \mathcal { S } _ { 2 } )$ and $T _ { 2 } \in \mathcal { L } ( \tilde { \mathcal { S } } , \mathcal { S } _ { 2 } )$ the equality

$$
T ( \pmb { x } ) = T _ { 1 } ( \pmb { x } _ { 1 } ) + T _ { 2 } ( \pmb { x } _ { 2 } )\tag{1}
$$

holds for any $\mathbf { \Delta x } \in \mathcal { S } _ { 1 }$ if and only if $T _ { 1 } = T | _ { \mathcal { S } _ { 0 } }$ and $T _ { 2 } = T | \tilde { \mathcal { s } }$ . □

A similar result can be easily formulated for a direct sum of several subspaces as defined in Section 3.6.

Suppose now that $\mathcal { S } _ { 1 } = \mathcal { S } _ { 2 }$ . Thus we investigate transformations $T \in { \mathcal { L } } ( { \mathcal { S } } )$ . The following concept, which is important in its own right, is helpful in this context.

Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ . A subspace $\mathcal { S } _ { 0 } \subset \mathcal { S }$ is called invariant under $T$ (or $T \cdot$ invariant), if for any $\pmb { x } \in \mathcal { S } _ { 0 }$ , the image $T ( { \pmb x } )$ also belongs to $\mathcal { S } _ { 0 }$

$$
T ( x ) \in \mathcal { S } _ { 0 } \qquad \mathrm { f o r ~ a l l ~ } x \in \mathcal { S } _ { 0 } .\tag{2}
$$

In other words, if $\mathcal { S } _ { 0 }$ is T-invariant, then every element $\pmb { x } \in \mathcal { S } _ { 0 }$ is transformed by T into an element of the same subspace $\mathcal { S } _ { 0 }$ . Hence the restriction $T | _ { \mathcal { S } _ { 0 } }$ in this case is a transformation acting on $\mathcal { S } _ { 0 }$ and therefore can be viewed as a “ part" of T in $\mathcal { S } _ { 0 }$

Obviously, $\{ \pmb { \theta } \}$ and the whole space are invariant under any transformation. These spaces are referred to as the trivial invariant subspaces and usually are excluded from further considerations.

The next exercise shows that linear transformations that are not invertible always have nontrivial invariant subspaces.

Exercise 3. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ . Show that Ker T and Im T are T-invariant.   
Show also that any subspace containing Im T is T-invariant.

SoLUTION. For the first subspace, let $\pmb { x } \in \mathbf { K }$ er T. Then $T ( \pmb { x } ) = \pmb { \theta }$ and, since $\pmb { \theta } \in \mathbf { K }$ er T, the condition (2) is valid. The proof of T-invariance of Im T is similar.

Exercise 4. Show that $\mathcal { S } _ { 0 }$ is T-invariant if and only if $T ( \mathbf { x } _ { i } ) \in \mathcal { S } _ { 0 } \ ( i = 1$ $2 , \ldots , k )$ , where $\{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \ldots , \pmb { x } _ { k } \}$ is a basis for $\mathcal { S } _ { 0 }$

Exercise 5. Check that if $T _ { 1 } T _ { 2 } = T _ { 2 } T _ { 1 }$ , then Ker $T _ { 2 }$ and Im $T _ { 2 }$ are $T _ { 1 } \cdot$ invariant.

Exercise 6. Show that sums and intersections of T-invariant subspaces are T-invariant. □

The notion of an invariant subspace for a matrix A is obtained from that for transformations by treating A as the transformation $T _ { A }$ introduced in Exercise 4.1.3.

Proposition 1. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and suppose that T has an invariant subspace in $\mathcal { S }$ of dimension k. Then there exists a matrix $A \in \mathcal { A } _ { T } ^ { 0 }$ such that one of its invariant subspaces is also of dimension k.

ProOF. Let the subspace $\mathcal { S } _ { 0 } \subset \mathcal { S }$ be T-invariant of dimension k. Let $\mathcal { E } _ { 0 }$ be a basis in $\mathcal { S } _ { 0 }$ and let the basis $\pmb { \delta }$ in $\mathcal { S }$ be the union of $\boldsymbol { \mathcal { E } } _ { 0 }$ and a basis in a direct complement to $\mathcal { S } _ { 0 }$ in S. If $\begin{array} { r } { \mathbf { y } = T ( \mathbf { x } ) , \mathbf { x } \in \mathcal { S } _ { 0 } } \end{array}$ , then, because of the invariance of $\mathcal { S } _ { 0 }$ under $T ,$ the representation β of y with respect to $\pmb { \delta } ^ { o }$ is of the form $\mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta } \mathbf { \beta \beta } \mathbf { \beta } \mathbf { \beta \beta } \mathbf \mathbf { \beta } \mathbf { \beta \beta } \mathbf \mathbf { \beta } \mathbf  \beta \mathbf { \beta } \mathbf \mathbf  $ The representation α of x with respect to the same basis $\pmb { \delta }$ is also of this form, and then Theorem 4.2.2 implies that the subspace of the representations of the elements of $\mathcal { S } _ { \mathfrak { d } }$ with respect to $\pmb { \delta } ^ { \pmb { \sigma } }$ is $A _ { \delta } { * }$ invariant. Clearly, the dimension of this subspace is equal to k.

Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and let $\mathcal { S } _ { \mathfrak { d } } \subset \mathcal { S }$ be a T-invariant subspace. Denote by $\mathcal { \tilde { S } }$ a direct complement to $\mathcal { S } _ { \mathbf { 0 } }$ in $\mathcal { S } \colon \mathcal { S } = \mathcal { S } _ { 0 } \dot { + } \tilde { \mathcal { S } } .$ (For the existence of such a space ${ \mathcal { \tilde { S } } } ,$ see Section 3.5.) Note that $\tilde { \mathcal { S } }$ is not necessarily T-invariant.

Example 7. Let $T \in \mathcal { L } ( \mathcal { F } ^ { 2 } )$ be defined as follows:

$$
T { \sqrt { \left( { \frac { x _ { 1 } } { x _ { 2 } } } \right) } } = { \left[ \begin{array} { l l } { x _ { 1 } + x _ { 2 } } \\ { \qquad x _ { 2 } } \end{array} \right] } .
$$

Obviously, $\begin{array} { r l } { \mathcal { S } _ { 0 } \triangleq \operatorname { s p a n } \{ [ 1 } & { { } 0 ] ^ { \mathrm { T } } \} = \{ [ \alpha \quad 0 ] ^ { \mathrm { T } } : \alpha \in \mathcal { F } \} } \end{array}$ is T-invariant: $\begin{array} { r l } { T ( [ \alpha } & { { } 0 ] ^ { \mathsf { T } } ) = [ \alpha \quad 0 ] ^ { \mathsf { T } } \in \mathcal { S } _ { 0 } } \end{array}$ . However, the subspace $\tilde { \mathcal { S } } \triangleq \operatorname { s p a n } \{ [ 0 \quad 1 ] ^ { \mathbf { T } } \}$ is a direct complement to $\mathcal { S } _ { \mathbf { 0 } }$ , but it fails to be T-invariant: $\begin{array} { r l } { T ( [ 0 } & { { } 1 ] ^ { \boldsymbol { \mathsf { T } } } ) = } \end{array}$ $\begin{array} { r l } { [ 1 } & { { } 1 ] ^ { \boldsymbol { \mathsf { T } } } \notin \tilde { \mathcal { S } } . } \end{array}$ Observing that $\mathcal { S } _ { \mathfrak { d } }$ is the only nontrivial T-invariant subspace of $\mathcal { F } ^ { 2 }$ . we deduce that it is impossible to decompose $\mathcal { F } ^ { 2 }$ into a direct sum of T-invariant subspaces. □

If the space $\mathcal { S }$ can be decomposed into a direct sum of k subspaces $\mathcal { S } _ { i } ,$ ,all of which are T-invariant, we may write, for every $\mathbf { x } \in { \mathcal { S } } ,$

$$
T ( \pmb { x } ) = \sum _ { i = 1 } ^ { k } { \frac { \ d } { \ d t } } T _ { i } ( \pmb { x } _ { i } ) ,\tag{3}
$$

where $\begin{array} { r } { \mathbf { \Delta x } = \sum _ { i = 1 } ^ { k } x _ { i } \left( x _ { i } \in \mathcal { S } _ { i } , i = 1 , 2 , . . . , k \right) } \end{array}$ and $T _ { i } = \left. T \right. _ { \mathcal { S } _ { i } }$ for each i. (See the remark immediately following Exercise 2.) Note that when $k = 2 \mathrm { E q }$ (3) differs from Eq. (1) to the extent that we may now interpret $T _ { i }$ as being in ${ \mathcal { L } } ( { \mathcal { S } } _ { i } )$ for $i = 1$ and 2. Bearing Eq. (3) in mind, we give the following definition.

Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and let $\begin{array} { r } { \mathcal { S } = \sum _ { i = 1 } ^ { k } \dot { \mathcal { S } } _ { i } } \end{array}$ , where each $\mathcal { S } _ { i }$ is T-invariant. Then the transformation $_ T$ is referred to as the direct sum of the transformations $T _ { i } = T | _ { \mathcal { S } _ { i } } \left( i = 1 , 2 , \ldots , k \right)$ and is written

$$
T = \sum _ { i = 1 } ^ { k } { } ^ { \cdot } T _ { i } \triangleq T _ { 1 } + T _ { 2 } + \cdots + T _ { k } .\tag{4}
$$

Note that Eq. (4) now implies Eq. (3) for every $\pmb { x } \in \mathcal { S } ,$ and vice versa. The significance of the representation (4) lies in the possibility of reducing the study of the transformation $T$ to that of its “parts" $T _ { i }$ acting on smaller subspaces. This is the basic strategy adopted in the next section for the analysis of the class of matrix representations of $T .$

Exercise 8. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and $p ( \lambda )$ be a scalar polynomial. Show that if a subspace is T-invariant, then it is $p ( T )$ -invariant. □

## 4.8 Direct Sums and Matrices

Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and let $\mathcal { A } _ { \mathrm { ~ T ~ } } ^ { 0 }$ denote the equivalence class of similar matrices associated with T. In searching for the simplest matrices in this class, we first study the representations of T in the case when the space $\mathcal { S }$ is decomposed into a direct sum of subspaces, at least one of which is T-invariant.

Let $\mathcal { S } = \mathcal { S } _ { 1 } \ : + \mathcal { S } _ { 2 }$ , where $\mathcal { S } _ { 1 }$ is T-invariant, assuming for the moment that such a decomposition is always possible. Now we construct a representation of $T$ that is most “appropriate"for the given decomposition of the space, namely, we build up the representation of T with respect to the basis

$$
\left\{ { \bf { x } } _ { 1 } , { \bf { x } } _ { 2 } , \ldots , { \bf { x } } _ { k } , { \bf { x } } _ { k + 1 } , \ldots , { \bf { x } } _ { n } \right\}\tag{1}
$$

in ${ \mathcal { S } } ,$ where k = dim $\mathcal { S } _ { 1 }$ and the first k elements constitute a basis in $\mathcal { S } _ { 1 }$ Since $\mathcal { S } _ { 1 }$ is T-invariant, $T ( \mathbf { x } _ { i } ) \in \mathcal { S } _ { 1 } \left( j = 1 , 2 , \ldots , k \right)$ and Eq. (4.2.1) gives

$$
T ( { \pmb x } _ { j } ) = \sum _ { i = 1 } ^ { k } \alpha _ { i j } { \pmb x } _ { i } , \qquad j = 1 , 2 , \ldots , k .\tag{2}
$$

Hence the matrix $A = [ \alpha _ { i j } ] _ { i , j = 1 } ^ { n }$ , where the $\alpha _ { i j } ( 1 \leq i , j \leq n )$ are found from the equation $\begin{array} { r } { T ( \pmb { x } _ { j } ) = \sum _ { i = 1 } ^ { n } \alpha _ { i j } \pmb { x } _ { i } ( j = 1 , 2 , \ldots , n ) } \end{array}$ , is of the form:

$$
A = { \left[ \begin{array} { l l } { A _ { 1 } } & { A _ { 3 } } \\ { 0 } & { A _ { 2 } } \end{array} \right] } ,\tag{3}
$$

where $A _ { 1 } \in { \mathcal { F } } ^ { k \times k }$ and $A _ { 2 } \in \mathcal { F } ^ { ( n - k ) \times ( n - k ) }$ . By definition, the matrix (3) is the representation of T with respect to the basis (1). Thus, a decomposition of the space into a direct sum of subspaces, one of which is T-invariant, admits a representation of T in block-triangular form (3).

Exercise 1. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ , where $\mathcal { S } = \mathcal { S } _ { 1 } \ : \dot { + } \mathcal { S } _ { 2 }$ and $\mathcal { S } _ { 1 }$ is T-invariant. Check that the representation of T with respect to a basis in which the basis elements of $\mathcal { S } _ { 1 }$ are in the last places is a lower-block-triangular matrix.

If $\mathcal { S } = \mathcal { S } _ { 1 } \ : + \mathcal { S } _ { 2 }$ and both subspaces $\mathcal { S } _ { 1 }$ and $\mathcal { S } _ { 2 }$ are T-invariant, then a simpler representation of $T$ can be found. Namely, reasoning as before and constructing the representation of T with respect to the basis $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { k } \right.$ $\mathbf { x } _ { k + 1 } , \ldots , \mathbf { x } _ { n } \}$ , in which the first k elements constitute a basis in $\mathcal { S } _ { 1 }$ and the others generate a basis in $\mathcal { S } _ { 2 }$ , we obtain the matrix

$$
A = { \left[ \begin{array} { l l } { A _ { 1 } } & { \ O } \\ { 0 } & { A _ { 2 } } \end{array} \right] } ,\tag{4}
$$

where $A _ { 1 } \in \mathcal { F } ^ { k \times k }$ and $A _ { 2 } \in \mathcal { F } ^ { ( n - k ) \times ( n - k ) }$ Hence, if $T \in { \mathcal { L } } ( { \mathcal { S } } )$ can be decomposed into a direct sum of transformations $T _ { 1 } \in \mathcal { L } ( \mathcal { S } _ { 1 } )$ and $T _ { 2 } \in \mathcal { L } ( \mathcal { S } _ { 2 } )$

that is, $T = T _ { 1 } + T _ { 2 }$ , then there is a representation A of T in a blockdiagonal form (4), where obviously $A _ { 1 }$ and $A _ { 2 }$ are representations of $T _ { 1 }$ and $T _ { 2 }$ , respectively. Note that, conversely, if there exists a matrix A in $\mathcal { A } _ { \mathrm { ~ T ~ } } ^ { 0 }$ of the form (4), then there is a basis in $\mathcal { S }$ such that the Eq. (2) holds and

$$
T ( { \pmb x } _ { j } ) = \sum _ { i = k + 1 } ^ { n } \alpha _ { i j } { \pmb x } _ { i } \qquad j = k + 1 , k + 2 \ldots , n .
$$

In view of Exercise 4.7.4, the subspaces $\mathcal { S } _ { 1 } = \mathtt { s p a n } \{ x _ { j } \} _ { j = 1 } ^ { k }$ and $\mathcal { S } _ { 2 } =$ span $\{ { \pmb x } _ { j } \} _ { j = k + 1 } ^ { n }$ are T-invariant and, obviously, ${ \mathcal { S } } _ { 1 } + { \mathcal { S } } _ { 2 } { \stackrel { . } { = } } { \mathcal { S } } .$ By analogy, the matrix A in (4) is said to be a direct sum of the matrices $A _ { 1 }$ and $A _ { 2 }$ and is written $A = A _ { 1 } \thinspace + \thinspace A _ { 2 }$ . A similar definition and notation, $A = A _ { 1 } \dot { + }$ $A _ { 2 } \div \cdots + A _ { p }$ or, briefly, $\begin{array} { r } { A = \sum _ { i = 1 } ^ { p } { \bf \nabla } \cdot { \bf \nabla } _ { A _ { i } } } \end{array}$ , is given for the direct sum of $p$ matrices. We summarize this discussion.

Theorem 1. A transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ has a representation $A \in \mathcal { A } _ { T } ^ { 0 }$ in block-diagonal form, consisting of p blocks, if and only if T can be decomposed into a direct sum of p linear transformations.

In symbols, if $A \in \mathcal { A } _ { \mathrm { { T } } } ^ { 0 }$ , then $\begin{array} { r } { \pmb { A } = \sum _ { i = 1 } ^ { p } { \pmb { \cdot } } \pmb { A } _ { i } } \end{array}$ if and only if $\begin{array} { r } { \pmb { T } = \sum _ { i = 1 } ^ { p } \pmb { T _ { i } } } \end{array}$ In this case the matrix $A _ { i }$ is the representation of $T _ { i } \left( 1 \leq i \leq p \right)$

Recall that Example 4.7.7 provides an example of a transformation T from $\mathcal { L } ( \mathcal { F } ^ { 2 } )$ that cannot be written $T = T _ { 1 } + T _ { 2 }$ . Hence, there are linear transformations having no block-diagonal representations (with more than one block). Such transformations can be referred to as one-block transformations. In contrast, a particularly important case arises when a transformation from ${ \mathcal { L } } ( { \mathcal { S } } )$ can be decomposed into a direct sum of transformations acting on one-dimensional spaces. Such transformations are called simple. Note the following consequence from Theorem 1 regarding simple transformations.

Theorem 2. Let $\mathcal { A } _ { \mathrm { ~ T ~ } } ^ { 0 }$ denote the equivalence class of matrix representations of the transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ . Any matrix $A \in \mathcal { A } _ { \mathrm { { T } } } ^ { 0 }$ is similar to a diagonal matrix D if and only if T is simple.

By analogy, a matrix $A \in { \mathcal { F } } ^ { n \times n }$ is simple if it is a representation of a simple transformation T acting on an n-dimensional space. Using this notion, the previous result can be partially restated

Theorem 2'. Any matrix $A \in { \mathcal { F } } ^ { n \times n }$ is simple if and only if it is similar to a diagonal matrix D.

The meaning of the diagonal elements in D, as well as the structure of the matrix that transforms A into D, will be revealed later (Theorem 4.10.2), after the effect of a linear transformation on a one-dimensional space is studied.

Exercise 2. Check that any circulant is a simple matrix.

Exercise 3. Show that if the nonsingular matrix A is simple, so are $A ^ { - 1 }$ and adj A.

Exercise 4. Let $A \in { \mathcal { F } } ^ { n \times n }$ and let there be a k-dimensional subspace of ${ \mathcal { F } } ^ { n }$ that is A-invariant $( 1 \leq k < n )$ . Show that the relation

$$
A = P { \left[ \begin{array} { l l } { A _ { 1 } } & { A _ { 3 } } \\ { 0 } & { A _ { 2 } } \end{array} \right] } P ^ { - 1 }\tag{5}
$$

is valid for some $A _ { 1 } \in { \mathcal { F } } ^ { k \times k }$ and a nonsingular $P \in \mathcal { F } ^ { n \times n }$

Hint. Choose a basis ${ \pmb b } _ { 1 } , { \pmb b } _ { 2 } , \dots , { \pmb b } _ { n }$ for ${ \mathcal { F } } ^ { n }$ by extending a basis $\boldsymbol { b } _ { 1 } , \ldots , \boldsymbol { b } _ { k }$ for the A-invariant subspace. Then define P to be the matrix whose columns are ${ \pmb b } _ { 1 } , { \pmb b } _ { 2 } , \dots , { \pmb b } _ { n }$

## 4.9 Eigenvalues and Eigenvectors of a Transformation

Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ . We start the investigation of one-dimensional T-invariant subspaces with a description of their elements in terms of T.

Proposition 1. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and let $\mathcal { S } _ { 0 } \subset \mathcal { S }$ be a T-invariant subspace of dimension 1. Then for all nonzero $\pmb { x } \in \mathcal { S } _ { \mathbf { 0 } }$ there is a scalar $\lambda \in \mathcal { F }$ (independent of x), such that

$$
T ( \mathbf { x } ) = \lambda \mathbf { x } .\tag{1}
$$

PROOF. Since $\mathcal { S } _ { 0 }$ is one-dimensional, it is of the form

$$
\mathcal { S } _ { 0 } = \{ \alpha \mathbf { x } _ { 0 } : \boldsymbol { \theta } \neq \mathbf { x } _ { 0 } \in \mathcal { S } _ { 0 } \mathrm { ~ a n d ~ } \alpha \in \mathcal { F } \} .
$$

The T-invariance of $\mathcal { S } _ { \mathbf { 0 } }$ means $T ( \pmb { x } ) \in \mathcal { S } _ { 0 }$ for every nonzero $\pmb { x } \in \mathcal { S } _ { 0 }$ and, therefore, representing x as $\alpha _ { 0 } \pmb { x } _ { 0 }$ , we have $T ( \alpha _ { 0 } { \pmb x } _ { 0 } ) = \alpha { \pmb x } _ { 0 }$ . Thus, the condition (1) holds for $\lambda = \alpha / \alpha _ { 0 } \ ( \alpha _ { 0 } \neq 0 )$ . If $\mathbf { x } _ { 1 }$ denotes another element from $\mathcal { S } _ { \mathbf { 0 } }$ , then ${ \pmb x } _ { 1 } = \gamma { \pmb x } _ { 0 }$ for some $\gamma \in \mathcal F$ and $T ( \mathbf { x } _ { 1 } ) = \gamma T ( \mathbf { x } _ { 0 } ) = \gamma \lambda \mathbf { x } _ { 0 } = \lambda \mathbf { x } _ { 1 }$ which shows the uniqueness of λ in Eq. (1).

Note that a one-dimensional T-invariant subspace exists provided Eq. (1) holds true for at least one nonzero element x.

Exercise 1. Check that if for some nonzero $\mathbf { \boldsymbol { x } } _ { 0 } \in \mathcal { S } ,$

$$
T ( \mathbf { x _ { 0 } } ) = \lambda \mathbf { x _ { 0 } } ,\tag{2}
$$

then the subspace $\mathcal { S } _ { 0 } = \mathfrak { s p a n } \{ \mathbf { { x } } _ { 0 } \}$ is T-invariant. □

Thus, the nonzero elements x satisfying Eq. (2) play a crucial role in the problem of existence and construction of one dimensional T-invariant subspaces. We need a formal definition. If $T \in { \mathcal { L } } ( { \mathcal { S } } ) ,$ a nonzero element $\pmb { x } _ { 0 } \in \mathcal { S }$ satisfying Eq. (2) is said to be an eigenvector of $T$ corresponding to the eigenvalue λ of $T .$ Thus, the existence of T-invariant subspaces of dimension 1 is equivalent to the existence of eigenvectors of $T$

If we now observe that Eq. (2) is equivalent to

$$
( T - \lambda I ) x _ { 0 } = \theta , \qquad x _ { 0 } \neq \theta ,
$$

we can characterize eigenvalues in another way.

Exercise 2. Show that $\lambda \in \mathcal { F }$ is an eigenvalue of $T$ if and only if the transformation $T - \lambda I$ fails to be invertible. □

The next proposition uses the concept of an algebraically closed field, which is introduced in Appendix 1. For our purposes, it is important to note that C is algebraically closed and R is not.

Proposition 2. Let $\mathcal { S }$ be a inite-dimensional linear space over an algebraically closed field. Then any linear transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ has at least one eigenvalue.

PRooF. By virtue of Exercise 4.1.12, there is a monic polynomial $p ( \lambda )$ with coefficients from $\mathcal { F }$ such that $p ( T ) = 0$ . Since $\mathcal { F }$ is an algebraically closed field, there exists a decomposition of $p ( \lambda )$ into a product of linear factors:

$$
p ( \lambda ) = \sum _ { i = 1 } ^ { l } { ( \lambda - \lambda _ { i } ) } ,
$$

where $\lambda _ { i } \in \mathcal { F } ; ( i = 1 , 2 , . . . , l )$ Then $p ( T ) = \prod _ { i = 1 } ^ { l } \left( T - \lambda _ { i } I \right)$ is the zero transformation, hence at least one of the factors $T \mathrm { ~ - ~ } \lambda _ { i } I \left( 1 \leq i \leq l \right)$ must be noninvertible (see Exercise 4.6.4). Now the required assertion follows from Exercise 2.

Obviously, if x is an eigenvector of $T$ corresponding to $\lambda ,$ then it follows from $T ( \alpha \mathbf { x } ) = \lambda ( \alpha \mathbf { x } )$ for any $\alpha \in \mathcal { F }$ that any nonzero element from the onedimensional space spanned by x is an eigenvector of $T$ corresponding to the same eigenvalue $\lambda .$ This also follows from the results of Proposition 1 and Exercise 2. Moreover, every nonzero linear combination of (linearly dependent or independent) eigenvectors corresponding to the same eigenvalue λ is an eigenvector associated with λ. Indeed, if $T ( \mathbf { x } _ { i } ) = \lambda \mathbf { x } _ { i } \ ( \mathbf { x } _ { i } \neq \mathbf { x } , i =$ $1 , 2 , \ldots , k )$ , then the linearity of T implies

$$
T { \biggl ( } \sum _ { i = 1 } ^ { k } \alpha _ { i } \mathbf { x } _ { i } { \biggr ) } = \sum _ { i = 1 } ^ { k } \alpha _ { i } T ( \mathbf { x } _ { i } ) = \lambda { \biggl ( } \sum _ { i = 1 } ^ { k } \alpha _ { i } \mathbf { x } _ { i } { \biggr ) } ,
$$

and if $\sum _ { i = 1 } ^ { k } { \alpha _ { i } } x _ { i } \neq \pmb { \theta }$ , it is an eigenvector of $T$ corresponding to $\lambda .$

Consider the linear hull $\mathcal { S } _ { 0 }$ of all eigenvectors of T corresponding to λ. In view of the last observation, every nonzero element of this subspace is an eigenvector of T associated with λ and hence it makes sense to call S0 the $T$ $\mathcal { S } _ { 0 }$ eigenspace of T corresponding to the eigenvalue λ of the transformation.

Exercise 3. Let λ denote an eigenvalue of $T \in { \mathcal { L } } ( { \mathcal { S } } )$ . Show that the eigenspace associated with λ coincides with the subspace $\mathbf { K e r } ( T - \lambda I )$

Exercise 4. Find eigenvectors, eigenspaces, and eigenvalues of the transformation $T \in \mathcal { L } ( \mathbb { R } ^ { 3 } )$ defined as follows:

$$
T { \sqrt { \left( { \binom { x _ { 1 } } { x _ { 2 } } } \right) } } = { \left[ \begin{array} { l } { 2 x _ { 1 } } \\ { \ x _ { 1 } } \\ { x _ { 2 } + x _ { 3 } } \end{array} \right] } .
$$

SoLUTION Solving the system $T ( { \boldsymbol { \mathbf { x } } } ) = \lambda { \boldsymbol { \mathbf { \mathit { x } } } } ,$ which becomes in this case

$$
2 x _ { 1 } = \lambda x _ { 1 } , \qquad x _ { 1 } = \lambda x _ { 2 } , \qquad x _ { 2 } + x _ { 3 } = \lambda x _ { 3 } ,
$$

we obtain

$$
\begin{array} { r l r l } & { \lambda = 2 } & & { \mathrm { a n d } \quad } & { x _ { 1 } = 2 x _ { 2 } = 2 x _ { 3 } , } \\ & { \lambda = 0 } & & { \mathrm { a n d } \quad } & { x _ { 1 } = 0 , ~ x _ { 2 } = - x _ { 3 } , } \\ & { \lambda = 1 } & & { \mathrm { a n d } \quad } & { x _ { 1 } = 0 , ~ x _ { 2 } = 0 . } \end{array}
$$

Thus, the transformation has three one-dimensional eigenspaces spanned by the elements $[ 2 , \phantom { - } 1 ] ^ { \mathrm { T } } , [ 0 \phantom { - } 1 ] ^ { \mathrm { T } } , [ 0 \phantom { - } 0 \phantom { - } 1 ] ^ { \mathrm { T } } , [ 0 \phantom { - } 0 \phantom { - } 1 ] ^ { \mathrm { T } }$ and corresponding to the eigenvalues 2, 0, and 1, respectively.

It is' important to note that, in contrast to Exercise 4, a transformation acting on an n-dimensional space may have less than n distinct eigenvalues.

Exercise 5. Check that the transformation $T \in \mathcal { L } ( \mathcal { F } ^ { 2 } )$ defned in Example 4.7.7 has only one eigenvalue, $\lambda = 1$ , associated with the eigenspace spanned by $\begin{array} { r l r } { [ 1 } & { { } 0 ] ^ { \mathbf { T } } . } & { \bigtriangledown } \end{array}$

Furthermore, it may happen that the transformation has two or more linearly independent eigenvectors corresponding to the same eigenvalue, as the next exercise shows.

Exercise 6. Check that the transformation $T \in \mathcal { L } ( \mathcal { F } ^ { 3 } )$ defined by

$$
T { \Bigg ( } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] } { \Bigg ) } = { \left[ \begin{array} { l } { 2 x _ { 1 } + x _ { 3 } } \\ { 2 x _ { 2 } } \\ { 3 x _ { 3 } } \end{array} \right] }
$$

has eigenvalues $\lambda _ { 1 } = \lambda _ { 2 } = 2$ and $\lambda _ { 3 } = 3$ associated with eigenspaces $\mathsf { s p a n } \{ [ \bar { 1 } \quad 0 \quad 0 ] ^ { \mathrm { T } } , [ 0 \quad 1 \quad 0 ] ^ { \mathrm { T } } \}$ and span $\{ [ 1 \mathrm { ~  ~ { ~ 0 ~ } ~ } 1 ] ^ { \boldsymbol { \mathsf { T } } } \}$ , respectively.□

Thus, two eigenvectors of $T$ corresponding to the same eigenvalue may be linearly dependent or independent. However, the situation is clear when the eigenvalues are distinct.

Theorem 1. Eigenvectors corresponding to distinct eigenvalues are linearly independent.

PROOF. Let $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ be the distinct eigenvalues of the transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and let ${ \bf x } _ { 1 } , { \bf x } _ { 2 } , \ldots , { \bf x } _ { s }$ denote corresponding eigenvectors.

Suppose that there exist numbers $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { s }$ such that

$$
\sum _ { i = 1 } ^ { s } \alpha _ { i } \pmb { x } _ { i } = \pmb { \theta } .\tag{3}
$$

To prove that $\alpha _ { i } = 0 ( i = 1 , 2 , \ldots , s )$ , we first multiply both sides of Eq. (3) on the left by $T - \lambda _ { 1 } I ,$ noting that $( T - \lambda _ { 1 } I ) \pmb { x } _ { 1 } = \pmb { \mathscr { 0 } }$ and $T ( { \pmb x } _ { i } ) = \lambda _ { i } { \pmb x } _ { i }$ $i = 1 , 2 , \ldots , s .$ Then

$$
\sum _ { i = 2 } ^ { s } ( \lambda _ { 1 } - \lambda _ { i } ) \alpha _ { i } \pmb { x } _ { i } = \pmb { 0 } .\tag{4}
$$

After premultiplication by $T \mathrm { ~ - ~ } \lambda _ { 2 } I ,$ Eq. (4) becomes

$$
\sum _ { i = 3 } ^ { s } ( \lambda _ { 1 } - \lambda _ { i } ) ( \lambda _ { 2 } - \lambda _ { i } ) \alpha _ { i } x _ { i } = \pmb { \mathscr { 0 } } .
$$

After $s - 1$ such operations we finally have

$$
( \lambda _ { 1 } - \lambda _ { s } ) ( \lambda _ { 2 } - \lambda _ { s } ) \cdot \cdot \cdot ( \lambda _ { s - 1 } - \lambda _ { s } ) \alpha _ { s } { \bf x } _ { s } = \pmb { 0 } .
$$

which implies $\alpha _ { s } = 0$ But the ordering of the eigenvalues and eigenvectors is arbitrary, so we can also prove $\alpha _ { 1 } = \alpha _ { 2 } = \cdot \cdot \cdot = \alpha _ { s - 1 } = 0$ Hence the elements ${ \pmb x } _ { 1 } , { \pmb x } _ { 2 } , \dots , { \pmb x } _ { s }$ are linearly independent.

The spectrum of a transformation $T \in { \mathcal { L } } ( { \mathcal { S } } ) _ { : }$ written $\sigma ( T )$ , is defined as the set of all distinct eigenvalues of T. Note that Proposition 2 can be restated in this terminology as follows: Any linear transformation acting on a finite-dimensional space over an algebraically closed field has a nonempty spectrum. Now Theorem 1 implies a limit to the size of the spectrum.

Corollary 1. The spectrum of a linear transformation acting on an n-dimensional space consists of at most n distinct eigenvalues.

PROOF. If $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and $T$ has k distinct eigenvalues, $k > n =$ dim ${ \mathcal { S } } ,$ then the n-dimensional space $\mathcal { S }$ has more than n linearly independent elements (eigenvectors of $T ,$ in this case). This is a contradiction.

Corollary 2. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and dim ${ \mathcal { S } } = n .$ If T has n distinct eigenvalues, then there is a basis for $\mathcal { S }$ consisting of eigenvectors of T.

In this event we also say that the eigenvectors of T span the space $\mathcal { S }$ or that $T$ has an eigenbasis in S. Note that Exercise 6 shows that a transformation ${ \mathcal { S } } .$ with $n _ { 0 } < n$ distinct eigenvalues can still have an eigenbasis. On the other hand, not every transformation (see Exercise 5) has enough eigenvectors to span the space. It turns out that the existence of an eigenbasis of T in S is $T$ $\mathcal { S }$ equivalent to saying that T is a simple transformation.

Theorem 2. A transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ is simple if and only if it has an eigenbasis in ${ \mathcal { S } } .$

PROOF. If $\left\{ { \pmb x } _ { j } \right\} _ { j = 1 } ^ { n }$ is an eigenbasis in ${ \mathcal { S } } ,$ then, putting ${ \mathcal { S } } _ { i } = \operatorname { s p a n } \{ { \pmb x } _ { i } \}$ for $1 \leq i \leq n ,$ we obtain the decomposition $\begin{array} { r } { T = \sum _ { i = 1 } ^ { n } { \bf \dot { \nabla } } T _ { i } } \end{array}$ , where $T _ { i }$ acts on $\mathcal { S } _ { i }$ and dim $\mathcal { S } _ { i } = 1 ( 1 \leq i \leq n )$ . Hence $T$ is simple. Conversely, let $\begin{array} { r } { \mathcal { S } = \sum _ { i = 1 } ^ { n } \dot { \mathcal { S } } _ { i } } \end{array}$ where subspaces $\mathcal { S } _ { i }$ of dimension one are T-invariant, $i = 1 , 2 , \ldots , n .$ By Proposition 1, any nonzero element of S, say x, is an eigenvector of $\mathcal { S } _ { i }$ $\mathbf { { \boldsymbol { x } } } _ { i } ,$ $T ,$ $1 \leq i \leq n$ . Clearly, the set of all such $x _ { i } ( i = 1 , 2 , \ldots , n )$ gives an eigenbasis of T in ${ \mathcal { S } } .$

In view of Theorem 2, Corollary 2 provides a sufficient (but not necessary) condition for $T$ to be simple (see Exercise 5).

Exercise 7. Check that the transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ is invertible if and only if all eigenvalues of T are nonzero.

Exercise 8. Prove that each T-invariant subspace $\mathcal { S } _ { \mathfrak { d } }$ contains at least one eigenvector of $T$ (the field is algebraically closed).

Hint. Consider $T | _ { \mathcal { S } _ { 0 } }$ and Proposition 2.

Exercise 9. Let T be a simple transformation from ${ \mathcal { L } } ( { \mathcal { S } } )$ . Show that

(a) Im T is spanned by the eigenvectors of T corresponding to the non- $T$ zero eigenvalues,

(b) Im $T n$ Ker ${ \pmb T } = \{ { \pmb \theta } \}$

Exercise 10. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and $\boldsymbol { \sigma } ( T ) = \{ \lambda _ { 1 } , \lambda _ { 2 } , \dots , \lambda _ { s } \}$ . Show that if $\mathcal { S } _ { j }$ denotes the eigenspace of T associated with $\lambda _ { j }$ , then

(a) The sum $\sum _ { j = 1 } ^ { s } \mathcal { S } _ { j }$ is direct ;

(b) The transformation T is simple if and only if

$$
\sum _ { j = 1 } ^ { s } \cdot \mathcal { S } _ { j } = \mathcal { S } . \sqsupset
$$

## 4.10 Eigenvalues and Eigenvectors of a Matrix

Let $A \in { \mathcal { F } } ^ { n \times n }$ . The matrix A can be viewed as a linear transformation acting in ${ \mathcal { F } } ^ { n }$ (see Exercise 4.1.3). Hence we define a nonzero vector $\alpha \in \mathcal { F } ^ { n }$ to be an eigenvector of A corresponding to the eigenvalue λ if

$$
A { \pmb \alpha } = \lambda { \pmb \alpha } , \qquad { \pmb \alpha } \neq { \pmb \theta } .\tag{1}
$$

The set of all distinct eigenvalues of A is called the spectrum of A and is denoted by $\sigma ( A )$ . Observe that the spectrum is invariant under similarity transformations.

Proposition 1. Similar matrices have the same spectrum.

ProoF. Let Eq. (1) hold and suppose $A = P B P ^ { - 1 }$ . Then

$$
B ( P ^ { - 1 } \alpha ) = P ^ { - 1 } A \alpha = \lambda ( P ^ { - 1 } \alpha )
$$

and since α $\neq \pmb { \theta } ,$ the vector $P ^ { - 1 } \alpha$ is an eigenvector of B corresponding to the eigenvalue λ. Hence $\lambda \in \sigma ( B )$ and $\sigma ( A ) \subset \sigma ( B )$ . The reverse inclusion is shown similarly.

Note that, in fact, we proved more.

Proposition 2. If α is an eigenvector of A associated with the eigenvalue $\lambda ,$ then $\alpha ^ { \prime } = P ^ { - 1 } \alpha$ is an eigenvector of the matrix $B = P ^ { - 1 } A P$ corresponding to the same eigenvalue λ.

Thus, all matrices from the equivalence class  of matrix representations $\mathcal { A } _ { T } ^ { 0 }$ for a transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ have the same eigenvalues associated with eigenvectors of the form $P ^ { - 1 } \mathbf { x } ,$ where P is a transforming matrix. Hence, in particular, the spectrum of the matrices from $\mathcal { A } _ { T } ^ { 0 }$ is uniquely determined by the transformation T. Consequently, a strong connection between the spectrum of T and the representations of T is to be expected.

Theorem 1. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and let $\mathcal { A } _ { \mathrm { ~ T ~ } } ^ { 0 }$ denote the corresponding equivalence class of matrix representations for T. Then

$$
\sigma ( T ) = \sigma ( A )\tag{2}
$$

for any $A \in \mathcal { A } _ { T } ^ { 0 }$

PRooF. In view of Proposition 1; it suffices to show that Eq. (2) holds for at least one matrix A from $\mathcal { A } _ { T } ^ { 0 }$ . Let $\lambda \in \sigma ( T )$ and

$$
T ( \mathbf { x } ) = \lambda \mathbf { x } , \qquad \mathbf { x } \neq { \pmb \theta } .\tag{3}
$$

If $\mathbf { \bar { \alpha } } _ { \mathbf { \alpha } } \in \mathcal { F } ^ { n }$ is a representation of x with respect to the same basis in $\mathcal { S }$ in which $A$ is a representation of $T ,$ then Theorem 4.2.2 and the isomorphism between elements and their representations show that the relation (3) is equivalent to $A \pmb { \alpha } = \lambda \pmb { \alpha } .$ Note that ${ \pmb { \alpha } } \neq { \pmb { \theta } }$ since $\pmb { x } \neq \pmb { \theta }$ and, therefore, $\lambda \in \sigma ( A )$

Observe that we have also found a relation between the eigenvectors of a matrix and the eigenvectors of the transformation which the matrix represents.

Proposition 3. An element $\boldsymbol { x } \in \mathcal { S }$ is an eigenvector of $T \in { \mathcal { L } } ( { \mathcal { S } } )$ associated with $\lambda \in \sigma ( T )$ if and only if the representation $\alpha \in \mathcal { F } ^ { n }$ of x with respect to a basis in $\mathcal { S }$ is an eigenvector of the matrix representation of T with respect to the same basis.

By varying the bases in ${ \mathcal { S } } ,$ we obtain a set of vectors $\{ P ^ { - 1 } \alpha \}$ det $P \neq 0 \}$ that are eigenvectors of the corresponding representations of $T$ (see Proposition 2). Note also that Theorem 1 and Proposition 3 provide an easy transition from the eigenvalues and eigenvectors of a transformation to those of matrices. In particular, they admit an analogous reformulation for matrices of the results concerning eigenvalues and eigenvectors of transformations. For instance, recalling that the representations of linearly independent elements also are linearly independent (see Exercise 3.7.2), we obtain an analog of Theorem 4.9.1.

Proposition 4. Eigenvectors of a matrix corresponding to distinct eigenvalues are linearly independent.

We now use this together with Proposition 4.9.2 and Theorem 4.9.2.

Proposition 5. The spectrum $\sigma ( A )$ of a matrix $\ b { A } \in \mathbb { C } ^ { n \times n }$ is not empty and consists of at most n distinct eigenvalues. If A has n distinct eigenvalues, then it is simple.

We can now complement the statement of Theorem $4 . 8 . 2 ^ { \prime }$ by indicating the structure of the diagonal matrix D and the corresponding transforming matrix P.

Theorem 2. Let $A \in { \mathcal { F } } ^ { n \times n }$ be a simple matrix and let D be the diagonal matrix occurring in Theorem 4.8.2' :

$$
A = P D P ^ { - 1 } , \qquad \operatorname* { d e t } P \neq 0 .\tag{4}
$$

Then $D = \mathrm { d i a g } [ \lambda _ { j } ] _ { j = 1 } ^ { n }$ with $\lambda _ { j } \in \sigma ( A ) , j = 1 , 2 , \ldots , n ,$ and

$$
P = [ { \pmb x } _ { 1 } \quad { \pmb x } _ { 2 } \quad \cdot \cdot \cdot \quad { \pmb x } _ { n } ] ,
$$

in which $\mathbf { { x } } _ { j } \left( 1 \leq j \leq n \right)$ is an eigenvector of A corresponding to the eigenvalue $\lambda _ { j } ( 1 \leq j \leq n )$

ProoF. Rewriting Eq. (4) in the form $A P = P D$ and comparing the columns of the matrices $A P$ and PD, it is easily found that

$$
A { \boldsymbol { \mathbf { \mathit { x } } } } _ { j } = \lambda _ { j } { \boldsymbol { \mathbf { \mathit { x } } } } _ { j } , \qquad j = 1 , 2 , \ldots , n ,\tag{5}
$$

where $\pmb { x } _ { j } \ ( 1 \leq j \leq n )$ is the jth column of P and $\lambda _ { j } ( 1 \leq j \leq n )$ is the jth diagonal element of D. Since P is nonsingular, none of its columns can be the zero element in ${ \mathcal { F } } ^ { n }$ and hence $x _ { j }$ in (5) is an eigenvector of A corresponding to $\lambda _ { j }$ .■

Theorem 2 can be reformulated in an illuminating way. Define the matrix $Q = ( P ^ { - 1 } ) ^ { \mathbf { T } }$ and write $Q = [ y _ { \pm } { \textbf { \textrm { y } } } _ { 2 } \ldots { \textbf { \textrm { y } } } _ { n } ]$ .Then $Q ^ { \mathsf { T } } \bar { P } = P ^ { - 1 } P = I$ and, comparing elements, we obtain

$$
y _ { j } ^ { \mathsf { T } } x _ { k } = \delta _ { j k }\tag{6}
$$

for $1 \leq j , k \leq n$ Note that in the sense of Section 3.13, the systems $\left\{ x _ { j } \right\} _ { j = 1 } ^ { n }$ and $\left\{ \overline { { \pmb { y } } } _ { j } \right\} _ { j = 1 } ^ { n }$ are biorthogonal with respect to the standard inner product in C".

Take transposes in Eq. (4) and we have $A ^ { \boldsymbol { \mathsf { T } } } = Q D Q ^ { - 1 }$ , so that

$$
A ^ { \mathbf { \boldsymbol { r } } } Q = Q D .
$$

This implies $A ^ { \mathrm { T } } y _ { j } = \lambda _ { j } y _ { j } { \mathrm { f o r } } j = 1 , 2 , \ldots , n .$ Thus, the columns of $( P ^ { - 1 } ) ^ { \mathbf { T } }$ are eigenvectors for A™. They are also known as left eigenvectors of A since they satisfy $\mathbf { \boldsymbol { y } } _ { j } ^ { \mathbf { T } } \boldsymbol { A } = \lambda _ { j } \mathbf { \boldsymbol { y } } _ { j } ^ { \mathbf { T } }$

Now, to recast Theorem 2, observe that Eq. (4) implies, using Eq. (1.3.6),

$$
\begin{array} { c } { { \displaystyle { \cal A } = P D Q ^ { \mathrm { T } } = [ { \bf x } _ { 1 } \quad { \bf x } _ { 2 } \quad \cdots \quad { \bf x } _ { n } ] \left[ \begin{array} { c } { { \lambda _ { 1 } y _ { 1 } ^ { \mathrm { T } } } } \\ { { \vdots } } \\ { { \lambda _ { n } y _ { n } ^ { \mathrm { T } } } } \end{array} \right] } }  \\ { { { \mathrm { } } } } \\ { { { \mathrm { } = \displaystyle { \sum _ { j = 1 } ^ { n } \lambda _ { j } { \bf x } _ { j } y _ { j } ^ { \mathrm { T } } } . } } } \end{array}
$$

Thus, A is expressed as a sum of matrices of rank one (or zero if $\lambda _ { j } = 0 )$ and each of these is defined in terms of the spectral properties of A, that is, in terms of its eigenvalues, eigenvectors, and left eigenvectors. Consequently the next result is called a spectral theorem.

Theorem 3. Let $\pmb { A } \in \mathcal { F } ^ { n \times n }$ be a simple matrix with eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { n }$ and associated eigenvectors ${ \pmb x } _ { 1 } , { \pmb x } _ { 2 } , \ldots , { \pmb x } _ { n }$ . Then there are left eigenvectors $y _ { 1 } , y _ { 2 } , \ldots , y _ { n } f o r$ which $\begin{array} { r } { \mathbf { y } _ { j } ^ { \mathsf { T } } x _ { k } = \delta _ { j k } , 1 \leq j k \leq n , } \end{array}$ and

$$
A = \sum _ { j = 1 } ^ { n } \lambda _ { j } x _ { j } y _ { j } ^ { \operatorname { T } } .\tag{7}
$$

Exercise 1. Consider a matrix $\pmb { A } \in \mathcal { F } ^ { n \times n }$ with eigenvectors $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ corresponding to the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ , respectively. Show that any subspace of $\mathcal { F } ^ { n }$ generated by a set of eigenvectors

$$
x _ { j _ { 1 } } , x _ { j _ { 2 } } , \dotsc , x _ { j _ { k } } ( 1 \leq j _ { 1 } < j _ { 2 } < \dots < j _ { k } \leq n )
$$

of A is A-invariant.

Exercise 2. Show that the spectrum of the square matrix

$$
A = { \left[ \begin{array} { l l } { A _ { 1 } } & { A _ { 3 } } \\ { 0 } & { A _ { 2 } } \end{array} \right] } ,
$$

where $A _ { 1 }$ and $A _ { 2 }$ are square, is the union of the spectra of $\pmb { A } _ { 1 }$ and $A _ { 2 }$

Exercise 3. Check that the matrix $\pmb { A } \in \mathcal { F } ^ { n \times n }$ is singular if and only if it has a zero eigenvalue.

Exercise 4. Let $\lambda \in \sigma ( A ) .$ , A be nonsingular, and $A \mathbf { x } = \lambda \mathbf { x } , \mathbf { x } \neq \pmb { 0 } .$ Prove that $\lambda ^ { - 1 }$ is an eigenvalue of $A ^ { - 1 }$ associated with eigenvector x. □

## 4.11 The Characteristic Polynomial

We now bring the ideas of the theory of determinants to bear on the problem of finding the eigenvalues of an $n \times n$ matrix $A \in { \mathcal { F } } ^ { n \times n }$ As in the situation for transformations (see Exercise 4.9.3), it is easily shown that $\lambda \in \sigma ( A )$ if and only if the matrix $\lambda I - A$ is not invertible, or equivalently (Theorem 2.6.2),

$$
\operatorname* { d e t } ( \lambda I - A ) = 0 .\tag{1}
$$

Observe now that the expression on the left side of Eq. (1) is a monic polynomial of degree n in $\lambda$

$$
\operatorname* { d e t } ( \lambda I - A ) = c _ { 0 } + c _ { 1 } \lambda + \cdot \cdot \cdot + c _ { n - 1 } \lambda ^ { n - 1 } + c _ { n } \lambda ^ { n } , \qquad c _ { n } = 1 .\tag{2}
$$

The polynomial $\begin{array} { r } { c ( \lambda ) \triangleq \sum _ { i = 0 } ^ { n } c _ { i } \lambda ^ { i } } \end{array}$ in Eq. (2) is referred to as the characteristic polynomial of the matrix A. These ideas are combined to give Theorem 1.

Theorem 1. A scalar $\lambda \in \mathcal { F }$ is an eigenvalue of $\pmb { A } \in \mathcal { F } ^ { n \times n }$ if and only if λ is a zero of the characteristic polynomial of A.

The significance of this result is that the evaluation of eigenvalues of a matrix is reduced to finding the zeros of a scalar polynomial and is separated from the problem of finding (simultaneously) its eigenvectors.

Exercise 1. Check that the eigenvalues of the matrix

$$
A = \left[ { \begin{array} { r r r } { 2 } & { 0 } & { 0 } \\ { 1 1 } & { 4 } & { 5 } \\ { 7 } & { - 1 } & { - 2 } \end{array} } \right]
$$

are $\lambda _ { 1 } = 2 , \lambda _ { 2 } = 3 , \lambda _ { 3 } = - 1$

Exercise 2. Show that the diagonal elements of a triangular matrix are its eigenvalues.□

Note that if the field $\mathcal { F }$ is algebraically closed (for definition and discussion see Appendix 1), then all the zeros of the scalar polynomial $c ( \lambda )$ belong to F. Hence the spectrum of any $A \in { \mathcal { F } } ^ { n \times n }$ is nonempty and consists of at most n points; properties that are already familiar. They are established in Theorem 4.10.5 and, as indicated in Theorem 4.10.1, are also properties of the underlying linear transformation.

Observe also that, if $A = P B P ^ { - 1 }$ , then

$$
c _ { A } ( \lambda ) = \operatorname * { d e t } ( \lambda I - A ) = \operatorname * { d e t } ( P ( \lambda I - B ) P ^ { - 1 } ) = \operatorname * { d e t } ( \lambda I - B ) = c _ { B } ( \lambda ) .
$$

Thus the characteristic polynomial is invariant under similarity and hence all matrices in the equivalence class $\mathcal { A } _ { T } ^ { 0 }$ have the same characteristic polynomial. In other words, this polynomial is a characteristic of the transformation T itself and therefore can be referred to as the characteristic polynomial of the transformation.

Proceeding to an investigation of the coefficients of the characteristic polynomial of a matrix A or, equivalently, of a transformation T having A as a representation, we first formulate a lemma.

Lemma 1. If $A \in { \mathcal { F } } ^ { n \times n }$ and distinct columns $i _ { 1 } , i _ { 2 } , \ldots , i _ { r } ( 1 \leq r < n )$ of A are the unit vectors $e _ { i _ { 1 } } , e _ { i _ { 2 } } , \ldots , e _ { i _ { r } }$ , then det A is equal to the principal minor of A obtained by striking out rows and columns $i _ { 1 } , i _ { 2 } , \ldots , i _ { r }$

ProoF. Expanding det A by column $i _ { 1 } ,$ we obtain

$$
\begin{array} { r l } { \operatorname* { d e t } A = ( - 1 ) ^ { i _ { 1 } + i _ { 1 } } A \binom { 1 } { 1 } \quad 2 \quad \cdots } & { i _ { 1 } - 1 \quad i _ { 1 } + 1 \quad \cdots \quad n } \\ { \qquad 2 \quad \cdots } & { i _ { 1 } - 1 \quad i _ { 1 } + 1 \quad \cdots } & { n } \end{array} ,
$$

Now evaluate this minor by expansion on the column numbered $i _ { 2 }$ . It is found that det A is the principal minor of A obtained by striking out rows and columns $i _ { 1 }$ and $i _ { 2 }$ . Continuing in this way with columns $i _ { 3 } , i _ { 4 } , \dots , i _ { r } ,$ the result is obtained.

Theorem 2. Let $A \in { \mathcal { F } } ^ { n \times n }$ and let $\begin{array} { r } { c ( \lambda ) = \sum _ { i = 0 } ^ { n } c _ { i } \lambda ^ { i } } \end{array}$ denote the characteristic polynomial of A. Then the scalar $c _ { r } ( 0 \leq r < n )$ is equal to the sum of all principal minors of order $n - r$ of A multiplied by $( - 1 ) ^ { n - r }$

PROOF. Let ${ \mathfrak { a } } _ { 1 } , { \mathfrak { a } } _ { 2 } , \ldots , { \mathfrak { a } } _ { n }$ be the columns of A. Then, using the unit vectors in ${ \mathcal { F } } ^ { n }$ , we write

$$
( - 1 ) ^ { n } c ( \lambda ) = \operatorname * { d e t } ( A - \lambda I ) = \operatorname * { d e t } [ a _ { 1 } - \lambda e _ { 1 } \quad a _ { 2 } - \lambda e _ { 2 } \quad \cdots \quad a _ { n } - \lambda e _ { n } ] .
$$

Since the determinant is a homogeneous linear function of its columns, we can express the latter determinant as the sum of $2 ^ { n }$ determinants of matrices having columns of the form $\pmb { a } _ { i } \ o \pmb { r } - \lambda \pmb { e } _ { i }$ . Let us select those determinants involving just r columns of the form $- \lambda e _ { i }$ for some i. There are precisely $C _ { n , \ l }$ , of these obtained by replacing r of the columns of A by $( - \lambda ) \times$ (a unit vector) in every possible way. Thus, from the lemma, each of these determinants is of the form $( - \lambda ) ^ { r }$ times a principal minor of $A$ of order $n - r .$ Furthermore, every principal minor of order $n - r$ appears in this summation. The result follows on putting $r = 0 , 1 , 2 , \ldots , n - 1$

In particular, by setting $r = n - 1$ and $r = 0$ in Theorem $^ { 2 , }$ we obtain

$$
- c _ { n - 1 } = \sum _ { i = 1 } ^ { n } a _ { i i } = \mathrm { t r } A \qquad \mathrm { a n d } \qquad c _ { 0 } = ( - 1 ) ^ { n } \mathrm { d e t } A ,
$$

respectively. The last result can be obtained directly by putting $\lambda = 0$ in the definition of the characteristic polynomial. A fundamental result of the theory of scalar polynomials tells us that $( - 1 ) ^ { n - r } c _ { r }$ is also the sum of all products of the n zeros of $c ( \lambda )$ taken $n - r$ at a time $( 0 \leq r < n )$ . Thus, if $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ are eigenvalues of A (not necessarily distinct) then Theorem 2 gives the important special cases:

$$
\operatorname { t r } A = \sum _ { r = 1 } ^ { n } \lambda _ { r } \qquad \mathrm { a n d } \qquad \operatorname* { d e t } A = \prod _ { r = 1 } ^ { n } \lambda _ { r } .\tag{3}
$$

We have seen that any $n \times n$ matrix has a monic polynomial for its characteristic polynomial. It turns out that, conversely, if c(λ) is a monic polynomial $c ( \lambda )$ over $\mathcal { F }$ of degree $n ,$ then there exists a matrix $A \in \mathcal { F } ^ { n \times n }$ such that its characteristic polynomial is $c ( \lambda )$

Exercise 3. Check that the n × n companion matrix

$$
{ \left[ \begin{array} { l l l l l } { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 1 } & { \ddots } & { \vdots } \\ { \vdots } & { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { - c _ { 0 } } & { - c _ { 1 } } & { - c _ { 2 } } & { \cdots } & { - c _ { n - 1 } } \end{array} \right] }
$$

has $\begin{array} { r } { c ( \lambda ) = \lambda ^ { n } + \sum _ { i = 0 } ^ { n - 1 } c _ { i } \lambda ^ { i } } \end{array}$ for its characteristic polynomial. (See Exercise $2 . 2 . 9 . ) \ \square$

The last result implies, in particular, that for any set $\sigma _ { 0 }$ of k points in C $( 1 \leq k \leq n )$ , there is an $n \times n$ matrix A such that $\sigma ( A ) = \sigma _ { 0 }$

It was mentioned earlier that similar matrices have the same characteristic polynomial. The converse is not true.

Exercise 4. Check that the matrices

$$
{ \begin{array} { l l l l l } { { \Bigl [ } 1 } & { 2 { \Bigr ] } } & { \quad \mathrm { a n d } } & { } & { { \Bigl [ } 1 } & { 0 { \Bigr ] } } \\ { 0 } & { 1 } & { } & { { \bigl \{ } 0 } } & { 1 { \bigr \} } \end{array} }
$$

are not similar and that they have the same characteristic polynomial, $c ( \lambda ) = ( \lambda - 1 ) ^ { 2 }$

Exercise 5. Prove that two simple matrices are similar if and only if their characteristic polynomials coincide.

## Exercise 6. Show that

(a) The characteristic polynomial of the matrix

$$
\left[ { \begin{array} { l l } { A _ { 1 } } & { A _ { 3 } } \\ { 0 } & { A _ { 2 } } \end{array} } \right]
$$

is equal to the product of the characteristic polynomials of $A _ { 1 }$ and $A _ { 2 }$

(b) If $\mathcal { S } _ { 0 }$ is T-invariant, then the characteristic polynomial of $T \vert _ { \mathcal { S } _ { 0 } }$ divides the characteristic polynomial of T.

An important relation between the eigenvalues of the matrices A and $p ( A )$ where $p ( \lambda )$ is a scalar polynomial, is considered next.

Theorem 3. Let $\lambda _ { 0 }$ be an eigenvalue of $A \in { \mathcal { F } } ^ { n \times n }$ and let $p ( \lambda )$ be any scalar polynomial. Then $p ( \lambda _ { 0 } )$ is an eigenvalue of $p ( A )$

ProoF. The reader can easily verify, using the commutativity of powers of A, that

$$
p ( A ) - p ( \lambda _ { 0 } ) I = ( A - \lambda _ { 0 } I ) q ( A )
$$

for some polynomial $q ( \lambda )$ . Thus det $( A - \lambda _ { 0 } I ) = 0$ yields det $( p ( A ) - p ( \lambda _ { 0 } ) I ) = 0$ and the required result follows from Theorem 1.

Exercise 7. Prove that the eigenvalues of an idempotent matrix are all equal to zero or one. Using Theorems 4.5.6 and 4.9.2, show that an idempotent is a simple matrix.

Exercise 8. Prove that the eigenvalues of nilpotent matrices are all equal to zero and that nonzero nilpotent matrices cannot be simple.

Exercise 9. Verify that the eigenvalues of A and $A ^ { \boldsymbol { \mathsf { T } } }$ coincide, while the eigenvalues of A and $A ^ { * }$ are complex conjugates.

Exercise 10. Show that the eigenvalues of the real symmetric matrix

$$
\left[ { \begin{array} { r r r } { 1 3 } & { 4 } & { - 2 } \\ { 4 } & { 1 3 } & { - 2 } \\ { - 2 } & { - 2 } & { 1 0 } \end{array} } \right]
$$

are 9, 9, and 18.

Exercise 11. Show that the following matrices are simple and find corresponding matrices D and P as described in Theorem 4.10.2:

(i)

$$
{ \left[ \begin{array} { l l l } { 1 } & { - 1 } & { 0 } \\ { 2 } & { 3 } & { 2 } \\ { 1 } & { 1 } & { 2 } \end{array} \right] } ,
$$

(ii)

$$
\left[ { \begin{array} { r r r } { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 1 } \end{array} } \right] ,
$$

(iii)

$$
\left[ \begin{array} { c c c } { { 5 } } & { { 8 } } & { { 1 6 } } \\ { { 4 } } & { { 1 } } & { { 8 } } \\ { { - 4 } } & { { - 4 } } & { { - 1 1 } } \end{array} \right] .
$$

Hint. Show first that the characteristic polynomials are

$$
( \lambda - 1 ) ( \lambda - 2 ) ( \lambda - 3 ) , ~ ( \lambda - 1 ) ( \lambda ^ { 2 } + 1 ) , ~ \mathrm { a n d } ~ ( \lambda - 1 ) ( \lambda + 3 ) ^ { 2 } ,
$$

respectively.□

## 4.12 The Multiplicities of an Eigenvalue

Let $\pmb { A } \in \mathcal { F } ^ { n \times n }$ be a representation of the transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ , and let $\mathcal { F }$ be algebraically closed. Then the characteristic polynomial $c ( \lambda )$ of A (or of T) can be factorized into a product of n linear factors:

$$
c ( \lambda ) = \prod _ { i = 1 } ^ { n } ( \lambda - \lambda _ { i } ) ,\tag{1}
$$

where $\lambda _ { i } \in \sigma ( A ) , i = 1 , 2 , \ldots , n .$ It may happen that some of these eigenvalues are equal, and we define the algebraic multiplicity of the eigenvalue $\lambda _ { i }$ of A (or of T) to be the number of times the factor $( \lambda - \lambda _ { i } )$ appears in Eq. (1). In other words, the algebraic multiplicity of $\lambda _ { i } \in \sigma ( A )$ is its multiplicity as a zero of the characteristic polynomial.

We have seen that $\lambda _ { 0 } \in \sigma ( A )$ if and only if $\operatorname { K e r } ( A - \lambda _ { 0 } I ) \neq \{ \pmb { \theta } \}$ , and the geometric multiplicity of the eigenvalue $\lambda _ { 0 }$ of A (or of T) is defined as the dimension of the subspace $\operatorname { K e r } ( A - \lambda _ { 0 } I )$ . Note that by referring to the subspace $\mathsf { K e r } ( A - \lambda I )$ as the eigenspace of the matrix A associated with the eigenvalue λ, we can restate for matrices all the results concerning eigenspaces for transformations. We also point out that scalars that fail to be eigenvalues of A can be viewed as having zero (algebraic and geometric)

multiplicities. However, the algebraic and geometric multiplicities are not generally equal.

Example 1. Consider the matrix

$$
A = \left[ { \begin{array} { r r } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} } \right] .
$$

The characteristic polynomial $c ( \lambda )$ of A is $c ( \lambda ) = \lambda ^ { 2 }$ and therefore the algebraic multiplicity of the zero eigenvalue $\lambda _ { 0 } = 0$ is 2. On the other hand, dim $( \operatorname { K e r } ( A - \lambda _ { 0 } I ) ) = \dim ( \operatorname { K e r } A ) = 1$ and the geometric multiplicity of $\lambda _ { 0 } = 0 \mathrm { i s } 1 . \ \bigtriangledown$

Theorem 1. The geometric multiplicity of an eigenvalue does not exceed its algebraic multiplicity

ProOF. Let λ be an eigenvalue of the $n \times n$ matrix A and let

$$
m _ { \lambda } = \dim ( \operatorname { K e r } ( A - \lambda I ) ) .
$$

If r denotes the rank of $A - \lambda I$ then, by Eq. (4.5.2), we have $r = n - m _ { \lambda }$ and all the minors of $A - \lambda I$ of order greater than $n - m _ { \lambda }$ are zero. Hence if $\begin{array} { r } { \tilde { c } ( \mu ) = \sum _ { i = 0 } ^ { n } \tilde { c } _ { i } \mu ^ { i } } \end{array}$ is the characteristic polynomial of $A - \lambda I ,$ Theorem 4.11.2 implies that $\tilde { c } _ { 0 } = \tilde { c } _ { 1 } = \cdot \cdot \cdot = \tilde { c } _ { m _ { \lambda } - 1 } = 0 .$ Therefore

$$
\tilde { c } ( \mu ) = \sum _ { i = m _ { \lambda } } ^ { n } \tilde { c } _ { i } \mu ^ { i }
$$

and must have a zero of multiplicity greater than or equal to $m _ { \lambda }$ . It remains to observe that, if $c ( \mu )$ is the characteristic polynomial of A, then

$$
c ( \mu ) = \widetilde { c } ( \mu - \lambda ) . \quad \equiv
$$

Denote by $\sum a$ (respectively, $\sum g )$ the sum of the algebraic (respectively, geometric) multiplicities of the eigenvalues of an $n \times n$ complex matrix A. Then Theorem 1 implies

$$
\begin{array} { r } { \sum _ { g } \le \sum _ { a } = n . } \end{array}\tag{2}
$$

In the case $\sum g = n ,$ the relations (2) imply that the algebraic and geometric multiplicities of each eigenvalue of A must coincide. On the other hand, if we use Proposition 4.10.4, the equality $\sum _ { \theta } = n$ also means that the space ${ \mathcal { F } } ^ { n }$ can be spanned by nonzero vectors from the eigenspaces of the matrix, that is, by their eigenvectors. Hence if $\sum _ { \mathbf { \boldsymbol { \theta } } } = \boldsymbol { n } ,$ then the matrix A is simple. It is easily seen that the converse also holds and a criterion for a matrix to be simple is obtained.

Theorem 2. Any matrix A with entries from an algebraically closed field is simple if and only if the algebraic and geometric multiplicities of each eigenvalue of A coincide.

## 4.13 First Applications to Differential Equations

Consider a system of ordinary differential equations with constant coefficients of the following form:

$$
{ \begin{array} { r l } & { { \dot { x } } _ { 1 } = a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 1 n } x _ { n } , } \\ & { } \\ & { { \dot { x } } _ { 2 } = a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { 2 n } x _ { n } , } \\ & { } \\ & { \quad \vdots } \\ & { { \dot { x } } _ { n } = a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n n } x _ { n } , } \end{array} }
$$

where $x _ { 1 } , \ldots , x _ { n }$ are functions of the independent variable $t ,$ the symbol $\dot { x } _ { j }$ denotes the derivative of $\boldsymbol { x } _ { j }$ with respect to $t ;$ and the coefficients $a _ { i j }$ are independent of t. We can obviously abbreviate this set of equations to one matrix equation:

$$
{ \dot { { \mathbf { x } } } } ( t ) = A { \mathbf { x } } ( t ) ,\tag{1}
$$

where $\pmb { x } ( t ) = [ \pmb { x } _ { 1 } \quad \pmb { x } _ { 2 } \quad \cdot \cdot \cdot \quad \pmb { x } _ { n } ] ^ { \mathrm { T } }$ and $\begin{array} { r } { A = [ a _ { i j } ] _ { i , j = 1 } ^ { n } . } \end{array}$ Note that we may write x or x instead of $\pmb { x } ( t )$ or ${ \dot { \mathbf { x } } } ( t )$ if their dependence on t is clear from the context.

If A has at least one eigenvalue, we can easily demionstrate the existence of a solution of ${ \dot { \pmb { x } } } = A { \pmb { x } }$ . We look for a solution of the form $\begin{array} { r } { { \bf x } ( t ) = { \bf x } _ { 0 } e ^ { \lambda _ { 0 } t } , } \end{array}$ where $\pmb { x _ { 0 } }$ and $\lambda _ { 0 }$ are independent of t. Then ${ \dot { \pmb x } } = \lambda _ { 0 } { \pmb x }$ and Eq. (1) can be written $( A - \lambda _ { 0 } I ) \mathbf { x } _ { 0 } = \pmb { 0 }$ . Thus, if we choose $\pmb { x } _ { 0 }$ to be a (right) eigenvector of A with eigenvalue $\lambda _ { 0 }$ , then ${ \pmb x } ( t )$ is indeed a solution. Furthermore, if $A \in \mathbb { C } ^ { n , \times n } ,$ , such a solution always exists because every A then has at least one eigenvalue with an associated (right) eigenvector.

Proposition 1. The vector-valued function $x ( t ) = x _ { 0 } e ^ { \lambda _ { 0 } t }$ is a solution of $E q .$ (1) $i f$ and only $i f \lambda _ { 0 }$ is an eigenvalue of A associated with an eigenvector $\pmb { x _ { 0 } }$

Hence the problem of determining the eigenvalues and eigenvectors of a matrix is closely related to finding the solutions of the corresponding system of differential equations. Can we characterize the solution set $\mathcal { S }$ of all solutions of Eq. (1)? It is easily verified that $\mathcal { S }$ is a linear space and it will be shown later that the dimension of this space is n (see Section 7.10). Here, the result will be proved for simple matrices only. The first exercise shows how a subspace of $\mathcal { S }$ can always be generated.

Exercise 1. Let $A \in \mathbb { C } ^ { n \times n }$ and let $\mathcal { S }$ denote the solution space of Eq. (1). If $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ are the distinct eigenvalues of A associated with the eigenvectors $\pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \dots , \pmb { x } _ { s }$ , respectively, show that the set

$$
\mathcal { S } _ { 0 } = \mathtt { s p a n } \{ \mathbf { x } _ { 1 } e ^ { \lambda _ { 1 } t } , \mathbf { x } _ { 2 } e ^ { \lambda _ { 2 } t } , \dots , \mathbf { x } _ { s } e ^ { \lambda _ { s } t } \}
$$

is a linear subspace in $\mathcal { S }$ of dimension s.

Hint. Observe that the linear independence of $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { s }$ implies that of $\pmb { x } _ { 1 } e ^ { \lambda _ { 1 } t } , \pmb { x } _ { 2 } e ^ { \lambda _ { 2 } t } , \dots , \pmb { x } _ { s } e ^ { \lambda _ { s } t }$ and use Proposition 1.

For a simple matrix A we can say rather more than the conclusion of Exercise 1, for in this case we have a basis for $\mathbb { C } ^ { n }$ consisting of eigenvectors of A. In fact, if $\mathbf { { \dot { x } } } _ { 1 } , \dots , \mathbf { { \dot { x } } _ { n } }$ is such a basis with associated eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { n }$ respectively, it is easily verified that the n vector-valued functions $x _ { j } e ^ { \lambda _ { j } t } ;$ are solutions, $j = 1 , 2 , \dots , n ,$ and they generate an n-dimensional subspace of solutions, $\mathcal { S } _ { 0 }$ . We are to show that $\mathcal { S } _ { 0 }$ is in fact, all of $\mathcal { S }$

More generally, let us first consider the inhomogeneous system

$$
{ \dot { \mathbf { x } } } ( t ) = A { \mathbf { x } } ( t ) + f ( t )\tag{2}
$$

(where $\pmb { f } ( t )$ is a given integrable function). It will be shown that Eq. (2) can be reduced to a set of n independent scalar equations. To see this, let eigenvectors, $\pmb { x } _ { 1 } , \ldots , \pmb { x } _ { n }$ and left eigenvectors $y _ { 1 } , \ldots , y _ { n }$ be defined for A as required by Theorem 4.10.3. If $P = [ { \pmb x } _ { 1 } \quad \cdots \quad { \pmb x } _ { n } ]$ and $Q = [ { \mathfrak { y } } _ { 1 } \quad \cdots \quad { \mathfrak { y } } _ { n } ] .$ then the biorthogonality properties of the eigenvectors (see Eq. (4.10.6)) are summarized in the relation

$$
Q ^ { \boldsymbol { \mathsf { T } } } \ P = I ,\tag{3}
$$

and the representation for A itself (see Eq. (4.10.7)) is

$$
A = P D Q ^ { \mathbf { T } } ,\tag{4}
$$

where $D = \mathrm { d i a g } [ \lambda _ { 1 } , . . . , \lambda _ { n } ] ,$

The reduction of the system (2) to a set of scalar equations is now accomplished if we substitute Eq. (4) in Eq. (2), multiply on the left by $Q ^ { \boldsymbol { \mathsf { T } } } .$ , and take advantage of Eq. (3) to obtain

$$
Q ^ { \mathsf { T } } \dot { \mathbf { x } } ( t ) = D Q ^ { \mathsf { T } } \mathbf { x } ( t ) + Q ^ { \mathsf { T } } f ( t ) .
$$

Introducing new variables $z _ { j } ( t ) = y _ { j } ^ { \mathrm { T } } x ( t )$ for $j = 1 , 2 , \dots , n$ and transformed prescribed functions $\phi _ { j } ( t ) \stackrel { \cdot } { = } y _ { j } ^ { \operatorname { T } } f ( t )$ , the equations become $\dot { z } ( t ) = D z ( t ) +$ $\varphi ( t )$ , where

$$
\begin{array} { r } { z ( t ) = [ z _ { 1 } ( t ) \quad z _ { 2 } ( t ) \quad \cdot \cdot \quad z _ { n } ( t ) ] ^ { \mathrm { T } } , \ : \ : \ : \ : \varphi ( t ) = [ \varphi _ { 1 } ( t ) \quad \varphi _ { 2 } ( t ) \quad \cdot \cdot \cdot \quad \varphi _ { n } ( t ) ] ^ { \mathrm { T } } . } \end{array}
$$

Or, equivalently, we have $n ^ { ~ 6 6 }$ uncoupled” scalar equations

$$
\dot { z } _ { j } ( t ) = \lambda _ { j } z _ { j } ( t ) + \varphi _ { j } ( t ) ,\tag{5}
$$

for $j = 1 , 2 , \dots , n .$ These can be solved by elementary methods and the solution of the original system (2) is recovered by observing that $z ( t ) = Q ^ { \mathrm { { r } } } x ( t )$ and, using Eq. (3) ${ \bf { \boldsymbol { x } } } ( t ) = P { \boldsymbol { \boldsymbol { z } } } ( t )$

For the homogeneous Eq. (1) (when $\pmb { f } ( t ) = \pmb { \theta }$ for all t in Eq. (2)), we simply have $\varphi _ { j } ( t ) = 0$ in Eq. (5) and the solution of (5) is $z _ { j } ( t ) = c _ { j } e ^ { \dot { a } _ { j } t }$ for some

constant $c _ { j }$ . Thus, in this case, $\boldsymbol { z } ( t ) = \mathrm { d i a g } [ e ^ { \lambda _ { 1 } t } , \dots , e ^ { \lambda _ { n } t } ] \boldsymbol { c }$ and so every solution of Eq. (1) has the form

$$
\mathbf { \boldsymbol { x } } ( t ) = P \operatorname { d i a g } [ e ^ { \lambda _ { 1 } t } , \ldots , e ^ { \lambda _ { n } t } ] \boldsymbol { c }\tag{6}
$$

for some $\pmb { c } \in \mathbb { C } ^ { n } , \pmb { c } = [ c _ { 1 } \textnormal { \texttt { \small c } } _ { 2 } \textnormal { \texttt { \small c } } _ { 1 } ] ^ { \mathtt { T } } .$

Observe that Eq. (6) just means that any solution of Eq. (1) is a linear combination of the primitive solutions $x _ { j } e ^ { \lambda _ { j } t } , j = 1 , 2 , \ldots , n .$ Since these primitive solutions are linearly independent (see Exercise 1), it follows that if $\mathcal { S }$ is the solution set of Eq. (1) and A is a simple $n \times n$ matrix, then dim ${ \mathcal { S } } = n .$

In Chapter 9 we will return to the discussion of Eq. (2) and remove our hypothesis that A be simple; also we will consider the case when $f ( t ) \neq \pmb { \theta }$ more closely.

Exercise 2. Describe the solutions of the following system of differential equations with constant coefficients $( x _ { j } = x _ { j } ( t ) , j = 1 , 2 , 3 )$

$$
\begin{array} { l } { \dot { x } _ { 1 } = 2 x _ { 1 } } \\ { \dot { x } _ { 2 } = 1 1 x _ { 1 } + 4 x _ { 2 } + 5 x _ { 3 } , } \\ { \dot { x } _ { 3 } = 7 x _ { 1 } - x _ { 2 } - 2 x _ { 3 } . } \end{array}\tag{7}
$$

SoLUTIoN. Rewrite the system in matrix form:

$$
{ \dot { \mathbf { x } } } = A \mathbf { x } ,\tag{8}
$$

where

$$
A = \left[ { \begin{array} { r r r } { 2 } & { 0 } & { 0 } \\ { 1 1 } & { 4 } & { 5 } \\ { 7 } & { - 1 } & { - 2 } \end{array} } \right] , \qquad x = \left[ { \begin{array} { r } { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} } \right] , \qquad \dot { x } = \left[ { \begin{array} { r } { \dot { x } _ { 1 } } \\ { \dot { x } _ { 2 } } \\ { \dot { x } _ { 3 } } \end{array} } \right] ,
$$

and recall (see Exercise 4.11.1) that A has eigenvalues 2, 3, and -1 corresponding to the eigenvectors $\mathbf { x } _ { 1 } = [ 3 \quad - 7 9 \quad 2 5 ] ^ { \mathrm { T } } , \ \mathbf { x } _ { 2 } = [ 0 \quad 5 \quad - 1 ] ^ { \mathrm { T } } ,$ and $\pmb { x } _ { 3 } = [ 0 \pmb { 1 } - 1 ] ^ { \mathbf { \hat { r } } }$ . Thus, by Eq. (6), any solution $\mathbf { x } = [ \mathbf { x } _ { 1 } \quad \mathbf { \Delta } \mathbf { x } _ { 2 } \quad \mathbf { \Delta } \mathbf { x } _ { 3 } ] ^ { \mathbf { I } }$ of Eq. (8) is of the form

$$
\begin{array} { r } { \pmb { x } = c _ { 1 } \pmb { x _ { 1 } } e ^ { 2 t } + c _ { 2 } \pmb { x _ { 2 } } e ^ { 3 t } + c _ { 3 } \pmb { x _ { 3 } } e ^ { - t } = \left[ \pmb { x _ { 1 } } \quad \pmb { x _ { 2 } } \quad \pmb { x _ { 3 } } \right] \left[ \begin{array} { l l l } { e ^ { 2 t } } & { 0 } & { 0 } \\ { 0 } & { e ^ { 3 t } } & { 0 } \\ { 0 } & { 0 } & { e ^ { - t } } \end{array} \right] \left[ \begin{array} { l } { c _ { 1 } } \\ { c _ { 2 } } \\ { c _ { 3 } } \end{array} \right] } \end{array}
$$

or, what is equivalent, comparing the components of the vectors,

$$
\begin{array} { l } { { x _ { 1 } = 3 c _ { 1 } e ^ { 2 t } , } } \\ { { x _ { 2 } = - 7 9 c _ { 1 } e ^ { 2 t } + 5 c _ { 2 } e ^ { 3 t } + c _ { 3 } e ^ { - t } , } } \\ { { x _ { 3 } = 2 5 c _ { 1 } e ^ { 2 t } - c _ { 2 } e ^ { 3 t } - c _ { 3 } e ^ { - t } , } } \end{array}
$$

for some $c _ { 1 } , c _ { 2 } , c _ { 3 } \in \mathbb { C }$ □

## 4.14 Miscellaneous Exercises

1. Let ${ \mathcal { S } } = { \mathcal { S } } _ { 1 } + { \mathcal { S } } _ { 2 }$ . Define a transformation $T$ on $\mathcal { S }$ by

$$
T ( { \boldsymbol { \mathbf { x } } } ) = { \boldsymbol { \mathbf { \mathit { x } } } } _ { 1 } ,
$$

where ${ \pmb x } = { \pmb x } _ { 1 } + { \pmb x } _ { 2 }$ and $\pmb { x } _ { 1 } \in \mathcal { S } _ { 1 } , \pmb { x } _ { 2 } \in \mathcal { S } _ { 2 }$ . Prove that

(a) $T \in { \mathcal { L } } ( { \mathcal { S } } )$ );

(b) $\mathcal { S } _ { 1 }$ and $\mathcal { S } _ { 2 }$ are T-invariant;

(c) T satisfies the condition $T ^ { 2 } = T ( \mathrm { i } . \mathrm { e } . , T$ is idempotent).

The transformation $T$ is called a projector of $\mathcal { S }$ on $\mathcal { S } _ { 1 }$ parallel to $\mathcal { S } _ { 2 }$ Observe that $T | _ { \mathcal { S } _ { 1 } }$ is the identity transformation on $\mathcal { S } _ { 1 }$

2. Consider a simple linear transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ where dim ${ \mathcal { S } } = n ,$ $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ are its eigenvalues, and ${ \mathfrak { x } } _ { 1 } , { \mathfrak { x } } _ { 2 } , \ldots , { \mathfrak { x } } _ { n }$ are corresponding eigenvectors which span $\mathcal { S }$ Define ${ \mathcal { S } } _ { 1 } = \operatorname { s p a n } ( x _ { i } )$ for $i = 1 , 2 , \ldots , n .$ Show that $\begin{array} { r } { T = \sum _ { i = 1 } ^ { n } \cdot \lambda _ { i } I _ { i } } \end{array}$ , where $I _ { i }$ is the identity transformation on $\mathcal { S } _ { i } \left( 1 \leq i \leq n \right)$ and that $\begin{array} { r } { \mathcal { S } = \sum _ { i = 1 } ^ { n } \cdot \mathcal { S } _ { i } } \end{array}$ ; this is the spectral theorem for simple transformations.

3. Consider the spectral decomposition presented as Theorem 4.10.3. Let

$$
G _ { j } = { \pmb x } _ { j } { \pmb y } _ { j } ^ { \operatorname { T } } \operatorname { f o r } j = 1 , 2 , \ldots , n , \operatorname { s o } \operatorname { t h a t } A = \sum _ { j = 1 } ^ { n } \lambda _ { j } G _ { j } .
$$

(a) Show that each $G _ { j }$ has rank one and that $G _ { 1 } , \ldots , G _ { n }$ are mutually orthogonal in the sense that $G _ { k } G _ { j } = \delta _ { k j } G _ { k }$ for $1 \leq j , k \leq n$

(b) If $p ( \lambda )$ is any scalar polynomial, show that $p ( A )$ is simple and $\begin{array} { r } { p ( A ) = \sum _ { j = 1 } ^ { n } p ( \lambda _ { j } ) G _ { j } } \end{array}$

The matrix $G _ { j } , 1 \le j \le n ,$ is referred to as the constituent matrix of A associated with $\lambda _ { j }$

4. The matrix $\ b { R _ { \lambda } } = ( \lambda \ b { I } - \lambda ) ^ { - 1 }$ , called the resolvent of A, is defined at the points $\lambda \not \in \sigma ( A )$ . Verify the following statements:

(a) $R _ { \lambda } - R _ { \mu } = ( \mu - \lambda ) R _ { \lambda } R _ { \mu }$ u;

(b) If A is simple and $G _ { 1 } , G _ { 2 } , \ldots , G _ { n }$ are defined as in Exercise 3, then

$$
R _ { \lambda } = \sum _ { i = 1 } ^ { n } \frac { 1 } { \lambda - \lambda _ { i } } G _ { i } , \qquad \lambda \notin \sigma ( { \cal A } ) .
$$

Hint. First use Eqs. (4.13.3) and (4.13.4) to write $R _ { \lambda } = P ( \lambda I - D ) ^ { - 1 } Q ^ { \mathbf { T } }$

5. Prove that if dim ${ \mathcal { S } } = n ,$ any transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ has an invariant subspace of dimension $n - 1$

Hint. Let $\lambda \in \sigma ( T )$ and use Eq. (4.5.2) for $T - \lambda I$ to confirm the existence of the k-dimensional subspace Im $( T - \lambda I )$ invariant under $T ,$

where $k \leq n - 1$ . Then observe that any subspace in $\mathcal { S }$ containing $\mathrm { I m } ( T - \lambda I )$ is T-invariant.

6. Prove that for any $T \in { \mathcal { L } } ( { \mathcal { S } } )$ there is a set of T-invariant subspaces $\mathcal { S } _ { i } \left( i = 1 , 2 , . . . , n = \dim \mathcal { S } \right)$ such that

$$
\mathcal { S } _ { 1 } \subset \mathcal { S } _ { 2 } \subset \dots \subset \mathcal { S } _ { n - 1 } \subset \mathcal { S } _ { n } = \mathcal { S }
$$

and dim $\mathcal { S } _ { i } = i \mathrm { f o r } i = 1 , 2 , \ldots , n .$

Hint. Use an inductive argument based on the previous result.

7. Interpret the result of Exercise 6 for matrices. Show that the representation of T with respect to the basis $\boldsymbol { \mathcal { E } } = \{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { n } \}$ , where $\pmb { x } _ { i } \in \mathscr { S } _ { i }$ $( 1 \leq i \leq n )$ (see Exercise 6) is an upper-triangular matrix, while with respect to $\mathcal { E } ^ { \prime } = \{ \boldsymbol { x } _ { n } , \boldsymbol { x } _ { n - 1 } , . . . , \boldsymbol { x } _ { 1 } \}$ , it is lower-triangular (Schur's theorem).

8. Prove that if A is a simple matrix with characteristic polynomial $c ( \lambda ) ,$ then $c ( A ) = 0 .$ (This is a special case of the Cayley-Hamilton theorem, to be proved in full generality in Sections 6.2 and 7.2).

Hint. Use theorem 4.10.2.

9. Show that the inverse of a nonsingular simple matrix $\ b { A } \in \mathbb { C } ^ { n \times n }$ is given by the formula

$$
A ^ { - 1 } = \mathrm { } - \frac { 1 } { c _ { 0 } } ( A ^ { n - 1 } + c _ { n - 1 } A ^ { n - 2 } + \mathrm { } \cdot \cdot \cdot + c _ { 1 } I ) ,
$$

where $\begin{array} { r } { c ( \lambda ) = \lambda ^ { n } + \sum _ { i = 0 } ^ { n - 1 } c _ { i } \lambda ^ { i } } \end{array}$ is the characteristic polynomial of A.

Hint. Observe that $A ^ { - 1 } c ( A ) = 0 .$

10. Check the following statements.

(a) If A or B is nonsingular, then $A B \approx B A$ . Consider the example

$$
A = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] } , \qquad B = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] }
$$

to confirm that in the case of singular matrices, AB and BA may not be similar.

(b) For any $A , B \in { \mathcal { F } } ^ { n \times n }$ , the matrices AB and BA have the same characteristic polynomial and hence the same eigenvalues.

Hint. For part (b) use the following polynomial identity in λ:

$$
\operatorname* { d e t } ( \lambda I - ( A - \mu I ) B ) = \operatorname* { d e t } ( \lambda I - B ( A - \mu I ) )
$$

for $\mu \in \mathcal F$ such that $A \mathrm { ~ - ~ } \mu I$ is nonsingular.

11. Prove that if $A B = B A ,$ , then A and B have at least one common eigenvector. Furthermore, if A and B are simple, then there exists a basis in the space consisting of their common eigenvectors.

Hint. Consider span $\{ \pmb { x } , B \pmb { x } , \dots , B ^ { s } \pmb { x } , \dots \}$ , where $A { \mathfrak { x } } = \lambda { \mathfrak { x } } , { \mathfrak { x } } \neq { \pmb { 0 } } ;$ and use Exercise 4.9.8 to establish the first statement.

12. Let $A \in { \mathcal { F } } ^ { n \times n }$ . Show that, in comparison with Exercise 4.5.12,

(a) If the zero eigenvalue of A has the same algebraic and geometric multiplicities, then Ker $A = \operatorname { K e r } A ^ { 2 }$

(b) If A is simple, then Im $A ^ { 2 } = \operatorname { I m } A .$

13. If A is an idempotent matrix of rank $r ,$ show that tr $A = r$

Hint. Use Exercise 4.11.7, Theorem 4.10.3, and Eq. (4.11.3).

14. Let $A \in { \mathcal { F } } ^ { n \times n }$ and let $A = [ \pmb { a } \pmb { a } \pmb { \cdots } \pmb { a } ]$ , where $a \in \mathcal { F } ^ { n }$ .Show that at least $n - 1$ eigenvalues of A are zero.

Hint. Use Theorem 4.11.2

15. (a) Let $A _ { n }$ be the $n \times n$ matrix

$$
{ \left[ \begin{array} { l l l l l } { 2 c } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 1 } & { 2 c } & { 1 } & & { \vdots } \\ { 0 } & { 1 } & { 2 c } & & { 0 } \\ { \vdots } & & { \ddots } & { \ddots } & { 1 } \\ { 0 } & { \cdots } & { 0 } & { 1 } & { 2 c } \end{array} \right] } ,
$$

where c = cos θ. If $D _ { n } = \operatorname* { d e t } A _ { n }$ , show that

$$
D _ { n } = { \frac { \sin ( n + 1 ) \theta } { \sin n \theta } }
$$

(b) Find the eigenvalues of $A _ { n }$

Note that $D _ { n } ( c )$ is the Chebyshev polynomial of the second kind, $U _ { n } ( c )$ The matrix $A _ { n }$ with $c = - 1$ arises in Rayleigh's finite-dimensional approximation to a vibrating string.

Hint. For part (b), observe that $A _ { n } - \lambda I$ preserves the form of $A _ { n }$ for small λ to obtain the eigenvalues of $A _ { n }$

$$
\lambda _ { k } = 2 { \bigg ( } c - \cos { \frac { k \pi } { n + 1 } } { \bigg ) } , \qquad k = 1 , 2 , \ldots , n .
$$

16. Find the eigenvalues and eigenvectors of the $n \times n$ circulant matrix with the first row $[ a _ { 0 } \quad a _ { 1 } \quad \cdots \quad a _ { n - 1 } ]$

Hint. Use Exercise $2 . 1 1 . 1 \bar { 4 }$ to determine the eigenvalues $\lambda _ { k } = a ( \varepsilon _ { k } ) ,$ and the eigenvectors $[ 1 \quad \varepsilon _ { k } \quad \varepsilon _ { k } ^ { 2 } \quad \cdot \cdot \cdot \quad \varepsilon _ { k } ^ { n - 1 } ] ^ { \mathrm { \bf T } }$ , where

$$
a ( \lambda ) = \sum _ { i = 0 } ^ { n - 1 } a _ { i } \lambda ^ { i }
$$

and

$$
\varepsilon _ { k } = \cos ( \frac { 2 \pi k } { n } ) + i \sin ( \frac { 2 \pi k } { n } \bigg ) , k = 0 , 1 , \ldots , n - 1 .
$$

17. Let $V \in \mathcal { L } ( \mathcal { S } _ { 1 } , \mathcal { S } _ { 2 } ) , X \in \mathcal { L } ( \mathcal { S } _ { 2 } , \mathcal { S } _ { 1 } )$ and satisfy $X V = I ,$ the identity on $\mathcal { S } _ { 1 }$ . Show that $\mathcal { S } _ { 2 } = \operatorname { I m } V + \operatorname { K e r } X$

Hint. To show that $\mathcal { S } _ { 2 } = \operatorname { I m } V + \mathbf { K }$ er $\scriptstyle { X , }$ let $\pmb { x } \in \mathcal { S } _ { 2 }$ and write ${ \pmb x } =$ $\ " + \ w _ { \ast }$ where $\ " \boldsymbol { \nu } = V X \boldsymbol { x }$ . Then show that the sum is direct.

# Linear Transformations in Unitary Spaces and Simple Matrices

The results discussed in Chapter 4 are obviously applicable to linear transformations mapping one unitary space into another. Some additional properties of transformations resulting from the existence of the inner product are considered in this chapter. In particular, it will be shown that any linear transformation acting on a unitary space has a dual transformation, known as its “adjoint." Normal matrices and transformations are defined and studied in terms of adjoints prior to the analysis of the important subclasses of Hermitian matrices (and self-adjoint transformations) and unitary matrices and transformations. All of these special classes are subsets of the simple matrices and transformations introduced in Chapter 4.

Other important ideas associated with simple matrices are developed, for example, projectors and the reduction of quadratic forms. The chapter concludes with an important application (Section 5.12) and some preparatory ideas for subsequent applications in systems theory (Section 5.13). Note that throughout this chapter the underlying field is assumed to be $\mathcal F = \mathbb C$ or $\mathcal F = \mathbb R$

## 5.1 Adjoint Transformations

Let ${ \mathcal { U } } , { \mathcal { V } }$ be unitary spaces with inner products $( \mathbf { \Phi } , \mathbf { \Phi } ) _ { 1 }$ and $( \ , \ ) _ { 2 }$ , respectively, and let $T \in { \mathcal { L } } ( { \mathcal { U } } , { \mathcal { V } } )$ . Observe first that any vector ${ \mathfrak { v } } \in { \mathcal { V } }$ is uniquely determined if $( { \pmb v } , { \pmb y } ) _ { 2 }$ is known for all $\mathbf { \boldsymbol { y } } \in \mathcal { V } .$ Indeed, as indicated in Exercise 3.12.8, it is sufficient to know these inner products for all vectors y in a basis for $\mathcal { V } .$ It follows that the action of $T$ is determined by the values of all the numbers $( T \mathbf { x } , y ) _ { 2 }$ , where x, y are any vectors from $\boldsymbol { \mathcal U }$ and $\mathcal { V } ,$ respectively. We ask whether this same set of numbers is also attained by first forming the image of $\pmb { y }$ under some $T _ { 1 } \in \mathcal { L } ( \mathcal { V } , \mathcal { U } )$ , and then taking the $( \mathbf { \lambda } , \mathbf { \lambda } ) _ { 1 }$ inner product with x. In other words, is there a $T _ { 1 } \in \mathcal { L } ( \mathcal { V } , \mathcal { U } )$ such that

$$
( T ( \pmb { x } ) , \pmb { y } ) _ { 2 } = ( \pmb { x } , T _ { 1 } ( \pmb { y } ) ) _ { 1 }\tag{1}
$$

for all $\mathbf { \boldsymbol { x } } \in \mathcal { U }$ and $\mathbf { \boldsymbol { y } } \in \mathcal { V } ?$ The answer is yes, and the “ partner" for T, written $T ^ { * }$ is known as the adjoint of T.

To define the adjoint we consider an orthonormal basis $\pmb { u } _ { 1 } , \ldots , \pmb { u } _ { n }$ for ${ \pmb u } .$ Then define a map $T ^ { * } { \colon } \mathcal { V }  \mathcal { U }$ in terms of $T$ by

$$
T ^ { * } ( y ) = \sum _ { j = 1 } ^ { n } { ( y , T ( u _ { j } ) ) _ { 2 } } { u _ { j } }\tag{2}
$$

for any $\pmb { y } \in \mathcal { V } .$ We check first that $T ^ { * } \in \mathcal { L } ( \mathcal { V } , \mathcal { U } )$ . If ${ \pmb y } , { \pmb z } \in \mathcal { V }$ and $\alpha , \beta \in \mathcal { F }$ then, using the linearity of the inner product (Section 3.11),

$$
\begin{array} { c } { { T ^ { * } ( \alpha y + \beta z ) = \displaystyle \alpha \sum _ { j = 1 } ^ { n } ( y , T ( u _ { j } ) ) _ { 2 } u _ { j } + \displaystyle \beta \sum _ { j = 1 } ^ { n } ( z , T ( u _ { j } ) ) _ { 2 } u _ { j } } } \\ { { { } } } \\ { { { } = \alpha T ^ { * } ( y ) + \beta T ^ { * } ( z ) , } } \end{array}
$$

by definition (2) of $T ^ { * }$ . Thus $T ^ { * } \in \mathcal { L } ( \mathcal { V } , \mathcal { U } )$ . Our first theorem will show that $T ^ { * } { } _ { ; }$ , so defined, does indeed have the property (1) that we seek. It will also show that our definition of $T ^ { * }$ is, in fact, independent of the choice of orthonormal basis for ${ \pmb u } .$

First we should note the important special case of this discussion in which $\mathcal { U } = \mathcal { V }$ and the inner products also coincide. In this case, the definition (2) reads

$$
T ^ { * } ( x ) = \sum _ { j = 1 } ^ { n } { ( x , T ( u _ { j } ) ) u _ { j } } ,\tag{3}
$$

and $T ^ { * } ,$ , as well as T, belongs to ${ \mathcal { L } } ( { \boldsymbol { \mathcal { U } } } )$

Theorem 1. Let $T \in { \mathcal { L } } ( { \mathcal { U } } , { \mathcal { V } } )$ , where $\pmb { \mathcal U }$ is a unitary space with inner product $( ~ , ~ ) _ { 1 }$ and $\mathcal { V }$ is a unitary space with inner product $( ~ , ~ ) _ { 2 }$ . The adjoint transformation $T ^ { * } \in \mathcal { L } ( \mathcal { V } , \mathcal { U } )$ satisfies the condition

$$
( T ( \mathbf { x } ) , \mathbf { y } ) _ { 2 } = ( \mathbf { x } , T ^ { * } ( \mathbf { y } ) ) _ { 1 }\tag{4}
$$

for every $\pmb { x } \in \mathcal { U } , \pmb { y } \in \mathcal { V }$ and is the unique member of $\mathcal { L } ( \mathcal { V } , \mathcal { U } )$ for which $E q$ (4) holds. Conversely, if Eq. (4) holds, then $T ^ { * }$ is the adjoint of T.

ProoF. It has been shown that $T ^ { * } \in \mathcal { L } ( \mathcal { V } , \mathcal { U } )$ . To prove the equality in Eq. (4) we use Exercise 3.12.3 to write $\begin{array} { r } { \pmb { x } = \sum _ { i = 1 } ^ { n } ( \pmb { x } , \pmb { u } _ { i } ) _ { 1 } \pmb { u } _ { i } . } \end{array}$ Then, using the linearity of $T ,$

$$
( T ( x ) , y ) _ { 2 } = \left( \sum _ { i = 1 } ^ { n } ( x , u _ { i } ) _ { 1 } T ( u _ { i } ) , y \right) _ { 2 } = \sum _ { i = 1 } ^ { n } ( x , u _ { i } ) _ { 1 } ( T ( u _ { i } ) , y ) _ { 2 } .\tag{5}
$$

On the other hand, by Eq. (2) and the orthonormality of the basis,

$$
\begin{array} { l } { { \displaystyle ( x , T ^ { * } ( y ) ) _ { 1 } = \left( \sum _ { i = 1 } ^ { n } ( x , u _ { i } ) _ { 1 } u _ { i } , \sum _ { j = 1 } ^ { n } ( y , T ( u _ { j } ) ) _ { 2 } u _ { j } \right) _ { 1 } } } \\ { { \displaystyle = \sum _ { i = 1 } ^ { n } ( x , u _ { i } ) _ { 1 } \widetilde { ( y , T ( u _ { i } ) ) _ { 2 } } . } } \end{array}\tag{6}
$$

Since $\overline { { ( y , T ( u _ { i } ) ) _ { 2 } } } = ( T ( u _ { i } ) , y ) _ { 2 }$ , Eq. (4) follows on comparing Eq. (6) with Eq. (5).

For the uniqueness, let $( T ( x ) , y ) _ { 2 } = ( x , T _ { 1 } ( y ) ) _ { \mathrm { \scriptsize { 1 } } }$ for some $T _ { 1 } \in \mathcal { L } ( \mathcal { V } , \mathcal { U } )$ and all ${ \pmb x } \in { \mathcal { U } } , { \pmb y } \in { \mathcal { V } } .$ Then, on comparison with Eq. (4),

$$
( { \pmb x } , T _ { 1 } ( { \pmb y } ) ) _ { 1 } = ( { \pmb x } , T ^ { * } ( { \pmb y } ) ) _ { 1 }
$$

for all $\boldsymbol { x } \in \mathcal { U }$ and $\mathbf { \boldsymbol { y } } \in \mathcal { V } .$ But this clearly means that $( x , ( T _ { 1 } - T ^ { * } ) ( y ) ) _ { 1 } = 0$ for all $\pmb { x } \in \mathcal { U }$ and ${ \mathfrak { y } } \in { \mathcal { V } } ,$ and this implies (by Exercise 3.13.2) that $T _ { 1 } - T ^ { * } =$ $\theta ,$ that is, $T _ { 1 } = T ^ { * }$

The proof of the converse statement uses similar ideas and is left as an exercise.

It is interesting to compare Eq. (4) with the result of Exercise 3.14.8. The similarity between these statements will be explained in our next theorem.

Exercise 1. Let $T \in \mathcal { L } ( \mathcal { F } ^ { 3 } , \mathcal { F } ^ { 4 } )$ be defined as in Exercise 4.2.1. Check that the transformation

$$
T _ { 1 } ( y ) = \left[ \begin{array} { c } { y _ { 2 } + y _ { 3 } + y _ { 4 } } \\ { y _ { 1 } + y _ { 2 } - y _ { 4 } } \\ { y _ { 1 } } \end{array} \right] ,
$$

for all $\pmb { y } = [ y _ { 1 } \quad y _ { 2 } \quad y _ { 3 } \quad y _ { 4 } ] ^ { \mathbf { T } } \in \mathcal { F } ^ { 4 }$ , is the adjoint of T with respect to the standard inner products in ³ and F⁴. Confirm Eq. (4) for the given trans- ${ \mathcal { F } } ^ { 3 }$ ${ \mathcal { F } } ^ { 4 }$ formations.□

Some important properties of the adjoint are indicated next.

Exercise 2. Prove the following statements:

(a) $I ^ { * } = I , \quad 0 ^ { * } = 0 ;$

(b) $( T ^ { * } ) ^ { * } = T ;$

(c) $( \alpha T ) ^ { * } = { \bar { \alpha } } T ^ { * }$ for any $\alpha \in \mathcal { F }$

(d) $( T _ { 1 } + T _ { 2 } ) ^ { * } = T _ { 1 } ^ { * } + T _ { 2 } ^ { * } ;$

(e) $( T _ { 2 } T _ { 1 } ) ^ { * } = T _ { 1 } ^ { * } T _ { 2 } ^ { * }$ for every $T _ { 1 } \in \mathcal { L } ( \mathcal { U } , \mathcal { W } ) , T _ { 2 } \in \mathcal { L } ( \mathcal { W } , \mathcal { V } )$

SoLuUTioN. We shall prove only the last equality, since all of them are established analogously. Successive use of Eq. (4) gives

$$
( { \pmb x } , ( T _ { 2 } T _ { 1 } ) ^ { * } ( { \pmb y } ) ) = ( T _ { 2 } T _ { 1 } ( { \pmb x } ) , { \pmb y } ) = ( T _ { 1 } ( { \pmb x } ) , T _ { 2 } ^ { * } ( { \pmb y } ) ) = ( { \pmb x } , T _ { 1 } ^ { * } T _ { 2 } ^ { * } ( { \pmb y } ) )
$$

for all ${ \pmb x } \in { \mathcal { U } } , { \pmb y } \in { \mathcal { V } } .$ Hence (see Exercise 3.13.2), $( T _ { 2 } T _ { 1 } ) ^ { * } ( y ) = T _ { 1 } ^ { * } T _ { 2 } ^ { * } ( y )$ for all $\pmb { y } \in \mathcal { V }$ and therefore part (e) holds.

Exercise 3. Check that $T \in { \mathcal { L } } ( { \mathcal { U } } )$ is invertible if and only if $T ^ { * } \in { \mathcal { L } } ( { \mathcal { U } } )$ is invertible and that in this case,

$$
( T ^ { * } ) ^ { - 1 } = ( T ^ { - 1 } ) ^ { * } .\tag{7}
$$

SoLUTION. Let T be invertible. If $T ^ { * } ( x ) = \pmb { \theta } ,$ then by Eq. (3),

$$
\sum _ { i = 1 } ^ { n } { ( x , T ( u _ { i } ) ) u _ { i } } = \theta
$$

and consequently $( { \pmb x } , T ( { \pmb u } _ { i } ) ) = 0 , i = 1 , 2 , \ldots , n .$ The invertibility of $T$ means that since all the elements $T ( u _ { i } )$ are images of the basis elements in ${ \bf \nabla } \mathcal { U } ,$ they generate another basis in ${ \pmb u } .$ Hence by Exercise 3.13.2, we must have $\begin{array} { r } { \mathbf { x } = \pmb { \theta } , } \end{array}$ and by Theorem 4.6.3, the transformation $T ^ { * }$ is invertible. The converse follows by applying part (b) of Exercise 2. To establish Eq. (7), write

$$
( x , ( T ^ { - 1 } ) ^ { * } ( y ) ) = ( T ^ { - 1 } ( x ) , y )
$$

and use the invertibility of $T ^ { * }$ to find an element $\pmb { z } \in \mathcal { U }$ such that $T ^ { * } ( z ) = y$ Hence, continuing, we have by Exercise 2(b)

$$
\bigl ( T ^ { - 1 } ( x ) , y \bigr ) = ( T ^ { - 1 } ( x ) , T ^ { * } ( z ) ) = ( T T ^ { - 1 } ( x ) , z ) = ( \pmb { x } , z ) = ( \pmb { x } , ( T ^ { * } ) ^ { - 1 } ( y ) )
$$

for any x, $\boldsymbol { y } \in \mathcal { U } .$ Thus, reasoning as in the solution of Exercise 2, we deduce the required relation (7). □

Proceeding to the study of matrix representations for a transformation $T \in { \mathcal { L } } ( { \mathcal { U } } , { \mathcal { V } } )$ and its adjoint, we discover the reason for the use of the “star" notation for both the adjoint of a linear transformation and the conjugate transpose of a matrix.

Theorem 2. Let $T \in \mathcal { L } ( \mathcal { U } , \mathcal { V } )$ and let $T ^ { * }$ denote the adjoint of T. If $A \in \mathcal { F } ^ { m \times n }$ is the representation of T with respect to the orthonormal bases $( \mathscr { E } , \mathscr { G } )$ , then the conjugate transpose matrix $A ^ { * } \in \mathcal { F } ^ { n \times m }$ is the representation of $T ^ { * }$ with respect to the pair of bases $( \mathcal { G } , \mathcal { E } )$

PROOF. Let $\mathcal { E } = \{ \boldsymbol { u } _ { 1 } , \boldsymbol { u } _ { 2 } , \ldots , \boldsymbol { u } _ { n } \}$ and $\mathcal { G } = \{ v _ { 1 } , v _ { 2 } , \ldots , v _ { m } \}$ denote orthonormal bases in $\alpha$ and $\mathcal { V } ,$ respectively. Then the representation $A = [ a _ { i j } ] _ { i , j = 1 } ^ { m , n }$ is found from the equations

$$
T ( u _ { j } ) = \sum _ { i = 1 } ^ { m } a _ { i j } v _ { i } , \qquad j = 1 , 2 , \ldots , n ,
$$

where $a _ { i j } = ( T ( u _ { j } ) , v _ { i } ) _ { 2 }$ , and $i = 1 , 2 , . . . , m , j = 1 , 2 , . . . , n $ Similarly, for the element $b _ { j i } \ ( 1 \leq i \leq m , \ 1 \leq j \leq n )$ of the representation of $T ^ { * }$ with respect to the bases $\mathscr { G }$ and $\clubsuit ,$ we have

$$
T ^ { * } ( v _ { i } ) = \sum _ { j = 1 } ^ { n } b _ { j i } u _ { j } , \qquad i = 1 , 2 , \ldots , m ,
$$

where $b _ { j i } = ( T ^ { * } ( \pmb { v } _ { i } ) , \pmb { u } _ { j } ) _ { 1 }$ , for $1 \leq i \leq m$ and $1 \leq j \leq n .$ Hence Theorem 1 implies

$$
b _ { j i } = ( \pmb { v } _ { i } , T ( \pmb { u } _ { j } ) ) _ { 2 } = ( \widetilde { T ( \pmb { u } _ { j } ) } , \pmb { v } _ { i } ) _ { 2 } = \widetilde { a _ { i j } } \qquad 1 \leq i \leq m , \quad 1 \leq j \leq n ,
$$

and the assertion follows.

Exercise 4. Check the assertion of Theorem 2 for the transformations $T$ and $T _ { 1 } = T ^ { * }$ considered in Exercise 1.

Exercise 5. Deduce from Theorem 2 properties of the conjugate transpose similar to those of the adjoint presented in Exercises 2 and 3.

Exercise 6. Check that for any $T \in \mathcal { L } ( \pmb { \mathcal { U } } , \pmb { \mathcal { V } } )$

$$
\mathrm { r a n k \ } T = \mathrm { r a n k \ } T ^ { * } ,
$$

and that, if ${ \mathcal { U } } = { \mathcal { V } } ,$ then in addition

$$
\operatorname { d e f } T = \operatorname { d e f } T ^ { * } .
$$

Exercise 7. Let $T \in \mathcal { L } ( \mathcal { U } , \mathcal { V } )$ and let $T ^ { * }$ denote the adjoint of T. Show that

$$
\mathcal { U } = \mathop { \mathrm { K e r } } \ T \oplus \mathrm { I m } \ T ^ { * } , \qquad \mathcal { V } = \mathop { \mathrm { K e r } } \ T ^ { * } \oplus \mathrm { I m } \ T .
$$

(See the remark at the end of Section 5.8.)

Hint. Note that $( { \pmb x } , T ( { \pmb y } ) ) _ { 2 } = 0$ for all $y \in \mathcal { U }$ yields $\pmb { x } \in \mathbb { K }$ er $T ^ { * }$

Exercise 8. Let $T \in { \mathcal { L } } ( { \mathcal { U } } )$ . Check that if a subspace $\mathcal { U } _ { 0 } \subset \mathcal { U }$ is T-invariant, then the orthogonal complement to 0 in  is T\*-invariant. ${ { \pmb u } _ { 0 } }$ $\pmb { \mathcal { U } }$ $T ^ { * } .$

The next example indicates that the relation between the representations of T and $T ^ { * }$ with respect to a pair of nonorthonormal bases is more complicated than the one pointed out in Theorem 2.

Exercise 9. Prove that if $T \in { \mathcal { L } } ( { \mathcal { U } } )$ , the set $\mathcal { E } = \{ \boldsymbol { u } _ { 1 } , \boldsymbol { u } _ { 2 } , \ldots , \boldsymbol { u } _ { n } \}$ is an orthogonal basis in $\mathcal { U } ,$ and A is the representation of T with respect to $\mathbf { \delta } ^ { \mathcal { E } } ,$ then the representation $A ^ { \prime }$ of $T ^ { * }$ with respect to the same basis is

$$
A ^ { \prime } = D ^ { - 1 } A ^ { * } D ,\tag{8}
$$

where $D = \mathrm { d i a g } \{ ( u _ { i } , u _ { i } ) \} _ { i = 1 } ^ { n } . \quad \bigsqcup$

In particular, the relation (8) shows that $A ^ { \prime } = A ^ { * }$ provided the basis $\pmb { \delta }$ is orthonormal. However, it turns out that the assertion of Theorem 2 remains true if $\pmb { \mathcal { U } } = \pmb { \mathcal { V } }$ and the two sets of basis vectors are biorthogonal in u (see Section 3.13).

Theorem 3. Let $T \in { \mathcal { L } } ( { \mathcal { U } } )$ and let $( \mathcal { E } , \mathcal { E } ^ { \prime } )$ denote a pair of biorthogonal bases in U. If A is the representation of $T$ with respect to $\begin{array} { r } { \pmb { \mathcal { E } } , } \end{array}$ then $A ^ { * }$ is the representation of $T ^ { * }$ with respect to $\clubsuit ^ { \prime }$

PROOF. Let $\boldsymbol { \mathcal { E } } = \{ u _ { 1 } , u _ { 2 } , . . . , u _ { n } \} , \boldsymbol { \mathcal { E } } ^ { \prime } = \{ u _ { 1 } ^ { \prime } , u _ { 2 } ^ { \prime } , . . . , u _ { n } ^ { \prime } \}$ , and $A = [ a _ { i j } ] _ { i , j = 1 } ^ { n }$ Since $\begin{array} { r } { T ( u _ { j } ) = \sum _ { i = 1 } ^ { n } a _ { i j } u _ { i } ( 1 \leq j \leq n ) } \end{array}$ and $( { \pmb u } _ { k } , { \pmb u } _ { i } ^ { \prime } ) = \delta _ { k i } ( 1 \leq i , k \leq n ) .$ it follows that $( T ( \pmb { u } _ { j } ) , \pmb { u } _ { i } ^ { \prime } ) = a _ { i j }$ . Computing the entries $b _ { i j }$ of the representation $B$ of $T ^ { * }$ with respect to $\clubsuit ^ { \prime }$ in a similar way, we obtain $\begin{array} { r } { \pmb { b } _ { i j } = ( T ^ { * } ( \pmb { u } _ { j } ^ { \prime } ) , \pmb { u } _ { i } ) } \end{array}$ $( 1 \leq i , j \leq n )$ . Hence for all possible i and j,

$$
b _ { i j } = ( { \pmb u } _ { j } ^ { \prime } , T ( { \pmb u } _ { i } ) ) = ( \overline { { T ( { \pmb u } _ { i } ) , { \pmb u } _ { j } ^ { \prime } } } ) = \overline { { a _ { j i } } } ,
$$

and therefore $B = A ^ { * }$

Exercise 10. Check that if $T \in { \mathcal { L } } ( { \mathcal { U } } )$ then $\lambda \in \sigma ( T )$ if and only if $\bar { \lambda } \in \sigma ( T ^ { * } )$ Hint. See Exercise 4.11.9.

Exercise 11. Prove that the transformation $T \in { \mathcal { L } } ( { \mathcal { U } } )$ is simple if and only if $T ^ { * }$ is simple.

Hint. Use Theorem 3.

Exercise 12. If $T \in { \mathcal { L } } ( { \mathcal { U } } )$ is simple, show that there exist eigenbases of $T$ and $T ^ { * }$ in ¿ that are biorthogonal.

Hint. Consider span $\{ x _ { 1 } , x _ { 2 } , \ldots , x _ { j - 1 } , x _ { j + 1 } , \ldots , x _ { n } \} , 1 \leq j \leq n ,$ where $\{ { \pmb x } _ { i } \} _ { i = 1 } ^ { n }$ is an eigenbasis of T in ${ \bf \nabla } \mathcal { U } ,$ and use Exercise 8.

Exercise 13. If $T \in { \mathcal { L } } ( { \mathcal { U } } )$ is simple and $\{ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \}$ is its eigenbasis in $\boldsymbol { \mathcal { U } } ,$ prove that a system $\{ y _ { 1 } , y _ { 2 } , \ldots , y _ { n } \}$ in $\pmb { \mathcal { U } }$ that is biorthogonal to $\left\{ x _ { i } \right\} _ { i = 1 } ^ { n }$ is an eigenbasis of $T ^ { * }$ in ¿. Moreover, show that $T ( { \pmb x } _ { i } ) = \lambda _ { i } { \pmb x } _ { i }$ yields $T ^ { * } ( y _ { i } ) =$ $\bar { \lambda } _ { i } y _ { i } , 1 \leq i \leq n .$

Hint. Use Eq. (4).

Exercise 14. Check that the eigenspaces of $T$ and $T ^ { * }$ associated with noncomplex-conjugate eigenvalues are orthogonal.

We conclude this section with an important result concerning the general linear equation $T ( \mathbf { x } ) = \pmb { b } ,$ ,where $T \in { \mathcal { L } } ( { \mathcal { U } } , { \mathcal { V } } )$ and $\pmb { b } \in \mathcal { V }$ are given and solutions x in $\boldsymbol { \mathcal U }$ are to be found. This is a general result giving a condition for existence of solutions for any choice of $\pmb { b } \in \mathcal { V }$ in terms of the adjoint operator $T ^ { * }$ . It is known as the Fredholm alternative. (Compare with Exercise 3.14.10.)

Theorem 4. Let $T \in { \mathcal { L } } ( { \mathcal { U } } , { \mathcal { V } } )$ . Either the equation $T ( { \pmb x } ) = { \pmb b }$ is solvable for any $\pmb { b } \in \mathcal { V }$ or the equation $T ^ { * } ( y ) = \pmb { \theta }$ has nonzero solutions.

PROOF. Since $T ^ { * }$ is a linear transformation it is enough to show that $T ( \mathbf { x } ) = \pmb { b }$ solvable for any $\boldsymbol { b } \in \mathcal { V }$ is equivalent to $T ^ { * } ( y ) = \pmb { \theta }$ implies $\mathbf { \nabla } \mathbf { y } = \mathbf { 0 }$

Now the solvability condition clearly implies that Im $T = \mathcal { V } .$ But, by Exercise 7,

$$
\mathcal { V } = \mathrm { I m } \ T \oplus \mathrm { K e r } \ T ^ { * } ,
$$

consequently Ker $T ^ { * } = \{ \pmb { \theta } \}$ , i.e., $T ^ { * } ( y ) = \pmb { \theta }$ implies $\begin{array} { r } { \mathbf { y } = \pmb { \theta } . } \end{array}$

Clearly, the argument can be reversed to establish the converse statement.

## 5.2 Normal Transformations and Matrices

It was shown in Section 4.9 that a simple transformation T acting on a linear space $\mathcal { S }$ has an eigenbasis in $\mathcal { S } .$ If the space is unitary, then the possibility arises of an orthonormal eigenbasis of $T ,$ that ${ \dot { \mathbf { i s } } } ,$ a basis consisting of mutually orthogonal normalized eigenvectors of the transformation. Obviously (see Theorem 4.9.2) transformations T with this property are necessarily simple. Thus, a transformation $T \in { \mathcal { L } } ( { \mathcal { U } } )$ , where $\boldsymbol { \mathcal U }$ is unitary, is said to be normal if there exists an orthonormal basis in $\boldsymbol { \mathcal U }$ consisting entirely of eigenvectors of T. The normal matrices are defined similarly.

Exercise 1. Show that a transformation $T \in { \mathcal { L } } ( { \mathcal { U } } )$ is normal if and only if the representation of $T$ with respect to any orthonormal basis in $\boldsymbol { \mathcal U }$ is a normal matrix.

Hint. See Theorem 4.2.2. □

For a further investigation of normal matrices and transformations, we need some preparations. First, let us agree to use the notation $\mathcal { A } _ { T } ^ { 0 }$ for the set of all matrices $\pmb { A } \in \mathcal { F } ^ { n \times n }$ such that A is a representation of $T \in { \mathcal { L } } ( { \mathcal { U } } )$ with respect to an orthonormal basis in ${ \pmb u } .$ Furthermore, recall (Exercise 3.14.12) that the transition matrix $P \in \mathcal { F } ^ { n \times n }$ from one orthonormal basis in @ into another is a unitary matrix, that is, P satisfies the condition $P ^ { * } P = I$ Hence Theorem 4.3.2 implies that any two representations A and $A ^ { \prime }$ from $\mathcal { A } _ { T } ^ { 0 }$ are related by the equation $A ^ { \prime } = P A P ^ { * }$ , where $P$ is some unitary matrix.

In general, if the matrix B is similar to A and there exists a unitary transforming matrix $U$ so that

$$
B = U A U ^ { * } = U A U ^ { - 1 } ,
$$

then we say that B is unitarily similar to A, and observe that B and A are simultaneously similar and congruent.† It is easily seen that unitary similarity is an equivalence relation. In other words, $\mathcal { A } _ { T } ^ { 0 }$ coincides with the equivalence class of matrix representations of $T \in { \mathcal { L } } ( { \mathcal { U } } )$ with respect to orthonormal bases in ${ \mathcal { U } } ,$ and all matrices in this class are unitarily similar. Note that the simplest (canonical) matrix in this class is a diagonal matrix of the eigenvalues of T. We now summarize the discussion of this paragraph in a formal statement.

Theorem 1. An n × n matrix A is normal if and only $i f$ it is unitarily similar to a diagonal matrix of its eigenvalues;

$$
A = U D U ^ { * } ,\tag{1}
$$

where $D = \mathrm { d i a g } [ \lambda _ { i } ] _ { i = 1 } ^ { n } , \lambda _ { i } \in \sigma ( A ) , i = 1 , 2 , \ldots , n ,$ and U is unitary.

Note (see Theorem 4.10.2) that the columns of U viewed as vectors from ${ \mathcal { F } } ^ { n }$ give the (orthonormal) eigenvectors of A and that D in Eq. (1) is a canonical form for matrices in $\mathcal { A } _ { T } ^ { 0 }$ with respect to unitary similarity.

Recall that in $\mathbb { R } ^ { n \times n }$ the unitary matrices are known as orthogonal matrices (ref. Exercise 2.6.16) and satisfy the condition $U ^ { \boldsymbol { \mathsf { T } } } U = I .$ Naturally, real matrices $A$ and B from $\mathbb { R } ^ { n \times n }$ are said to be orthogonally similar when $B =$ $U A U ^ { \boldsymbol { \mathsf { T } } }$ for some orthogonal matrix $U \in \mathbb { R } ^ { n \times n }$

Exercise 2. Let A denote a normal matrix. Prove that the matrix $A ^ { p }$ is normal for any positive integer p (and, if det $A \neq 0 ,$ , for any integer p).

Exercise 3. Show that the matrix A is normal if and only if $A ^ { * }$ is normal and that the eigenspaces associated with mutually conjugate eigenvalues, of A and $A ^ { * }$ coincide.

Exercise 4. Check that if A is normal then, for any polynomial $p ( \lambda )$ over $\mathbb { C } ,$ the matrix $p ( A )$ is normal.

Exercise 5. Prove a spectral theorem for normal matrices (see Theorem 4.10.3): If A is an $n \times n$ normal matrix with eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n } ,$ then there is an associated set of orthonormal eigenvectors $\{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \ldots , \pmb { x } _ { n } \}$ such that $\begin{array} { r } { A = \sum _ { j = 1 } ^ { n } \lambda _ { j } \ d x _ { j } \ d x _ { j } ^ { * } } \end{array}$ □

If a matrix fails to be normal then by Theorem 1 it cannot be unitarily similar to a diagonal matrix. However, it is interesting to ask how far an arbitrary matrix can be reduced by means of a unitary similarity. The next theorem, which is due to Schur† and Toeplitz, casts some light on this more general question.

Theorem 2. Any square matrix is unitarily similar to an upper triangular matrix.

PROOF. Let $A \in { \mathcal { F } } ^ { n \times n }$ and let ¿ be the unitary space of ${ \mathcal { F } } ^ { n }$ equipped with the standard inner product. Then, in the natural way, A determines a transformation $T \in { \mathcal { L } } ( { \mathcal { U } } )$ . By Exercise 4.14.6 there exists a chain of T-invariant subspaces

$$
\{ \mathbf { 0 } \} = \mathcal { U } _ { 0 } \subset \mathcal { U } _ { 1 } \subset \cdots \subset \mathcal { U } _ { n } = \mathcal { U }
$$

such that ${ \pmb q } _ { i }$ has dimension i for each i. It follows that, using the Gram-Schmidt procedure, an orthonormal basis $\{ u _ { 1 } , \ldots , u _ { n } \}$ can be constructed for  with the properties that ${ \pmb u } _ { i } \in \mathcal { U } _ { i }$ and $\pmb { u } _ { i } \notin \pmb { \mathcal { U } } _ { i - 1 }$ for $i = 1 , 2 , \ldots , n$ Then the T-invariance of the chain of subspaces implies that the representation of T with respect to this orthonormal basis must be an upper-triangular matrix, B say (see Section 4.8)

But the matrix A is simply the representation of T with respect to the standard basis for ${ \mathcal { F } } ^ { n }$ (which is also orthonormal), and so A and B must be unitarily similar.

The Schur-Toeplitz theorem plays a crucial role in proving the next beautiful characterization of normal matrices; it is, in fact, often used as the definition of a normal matrix.

Theorem 3. An n × n matrix A is normal if and only if

$$
A A ^ { * } = A ^ { * } A .\tag{2}
$$

ProoF. If A is normal, then by Eq. (1) there is a unitary matrix U and a diagonal matrix D for which $A = U D U ^ { \star }$ . Then

$$
A A ^ { * } = ( U D U ^ { * } ) ( U { \bar { D } } U ^ { * } ) = U D { \bar { D } } U ^ { * } = U { \bar { D } } D U ^ { * } = ( U { \bar { D } } U ^ { * } ) ( U D U ^ { * } ) = A ^ { * } A ,
$$

so that A satisfies Eq. (2).

Conversely, we suppose $A A ^ { * } = A ^ { * } A$ and apply Theorem 2. Thus, there is a unitary matrix U and an upper triangular matrix $S = [ s _ { i j } ] _ { i , j = 1 } ^ { n }$ for which $A = U S U ^ { * }$ . It is easily seen that $A A ^ { * } = A ^ { * } A$ if and only if $S S ^ { * } = S ^ { * } S$ The 1,1 element of the last equation now reads

$$
| s _ { 1 1 } | ^ { 2 } + | s _ { 1 2 } | ^ { 2 } + \cdot \cdot \cdot + | s _ { 1 n } | ^ { 2 } = | s _ { 1 1 } | ^ { 2 } .
$$

Hence $s _ { 1 j } = 0 \mathrm { f o r } j = 2 , 3 , \ldots , n$ . The 2,2 element of the equation $S S ^ { * } = S ^ { * } S$ yields

$$
| s _ { 2 2 } | ^ { 2 } + | s _ { 2 3 } | ^ { 2 } + \cdot \cdot \cdot + | s _ { 2 n } | ^ { 2 } = | s _ { 1 2 } | ^ { 2 } + | s _ { 2 2 } | ^ { 2 } ,
$$

and since we have proved $s _ { 1 2 } = 0$ it follows that $s _ { 2 j } = 0$ for $j = 3 , 4 , \dots , n .$ Continuing in this way we find that $s _ { j k } = 0$ whenever $j \neq$ k and $1 \leq j , k \leq n ,$ Thus, S must be a diagonal matrix and $A = U S U ^ { * }$ . Now use Theorem 1.

Note that by virtue of Exercise 1 and the relation (4.2.4), a similar result holds for transformations.

Theorem 3'. A transformation $T \in { \mathcal { L } } ( { \mathcal { U } } )$ is normal if and only if

$$
T T ^ { * } = T ^ { * } T .\tag{3}
$$

Proceeding to special kinds of normal transformations, we first define a transformation $T \in \mathcal { L } ( \pmb { \mathcal { U } } )$ to be self-adjoint if $T = T ^ { * }$ , and to be unitary if $T T ^ { * } = T ^ { * } T = I$

Exercise 6. Check that a transformation $T \in { \mathcal { L } } ( { \mathcal { U } } )$ is self-adjoint (respectively, unitary) if and only if its representation with respect to any orthonormal basis is a Hermitian (respectively, unitary) matrix.

The important results of Exercise 6 allow us to deduce properties of selfadjoint and unitary transformations from those of the corresponding matrices studied in the subsequent sections. If not indicated otherwise, the inner product in ${ \mathcal { F } } ^ { n }$ is assumed to be standard, that is, $( { \pmb x } , { \pmb y } ) = { \pmb y } ^ { * } { \pmb x }$ for any $\mathbf { x } , \mathbf { y } \in \mathcal { F } ^ { n }$

Exercise 7. If $T \in { \mathcal { L } } ( { \mathcal { U } } )$ is normal and $\{ u _ { 1 } , u _ { 2 } , \ldots , u _ { n } \}$ is an orthonormal eigenbasis in $\pmb { \mathcal { U } } ,$ prove that $\left\{ u _ { i } \right\} _ { i = 1 } ^ { n }$ is also an (orthonormal) eigenbasis of $T ^ { * }$ in ¿. Furthermore, if $T ( { \pmb u } _ { i } ) = \lambda _ { i } { \pmb u } _ { i }$ , then $T ^ { * } ( u _ { i } ) = \bar { \lambda } _ { i } u _ { i }$ for all $i = 1 , 2 , \dots , n .$ Obviously, a similar result holds for normal matrices.

Hint. See Exercise 5.1.13.

Exercise 8. Find a real unitary matrix U and a diagonal matrix D for which $\mathbf { \Omega } _ { A } = U D U ^ { \dagger }$ if

$$
\begin{array} { r } { A = \left[ { \begin{array} { r r r } { 1 } & { 0 } & { - 4 } \\ { 0 } & { 5 } & { 4 } \\ { - 4 } & { 4 } & { 3 } \end{array} } \right] . } \end{array}
$$

Exercise 9. If $T \in { \mathcal { L } } ( { \mathcal { U } } )$ is normal and ${ { \pmb u } _ { 0 } }$ is a T-invariant subspace in ${ \pmb q } _ { 3 }$ show that $T \vert _ { \pmb { q } _ { \pmb { \imath } _ { 0 } } }$ is a normal transformation.

Exercise 10. Consider a simple transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ . Show that an inner product (, ) can be defined on $\mathcal { S }$ such that the transformation $T \in { \mathcal { L } } ( { \mathcal { U } } )$ is normal, where $\pmb { \mathcal { U } } = \mathcal { S } , ( \mathbf { \Omega } , \mathbf { \omega } )$ □

## 5.3 Hermitian, Skew-Hermitian, and Definite Matrices

The structure and properties of Hermitian matrices are particularly simple and elegant. Because such matrices arise frequently in applications, it is important that we fully understand them. In particular, A is Hermitian if $A ^ { * } = A$ .Thus, using Theorem 5.2.3, it is apparent that a Hermitian matrix is normal and so they have all the properties of normal matrices established in the previous section.

## Theorem 1. The spectrum of a Hermitian matrix is real.

ProoF. A Hermitian matrix H is normal and so, by Eq. (5.2.1), $H = U D U ^ { * }$ where U is unitary and D is a diagonal matrix of the eigenvalues of H. But $H ^ { * } = H$ implies $U \overleftrightarrow { D } U ^ { * } = U D U ^ { * }$ and hence $\begin{array} { r } { \overrightarrow { D } = D ; } \end{array}$ , from which the result follows.

More can be said: the existence of a real spectrum for a normal matrix A is a necessary and sufficient condition for A to be Hermitian.

Theorem 2. A normal matrix A is Hermitian if and only if its spectrum lies on the real line.

PROOF. Let $A ^ { * } A = A A ^ { * }$ and suppose $\sigma ( A ) \subset ( - \infty , \infty )$ . Since $A = U D U ^ { \star }$ and $A ^ { * } = U D ^ { * } U ^ { * } = U D U ^ { * }$ , it follows that $A = A ^ { * }$ and hence A is Hermitian.

The second part of this theorem is Theorem 1.

Thus Hermitian matrices, and only they, have an orthonormal eigenbasis along with a real spectrum. Another important description of Hermitian matrices follows from their definition and Theorem 5.1.1.

Exercise 1. Prove that an n × n matrix A is Hermitian if and only if (Ax, y) $\mathbf { \ x { \equiv } } = ( \mathbf { x } , A \mathbf { y } )$ for all $\mathbf { x } , \mathbf { y } \in { \mathcal { F } } ^ { n } , \ \mathbf { \partial } \bigcirc$

We know that for an arbitrary square matrix, the eigenvectors associated with distinct eigenvalues are necessarily linearly independent (Proposition 4.10.4). If the matrix is Hermitian, it is also normal and, by definition of a normal transformation, it has an orthonormal eigenbasis.

Exercise 2. Show (without using the fact that a Hermitian matrix is normal) that the eigenvectors associated with distinct eigenvalues of a Hermitian matrix are orthogonal.

It turns out that any square matrix A can be represented in terms of a pair of Hermitian matrices. Indeed, it is easy to verify that for $A \in { \mathcal { F } } ^ { n \times n }$

$$
{ \cal A } = H _ { 1 } + i H _ { 2 } ,\tag{1}
$$

where $i ^ { 2 } = - 1$ and $H _ { 1 }$ and $H _ { 2 }$ are Hermitian matrices defined by

$$
H _ { 1 } = \mathcal { R } _ { e } \ A \triangleq \frac 1 2 ( A + A ^ { * } ) , \qquad H _ { 2 } = \mathcal { I } _ { m } \ A \triangleq \frac 1 { 2 i } ( A - A ^ { * } ) .\tag{2}
$$

The representation (1) is called the Cartesian decomposition of A. Its analog in the case n == 1 is the Cartesian decomposition of a complex number in the form $z = a + i b ,$ , where a and $b$ are real.

Exercise 3. Check that a matrix A is normal if and only if its real part $( { \mathcal { R } } A )$ and imaginary part $( \mathcal { P } { M } A )$ commute.

Exercise 4. Prove that if A is normal and $\lambda \in \sigma ( A )$ , then $\lambda = \lambda _ { 1 } + i \lambda _ { 2 }$ where $\lambda _ { 1 } \in \sigma ( \mathscr { R e } A )$ and $\lambda _ { 2 } \in \sigma ( { \mathcal { A } } _ { { \mathcal { M } } } ~ A ) . ~ \varbigcup$

Consider a Hermitian matrix H of order n. Since all eigenvalues of H are real, they can be ordered: $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \cdots \leq \lambda _ { n }$ Those cases in which all eigenvalues are of one sign are particularly important. A Hermitian matrix A is said to be positive (respectively, negative) definite if all its eigenvalues are positive (respectively, negative). Obviously, a definite (i.e., either positive or negative definite) matrix is nonsingular (see Exercise 4.10.3). We shall also need some refinements: A Hermitian matrix is called positive (respectively, negative) semi-definite or nonnegative (respectively, nonpositive) definite, if all its eigenvalues are nonnegative (respectively, nonpositive). A semidefinite matrix is understood to be one of the two varieties defined above. We shall write $H > 0$ and $H \geq 0$ for positive definite and positive semidefinite matrices, respectively. Similarly, the notations $H < 0$ and $H \leq 0$ will be used for negative definite and negative semi-definite matrices.

The following result is very important and is frequently used in the definition of definite matrices. It has the great advantage of being free of ideas associated with the spectrum of A.

Theorem 3. Given a Hermitian matrix $H \in { \mathcal { F } } ^ { n \times n } , H \geq 0 \ ( o r \ H > 0 )$ if and only $i f ( H \pmb { x } , \pmb { x } ) \ge 0 \left( o r \left( H \pmb { x } , \pmb { x } \right) > 0 \right)$ for all nonzero $\pmb { x } \in \mathcal { F } ^ { n }$

ProoF. The necessity of the condition will be shown in Corollary 5.4.1.

Let $( H \mathbf { x } , x ) \geq 0$ for all $\ b { x } \in \mathcal { F } ^ { n }$ and let the eigenvectors ${ \pmb u } _ { 1 } , { \pmb u } _ { 2 } , \dots , { \pmb u } _ { n }$ of H associated with the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ , respectively, form an orthonormal basis in ${ \mathcal { F } } ^ { n }$ . Since

$$
0 \leq ( H \pmb { u } _ { i } , \pmb { u } _ { i } ) = \lambda _ { i } ( \pmb { u } _ { i } , \pmb { u } _ { i } ) = \lambda _ { i }
$$

for $i = 1 , 2 , \ldots , n ,$ the matrix H is positive semi-definite.

The positive definite case is proved similarly.■

Note that results similar to Theorem 3 hold for negative definite and semidefinite matrices

Exercise 5. Show that for any (even rectangular) matrix A, the matrices $A ^ { * } A$ and $A A ^ { * }$ are positive semi-definite

Hint. Let A be $m \times n$ and consider $( A ^ { * } A { \pmb x } , { \pmb x } )$ for $\pmb { x } \in \mathcal { F } ^ { n }$

Exercise 6. Confirm that for any $A \in { \mathcal { F } } ^ { m \times \prime }$

$$
\operatorname { K e r } ( A ^ { * } A ) = \operatorname { K e r } A , \qquad \operatorname { I m } ( A ^ { * } A ) = \operatorname { I m } A ^ { * } .
$$

Exercise 7. Deduce from Exercise 6 that the matrix $A ^ { * } A$ (where $A \in \mathcal { F } ^ { m \times n }$ and $m \geq n )$ is positive definite if and only if A is of full rank.

Exercise 8. Check that if $H _ { 1 }$ and $H _ { 2 }$ are positive definite and $\alpha , \beta \in \mathbb { R }$ are nonnegative real numbers, not both zero, then the matrices $H _ { 1 } ^ { - 1 }$ and $\alpha H _ { 1 } +$ $\beta H _ { 2 }$ are positive definite.

Exercise 9. Show that if H is positive semi-definite and rank $H = r ,$ then H has exactly r positive eigenvalues.

Exercise 10. Show that if H is any positive definite matrix, then the function ( , ) defined on $\mathbb { C } ^ { n } \times \mathbb { C } ^ { n }$ by $( { \bf x } , { \bf y } ) = { \bf y } ^ { * } H { \bf x }$ is an inner product on C". □

Skew-Hermitian matrices have a number of properties that can be seen as analogs to those of Hermitian matrices. The next two exercises give results of this kind.

Exercise 11. Prove that the spectrum of a skew-Hermitian matrix is pure imaginary.

Exercise 12. Show that a normal matrix is skew-Hermitian if and only if its spectrum lies on the imaginary axis.

Exercise 13. Let A be Hermitian and let H be a positive definite matrix of the same size. Show that AH has only real eigenvalues.

Exercise 14. Use Exercise 2.10.2 to show that, if H is positive definite, there is a unique lower triangular matrix G with positive diagonal elements such that $H = G G ^ { * }$ . (This is known as the Cholesky factorization of H.)

## 5.4 Square Root of a Definite Matrix and Singular Values

An analogy between Hermitian matrices and real numbers can be seen in the following result, which states the existence of a square root $H _ { 0 }$ of a positive semi-definite matrix H, that is, a matrix $H _ { 0 }$ such that $H _ { 0 } ^ { 2 } = H ,$

Theorem 1. A matrix H is positive definite (or semi-definite) if and only if it has a positive definite (respectively, semi-definite) square root Ho. Moreover, $H _ { 0 }$ rank $H _ { 0 } = \mathrm { r a n k }$ H.

PROOF. If $H \geq 0$ then, by definition, its eigenvalues $\{ \lambda _ { i } \} _ { i = 1 } ^ { n }$ are nonnegative and we can define a real matrix $D _ { 0 } = \mathrm { d i a g } [ \sqrt { \lambda _ { 1 } } , \sqrt { \lambda _ { 2 } } , \dots , \sqrt { \lambda _ { n } } ]$ . The matrix H is normal and hence there is a unitary matrix U such that $H =$ $U D U ^ { * }$ , where $D = D _ { 0 } ^ { 2 }$ . The required square root of H is the matrix

$$
H _ { 0 } = U D _ { 0 } U ^ { * } ,\tag{1}
$$

since $H _ { 0 } ^ { 2 } = U D _ { 0 } U ^ { * } U D _ { 0 } U ^ { * } \approx U D _ { 0 } ^ { 2 } U ^ { * } = H$ . Note that the representation (1) shows that the eigenvalues of Ho are the (arithmetic) square roots of the $H _ { 0 }$ eigenvalues of H. This proves that rank $H _ { 0 } = \mathrm { r a n k } \ H$ (Exercise 5.3.9), and $H \geq 0$ yields $H _ { 0 } \geq 0 .$

Conversely, if $H = H _ { 0 } ^ { 2 }$ and $H _ { 0 } \geq 0 ,$ then the eigenvalues of H, being the squares of those of H0, are nonnegative. Hence $H _ { 0 }$ $H \geq 0 .$ This fact also implies the equality of ranks.

The same argument proves the theorem for positive definite matrices.■

The following simple corollary gives a proof of the necessary part of Theorem 5.3.3.

Corollary 1. If $H \geq 0 \ ( o r \ H > 0 )$ , then $( H x , x ) \ge 0 \ ( o r \ ( H x , x ) > 0 )$ for all $\pmb { x } \in \mathcal { F } ^ { n }$

PRooF. Representing $H = H _ { 0 } ^ { 2 }$ and using the matrix version of Theorem 5.1.1, we have

$$
\begin{array} { r } { ( H x , x ) = ( H _ { 0 } ^ { 2 } x , x ) = ( H _ { 0 } x , H _ { 0 } x ) \geq 0 \qquad \mathrm { f o r ~ a l l ~ } x \in \mathcal { F } ^ { n } . } \end{array}
$$

Exercise 1. Prove that if H is positive semi-definite and $( H \pmb { x } , \pmb { x } ) = 0$ for some $\boldsymbol { x } \in \mathcal { F } ^ { n }$ , then $H \mathbf { x } = \mathbf { 0 }$ □

Note that the square root of a positive semi-definite matrix cannot be unique since any matrix of the form (1) with a diagonal matrix

$$
D = \mathrm { d i a g } [ \pm \sqrt { \lambda _ { 1 } } , \pm \sqrt { \lambda _ { 2 } } , . . . , \pm \sqrt { \lambda _ { n } } ]
$$

is a square root of H. However, the positive semi-definite square root H0 of $H _ { 0 }$ H is unique.

Proposition 1. Let H be positive semi-definite. The positive semi-definite square root Ho of H is unique and is given by $H _ { 0 }$ $E q . ( 1 )$

PROOF. Let $H _ { 1 }$ satisfy $H _ { 1 } ^ { 2 } = H$ . By Theorem 4.11.3, the eigenvalues of H1 are $H _ { 1 }$ square roots of those of H and, since $H _ { 1 } \geq 0$ ), they must be nonnegative. Thus, the eigenvalues of H1 and Ho of Eq. (1) coincide. Furthermore, $H _ { 1 }$ $H _ { 0 }$ $H _ { 1 }$ is Hermitian and, therefore (Theorem 5.2.1), $H _ { 1 } = V D _ { 0 } V ^ { * }$ for some unitary V. Now $H _ { 1 } ^ { 2 } = H _ { 0 } ^ { 2 } = H _  \mathrm  $ so $V D _ { 0 } ^ { 2 } V ^ { \ast } = U D _ { 0 } ^ { 2 } U ^ { \ast }$ and hence $( U ^ { * } V ) D _ { 0 } ^ { 2 } =$ $D _ { 0 } ^ { 2 } ( U ^ { * } V )$ . It is easily seen that, because $D _ { 0 } \geq 0 ,$ this implies $( U ^ { * } V ) D _ { 0 } =$ $D _ { 0 } ( U ^ { * } V )$ and, consequently, $H _ { 1 } = H _ { 0 }$ , as required.

In the sequel the unique positive semi-definite (or definite) square root of a positive semi-definite (or definite) matrix H is denoted by $H ^ { 1 / 2 }$ . Summarizing the above discussion, note that $\lambda \in \sigma ( H ^ { 1 / 2 } )$ if and only if $\lambda ^ { 2 } \in \sigma ( H )$ , and the corresponding eigenspaces of $H ^ { 1 / 2 }$ and H coincide. The concept of a square root of a positive semi-definite matrix allows us to introduce a spectral characteristic for rectangular matrices.

Consider an arbitrary m × n matrix A. The n × n matrix $A ^ { * } A$ is (generally) positive semi-definite (see Exercise 5.3.5). Therefore by Theorem 1 the matrix $A ^ { * } A$ has a positive semi-definite square root $H _ { 1 }$ such that $A ^ { * } A = H _ { 1 } ^ { 2 }$ The eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ of the matrix $H _ { 1 } = ( A ^ { * } A ) ^ { 1 / 2 }$ are referred to as the singular values $s _ { 1 } , s _ { 2 } , \ldots , s _ { n }$ of the (generally rectangular) matrix A. Thus, for $i = 1 , 2 , \ldots , n ,$

$$
s _ { i } ( A ) \triangleq \lambda _ { i } ( ( A ^ { * } A ) ^ { 1 / 2 } ) .
$$

Obviously, the singular values of a matrix are nonnegative numbers.

Exercise 2. Check that $s _ { 1 } = \sqrt { 2 } , s _ { 2 } = 1$ are singular values of the matrix

$$
A = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } . \quad \sqcap
$$

Note that the singular values of A are sometimes defined as eigenvalues of the matrix $( A A ^ { * } ) ^ { 1 / \bar { 2 } }$ of order m. It follows from the next fact that the difference in definition is not highly significant.

Theorem 2. The nonzero eigenvalues of the matrices $( A ^ { * } A ) ^ { 1 / 2 }$ and $( A A ^ { * } ) ^ { 1 / 2 }$ coincide.

ProoF. First we observe that it suffices to prove the assertion of the theorem for the matices $A ^ { * } A$ and $A A ^ { * }$ . Furthermore, we select eigenvectors ${ \mathfrak { x } } _ { 1 } , { \mathfrak { x } } _ { 2 } , \ldots , { \mathfrak { x } } _ { n }$ of $A ^ { * } A$ corresponding to the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ such that $\{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \ldots , \pmb { x } _ { n } \}$ forms an orthonormal basis in ${ \mathcal { F } } ^ { n }$ We have

$$
( A ^ { * } A { \bf x } _ { i } , { \bf x } _ { j } ) = \lambda _ { i } ( { \bf x } _ { i } , { \bf x } _ { j } ) = \lambda _ { i } \delta _ { i j } , \qquad 1 \leq i , j \leq n .
$$

On the other hand, $( A ^ { * } A x _ { i } , x _ { j } ) = ( A x _ { i } , A x _ { j } )$ , and comparison shows that $( A x _ { i } , A x _ { i } ) = \lambda _ { i } , i = 1 , 2 , . . . , \dot { n } .$ Thus, $A { \boldsymbol { \mathbf { \mathit { x } } } } _ { i } = \theta \left( 1 \leq i \leq n \right)$ if and only if $\lambda _ { i } = 0$ Since

$$
A A ^ { * } ( A x _ { i } ) = A ( A ^ { * } A x _ { i } ) = \lambda _ { i } ( A x _ { i } ) , \qquad 1 \leq i \leq n ,
$$

the preceding remark shows that for $\lambda _ { i } \neq 0$ , the vector $A \mathbf { x } _ { i }$ is an eigenvector of $A A ^ { * }$ . Hence if a nonzero $\lambda _ { i } \in \sigma ( A ^ { * } A )$ is associated with the eigenvector $\mathbf { \lambda } _ { \mathbf { \lambda } _ { \mathbf { \lambda } } } \mathbf { \hat { x } } _ { i } ,$ then $\lambda _ { i } \in \sigma ( A A ^ { * } )$ )and is associated with the eigenvector Ax. In particular, $A { \mathfrak { x } } _ { i }$ $\sigma ( A ^ { * } A ) \subset \sigma ( A A ^ { * } )$ ). The opposite inclusion is obtained by exchanging the roles of A and $A ^ { * }$

Thus the eigenvalues of A\*A and AA\*, as well as of $A ^ { * } A$ $A A ^ { * }$ $( A ^ { * } A ) ^ { 1 / 2 }$ and $( A A ^ { * } ) ^ { 1 / 2 }$ differ only by the geometric multiplicity of the zero eigenvalue, which is $n \sim r$ for $A ^ { * } A$ and $m - r$ for $A A ^ { * }$ , where $r = \operatorname { r a n k } ( A ^ { * } A ) = \operatorname { r a n k } ( A A ^ { * } )$ Also, for a square matrix A it follows immediately that the eigenvalues of $A ^ { * } A$ and AA\* coincide and have the same multiplicities. [Compare this with $A A ^ { * }$ the result of Exercise 4.14.10(b).]

Note that we proved more than was stated in Theorem 2.

Exercise 3. Show that if ${ \mathfrak { x } } _ { 1 } , { \mathfrak { x } } _ { 2 } , \ldots , { \mathfrak { x } } _ { k }$ are orthonormal eigenvectors of $A ^ { * } A$ corresponding to nonzero eigenvalues, then $A x _ { 1 } , A x _ { 2 } , \ldots , A x _ { k }$ are orthogonal eigenvectors of $A A ^ { * }$ corresponding to the same eigenvalues. A converse statement is obtained by replacing A by $A ^ { * }$

Exercise 4. Verify that the nonzero singular values of the matrices A and $A ^ { * }$ are the same. $\mathbf { I f } ,$ in addition, A is a square $n \times n$ matrix, show that $s _ { i } ( A ) =$ $s _ { i } ( A ^ { * } )$ for $i = 1 , 2 , \ldots , n .$ □

In the rest of this section only square matrices are considered.

Proposition 2. The singular values of a square matrix are invariant under unitary transformation.

In other words, for any unitary matrix $U \in \mathbb { C } ^ { n \times n }$ and any $A \in \mathbb { C } ^ { n \times n } ,$

$$
s _ { i } ( A ) = s _ { i } ( U A ) = s _ { i } ( A U ) , \quad \quad i = 1 , 2 , \ldots , n .\tag{2}
$$

PRoOF. By definition,

$$
s _ { i } ( U A ) = \lambda _ { i } ( ( A ^ { * } U ^ { * } U A ) ^ { 1 / 2 } ) = \lambda _ { i } ( ( A ^ { * } A ) ^ { 1 / 2 } ) = s _ { i } ( A ) .
$$

To prove the second equality in Eq. (2), use Exercise 4 and the part of the proposition already proved.

Theorem 3. For an n × n normal matrix $A \in { \mathcal { F } } ^ { n \times n } ,$

$$
s _ { i } ( A ) = | \lambda _ { i } ( A ) | , \qquad i = 1 , 2 , \ldots , n .
$$

ProoF. Let λ, denote an eigenvalue of A associated with the eigenvector x. $\lambda _ { i }$ $\pmb { x _ { i } }$ Since $A ^ { * } A = A A ^ { * }$ , it follows (see Exercise 5.2.7) that

$$
A ^ { * } A x _ { i } = \lambda _ { i } A ^ { * } x _ { i } = \lambda _ { i } \bar { \lambda } _ { i } x _ { i } = | \lambda _ { i } | ^ { 2 } x _ { i } .\tag{3}
$$

Hence $\mathbf { \pmb { x } } _ { i }$ is an eigenvector of $A ^ { * } A$ corresponding to the eigenvalue $| \lambda _ { i } | ^ { 2 }$ By definition, | λ is a singular value of A. Note that A has no other singular $| \lambda _ { i } |$ values, since in varying i from 1 to n in $\mathbf { E q . } \left( 3 \right)$ , all the eigenvalues of $A ^ { * } A$ are obtained.

Exercise 5. Check that for any $n \times n$ matrix A,

$$
| \operatorname * { d e t } A | = s _ { 1 } ( A ) s _ { 2 } ( A ) \cdot \cdot \cdot s _ { n } ( A ) .
$$

Hint. If $H ^ { 2 } = A ^ { * } A$ , where $H \geq O ,$ then det $H = | \operatorname* { d e t } A |$

Exercise 6. Confirm that a square matrix is unitary if and only if all its singular values are equal to one.

Exercise 7. Let $A \in \mathbb { C } ^ { m \times n }$ and $A = Q R$ be the “Q-R decomposition" of A described in Exercise 3.12.7. Show that A and R have the same singular values.□

## 5.5 Congruence and the Inertia of a Matrix

The notion of unitary similarity discussed in Section 5.2 can be generalized in the following way. Two square matrices A and B are said to be congruent if there exists a nonsingular matrix P such that

$$
A = P B P ^ { * } .\tag{1}
$$

It is clear that for a unitary P the matrix A is unitarily similar to B. Also, congruence is an equivalence relation on ${ \mathcal { F } } ^ { n \times n }$ . It is also obvious from Eq. (1) that if A is Hermitian then all matrices in the equivalence class of A are Hermitian. In Theorem 1 it will be shown that there is a particularly simple canonical matrix in each such class of Hermitian matrices.

Theorem 1. A Hermitian matrix $H \in \mathcal { F } ^ { n \times n }$ is congruent to the matrix

$$
D _ { 0 } = \left[ { \begin{array} { c c c } { I _ { s } } & { 0 } & { 0 } \\ { 0 } & { - I _ { r ^ { - s } } } & { 0 } \\ { 0 } & { 0 } & { 0 _ { n - r } } \end{array} } \right] ,\tag{2}
$$

where r = rank H and s is the number of positive eigenvalues of H counted according to multiplicities.

In other words, the matrix $D _ { 0 }$ in Eq. (2) is the canonical form of H with respect to congruence; it is the simplest representative of the equivalence class of Hermitian matrices congruent to H.

ProOF. By Theorem 5.2.1,

$$
H = U D U ^ { * } ,\tag{3}
$$

where D is a diagonal matrix of the eigenvalues of $H ,$ and U is unitary.

Ordering the eigenvalues so that the first s scalars $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ on the main diagonal of D are positive and the next $r \mathrm { ~ - ~ } s$ numbers $\lambda _ { s + 1 } , \lambda _ { s + 2 } , \ldots , \lambda _ { r }$ are negative, we may write ${ \cal D } = U _ { 1 } D _ { 1 } D _ { 0 } D _ { 1 } U _ { 1 } ^ { * }$ , where

$$
D _ { 1 } = \mathrm { d i a g } [ \sqrt { \lambda _ { 1 } } , \sqrt { \lambda _ { 2 } } , \ldots , \sqrt { \lambda _ { s } } , \sqrt { | \lambda _ { s + 1 } | } , \ldots , \sqrt { | \lambda _ { r } | } , 0 , \ldots , 0 ] ,
$$

$D _ { 0 }$ is given by Eq. (2), and U, is a permutation (and therefore a unitary) $U _ { 1 }$ matrix. Hence, substituting into (3), we obtain $H = P D _ { 0 } P ^ { * }$ , where $P =$ $U U _ { 1 } D _ { 1 }$ . The theorem is established.

Corollary 1. A Hermitian matrix $H \in { \mathcal { F } } ^ { n \times n }$ is positive definite if and only if it is congruent to the identity matrix.

In other words, $H > 0$ if and only if $H = P P ^ { * }$ for some nonsingular matrix P.

Corollary 2. A Hermitian matrix $H \in \mathcal { F } ^ { n \times n }$ of rank r is positive semideinite if and only if it is congruent to a matrix of the form

$$
\left[ \begin{array} { l l } { I _ { r } } & { 0 } \\ { 0 } & { \operatorname { \cal O } _ { n - r } } \end{array} \right] .
$$

Thus $H \ge O$ if and only if $H = P ^ { * } P$ for some P.

Corollary 3. Two Hermitian matrices A, $B \in \mathcal { F } ^ { n \times n }$ are congruent if and only if rank A = rank B and the number of positive eigenvalues (counting multiplicities) of both matrices is the same.

We already know that a Hermitian matrix H can be reduced by a congruence transformation to a diagonal matrix. If several Hermitian matrices are given, then each of them can be reduced to diagonal form by means of (generally distinct) congruence transformations.

The important problem of the simultaneous reduction of two Hermitian matrices to diagonal form using the same congruence transformation will now be discussed. This turns out to be possible provided one of the Hermitian matrices is positive (or negative) definite. If this condition is relaxed, the question of canonical reduction becomes significantly more complicated.

Theorem 2. If $H _ { 1 }$ and $H _ { 2 }$ are two $n \times n$ Hermitian matrices and at least one of them, say H1, is positive deinite, then there exists a nonsingular matrix Q $H _ { 1 }$ such that

$$
Q ^ { * } H _ { 1 } Q = I \qquad a n d \qquad Q ^ { * } H _ { 2 } Q = D ,\tag{4}
$$

where $D = \mathrm { d i a g } [ \lambda _ { 1 } , \dots , \lambda _ { n } ]$ and $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ are the eigenvalues of $H _ { 1 } ^ { - 1 } H _ { 2 }$ all of which are real

Furthermore, $i f q _ { j }$ denotes the jth column of Q, then for $j = 1 , 2 , \dots , n ,$

$$
( \lambda _ { j } H _ { 1 } - H _ { 2 } ) \pmb { q } _ { j } = \pmb { 0 } .\tag{5}
$$

PROOF. Let $H _ { 1 } ^ { 1 / 2 }$ be the positive definite square root of $H _ { 1 }$ and define $H _ { 1 } ^ { - 1 / 2 } = \big ( H _ { 1 } ^ { 1 / 2 } \big ) ^ { - 1 }$ . Observe that $H = H _ { 1 } ^ { - 1 / 2 } \bar { H } _ { 2 } H _ { 1 } ^ { - 1 / 2 }$ is Hermitian, and so there is a unitary matrix U such that $U ^ { * } H U = \mathrm { d i a g } [ \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n } ] \triangleq D ,$ a real diagonal matrix, where $\lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { n }$ are the eigenvalues of H. Since $H = H _ { 1 } ^ { 1 / 2 } ( H _ { 1 } ^ { - 1 } H _ { 2 } ) H _ { 1 } ^ { - 1 / 2 }$ , the matrices H and $H _ { 1 } ^ { - 1 } \pmb { H } _ { 2 }$ are similar. It follows that $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ are also the eigenvalues of $H _ { 1 } ^ { - 1 } H _ { 2 }$ and are real.

Now define $Q = H _ { 1 } ^ { - 1 / 2 } U$ ; we have

$$
Q ^ { * } H _ { 1 } Q = U ^ { * } H _ { 1 } ^ { - 1 / 2 } H _ { 1 } H _ { 1 } ^ { - 1 / 2 } U = U ^ { * } U = I ,
$$

$$
Q ^ { * } H _ { 2 } Q = U ^ { * } H _ { 1 } ^ { - 1 / 2 } H _ { 2 } H _ { 1 } ^ { - 1 / 2 } U = U ^ { * } H U = D ,\tag{6}
$$

as required for the first part of the theorem.

It is clear from Eqs. (6) that

$$
( Q ^ { * } H _ { 1 } Q ) D - Q ^ { * } H _ { 2 } Q = 0 ,
$$

and this implies $H _ { 1 } Q D - H _ { 2 } Q = O$ The jth column of this relation is Eq. (5). ■

Exercise 1. Show that if the matrices $H _ { 1 }$ and $H _ { 2 }$ of Theorem 2 are real, then there is a real transforming matrix $Q$ with the required properties.

Exercise 2. Prove that the eigenvalues of $H _ { 1 } ^ { - 1 } \pmb { H } _ { 2 }$ in Theorem 2 are real by first defining an inner product $\langle \pmb { x } , \pmb { y } \rangle = \pmb { y } ^ { * } \pmb { H } _ { 1 } \pmb { x }$ and then showing that $H _ { 1 } ^ { - 1 } H _ { 2 }$ is Hermitian in this inner product.

We conclude our discussion on the simultaneous reduction of a pair of Hermitian matrices to a diagonal form by noting that this is not always possible.

Exercise 3. Show that there is no nonsingular matrix $Q$ such that both matrices

$$
Q ^ { * } { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } Q \qquad { \mathrm { a n d } } \qquad Q ^ { * } { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] } Q
$$

are diagonal.

In the study of differential equations, the analysis of stability of solutions requires information on the location of the eigenvalues of matrices in relation to the imaginary axis. Many important conclusions can be deduced by knowing only how many eigenvalues are located in the right and left halfplanes and on the imaginary axis itself. These numbers are summarized in the notion of "inertia." The inertia of a square matrix $A \in { \mathcal { F } } ^ { n \times n }$ , written In A, is the triple of integers

$$
{ \mathrm { I n ~ } } A = \{ \pi ( A ) , \nu ( A ) , \delta ( A ) \} ,
$$

where $\pi ( A ) \nu ( A )$ and $\delta ( A )$ denote the number of eigenvalues of A, counted with their algebraic multiplicities, lying in the open right half-plane, in the open left half-plane, and on the imaginary axis, respectively. Obviously,

$$
\pi ( A ) + \nu ( A ) + \delta ( A ) = n
$$

and the matrix A is nonsingular if $\delta ( A ) = 0 .$

In the particular case of a Hermitian matrix H, the number $\pi ( H )$ (respectively, $\nu ( H ) )$ merely denotes the number of positive (respectively, negative) eigenvalues counted with their multiplicities. Furthermore, $\delta ( H )$ is equal to the number of zero eigenvalues of H, and hence, H is nonsingular if and only if $\delta ( H ) = 0$ Note also that for a Hermitian matrix H,

$$
\pi ( H ) + \nu ( H ) = \operatorname { r a n k } H .
$$

The difference $\pi ( H ) - \nu ( H )$ , written sig H, is referred to as the signature of H.

The next result gives a useful sufficient condition for two matrices to have the same inertia. The corollary is a classical result that can be proved more readily by a direct calculation. The interest of the theorem lies in the fact that matrix M of the hypothesis may be singular.

Theorem 3. Let A and B be $n \times n$ Hermitian matrices of the same rank r. $H A = M B M ^ { * }$ for some matrix M, then In $A = \operatorname { I n } B .$

ProoF. By Theorem 1 there exist nonsingular matrices P and Q such that

$$
P A P ^ { * } = \mathrm { d i a g } [ I _ { t } , \quad - I _ { r - t } , \quad 0 ] \triangleq { \cal D } _ { 0 } ^ { ( 1 ) }
$$

and

$$
Q ^ { - 1 } B ( Q ^ { - 1 } ) ^ { * } = \mathrm { d i a g } [ I _ { s } , - I _ { r - s } , 0 ] \triangleq D _ { 0 } ^ { ( 2 ) } ,
$$

where t and s denote the number of positive eigenvalues of A and B, respectively; $t = \pi ( A )$ and $s = \pi ( B )$

To prove the theorem it suffices to show that $s = t .$ Observe that, since $A = M B M ^ { * }$ 2

$$
D _ { 0 } ^ { ( 1 ) } = P A P ^ { * } = P M ( { Q } D _ { 0 } ^ { ( 2 ) } Q ^ { * } ) M ^ { * } P ^ { * }
$$

or, writing $R = P M Q$

$$
D _ { 0 } ^ { ( 1 ) } = R D _ { 0 } ^ { ( 2 ) } R ^ { * } .\tag{7}
$$

Now suppose $s < t$ and let us seek a contradiction. Let $\mathbf { x } \in \mathcal { F } ^ { n }$ be given by $\pmb { x } = \left[ \begin{array} { c } { \pmb { x } _ { 1 } } \\ { \pmb { 0 } } \end{array} \right]$ , where $\pmb { x } _ { 1 } = [ \pmb { x } _ { 1 } \quad \pmb { x } _ { 2 } \quad \cdots \quad \pmb { x } _ { i } ] ^ { \mathbf { T } } \in \mathcal { F } ^ { t }$ and $\pmb { x } _ { 1 } \neq \pmb { 0 }$ Then

$$
x ^ { * } D _ { 0 } ^ { ( 1 ) } x = \sum _ { i = 1 } ^ { t } | x _ { i } | ^ { 2 } > 0 .\tag{8}
$$

Partition $R ^ { * }$ in the form

$$
R ^ { * } = \left[ \begin{array} { l l } { R _ { 1 } } & { R _ { 2 } } \\ { R _ { 3 } } & { R _ { 4 } } \end{array} \right] ,
$$

where $R _ { 1 }$ is $s \times t .$ Since $s < t ,$ an $\pmb { x } _ { 1 }$ can be chosen so that $\ b x _ { 1 } \neq \pmb \theta$ and $R _ { 1 } \pmb { x } _ { 1 } =$ 0. Then define ${ \pmb y } = R _ { 3 } { \pmb x } _ { 1 } \in \mathcal { F } ^ { n - s }$ and we have $R ^ { * } x = { \binom { 0 _ { s } } { y } }$ . Consequently, using Eq. (7) and writing $\pmb { y } = [ y _ { 1 } , y _ { 2 } , \dots , y _ { n - s } ] ^ { \mathbf { T } }$

$$
x ^ { * } D _ { 0 } ^ { ( 1 ) } x = ( R ^ { * } x ) ^ { * } D _ { 0 } ^ { ( 2 ) } ( R ^ { * } x ) = - \sum _ { j = 1 } ^ { r - s } | y _ { j } | ^ { 2 } \leq 0 ,
$$

and a contradiction with Eq. (8) is achieved.

Similarly, interchanging the roles of $D _ { 0 } ^ { ( 1 ) }$ and $D _ { 0 } ^ { ( 2 ) } .$ , it is found that $t < s$ is impossible. Hence $s = t$ and the theorem is proved.

Corollary 1. (Sylvester's law of inertia). Congruent Hermitian matrices have the same inertia characteristics.

PROOF. If $A = P B P ^ { * }$ and P is nonsingular, then rank $A = \operatorname { r a n k } B$ and the result follows.

Exercise 4. Show that the inertia of the Hermitian matrix

$$
\left[ { \begin{array} { l l } { 0 } & { i I _ { n } } \\ { - i I _ { n } } & { 0 } \end{array} } \right]
$$

is $( n , n , 0 )$ □

## 5.6 Unitary Matrices

We now continue the study of unitary matrices. Recall that a square matrix U is unitary if it satisfies the condition $U ^ { * } U = U U ^ { * } = I$

Theorem 1. The spectrum of a unitary matrix lies on the unit circle.

PROOF. If $U { \pmb x } = \lambda { \pmb x }$ and $( { \pmb x } , { \pmb x } ) = 1$ , we obtain

$$
( U \mathbf { x } , U \mathbf { x } ) = \left( U ^ { * } U \mathbf { x } , \mathbf { x } \right) = ( \mathbf { x } , \mathbf { x } ) = 1 .
$$

On the other hand,

$$
( U \mathbf { x } , U \mathbf { x } ) = ( \lambda \mathbf { x } , \lambda \mathbf { x } ) = | \lambda | ^ { 2 } ( \mathbf { x } , \mathbf { x } ) = | \lambda | ^ { 2 } .
$$

The comparison yields $| \lambda | ^ { 2 } = 1$ and the desired result.

The converse of this statement is also true for normal matrices. (It is an analog of Theorem 5.3.2 for Hermitian matrices).

Theorem 2. A normal matrix $A \in { \mathcal { F } } ^ { n \times n }$ is unitary if all its eigenvalues lie on the unit circle.

PROOF. Let $A \mathbf { x } _ { i } = \lambda _ { i } \mathbf { x } _ { i }$ , where $| \lambda _ { i } | = 1$ and $( x _ { i } , x _ { j } ) = \delta _ { i j } \ ( 1 \leq i , j \leq n )$ For any vector $\ b { x } \in \mathcal { F } ^ { n }$ , write $\begin{array} { r } { { \pmb x } = \sum _ { i = 1 } ^ { n } { \pmb \alpha } _ { i } { \pmb x } _ { i } } \end{array}$ ; then it is found that

$$
A ^ { * } A { \boldsymbol { \mathbf { \mathit { x } } } } = A ^ { * } { \biggl ( } \sum _ { i = 1 } ^ { n } \alpha _ { i } A x _ { i } { \biggr ) } = A ^ { * } { \biggl ( } \sum _ { i = 1 } ^ { n } \alpha _ { i } \lambda _ { i } x _ { i } { \biggr ) } .\tag{1}
$$

From Exercise 5.2.7 we know that $A ^ { * } x _ { i } = \bar { \lambda } _ { i } \mathbf { x } _ { i } ( i = 1 , 2 , \ldots , n )$ , so Eq. (1) becomes

$$
A ^ { * } A x = \sum _ { i = 1 } ^ { n } \alpha _ { i } \lambda _ { i } A ^ { * } x _ { i } = \sum _ { i = 1 } ^ { n } \alpha _ { i } \vert \lambda _ { i } \vert ^ { 2 } \mathbf { x } _ { i } = \sum _ { i = 1 } ^ { n } \alpha _ { i } \mathbf { x } _ { i } = \mathbf { x } .
$$

Thus $A ^ { * } A { \mathbf { x } } = { \mathbf { x } }$ for every $\pmb { x } \in \mathcal { F } ^ { n }$ and therefore $A ^ { * } A = I$ The relation, $A A ^ { * } = I$ now follows since a left inverse is also a right inverse (see Section 2.6). Hence the matrix A is unitary.

Thus, a normal matrix is unitary if and only if its eigenvalues lie on the unit circle. Unitary matrices can also be described in terms of the standard inner product. In particular, the next result shows that if U is unitary, then for any x the vectors x and Ux have the same Euclidean length or norm.

Theorem 3. A matrix $U \in \mathcal { F } ^ { n \times n }$ is unitary if and only if

$$
( U \mathbf { x } , U \mathbf { y } ) = ( \mathbf { x } , y )\tag{2}
$$

for all $x , y \in { \mathcal { F } } ^ { n } .$

PROOF. If $U ^ { * } U = I ,$ then

$$
( U \pmb { x } , U y ) = ( U ^ { * } U \pmb { x } , y ) = ( \pmb { x } , \pmb { y } )
$$

and Eq. (2) holds. Conversely, from Eq. (2) it follows that $( U ^ { * } U x , y ) = ( { \boldsymbol { x } } , { \boldsymbol { y } } )$ or, equivalently, $( ( U ^ { * } U - I ) x , y ) = 0$ for all $\mathbf { x } , \mathbf { y } \in \mathcal { F } ^ { n } ,$ . Referring to Exercise 3.13.2, we immediately obtain $U ^ { * } U = I$ . Consequently, $U U ^ { * } = I$ also, and U is a unitary matrix.

Observe that Eq. (2) holds for every x, $y \in { \mathcal { F } } ^ { n }$ if and only if it is true for the vectors of a basis in ${ \mathcal { F } } ^ { n }$ . (Compare the statement of the next Corollary with Exercise 3.14.12.)

Corollary 1. A matrix $U \in { \mathcal { F } } ^ { n \times n }$ is unitary if and only if it transforms an orthonormal basis for ${ \mathcal { F } } ^ { n }$ into an orthonormal basis.

Now take the elements $\boldsymbol { e } _ { i } ( i = 1 , 2 , \dots , n )$ of the standard basis in ${ \mathcal { F } } ^ { n }$ for x and y in Eq. (2).

Corollary 2. A matrix $U \in \mathcal { F } ^ { n \times n }$ is unitary if and only if the columns of U, viewed as vectors of ${ \mathcal { F } } ^ { n }$ , constitute an orthonormal basis in ${ \mathcal { F } } ^ { n }$

Note, in conclusion, that some properties of unitary matrices are reminiscent of those of the unimodular complex numbers $e ^ { i \gamma } { \mathrm { : } }$ ,where $0 \leq \gamma < 2 \pi$ . In particular, it follows from Theorem 1 that all eigenvalues of a unitary matrix are of this form. The polar form of more general complex numbers is the starting point for our next topic.

Exercise 1. (Householder transformations). Let x be a nonzero vector in $\mathbb { C } ^ { n }$ and define the $n \times n$ matrix

$$
U = I - \alpha x x ^ { * } ,
$$

where $\alpha = 2 ( \pmb { x } ^ { * } \pmb { x } ) ^ { - 1 }$ . Show that U is both Hermitian and unitary. Find the n eigenvalues of U and an associated orthonormal eigenbasis.

## 5.7 Polar and Singular-Value Decompositions

The following result has its origin in the familiar polar form of a complex number: $\lambda = \lambda _ { 0 } e ^ { i \gamma }$ , where $\lambda _ { 0 } \geq 0$ and $0 \leq \gamma < 2 \pi$

Theorem 1. Any matrix $A \in { \mathcal { F } } ^ { n \times n }$ can be represented in the form

$$
A = H U ,\tag{1}
$$

where $H \geq \theta$ and U is unitary. Moreover, the matrix H in $E q . ( 1 )$ is unique and is given by $H = ( A A ^ { * } ) ^ { 1 / 2 }$

PROOF. Let

$$
\lambda _ { 1 } \geq \lambda _ { 2 } \geq \cdots \geq \lambda _ { r } > 0 = \lambda _ { r + 1 } = \cdots = \lambda _ { n }
$$

denote the eigenvalues of $A ^ { * } A$ (see Theorem 5.4.2) with corresponding eigenvectors ${ \mathfrak { x } } _ { 1 } , { \mathfrak { x } } _ { 2 } , \ldots , { \mathfrak { x } } _ { n }$ that comprise an orthonormal basis in ${ \mathcal { F } } ^ { n }$

Then, by Exercise 5.4.3, the normalized elements

$$
y _ { i } = { \frac { 1 } { \| A x _ { i } \| } } A { \mathbf { x } } _ { i } = { \frac { 1 } { \sqrt { \lambda _ { i } } } } A x _ { i } , \qquad i = 1 , 2 , \ldots , r ,\tag{2}
$$

are orthonormal eigenvectors of $A A ^ { * }$ corresponding to the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { r }$ , respectively. Choosing an orthonormal basis $\{ y _ { r + 1 } , \ldots , y _ { n } \}$ in Ker $A A ^ { * }$ , we extend it to an orthonormal eigenbasis $\left\{ y _ { i } \right\} _ { i = 1 } ^ { n }$ for $A A ^ { * }$

Proceeding to a construction of the matrices H and U in Eq. (1), we write $H = ( A A ^ { * } ) ^ { 1 / 2 }$ and note (see Section 5.4) that $H y _ { i } = ( \lambda _ { i } ) ^ { 1 / 2 } y _ { i } { \mathrm { f o r } } i = 1 , 2 , \ldots , n .$ Also, we introduce an $n \times n$ (transition) matrix U by $U \pmb { x } _ { i } = y _ { i } , i = 1 , 2 , \ldots , n .$ Note that Corollary 5.6.1 asserts that U is unitary. We have

$$
H U \pmb { x } _ { i } = H \pmb { y } _ { i } = \sqrt { \lambda _ { i } } y _ { i } = A \pmb { x } _ { i } , \qquad i = 1 , 2 , \ldots , r .\tag{3}
$$

Since $( A \pmb { x } _ { i } , A \pmb { x } _ { i } ) = ( A ^ { \ast } A \pmb { x } _ { i } , \pmb { x } _ { i } ) = \lambda _ { i } = 0$ for $i = r + 1 , r + 2 , \ldots , n ,$ it follows that $A { \mathbf { } x } _ { i } = \theta \left( r + 1 \leq i \leq n \right)$ . Furthermore, as observed in Section 5.4, $A A ^ { * } y _ { i } = \theta$ implies $H y _ { i } = \theta .$ Thus

$$
H U x _ { i } = H y _ { i } = \theta = A x _ { i } , \qquad i = r + 1 , \ldots , n .\tag{4}
$$

The equalities (3) and (4) for basis elements clearly give $H U x = A x$ for all $\ b { x } \in \mathcal { F } ^ { n }$ , proving Eq. (1). ■

Note that if A is nonsingular, so is $( A A ^ { * } ) ^ { 1 / 2 }$ and in the polar decomposition (1), the matrix $H = ( A A ^ { * } ) ^ { 1 / 2 }$ is positive definite. Observe that in this case the unitary matrix U can be chosen to be $H ^ { - 1 } A$ and the representation (1) is unique.

A dual polar decomposition can be established similarly.

Exercise 1. Show that any $A \in { \mathcal { F } } ^ { n \times n }$ can be represented in the form

$$
A = U _ { 1 } H _ { 1 } ,\tag{5}
$$

where $H _ { 1 } = ( A ^ { * } A ) ^ { 1 / 2 }$ and $U _ { 1 }$ is unitary. □

For normal matrices both decompositions coincide in the following sense.

Proposition 1. A matrix $A \in { \mathcal { F } } ^ { n \times n }$ is normal if and only if the matrices H and U in Eq. (1) commute.

PROOF. If $A = H U = U H _ { \cdot }$ then

$$
A ^ { * } A = ( H U ^ { * } ) ( U H ) = H ^ { 2 } = ( H U ) ( U ^ { * } H ) = A A ^ { * }
$$

and A is normal.

Conversely. let A be normal and adopt the notations used in the proof of Theorem 1. Since $A A ^ { * } = A ^ { * } A$ , the system $\{ { \pmb x } _ { i } \} _ { i = 1 } ^ { n }$ is an orthonormal eigenbasis for $A A ^ { * }$ and, consequently, for $\dot { H } = ( A A ^ { * } ) ^ { 1 / 2 }$ . Hence, for $i = 1 , 2 , \ldots , n ,$

$$
U H \mathbf { x } _ { i } = { \sqrt { \lambda _ { i } } } U \mathbf { x } _ { i } .\tag{6}
$$

Furthermore, from $A = H U$ it follows that $\lambda _ { i } { x _ { i } } = A ^ { * } A { x _ { i } } = U ^ { * } H ^ { 2 } U { x _ { i } }$ , and consequently $H ^ { 2 } U { \bf x } _ { i } = \lambda _ { i } U { \bf x } _ { i }$ . Thus the vectors $U { \pmb x } _ { i }$ are eigenvectors of

$H ^ { 2 }$ corresponding to the eigenvalues $\lambda _ { i } ( i = 1 , 2 , \ldots , n )$ . Then the matrix H has the same eigenvectors corresponding to the eigenvalues $\sqrt { \lambda _ { i } }$ , respectively:

$$
H U \pmb { x } _ { i } = \sqrt { \lambda _ { i } } U \pmb { x } _ { i } , \qquad i = 1 , 2 , \ldots , n .
$$

Comparing this with Eq. (6), it is deduced that $U H = H U .$ as required.■

Exercise 2. Check that if $\lambda = \lambda _ { 0 } e ^ { i \gamma } ( \lambda _ { 0 } > 0 )$ is a nonzero eigenvalue of a normal matrix A, then $\lambda _ { 0 }$ is an eigenvalue of H while $e ^ { i \gamma }$ is an eigenvalue of U in the polar decomposition (1).

Exercise 3. Check that the representation

$$
A \triangleq { \left[ \begin{array} { l l } { 0 } & { 2 } \\ { 0 } & { 2 } \end{array} \right] } = { \left[ \begin{array} { l l } { \alpha ^ { - 1 } } & { \alpha ^ { - 1 } } \\ { \alpha ^ { - 1 } } & { \alpha ^ { - 1 } } \end{array} \right] } { \left[ \begin{array} { l l } { \alpha } & { \alpha } \\ { - \alpha } & { \alpha } \end{array} \right] } , \qquad \alpha = { \frac { 1 } { \sqrt { 2 } } } ,
$$

is a polar decomposition of A. Find its dual polar decomposition.

The procedure used in proving Theorem 1 can be developed to prove another important result

Theorem 2. Let A denote an arbitrary matrix from ${ \mathcal { F } } ^ { m \times n }$ and let $\left\{ s _ { i } \right\} _ { i = 1 } ^ { r }$ be the nonzero singular values of A. Then A can be represented in the form

$$
A = U D V ^ { * } ,\tag{7}
$$

where $U \in \mathcal { F } ^ { m \times m }$ and $V \in \mathcal { F } ^ { n \times n }$ are unitary and the m × n matrix D has $s _ { i }$ in the i, i position $( 1 \leq i \leq r )$ and zeros elsewhere.

The representation (7) is referred to as a singular-value decomposition of the matrix A.

ProoF. Let us agree to preserve the notation introduced in the proof of Theorem 1. Note only that now the matrix A is generally a rectangular matrix and the systems of eigenvectors $\{ { \pmb x } _ { i } \} _ { i = 1 } ^ { n }$ for $A ^ { * } A$ and $\{ y _ { j } \} _ { j = 1 } ^ { m }$ for $A A ^ { * }$ are now orthonormal bases in ${ \mathcal { F } } ^ { n }$ and ${ \mathcal { F } } ^ { m }$ , respectively. We have [see Eq. (2)]

$$
A { \pmb x } _ { i } = \sqrt { \lambda _ { i } } { \pmb y } _ { i } , \qquad i = 1 , 2 , \ldots , r ,\tag{8}
$$

and, by definition of $\pmb { x } _ { i }$ (see Exercise 5.3.6), $A x _ { i } = \theta \left( r + 1 \leq i \leq n \right)$

Now we construct matrices

$$
V = \left[ \ b { x } _ { 1 } \quad \ b { x } _ { 2 } \quad \cdots \quad \ b { x } _ { n } \right] \qquad \mathrm { a n d } \qquad \ b { U } = \left[ \ b { y } _ { 1 } \quad \ b { y } _ { 2 } \quad \cdots \quad \ b { y } _ { m } \right]\tag{9}
$$

and note that, according to Corollary 5.6.2, they are unitary. Since by definition $s _ { i } = \sqrt { \lambda _ { i } } ( i = 1 , 2 , \ldots , n )$ , the relation (8) implies

$$
A V = [ s _ { 1 } y _ { 1 } s _ { 2 } y _ { 2 } \dotsm s _ { r } y _ { r } \theta \dotsm \theta ] = U D ,
$$

where D is the matrix in Eq. (7). Thus, the representation (7) is established.

Note the structure of the matrices U and V in Eqs. (7) and (9): the columns of U (respectively, V) viewed as vectors from ${ \mathcal { F } } ^ { m }$ (respectively, ${ \mathcal { F } } ^ { n } )$ constitute an orthonormal eigenbasis of $A A ^ { * }$ in ${ \mathcal { F } } ^ { m }$ (respectively, of $A ^ { * } A$ in ${ \mathcal { F } } ^ { n } )$ . Thus, a singular-value decomposition of A can be obtained by solving the eigenvalue-eigenvector problem for the matrices $A A ^ { * }$ and $A ^ { * } A$

Example 4. Consider the matrix A defined in Exercise 5.4.2; it has singular values $s _ { 1 } = \sqrt { 2 }$ and $s _ { 2 } = 1$ . To find a singular-value decomposition of A, we compute $A ^ { * } A$ and $A A ^ { * }$ and construct orthonormal eigenbases for these matrices. The standard basis in $\mathcal { F } ^ { 2 }$ can be used for $A ^ { * } A$ and the system $\{ [ { \boldsymbol { \alpha } } \quad { \boldsymbol { 0 } } \quad \alpha ] ^ { \mathrm { { T } } } , [ { \boldsymbol { 0 } } \quad { \boldsymbol { 1 } } \quad { \boldsymbol { 0 } } ] ^ { \mathrm { { T } } } , [ { \boldsymbol { \alpha } } \quad { \boldsymbol { 0 } } \quad - \alpha ] ^ { \mathrm { { T } } } \}$ , where $\alpha = 1 / \sqrt { 2 } ,$ can be used for $A A ^ { * }$ . Hence

$$
A = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } = { \left[ \begin{array} { l l l } { \alpha } & { 0 } & { \alpha } \\ { 0 } & { 1 } & { 0 } \\ { \alpha } & { 0 } & { - \alpha } \end{array} \right] } { \left[ \begin{array} { l l } { { \sqrt { 2 } } } & { 0 } \\ { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] }
$$

is a singular-value decomposition of A.

The relation (7) gives rise to the general notion of unitary equivalence of two $m \times n$ matrices A and B. We say that A and B are unitarily equivalent if there exist unitary matrices U and V such that $A = U B V ^ { * }$ . It is clear that unitary equivalence is an equivalence relation and that Theorem 2 can be interpreted as asserting the existence of a canonical form (the matrix D) with respect to unitary equivalence in each equivalence class. Now the next result is to be expected.

Proposition 2. Two m × n matrices are unitarily equivalent if and only if they have the same singular values.

ProoF. Assume that the singular values of the matrices A, $\pmb { { \cal B } } \in \mathcal { F } ^ { m }  ^ { \star , }$ coincide. Writing a singular-value decomposition of the form (7) for each matrix (with the same D), the unitary equivalence readily follows.

Conversely, let A and B be unitarily equivalent, and let $D _ { 1 }$ and $D _ { 2 }$ be the matrices of singular values of A and B, respectively, that appear in the singular-value decompositions of the matrices. Without loss of generality, it may be assumed that the singular values on the diagonals of $D _ { 1 }$ and $D _ { 2 }$ are in nondecreasing order. It is easily found that the equivalence of A and B implies that $D _ { 1 }$ and $D _ { 2 }$ are also unitarily equivalent: $\ b { D _ { 2 } } = \ b { U _ { 1 } D _ { 1 } } \ b { V _ { 1 } ^ { * } }$ Viewing the last relation as the singular-value decomposition of $D _ { 2 }$ and noting that the middle factor $D _ { 1 }$ in such a representation is uniquely determined, we conclude that $D _ { 1 } = D _ { 2 }$

Corollary 1. Two $m \times n$ matrices A and B are unitarily equivalent if and only if the matrices $A ^ { * } A$ and $B ^ { * } B$ are similar.

PROOF. If $A = U B V ^ { * }$ , then

$$
A ^ { * } A = V B ^ { * } U ^ { * } U B V ^ { * } = V B ^ { * } B V ^ { * } = V B ^ { * } B V ^ { - 1 } .
$$

Conversely, the similarity of $A ^ { * } A$ and $B ^ { * } B$ yields, in particular, that they have the same spectrum. Hence A and B have the same singular values and, consequently, are unitarily equivalent.

## 5.8 Idempotent Matrices (Projectors)

By definition, an idempotent matrix P satisfies the condition $P ^ { 2 } = P .$ Another name for such a matrix is a projector. The name has geometrical origins that, among other things, will be developed in this section. Observe that the definition can also be applied to transformations $P \in { \mathcal { L } } ( { \mathcal { S } } )$ for any linear space $\mathcal { L }$ It is left as an exercise for the reader to formulate analogues of Theorems 1–5 in this case. We start with the following simple proposition.

Theorem 1. If P is idempotent, then:

(a) $I - P$ is idempotent;

(b) Im $( I - P ) = \operatorname { K e r } P ;$

(c) $\operatorname { K e r } ( I - P ) = \operatorname { I m } P .$

PRooF. For part (a), observe that $( I - P ) ^ { 2 } = I - 2 P + P ^ { 2 } = I - 2 P +$ $P = I - P $ . Proceeding to part (b), we see that if $y \in \operatorname { I m } ( I - P ) .$ then $y =$ $( I - P ) x$ for some $x \in \mathcal { F } ^ { n }$ . Hence $P y = P ( I - P ) x = ( P - P ^ { 2 } ) x = \theta$ and y∈ Ker P. Conversely, if $P y = \pmb { \theta } _ { ; }$ then $( I - P ) { \bf y } = { \bf y }$ and therefore ${ \pmb y } \in \operatorname { I m } ( I - P )$ Thus Im(I — P) = Ker P. A similar argument gives the proof of part (c).

Note that the idempotent matrix $Q = I - P$ is called the complementary projector to P. The importance of the last theorem becomes clearer when we recognize that the kernel and image of P constitute a direct sum decomposition of the space ${ \mathcal { F } } ^ { n }$ on which P acts. Note also that, for the complementary projector $Q ,$

$$
\mathrm { I m } ~ Q = \mathrm { K e r } ~ P , ~ \mathrm { K e r } ~ Q = \mathrm { I m } ~ P .
$$

Theorem 2. If P is a projector, then Ker $P \dot { + }$ Im $P = \mathcal { F } ^ { n }$

PrOOF. For any $\pmb { x } \in \mathcal { F } ^ { n }$ , we can write ${ \pmb x } = { \pmb x } _ { 1 } + { \pmb x } _ { 2 }$ , where $\pmb { x } _ { 1 } = ( I - P ) \pmb { x } \in$ Ker P and ${ \pmb x } _ { 2 } = P { \pmb x } \in$ Im P. Hence $\mathcal { F } ^ { n } =  { \mathrm { K e r } } P +$ Im P. Finally, if ${ \pmb x } \in { \bf K }$ er $P \cap$ Im $P ,$ it must be the zero element. For, $\pmb { x } \in \mathbb { K }$ er P implies $P { \boldsymbol { x } } = \theta ,$ while x ∈ Im P implies by Theorem 1 that $( I - P ) x = \pmb { \theta }$ These two conclusions mean that $\scriptstyle { \pmb x } = { \pmb \theta }$ and so the sum Ker P + Im P is direct. ■

Thus, each idempotent matrix P generates two uniquely defined mutually complementary subspaces $\mathcal { S } _ { 1 } = \mathop { \mathrm { K e r } } \ P$ and $\mathcal { S } _ { 2 } = \mathrm { I m } ~ P$ such that their direct sum is the entire space. The converse is also true: If $\mathcal { S } _ { 1 } + \mathcal { S } _ { 2 } = \mathcal { F } ^ { n } ,$ there exists a unique idempotent P for which $\mathcal { S } _ { 1 } = \mathrm { K e r }$ P and $\mathcal { S } _ { 2 } =$ Im P. To see this, just define† P on ${ \mathcal { F } } ^ { n }$ by $P { \mathbf { x } } = { \mathbf { x } } _ { 2 }$ , where ${ \pmb x } = { \pmb x } _ { 1 } + { \pmb x } _ { 2 }$ and $\pmb { x } _ { 1 } \in \mathcal { S } _ { 1 }$ $\pmb { x } _ { 2 } \in \mathcal { S } _ { 2 }$ . Then it is clear that $P ^ { 2 } = P$ and $\mathcal { S } _ { 1 } = \mathrm { K }$ er $P , \mathcal { S } _ { 2 } =$ Im P. Also, the uniqueness of P follows immediately from the definition. Thus, there is a one-to-one correspondence between idempotent matrices in ${ \mathcal { F } } ^ { n \times n }$ and pairs of subspaces $\mathcal { S } _ { 1 } , \mathcal { S } _ { 2 }$ such that $\mathcal { S } _ { 1 } \dot { + } \mathcal { S } _ { 2 } = \mathcal { F } ^ { n }$

In view of this result, we shall say that the idempotent matrix P performs the projection of the space ${ \mathcal { F } } ^ { n }$ on the subspace $\mathcal { S } _ { 2 }$ parallel to $\mathcal { S } _ { 1 }$ , or onto $\mathcal { S } _ { 2 }$ along $\mathcal { S } _ { 1 }$ . Hence the name “projector" as an alternative to “idempotent matrix."

We now go on to study the spectral properties of projectors.

## Theorem3. An idempotent matrix is simple.

ProoF. We have already seen in Exercise 4.11.7 that the eigenvalues of an idempotent matrix are all equal to 1 or 0. It follows then that the eigenvectors of P all belong to either Im $P \left( \lambda = 1 \right)$ or Ker $P \left( \lambda = 0 \right)$ . In view of Theorem 2, the eigenvectors of P must span ${ \mathcal { F } } ^ { n }$ and hence P is a simple matrix.

The spectral theorem (Theorem 4.10.3) can now be applied

Corollary 1. An $n \times n$ projector P admits the representation

$$
P = \sum _ { j = 1 } ^ { r } x _ { j } y _ { j } ^ { * } ,\tag{1}
$$

where $r = \operatorname { r a n k } P$ and $\{ \boldsymbol { x } _ { 1 } , \ldots , \boldsymbol { x } _ { r } \} , \{ \boldsymbol { y } _ { 1 } , \ldots , \boldsymbol { y } _ { r } \}$ are biorthogonal systems in $\mathcal { F } _ { n }$

Note that a direct computation of $P ^ { 2 }$ shows that, conversely, any matrix of the form (1) is idempotent

An important case arises when P is both idempotent and Hermitian: $P ^ { 2 } = P$ and $P ^ { * } = P .$ In this case the subspaces $\mathcal { S } _ { 1 } = \mathop { \mathrm { K e r } } P$ and $\mathcal { S } _ { 2 } = \operatorname { I m } P$ are found to be orthogonal. For, if $\pmb { x } \in \mathcal { S } _ { 1 }$ and $\pmb { y } \in \mathcal { S } _ { 2 }$ , then

$$
( { \pmb x } , { \pmb y } ) = ( { \pmb x } , P { \pmb y } ) = ( P ^ { * } { \pmb x } , { \pmb y } ) = ( P { \pmb x } , { \pmb y } ) = 0
$$

and therefore ${ \mathcal { S } } _ { 1 } \oplus { \mathcal { S } } _ { 2 } = { \mathcal { F } } ^ { n }$ . A Hermitian idempotent P is called an orthogonal projector: it carries out the projection of ${ \mathcal { F } } ^ { n }$ onto $\mathcal { S } _ { 2 } = \operatorname { I m } P$ along the orthogonal complement $\mathcal { S } _ { 1 } = \mathop { \mathrm { K e r } } P$

The effect of an orthogonal projector can be described in terms of its eigenvectors. To see this, we choose an orthonormal set of (right) eigenvectors $\{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \ldots , \pmb { x } _ { n } \}$ for P. Then the corresponding left eigenvectors are just the adjoints of the (right) eigenvectors and the representation (1) becomes (see Exercise 5.2.5)

$$
P = \sum _ { j = 1 } ^ { r } x _ { j } x _ { j } ^ { * } ,
$$

and for any $x \in \mathcal { F } ^ { n }$

$$
P x = \sum _ { j = 1 } ^ { r } x _ { j } x _ { j } ^ { * } x = \sum _ { j = 1 } ^ { r } ( x , x _ { j } ) x _ { j } .
$$

Now we see that each term of this summation is an orthogonal projection of x onto the span of a (right) eigenvector xj. Hence P is an orthogonal $\mathbf { \boldsymbol { x } } _ { j }$ $P$ projector onto the space spanned by $x _ { 1 } , x _ { 2 } , \ldots , x _ { r } ,$ that is, onto Im P.

It is instructive to make a more direct approach to orthogonal projectors as follows. Suppose we are given a subspace ${ \mathcal { S } } \subset { \mathcal { F } } ^ { n }$ with a basis $\{ \pmb { u } _ { 1 } , \pmb { u } _ { 2 } , \dots , \pmb { u } _ { k } \}$ and we want to find an orthogonal projector onto S. Define $\mathcal { S }$ the $n \times k$ matrix $A = \left[ \pmb { u } _ { 1 } , \pmb { u } _ { 2 } , \ldots , \pmb { u } _ { k } \right]$ , then a typical member of $\mathcal { S }$ is of the form Ax for some $\ b { x } \in \mathcal { F } ^ { k }$ . Given an $\pmb { a } \in \mathcal { F } ^ { n }$ , we want to find a vector $A x \in { \mathcal { S } }$ that can appropriately be called the projection of a onto $\mathcal { S } .$

We determine Ax by demanding that ${ \pmb a } - { \pmb A } { \pmb x }$ should be orthogonal to every member of $\mathcal { S }$ This will be the case if and only if $a - A x$ is orthogonal to each of the basis vectors. Thus, in the standard inner product,

$$
( \pmb { a } - \pmb { A } \pmb { x } , \pmb { u } _ { j } ) = \pmb { u } _ { j } ^ { * } ( \pmb { a } - \pmb { A } \pmb { x } ) = 0 , \qquad j = 1 , 2 , \ldots , k ,
$$

which is equivalent to the matrix equation

$$
A ^ { * } ( a - A x ) = 0 .
$$

Solving for x, we obtain $\pmb { x } = ( A ^ { * } A ) ^ { - 1 } A ^ { * } \pmb { a }$ , noting that the inverse exists because $A ^ { * } A$ is the Gram matrix of linearly independent vectors (Theorem 3.12.2). Thus if P is to be an orthogonal projector on ${ \mathcal { S } } ,$ we must have

$$
\begin{array} { r } { P { \pmb { a } } = A { \pmb { x } } = A ( A ^ { * } A ) ^ { - 1 } A ^ { * } { \pmb { a } } , \qquad { \pmb { a } } \in { \mathscr F } ^ { n } , } \end{array}
$$

that is,

$$
P = A ( A ^ { * } A ) ^ { - 1 } A ^ { * } .\tag{2}
$$

In fact, it is easy to verify that P is idempotent and Hermitian. Thus, we have $P$ determined an orthogonal projector on S in terms of an arbitrary basis for $\mathcal { S }$ $\mathcal { S }$

What is of particular interest, however, is the fact that P is independent of the choice of basis vectors for . To see this, observe that if X is the $\mathcal { S } .$ $n \times k$

matrix of another set of basis vectors, $( \operatorname { a n d } k \leq n )$ then there is a nonsingular $k \times k$ matrix M such that $A = X M$ , whence

$$
\begin{array} { l } { { P = X M ( M ^ { * } X ^ { * } X M ) ^ { - 1 } M ^ { * } X ^ { * } } } \\ { { \ = X M ( M ^ { - 1 } ( X ^ { * } X ) ^ { - 1 } ( M ^ { * } ) ^ { - 1 } ) M ^ { * } X ^ { * } } } \\ { { \ = X ( X ^ { * } X ) ^ { - 1 } X ^ { * } . } } \end{array}
$$

Hence, we get the same projector P whatever the choice of basis vectors for $\mathcal { S }$ may be. In particular, if we choose an orthonormal basis for ${ \mathcal { S } } ,$ then $X ^ { * } X = I$ and

$$
P = X X ^ { * } = \sum _ { j = 1 } ^ { k } x _ { j } x _ { j } ^ { * } ,
$$

and we have returned to the form for P that we had before.

Exercise 1. If $P \in \mathcal { F } ^ { n \times n }$ is a projector on $\mathcal { S } _ { 1 }$ along $\mathcal { S } _ { 2 }$ , show that:

(a) $P ^ { * }$ is a projector on $\mathcal { S } _ { 2 } ^ { \perp }$ along $\mathcal { S } _ { \textbf { 1 } } ^ { \perp }$ (see Section 3.13);

(b) For any nonsingular $H \in \mathcal { F } ^ { n \times n }$ , the matrix $H ^ { - 1 } P H$ is a projector. Describe its image and kernel.

The next results concern properties of invariant subspaces (see Section 4.7), which can be readily described with the help of projectors.

Theorem 4. Let $A \in { \mathcal { F } } ^ { n \times n }$ A subspace $\mathcal { S }$ of ${ \mathcal { F } } ^ { n }$ is A-invariant if and only if $P A P = A P$ for any projector P of ${ \mathcal { F } } ^ { n }$ onto S.

PROOF, Let $\mathcal { S }$ be A-invariant, so that $A { \boldsymbol { x } } \in { \mathcal { S } }$ for all $\pmb { x } \in \mathcal { S } .$ If P is any projector onto ${ \mathcal { S } } ,$ then $( I - P ) A x = A x - A x = 0$ for all $\textstyle { \boldsymbol { \mathbf { \mathit { x } } } } \in { \mathcal { G } } .$ Since for any $y \in \mathcal { F } ^ { n }$ the vector $\boldsymbol { x } = P \boldsymbol { y }$ is in ${ \mathcal { S } } ,$ it follows that $( I - P ) A P y = 0$ for all $y \in \mathcal { F } ^ { n }$ , and we have $P A P = A P $ , as required.

Conversely, if P is a projector onto $\mathcal { S }$ and $P A P = A P$ , then for any $\pmb { x } \in \mathcal { S } ,$ we have $P { \bf { x } } = { \bf { x } }$ and $A { \mathbf { x } } = A P { \mathbf { x } } = P A P { \mathbf { x } }$ . Thus, Ax ∈ Im $\boldsymbol { P } = \mathcal { S }$ and, since x is any member of ${ \mathcal { S } } ,$ the space $\mathcal { S }$ is A-invariant.

Note that the sufficient condition for $\mathcal { S }$ to be invariant is reduced, in fact, to the existence of at least one projector P onto $\mathcal { S }$ such that $Q A P =$ $( I - P ) A P = O .$

A particularly important role is played in the spectral theory of matrices by A-invariant subspaces that have a complementary subspace that is also A-invariant. Such a subspace is said to be A-reducing. Thus, subspace $\mathcal { S } _ { 1 }$ of ${ \mathcal { F } } ^ { n }$ is A-reducing if $A ( \mathcal { S } _ { 1 } ) \subset \mathcal { S } _ { 1 }$ and there is a subspace $\mathcal { S } _ { 2 }$ such that $A ( \mathcal { S } _ { 2 } ) \subset \mathcal { S } _ { 2 }$ and $\mathcal { F } ^ { n } = \mathcal { S } _ { 1 } \dot { + } \mathcal { S } _ { 2 }$ In this case, we may also say that the pair of subspaces $\mathcal { S } _ { 1 } , \mathcal { S } _ { 2 }$ is $A { \mathrm { - } } r e d u c i n g .$ When a subspace is A-reducing, there is a more symmetric characterization than that of Theorem 4.

Theorem 5. Let $A \in { \mathcal { F } } ^ { n \times n }$ . A pair of subspaces ${ \mathcal { S } } _ { 1 } , { \mathcal { S } } _ { 2 } \subset { \mathcal { F } } ^ { n }$ is A-reducing if and only if $A P = P A ,$ where P is the projector onto $\mathcal { S } _ { 2 }$ along $\mathcal { S } _ { 1 }$

PROOF. Let $\mathcal { F } ^ { n } = \mathcal { S } _ { 1 } \dot { + } \mathcal { S } _ { 2 }$ , and $A ( \mathcal { S } _ { 1 } ) \subset \mathcal { S } _ { 1 } , A ( \mathcal { S } _ { 2 } ) \subset \mathcal { S } _ { 2 }$ . For any $\pmb { x } \in \mathcal { F } ^ { n }$ write ${ \pmb x } = { \pmb x } _ { 1 } + { \pmb x } _ { 2 }$ , where $\mathbf { x } _ { 1 } \in \mathcal { S } _ { 1 } , ~ \mathbf { x } _ { 2 } \in \mathcal { S } _ { 2 }$ . Then $A P x = A x _ { 2 }$ and, since $\begin{array} { r } { A { \boldsymbol { x } } _ { 1 } \in \mathcal { S } _ { 1 } = \operatorname { K e r } P , } \end{array}$

$$
P A x = P A x _ { 1 } + P A x _ { 2 } = P A x _ { 2 } .
$$

But $A { \boldsymbol { x } } _ { 2 } \in \mathcal { S } _ { 2 } = \operatorname { I m } P ;$ sO

$$
P A x = P A x _ { 2 } = A x _ { 2 } = A P x
$$

for all $\pmb { x } \in \mathcal { F } ^ { n }$ Thus $P A = A P$

Now let P be a projector on $\mathcal { S } _ { 2 }$ along $\mathcal { S } _ { 1 }$ and suppose that $A P = P A .$ We are to show that both $\mathcal { S } _ { 1 }$ and $\mathcal { S } _ { 2 }$ are A-invariant.

If $\pmb { x } _ { 2 } \in \mathcal { S } _ { 2 }$ then $P x _ { 2 } = x _ { 2 }$ and

$$
A x _ { 2 } = A P x _ { 2 } = P A x _ { 2 } \in \mathcal { S } _ { 2 } ,
$$

so that $A ( \mathcal { S } _ { 2 } ) \subset \mathcal { S } _ { 2 }$ . Next, if $\pmb { x } _ { 1 } \in \mathcal { S } _ { 1 }$

$$
A x _ { 1 } = A ( I - P ) x _ { 1 } = ( I - P ) A x _ { 1 } \in \mathcal { S } _ { 1 } ,
$$

so that $A ( \mathcal { S } _ { 1 } ) \subset \mathcal { S } _ { 1 }$ and the proof is complete.

Let us take this opportunity to bring together several points concerning the image and kernel of a matrix. For the sake of clarity and future use, we consider a matrix $A \in \mathbb { C } ^ { m \times n }$ to be a linear transformation from $\mathbb { C } ^ { n }$ into $\mathbb { C } ^ { m }$ although the discussion can also be put into the context of abstract linear transformations. Recall first that Im $A \subset \mathbb { C } ^ { m }$ and Ker $A \subset \mathbb { C } ^ { n }$ .Then, by Theorem 4.5.5,

$$
\dim ( \operatorname { I m } A ) + \dim ( \operatorname { K e r } A ) = n .\tag{3}
$$

In particular, if $m = n$ it is possible that this statement can be strengthened to yield

$$
\operatorname { I m } A \ + \operatorname { K e r } A = \mathbb { C } ^ { n } .\tag{4}
$$

Theorem 2 says that this is true if $A ^ { 2 } = A _ { \mathrm { { } } }$ , that is, if A is a projector, and it is easily seen to be true if A is normal (and especially, if A is Hermitian or unitary). In the latter case more is true: when A is normal the direct sum is orthogonal,

$$
\mathbf { I m } ~ A ~ \oplus ~ \mathbf { K e r } ~ A = \mathbb { C } ^ { n } .\tag{5}
$$

However, it is important to bear in mind that Eq. (4) is not generally true for square matrices, as the example

$$
A = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] }
$$

quickly shows.

The general property (3) can be seen as one manifestation of the results in Exercise 5.1.7. These results are widely useful and are presented here as a formal proposition about matrices, including some of the above remarks.

Proposition 1. $\ b { I f A } \in \mathbb { C } ^ { m \times n }$ then

$$
\mathbb { C } ^ { n } = \operatorname { K e r } A \ \mathrm { ~ \oplus ~ I m ~ } A ^ { * } , \qquad \mathbb { C } ^ { m } = \operatorname { K e r } A ^ { * } \ \mathrm { ~ \oplus ~ I m ~ } A .
$$

Exercise 2. Use Theorem 5.1.2 to prove Proposition 1.

Exercise 3. Verify that the matrix

$$
\begin{array} { r } { \frac { 1 } { 3 } \left[ { \begin{array} { r r r } { 2 } & { 1 } & { - 1 } \\ { 1 } & { 2 } & { 1 } \\ { - 1 } & { 1 } & { 2 } \end{array} } \right] } \end{array}
$$

is an orthogonal projector and find bases for its image and kernel.

Exercise 4. Let P and Q be commuting projectors.

(a) Show that PQ is a projector and

$$
\mathrm { I m } ~ P Q = ( \mathrm { I m } ~ P ) \cap ( \mathrm { I m } ~ Q ) , ~ \mathrm { K e r } ~ P Q = ( \mathrm { K e r } ~ P ) + ( \mathrm { K e r } ~ Q ) .
$$

(b) Show that if we define $P \boxplus Q = P + Q - P Q$ (the “Boolean sum" of P and Q), then P ⊕ Q is a projector and

$$
\mathbf { I m } ( P \boxplus Q ) = ( \operatorname { I m } P ) + ( \operatorname { I m } Q ) , \qquad \operatorname { K e r } ( P \boxplus Q ) = ( \operatorname { K e r } P ) \cap ( \operatorname { K e r } Q ) .
$$

Hint. For part (b) observe that $I - ( P \boxplus Q ) = ( I - P ) ( I - Q )$ and use part(a).

Exercise 5. Let P and $Q$ be projectors. Show that $Q P = Q$ if and only if Ker $P \subset \mathsf { K e r } Q .$

Exercise 6. Let $T \in { \mathcal { L } } ( { \mathcal { U } } , { \mathcal { V } } )$ (as in Theorem 5.1.4). Show that there is a unique solution $\pmb { x _ { 0 } } \in$ Im $T ^ { * }$ of $T ( x ) = b$ if and only if $\pmb { b } \in$ Im $T .$

Hint. Using Exercise 5.1.7 define $P \in { \mathcal { L } } ( \mathcal { V } )$ as the orthogonal projector on Im $T ^ { * }$ along Ker T. If x satisfies $T ( { \pmb x } ) = { \pmb b } ,$ define $\boldsymbol { x } _ { 0 } = P \boldsymbol { x }$ □

## 5.9 Matrices over the Field of Real Numbers

Let $A \in \mathbb { R } ^ { n \times n }$ . Clearly, all statements made above for an arbitrary field $\mathcal { F }$ are valid in the particular case ${ \mathcal { F } } = \mathbb { R }$ However, R fails to be algebraically closed and therefore matrices in $\mathbb { R } ^ { n \times n }$ may lose some vital properties. For instance, a matrix with real elements may have no (real) eigenvalues. An example of such a matrix is

$$
\left[ - \frac { \mu } { \nu } \quad \frac { \nu } { \mu } \right] , \qquad , \nu \in \mathbb { R } , \quad \nu \neq 0 .\tag{1}
$$

(See also the matrix in Example 4.1.2, in which $\gamma$ is not an integer multiple of $\pi . )$ On the other hand, if the spectrum of a real matrix is entirely real, then there is no essential difference between the real and complex cases.

Now we discuss a process known as the method of complexification, which reduces the study of real matrices to that of matrices with complex entries.

First we observe the familiar Cartesian decomposition ${ \pmb z } = { \pmb x } + i { \pmb y } _ { \mathrm { : } }$ , where $z \in \mathbb { C } ^ { n }$ and $x , y \in \mathbb { R } ^ { n }$ . Hence if $\{ a _ { 1 } , a _ { 2 } , \ldots , a _ { n } \}$ is a basis in $\mathbb { R } ^ { n }$

$$
\boldsymbol { x } = \sum _ { j = 1 } ^ { n } \alpha _ { j } \boldsymbol { a } _ { j } \qquad \mathrm { a n d } \qquad \boldsymbol { y } = \sum _ { j = 1 } ^ { n } \beta _ { j } \boldsymbol { a } _ { j } \qquad ( \alpha _ { j } , \beta _ { j } \in \mathbb { R } , j = 1 , 2 , \ldots , n ) ,
$$

then

$$
z = x + i y = \sum _ { j = 1 } ^ { n } { \bigl ( } \alpha _ { j } + i \beta _ { j } { \bigr ) } \pmb { a } _ { j } .
$$

Thus $\mathbb { C } ^ { n }$ can be viewed as the set of all vectors having complex coordinates in this basis, while $\mathbb { R } ^ { n }$ is the set of all vectors with real coordinates with respect to the same basis. The last remark becomes obvious if the basis in $\mathbb { R } ^ { n }$ is standard. Note that the vectors x in $\mathbb { R } ^ { n }$ can be viewed as vectors of the form $x + i 0$ in C".

Proceeding to a matrix $A \in \mathbb { R } ^ { n \times n } ,$ , we extend its action to vectors from $\mathbb { C } ^ { n }$ by the rule

$$
\tilde { A } \mathbf { z } = A \mathbf { x } + i A \mathbf { y }\tag{2}
$$

for $z = x + i y , x , y \in \mathbb { R } ^ { n }$ . Note that the matrices $A$ and $\tilde { A }$ are in fact the same and therefore have the same characteristic polynomial with real coefficients. It should also be emphasized that only real numbers are admitted as eigenvalues of $A _ { i }$ , while only vectors with real entries (i.e., real vectors) are admitted as eigenvectors of $A$

Let $\lambda _ { 0 } \in \sigma ( A )$ and $A x _ { 0 } = \lambda _ { 0 } x _ { 0 }$ , where $\pmb { x _ { 0 } } \in \mathbb { R } ^ { n }$ and $\begin{array} { r } { \pmb { x } _ { 0 } \neq \pmb { \theta } _ { \ast } } \end{array}$ By Eq. (2), $\tilde { A } \mathbf { x _ { 0 } } = A \mathbf { x _ { 0 } } = \lambda _ { 0 } \mathbf { x _ { 0 } }$ and the matrix $\tilde { A }$ has the same eigenvalue and eigenvector. If $\lambda _ { 0 }$ is a complex zero of the characteristic polynomial $c ( \lambda )$ of $\tilde { A }$ then so is $\bar { \lambda } _ { 0 }$ , and $\lambda _ { 0 } , \bar { \lambda } _ { 0 } \in \sigma ( \widetilde { A } )$ . The eigenvectors of A corresponding to $\tilde { A }$ $\lambda _ { 0 }$ and $\bar { \lambda } _ { 0 }$ , respectively, are mutually complex conjugate, that is, of the form $x + i y$ and $\boldsymbol { x } - i \boldsymbol { y }$ Indeed, if $\widetilde { A } z = \lambda _ { 0 } z ,$ where ${ \pmb z } = { \pmb x } + i { \pmb y } ,$ then it is easily checked that $\tilde { A } ( \mathbf { x } - i \mathbf { y } ) = \bar { \lambda } _ { 0 } ( \mathbf { x } - i \mathbf { y } )$ Note that since $\lambda _ { 0 } \neq \bar { \lambda } _ { 0 }$ , the eigenvectors $\boldsymbol { x } + i \boldsymbol { y }$ and ${ \pmb x } - i { \pmb y }$ are linearly independent (Proposition 4.10.4). Consider the subspace $\mathcal { S } = \operatorname { s p a n } \{ x + i y , x - i y \}$ . It has a real basis $\{ { \pmb x } , { \pmb y } \}$ . Referring to $\mathcal { S }$ as a subspace of $\mathbb { R } ^ { n } ;$ that is, as the set of all linear combinations of $\mathbf { \delta x } , \mathbf { y }$ with real coefficients, it is clear from the relations

$$
A x = \mu x - \nu y , \qquad A y = \nu x + \mu y ,\tag{3}
$$

where $\mu + i \nu = \lambda _ { 0 }$ , that $\mathcal { S }$ is A-invariant. However, the matrix A has no (real) eigenvectors in $\mathcal { S }$ (Compare with Exercise 4.9.8.) For example, if A is the coefficient matrix given in (1), the linear system

$$
A ( \alpha { \pmb x } + \beta { \pmb x } ) = \lambda ( \alpha { \pmb x } + \beta { \pmb y } ) , \qquad \lambda \in \mathbb { R } ,
$$

implies that $\alpha x + \beta y = 0 .$

Thus, if the characteristic polynomial of a real matrix A has a complex zero, then it is associated with a two-dimensional A-invariant subspace $\mathcal { S }$ in $\mathbb { R } ^ { n }$ , although $A \mid _ { \mathcal { S } }$ has no eigenvalues and, consequently, no eigenvectors in ${ \mathcal { S } } .$

We summarize this discussion.

Theorem 1. A real matrix $A \in \mathbb { R } ^ { n \times n }$ has a one-dimensional (two-dimensional) invariant subspace in $\mathbb { R } ^ { n }$ associated with each real (complex) zero of the characteristic polynomial.

In the first case, the invariant subspace is spanned by a (real) eigenvector of $A ,$ while in the second case the matrix has no eigenvectors lying in this invariant subspace.

A matrix $U \in \mathbb { R } ^ { n \times n }$ satisfying the condition $U ^ { \mathrm { T } } U = U U ^ { \mathrm { T } } = I$ is an orthogonal matrix. The properties of orthogonal matrices viewed as matrices in $\mathbb { C } ^ { n \times n }$ can be deduced from those of unitary ones. In particular, since a únitary matrix is simple, it is similar to a diagonal matrix of its eigenvalues. Some of the eigenvalues may be complex numbers and therefore are not eigenvalues of $U$ viewed as a matrix in $\mathbb { R } ^ { n \times n }$ . Hence the following result is of interest.

Corollary 1. Any orthogonal matrix $U \in \mathbb { R } ^ { n \times n }$ is similar (over R) to a matrix of the form

$$
\mathrm { d i a g } [ 1 , \ldots , 1 , - 1 , \ldots , - 1 , D _ { 1 } , D _ { 2 } , \ldots , D _ { k } ] ,
$$

where $D _ { i } \in \mathbb { R } ^ { 2 \times 2 } ( i = 1 , 2 , . . . , k )$ are matrices of the form (1), in which $\mu =$ cos $\gamma , \nu = - \sin \gamma , \gamma \neq \pi t , t = 0 , \pm 1 , \ldots .$

## 5.10 Bilinear, Quadratic, and Hermitian Forms

Let $A \in { \mathcal { F } } ^ { n \times n }$ and $\pmb { x } , \pmb { y } \in \mathcal { F } ^ { n }$ . Consider the function $f _ { A }$ defined on $\mathcal { F } ^ { n } \times \mathcal { F } ^ { n }$ by

$$
f _ { A } ( x , y ) \triangleq ( A x , y ) .\tag{1}
$$

Recalling the appropriate properties of the inner product, it is clear that,. for a fixed A, the function $f _ { A }$ in Eq. (1) is additive with respect to both vector variables (the subscript A is omitted):

$$
\begin{array} { r } { f ( x _ { 1 } + x _ { 2 } , y ) = f ( x _ { 1 } , y ) + f ( x _ { 2 } , y ) , } \\ { f ( x , y _ { 1 } + y _ { 2 } ) = f ( x , y _ { 1 } ) + f ( x , y _ { 2 } ) , } \end{array}\tag{2}
$$

and homogeneous with respect to the first vector variable:

$$
f ( \alpha x , y ) = \alpha f ( x , y ) , \qquad \alpha \in { \mathcal { F } } .\tag{3}
$$

If ${ \mathcal { F } } = \mathbb { R }$ , the function is also homogeneous with respect to the second vector variable:

$$
f ( x , { \boldsymbol { \beta } } { \boldsymbol { y } } ) = \beta f ( x , \boldsymbol { y } ) , \qquad \beta \in \mathbb { R } ,\tag{4}
$$

while in the case ${ \mathcal { F } } = \mathbb { C } .$ , the function $f \equiv f _ { A }$ is conjugate-homogeneous with respect to the second argument:

$$
f ( \mathbf { x } , \beta \mathbf { y } ) = \bar { \beta } f ( \mathbf { x } , \mathbf { y } ) , \qquad \beta \in \mathbb { C } .\tag{4'}
$$

Now we formally define a function $f ( x , y )$ , defined on pairs of vectors from ${ \mathcal { F } } ^ { n }$ , to be bilinear (respectively, conjugate bilinear) if it satisfies the conditions (1) through (4) (respectively, (1) through (3) and (4')). Consider the conjugate bilinear function $f _ { A } ( { \boldsymbol { \mathbf { x } } } , { \boldsymbol { \mathbf { y } } } )$ defined by Eq. (1) on $\mathbb { C } ^ { n } \times \mathbb { C } ^ { n }$ If $\mathcal { E } = \{ \boldsymbol { x } _ { 1 } , \boldsymbol { x } _ { 2 } , \ldots , \boldsymbol { x } _ { n } \}$ is a basis in $\mathbb { C } ^ { n }$ and $\begin{array} { r } { { \pmb x } = \sum _ { i = 1 } ^ { n } \alpha _ { i } { \pmb x } _ { i } , { \pmb y } = \sum _ { j = 1 } ^ { n } \beta _ { j } { \pmb x } _ { j } } \end{array}$ then

$$
f _ { A } ( { \pmb x } , { \pmb y } ) = ( A { \pmb x } , { \pmb y } ) = \sum _ { i , j = 1 } ^ { n } ( A { \pmb x } _ { i } , { \pmb x } _ { j } ) \alpha _ { i } \overline { { \beta } } _ { j } = \sum _ { i , j = 1 } ^ { n } \gamma _ { i j } \alpha _ { i } \overline { { \beta } } _ { j } ,\tag{5}
$$

where

$$
\gamma _ { i j } = ( A x _ { i } , x _ { j } ) , \qquad i , j = 1 , 2 , \ldots , n .\tag{6}
$$

When expressed in coordinates as in Eq. (5), $f _ { A }$ is generally called a conjugate bilinear form or simply a bilinear form according as $\mathcal F = \mathbb C$ or $\mathcal { F } = \mathbb { R }$ respectively. The form is said to be generated by the matrix $A ,$ and the matrix $\tilde { A } = [ \gamma _ { i j } ] _ { i , j = 1 } ^ { n }$ is said to be the matrix of the form $f _ { A }$ with respect to the basis . Our first objective is to investigate the connection between matrices of the bilinear form (1) with respect to different bases and, in particular, between them and the generating matrix A.

We first note that the matrix A is, in fact, the matrix of the form (1) with respect to the standard basis $\{ \mathbf { e } _ { 1 } , \mathbf { e } _ { 2 } , \ldots , \mathbf { e } _ { n } \}$ in $\mathbb { C } ^ { n } .$ Furthermore, if P denotes the transition matrix from the standard basis to a basis $\{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \ldots , \pmb { x } _ { n } \}$ in $\mathbb { C } ^ { n }$ then, by Eq. (3.9.3), $x _ { i } = P e _ { i } , i = 1 , 2 , . . . , n$ . Hence for $i , j = 1 , 2 , \ldots , n ,$

$$
\gamma _ { i j } = ( A \pmb { x } _ { i } , \pmb { x } _ { j } ) = ( A P e _ { i } , P e _ { j } ) = ( P ^ { * } A P e _ { i } , e _ { j } ) .
$$

Recalling that the standard basis is orthonormal in the standard inner product, we find that the γ are just the elements of the matrix $\gamma _ { i j }$ $P ^ { * } A P .$ Thus $\mathbf { \bar { \boldsymbol { A } } } = \mathbf { \boldsymbol { P } } ^ { * } \boldsymbol { A } \boldsymbol { P }$ and matrices of the same conjugate bilinear form with respect to different bases must be congruent.

Theorem 1. Matrices of a conjugate bilinear form with respect to different bases in C generate an equivalence class of congruent matrices. $\mathbb { C } ^ { n }$

Now consider some special kinds of conjugate bilinear forms. A conjugate bilinear form $f _ { A } ( { \pmb x } , { \pmb y } ) = ( A { \pmb x } , { \pmb y } )$ is Hermitian if $\overline { { f _ { A } ( x , y ) } } = f _ { A } ( y , x )$ for all $\pmb { x } , \pmb { y } \in \mathbb { C } ^ { n }$

Exercise 1. Check that a conjugate bilinear form is Hermitian if and only if the generating matrix A is Hermitian. Moreover, all matrices of such a form are Hermitian matrices having the same inertia characteristics.

Hint. Use Theorem 1 and Sylvester's law of inertia.

Particularly interesting functions generated by conjugate bilinear forms are the quadratic forms obtained by substituting $y = x$ in $f _ { A } ( y , x )$ , that is, the forms $f _ { A } ( { \boldsymbol { \mathbf { \mathit { x } } } } ) = ( A { \boldsymbol { \mathbf { \mathit { x } } } } , { \boldsymbol { \mathbf { \mathit { x } } } } )$ defined on ${ \mathcal { F } } ^ { n }$ with values in $\mathcal { F } .$

Exercise 2. By using the identity

$$
\begin{array} { c } { { f ( x , y ) = \frac 1 4 ( f ( x + y , x + y ) + i f ( x + i y , x + i y ) } } \\ { { - i f ( x - i y , x - i y ) - f ( x - y , x - y ) ) , } } \end{array}
$$

show that any conjugate bilinear form is uniquely determined by the corresponding quadratic form.

Exercise 3. Show that the conjugate bilinear form $f _ { A } ( { \boldsymbol x } , { \boldsymbol y } ) = ( A { \boldsymbol x } , { \boldsymbol y } )$ is Hermitian if and only if the corresponding quadratic form is a real-valued function. □

The rest of this section is devoted to the study of quadratic forms generated by a Hermitian matrix, therefore called Hermitian forms. Clearly, such a form is defined on " but now takes values in R. In this case ${ \mathcal { F } } ^ { n }$

$$
f _ { A } ( { \boldsymbol { \mathbf { x } } } ) = ( A x , x ) = \sum _ { i , j = 1 } ^ { n } \gamma _ { i j } \alpha _ { i } { \bar { \alpha } } _ { j } ,\tag{7}
$$

where $\gamma _ { i j } = \bar { \gamma } _ { j i } \left( i , j = 1 , 2 , \ldots , n \right)$ and the $\alpha _ { i } ( i = 1 , 2 , \ldots , n )$ are the coordinates of x with respect to some basis in C". In view of Theorem 1, the Hermitian $\mathbb { C } ^ { n } .$ matrices $\pmb { \tilde { A } } = [ \gamma _ { i j } ] _ { i , j = 1 } ^ { n }$ defined by Eq. (7) are congruent. Consequently, Theorem 5.5.1 asserts the existence of a basis in $\mathbb { C } ^ { n }$ with respect to which there is a matrix of the form $\tilde { A } _ { 0 } = \mathrm { d i a g } [ I _ { s } , - I _ { r - s } , 0 ]$ . In this (canonical) basis, the Hermitian form is reduced to an (algebraic) sum of squares:

$$
( \widetilde { A } _ { 0 } x , x ) = \sum _ { i , j = 1 } ^ { n } \gamma _ { i j } ^ { ( 0 ) } \alpha _ { j } \bar { \alpha } _ { j } = \sum _ { i = 1 } ^ { s } | \alpha _ { i } | ^ { 2 } - \sum _ { j = s + 1 } ^ { r } | \alpha _ { j } | ^ { 2 } ,\tag{8}
$$

where $[ { \alpha } _ { 1 } \quad { \alpha } _ { 2 } \quad \cdots \quad { \alpha } _ { n } ] ^ { \mathrm { T } }$ is the representation of x with respect to the canonical basis.

Theorem 2. For any Hermitian form $( A x , x )$ , there exists a basis in $\mathbb { C } ^ { n }$ with respect to which the form is represented as the sum of squares in Eq. (8), where $s = \pi ( A )$ and r = rank A.

Corollary 1. (Sylvester's law of inertia).† The numbers of positive and negative squares in Eq. (8) are invariants of the Hermitian form fa, denoted $f _ { A }$ $s = \pi ( A ) , r - s = \nu ( A )$

Note that the representation (8) is referred to as the first canonical form of $( A x , x )$ in contrast to the second canonical form:

$$
( A x , x ) = \sum _ { i = 1 } ^ { r } \lambda _ { i } | \alpha _ { i } | ^ { 2 } ,\tag{9}
$$

where $\{ \lambda _ { i } \} _ { i = 1 } ^ { r }$ are the nonzero eigenvalues of A and $[ { \alpha } _ { 1 } \quad { \alpha } _ { 2 } \quad \cdots \quad { \alpha } _ { n } ] ^ { \mathrm { { T } } }$ is the representation of x with respect to a corresponding orthonormal eigenbasis. The representation (9) readily follows from Theorem 5.2.1. In addition, since $A = U D U ^ { * }$ , where $D = \mathrm { d i a g } [ \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { r } , 0 , \ldots , 0 ]$ and U is unitary, the second canonical form (9) can be obtained by a unitary congruent transformation of bases. This is an advantage of this canonical form. (See the next section.)

Consider some particular cases of Hermitian forms. By analogy with matrices, define the Hermitian form $f ( x )$ to be positive (respectively, negative) definite if $f ( { \pmb x } ) > 0$ (respectively, $f ( x ) < 0 )$ for all nonzero $\boldsymbol { x } \in \mathbb { C } ^ { n }$ This analog extends to the definition of semi-definite Hermitian forms also.

Exercise 4. Check that a Hermitian form is definite or semi-definite according as its generating matrix (or any other matrix of the form) is definite or semi-definite of the same kind.

## Hint. See Theorem 5.3.3. □

It should also be noted that a parallel exists between Hermitian matrices and Hermitian forms in that the rank and the inertia characteristics of a matrix can be ascribed to the form that it generates. Also, the simultaneous reduction of two Hermitian matrices to diagonal matrices by the same congruent transformation, as discussed in Section 5.5, is equivalent to a simultaneous reduction of the corresponding Hermitian forms to sums of squares.

Exercise 5. Consider a Hermitian form $f ( x )$ defined on $\mathbb { R } ^ { 3 }$ . The set of points in $\mathbb { R } ^ { 3 }$ (if any) that satisfies the equation $f ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = 1$ is said to form a central quadric. Show that if the equation of the quadric is referred to suitable new axes, it is reduced to the form

$$
\lambda _ { 1 } z _ { 1 } ^ { 2 } + \lambda _ { 2 } z _ { 2 } ^ { 2 } + \lambda _ { 3 } z _ { 3 } ^ { 2 } = 1 .\tag{10}
$$

The new coordinate axes are called the principal axes of the quadric. (Note that the nature of the quadric surface is determined by the relative magnitudes and signs of $\lambda _ { 1 } , \lambda _ { 2 } , \lambda _ { 3 } . )$

Hint. Use $f ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x ^ { * } H x { \mathrm { ~ a n d ~ } } \operatorname { E q . } ( 9 )$

Exercise 6. Verify that $\lambda _ { 1 } \leq \lambda _ { 2 } \leq \lambda _ { 3 }$ in Eq. (10) are the eigen values of H and that for $H > O ,$ the quadric surface (10) is an ellipsoid with the point $( 1 / \sqrt { \lambda _ { 1 } } , 0 , 0 )$ farthest from the origin.

Exercise 7. Examine the nature of the central quadric whose equation is

$$
3 x _ { 2 } ^ { 2 } + 3 x _ { 3 } ^ { 2 } - 2 x _ { 2 } x _ { 3 } - 4 x _ { 1 } x _ { 3 } - 4 x _ { 1 } x _ { 2 } = 1 .
$$

Hint. Diagonalize the matrix of the Hermitian form on the left using Theorem 5.2.1.

## 5.11 Finding the Canonical Forms

We shall describe in this section some techniques for computing the canonical forms of a given Hermitian quadratic form under congruence.

If A is an n × n Hermitian matrix, we note that the second canonical form of $( A x , x )$ is easily found if all the eigenvalues $\{ \lambda _ { i } \} _ { i = 1 } ^ { n }$ and eigenvectors $\{ { \pmb x } _ { i } \} _ { i = 1 } ^ { n }$ are known. Indeed, proceeding from $\left\{ x _ { i } \right\} _ { i = 1 } ^ { n }$ to an orthonormal eigenbasis $\left\{ \tilde { \pmb { x } } _ { i } \right\} _ { i = 1 } ^ { n }$ for A in $\mathbb { C } ^ { n }$ and constructing the unitary matrix

$$
U = [ \tilde { \pmb { x } } _ { 1 } \tilde { \pmb { x } } _ { 2 } \dots \tilde { \pmb { x } } _ { n } ] ,
$$

we deduce by use of Theorem 5.2.1 that $U ^ { * } A U$ is a diagonal matrix D of the eigenvalues of A. Hence for $\textstyle { \pmb { x } } = \sum _ { i = 1 } ^ { n } { \pmb { x } } _ { i } { \pmb { x } } _ { i }$ , we obtain the second canonical form

$$
( A x , x ) = \sum _ { i = 1 } ^ { r } \lambda _ { i } | \alpha _ { i } | ^ { 2 } ,
$$

where r = rank A and $\lambda _ { 1 } , \ldots , \lambda _ { r }$ denote the nonzero eigenvalues of A corresponding (perhaps, after reordering) to the eigenvectors $\tilde { x } _ { 1 } , \ldots , \tilde { x } _ { r }$ . However, the difficulties involved in finding the full spectral properties of a matrix encourage us to develop a simpler method for reducing a Hermitian form. A method suggested by Lagrange allows us to obtain the first canonical form, as well as the transforming matrix, by relatively simple calculations.

For convenience we confine our attention to real Hermitian forms. If $\mathbf { x } = [ \alpha _ { 1 } \quad \alpha _ { 2 } \quad \cdot \cdot \cdot \quad \alpha _ { n } ] ^ { \mathrm { T } }$ , we write

$$
\begin{array} { l } { f ( { \pmb x } ) = \displaystyle \sum _ { i , j = 1 } ^ { n } \gamma _ { i j } \alpha _ { i } \alpha _ { j } } \\ { = \gamma _ { 1 1 } \alpha _ { 1 } ^ { 2 } + \dots + \gamma _ { n n } \alpha _ { n } ^ { 2 } + 2 \gamma _ { 1 2 } \alpha _ { 1 } \alpha _ { 2 } + \dots + 2 \gamma _ { n - 1 } , _ { n } \alpha _ { n - 1 } \alpha _ { n } , } \end{array}\tag{1}
$$

where all numbers involved are real and $\gamma _ { i j } = \gamma _ { j i }$ for $i , j = 1 , 2 , \ldots , n .$ Note that the expression (1) can be viewed as a real function in n real variables $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { n }$

Case 1. Assume that not all of $\gamma _ { i i }$ are zero. Then assuming, for instance, that $\gamma _ { 1 1 } \neq 0 ;$ we rewrite Eq. (1) in the form

$$
f ( { \pmb x } ) = \gamma _ { 1 1 } \bigg ( \alpha _ { 1 } ^ { 2 } + 2 \frac { \gamma _ { 1 2 } } { \gamma _ { 1 1 } } \alpha _ { 1 } \alpha _ { 2 } + \cdots + 2 \frac { \gamma _ { 1 n } } { \gamma _ { 1 1 } } \alpha _ { 1 } \alpha _ { n } \bigg ) + f _ { 1 } ( { \pmb x } _ { 1 } ) ,
$$

where $\pmb { x } _ { 1 } = [ \pmb { \alpha } _ { 2 } \pmb { \alpha } _ { 3 } \cdots \pmb { \alpha } _ { n } ] ^ { \pmb { \Gamma } }$ Obviously, $f _ { 1 } ( \pmb { x } _ { 1 } )$ is a Hermitian form, Following the process of “completing the square," we obtain

$$
f ( { \pmb x } ) = \gamma _ { 1 1 } \bigg ( \alpha _ { 1 } + \frac { \gamma _ { 1 2 } } { \gamma _ { 1 1 } } \alpha _ { 2 } + \cdots + \frac { \gamma _ { 1 n } } { \gamma _ { 1 1 } } \alpha _ { n } \bigg ) ^ { 2 } + f _ { 2 } ( { \pmb x } _ { 1 } ) ,
$$

where $f _ { 2 } ( { \pmb x } _ { 1 } )$ is another Hermitian form in $\mathbf { \delta x _ { 1 } }$ . Thus, the nonsingular transformation of coordinates determined by

$$
\beta _ { 1 } = \alpha _ { 1 } + \frac { \gamma _ { 1 2 } } { \gamma _ { 1 1 } } \alpha _ { 2 } + \cdot \cdot \cdot + \frac { \gamma _ { 1 n } } { \gamma _ { 1 1 } } \alpha _ { n } , \qquad \beta _ { 2 } = \alpha _ { 2 } , \cdot \cdot \cdot , \beta _ { n } = \alpha _ { n }
$$

transforms the given form into the form

$$
\gamma _ { 1 1 } \beta _ { 1 } ^ { 2 } + f _ { 2 } ( { \pmb x } _ { 1 } ) .\tag{2}
$$

and we can write $\begin{array} { r } { \pmb { x } _ { 1 } = [ \beta _ { 2 } \quad \beta _ { 3 } \quad \cdots \quad \beta _ { n } ] ^ { \mathrm { \pmb { r } } } . } \end{array}$

Case 2. If $\because _ { 1 1 } = \gamma _ { 2 2 } = \cdot \cdot \cdot = \gamma _ { n n } = 0 ,$ then we consider a coefficient $\alpha _ { i j } \neq 0$ where $i \neq j ,$ and assume, for instance, that $\alpha _ { 1 2 } \neq 0$ . We now make a congruence transformation of f determined by the coordinate transformation $\beta _ { 1 } = \alpha _ { 1 } , \ \beta _ { 2 } = \pmb { x } _ { 2 } - \alpha _ { 1 } , \ \beta _ { 3 } = \alpha _ { 3 } , \ldots$ , and $\beta _ { n } = \alpha _ { n }$ . It is easily seen that the form determined by the transformed matrix has a term in $\dot { \beta } _ { 1 } ^ { 2 }$ .We may now apply the technique described in case 1 to reduce f to the form (2).

## 5.11 FINDING THE CANONICAL FORMS

Thus, we have proved that any real Hermitian form can be reduced to the form (2). Applying the same process to $f _ { 2 } ( { \pmb x } _ { 1 } )$ and so on, the reduction is completed in at most $n - 1$ such steps.

Exercise 1. Find the rank and inertia of the form $f ( \pmb { x } ) = 2 \alpha _ { 1 } \alpha _ { 2 } + 2 \alpha _ { 2 } \alpha _ { 3 } +$ $\alpha _ { 3 } ^ { 2 }$ and determine a transformation of the coordinates $a _ { 1 } , a _ { 2 } , a _ { 3 }$ that reduces f to a sum of squares.

SoLUTION. Performing the transformation $\alpha _ { 1 } = \beta _ { 3 } , \alpha _ { 2 } = \beta _ { 2 } , \alpha _ { 3 } = \beta _ { 1 }$ , we have

$$
f ( x ) = ( \beta _ { 1 } ^ { 2 } + 2 \beta _ { 1 } \beta _ { 2 } ) + 2 \beta _ { 2 } \beta _ { 3 } = ( \beta _ { 1 } + \beta _ { 2 } ) ^ { 2 } - \beta _ { 2 } ^ { 2 } + 2 \beta _ { 2 } \beta _ { 3 } .
$$

Now put $\gamma _ { 1 } = \beta _ { 1 } + \beta _ { 2 } , \gamma _ { 2 } = \beta _ { 2 } , \gamma _ { 3 } = \beta _ { 3 }$ and obtain

$$
f ( x ) = \gamma _ { 1 } ^ { 2 } - \gamma _ { 2 } ^ { 2 } + 2 \gamma _ { 2 } \gamma _ { 3 } = \delta _ { 1 } ^ { 2 } - \delta _ { 2 } ^ { 2 } + \delta _ { 3 } ^ { 2 }
$$

where $\delta _ { 1 } = \gamma _ { 1 } , \delta _ { 2 } = \gamma _ { 2 } - \gamma _ { 3 } , \delta _ { 3 } = \gamma _ { 3 }$ . Thus the rank of the form is $r = 3 ,$ the number of positive squares is $\pi = 2 ,$ and the signature is $\pi - \nu = 2 - 1 = 1$ Note that the transformation P yielding the reduction is obtained by combining the preceding transformations:

$$
\left[ \begin{array} { c } { \delta _ { 1 } } \\ { \delta _ { 2 } } \\ { \delta _ { 3 } } \end{array} \right] = \left[ \begin{array} { r r r } { 0 } & { 1 } & { 1 } \\ { - 1 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \end{array} \right] \left[ \begin{array} { c } { \alpha _ { 1 } } \\ { \alpha _ { 2 } } \\ { \alpha _ { 3 } } \end{array} \right] .
$$

Inverting the transforming matrix it is found that substitutions which reduce $f ( \mathbf { x } )$ to a sum of squares are given by

$$
\begin{array} { r } { \left[ \alpha _ { 1 } \right] = \left[ \begin{array} { c c c } { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 1 } \\ { 1 } & { - 1 } & { - 1 } \end{array} \right] \left[ \begin{array} { c c c } { \delta _ { 1 } } \\ { \delta _ { 2 } } \\ { \delta _ { 3 } } \end{array} \right] . } \end{array}
$$

Note also that, by using Lagrange's method, we have avoided the computation of eigenvalues of the matrix

$$
A = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 1 } \end{array} \right] }
$$

that generates the form. Such a computation would require the calculation of all the zeros of the characteristic equation $\lambda ^ { 3 } - \lambda ^ { 2 } - 2 \lambda + 1 = 0$ As we already know, two of them must be positive and one negative.

Another method (due to Jacobi) for finding the inertia of A or, equivalently, of the corresponding Hermitian form will be discussed in Section 8.6.

Exercise 2. Find the rank and inertia of the following Hermitian forms and find transformations reducing them to sums of squares:

$$
\begin{array} { r l } { \mathrm { ( a ) } } & { 2 \alpha _ { 1 } ^ { 2 } - \alpha _ { 3 } ^ { 2 } + \alpha _ { 1 } \alpha _ { 2 } + \alpha _ { 1 } \alpha _ { 3 } ; } \\ { \mathrm { ( b ) } } & { \alpha _ { 1 } ^ { 2 } + 2 ( \alpha _ { 1 } \alpha _ { 2 } + \alpha _ { 2 } \alpha _ { 3 } + \alpha _ { 3 } \alpha _ { 4 } + \alpha _ { 4 } \alpha _ { 5 } + \alpha _ { 1 } \alpha _ { 5 } ) ; } \\ { \mathrm { ( c ) } } & { 2 \alpha _ { 1 } \alpha _ { 2 } - \alpha _ { 1 } \alpha _ { 3 } + \alpha _ { 1 } \alpha _ { 4 } - \alpha _ { 2 } \alpha _ { 3 } + \alpha _ { 2 } \alpha _ { 4 } - 2 \alpha _ { 3 } \alpha _ { 4 } . } \end{array}
$$

Answers. (a) $r = 3 , \pi = 1 , \nu = 2 ; ( { \bf b } ) r = 5 , \pi = 3 , \nu = 2 ;$ (c) $r = 3 ,$ $\pi = 1 , \nu = 2$ . The respective transforming matrices are

$$
 \begin{array} { r }  { \left[ \begin{array} { l l l } { 1 } & { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } , \qquad { \left[ \begin{array} { l l l l } { 1 } & { 1 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { - 1 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 1 } & { - 1 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { - 2 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] } , \qquad { \left[ \begin{array} { l l l l } { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { - { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { - 1 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] } . \quad  \begin{array} { l } { { \boxed { 1 } } } \\   \begin{array} { r l } { { \boxed { 2 } } } \\   \begin{array} { r l } { { \boxed { 4 } } } \\ { { \begin{array} { r l } { { \boxed { 4 } } } \end{array} } } \\ { { \begin{array} { r l } { { \boxed { 4 } } } \end{array} } } \\  { \begin{array} { r l } { { \boxed { 4 } } } \end{array} } \\  { \begin{array} { r l } { { \boxed { 4 } } } \end{array} } \\  { \begin{array} { r l } { { \boxed { 4 } } } \end{array} } \\  { \begin{array} { r l } { { \boxed { 4 } } } \end{array} } \\  { \begin{array} { r l } { { \boxed { 4 } } } \end{array} } \\  { \begin{array} { r l } { { \boxed { 4 } } } \end{array} } \\  { \begin{array} { r l } { { \boxed { 4 } } } \end{array} } \\   \begin{array} { r l }  \end{array} \end{array} \end{array} \end{array} \end{array}
$$

## 5.12 The Theory of Small Oscillations

In this section we introduce an important physical problem whose solution depends on the problem resolved in Theorem 5.5.2: the simultaneous reduction of two Hermitian matrices (or forms). We will describe the small oscillations of mechanical systems, although the resulting equations and their solution also arise in quite different circumstances; the oscillations of current and voltage in electrical circuits, for example.

Consider the motion of an elastic mechanical system whose displacement from some stable equilibrium position can be specified by n coordinates. Let these coordinates be $p _ { 1 } , p _ { 2 } , \ldots , p _ { n }$ . If the system performs small oscillations about the equilibrium position, its kinetic energy T is represented $T$ by a quadratic form in the time rates of change of the coordinates; $\dot { p } _ { 1 } , \dots , \dot { p } _ { n }$ say. Thus, there exists a real symmetric matrix A such that

$$
\begin{array} { r } { T = \frac 1 2 \displaystyle \sum _ { j = 1 } ^ { n } \sum _ { k = 1 } ^ { n } a _ { j k } \dot { p } _ { j } \dot { p } _ { k } = \frac 1 2 \dot { p } ^ { \mathrm { T } } A \dot { p } , } \end{array}
$$

where $\pmb { p } = [ \pmb { p } _ { 1 } \quad p _ { 2 } \quad \cdots \quad p _ { n } ] ^ { \mathrm { T } }$ and $\pmb { \dot { p } } = [ \pmb { \dot { p } } _ { 1 } \quad \pmb { \dot { p } } _ { 2 } \quad \dotsb \ \dot { p } _ { n } ] ^ { \mathtt { T } }$ Furthermore, for any motion whatever, $\pmb { \dot { p } } \in \mathbb { R } ^ { n }$ and for physical reasons, T is positive. Thus, A is a real, positive definite matrix (see Exercise 5.10.4).

When the system is distorted from its equilibrium position, there is generally potential energy stored in the system. It can be shown that if the coordinates are defined so that $\pmb { p } = \pmb { \theta }$ in the equilibrium position and the potential

energy V is agreed to be zero in this position, then for small oscillations,

$$
\begin{array} { r } { V = \frac { 1 } { 2 } \displaystyle \sum _ { j = 1 } ^ { n } \displaystyle \sum _ { k = 1 } ^ { n } c _ { j k } p _ { j } p _ { k } = \frac { 1 } { 2 } p ^ { \operatorname { T } } C p , } \end{array}
$$

where C is a real symmetric nonnegative (or positive) definite matrix, that is, $V \geq 0$ for any $\pmb { p } \in \mathbb { R } ^ { n }$

We define the derivative of a matrix (or a vector) P to be the matrix whose elements are the derivatives of those of P. For any conformable matrices $P$ and $Q$ whose elements are differentiable functions of $\mathbf { \boldsymbol { x } } ,$ it is easily seen that

$$
{ \frac { d } { d x } } ( P Q ) = { \frac { d P } { d x } } Q + P { \frac { d Q } { d x } } .\tag{1}
$$

We now view $p _ { 1 } , p _ { 2 } , \ldots , p _ { n } , \dot { p } _ { 1 } , \dot { p } _ { 2 } , \ldots , p _ { n }$ as a set of 2n independent variables and we obtain

$$
\begin{array} { l } { { \displaystyle { \frac { \partial T } { \partial { \dot { p } } _ { i } } = \frac { 1 } { 2 } \left( \frac { \partial { \dot { p } } ^ { \mathrm { T } } } { \partial { \dot { p } } _ { i } } A { \dot { p } } + { \dot { p } } ^ { \mathrm { T } } A \frac { \partial { \dot { p } } } { \partial { \dot { p } } _ { i } } \right) } } } \\ { ~ } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \left( e _ { i } ^ { \mathrm { T } } A { \dot { p } } + { \dot { p } } ^ { \mathrm { T } } A e _ { i } \right) } } \\ { ~ } \\ { { \displaystyle ~ = A _ { i * } { \dot { p } } } , } \end{array}
$$

where $\pmb { A } _ { i * }$ denotes the ith row of A. Similarly,

$$
\frac { \partial V } { \partial p _ { i } } = C _ { i * } \ ' p .
$$

Equations of motion for the system (with no external forces acting) are obtained by Lagrange's method in the following form:

$$
{ \frac { d } { d t } } \left( { \frac { \partial T } { \partial { \dot { p } } _ { i } } } \right) - { \frac { \partial T } { \partial p _ { i } } } = \ - { \frac { \partial V } { \partial p _ { i } } } , \qquad i = 1 , 2 , \ldots , n .
$$

From the above expressions for the derivatives we find that the equations of motion are

$$
A _ { i * } \ddot { p } = - C _ { i * } p , \qquad i = 1 , 2 , \ldots , n ,
$$

or, in matrix form,

$$
A { \ddot { p } } + C p = 0 .\tag{2}
$$

Following the methods in Section 4.13, and anticipating sinusoidal solutions, we look for a solution $p ( t )$ of Eq. (2) of the form $p ( t ) = q e ^ { i \omega t } ;$ where q is independent of t and ω is real. Then $\ddot { p } = - \omega ^ { 2 } q e ^ { i \omega t }$ . and if we write $\lambda = \omega ^ { 2 }$ , Eq. (2) becomes

$$
( - \lambda A + C ) q = \pmb { \theta } ,\tag{3}
$$

or

$$
( \lambda I - A ^ { - 1 } C ) q = \pmb { \theta } .\tag{4}
$$

The admissible values of λ (defining natural frequencies of vibration) are the n eigenvalues of the matrix $A ^ { - 1 } C$ The modes of vibration are determined by corresponding right eigenvectors. However, we need to ensure that the eigenvalues are real and nonnegative before our solutions have the required form with a real value of ω.

The algebraic problem posed by Eq. (3) is just a special case of Eq. (5.5.5) and, using the argument of that section, the eigenvalues of $A ^ { - 1 } C$ are just those of $\bar { A } ^ { - 1 / 2 } C \bar { A } ^ { - 1 / 2 }$ . But the latter matrix is obviously nonnegative (or positive) definite along with C. Hence, all eigenvalues of Eq. (4) are real and nonnegative (or positive if C is positive definite). Write for the jth eigenvalue $\lambda _ { i } = \omega _ { j } ^ { 2 } , ( \omega _ { j } \geq 0 )$ , and set $W = \mathrm { d i a g } [ \omega _ { 1 } , . . . , \omega _ { n } ]$

The proof of Theorem 5.5.2 shows that if we define new coordinates in $\mathbb { C } ^ { n }$ by $\overset { \cdot } { \pmb { q } } = \pmb { A } ^ { - 1 / 2 } \pmb { U } \overset { \cdot } { \pmb { s } }$ , where $U ^ { * } U = I$ and

$$
U ^ { * } ( A ^ { - 1 / 2 } C A ^ { - 1 / 2 } ) U = \Lambda = W ^ { 2 } ,
$$

then A and C can be simultaneously diagonalised. (In fact, U is here a (real) orthogonal matrix.) Reverting to the time-dependent equations, this suggests the definition of new generalised coordinates for the system: $\xi _ { 1 } , \ldots , \xi _ { n } ,$ given by $p ( t ) = A ^ { - 1 / 2 } U \xi ( t )$ , so that $\ddot { p } = A ^ { - 1 / 2 } U \ddot { \xi } .$ Substitution into Eq. (2) and premultiplication by $U ^ { * } A ^ { - 1 / 2 }$ leads to the “decoupled" equation:

$$
\ddot { \pmb { \xi } } + W ^ { 2 } \pmb { \xi } = \pmb { \theta } ,
$$

or

$$
\ddot { \zeta } _ { i } + \omega _ { i } ^ { 2 } \xi _ { i } = 0 , \qquad i = 1 , 2 , \ldots , n .
$$

This implies that

$$
\xi _ { i } ( t ) = \alpha _ { i } \cos ( \omega _ { i } t + \varepsilon _ { i } ) \qquad \mathrm { i f } \quad \omega _ { i } \neq 0 .
$$

The ${ \pmb { \alpha } } { \bf \dot { s } }$ and ${ \pmb \varepsilon } { \pmb s }$ in these equations are arbitrary constants that are usually determined by applying given initial conditions. When $\xi _ { i }$ varies in this fashion while all other $\xi \mathbf { \hat { s } }$ are zero, we say that the system is oscillating in the ith normal mode. The coordinates $\xi _ { 1 } , \xi _ { 2 } , \ldots , \xi _ { n }$ are normal coordinates for the system. Notice that

$$
\begin{array} { r l } & { T = \frac { 1 } { 2 } \dot { p } ^ { \mathrm { T } } A \dot { p } = \frac { 1 } { 2 } \dot { \xi } ^ { \mathrm { T } } \dot { \xi } } \\ & { \phantom { T = } = \frac { 1 } { 2 } ( \dot { \xi } _ { 1 } ^ { 2 } + \dot { \xi } _ { 2 } ^ { 2 } + \cdot \cdot \cdot + \dot { \xi } _ { n } ^ { 2 } ) } \end{array}
$$

and

$$
\begin{array} { l } { { V = \frac { 1 } { 2 } p ^ { \mathrm { T } } C p = \frac { 1 } { 2 } \xi ^ { \mathrm { T } } W ^ { 2 } \xi } } \\ { { \mathrm { } } } \\ { { = \frac { 1 } { 2 } ( \omega _ { 1 } ^ { 2 } \xi _ { 1 } ^ { 2 } + \cdot \cdot \cdot + \omega _ { n } ^ { 2 } \xi _ { n } ^ { 2 } ) . } } \end{array}
$$

Thus, when expressed in terms of the normal coordinates, both the kinetic and potential energies are expressed as sums of squares of the appropriate variables.

We can obtain some information about the normal modes by noting that when the system vibrates in a normal mode of frequency $\omega _ { i }$ , we have $\mathbf { \boldsymbol { s } } = \boldsymbol { e } _ { i }$ and so the solution for the ith normal-mode vector $\pmb { q } _ { i }$ is

$$
\pmb { q } _ { i } = \big ( A ^ { - 1 / 2 } U \big ) \pmb { e } _ { i } = i \mathrm { t h } \mathrm { c o l u m n o f } A ^ { - 1 / 2 } U .
$$

Hence the matrix of normal-mode vectors, $Q = [ \pmb q _ { 1 } \pmb q _ { 2 } \pmb \cdots \pmb q _ { n } ]$ is given by $Q = A ^ { - 1 / 2 } U$ . Furthermore,

$$
Q ^ { \boldsymbol { \mathsf { T } } } A Q = I , \qquad Q ^ { \boldsymbol { \mathsf { T } } } C Q = W ^ { 2 } ,\tag{5}
$$

which may be described as the biorthogonality properties of the normalmode vectors.

Now we briefly examine the implications of this analysis for a system to which external forces are applied. We suppose that, as in the above analysis, the elastic system makes only small displacements from equilibrium but that, in addition, there are prescribed forces $f _ { 1 } ( t ) , \ldots , f _ { n } ( t )$ applied in the coordinates $p _ { 1 } , p _ { 2 } , \ldots , p _ { n }$ . Defining $\pmb { f } ( t ) = [ f _ { 1 } ( t ) \quad \cdots \quad f _ { n } ( t ) ] ^ { \mathrm { T } }$ , we now have the equations of motion:

$$
A { \ddot { p } } + C p = f ( t ) .\tag{6}
$$

Putting $\pmb { p } = Q \pmb { \xi }$ , premultiplying by $Q ^ { \boldsymbol { \mathsf { T } } }$ , and using Eq. (5), Eq. (6) is immediately reduced to

$$
\ddot { \xi } + W ^ { 2 } \xi = \mathcal { Q } ^ { \mathrm { T } } f ( t ) ,
$$

or

$$
\ddot { \zeta } _ { j } + \omega _ { j } ^ { 2 } \xi _ { j } = \pmb q _ { j } ^ { \operatorname { T } } f ( t ) , \qquad j = 1 , 2 , \dotsc , n .
$$

If $\omega _ { j } \neq 0 ;$ , a particular integral of such an equation can generally be obtained in the form

$$
\boldsymbol { \xi } _ { j } ( t ) = \frac { 1 } { \omega _ { j } } \int _ { 0 } ^ { t } \boldsymbol { q } _ { j } ^ { \intercal } \boldsymbol { f } ( \tau ) \sin ( \omega _ { j } ( t - \tau ) ) \ d \tau ,
$$

and if $\omega _ { j } = 0$ , then

$$
\begin{array} { l } { { \displaystyle \xi _ { j } ( t ) = \int _ { 0 } ^ { t } q _ { j } ^ { \operatorname { T } } f ( \tau ) ( t - \tau ) d \tau . } } \end{array}
$$

In particular, if det $W \neq 0 ,$ we may write

$$
\boldsymbol { \xi } ( t ) = \boldsymbol { W } ^ { - 1 } \int _ { 0 } ^ { t } \sin ( \boldsymbol { W } ( t - \tau ) ) \boldsymbol { Q } ^ { \mathrm { T } } \boldsymbol { f } ( \tau ) d \tau ,
$$

where integration of the vector integrand is understood to mean term-wise integration, and the jth diagonal term of the diagonal matrix sin $W ( t \gets \tau )$ is sin $( \cos ( t - \tau ) )$

An important case that arises in practice can be described by writing $f ( t ) = f _ { 0 } e ^ { i \omega t } ,$ where $f _ { 0 }$ is independent of t. This is the case of a prescribed sinusoidal external (or exciting) force. It is left as an exercise to prove that if ω $\neq \omega _ { j } ( j = 1 , 2 , \ldots , n ) ,$ , then

$$
p ( t ) = Q \xi ( t ) = e ^ { i \omega t } \sum _ { j = 1 } ^ { n } q _ { j } \frac { \omega _ { j } ( q _ { j } ^ { \top } f _ { 0 } ) } { \omega _ { j } ^ { 2 } - \omega ^ { 2 } }\tag{7}
$$

is a solution of Eq. (6).

This result can be used to discuss the resonance phenomenon. If we imagine the applied frequency ω to be varied continuously in a neighbourhood of a natural frequency $w _ { j } , E q , ( 7 )$ indicates that in general the magnitude of the solution vector (or response) tends to infinity as $\phi  \phi _ { j }$ . However, the singularity may be avoided if $q _ { j } ^ { \mathrm { T } } f _ { 0 } = 0$ for all $q _ { j }$ associated with $\omega _ { j }$

Exercise 1. Establish Eq. (7).

Exercise 2. Show that if C is singular, that is, C is nonnegative (but not positive) definite, then there may be normal coordinates $\xi _ { i } ( t )$ for which $| \xi _ { i } ( t ) |  \infty \ a s \ t  \infty$

Exercise 3. Consider variations in the “stiffness" matrix C of the form $C + k l ,$ where k is a real parameter. What is the effect on the natural frequencies of such a change when $k > 0$ and when $k < 0 ? \square$

## 5.13 Admissible Pairs of Matrices

When an $r \times p$ matrix X is multiplied on the right by a $p \times p$ matrix $T ,$ the resulting matrix $\pmb { \chi } T$ is again $r \times p .$ In fact, all matrices in the sequence $X , X T , X T ^ { 2 } , \ldots$ , are of size $r \times p .$ Such sequences appear frequently in some modern applications of the theory of matrices and particularly in systems theory. We give a brief introduction to some of their properties in this section.

First, any pair of matrices $( X , T )$ of sizes $r \times p$ and $p \times p ,$ respectively, with Ker $X \neq \{ 0 \}$ is said to be an admissible pair of order p. Of course, r and $\pmb { p }$ are arbitrary positive integers, although in applications it is frequently the case that $r \leq p _ { 1 }$ and if $r < p ,$ then certainly Ker $X \neq \{ 0 \}$ (see Proposition

3.8.1). Indeed, the case $r = 1$ is of considerable interest. Let $K _ { 1 } = { \sf K }$ er X and let $K _ { 2 }$ be the set of all vectors in both Ker X and Ker XT. Obviously, $K _ { 2 } \subset K _ { 1 }$ , although we may have $K _ { 2 } = K _ { 1 }$ . (When $p = 1$ and $T \neq O$ , for example.) It is also clear that we may write

$$
K _ { 2 } = \mathop { \mathrm { K e r } } \left[ { X \atop X T } \right] .
$$

More generally, for $l = 1 , 2 , \ldots ,$ define

$$
K _ { \iota } = { \bf K } { \bf e r } \left[ \begin{array} { c } { { X } } \\ { { X T } } \\ { { X T ^ { 2 } } } \\ { { \vdots } } \\ { { X T ^ { l - 1 } } } \end{array} \right] ,
$$

and it is seen that we have a “nested” sequence of subspaces of $\mathbb { C } ^ { p }$

$$
K _ { 1 } \supset K _ { 2 } \supset K _ { 3 } \supset \cdots .
$$

A fundamental property of this sequence is contained in the next lemma.

Lemma 1. Let $( X , T )$ be an admissible pair of order p and let the sequence $K _ { 1 } , K _ { 2 } , \ldots o f$ subspaces $o f \mathbb { C } ^ { p }$ be defined as above. If $K _ { j } = K _ { j + 1 }$ , then $K _ { j } =$ $K _ { j + 1 } = K _ { j + 2 } = \cdots$

PROOF.. The matrices

$$
{ \left[ \begin{array} { l } { \quad X } \\ { X T } \\ { \vdots } \\ { X T ^ { j - 1 } } \end{array} \right] } \qquad { \mathrm { a n d } } \qquad { \left[ \begin{array} { l } { \quad X } \\ { X T } \\ { \vdots } \\ { X T ^ { j } } \end{array} \right] }\tag{1}
$$

have sizes $j r \times p$ and $( j + 1 ) r \times p ,$ respectively. If $K _ { j } = K _ { j + 1 }$ then, using Proposition 3.8.1, these two matrices are seen to have the same rank. Thinking in terms of “row rank," this means that the rows of $X T ^ { j }$ are linear combinations of the rows of the first matrix in (1). Thus, there is an $r \times j r$ matrix E such that

$$
X T ^ { j } = E \left[ \begin{array} { c } { { X } } \\ { { X T } } \\ { { \vdots } } \\ { { X T ^ { j - 1 } } } \end{array} \right] .\tag{2}
$$

Now let $\pmb { x } \in K _ { j } = K _ { j + 1 }$ . Then, using Eq. (2),

$$
X T ^ { j + 1 } x = ( X T ^ { j } ) T x = E \left[ \begin{array} { c } { X } \\ { X T } \\ { \vdots } \\ { X T ^ { j - 1 } } \end{array} \right] T x = E \left[ \begin{array} { c } { X T } \\ { X T ^ { 2 } } \\ { \vdots } \\ { X T ^ { j } } \end{array} \right] x = 0 ,
$$

since $\pmb { x } \in K _ { j + 1 }$ . Consequently. ${ \pmb x } \in { \bf K e r } ( X T ^ { j + 1 } )$ and so $\pmb { x } \in K _ { j + 2 }$ . Then it follows inductively that for any $i \geq j ,$ we have $K _ { i } = K _ { j }$

The lemma now shows that the inclusions in the sequence $K _ { 1 } \supset K _ { 2 } \supset$ $K _ { 3 } = \cdots$ are proper until equality first holds, and thereafter all $K _ { j } { \mathrm { ' s } }$ are equal. The least positive integer s such that $K _ { s } = K _ { s + 1 }$ is a characteristic of the admissible pair $( . 5 , T )$ and is called the index (of stabilization) of the pair. Thus, if $K _ { j }$ has dimension $k _ { j }$ , then $k _ { 1 } > k _ { 2 } > \dots > k _ { s } = k _ { s + 1 } = \cdot \cdot \cdot$ Since the first $s - 1$ inclusions are proper it is clear that $s \leq p$ (see also Exercise 3 below). The subspace $K _ { s }$ is said to be residual.

A distinction is now made between the cases when the residual subspace $K _ { s }$ is just $\{ \theta \}$ , so that $k _ { s } = 0$ and when $K _ { s }$ contains nonzero vectors, so that $k _ { s } \geq 1$ . If s is the index of stabilization of the admissible pair $( X , T )$ and $k _ { s } = 0 .$ the pair $( X , T )$ is said to be observable. Otherwise, the residual subspace $K _ { s }$ is said to be unobserrable. a terminology originating in systems theory (see Section 9.11).

Exercise 1. Let $( X , T )$ be an admissible pair of order $p ,$ and establish the following special cases.

(a) If $r = 1 , X \neq 0 .$ and $T = I _ { p }$ , then the index of $( X , I _ { p } )$ is one, and $k _ { 1 } = k _ { 2 } = \cdot \cdot \cdot = p - 1$

(b) ${ \mathrm { I f } } \ r = 1 . \ X \neq 0 .$ and $( X , T )$ are observable, then the index is $p .$

(c) If $r = p$ and det $X \neq \theta$ , then for any $p \times p$ matrix T, the pair (X, T) is observable with index one.

(d) If $\mathbf { x ^ { \mathrm { { T } } } }$ is a left eigenvector of $T ,$ then the pair $( \mathbf { x } ^ { \mathrm { { T } } } , T )$ has index $s = 1$

Exercise 2. Show that the unobservable subspace of an admissible pair (X, T) is T-invariant.

Exercise 3. If (X, T) is an admissible pair of order $p$ and has index $s ,$ and if X has rank ${ \boldsymbol { \rho } } \neq \mathbf { 0 } .$ show that

$$
\frac { p - k _ { s } } { \rho } \leq s \leq p + 1 - \rho - k _ { s } .
$$

Exercise 4. Let $( X , T )$ be admissible of order $p$ with X of size $r \times p .$ Show that for any matrix G of size $p \times r ,$ the pairs

$$
( X , T ) \qquad \mathrm { a n d } \qquad ( X , T + G X )
$$

have the same index and unobservable subspace.

Exercise 5. Let $( X , T )$ be as in Exercise 4 and let R, S be nonsingular matrices of sizes $r \times r$ and $p \times p ,$ respectively. Show that the pairs

$$
( X , T ) \qquad \mathrm { a n d } \qquad ( R X S , S ^ { - 1 } T S )
$$

have the same index and unobservable subspaces of the same dimension (admitting zero dimension in the case of observable pairs). Observe that, using Theorems 4.3.1 and 4.3.2 this exercise implies that observability can be interpreted as a property of a pair of linear transformations which have X and $T$ as matrix representations.

The next result is the form in which the observability of $( X , T )$ is usually presented. Note that the value of the index of the pair $( X , T )$ does not appear explicitly in the statement.

Theorem 1. The admissible pair $( X , T )$ of order p is observable if and only if

$$
{ \mathrm { r a n k } } { \left[ \begin{array} { c } { X } \\ { X T } \\ { \vdots } \\ { X T ^ { p - 1 } } \end{array} \right] } = p .\tag{3}
$$

ProoF. If condition (3) holds, then in the above notation, the kernel $K _ { p } = \{ \boldsymbol { \mathbf { 0 } } \}$ . Thus, the unobservable subspace is trivial and $( X , T )$ is an observable pair.

Conversely, if $( X , T )$ is observable then, by Exercise 3, the index s cannot exceed $p .$ Hence $K _ { s } = K _ { p } = \{ \pmb { \theta } \}$ , and this implies the rank condition (3).■

The results described so far in this section have a dual formulation. The discussion could begin with consideration of the subspaces of $\mathbb { C } _ { } ^ { p } { \mathrm { ~ } } _ { : }$

$$
R _ { 1 } = { \mathrm { I m ~ } } X ^ { * } , \qquad R _ { 2 } = { \mathrm { I m ~ } } X ^ { * } + { \mathrm { I m ~ } } T ^ { * } X ^ { * } ,
$$

and the trivial observation that $R _ { 1 } \subset R _ { 2 } \subset \mathbb { C } ^ { p } .$ .But there is a quicker way. Define $\begin{array} { r } { R _ { j } = \sum _ { k = 1 } ^ { j } \operatorname { I m } ( ( T ^ { * } ) ^ { k - 1 } X ^ { * } ) } \end{array}$ and observe that

$$
R _ { j } = \operatorname { I m } [ X ^ { * } \quad T ^ { * } X ^ { * } . \cdot T ^ { * j - 1 } X ^ { * } ] .\tag{4}
$$

Then Proposition 5.8.1 shows that

$$
\begin{array} { r } { \ker \left[ \begin{array} { c } { X } \\ { X T } \\ { \vdots } \\ { X T ^ { j - 1 } } \end{array} \right] \oplus \mathrm { I m } [ X ^ { * } \quad T ^ { * } X ^ { * } \cdot \cdot \cdot T ^ { * j - 1 } X ^ { * } ] = \mathbb { C } ^ { p } . } \end{array}
$$

Consequently, we have the relation

$$
K _ { j } \oplus R _ { j } = \mathbb { C } ^ { p }\tag{5}
$$

for $j = 1 , 2 , \dots .$ The properties of the sequence $K _ { 1 } , K _ { 2 } , \ldots$ . now tell us immediately that $R _ { 1 } \subset R _ { 2 } \subset \cdots \subset \mathbb { C } ^ { p }$ with proper inclusions up to $R _ { s - 1 } \subset R _ { s } ,$ where s is the index of $( X , T )$ , and thereafter $R _ { s } = R _ { s + 1 } = \cdots$ . Furthermore, $R _ { s } = \mathbb { C } ^ { p }$ if the pair $( X , ~ T )$ is observable.

In this perspective, it is said that the pair $( T ^ { * } , X ^ { * } )$ is controllable when $( X , T )$ is observable, and in this case $K _ { s } = \langle \theta \rangle$ and $R _ { s } = \mathbb { C } ^ { p } .$ If $R _ { s } \neq \mathbb { C } ^ { p } ;$ then $R _ { s }$ is called the controllable subspace and the pair $( T ^ { * } , X ^ { * } )$ is uncontrollable.

Note that, using Eq. (4) and the fact that $s \leq p ,$ we may write

$$
R _ { s } = \sum _ { k = 0 } ^ { s - 1 } \operatorname { I m } ( ( T ^ { * } ) ^ { k } X ^ { * } ) = \sum _ { k = 0 } ^ { p - 1 } \operatorname { I m } ( ( T ^ { * } ) ^ { k } X ^ { * } ) .\tag{6}
$$

The criterion of Theorem 1 now gives a criterion for controllability which is included in the following summary of our discussion.

Corollary 1. Let A and B be matrices of sizes $p \times p$ and $p \times r ,$ respectively. Then the following statements are equivalent:

(a) The pair $( A , B )$ is controllable;

(b) The pair $( B ^ { * } , A ^ { * } )$ is observable;

(c) rank[B $A B \quad \cdots \quad A ^ { p - 1 } B ] = p ;$

(d) $\begin{array} { r } { \mathbb { C } ^ { p } = \sum _ { k = 0 } ^ { p - 1 } \operatorname { I m } ( A ^ { k } B ) . } \end{array}$

Exercise 6. Consider a pair $( A , b )$ , where A is $p \times p$ and $\pmb { b } \in \mathbb { C } ^ { p } \left( \mathrm { i } . \mathrm { e } . , r = 1 \right.$ in Corollary 1). Let $A$ be simple with the spectral representation of Theorem 4.10.3, and let $\begin{array} { r } { \pmb { \flat } = \sum _ { j = 1 } ^ { p } \beta _ { j } \pmb { x } _ { j } } \end{array}$ be the representation of $\pmb { b }$ in the eigenbasis for A (with n replaced by $p )$ . Show that if $\beta _ { j } = 0$ for some $j ,$ then $( A , b )$ is not controllable.

Exercise 7. Use Exercise 4 to show that if A, B, and F are matrices of sizes $p \times p , p \times r ,$ and $r \times p ,$ , respectively, then the pairs

$$
( A , B ) \qquad \mathrm { a n d } \qquad ( A + B F , B )
$$

have the same controllable subspace.

Exercise 8. Let A, B be as in Exercise 7 and let U, V be nonsingular matrices of sizes $p \times p$ and $r \times r ,$ respectively. Use Exercise 5 to show that the pair $( A , B )$ is controllable if and only if the pair $( U ^ { - 1 } A U , U ^ { - 1 } B V )$ is controllable.

Exercise 9. Let $A \in \mathbb { C } ^ { n \times n }$ and $B \in \mathbb { C } ^ { n \times m }$ . Show that the following three statements are equivalent:

(a) The pair $( A , B )$ is controllable;

(b) For any m × n matrix K the pair $( A + B K , B )$ is controllable;

(c) For any complex number $\lambda ,$ the pair $( A - \lambda I , B )$ is controllable.

Hint. Prove that there are m × m matrices $M _ { j k } , k \ge 2 , j = 1 , 2 , \ldots , k - 1$ such that

$$
\begin{array} { l l l } { [ B } & { ( A + B K ) B } & { \cdots } & { ( A + B K ) ^ { n - 1 } B ] = } \end{array}
$$

$$
[ B \quad A B \quad \cdots \quad A ^ { n - 1 } B ] \left[ \begin{array} { l l l l l } { I } & { M _ { 1 2 } } & { \cdots } & & { M _ { 1 n } } \\ { { { \cal O } } } & { I } & & { \vdots } \\ { \vdots } & & { \ddots } & & { M _ { n - 1 , n } } \\ { { { \cal O } } } & { \cdots } & { { { \cal O } } } & { I } \end{array} \right] . \quad \sqsubseteq \quad \varTheta \left[ \begin{array} { l } { I } \\ { \cdots } \\ { \cdots } \\ { \cdots } \\ { \cdots } \end{array} \right] .
$$

## 5.14 Miscellaneous Exercises

1. For which real values of α are the following matrices positive definite:

(a)

$$
{ \left[ \begin{array} { l l l } { 1 } & { \alpha } & { \alpha } \\ { \alpha } & { 1 } & { \alpha } \\ { \alpha } & { \alpha } & { 1 } \end{array} \right] } ,
$$

(b)

$$
{ \left[ \begin{array} { l l l } { 1 } & { 1 } & { \alpha } \\ { 1 } & { 1 } & { 1 } \\ { \alpha } & { 1 } & { 1 } \end{array} \right] } .
$$

Answer. (a) $- \frac { 1 } { 2 } < \alpha < 1$ ; (b) none.

2. Let $A \in \mathbb { C } ^ { n \times n }$ and suppose $A { \boldsymbol { \mathbf { x } } } = \lambda { \boldsymbol { \mathbf { x } } }$ and $A ^ { * } y = \mu { \bf { y } } \left( { \bf { x } } , { \bf { y } } \neq 0 \right)$ . Prove that if $\lambda \neq \mu$ , then $\pmb { x } \perp \mathbf { y } .$ , and that if $\mathbf { \nabla } x = y ;$ , then $\lambda = \bar { \mu }$

3. Check that the matrix $H \geq \theta$ is positive definite if and only if det $H \neq 0 .$

4. Let $A , B \in \mathbb { C } ^ { n \times n }$ and define

$$
R = { \left[ \begin{array} { l l } { A } & { B } \\ { B } & { - A } \end{array} \right] }
$$

Show that λ is an eigenvalue of R only if — λ is an eigenvalue of R.

Hint. Observe that $P R + R P = 0$ where

$$
P = \left[ { \begin{array} { r r } { 0 } & { I } \\ { - I } & { 0 } \end{array} } \right] .
$$

5. Verify that a Hermitian unitary matrix may have only + 1 and —1 as its eigenvalues.

6. If P is an orthogonal projector and $\alpha _ { 1 } , \alpha _ { 2 }$ are nonzero real numbers, prove that the matrix $\alpha _ { 1 } ^ { 2 } P + \alpha _ { 2 } ^ { 2 } ( I - P )$ is positive definite.

Hint. Use Theorem 5.2.1.

7. Prove that an orthogonal projector that is not a zero-matrix or a unit matrix is positive semi-definite.

8. Prove that if A is Hermitian, then the matrix $I + \varepsilon A$ is positive definite for sufficiently small real numbers ε.

9. Show that a circulant matrix is normal

10. Prove that an idempotent matrix is normal if and only if it is an orthogonal projector.

11. Prove that A is a normal matrix if and only if each eigenvector of A is an eigenvector of $A ^ { * }$

Hint. See Exercise 5.2.3 and compare with Exercise 2 above.

12. Prove that if $A ^ { * } B = 0 .$ , then the subspaces Im A and Im B are orthogonal.

13. Prove that any leading principal submatrix of a positive semi-definite matrix is positive semi-definite.

Hint. See Corollary 5.5.2.

14. If A, $B \in \mathbb { C } ^ { n \times n }$ are positive semi-definite matrices, prove that

(a) The eigenvalues of AB are real and nonnegative;

(b) $A B = 0$ if and only if tr $A B = 0$

Hint. For part (a) consider the characteristic polynomial of AB, where $A = U \mathrm { d i a g } [ D _ { 0 } , { \cal O } ] U ^ { * } , D _ { 0 } \geq 0 .$

15. Prove that the Gram matrix is a positive semi-definite matrix for any system of elements and is positive definite if the system is linearly independent.

16. Let $\mathbf { \delta x } , \mathbf { y }$ be elements of a unitary space ¿ with a basis $\mathcal { E } = \{ \mathbf { { x } } _ { 1 } , \mathbf { { x } } _ { 2 } , \ldots , \mathbf { { x } } _ { n } \}$ Prove that, if α and $\pmb { \beta }$ are representations of x and y, respectively, with respect to ${ \boldsymbol { \mathscr { E } } } ,$ then

$$
( x , y ) = ( \alpha , G \beta ) ,\tag{1}
$$

where $G$ is the Gram matrix of $\clubsuit .$ T

Conversely, show that for any $G > 0 ,$ the rule in Eq. (1) gives an inner product in $\pmb { \mathcal U }$ and that G is the Gram matrix of the system $\pmb { \delta } ^ { \pmb { \sigma } }$ with respect to this inner product.

17. Let $A , B , C \in \mathbb { C } ^ { n \times n }$ be positive definite.

(a) Prove that all 2n zeros $\lambda _ { i }$ of det $( \lambda ^ { 2 } A + \lambda B + C )$ have negative real parts.

Hint. Consider the scalar polynomial $( { \bf x } , { \bf \alpha } ( \lambda _ { i } ^ { 2 } A + \lambda _ { i } B + C ) { \bf x } )$ for $\pmb { x } \in \mathrm { K e r } ( \lambda _ { i } ^ { 2 } A + \lambda _ { i } B + C )$ and use Exercise 5.10.4.

(b) Show that all zeros of det $( \lambda ^ { 2 } A + \lambda B - C )$ are real.

18. Let $A \in \mathbb { C } ^ { n \times n }$ . Prove that if there exists a positive definite $n \times n$ matrix

H such that the matrix $B \triangleq A ^ { * } H + H A$ is positive definite, then In A $= \{ n , 0 , 0 \}$

Hint. Consider the form $( B \pmb { x } , \pmb { x } )$ evaluated at the eigenvectors of A.

19. Let ${ \cal A } = { \cal H } _ { 1 } + i { \cal H } _ { 2 }$ be the Cartesian decomposition of A. Show that if $H _ { 1 } < O ,$ then ${ \dot { \pi } } ( A ) = 0$

20. Check that if $\pi ( A ) = 0 ,$ then $\pi ( A H ) = 0$ for any $H > 0 ,$

Hint. Observe that $H ^ { 1 / 2 } ( A H ) H ^ { ( - 1 / 2 ) } = H ^ { 1 / 2 } A ( H ^ { 1 / 2 } ) ^ { * }$

21. Let $H _ { 1 } = H _ { 1 } ^ { * } , H _ { 2 } \stackrel { . } { = } H _ { 2 } ^ { * }$ We write $H _ { 1 } \geq H _ { 2 }$ if $H _ { 1 } \mathrm { ~ - ~ } H _ { 2 }$ is a positive semi-definite matrix. Prove the following statements:

(a) $H _ { 1 } \geq H _ { 1 } ( s y m m e t r y ) ;$

(b) If $H _ { 1 } \geq H _ { 2 }$ and $H _ { 2 } \geq H _ { 3 }$ , then $H _ { 1 } \geq H _ { 3 }$ (transitivity);

(c) If $H _ { 1 } > O , H _ { 2 } > O ,$ and $H _ { 1 } \geq H _ { 2 }$ , then $H _ { 2 } ^ { - 1 } \geq H _ { 1 } ^ { - 1 }$

Hint. For part (c) use Exercise 20.

22. Prove the Fredholm alternative for matrices: If $A \in \mathbb { C } ^ { m \times n }$ then either the system $A \mathbf { x } = \pmb { b }$ is solvable for any $\pmb { b } \in \mathbb { C } ^ { m }$ or the homogeneous system $A ^ { * } y = \theta$ has nonzero solutions.

23. Prove that if S is real and skew-symmetric, then $I + S$ is nonsingular and the Cayley transform,

$$
T = ( I - S ) ( I + S ) ^ { - 1 } ,
$$

is an orthogonal matrix.

24. (a) If A is a real orthogonal matrix and $I + A$ is nonsingular, prove that we can write

$$
A = ( I - S ) ( I + S ) ^ { - 1 } ,
$$

where S is a real skew-symmetric matrix.

(b) If U is a unitary matrix and $I + U$ is nonsingular, show the matrix

$$
A = i ( I - U ) ( I + U ) ^ { - 1 }
$$

is Hermitian.

25. Let $B , C \in \mathbb { R } ^ { n \times n } , A = B + i C .$ and

$$
R = \left[ { \begin{array} { r r } { B } & { - C } \\ { C } & { B } \end{array} } \right] .
$$

Prove that

(a) If A is normal, then so is the real matrix R;

(b) If A is Hermitian, then R is symmetric;

(c) If A is positive definite, then so is the real matrix R;

(d) If A is unitary, then R is orthogonal.

# The Jordan Canonical Form: A Geometric Approach

Let T denote a linear transformation acting on an n-dimensional linear space $\mathcal { S }$ It has been seen in Section 4.3 that a matrix representation of T is determined by each choice of basis for ${ \mathcal { S } } ,$ that all such matrices are similar to one another, and that they form an equivalence class in the set of all $n \times n$ matrices. The simplest (canonical) matrix in the equivalence class $\mathcal { A } _ { T } ^ { 0 }$ of similar matrices (representations of $T$ in different bases of $\mathcal { S } )$ will be found in this chapter. For simple transformations, this problem has already been solved in Section 4.8; its solution was based on the existence of a basis in $\mathcal { S }$ consisting of eigenvectors of the transformation. Furthermore, the canonical form was found to be a diagonal matrix of eigenvalues.

For a general transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ there may be no eigenbasis of T in $\mathcal { S }$ Therefore, additional elements from $\mathcal { S }$ must be joined to a set of linearly independent eigenvectors of $T$ to construct a “canonical" basis for $\mathcal { S }$ with respect to which the representation of $T$ is in a canonical form (although no longer diagonal). This procedure will be performed in Section $6 . 5 ,$ after the structure of T-invariant subspaces is better understood. This is called the geometric (or operator) approach, in contrast to that presented in the next chapter and based on algebraic properties of matrices of the form $\lambda I - A$

## 6.1 Annihilating Polynomials

We shall first consider the notion of annihilating polynomials for a linear transformation $T \colon { \mathcal { S } }  { \mathcal { S } } .$ The significance of this for our geometric approach mentioned above is not immediately obvious, but it will be seen that the main result of the section, Theorem 4, does indeed present a decomposition of $\mathcal { S }$ as a direct sum of subspaces. This will be important later in the chapter.

Let $\mathcal { S }$ be a linear space over ${ \mathcal F } ,$ let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ , and let $\begin{array} { r } { p ( \lambda ) = \sum _ { i = 0 } ^ { l } p _ { i } \lambda ^ { i } } \end{array}$ $( p _ { l } \neq 0 )$ be a polynomial over ${ \mathcal { F } } .$ As with matrices (see Section 1.7), the transformation $p ( T )$ is defined by the equality $\begin{array} { r } { p ( T ) \triangleq \sum _ { i = 0 } ^ { l } p _ { i } T ^ { i } } \end{array}$

Exercise 1. Show that for any two scalar polynomials $p _ { 1 } ( \lambda )$ and $p _ { 2 } ( \lambda )$ over $\mathcal { F }$ and any $T \in { \mathcal { L } } ( { \mathcal { S } } )$ , the transformations $p _ { 1 } ( T )$ and $p _ { 2 } ( T )$ commute.

The result of the first exercise yields the possibility of substituting $T$ instead of λ in any expression consisting of sums and products of polynomials.

Exercise 2. Show that the equality

$$
p ( \lambda ) = \sum _ { j = 1 } ^ { s } \prod _ { i = 1 } ^ { k } p _ { i j } ( \lambda ) ,
$$

where $p _ { i j } ( \lambda )$ are polynomials in λ, implies

$$
p ( T ) = \sum _ { j = 1 } ^ { s } \prod _ { i = 1 } ^ { k } p _ { i j } ( T ) .
$$

Exercise 3. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and let $\mathcal { S } _ { 0 }$ be a subspace in $\mathcal { S } .$ Show that if $\mathcal { S } _ { 0 }$ is T-invariant, then it is $p ( T )$ -invariant for any polynomial $p ( \lambda )$ over $\mathcal { F } .$

Exercise 4. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ with $\mathcal { S }$ a linear space over ${ \mathcal { F } } .$ If $\lambda _ { 0 } \in \sigma ( T )$ $( \lambda _ { 0 } \in \mathcal { F } )$ , and $p ( \lambda )$ is any polynomial over ${ \mathcal F } ,$ show that $p ( \hat { \lambda } _ { 0 } ) \in \sigma ( p ( T ) )$ Moreover, if x is an eigenvector of $T$ corresponding to $\lambda _ { 0 }$ , then x is an eigenvector of $p ( T )$ associated with $p ( \lambda _ { 0 } )$

SOLUTION. If $T ( \mathbf { x } ) = \lambda _ { 0 } \mathbf { x }$ , then

$$
p ( T ) ( { \pmb x } ) = \biggl ( \sum _ { i = 0 } ^ { l } p _ { i } T ^ { i } \biggr ) ( { \pmb x } ) = \sum _ { i = 0 } ^ { l } p _ { i } \lambda _ { 0 } ^ { i } { \pmb x } = p ( \lambda _ { 0 } ) { \pmb x } . \quad \prod
$$

Theorem 1. Let $p _ { 1 } ( \lambda ) , p _ { 2 } ( \lambda ) , \ldots , p _ { k } ( \lambda )$ be arbitrary nonzero polynomials over $\mathcal { F }$ and let $p ( \lambda )$ denote their least common multiple. Then for any $T \in { \mathcal { L } } ( { \mathcal { S } } )$

$$
\ker p ( T ) = \sum _ { i = 1 } ^ { k } \operatorname { K e r } p _ { i } ( T ) .\tag{1}
$$

PROOF. Let ${ \boldsymbol { x } } \in \sum _ { i = 1 } ^ { k }$ Ker $p _ { i } ( T )$ . Then $\begin{array} { r } { \pmb { x } = \sum _ { i = 1 } ^ { k } \pmb { x } _ { i } , } \end{array}$ , where $p _ { i } ( T ) ( \mathbf { x } _ { i } ) = \mathbf { 0 } .$ $i = 1 , 2 , \ldots , k .$ Since $p ( \lambda )$ is a common multiple of $p _ { 1 } ( \lambda ) , \ldots , p _ { k } ( \lambda )$ , there exist polynomials $q _ { i } ( \lambda )$ such that $p ( \lambda ) = q _ { i } ( \lambda ) p _ { i } ( \lambda ) , i = 1 , 2 , . . . , k .$ Using Exercise 2, we obtain $p ( T ) = q _ { i } ( T ) p _ { i } ( T )$ . Hence $x _ { i } \in \mathsf { K e r } p _ { i } ( T )$ implies $\pmb { x } _ { i } \in \mathsf { K e r } p ( T )$ and consequently $\begin{array} { r } { \pmb { x } = \sum _ { i = 1 } ^ { k } \pmb { x _ { i } } \in \mathrm { K e r } p ( T ) } \end{array}$ . Thus, $\sum \limits _ { i = 1 } ^ { k }$ Ker $p _ { i } ( T )$ $\mathbf { \Sigma } \subset \mathop { \bf K e r } p ( T )$ for any common multiple $p ( \lambda )$ of $p _ { 1 } ( \lambda ) , p _ { 2 } ( \lambda ) , \ldots , p _ { k } ( \lambda )$

The opposite inclusion can be proved by induction on k. The crux of the argument is contained in the case $k = 2$ . So first let $k = 2$ and assume $p ( T ) ( \mathbf { x } ) = \pmb { \theta } .$ Then, as in the first part of the proofs, $p _ { i } ( T ) q _ { i } ( T ) ( \mathbf { x } ) = \pmb { \theta }$ for $i = 1 , 2$ If ${ \bf y } _ { i } = q _ { i } ( T ) ( { \bf x } )$ then, obviously, $y _ { i } \in \mathsf { K e r } p _ { i } ( T )$ . Furthermore, $p ( \lambda )$ is the least common multiple of $p _ { 1 } ( \lambda )$ and $p _ { 2 } ( \lambda )$ and, therefore, the polynomials $q _ { 1 } ( \lambda )$ and $\mathbf { \ } q _ { 2 } ( \lambda )$ are relatively prime. (See Exercise 8 in Appendix 1.) This is equivalent (see Eq. (3) in Appendix 1) to saying that $c _ { 1 } ( \lambda ) q _ { 1 } ( \lambda ) + c _ { 2 } ( \lambda ) q _ { 2 } ( \lambda )$ $= 1$ for some polynomials $c _ { 1 } ( \lambda )$ and $c _ { 2 } ( \lambda )$ . Thus there are polynomials $c _ { i } ( \lambda ) ( i = 1 , 2 )$ such that

$$
c _ { 1 } ( T ) q _ { 1 } ( T ) + c _ { 2 } ( T ) q _ { 2 } ( T ) = I .
$$

Writing $\begin{array} { r } { { \pmb x } _ { i } = c _ { i } ( T ) ( { \pmb y } _ { i } ) . } \end{array}$ and applying this representation of I to x we obtain $\pmb { x } = \pmb { x } _ { 1 } + \pmb { x } _ { 2 }$ , where $x _ { i } \in \mathrm { K e r } \ p _ { i } ( T ) \quad ( i = 1 , 2 )$ Hence $\pmb { x } \in \mathbb { K }$ er $p _ { 1 } ( T )$ + Ker $p _ { 2 } ( T ) .$ , as required.

Now let the result hold for the polynomials $p _ { 1 } ( \lambda ) , \ p _ { 2 } ( \lambda ) , \dots , p _ { n - 1 } ( \lambda )$ $( 2 < n \leq k )$ . Thus if $\tilde { p } ( \lambda )$ denotes their least common multiple, then

$$
\ker \tilde { p } ( T ) = \sum _ { i = 1 } ^ { n - 1 } \operatorname { K e r } p _ { i } ( T ) .
$$

But the least common multiple $p ( \lambda )$ of $p _ { 1 } ( \lambda ) , \ldots , p _ { n } ( \lambda )$ coincides with the least common multiple of $\tilde { p } ( \lambda )$ and $p _ { n } ( \lambda )$ (Exercise 9 in Appendix 1) Therefore, using the already proved part of the theorem and the inductive hypothesis,

$$
\operatorname { K e r } p ( T ) = \operatorname { K e r } { \tilde { p } } ( T ) + \operatorname { K e r } p _ { n } ( T ) = \sum _ { i = 1 } ^ { n } \operatorname { K e r } p _ { i } ( T ) .
$$

The proof is complete.■

Theorem 2. If, in the notation of Theorem I, each pair of polynomials selected from $\{ p _ { 1 } ( \lambda ) , p _ { 2 } ( \lambda ) , \ldots , p _ { k } ( \lambda ) \}$ is relatively prime, then

$$
\operatorname { K e r } p ( T ) = \sum _ { i = 1 } ^ { k } \cdot \operatorname { K e r } p _ { i } ( T ) .\tag{2}
$$

ProoF. Consider the case $k = 2$ . To show that the given sum is direct, it suffices to show that Ker $p _ { 1 } ( T ) \cap \mathop { \mathrm { K e r } } p _ { 2 } ( T ) = \{ \pmb { 0 } \}$ . But if simultaneously

$p _ { 1 } ( T ) ( x ) = 0$ and $p _ { 2 } ( T ) ( x ) = 0$ then, since $p _ { 1 } ( \lambda )$ and $p _ { 2 } ( \lambda )$ are relatively prime (see Theorem 3 in Appendix 1)

$$
I ( x ) = c _ { 1 } ( T ) p _ { 1 } ( T ) ( x ) + c _ { 2 } ( T ) p _ { 2 } ( T ) ( x ) = 0 ,
$$

and consequently the required result: $\pmb { x } = \pmb { 0 }$ An induction argument like that of Theorem 1 completes the proof.

Note that the hypothesis on the polynomials in Theorem 2 is stronger than the condition that the set $\{ p _ { i } ( \lambda ) \} _ { i = } ^ { k }$ , be relatively prime. (See Exercise 4 in Appendix 1 and recall that the polynomials being considered are assumed to be monic.)

Now we define a nonzero scalar polynomial $p ( \lambda )$ over $\mathcal { F }$ to be an annihilating polynomial of the transformation $T$ if $p ( T )$ is the zero transformation: $p ( T ) = O$ . It is assumed here, and elsewhere, that $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and $\mathcal { S }$ is over $\mathcal { F } .$

Exercise 5. Show that if $p ( \lambda )$ is an annihilating polynomial for T, then so is the polynomial $p ( \lambda ) q ( \lambda )$ for any $q ( \lambda )$ over $\mathcal { F } .$

Exercise 6. Check that if $p ( \lambda )$ is an annihilating polynomial of $T$ and $\lambda _ { 0 } \in \sigma ( T ) , \lambda _ { 0 } \in \mathcal { F } ,$ then $p ( \lambda _ { 0 } ) = 0$ (See Exercise 4.)

In other words, Exercise 6 shows that the spectrum of a transformation $T$ is included in the set of zeros of any annihilating polynomial of T. Note that, in view of Exercise 5, the converse cannot be true.

Theorem 3. For any $T \in { \mathcal { L } } ( { \mathcal { S } } )$ there exists an annihilating polynomial of degree $l \leq n ^ { 2 }$ , where n = dim S.

ProoF. We first observe that the existence of a (monic) annihilating polynomial $p ( \lambda )$ for T is provided by Exercise 4.1.12 and is equivalent to the condition that T be a linear combination of the transformations $T ^ { l }$ $T ^ { i } ,$ $i = 0 , 1 , \ldots , l - 1$ , viewed as elements in ${ \mathcal { L } } ( { \mathcal { S } } )$ . (We define $T ^ { 0 } \triangleq I . )$ Thus, for some $p _ { 0 } , p _ { 1 } , \dotsc , p _ { l - 1 } \in \mathcal { F } ,$

$$
T ^ { l } = { { } - p _ { 0 } } I - p _ { 1 } T - \cdot \cdot \cdot - p _ { l - 1 } T ^ { l - 1 } .\tag{3}
$$

To verify Eq. (3), we examine the sequence $I , T , T ^ { 2 } , \ldots$ . Since the dimension of the linear space ${ \mathcal { L } } ( { \mathcal { S } } )$ is $n ^ { 2 }$ (see Exercise 4.1.8), at most $n ^ { 2 }$ elements in this sequence are linearly independent. Thus there exists a positive integer $l ( 1 \leq l \leq n ^ { 2 } )$ such that $I , \bar { T _ { 9 } } . . . , T ^ { l - 1 }$ viewed as elements in ${ \mathcal { L } } ( { \mathcal { S } } )$ are linearly independent, while $I , T , \dots , T ^ { I }$ form a linearly dependent system. Hence $T ^ { l }$ is a linear combination of $T ^ { i } , i = 0 , 1 , . . . , l - 1$ . This proves the theorem.

The main result follows readily from Theorem 2, bearing in mind that if $p ( T ) = 0$ then $\begin{array} { r } { \mathsf { K e r } ( p ( T ) ) = \mathcal { S } . } \end{array}$

Theorem 4. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and let $p ( \lambda )$ denote an annihilating polynomial of T. If $p ( \lambda ) = \prod _ { i = 1 } ^ { k } p _ { i } ( \lambda )$ for some polynomials $p _ { 1 } ( \lambda ) , \ldots , p _ { k } ( \lambda )$ and if each pair of polynomials selected from $\{ p _ { 1 } ( \lambda ) , p _ { 2 } ( \lambda ) , . . . , p _ { k } ( \lambda ) \}$ is relatively prime, then

$$
\mathcal { S } = \sum _ { i = 1 } ^ { k } \cdot \operatorname { K e r } p _ { i } ( T ) .\tag{4}
$$

Theorem 4 is the main conclusion of this section and, as it will be seen, allows us to study the action of $T$ on $\mathcal { S }$ in terms of its action on the $( T -$ invariant) subspaces $p _ { i } ( T )$ .

Exercise 7. Suppose $\lambda _ { 1 } \neq \lambda _ { 2 }$ and the matrix

$$
A = { \left[ \begin{array} { l l l l } { \lambda _ { 1 } } & { 1 } & { 0 } & { 0 } \\ { 0 } & { \lambda _ { 1 } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { \lambda _ { 2 } } & { 1 } \\ { 0 } & { 0 } & { 0 } & { \lambda _ { 2 } } \end{array} \right] }
$$

is viewed as a linear transformation on $\mathbb { C } ^ { 4 }$ . Show that

$$
p ( \lambda ) \triangleq ( \lambda - \lambda _ { 1 } ) ^ { 2 } ( \lambda - \lambda _ { 2 } ) ^ { 2 }
$$

is an annihilating polynomial for A and verify Theorem 4 with $p _ { 1 } ( \lambda ) =$ $( \lambda - \lambda _ { 1 } ) ^ { 2 }$ and $p _ { 2 } ( \lambda ) = ( \lambda - \lambda _ { 2 } ) ^ { 2 }$

Show that the conclusion does not hold with the choice of factors $q _ { 1 } ( \lambda ) = q _ { 2 } ( \lambda ) = ( \lambda - \lambda _ { 1 } ) ( \lambda - \lambda _ { 2 } )$ for $p ( \lambda )$ . □

## 6.2 Minimal Polynomials

It is clear that a fixed linear transformation $T \in { \mathcal { L } } ( { \mathcal { S } } )$ has many annihilating polynomials. It is also clear that there is a lower bound for the degrees of all annihilating polynomials for a fixed T. It is natural to seek a monıc annihilating polynomial of the least possible degree, called a minimal polynomial for Tand written $m _ { T } ( \lambda )$ , or just m(λ). It will be shown next that the set of all annihilating polynomials for T is “well ordered" by the degrees of the polynomials and, hence, there is a unique minimal polynomial

Theorem 1. A minimal polynomial of $T \in { \mathcal { L } } ( { \mathcal { S } } )$ divides any other annihilating polynomial of T.

PROOF. Let $p ( \lambda )$ be an annihilating polynomial of T and let $m ( \lambda )$ denote a minimal polynomial of the transformation. Using Theorem 1 of Appendix 1, we write

$$
p ( \lambda ) = m ( \lambda ) d ( \lambda ) + r ( \lambda ) ,\tag{1}
$$

where either deg $\boldsymbol { r } ( \lambda ) < \deg { m ( \lambda ) }$ or $r ( \lambda ) \equiv 0 .$ Assuming that $m ( \lambda )$ does not divide $p ( \lambda )$ , that is, $r ( \lambda ) \not \equiv 0 ,$ we arrive at a contradiction. Indeed, applying the result of Exercise 6.1.2 to Eq. (1), we find from $p ( T ) = m ( T ) = 0$ that $r ( T ) = 0$ Hence $r ( \lambda )$ is an annihilating polynomial of T of degree less than that of the minimal polynomial $m ( \lambda )$ . This conflicts with the definition of $m ( \lambda )$

Corollary 1. The minimal polynomial of T is unique

PROOF. If $m _ { 1 } ( \lambda )$ and $m _ { 2 } ( \lambda )$ are minimal polynomials of the transformation T, then by Theorem 1 each of them divides the other. Since both of them are monic, Exercise 2 of Appendix 1 yields $m _ { 1 } ( \lambda ) = m _ { 2 } ( \lambda )$

Corollary 2. The set of all annihilating polynomials of $T$ consists of all polynomials divisible by the minimal polynomial of T.

ProoF. To see that every polynomial divisible by $m ( \lambda )$ is an annihilating polynomial of T, it suffices to recall the result of Exercise 6.1.5.

Theorem 2. The set of the distinct zeros of the minimal polynomial of T coincides with the spectrum of T.

PRooF. In view of Exercise 6.1.6, it suffices to show that any zero of the minimal polynomial $m ( \lambda )$ of T belongs to the spectrum $\sigma ( T )$ of T.

Let $m ( \lambda ) = q ( \lambda ) \prod _ { i = 1 } ^ { k } { ( \lambda - \lambda _ { i } ) }$ , where q(λ) is irreducible over F. Assume on the contrary that $\lambda _ { s } \notin \sigma ( T ) ( 1 \le s \le k ) .$ ; in other words, $T - \lambda _ { s } I$ is nonsingular. Since $m ( T ) = 0 { \mathrm { . } }$ , Exercise 6.1.2 implies

$$
q ( T ) \prod _ { i = 1 , i \ne s } ^ { k } \left( T - \lambda _ { i } I \right) = 0 .
$$

Hence $\tilde { m } ( \lambda ) = m ( \lambda ) / ( \lambda - \lambda _ { s } )$ is an annihilating polynomial of T. This contradicts the assumption that $m ( \lambda )$ is minimal and shows that $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { k } \in \sigma ( T )$ as required.

In this chapter the nature of the field $\mathcal { F }$ has not played an important role. Now, and for the rest of the chapter, it is necessary to assume that $\mathcal { F }$ is algebraically closed (see Appendix 1). In fact, we assume for simplicity that ${ \mathcal { F } } = \mathbb { C } ,$ , although any algebraically closed field could take the place of C.

Corollary 1. Let ${ \mathcal { F } } = \mathbb { C } ,$ and let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ , with $\boldsymbol { \sigma } ( T ) = \{ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { s } \}$ The minimal polynomial m(λ) of $T$ is given by

$$
m ( \lambda ) = \prod _ { i = 1 } ^ { s } ( \lambda - \lambda _ { i } ) ^ { m _ { i } }\tag{2}
$$

for some positive integers $m _ { i } ( i = 1 , 2 , \ldots , s )$

The exponent $m _ { i }$ associated with the eigenvalue $\lambda _ { i } \in { \mathfrak { o } } ( A )$ is clearly unique (see Corollary 1 of Theorem 1). It plays an important role in this and subsequent chapters and is known as the index of $\lambda _ { i }$

Applying Theorem 6.1.4 to $m ( \lambda )$ written in the form (2), we arrive at the following important decomposition of a linear transformation.

Theorem 3. Let $T \in { \mathcal { L } } ( { \mathcal { S } } ) ,$ let $\boldsymbol { \sigma } ( T ) = \{ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { s } \}$ ; and let $\lambda _ { i }$ have index $m _ { i } f o r$ each i. Then

$$
T = \sum _ { i = 1 } ^ { s } \cdot \ : T | _ { \mathfrak { s } _ { i } } ,\tag{3}
$$

where, for $i = 1 , 2 , \ldots , s ,$

$$
\mathcal { G } _ { i } = \mathrm { K e r } ( ( T - \lambda _ { i } I ) ^ { m _ { i } } )\tag{4}
$$

is a T-invariant subspace

PRooF. By Eq. (6.1.5) we have, on putting $p _ { i } ( \lambda ) = ( \lambda - \lambda _ { i } ) ^ { m _ { i } } , i = 1 , 2 , \ldots , s ,$

$$
{ \mathcal { S } } = \sum _ { i = 1 } ^ { s } \cdot { \mathcal { G } } _ { i } .\tag{5}
$$

Therefore, recalling the definition of the direct sum of transformations, it suffices to show that each $\mathscr { G } _ { i }$ is T-invariant. Indeed, if $\pmb { x } \in \mathcal { G } _ { i }$ then $( T - \lambda _ { i } I ) ^ { m _ { i } } ( x )$ ${ \bf \mu } = \pmb { \mathbb { \mathbb { \mathbb { \mathbb { \mathbb { \mathbb { \Lambda } } } } } } } \mathbf { \mathbb { \mathbb { \Lambda } } } \mathbf { \mathbb { \Lambda } } = \pmb { \mathbb { \mathbb { \mathbb { \mathbb { \Lambda } } } } } \mathbf { \mathbb { \pmb { \mathbb { \mathbb { \Lambda } } } } } \mathbf { \mathbb { \mathbb \Lambda } } \mathbf { \mathbb { \Lambda } }$ Thus, by Exercise 6.1.1,

$$
( T - \lambda _ { i } I ) ^ { m _ { i } } T ( x ) = T ( T - \lambda _ { i } I ) ^ { m _ { i } } ( x ) = 0
$$

and $T ( x ) \in \mathcal G _ { i }$ for $1 \leq i \leq s$ , showing that $\mathscr { G } _ { i }$ is T-invariant.

Now it is to be shown that for $j = 1 , 2 , \dots , s ,$ the minimal polynomial of $T _ { j } = T | _ { \mathfrak { s } _ { j } }$ acting in $\mathscr { G } _ { j }$ is $( \lambda - \lambda _ { j } ) ^ { m _ { j } } .$ Indeed, if $I _ { j }$ denotes the identity transformation in $\mathscr { G } _ { j }$ , then for any $\mathbf { \boldsymbol { x } } \in \mathcal { G } _ { j }$ we have

$$
( T _ { j } - \lambda _ { j } I _ { j } ) ^ { m _ { j } } ( x ) = ( T - \lambda _ { j } I ) ^ { m _ { j } } ( x ) = 0
$$

and, therefore, $( T _ { j } - \lambda _ { k } I _ { j } ) ^ { m _ { j } } = 0 ( \mathrm { i n } \mathcal { G } _ { j } ) .$ Thus, $( \lambda - \lambda _ { j } ) ^ { m _ { j } }$ is an annihilating polynomial of $T _ { j }$ . Assume that this polynomial is not minimal, and let $( \lambda - \lambda _ { j } ) ^ { r _ { j } } ( r _ { j } < m _ { j } )$ be the minimal polynomial of $T _ { j }$ . Write

$$
m _ { 1 } ( \lambda ) = ( \lambda - \lambda _ { j } ) ^ { r _ { j } } \prod _ { i = 1 , i \neq j } ^ { s } ( \lambda - \lambda _ { i } ) ^ { m _ { i } } .
$$

In view of $\mathbf { E q . } ( 5 ) ;$ , we may represent any $\pmb { x } \in \mathcal { S }$ as $\begin{array} { r } { \pmb { x } = \sum _ { i = 1 } ^ { s } \pmb { x } _ { i } , } \end{array}$ where $\pmb { x _ { i } } \in \mathcal { G } _ { i }$ for $i = 1 , 2 , \ldots , s .$ Then, using the commutativity of polynomials in $T$ and the conditions $( T _ { i } - \lambda _ { i } I _ { i } ) ^ { m _ { i } } x _ { i } = \pmb { \theta } ( i = 1 , 2 , \ldots , s , i \neq j )$ and $( T _ { j } - \lambda _ { j } I _ { j } ) ^ { r _ { j } } ( x _ { j } )$ ${ } = \mathbf { \nabla } \theta ,$ , it is easily found that $m _ { 1 } ( T ) = 0$ Since $m _ { 1 } ( \lambda )$ is annihilating and divides the minimal polynomial $m ( \lambda ) ,$ , a contradiction is obtained.■

Proposition 1. With the notation of Theorem 3, dim $\mathcal { G } _ { i } \geq m _ { i }$

ProoF. It has been shown above that $( \lambda - \lambda _ { i } ) ^ { m _ { i } }$ is the minimal polynomial of $T _ { i }$ . Hence $( T _ { i } - \lambda _ { i } I ) ^ { m _ { i } } = 0$ and $( T _ { i } - \lambda _ { i } I ) ^ { m _ { i } = 1 } \neq 0 .$ From Exercise 4.5.14 we see that

$$
\operatorname { K e r } ( T _ { i } - \lambda _ { i } I ) \subset \operatorname { K e r } ( T _ { i } - \lambda _ { i } I ) ^ { 2 } \subset \dots \subset \operatorname { K e r } ( T _ { i } - \lambda _ { i } I ) ^ { m _ { i } } ,
$$

each inclusion being strict, and $\dim ( \mathbf { K e r } ( T _ { i } - \lambda _ { i } I ) ) \geq 1$ Consequently,

$$
\dim { \mathcal { G } } _ { i } = \dim ( \operatorname { K e r } ( T _ { i } - \lambda _ { i } I ) ^ { m _ { i } } ) \geq m _ { i } . \quad |
$$

Exercise 1. Show that if $\mathcal { S }$ has dimension n and $T \in { \mathcal { L } } ( { \mathcal { S } } )$ , then the degree of the minimal polynomial of T does not exceed n.

Note that the spectrum of each $T _ { i } = \left. T \right| _ { \mathfrak { s } _ { i } }$ in Eq. (3) consists of one point only and that $\sigma ( T _ { i } ) \cap \sigma ( T _ { j } ) = \phi$ for $i \neq j .$ It turns out that the decomposition of a linear'transformation into a direct sum of such transformations is unique.

Theorem 4 The representation (3) is unique (up to the order of summands).

PRoOF. Indeed, let $\tilde { T } \sum _ { i = 1 } ^ { s } \cdot \tilde { T } _ { i }$ , where $\sigma ( \widetilde { T } _ { i } ) = \{ \lambda _ { i } \} ( 1 \leq i \leq s )$ and $\lambda _ { i } \neq \lambda _ { j }$ if $i \neq j .$ If $( \lambda - \lambda _ { i } ) ^ { r _ { i } }$ is the minimal polynomial of $\widetilde { T } _ { i }$ (by Theorem 2, only such polynomials can be minimal for $\dot { \widetilde { T } } _ { i } )$ , then the product $\prod _ { i = 1 } ^ { s } ( \lambda - \lambda _ { i } ) ^ { r _ { i } }$ $( i = 1 , 2 , \dots , s )$ must coincide with the minimal polynomial $m ( \lambda )$ of $T .$ This is easily checked by repeating th: argument used in the proof of Theorem 3.

The fundamental result obtained in Theorem 3 will be developed further in Section 4 after the structure of the subspaces $\mathcal { G } _ { 1 } , \mathcal { G } _ { 2 } , \ldots , \mathcal { G } _ { s }$ in Eq. (4) is studied.

Considering the representations of T and the $T _ { i } \mathbf { \hat { s } }$ together with the ideas of Section 4.8, we immediately obtain the following consequences of Theorems 3 and 4.

Corollary 1. Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ with $\mathcal { F } = \mathbb { C }$ There exists a basis in $\mathcal { S }$ in which the representation A of T is a complex block-diagonal matrix

$$
A = \mathrm { d i a g } [ A _ { 1 } , A _ { 2 } , . . . , A _ { s } ] ,\tag{6}
$$

and the spectrum of $A _ { i } \left( 1 \leq i \leq s \right)$ consists of one point only. Moreover, these points are distinct and $i f q _ { i }$ is the size of $A _ { i } , 1 \leq i \leq s .$ then $q _ { 1 } , q _ { 2 } , \ldots , q _ { s }$ are uniquely determined by T.

It will be shown later (see Proposition 6.6.1) that the numbers $q _ { 1 } , q _ { 2 } , \ldots , q _ { s }$ are, in fact, the algebraic multiplicities of the eigenvalues of T (or of A).

Note that each matrix A in Eq. (6) can also be described as a representa- $A _ { i }$ tion of the transformation $T _ { i } = T | _ { \mathfrak { s } _ { \mathrm { \ i } } }$ with respect to an arbitrary basis in $\mathscr { G } _ { i }$ Corollary 1 above can be restated in the following equivalent form.

Corollary 2. Any complex square matrix B is similar to a matrix A of the form (6), where $\begin{array} { r } { \dot { A } _ { i } \in \mathcal { F } ^ { q _ { i } \times q _ { i } } , \sigma ( A _ { i } ) = \{ \lambda _ { i } \} , 1 \leq i \leq s , } \end{array}$ and the numbers $q _ { i }$ are uniquely determined by B.

Note that the positive integer s in Eq. (6) can be equal to 1, in which case the spectrum of T consists of a single point.

Exercise 2. Let λ be an eigenvalue of two similar matrices A and B. Show that the indices of λ with respect to A and to B are equal.

The final theorem of the section is known as the Cayley-Hamilton theorem and plays an important part in matrix theory. Another proof will appear in Section 7.2 in terms of matrices rather than linear transformations.

Theorem 5. The characteristic polynomial c(λ) of $T \in { \mathcal { L } } ( { \mathcal { S } } )$ is one of its annihilating polynomials: $c ( T ) = 0 .$

ProoF. First recall that the characteristic polynomial of a linear transformation is just that of any of its representations (see Section 4.11). Referring to Eq. (6), we see that c(T) is just the product of the characteristic polynomials of $A _ { 1 } , A _ { 2 } , \ldots , A _ { s }$ . For $j = 1 , 2 , \dots , s ,$ the size of the square matrix $A _ { j }$ is just $q _ { j } = \dim \mathcal { G } _ { j }$ and $\sigma ( A _ { j } ) = \{ \lambda _ { j } \}$ . Consequently, the characteristic polynomial of $A _ { j }$ is $( \lambda - \lambda _ { j } ) ^ { q _ { j } }$ Then, by Proposition 1, $q _ { j } \geq m _ { j }$ . Finally, since

$$
c ( T ) = c ( A ) = \prod _ { j = 1 } ^ { s } ( \lambda - \lambda _ { j } ) ^ { q _ { j } }
$$

and

$$
m ( T ) = \sum _ { j = 1 } ^ { s } { ( \lambda - \lambda _ { j } ) ^ { m _ { j } } } ,
$$

it is clear that c(T) is divisible by m(T). By Corolary 2 to Theorem 1 the $c ( T )$ conclusion is obtained.

Exercise 3. Use the Cayley-Hamilton theorem to check that the matrix A of Exercise 4.11.1 satisfies the equation

$$
A ^ { 3 } = 4 A ^ { 2 } - A + 6 I .
$$

Exercise 4. Check that $m ( \lambda ) = ( \lambda - 4 ) ^ { 2 } ( \lambda - 2 )$ is the minimal polynomial of the matrix

$$
A = { \left[ \begin{array} { l l l } { 6 } & { 2 } & { 2 } \\ { - 2 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 2 } \end{array} \right] } . \quad \Pi
$$

## 6.3 Generalized Eigenspaces

In the previous section it was shown that if $T \in { \mathcal { L } } ( { \mathcal { S } } )$ , the action of $T$ on $\mathcal { S }$ can be broken down to the study of the action of the more primitive transformations $T _ { i } = \left. T \right| _ { \mathfrak { s } _ { i } }$ on the T-invariant subspaces ${ \pmb { \mathscr { G } } } _ { i }$ of Eq. (6.2.4). To continue with the “decomposition" of $T ,$ we now study the structure of these subspaces more closely. Also, a technique will be developed in Section 9.5 that generates a system of projectors onto the subspaces $\mathcal { G } _ { 1 } , \ldots , \mathcal { G } _ { s }$

Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ with $\mathcal { F } = \mathbb { C } , \ \lambda \in \sigma ( T )$ , and $\mathcal { S } _ { r } = \mathop { \mathrm { K e r } } ( T - \lambda I ) ^ { r }$ , where r varies over the set of nonnegative integers. Exercise 4.5.14 asserts that

$$
\{ \pmb { \theta } \} = \mathcal { S } _ { \pmb { \theta } } \subset \mathcal { S } _ { 1 } \subset \mathcal { S } _ { 2 } \subset \cdots \subset \mathcal { S } _ { p } = \mathcal { S } _ { p + 1 } = \cdots \subset \mathcal { S }\tag{1}
$$

for some positive integer $p .$ Note that $\mathcal { S } _ { 1 }$ is the eigenspace of T associated with $\lambda ;$ the strict inclusion $\{ \pmb { \theta } \} \subset \mathcal { S } _ { 1 }$ follows from the assumption $\lambda \in \sigma ( T )$ .•

Exercise 1. Check that $\mathbf { \boldsymbol { x } } \in \mathcal { S } _ { r }$ if and only if $( T - \lambda I ) ( { \pmb x } ) \in \mathcal { S } _ { r - 1 }$ .□

The subspace $\mathcal { S } _ { r } ( 1 \leq r \leq p )$ in (1) is referred to as a generalized eigenspace of $T$ of order r associated with the eigenvalue λ. Also, a nonzero element x such that $\mathbf { \boldsymbol { x } } \in \mathcal { S } _ { r }$ but $x \notin \mathcal { S } _ { r - 1 }$ is said to be a generalized eigenvector of $T$ of order r corresponding to the eigenvalue $\lambda ,$ that is,

$$
\pmb { x } \in \mathrm { K e r } ( T - \lambda I ) ^ { r } , \qquad \mathsf { b u t } \qquad \pmb { x } \notin \mathrm { K e r } ( T - \lambda I ) ^ { r - 1 } .
$$

In particular, the customary eigenvectors of T can be viewed as generalized eigenvectors of T of order 1 corresponding to the same eigenvalue. The same can be said with regard to eigenspaces and generalized eigenspaces of order 1 of the transformation. Note that throughout this section, all generalized eigenvectors and eigenspaces are assumed (if not indicated otherwise) to be associated with the fixed eigenvalue λ of $T .$

It is important to note that the subspaces $\mathscr { G } _ { i }$ of Eq. (6.2.4) are generalized eigenspaces, and the basic decomposition of Theorem 6.2.3 depends on the decomposition (6.2.5) of the whole space $\mathcal { S }$ into a direct sum of generalized eigenspaces.

Exercise 2. Show that $\mathbf { \delta } _ { \mathbf { \lambda } ^ { \mathbf { X } } \mathbf { \lambda } ^ { \mathbf { \alpha } } }$ is a generalized eigenvector of $T$ of order $r \geq 2$ (corresponding to the eigenvalue $\lambda )$ if and only if the element $x _ { r - 1 } =$ $( T - \lambda I ) ( x _ { r } )$ is a generalized eigenvector of $T$ of order $r - 1$ , or, equivalently,

$$
T ( { \boldsymbol { \mathbf { x } } } _ { r } ) = \lambda { \boldsymbol { \mathbf { \mathit { x } } } } _ { r } + { \boldsymbol { \mathbf { \mathit { x } } } } _ { r - 1 } ,\tag{2}
$$

where ${ \pmb x } _ { r - 1 } \in \mathcal { S } _ { r - 1 } , { \pmb x } _ { r - 1 } \notin \mathcal { S } _ { r - 2 }$

Exercise 3. Check that $\mathbf { \delta x } _ { r }$ is a generalized eigenvector of $T$ of order $r \geq 1$ if and only if the vector $( T - \lambda I ) ^ { r - 1 } ( { \bf x } _ { r } )$ is an eigenvector of $T$ or, equivalently, $( T - \lambda I ) ^ { k } ( \mathbf { x } _ { r } ) = 0$ for $k \geq r$ □

Using Exercise $^ { 2 , }$ observe that if $\scriptstyle \mathbf { \pmb { x } } _ { r }$ is a generalized eigenvector of $T$ of order $r ,$ then there are vectors $\pmb { x } _ { r - 1 } , \ldots , \pmb { x } _ { 2 } , \pmb { x } _ { 1 }$ for which

$$
\begin{array} { c } { T ( { \boldsymbol x } _ { 1 } ) = \lambda { \boldsymbol x } _ { 1 } } \\ { T ( { \boldsymbol x } _ { 2 } ) = \lambda { \boldsymbol x } _ { 2 } + { \boldsymbol x } _ { 1 } , } \\ { \vdots } \\ { T ( { \boldsymbol x } _ { r } ) = \lambda { \boldsymbol x } _ { r } + { \boldsymbol x } _ { r - 1 } , } \end{array}\tag{3}
$$

where $\boldsymbol { x } _ { j } \in \mathcal { S } _ { j }$ for $j = 1 , 2 , \dots , r .$ Such a sequence $\pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \dots , \pmb { x } _ { r }$ is called a Jordan chain of length r associated with the eigenvalue $\lambda .$ The chain may also be seen as being associated with $\pmb { x } _ { 1 }$ . From this point of view, an eigenvector $\mathbf { x _ { 1 } }$ is selected and the vectors $x _ { 2 } , \ldots , x ,$ . are generated by successively solving the equations of (3) for as long as there exist solutions to the nonhomogeneous equation $( T - \lambda I ) x _ { j } = x _ { j - 1 }$ for $j = 2 , 3 , \dots .$ Obviously, the length of any Jordan chain of T is finite since $r \leq$ dim $\mathcal { S } _ { p } \leq$ dim $\mathcal { S }$ for a chain of length r. Furthermore, the members of a Jordan chain are linearly independent, as the next exercise demonstrates.

Exercise 4. Show that any Jordan chain consists of linearly independent elements.

SOLUTION. Let $\begin{array} { r } { \sum _ { i = 1 } ^ { r } \pmb { x } _ { i } \pmb { x } _ { i } = \pmb { \theta } . } \end{array}$ Applying the transformation $( T - \lambda I ) ^ { r - 1 }$ to both sides of this equation and noting that $( T - \lambda I ) ^ { r - 1 } ( { \bf x } _ { i } ) = \pmb { \theta }$ for $1 \leq i \leq r - 1$ (Exercise 3), we obtain $\alpha _ { r } ( T - \lambda I ) ^ { r - 1 } ( x _ { r } ) = 0 .$ By Exercise 3 the element $( T - \lambda I ) ^ { r - 1 } ( \pmb { x } _ { r } )$ is an eigenvector of T and hence nonzero. Thus, $\mathfrak { X } _ { r } = 0$ Applying the transformation $( T - \lambda I ) ^ { r - 2 }$ to the equation $\begin{array} { r } { \sum _ { i = 1 } ^ { r - 1 } \pmb { \alpha } _ { i } \pmb { x } _ { i } = \pmb { \theta } _ { 2 } } \end{array}$ we similarly derive $\pmb { \alpha _ { r - 1 } } = 0$ . Repeating this procedure, the linear independence of the set of generalized eigenvectors of the Jordan chain is established.

In particular, Exercise 4 shows that the Jordan subspace for $T ,$

$$
{ \mathcal { J } } = \operatorname { s p a n } \{ x _ { 1 } , x _ { 2 } , . ~ . ~ . , x _ { r } \} ,\tag{4}
$$

generated by the elements of a Jordan chain of T of length r has dimension r.

Exercise 5. Check that any Jordan subspace for T is T-invariant.

Exercise 6. Prove that any Jordan subspace contains only one (linearly independent) eigenvector.

SoLUTIoN. Suppose the Jordan subspace is generated by the chain $\mathbf { x } _ { 1 } ,$ $\cdots , x _ { r }$ and has associated eigenvalue λ. If $\begin{array} { r } { \pmb { x } = \sum _ { i = 1 } ^ { r } \pmb { \alpha _ { i } } \pmb { x _ { i } } } \end{array}$ is an eigenvector of T associated with $\lambda _ { 0 }$ , then using Eq. (2) we have (with $x _ { 0 } = \theta )$

$$
\lambda _ { 0 } \sum _ { i = 1 } ^ { r } \alpha _ { i } \mathbf { x } _ { i } = T { \Biggr ( } \sum _ { i = 1 } ^ { r } \alpha _ { i } \mathbf { x } _ { i } { \Biggr ) } = \sum _ { i = 1 } ^ { r } \alpha _ { i } ( \lambda x _ { i } + \mathbf { x } _ { i - 1 } ) .
$$

Consequently, comparing the coefficients (see Exercise 4),

$$
\begin{array} { r l } & { \lambda _ { 0 } \alpha _ { i } = \lambda \alpha _ { i } + \alpha _ { i + 1 } , \qquad 1 \leq i \leq r - 1 , } \\ & { \lambda _ { 0 } \alpha _ { r } = \lambda \alpha _ { r } , } \end{array}
$$

so that $\lambda = \lambda _ { 0 }$ and $\alpha _ { 2 } = \alpha _ { 3 } = \cdot \cdot \cdot = \alpha _ { r } = 0$ Thus $\pmb { x } = \pmb { \alpha } _ { 1 } \pmb { x } _ { 1 }$ with $\mathfrak { x } _ { 1 } \neq 0 ,$ as required. □

Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ and let the subspace $\mathcal { S } _ { \mathfrak { d } } \subset \mathcal { S }$ be T-invariant. If $\pmb { x } \in \mathcal { S } _ { \pmb { 0 } }$ and there exists a basis in $\mathcal { S } _ { \mathfrak { d } }$ of the form

$$
\{ x , T ( x ) , \ldots , T ^ { k - 1 } ( x ) \} , \qquad k = \dim \mathcal { S } _ { 0 } ,
$$

then $\mathcal { S } _ { 0 }$ is said to be a cyclic subspace of $\mathcal { S }$ (with respect to $T$ or $T | _ { \mathcal { S } _ { \mathfrak { o } } } )$

Proposition 1. A Jordan subspace is cyclic

PROOF. Let $x _ { 1 } , x _ { 2 } , \ldots , x _ { r }$ be a Jordan chain and observe that Eqs. (3) imply

$$
\begin{array} { r } { \begin{array} { c } { x _ { r - 1 } = ( T - \lambda I ) x _ { r } , } \\ { \vdots } \\ { x _ { 2 } = ( T - \lambda I ) ^ { r - 2 } x _ { r } , } \\ { x _ { 1 } = ( T - \lambda I ) ^ { r - 1 } x _ { r } . } \end{array} } \end{array}\tag{5}
$$

Using the binomial theorem, it is clear that the Jordan subspace generated by $x _ { 1 } , x _ { 2 } , \ldots , x _ { r }$ is also generated by $x _ { r } , T x _ { r } , \ldots , T ^ { r ^ { - 1 } } x _ { r }$ . Since the Jordan subspace is T-invariant (Exercise 5) and $x _ { r }$ is in this subspace, it follows that the subspace is cyclic with respect to $T .$

Observe that Eqs. (5) show that if $\mathbf { \delta } _ { \mathbf { \pmb { x } _ { p } } }$ is a generalized eigenvector of order $r ,$ then $( T - \lambda I ) ^ { i } x _ { r }$ is a generalized eigenvector of order $r - i ,$ for i = 0, 1, . . . , $r - 1$

## 6.4 The Structure of Generalized Eigenspaces

In the preceding section some basic ideas on generalized eigenspaces and Jordan chains have been introduced. In this section we put them to work to prove that each generalized eigenspace $\mathscr { G } _ { i }$ of Eq. (6.2.4) has a basis made up of one or several Jordan chains.

Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ with $\mathcal F = \mathbb C$ and let $\mathcal { S } _ { p } = \mathop { \bf K e r } ( T - \lambda I ) ^ { p }$ be the generalized eigenspace of T of maximal order p associated with the eigenvalue $\lambda ,$ that is, $\mathcal { S } _ { p - 1 } \neq \mathcal { S } _ { p } = \mathcal { S } _ { p + 1 }$ . The subspace $\mathcal { S } _ { p }$ satisfying this condition is referred to as the generalized eigenspace of T associated with λ. Thus, “the generalized eigenspace" of an eigenvalue, without reference to order, implies that the order $\mathbf { i s } ,$ in fact, maximal.

Theorem 1. There exists a unique decomposition

$$
\mathcal { S } _ { p } = \sum _ { i = 1 } ^ { t _ { p } } \cdot \mathcal { J } _ { p } ^ { ( i ) } \dot { + } \sum _ { i = 1 } ^ { t _ { p - i } } \cdot \mathcal { J } _ { p - 1 } ^ { ( i ) } \dot { + } \cdots \dot { + } \sum _ { i = 1 } ^ { t _ { 1 } } \cdot \mathcal { J } _ { 1 } ^ { ( i ) } ,
$$

where $\mathcal { J } _ { j } ^ { ( i ) } \left( 1 \leq j \leq p , 1 \leq i \leq t _ { j } \right)$ is a cyclic Jordan subspace of dimension j.

In this decomposition of $\mathcal { S } _ { p } ,$ there is the possibility that $t _ { j } = 0$ when the corresponding sum on the right is interpreted as the trivial subspace $\{ \pmb { \theta } \}$

Theorem 1 implies that there exists a basis in $\mathsf { K e r } ( T - \lambda I ) ^ { p }$ consisting of Jordan chains; each chain is a basis in a cyclic Jordan subspace $\mathcal { J } _ { j } ^ { ( i ) }$ $( 1 \leq j \leq p , 1 \leq i \leq t _ { j } )$ . Namely, starting with $j = p ,$ we have the basis

$$
\begin{array} { l l l l l } { x _ { 1 } ^ { ( 1 ) } , } & { x _ { 2 } ^ { ( 2 ) } , } & { \cdots , } & { x _ { 0 } ^ { ( n _ { 2 } ) } , } & { x _ { 0 } ^ { ( n ) } , } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { x _ { 1 } ^ { ( n _ { p } ) } , } & { x _ { 2 } ^ { ( n _ { p } ) } , } & { \cdots , } & { x _ { p - \cdot } ^ { ( n _ { p } ) } , } & { x _ { p } ^ { ( n _ { p } ) } , } \\ { x _ { 1 } ^ { ( t _ { p } + 1 ) } , } & { x _ { 2 } ^ { ( t _ { p } + 1 ) } , } & { \cdots , } & { x _ { p - \cdot } ^ { ( t _ { p } + 1 ) } , } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { x _ { 1 } ^ { ( t _ { p } + t _ { p - 1 } ) } , } & { x _ { 2 } ^ { ( t _ { p } + t _ { p - 1 } ) } , } & { \cdots , } & { x _ { p - 1 } ^ { ( t _ { p } + t _ { p - 1 } ) } , } \\ { \vdots } & { \vdots } & \\ { x _ { 1 } ^ { ( t _ { - 1 } + 1 ) } , } & { } & { } & { } & { } \\ { \vdots } & { } & { } & { } & { } \\ { x _ { 2 } ^ { ( t ) } } & { } & { } & { } & { } \end{array}\tag{1}
$$

where $\begin{array} { r } { t = \sum _ { j = 1 } ^ { p } t _ { j } } \end{array}$ and the elements of each row form a Jordan chain of maximal possible length. Also, the elements of column r in (1) are generalized eigenvectors of T of order r associated with λ. The basis (1) of $\mathrm { K e r } ( T - \lambda I ) ^ { p }$ is called a Jordan basis of the generalized eigenspace.

PRooF. Bearing in mind the relationships (6.3.1), let $\mathbf { \Delta } \mathbf { x } _ { p } ^ { ( 1 ) } , \mathbf { \Delta } \mathbf { x } _ { p } ^ { ( 2 ) } , \ldots , \mathbf { \Delta } \mathbf { x } _ { p } ^ { ( t _ { p } ) }$ denote linearly independent elements in $\mathcal { S } _ { p }$ such that

$$
\mathcal { S } _ { p - 1 } \dot { + } \operatorname { s p a n } \{ \mathbf { x } _ { p } ^ { ( 1 ) } , \mathbf { x } _ { p } ^ { ( 2 ) } , \dots , \mathbf { x } _ { p } ^ { ( t _ { p } ) } \} = \mathcal { S } _ { p } .\tag{2}
$$

Obviously, the vectors $\boldsymbol { x } _ { p } ^ { ( 1 ) } , \ldots , \boldsymbol { x } _ { p } ^ { ( t _ { p } ) }$ in Eq. (2) are generalized eigenvectors of $T$ of order $p .$ It is claimed that the ${ \pmb { p } } t _ { p }$ vectors of the form

$$
( T - \lambda I ) ^ { k } ( \pmb { x } _ { p } ^ { ( 1 ) } ) , ~ ( T - \lambda I ) ^ { k } ( \pmb { x } _ { p } ^ { ( 2 ) } ) , ~ \dots , ~ ( T - \lambda I ) ^ { k } ( \pmb { x } _ { p } ^ { ( t _ { p } ) } ) ,\tag{3}
$$

$k = 0 , 1 , \ldots , p - 1$ , are linearly independent. Indeed, if

$$
\sum _ { k = 0 } ^ { p - 1 } \sum _ { i = 1 } ^ { t _ { p } } \alpha _ { i k } ( T - \lambda I ) ^ { k } ( x _ { p } ^ { ( i ) } ) = \theta ,\tag{4}
$$

then, applying the transformation $( T - \lambda I ) ^ { p - 1 }$ , we deduce by use of Exercise 6.3.3 that

$$
( T - \lambda I ) ^ { p - 1 } \biggl ( \sum _ { i = 1 } ^ { t _ { p } } \alpha _ { i 0 } x _ { p } ^ { ( i ) } \biggr ) = \pmb { 0 } .
$$

Hence $\sum _ { i = 1 } ^ { t _ { p } } \alpha _ { i 0 } x _ { p } ^ { ( i ) } \in \mathcal { S } _ { p - 1 }$ and, recalling the choice of $\{ \boldsymbol { x } _ { p } ^ { ( i ) } \} _ { i = 1 } ^ { t p }$ in Eq. (2), we obtain $\begin{array} { r } { \sum _ { i = 1 } ^ { t p } \alpha _ { i 0 } x _ { p } ^ { ( i ) } = \pmb { \mathscr { 0 } } . } \end{array}$ Consequently, $\alpha _ { i 0 } = 0 ~ ( i = \dot { 1 } , 2 , \ldots , t _ { p } ) .$ Now applying the transformation $( T - \lambda I ) ^ { p - 2 }$ to Eq. (4), it is shown similarly that $\alpha _ { i 1 } = 0 ( i = 1 , 2 , \ldots , t _ { p } ) .$ , and so on.

Thus, the cyclic Jordan subspaces $\mathcal { J } _ { p } ^ { ( i ) } \left( i = 1 , 2 , \ldots , t _ { p } \right)$ constructed by the rule

$$
\mathcal { J } _ { p } ^ { ( i ) } = \mathrm { s p a n } \{ ( T - \lambda I ) ^ { k } ( x _ { p } ^ { ( i ) } ) \} _ { k = 0 } ^ { p - 1 } , \qquad 1 \leq i \leq t _ { p } ,
$$

satisfy the conditions dim $( \mathcal { J } _ { p } ^ { ( i ) } ) = p ( 1 \leq i \leq t _ { p } )$ and, if $i \neq j ,$ then

$$
{ \mathcal { J } } _ { p } ^ { ( i ) } \cap { \mathcal { J } } _ { p } ^ { ( j ) } = \{ \pmb { \theta } \} .
$$

Now we will show that for any fixed $k ( 0 \leq k \leq p - 1 )$

$$
\mathcal { S } _ { p - k - 1 } \cap \operatorname { s p a n } \{ ( T - \lambda I ) ^ { k } ( x _ { p } ^ { ( i ) } ) ; 1 \leq i \leq t _ { p } \} = \{ \theta \} .\tag{5}
$$

This is obvious from Eq. (2) when $k = 0$ . More generall $| \mathbf { y } ,$ suppose that $\begin{array} { r } { \sum _ { i = 1 } ^ { t _ { p } } \alpha _ { i k } ( T - \lambda I ) ^ { k } ( \boldsymbol x _ { p } ^ { ( i ) } ) \in \mathcal S _ { p - k - 1 } } \end{array}$ . Then

$$
( T - \lambda I ) ^ { p - 1 } \biggl ( \sum _ { i = 1 } ^ { t _ { p } } \alpha _ { i k } x _ { p } ^ { ( i ) } \biggr ) = \pmb { \theta }
$$

and $\sum _ { i = 1 } ^ { t _ { p } } \alpha _ { i k } x _ { p } ^ { ( i ) } \in \mathcal { S } _ { p - 1 }$ , which contradicts (2) again unless ${ \pmb { \alpha } } _ { 1 k } = { \pmb { \alpha } } _ { 2 k } = \cdots$ $= \alpha _ { t _ { p } k } = 0 .$ so that Eq. (5) follows.

Now consider the elements $\pmb { x } _ { p - 1 } ^ { ( i ) } = ( T - \lambda I ) ( \pmb { x } _ { p } ^ { ( i ) } ) , i = 1 , 2 , \ldots , t _ { p } ,$ from (3), which are generalized eigenvectors of T of order $p - 1$ (Exercise 6.3.2). It follows from above that $\pmb { x } _ { p - 1 } ^ { ( i ) }$ are linearly independent and that, by Eq. (5),

$$
\begin{array} { r } { \mathcal { S } _ { p ^ { - } 2 } \cap \mathrm { s p a n } \{ \pmb { x } _ { p ^ { - } 1 } ^ { ( 1 ) } , \pmb { x } _ { p ^ { - } 1 } ^ { ( 2 ) } , \dots , \pmb { x } _ { p ^ { - } 1 } ^ { ( t _ { p } ) } \} = \{ \pmb { \theta } \} . } \end{array}
$$

Hence there is a set of linearly independent elements $\{ \boldsymbol { x } _ { p - 1 } ^ { ( i ) } \} _ { i = 1 } ^ { t _ { p } + t _ { p - 1 } }$ in $\mathcal { S } _ { p ^ { - } }$ 1 such that

$$
\mathcal S _ { p - 2 } + \mathrm { s p a n } \{ \boldsymbol { x } _ { p - 1 } ^ { ( i ) } \} _ { i = 1 } ^ { t _ { p } + t _ { p } - 1 } = \mathcal S _ { p - 1 } .\tag{6}
$$

Applying the previous argument to Eq. (6) as we did with Eq. (2), we obtain a system of elements of the form (3), where $\pmb { p }$ is replaced by $p - 1$ , and having similar properties. It remains to denote

$$
\mathcal { J } _ { p - 1 } ^ { ( i ) } = \mathrm { s p a n } \{ ( T - \lambda I ) ^ { k } ( x _ { p - 1 } ^ { ( i + t _ { p } ) } ) \} _ { k = 0 } ^ { p - 2 } , \qquad 1 \leq i \leq t _ { p - 1 } ,
$$

to obtain cyclic Jordan subspaces of dimension $p - 1$

Continuing this process, we eventually arrive at the relationship

$$
\mathcal { S } _ { 1 } + \mathrm { s p a n } \{ \boldsymbol { x } _ { 2 } ^ { ( i ) } \} _ { i = 1 } ^ { t _ { p } + t _ { p } - 1 } \cdots + t _ { 2 } = \mathcal { S } _ { 2 } ,\tag{7}
$$

where the vectors $\pmb { x } _ { 2 } ^ { ( i ) } ,$ with $i = 1 , 2 , \ldots , \sum _ { j = 2 } ^ { p } t _ { j }$ , denote linearly independent generalized eigenvectors of T of order 2. As before, it can be shown that the elements $\pmb { x } _ { 1 } ^ { ( i ) } = ( T - \lambda I ) ^ { ( k ) } \pmb { x } _ { 2 } ^ { ( i ) } ( k = 0 , 1 )$ are linearly independent members of $\mathcal { S } _ { 1 }$ and, together with a few other linearly independent elements from $\mathcal { S } _ { 1 }$ , form a basis $\begin{array} { r } { \{ \boldsymbol { x } _ { 1 } ^ { ( i ) } \} _ { i = 1 } ^ { t } \left( t = \sum _ { j = 1 } ^ { p } t _ { p } \right) } \end{array}$ in $\mathcal { S } _ { 1 } . \mathrm { F o r } i = 1 , 2 , . . . , t ,$ we write

$$
{ \mathcal { J } } _ { 1 } ^ { ( i ) } = { \mathrm { s p a n } } \{ x _ { 1 } ^ { ( t _ { p } + \cdots + t _ { 2 } + i ) } \} , \qquad 1 \leq i \leq t _ { 1 } .
$$

The system of elements built up above constitute a basis in S. Indeed $\mathcal { S } _ { p }$ $\{ \boldsymbol { x } _ { 1 } ^ { ( i ) } \} _ { i = 1 } ^ { t } \left( t = \sum _ { j = 1 } ^ { p } t _ { j } \right)$ is a basis in $\mathcal { S } _ { 1 }$ , while Eq. (7) shows that the union of $\{ \pmb { x } _ { 1 } ^ { ( i ) } \} _ { i = 1 } ^ { t }$ and $\overline { { \{ \boldsymbol { x } } _ { 2 } ^ { ( i ) } \} } _ { i = 1 } ^ { t _ { p } + t _ { p } } - 1 + \dots + t _ { 2 }$ generates a basis in $\mathcal { S } _ { 2 }$ , and so on. Note also (see Eqs. (2), (6), and (7)) that for $r = p , p - 1 , \ldots , 1$

$$
t _ { p } + t _ { p - 1 } + \dots + t _ { r } = \dim \mathcal { S } _ { r } - \dim \mathcal { S } _ { r - 1 } ,\tag{8}
$$

and therefore the numbers $t _ { j } ( 1 \leq j \leq p )$ are uniquely defined by T and λ.   
The proof is complete.

Exercise 1. Find a Jordan basis in $\mathcal { F } ^ { 2 }$ associated with the transformation T discussed in Exercises 4.7.7 and 4.9.5.

SoLUTioN. The transformation T has only one eigenvector, $\mathbf { x } _ { 1 } = [ 1 \quad 0 ] ^ { \mathbf { T } }$ corresponding to the eigenvalue $\lambda = 1$ . Hence there is a generalized eigenvector $\mathbf { { \boldsymbol { x } } } _ { 2 }$ such that span $\{ x _ { 1 } , x _ { 2 } \} = \mathcal { F } ^ { 2 }$ . Indeed, writing $\mathbf { \pmb { x } } _ { 2 } = [ { \pmb { \alpha } } \quad \beta ] ^ { \bar { \mathbf { T } } }$ , it follows from $T ( \pmb { x } _ { 2 } ) = \pmb { x } _ { 2 } + \pmb { x } _ { 1 }$ that

$$
 \begin{array} { r } { { \left[ { \alpha } + { \beta } {  } } \\ { \right]\beta } \end{array} } = { \left[ { \begin{array} { l } { \alpha } \\ { \beta } \end{array} } \right] } + { \left[ { \begin{array} { l } { 1 } \\ { 0 } \end{array} } \right] } ,
$$

and consequently $\beta = 1$ . Thus, any vector $[ { \mathfrak { a } } \quad 1 ] ^ { \mathbf { r } } \left( { \mathfrak { a } } \in { \mathcal { F } } \right)$ is a generalized eigenvector of T and a required Jordan basis is, for instance, $\{ \boldsymbol { \mathrm { L } } \ \textbf { 0 } \} ^ { \boldsymbol { \mathbf { r } } }$ $[ 0 \quad 1 ] ^ { \boldsymbol { \mathsf { T } } } \}$

Exercise 2. Check that the number km of Jordan chains in (1) of order m is $k _ { m }$

$$
k _ { m } = 2 l _ { m } - l _ { m - 1 } - l _ { m + 1 }
$$

where $l _ { s } = \dim ( \operatorname { K e r } ( T - \lambda I ) ^ { s } )$

Hint. Use Eq. (8).

Exercise 3. Let the subspace $\mathcal { G } _ { i } = \mathrm { K e r } ( T - \lambda _ { i } I ) ^ { m _ { i } }$ be defined as in Theorem 6.2.3. Show that for $i = 1 , 2 , \dots , s ,$

$$
\mathbf { K e r } ( T - \lambda _ { i } I ) ^ { m _ { i } - 1 } \subset \mathbf { K e r } ( T - \lambda _ { i } I ) ^ { m _ { i } } = \mathbf { K e r } ( T - \lambda _ { i } I ) ^ { m _ { i } + r }\tag{9}
$$

for any positive integer $r ,$ and the inclusion is strict.

In other words, for $\lambda = \lambda _ { i }$ , the number p of Theorem 1 coincides with $m _ { i }$ and the generalized eigenspace of T associated with the eigenvalue $\lambda _ { i }$ is just

$$
{ \mathrm { K e r } } ( T - \lambda _ { i } I ) ^ { m _ { i } } ,
$$

where $m _ { i }$ is the index of $\lambda _ { i } , 1 \leq i \leq s .$

SOLUTION. Let $p _ { j } ( \lambda ) = ( \lambda - \lambda _ { j } ) ^ { m _ { j } }$ so that, as in Eq. (6.2.2),

$$
m ( \lambda ) = p _ { 1 } ( \lambda ) p _ { 2 } ( \lambda ) \cdot \cdot \cdot p _ { s } ( \lambda )
$$

is the minimal polynomial for T and, by Theorem 6.1.4,

$$
\mathcal { S } = \sum _ { j = 1 } ^ { s } \cdot \operatorname { K e r } p _ { j } ( T ) .\tag{10}
$$

Now define $\hat { p } _ { i } ( \lambda ) = ( \lambda - \lambda _ { i } ) ^ { r } p _ { i } ( \lambda )$ and $\hat { p } _ { j } ( \lambda ) = p _ { j } ( \lambda )$ if $j \neq i .$ Then by Corollary 2 of Theorem 6.2.1 the polynomial

$$
\hat { m } ( \lambda ) = \hat { p } _ { 1 } ( \lambda ) \hat { p } _ { 2 } ( \lambda ) \cdot \cdot \cdot \hat { p } _ { s } ( \lambda )
$$

annihilates T and Theorem 6.1.4 applies once more to give

$$
\mathcal { S } = \sum _ { j = 1 } ^ { s } \cdot \operatorname { K e r } \hat { p } _ { j } ( T )
$$

Comparing with (10) it is clear that Ker $p _ { i } ( T ) = { \bf K }$ er ${ \hat { p } } _ { i } ( T )$ , as required.

Clearly $\mathrm { K e r } ( T - \lambda _ { i } I ) ^ { m _ { i } - 1 } \subset \mathrm { K e r } p _ { i } ( T )$ and if equality obtains then the polynomial $q ( \lambda ) \triangleq m ( \lambda ) ( \lambda - \lambda _ { i } ) ^ { - 1 }$ annihilates T. This is because

$$
\underset { . } { \mathbf { K e r } } q ( T ) = \sum _ { j = 1 } ^ { s } \cdot \mathbf { K e r } p _ { j } ( T ) = \mathcal { S } ,
$$

which implies $q ( T ) = 0$ But this contradicts the fact that $m ( \lambda )$ is the minimal polynomial for T. So the inclusion in (9) must be strict.

Recalling the result of Exercise 6.3.5, Theorem 1 allows us to develop the result of Theorem 6.2.3 further with the following statement.

Theorem 2. Using notation of Theorem 6.2.3 and defining $T _ { i } = \left. T \right| _ { \mathcal { G } _ { i } }$

$$
T _ { i } = \sum _ { j = 1 } ^ { t ^ { ( i ) } } \cdot T _ { i } ^ { ( j ) } , \qquad 1 \le i \le s ,\tag{11}
$$

where $t ^ { ( i ) } = \mathrm { d i m } ( \mathrm { K e r } ( T - \lambda _ { i } I ) )$ and the transformations $T _ { i } ^ { ( j ) } ( 1 \leq i \leq s ,$ $j = 1 , 2 , \dots , t ^ { ( i ) } )$ act in cyclic Jordan subspaces

The decomposition (6.2.3) together with Eq. (11) is said to be the Jordan decomposition of the transformation $T .$

## 6.5 The Jordan Theorem

Consider a linear transformation T acting in a finite-dimensional space $\mathcal { S }$ In view of Corollary 1 to Theorem 6.2.4, the problem of finding the canonical representation of $T$ is reduced to that for a transformation $T _ { i }$ $( 1 \leq i \leq s )$ acting in the typical generalized eigenspace $\mathsf { K e r } ( T - \lambda _ { i } I ) ^ { m _ { i } }$ $( m _ { i }$ being the index of $\lambda _ { i } )$ . Then Theorem 6.4.2 states that, for this purpose, it suffices to find a simple representation of the transformations $T _ { i } ^ { ( j ) } ( 1 \leq j \leq t ^ { ( i ) } )$ acting on cyclic Jordan subspaces.

Let $\mathcal { J }$ denote a cyclic Jordan subspace for T spanned by

$$
( T - \lambda _ { i } I ) ^ { r - 1 } ( { \pmb x } ) , \ldots , ( T - \lambda _ { i } I ) ( { \pmb x } ) , { \pmb x } ,\tag{1}
$$

where $\lambda _ { i } \in \sigma ( T )$ and x is a generalized eigenvector of T of order r associated with $\lambda _ { i }$ . Denote $\pmb { x } _ { i } = ( T - \lambda _ { i } I ) ^ { r - j } ( \pmb { x } ) ~ ( j = 1 , 2 , \dots , r )$ and observe [see Exercise 6.3.2 and Eqs. (6.3.3)] that $T ( { \pmb x } _ { 1 } ) = \lambda _ { i } { \pmb x } _ { 1 }$ and

$$
T ( \pmb { x } _ { j } ) = \lambda _ { i } \pmb { x } _ { j } + \pmb { x } _ { j - 1 } , \qquad j = 2 , 3 , \ldots , r .\tag{2}
$$

Hence, comparing Eq. (2) with the definition of the representation $J _ { i } = [ \alpha _ { i j } ] _ { i , j = 1 } ^ { r } \in \mathbb { C } ^ { r \times r }$ of $T | _ { \mathcal { J } }$ with respect to the basis (1), that is

$$
T ( \boldsymbol { x } _ { j } ) = \sum _ { i = 1 } ^ { r } \alpha _ { i j } \boldsymbol { x } _ { i } , \qquad j = 1 , 2 , \ldots , r ,
$$

we obtain

$$
J _ { i } = { \left[ \begin{array} { l l l l l } { \lambda _ { i } } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \lambda _ { i } } & { 1 } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \ldots } & { 0 } & { \lambda _ { i } } \end{array} \right] } ,\tag{3}
$$

where all superdiagonal elements are ones and all unmarked elements are zeros. The matrix in (3) is referred to as a Jordan block (or cell) of order r

corresponding to the eigenvalue $\lambda _ { i }$ . Thus, the Jordan block (3) is the representation of $T | _ { \mathcal { J } }$ with respect to the basis (1), which is a Jordan chain generating ${ \mathcal { J } } .$

Exercise 1. Show that the Jordan block in (3) cannot be similar to a blockdiagonal matrix diag $A _ { 1 } , A _ { 2 } , \ldots , A _ { k } ]$ , where $k \geq 2$

SoLUTION. If, for some nonsingular $P \in \mathbb { C } ^ { r \times r }$

$$
J = P \mathrm { d i a g } [ A _ { 1 } , A _ { 2 } ] P ^ { - 1 } ,
$$

then the dimension of the eigenspace for J is greater than or equal to 2 (one for each diagonal block). This contradicts the result of Exercise 6.3.6.

Thus, a Jordan block cannot be “decomposed" into smaller blocks by any similarity transformation.

Let $T \in { \mathcal { L } } ( { \mathcal { S } } )$ with ${ \mathcal { F } } = \mathbb { C } .$ and write $\boldsymbol { \sigma } ( T ) = \{ \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { s } \}$ . By Theorem 6.2.3, $\begin{array} { r } { T = \sum _ { i = 1 } ^ { s } T _ { i } } \end{array}$ , where $T _ { i } = \left. T \right. _ { \pmb { \mathscr { s } } _ { i } }$ and $\pmb { \mathscr { G } } _ { i } = \mathbf { K e r } ( T - \lambda _ { i } I ) ^ { m _ { i } } ( 1 \leq i \leq s )$ Choosing in each $\mathscr { G } _ { i }$ a Jordan basis of the form (6.4.1), we obtain a Jordan basis for the whole space $\mathcal { S }$ as a union of Jordan bases; one for each generalized eigenspace. This is described as a T-Jordan basis for $\mathcal { S }$ We now appeal to Theorem 6.4.1.

Theorem 1. In the notation of the preceding paragraph, the representation of T with respect to a T-Jordan basis is the matrix

$$
J = \mathrm { d i a g } [ J ( \lambda _ { 1 } ) , J ( \lambda _ { 2 } ) , \ldots , J ( \lambda _ { s } ) ] ,\tag{4}
$$

where for $1 \leq i \leq s ,$

$$
J ( \lambda _ { i } ) = \mathrm { d i a g } [ J _ { p } ^ { ( i ) } , \ldots , J _ { p } ^ { ( i ) } , J _ { p - 1 } ^ { ( i ) } , \ldots , J _ { p - 1 } ^ { ( i ) } , \ldots , J _ { 1 } ^ { ( i ) } , \ldots , J _ { 1 } ^ { ( i ) } , \ldots , J _ { 1 } ^ { ( i ) } ] ,\tag{5}
$$

in which the $j \times j$ matrix $J _ { j } ^ { ( i ) }$ of the form (3) appears $t _ { j } ^ { ( i ) }$ times in Eq. (5). The numbers $t _ { j } ^ { ( i ) } \left( i = 1 , 2 , \ldots , \bar { s } ; j = 1 , 2 , \ldots , p \right)$ are uniquely determined by the transformation T.

It is possible that $t _ { j } ^ { ( i ) } = 0$ for some $j < m _ { i }$ , in which case no blocks of size j appear in Eq. (5).

Note that the decomposition of J in Eqs. (4) and (5) is the best possible in the sense of Exercise 1. The representation J in Eqs. (4) and (5) is called a Jordan matrix (or Jordan canonical form)† of the transformation T. We now apply Corollary 2 of Theorem 6.2.4 to obtain the following.

Corollary 1. Any complex square matrix A is similar to a Jordan matrix that is uniquely determined by A up to the order of the matrices $J ( \lambda _ { i } )$ in Eq. (4) and the Jordan blocks in Eq. (5)

† Jordan, C., Traité des substitutions et des équations algébriques, Paris, 1870 (p. 125).

Example 2. Consider the matrix

$$
A = { \left[ \begin{array} { l l l } { 6 } & { 2 } & { 2 } \\ { - 2 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 2 } \end{array} \right] } .
$$

Since det $( A - \lambda I ) = ( 2 - \lambda ) ( \lambda - 4 ) ^ { 2 }$ , it follows that $\sigma ( A ) = \{ 2 , 4 \}$ . It is easily seen that the matrix A has one (linearly independent) eigenvector, say $\mathbf { x } _ { 1 } = [ 0 \ - 1 \ \mathrm { ~  ~ 1 ~ } ] ^ { \mathtt { T } }$ , corresponding to the eigenvalue $\lambda _ { 1 } = 2$ and one (linearly independent) eigenvector, say $\mathbf { x } _ { 2 } = [ 2 { \mathbf { \Gamma } } - 2 { \mathbf { \Gamma } } 0 ] ^ { \mathbf { T } }$ , associated with $\lambda _ { 2 } = 4 .$ From the equation $( A - 4 I ) \pmb { x } _ { 3 } = \pmb { x } _ { 2 }$ it is found that $\mathbf { x } _ { 3 } = [ 1 0 0 ] ^ { \mathrm { { T } } }$ is a generalized eigenvector of A of order 2 associated with $\lambda _ { 2 } = 4 .$ Hence a Jordan basis for A is $\{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \pmb { x } _ { 3 } \}$ and the matrix

$$
P = [ { \pmb x } _ { 1 } \quad { \pmb x } _ { 2 } \quad { \pmb x } _ { 3 } ] = \left[ \begin{array} { r r r } { 0 } & { 2 } & { 1 } \\ { - 1 } & { - 2 } & { 0 } \\ { 1 } & { 0 } & { 0 } \end{array} \right]
$$

transforms A into the Jordan form:

$$
A = P \left[ { \begin{array} { l l l } { 2 } & { 0 } & { 0 } \\ { 0 } & { 4 } & { 1 } \\ { 0 } & { 0 } & { 4 } \end{array} } \right] P ^ { - 1 } . \quad \bigsqcup
$$

The problem of determining the parameters of the Jordan matrix for a given $\ b { A } \in \mathbb { C } ^ { n \times n }$ without constructing the Jordan basis is considered in the next section. We emphasize again that, in discussing the Jordan form of a matrix $A \in { \mathcal { F } } ^ { n \times n }$ , the field $\mathcal { F }$ is assumed to be algebraically closed. Hence $n \times n$ real matrices should be considered as members of $\mathbb { C } ^ { n \times n }$ in order to guarantee the existence of the Jordan form presented here.

Exercise 3. Let $A \in \mathbb { C } ^ { n \times n }$ and define a set of Jordan vectors for A to be a set of linearly independent vectors in $\mathbb { C } ^ { n }$ made up of a union of Jordan chains for A. Show that a subspace $\mathcal { S } _ { 0 } \subset \mathbb { C } ^ { n }$ is A-invariant if and only if $\mathcal { S } _ { 0 }$ has a basis consisting of a set of Jordan vectors. (In other words, every A-invariant subspace is a direct sum of subspaces that are cyclic with respect to A.)

Hints. Given that $\mathcal { S } _ { \mathfrak { d } }$ has a set of Jordan vectors as a basis, use Exercise 6.3.5 to show that $\mathcal { S } _ { 0 }$ is T-invariant. For the converse, let $X = [ \pmb { x } _ { 1 } \quad \pmb { x } _ { 2 } \quad \cdots \quad \pmb { x } _ { r } ]$ be an n × r matrix whose columns form an arbitrary basis for $\mathcal { S } _ { 0 }$ . Observe that $A X = X G$ for some $G \in \mathbb { C } ^ { r \times r }$ . Write $G = S J S ^ { - 1 }$ where J is a Jordan matrix, and examine the columns of the matrix XS.

The following exercise shows that there are, in general, many similarities which will reduce a given matrix to a fixed Jordan normal form and also shows how they are related to one another.

Exercise 4. Show that if $A = S J S ^ { - 1 }$ and $A = T J T ^ { - 1 }$ , then $T = S U$ for some nonsingular U commuting with J.

Conversely, if U is nonsingular and commutes with J, $A = S J S ^ { - 1 }$ , and if we define $T = S U$ , then $\overset { } { A } \overset { = } \underset { } { T } J T ^ { - 1 }$ □

## 6.6 Parameters of a Jordan Matrix

Let $A \in \mathbb { C } ^ { n \times n }$ and let J, given by Eqs. (6.5.4) and (6.5.5) be a Jordan canonical form of A, that is, $\bar { A } = P J \bar { P } ^ { - 1 }$ for some invertible P. In this section we shall indicate some relations between the multiplicities of an eigenvalue and the parameters of the corresponding submatrices $J ( \lambda _ { i } )$ of J.

Proposition 1. The dimension of the generalized eigenspace of $\ b { A } \in \mathbb { C } ^ { n \times n }$ associated with the eigenvalue $\lambda _ { i } \in \sigma ( A )$ [that is, the order of the matrix $J ( \lambda _ { i } )$ in $E q$ (6.5.4)] is equal to the algebraic multiplicity of $\lambda _ { i }$

PROOF. Let $A = P J P ^ { - 1 }$ , where J is given by Eq. (6.5.4). The characteristic polynomials of A and J coincide (Section 4.11) and hence

$$
c ( \lambda ) = { \operatorname * { d e t } ( \lambda I - J ) } = \prod _ { i = 1 } ^ { s } { \operatorname * { d e t } ( \lambda I - J ( \lambda _ { i } ) ) } .
$$

In view of Eqs. (6.5.5) and (6.5.3),

$$
c ( \lambda ) = \prod _ { i = 1 } ^ { s } ( \lambda - \lambda _ { i } ) ^ { q _ { i } } ,\tag{1}
$$

where $q _ { i }$ is the order of $J ( \lambda _ { i } ) \left( 1 \leq i \leq s \right)$ . In remains to recall that $q _ { i }$ in Eq. (1) is, by definition, the algebraic multiplicity of $\lambda _ { i }$ . ■

Note that the number of Jordan blocks in $J ( \lambda _ { i } )$ is equal to the number of rows in (6.4.1), that is, to the geometric multiplicity of the eigenvalue $\lambda _ { i }$ so that it readily follows from (6.4.1) and Proposition 1 that the geometric multiplicity of an eigenvalue does not exceed its algebraic multiplicity (the total number of elements in (6.4.1)). However, these two characteristics uniquely determine the Jordan submatrix $J ( \lambda _ { i } )$ associated with $\lambda _ { i }$ only in the cases considered next.

Proposition 2. The matrix A is simple if and only if the geometric multiplicity of each of its eigenvalues is equal to the algebraic multiplicity. Equivalently, A is simple if and only if the minimal polynomial of A has only simple zeros.

PRooF. A matrix is simple if and only if it is similar to a diagonal matrix (see Theorem 4.8.2'). Hence, in view of Exercise 6.5.1 and Theorem 6.5.1, the corresponding Jordan matrix must be diagonal and therefore consists of $1 \times 1$ Jordan blocks. Thus, recalling Proposition 1 and the foregoing discussion, the multiplicities of the matrix coincide. Proceeding to the second statement, we note that the multiplicity of an eigenvalue as a zero of the minimal polynomial (the index) is equal to the maximal order of Jordan blocks associated with the eigenvalue (remember the meaning of p in (6.4.1). This observation completes the proof.

Note that in this case the matrix has no proper generalized eigenvectors.

Exercise 1. Show that if the geometric multiplicity of an eigenvalue $\lambda _ { i }$ is equal to one, then the Jordan matrix has only one Jordan block associated with $\lambda _ { i }$ . The order of this block is equal to the algebraic multiplicity of the eigenvalue. □

When Exercise 1 holds for all the eigenvalues, the minimal and the characteristic polynomials coincide. The converse is also true.

Exercise 2. Check that the minimal and the characteristic polynomials of a matrix coincide if and only if its Jordan matrix has only one Jordan block associated with each distinct eigenvalue of the matrix.

Hint. See the proof of Proposition 2. □

A matrix $\pmb { A } \in \mathcal { F } ^ { { n } \times { n } }$ is said to be nonderogatory if its characteristic and minimal polynomials coincide; otherwise it is derogatory. Thus, Exercise 2 reveals the structure of nonderogatory matrices.

Exercise 3. Check that a companion matrix is nonderogatory.

Exercise 4. Find a Jordan matrix J of the matrix A having the characteristic polynomial $c ( \lambda ) = ( \lambda - 1 ) ^ { 3 } ( \lambda - 2 ) ^ { 4 }$ if the geometric multiplicities are also known: dim(Ker(A − I)) = 2 and $\mathrm { d i m } ( \mathrm { K e r } ( A - 2 I ) ) = 3$

SoLUTioN. Consider Jordan blocks of A associated with $\lambda _ { 1 } = 1$ The geometric multiplicity 2 means that there are two blocks associated with this eigenvalue, while the algebraic multiplicity 3 implies that one of the blocks must be of order 2. Reasoning in a similar way for the second eigenvalue, we obtain

$$
J = \mathrm { d i a g } \left[ { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } , \quad { \lbrack 1 \rbrack } , \begin{array} { l } { { \left[ { 2 } \right]} & { 1 } \\ { 0 } & { 2 } \end{array}  } , \begin{array} { l l } { { \lbrack 2 \rbrack , } } & { { \lbrack 2 \rbrack } } \end{array} \right] . \quad { \mit \sqcup } \quad
$$

In cases different from those discussed above, the orders of the Jordan blocks are usually found by use of Eq. (6.4.8) and Exercise 6.4.2, which require the determination of dim(Ker(A — λI)) for certain positive integers s.

Exercise 5. Determine the Jordan form of the matrix

$$
A = \left[ { \begin{array} { r r r r } { 2 } & { 0 } & { 0 } & { 0 } \\ { - 3 } & { 2 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 2 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 2 } \end{array} } \right] .
$$

SoLUTioN. Obviously, the characteristic polynomial is $c ( \lambda ) = ( \lambda - 2 ) ^ { 4 }$ and $\dim ( \operatorname { K e r } ( A - 2 I ) ) = 2 .$ Hence the Jordan form consists of two blocks. To determine their orders (2 and 2, or 3 and 1), we calculate that $( A - 2 I ) ^ { 2 }$ $= O$ and, therefore, the number $k _ { 2 }$ in Exercise 6.4.2 is equal to 2. Hence $k _ { 2 } = 2 l _ { 2 } - l _ { 1 } - l _ { 3 } = 8 - 2 - 4 = 2$ , and consequently there are two blocks of order 2:

$$
J = \mathrm { d i a g } \left[ { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 0 } & { 2 } \end{array} \right] } , { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 0 } & { 2 } \end{array} \right] } \right] . \quad \bigsqcup
$$

There is a concept that summarizes the parameters of the Jordan form. Let $A \in \mathbb { C } ^ { n \times n }$ and let $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ denote all its distinct eigenvalues of geometric multiplicities $p _ { 1 } , p _ { 2 } , \ldots , p _ { s }$ , respectively. Thus, there are $p _ { j }$ Jordan blocks in the Jordan form J of A associated with the eigenvalue $\lambda _ { j }$ $( 1 \leq j \leq s )$ . Denote by $\delta _ { j } ^ { ( 1 ) } \geq \delta _ { j } ^ { ( 2 ) } \geq \cdot \cdot \cdot \geq \delta _ { j } ^ { ( p _ { j } ) }$ the orders of these blocks and write

$$
\{ ( \delta _ { 1 } ^ { ( 1 ) } , \delta _ { 1 } ^ { ( 2 ) } , \ldots , \delta _ { 1 } ^ { ( p _ { 1 } ) } ) , ( \delta _ { 2 } ^ { ( 1 ) } , \delta _ { 2 } ^ { ( 2 ) } , \ldots , \delta _ { 2 } ^ { ( p _ { 2 } ) } ) , \ldots , ( \delta _ { s } ^ { ( 1 ) } , \delta _ { s } ^ { ( 2 ) } , \ldots , \delta _ { s } ^ { ( p _ { s } ) } ) \} .\tag{2}
$$

The form (2) is referred to as the Segre characteristic† of the matrix A. Obviously this characteristic, along with the eigenvalues of the matrix, uniquely defines its Jordan form. Note that the numbers $q _ { j } = \delta _ { j } ^ { ( 1 ) } + \delta _ { j } ^ { ( 2 ) }$ ${ } + \cdot \cdot \cdot { } + \delta _ { j } ^ { ( p _ { j } ) } , j = 1 , 2 , . . . , s ,$ are the algebraic multiplicities of the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ , respectively.

Exercise 6. Verify that the Segre characteristic of the matrices discussed in Exercises 4 and 5 are, respectively,

$$
\{ ( 2 , 1 ) , ( 2 , 1 , 1 ) \} \qquad \mathrm { a n d } \qquad \{ ( 2 ) , ( 2 ) \} .
$$

†Segre, C., Atti Accad. naz. Lincei, Mem. III, 19 (1884), 127–148.

## 6.7 The Real Jordan Form

Let $A \in \mathbb { R } ^ { n \times n }$ . If A is viewed as a complex matrix, then it follows from Theorem 6.5.1 that $A$ is similar to a Jordan matrix as defined in Eqs. (6.5.4) and (6.5.5). However, this Jordan matrix $J ,$ and the matrix P for which $P ^ { - 1 } A P = J ,$ , will generally be complex. In this section we describe a normal form for A that can be achieved by confining attention to real transforming matrices P, and hence a real canonical form. To achieve this, we take advantage of the (complex) Jordan form already derived and the fundamental fact (see Section 5.9) that the eigenvalues of $A$ may be real, and if not, that they appear in complex conjugate pairs.

We shall use the construction of a (complex) Jordan basis for A from the preceding sections to obtain a real basis. The vectors of this basis will form the columns of our real transforming matrix P.

First, if λ is a real eigenvalue of $A ,$ then there is a real Jordan basis for the generalized eigenspace of $\lambda ,$ as described in (6.4.1); these vectors will form a part of our new real basis for $\mathbb { R } ^ { n } .$ If $\lambda \in \sigma ( A )$ and is not real, then neither is $\bar { \lambda } \in \sigma ( A )$ . Construct Jordan chains (necessarily non-real) to span the generalized eigenspace of $\lambda$ as in (6.4.1). Thus, each chain in this spanning set satisfies relations of the form (6.3.3) (with T replaced by $A ) .$ Taking complex conjugates in these relations, the complex conjugate vectors form chains spanning the generalized eigenspace of λ.

It will be sufficient to show how the vectors for a single chain of length $r ,$ together with those of the conjugate chain, are combined to produce the desired real basis for a 2r-dimensional real invariant subspace of $A .$ Let $\lambda$ be the eigenvalue in question and write $\lambda = \mu + i \omega ,$ where $\mu ,$ ω are real and $\omega \neq 0$ . Let P be the $n \times r$ complex matrix whose columns are the vectors $\pmb { x } _ { 1 } , \pmb { x } _ { 2 } , \ldots , \pmb { x } _ { r }$ of a Jordan chain corresponding to λ. If $J ( \lambda )$ is the $r \times r$ Jordan block with eigenvalue $\lambda ,$ then $A P = P J ( \lambda )$ and, taking conjugates, $A { \overline { { P } } } = { \overline { { P } } } J ( { \bar { \lambda } } )$ . Thus,

$$
A [ P \quad \bar { P } ] = [ P \quad \bar { P } ] \left[ \begin{array} { c c } { J ( \lambda ) } & { 0 } \\ { 0 } & { J ( \bar { \lambda } ) } \end{array} \right] ,
$$

and for any unitary matrix U of size $2 r$

$$
\begin{array} { r } { A [ P \quad \hat { P } ] U = [ P \quad \hat { P } ] U U ^ { * } \biggl [ \begin{array} { c c } { J ( \lambda ) } & { 0 } \\ { 0 } & { J ( \hat { \lambda } ) } \end{array} \biggr ] U . } \end{array}
$$

We claim that there is a unitary matrix U such that the $2 r$ columns of $Q ^ { \ \triangleq }$ ${ \begin{array} { r l } { [ P } & { { } { \bar { P } } ] U } \end{array} }$ are real and such that $J _ { r } ( \lambda , \bar { \lambda } ) \triangleq U ^ { * } \mathrm { d i a g } [ J ( \lambda ) , J ( \bar { \lambda } ) ] U$ is also real. The matrix $J _ { r } ( \lambda , \bar { \lambda } )$ then plays the same role in the real Jordan form for A that diag[J(λ), J(λ)] plays in the complex form.

We confirm our claim simply by verification. We confine attention to the case $r = 3$ ; the modifications for other values of r are obvious. Define the unitary matrix

$$
U = \frac { 1 } { \sqrt { 2 } } \left[ \begin{array} { c c c c c c } { 1 } & { - i } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - i } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - i } \\ { 1 } & { i } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { i } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { i } \end{array} \right] .
$$

Recalling that $\lambda = \mu + i \omega ,$ , it is easily verified that

$$
J _ { r } ( \lambda , \bar { \lambda } ) = U ^ { * } { \left[ \begin{array} { l l } { J ( \lambda ) } & { 0 } \\ { 0 } & { J ( \bar { \lambda } ) } \end{array} \right] } U = { \left[ \begin{array} { l l l l l l } { \mu } & { \omega } & { 1 } & { 0 } & { 0 } & { 0 } \\ { - \omega } & { \mu } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { \mu } & { \omega } & { 1 } & { 0 } \\ { 0 } & { 0 } & { - \omega } & { \mu } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \mu } & { \omega } \\ { 0 } & { 0 } & { 0 } & { 0 } & { - \omega } & { \mu } \end{array} \right] } .
$$

Furthermore, with the Cartesian decompositions $x _ { j } = y _ { j } + i z _ { j }$ for $j = 1 , 2 ,$ $\cdots , r ,$ we get

$$
Q = [ P \quad \bar { P } ] U = \sqrt { 2 } [ y _ { 1 } \ z _ { 1 } \quad y _ { 2 } \quad z _ { 2 } \quad y _ { 3 } \quad z _ { 3 } ] ,
$$

which is real and of full rank since $[ P _ { \mathrm { ~ \pm ~ } } \bar { P } ]$ has full rank and U is unitary. These vectors span a six-dimensional real invariant subspace of A associated with the non-real eigenvalue pair $\lambda , \bar { \lambda }$ (see Theorem 5.9.1). This statement is clear from the relation $A Q = Q J _ { r } ( \lambda , \bar { \lambda } )$ . Our discussion leads to the following conclusion.

Theorem 1. If $A \in \mathbb { R } ^ { n \times n }$ , there is a nonsingular matrix $\pmb { X } \in \mathbb { R } ^ { n \times n }$ such that $X ^ { - 1 } A X$ is a real block-diagonal matrix, each block of which has one of two forms:

(a) the form of (6.5.3), in which case the size of the block is equal to the lenath of a complete Jordan chain of a set (6.4.1) corresponding to a real eigenvalue;

(b) the form $J _ { r } ( \lambda , \bar { \lambda } )$ indicated above in which case the size of the block is equal to twice the length of a (complex) complete Jordan chain of a set (6.4.1) corresponding to a non-real eigenvalue $\lambda = \mu + i \omega .$

Exercise 1. Describe the real Jordan form for a matrix that is real and simple. □

## 6.8 Miscellaneous Exercises

1. Prove that two simple matrices are similar if and only if they have the same characteristic polynomial

2. Show that any square matrix is similar to its transpose.

3. Check that the Jordan canonical form of an idempotent matrix (a projector) is a diagonal matrix with zeros and ones in the diagonal positions.

4. Show that

(a) the minimal and the characteristic polynomials of a Jordan block of order r are both $( \lambda - \lambda _ { 0 } ) ^ { r }$

(b) the minimal polynomial of a Jordan matrix is the least common multiple of the minimal polynomials of the Jordan blocks.

5. Show that a Jordan block is similar to the companion matrix associated with its characteristic (or minimal) polynomial.

Hint. For a geometrical solution: Show that the representation of $T | _ { \mathcal { g } }$ with respect to the basis $\{ \pmb { x } , T ( \pmb { x } ) , \hdots , T ^ { r ^ { - 1 } } ( \pmb { x } ) \}$ for a Jordan subspace $\mathscr { J }$ is a companion matrix.

6. Prove that any matrix $A \in \mathbb { C } ^ { n \times n }$ can be represented as a sum of a simple matrix and a nilpotent matrix.

Hint. Represent an $r \times r$ Jordan block in the form $\lambda _ { i } I + N$ , where $N = [ \delta _ { j + 1 , k } ] _ { j , k = 1 } ^ { r }$ , and observe that $N ^ { r } = O$

7. Check that the matrices

$$
\left[ { \begin{array} { c c c c } { a _ { 0 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 r } } \\ { 0 } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { a _ { r - 1 , r } } \\ { 0 } & { \cdots } & { 0 } & { a _ { 0 } } \end{array} } \right] \qquad { \mathrm { a n d } } \qquad \left[ { \begin{array} { c c c c } { a _ { 0 } } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { a _ { 0 } } \end{array} } \right]
$$

are similar, provided $a _ { i , i + 1 } \neq 0 , i = 1 , 2 , \ldots , r - 1$

8. Check that for an $r \times r$ Jordan block J associated with an eigenvalue $\lambda _ { 0 }$ , and for any polynomial $p ( \lambda )$

$$
p ( J ) = \left[ \begin{array} { l l l l l } { p ( \lambda _ { 0 } ) } & { p ^ { \prime } ( \lambda _ { 0 } ) / 1 ! } & { \cdots } & { p ^ { ( r - 1 ) } ( \lambda _ { 0 } ) / ( r - 1 ) ! } \\ { 0 } & { } & { \ddots } & { \ddots } & { \vdots } \\ { \vdots } & { } & { \ddots } & { } & { p ^ { \prime } ( \lambda _ { 0 } ) / 1 ! } \\ { 0 } & { \cdots } & { } & { 0 } & { p ( \lambda _ { 0 } ) } \end{array} \right] .
$$

9. If $m ( \lambda )$ is the minimal polynomial of $\pmb { A } \in \mathbb { C } ^ { n \times n }$ and $p ( \lambda )$ is a polynomial over $\mathbb { C } ,$ prove that $p ( A )$ is nonsingular if and only if $m ( \lambda )$ and $p ( \lambda )$ are relatively prime.

10. If $\alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } \in \mathbb { R }$ and are not all zero, show that the characteristic and minimal polynomials of the matrix

$$
\left[ { \begin{array} { r r r r } { \alpha _ { 0 } } & { \alpha _ { 1 } } & { \alpha _ { 2 } } & { \alpha _ { 3 } } \\ { - \alpha _ { 1 } } & { \alpha _ { 0 } } & { - \alpha _ { 3 } } & { \alpha _ { 2 } } \\ { - \alpha _ { 2 } } & { \alpha _ { 3 } } & { \alpha _ { 0 } } & { - \alpha _ { 1 } } \\ { - \alpha _ { 3 } } & { - \alpha _ { 2 } } & { \alpha _ { 1 } } & { \alpha _ { 0 } } \end{array} } \right]
$$

are

$$
( \lambda ^ { 2 } - 2 \alpha _ { 0 } \lambda + ( \alpha _ { 0 } ^ { 2 } + \alpha _ { 1 } ^ { 2 } + \alpha _ { 2 } ^ { 2 } + \alpha _ { 3 } ^ { 2 } ) ) ^ { j }
$$

with $j = 2$ and $j = 1$ , respectively.

Hint. First reduce to the case ${ \mathfrak { X } } _ { 0 } = 0$ and show that in this case $\lambda _ { 1 } = i ( \alpha _ { 1 } ^ { 2 } + \alpha _ { 2 } ^ { 2 } + \alpha _ { 3 } ^ { 2 } ) ^ { 1 / 2 }$ is an eigenvalue with eigenvectors

$$
\left[ \begin{array} { l } { \lambda _ { 1 } } \\ { \alpha _ { 1 } } \\ { \alpha _ { 2 } } \\ { \alpha _ { 3 } } \end{array} \right] \qquad \mathrm { a n d } \qquad \left[ \begin{array} { l } { \alpha _ { 3 } } \\ { \alpha _ { 2 } } \\ { - \alpha _ { 1 } } \\ { - \lambda _ { 1 } } \end{array} \right] .
$$

11. Let $A \in \mathbb { C } ^ { n \times n }$ . Show that $A = A ^ { - 1 }$ if and only if there is an $m \leq n$ and a nonsingular S such that

$$
A = S { \binom { I _ { m } } { 0 } } \quad \quad 0 \quad \quad \quad \quad \quad
$$

Hint. Use the Jordan form for A.

# Matrix Polynomials and Normal Forms

The important theory of invariant polynomials and λ-matrices developed in this chapter allows us to obtain an independent proof of the possibility of reducing a matrix to the Jordan canonical form, as well as a method of constructing that form directly from the elements of the matrix. Also, other normal forms of a matrix are derived. This approach to the Jordan form can be viewed as an algebraic one in contrast to the geometrical approach developed in Chapter 6. It requires less mathematical abstraction than the geometrical approach and may be more accessible for some readers. In addition, the analysis of matrix polynomials is important in its own right. Direct applications to differential and difference equations are developed in this chapter, and foundations are laid for the spectral theory of matrix polynomials to be studied in Chapter 14.

## 7.1 The Notion of a Matrix Polynomial

Consider an $n \times n$ matrix $A ( \lambda )$ whose elements are polynomials in $\lambda$

$$
A ( \lambda ) = { \begin{array} { r c c c } { \left[ a _ { 1 1 } ( \lambda ) } & { a _ { 1 2 } ( \lambda ) } & { \cdots } & { a _ { 1 n } ( \lambda ) \right] } \\ { a _ { 2 1 } ( \lambda ) } & { a _ { 2 2 } ( \lambda ) } & { \cdots } & { a _ { 2 n } ( \lambda ) } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { a _ { n 1 } ( \lambda ) } & { a _ { n 2 } ( \lambda ) } & { \cdots } & { a _ { n n } ( \lambda ) } \end{array} } ,\tag{1}
$$

and suppose that λ and the coefficients of the polynomials $a _ { i j } ( \lambda )$ are from a field ${ \mathcal F } ,$ so that when the elements of $A ( \lambda )$ are evaluated for a particular value of $\lambda ,$ say $\lambda = \lambda _ { 0 }$ , then $A ( \lambda _ { 0 } ) \in \mathcal { F } ^ { n \times n }$ .The matrix $A ( \lambda )$ is known as a matrix polynomial or a lambda matrix, or a λ-matrix. Where the underlying field needs to be stressed we shall call $A ( \lambda )$ a λ-matrix over ${ \mathcal { F } } .$ Note that an example of a $\lambda - \operatorname* { m a t r i x }$ is provided by the matrix $\lambda I - A$ and that the matrices whose elements are scalars $( \mathrm { i . } \mathsf { e . } ,$ polynomials of degree zero, or just zeros) can be viewed as a particular case of λ-matrices.

A λ-matrix $A ( \lambda )$ is said to be regular if the determinant det $A ( \lambda )$ is not identically zero. Note that det $A ( \lambda )$ is itself a polynomial with coefficients in ${ \mathcal F } ,$ so $A ( \lambda )$ is not regular if and only if each coefficient of det $A ( \lambda )$ is the zero of $\mathcal { F } .$ The degree of a λ-matrix $A ( \lambda )$ is defined to be the greatest degree of the polynomials appearing as entries of $A ( \lambda )$ and is denoted by deg $A ( \lambda )$ Thus, deg( $\lambda I - A ) = 1$ and deg $A = 0$ for any nonzero $A \in { \mathcal { F } } ^ { n \times n }$

Lambda matrices of the same order may be added and multiplied together in the usual way, and in each case the result is another λ-matrix. In particular, a λ-matrix $A ( \lambda )$ is said to be invertible if there is a λ-matrix $B ( \lambda )$ such that $A ( \lambda ) B ( \lambda ) = B ( \lambda ) A ( \lambda ) = I .$ In other words, $A ( \lambda )$ is invertible if $B ( \lambda ) = [ A ( \lambda ) ] ^ { - 1 }$ exists and is also a λ-matrix.

Proposition 1. A λ-matrix $A ( \lambda )$ is invertible if and only if det $A ( \lambda )$ is a nonzero constant.

PROOF. If det $A ( \lambda ) = c \neq 0 ;$ then the entries of the inverse matrix are equal to the minors of $A ( \lambda )$ of order $n - 1$ divided by $c \neq 0$ and hence are polynomials, in λ. Thus $[ A ( \lambda ) ] ^ { - 1 }$ is a λ-matrix. Conversely, if $A ( \lambda )$ is invertible, then the equality $A ( \lambda ) B ( \lambda ) = I$ yields

$$
\operatorname* { d e t } A ( \lambda ) \operatorname* { d e t } B ( \lambda ) = 1 .
$$

Thus, the product of the polynomials det $A ( \lambda )$ and det $B ( \lambda )$ is a nonzero constant. This is possible only if they are each nonzero constants.■

A λ-matrix with a nonzero constant determinant is also referred to as a unimodular λ-matrix. This notion permits the restatement of Proposition 1: A λ-matrix is invertible if and only if it is unimodular. Note that the degree of a unimodular matrix is arbitrary.

Exercise 1. Check that the following λ-matrices are unimodular:

$$
A _ { 1 } ( \lambda ) = { \left[ \begin{array} { l l l } { 1 } & { \lambda } & { - 2 \lambda ^ { 2 } } \\ { 0 } & { 1 } & { \lambda ^ { 4 } } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } , \qquad A _ { 2 } ( \lambda ) = { \left[ \begin{array} { l l } { ( \lambda - 1 ) ^ { 2 } } & { \lambda } \\ { \lambda - 2 } & { 1 } \end{array} \right] } . \quad \boxed { 1 }
$$

Unimodular λ-matrices play an important role in reducing an arbitrary λ-matrix to a simpler form. Before going on to develop this idea in the next two sections, we wish to point out a different viewpoint on λ-matrices.

Let $A ( \lambda )$ denote an $n \times n \lambda – \mathrm { m a t r i x }$ of degree l. The (i, j)th element of $A ( \lambda )$ can be written in the form

$$
a _ { i j } ( \lambda ) = a _ { i j } ^ { ( 0 ) } + a _ { i j } ^ { ( 1 ) } \lambda + \cdots + a _ { i j } ^ { ( l ) } \lambda ^ { l } ,
$$

and there is at least one element for which $a _ { i j } ^ { ( l ) } \neq 0 ( 1 \leq i , j \leq n )$ . If we let $A _ { r }$ be the matrix whose i, jth element is $a _ { i j } ^ { ( r ) } ( r \dot { = } 0 , 1 , \dots , l$ for each $i , j )$ , then we have $A _ { l } \neq O$ and

$$
A ( \lambda ) = A _ { 0 } + \lambda A _ { 1 } + \cdots + \lambda ^ { l - 1 } A _ { l - 1 } + \lambda ^ { l } A _ { l } .
$$

This formulation motivates the term “matrix polynomial" as an alternative for “λ-matrix."

Exercise 2. Check that

$$
\begin{array} { r } { \left[ \lambda ^ { 2 } + \lambda + 1 \lambda ^ { 2 } - \lambda + 2 \atop 2 \lambda \lambda \right]} \lambda ^ { 2 } - 3 \lambda - 1  = \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 0 } & { - 1 } \end{array} \right] + \lambda \left[ \begin{array} { l l } { 1 } & { - 1 } \\ { 2 } & { - 3 } \end{array} \right] + \lambda ^ { 2 } \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] . \bigsqcup \lambda  \end{array}
$$

The description of λ-matrices as matrix polynomials suggests problems concerning divisibility, the solution of polynomial equations, and other generalizations of the theory of scalar polynomials. Of course, the lack of commutativity of the coefficients of matrix polynomials causes some difficulties and modifications in this program. However, an important and useful theory of matrix polynomials has recently been developed, and an introduction to this theory is presented in Chapter 14.

In the next section we present some fundamental facts about divisibility of matrix polynomials needed for use in this and subsequent chapters.

## 7.2 Division of Matrix Polynomials

Let $\begin{array} { r } { A ( \lambda ) = \sum _ { i = 0 } ^ { l } \lambda ^ { i } A _ { i } } \end{array}$ be an $n \times n$ matrix polynomial $( \mathrm { i . e . , ~ } A _ { i } \in \mathcal { F } ^ { n \times n }$ $i = 0 , 1 , \ldots , l )$ of degree l. If $A _ { l } = I ,$ , then the matrix polynomial $A ( \lambda )$ is said to be monic. If $\begin{array} { r } { B ( \lambda ) = \sum _ { i = 0 } ^ { m } \lambda ^ { i } B _ { i } } \end{array}$ denotes an $n \times n$ matrix polynomial of degree $m ,$ then obviously

$$
A ( \lambda ) + B ( \lambda ) = \sum _ { i = 0 } ^ { k } \lambda ^ { i } ( A _ { i } + B _ { i } ) ,
$$

where $k = \operatorname* { m a x } ( l , m )$ . Thus, the degree of $A ( \lambda ) + B ( \lambda )$ doex not exceed k.

Furthermore, the degree of the product

$$
A ( \lambda ) B ( \lambda ) = A _ { 0 } B _ { 0 } + \lambda ( A _ { 1 } B _ { 0 } + A _ { 0 } B _ { 1 } ) + \dots + \lambda ^ { l + m } A _ { l } B _ { m }
$$

does not exceed $l + m$ . Clearly, if either $A ( \lambda )$ or $B ( \lambda )$ is a matrix polynomial with an invertible leading coefficient, then the degree of the product is exactly $l + m$

Suppose that $B ( \lambda )$ is a matrix polynomial of degree m with an invertible leading coefficient and that there exist matrix polynomials $Q ( \lambda ) , R ( \lambda )$ , with $R ( \lambda ) \equiv 0$ or the degree of $R ( \lambda )$ less than m, such that

$$
A ( \lambda ) = Q ( \lambda ) B ( \lambda ) + R ( \lambda ) .
$$

If this is the case we call $Q ( \lambda )$ a right quotient of $A ( \lambda )$ on division by B(λ) and $R ( \lambda )$ is a right remainder of $A ( \lambda )$ on division by $B ( \lambda )$ . Similarly, $\tilde { Q } ( \lambda )$ $\widetilde { R } ( \lambda )$ are a left quotient and left remainder of $A ( \lambda )$ on division by $B ( \lambda )$ if

$$
A ( \lambda ) = B ( \lambda ) { \widetilde Q } ( \lambda ) + { \widetilde R } ( \lambda )
$$

and $\widetilde { R } ( \lambda ) \equiv 0$ or the degree of $R ( \lambda )$ is less than m.

If the right remainder of $A ( \lambda )$ on division by $B ( \lambda )$ is zero, then $Q ( \lambda )$ is said to be a right divisor of $A ( \lambda )$ on division by $B ( \lambda )$ . A similar definition applies for a left divisor of $A ( \lambda )$ on division by $B ( \lambda )$

In order to make these formal definitions meaningful, we must show that, given this $A ( \lambda )$ and $B ( \lambda )$ , there do exist quotients and remainders as defined. When we have done this we shall prove that they are also unique. The proof of the next theorem is a generalization of the division algorithm for scalar polynomials.

Theorem 1. Let $\begin{array} { r } { A ( \lambda ) = \sum _ { i = 0 } ^ { l } \lambda ^ { i } A _ { i } , B ( \lambda ) = \sum _ { i = 0 } ^ { m } \lambda ^ { i } B _ { i } } \end{array}$ be $n \times n$ matrix polynomials of degrees l and m, respectively, with det $B _ { m } \neq 0$ . Then there exists a right quotient and right remainder of $A ( \lambda )$ on division by $B ( \lambda )$ and similarly for a left quotient and left remainder.

PROOF. If $l < m$ , we have only to put $Q ( \lambda ) = \theta$ and $R ( \lambda ) = A ( \lambda )$ to obtain the result.

If $l \geq m ,$ , we first “divide by" the leading term of $B ( \lambda )$ , namely, $B _ { m } \lambda ^ { m }$ Observe that the term of highest degree of the λ-matrix $A _ { l } B _ { m } ^ { - 1 } \lambda ^ { l - m } B ( \lambda )$ is just $A _ { l } \lambda ^ { l }$ . Hence

$$
A ( \lambda ) = A _ { l } B _ { m } ^ { - 1 } \lambda ^ { l - m } B ( \lambda ) + A ^ { ( 1 ) } ( \lambda ) ,
$$

where $A ^ { ( 1 ) } ( \lambda )$ is a matrix polynomial whose degree, $l _ { 1 }$ , does not exceed ${ l - 1 }$ . Writing $A ^ { ( 1 ) } ( \lambda )$ in decreasing powers, let

$$
A ^ { ( 1 ) } ( \lambda ) = A _ { l _ { 1 } } ^ { ( 1 ) } \lambda ^ { l _ { 1 } } + \cdot \cdot \cdot + A _ { 0 } ^ { ( 1 ) } , \qquad A _ { l _ { 1 } } ^ { ( 1 ) } \neq 0 , \qquad l _ { 1 } < l .
$$

If $l _ { 1 } \geq m$ we repeat the process, but on $A ^ { ( 1 ) } ( \lambda )$ rather than $A ( \lambda )$ to obtain

$$
A ^ { ( 1 ) } ( \lambda ) = A _ { l _ { 1 } } ^ { ( 1 ) } B _ { m } ^ { - 1 } \lambda ^ { l _ { 1 } - m } B ( \lambda ) + A ^ { ( 2 ) } ( \lambda ) ,
$$

where

$$
A ^ { ( 2 ) } ( \lambda ) = A _ { l _ { 2 } } ^ { ( 2 ) } \lambda ^ { l _ { 2 } } + \cdot \cdot \cdot + A _ { 0 } ^ { ( 2 ) } , \qquad A _ { l _ { 2 } } ^ { ( 2 ) } \neq 0 , l _ { 2 } < l _ { 1 } .
$$

In this manner we can construct a sequence of matrix polynomials $A ( \lambda )$ ${ \cal A } ^ { ( 1 ) } ( \lambda ) , { \cal A } ^ { ( 2 ) } ( \lambda ) , . .$ . whose degrees are strictly decreasing, and after a finite number of terms we arrive at a matrix polynomial $A ^ { ( r ) } ( \lambda )$ of degree $l _ { r } < m ,$ with $l _ { r - 1 } \geq m$ Then, if we write ${ \cal A } ( \lambda ) = { \cal A } ^ { ( 0 ) } ( \lambda )$

$$
A ^ { ( s - 1 ) } ( \lambda ) = A _ { l _ { s - 1 } } ^ { ( s - 1 ) } B _ { m } ^ { - 1 } \lambda ^ { l _ { s - 1 } - m } B ( \lambda ) + A ^ { ( s ) } ( \lambda ) , \qquad s = 1 , 2 , \ldots , r .
$$

Combining these equations, we have

$$
\begin{array} { r } { A ( \lambda ) = ( A _ { l } B _ { m } ^ { - 1 } \lambda ^ { l - m } + A _ { l _ { 1 } } ^ { ( 1 ) } B _ { m } ^ { - 1 } \lambda ^ { l _ { 1 } - m } + \cdot \cdot \cdot } \\ { + \ A _ { l _ { r - 1 } } ^ { ( r - 1 ) } B _ { m } ^ { - 1 } \lambda ^ { l _ { r - 1 } - m } ) B ( \lambda ) + A ^ { ( r ) } ( \lambda ) . } \end{array}
$$

The matrix in parentheses can now be identified as a right quotient of $A ( \lambda )$ on division by $B ( \lambda )$ , and $A ^ { ( r ) } ( \lambda )$ is the right remainder.

It is not difficult to provide the modifications to the proof needed to prove the existence of a left quotient and remainder.

Theorem 2. With the hypotheses of Theorem 1, the right quotient, right remainder, left quotient, and left remainder are each unique.

ProoF. Suppose that there exist matrix polynomials Q(λ), R(λ) and $Q _ { 1 } ( \lambda )$ $R _ { 1 } ( \lambda )$ such that

$$
A ( \lambda ) = Q ( \lambda ) B ( \lambda ) + R ( \lambda )
$$

and

$$
A ( \lambda ) = Q _ { 1 } ( \lambda ) B ( \lambda ) + R _ { 1 } ( \lambda )
$$

where $R ( \lambda ) , R _ { 1 } ( \lambda )$ each have degree less than m. Then

$$
( Q ( \lambda ) - Q _ { 1 } ( \lambda ) ) B ( \lambda ) = R _ { 1 } ( \lambda ) - R ( \lambda ) .
$$

If $Q ( \lambda ) \neq Q _ { 1 } ( \lambda )$ , then the left-hand side of this equation is a matrix polynomial whose degree is at least m. However, the right-hand side is a matrix polynomial of degree less than m. Hence $Q _ { 1 } ( \lambda ) = Q ( \lambda )$ , whence $R _ { 1 } ( \lambda ) = R ( \lambda )$ also.

A similar argument can be used to establish the uniqueness of the left quotient and remainder.

Exercise 1. Examine the right and left quotients and remainders of A(λ) on division by B(λ), where

$$
A ( \lambda ) = \left[ \begin{array} { c c } { { \lambda ^ { 4 } + \lambda ^ { 2 } + \lambda - 1 } } & { { \lambda ^ { 3 } + \lambda ^ { 2 } + \lambda + 2 } } \\ { { 2 \lambda ^ { 3 } - \lambda } } & { { 2 \lambda ^ { 2 } + 2 \lambda } } \end{array} \right] ,
$$

$$
B ( \lambda ) = \left[ \begin{array} { c c } { { \lambda ^ { 2 } + 1 } } & { { 1 } } \\ { { \lambda } } & { { \lambda ^ { 2 } + \lambda } } \end{array} \right] .
$$

SoLUTIoN. Note first of all that B(λ) has an invertible leading coefficient. It is found that

$$
\begin{array} { l } { { A ( \lambda ) = { \displaystyle { \left[ \lambda ^ { 2 } - 1 \quad \lambda - 1 \right] } } { \displaystyle { \left[ \lambda ^ { 2 } + 1 \quad \lambda ^ { 2 } + 3 \right] } } { \displaystyle { \left[ \lambda ^ { 2 } + 1 \quad \lambda ^ { 2 } + \lambda \right] } } + { \displaystyle { \left[ \begin{array} { c c } { { 2 \lambda } } & { { 2 \lambda + 3 } } \\ { { - 5 \lambda } } & { { - 2 \lambda } } \end{array} \right] } } } } \\ { { \mathrm { } } } \\ { { \mathrm { } = Q ( \lambda ) B ( \lambda ) + R ( \lambda ) , } } \end{array}
$$

and

$$
A ( \lambda ) = { \binom { \lambda ^ { 2 } + 1 } { \lambda } } \quad { 1 } _ { 2 } ^ { 1 } + { \lambda } { \biggr ] } { \left[ \begin{array} { l l } { \lambda ^ { 2 } } & { \lambda + 1 } \\ { \lambda - 1 } & { 1 } \end{array} \right] } = B ( \lambda ) { \widetilde { Q } } ( \lambda ) .
$$

Thus, $\tilde { Q } ( \lambda )$ is a left divisor of A(λ). □

Now we consider the important special case in which a divisor is linear (i.e., a matrix polynomial of the first degree). But first note that when discussing a' scalar polynomial $p ( \lambda )$ , we may write

$$
p ( \lambda ) = a _ { l } \lambda ^ { l } + a _ { l - 1 } \lambda ^ { l - 1 } + \cdot \cdot \cdot + a _ { 0 } = \lambda ^ { l } a _ { l } + \lambda ^ { l - 1 } a _ { l - 1 } + \cdot \cdot \cdot + a _ { 0 } .
$$

For a matrix polynomial with a matrix argument, this is not generally possible. If A(λ) is a matrix polynomial over $\mathcal { F }$ and $B \in \mathcal { F } ^ { n \times n } .$ , we define the right value A(B) of A(λ) at B by

$$
A ( B ) = A _ { l } B ^ { l } + A _ { l - 1 } B ^ { l - 1 } + \dots + A _ { 0 }
$$

and the left value $\tilde { A } ( B )$ of A(λ) at B by

$$
\widetilde { A } ( B ) = B ^ { l } A _ { l } + B ^ { l - 1 } A _ { l - 1 } + \cdot \cdot \cdot + A _ { 0 } .
$$

The reader should be familiar with the classical remainder theorem: On dividing the scalar polynomial $p ( \lambda )$ by $\lambda - b$ the remainder is $p ( b )$ . We now prove a remarkable extension of this result to matrix polynomials. Note first of all that λI — B is monic.

Theorem 3. The right and left remainders of a matrix polynomial $A ( \lambda )$ on division by $\lambda I - B$ are $A ( B )$ and $\tilde { A } ( B )$ , respectively.

PRoOF. The factorization

$$
\lambda ^ { j } I - B ^ { j } = ( \lambda ^ { j - 1 } I + \lambda ^ { j - 2 } B + \cdots + \lambda B ^ { j - 2 } + B ^ { j - 1 } ) ( \lambda I - B )
$$

can be verified by multiplying out the product on the right. Premultiply both sides of this equation by $A _ { j }$ and sum the resulting equations for $j = 1 , 2 , \dots l .$ The right-hand side of the equation obtained is of the form $C ( \lambda ) ( \lambda I - B )$ , where $C ( \lambda )$ is a matrix polynomial.

The left-hand side is

$$
\sum _ { j = 1 } ^ { l } A _ { j } \lambda ^ { j } - \sum _ { j = 1 } ^ { l } A _ { j } B ^ { j } = \sum _ { j = 0 } ^ { l } A _ { j } \lambda ^ { j } - \sum _ { j = 0 } ^ { l } A _ { j } B ^ { j } = A ( \lambda ) - A ( B ) .
$$

Thus,

$$
A ( \lambda ) = C ( \lambda ) ( \lambda I - B ) + A ( B ) .
$$

The result now follows from the uniqueness of the right remainder on division of $A ( \lambda )$ by $( \lambda I - B )$

The result for the left remainder is obtained by reversing the factors in the initial factorization, multiplying on the right by $A _ { j } ,$ and summing.

An $n \times n$ matrix $\pmb { X } \in \mathcal { F } ^ { n \times n }$ such that $A ( X ) = 0$ (respectively, $\tilde { A } ( X ) = 0 )$ is referred to as a $r i g h t$ (respectively, left) solvent of the matrix polynomial $A ( \lambda )$

Corollary 1. The matrix polynomial $A ( \lambda )$ is divisible on the right (respectively, left) by $\lambda I - B$ with zero remainder if and only if B is a right (respectively, left) solvent of A(λ)

This result provides a second proof of the Cayley-Hamilton theorem (see Theorem 6.2.5).

Theorem 4. If A is a square matrix with characteristic polynomial $c ( \lambda )$ then $c ( A ) = 0 .$ In other words, A is a zero of its characteristic polynomial.

PROOF. Let $A \in { \mathcal { F } } ^ { n \times n }$ and let $c ( \lambda )$ denote the characteristic polynomial of A. Define the matrix $B ( \lambda ) = \operatorname { a d j } ( \lambda I - A )$ and (see Section 2.6) observe that

$B ( \lambda )$ is, by definition, an $n \times n$ matrix polynomial over $\mathcal { F }$ of degree $n - 1$ and that

$$
( \lambda I - A ) B ( \lambda ) = B ( \lambda ) ( \lambda I - A ) = c ( \lambda ) I .\tag{1}
$$

Now, $c ( \lambda ) I$ is a matrix polynomial of degree n that is divisible on both the left and the right by $\lambda I - A$ with zero remainder. It remains now to apply Corollary 1 above.

Corollary 2. If f is any scalar polynomial over $\mathcal { F }$ and $A \in { \mathcal { F } } ^ { n \times n } ,$ , then there is a polynomial p (depending on A) of degree less than n for which $f ( A ) = p ( A )$

PROOF. Let $f ( \lambda ) = q ( \lambda ) c ( \lambda ) + r ( \lambda )$ , where $c ( \lambda )$ is the characteristic polynomial of A and $r ( \lambda )$ is either zero or a polynomial of degree not exceeding $n - 1$ . Then $f ( A ) = q ( A ) c ( A ) + r ( A )$ and, by Theorem $4 , f ( A ) = r ( A )$

This result appears again later as a consequence of the definition of $f ( A )$ for more general classes of scalar functions $f .$

## 7.3 Elementary Operations and Equivalence

In this section our immediate objective is the reduction of a matrix polynomial to a simpler form by means of equivalence transformations, which we will now describe. This analysis is a natural extension of that developed in Sections 2.7 and 2.10 for matrices with entries from a field $\mathcal { F }$ to matrices whose entries are scalar polynomials and so no longer form a field. Afterwards, on confining our attention to the matrix polynomial $\lambda I - A$ , the desired normal (canonical) forms for the (constant) matrix A will be derived.

We start by defining the elementary row and column operations on a matrix polynomial over $\mathcal { F }$ by an appropriate generalization of those (in fact, only of the third one) on a matrix with constant entries as described in Section 2.7. The parentheses refer to the right elementary operations.

(1) Multiply any row (column) by a nonzero $c \in { \mathcal { F } } .$

(2) Interchange any two rows (columns).

(3) Add to any row (column) any other row (column) multiplied by an arbitrary polynomial $b ( \lambda )$ over $\mathcal { F } .$

It is easy to verify (comparing with Section 2.7) that performing an elementary row operation on an $n \times n$ matrix polynomial is equivalent to premultiplication of the matrix polynomial by an $n \times n$ matrix of one of the following three forms, respectively:

$$
E ^ { ( 1 ) } = \left[ \begin{array} { c c c c c c } { { 1 } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { c } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { 1 } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { 1 } } \end{array} \right] ,
$$

$$
E ^ { ( 2 ) } = \left[ \begin{array} { c c c c c c c } { { 1 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { 0 } } & { { \cdots } } & { { 1 } } & { { } } & { { } } \\ { { } } & { { } } & { { 1 } } & { { \ddots } } & { { } } & { { \vdots } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { 1 } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \end{array} \right] ,
$$

$$
E _ { 1 } ^ { ( 3 ) } ( \lambda ) = \left[ \begin{array} { c c c c c c } { { 1 } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { 1 } } & { { \cdots } } & { { b ( \lambda ) } } & { { } } \\ { { } } & { { } } & { { } } & { { \ddots } } & { { \vdots } } & { { } } \\ { { } } & { { } } & { { } } & { { 1 } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { 1 } } \end{array} \right] ,\tag{or}
$$

$$
E _ { 2 } ^ { ( 3 ) } ( \lambda ) = \left[ \begin{array} { c c c c c c c } { { 1 } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { 1 } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \vdots } } & { { \ddots } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { b ( \lambda ) } } & { { \cdots } } & { { 1 } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { } } & { { 1 } } \end{array} \right] .
$$

As in Section 2.7, the matrices above are said to be elementary matrices of the first, second; or third kind. Observe that the elementary matrices can be generated by performing the desired operation on the unit matrix, and that postmultiplication by an appropriate elementary matrix produces an elementary column operation on the matrix polynomial.

Exercise 1. Prove that elementary matrices are unimodular and that their inverses are also elementary matrices.

We can now make a formal definition of equivalence transformations: two matrix polynomials $A ( \lambda )$ and $B ( \lambda )$ , over ${ \mathcal F } ,$ are said to be equivalent, or to be connected by an equivalence transformation, if B(λ) can be obtained from $A ( \lambda )$ by a finite sequence of elementary operations. It follows from the equivalence of elementary operations and operations with elementary matrices that $A ( \lambda )$ and B(λ) are equivalent if and only if there are elementary matrices $E _ { 1 } ( \lambda ) , E _ { 2 } ( \lambda ) , \dots , E _ { k } ( \lambda ) , E _ { k + 1 } ( \lambda ) , \dots , E _ { s } ( \lambda )$ such that

$$
B ( \lambda ) = E _ { k } ( \lambda ) \cdot \cdot \cdot E _ { 1 } ( \lambda ) A ( \lambda ) E _ { k + 1 } ( \lambda ) \cdot \cdot \cdot E _ { s } ( \lambda )
$$

or, equivalently,

$$
B ( \lambda ) = P ( \lambda ) A ( \lambda ) Q ( \lambda ) ,\tag{1}
$$

where $P ( \lambda ) = E _ { k } ( \lambda ) \cdots E _ { 1 } ( \lambda )$ and $Q ( \lambda ) = E _ { k + 1 } ( \lambda ) \cdot \cdot \cdot E _ { s } ( \lambda )$ are matrix polynomials over F. Exercise 1 implies that the matrices P(λ) and $Q ( \lambda )$ are unimodular and hence the following propositions.

Proposition 1. The matrix polynomials $A ( \lambda )$ and B(λ) are equivalent if and only if there are unimodular matrices P(λ) and Q(λ) such that Eq. (1) is valid

The last fact readily implies that equivalence between matrix polynomials is an equivalence relation.

Exercise 2. Denoting the fact that A(λ) and B(λ) are equivalent by $A \sim B ,$ prove that

(a) $A \sim A$

(b) $A \sim B$ implies $B \sim A$ •う

(c) A \~ B and B ∼ C implies $A \sim C$

Exercise 3. Prove that any unimodular matrix is equivalent to the identity matrix.

SOLUTION. If A(λ) is unimodular, then $A ( \lambda ) [ A ( \lambda ) ] ^ { - 1 } = I$ and hence relation (1) holds with P(λ) = I and Q(λ) = [A(λ)]−1. □

Exercise 2 shows that the set of all $n \times n$ matrix polynomials splits into subsets of mutually equivalent matrices. Exercise 3 gives one of these classes, namely, the class of unimodular matrices.

Exercise 4. Prove that a matrix polynomial is unimodular if and only if it can be decomposed into a product of elementary matrices.

Hint. For the necessary part, use Exercise 3.

Exercise 5. Show that the matrices

$$
A ( \lambda ) = \left[ \lambda \begin{array} { l l } { { \lambda } } & { { \lambda + 1 } } \\ { { \lambda ^ { 2 } - \lambda } } & { { \lambda ^ { 2 } - 1 } } \end{array} \right] \qquad \mathrm { a n d } \qquad B = \left[ \begin{array} { l l } { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } \end{array} \right]
$$

are equivalent and find the transforming matrices P(λ) and Q(λ).

SOLUTION. To simplify $A ( \lambda ) ,$ , add $- ( \lambda - 1 )$ times the first row to the second row, and then add –1 times the first column to the second. Finally, adding — λ times the second column of the new matrix to the first and interchanging columns, obtain the matrix B. Translating the operations performed into elementary matrices and finding their product, it is easily found that

$$
Q ( \lambda ) = \left[ { \begin{array} { c c } { - 1 } & { 1 + \lambda } \\ { 1 } & { - \lambda } \end{array} } \right] \qquad P ( \lambda ) = \left[ { \begin{array} { c c } { 1 } & { 0 } \\ { 1 - \lambda } & { 1 } \end{array} } \right]
$$

and that Eq. (1) holds.

Exercise 6. Show that the following pairs of matrices are equivalent:

(a)

(b)

$$
{ \begin{array} { r l } & { { \left[ \begin{array} { l l l l } { } & { 0 } & { 1 } & { \lambda } \\ { \lambda } & { \lambda } & { 1 } \\ { \lambda ^ { 2 } - \lambda } & { \lambda ^ { 2 } - 1 } & { \lambda ^ { 2 } - 1 } \end{array} \right] } \qquad { \mathrm { a n d } } \qquad { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] } ; } \\ & { { \left[ \begin{array} { l l l } { } & { \lambda ^ { 2 } } & { \lambda + 1 } \\ { \lambda - 1 } & { \lambda ^ { 2 } } \end{array} \right] } \qquad { \mathrm { a n d } } \qquad { \left[ \begin{array} { l l l } { 1 } & { } & { 0 } \\ { 0 } & { \lambda ^ { 4 } - \lambda ^ { 2 } + 1 } \end{array} \right] } . } \end{array} }
$$

Exercise 7. Show that if E(λ) is a unimodular matrix polynomial, then all minors of size two or more are independent of λ.

SoLUTIoN. Observe that this is true for all elementary matrices. Express $E ( \lambda )$ as a product of elementary matrices and use the Binet-Cauchy formula.

## 7.4 A Canonical Form for a Matrix Polynomial

The objective of this section is to find the simplest matrix polynomial in each equivalence class of mutually equivalent matrix polynomials. In more detail, it will be shown that any n × n matrix polynomial is equivalent to a

diagonal matrix polynomial

$$
A _ { 0 } ( \lambda ) = \mathrm { d i a g } [ a _ { 1 } ( \lambda ) , a _ { 2 } ( \lambda ) , \ldots , a _ { n } ( \lambda ) ] ,\tag{1}
$$

in which $a _ { j } ( \lambda )$ is zero or a monic polynomial, $j = 1 , 2 , \dots , n ,$ and $a _ { j } ( \lambda )$ is divisible by $a _ { j - 1 } ( \lambda ) , j = 2 , 3 , \ldots , n .$ A matrix polynomial with these properties is called a canonical matrix polynomial. Note that if there are zeros among the polynomials $a _ { j } ( \lambda )$ then they must occupy the last places, since nonzero polynomials are not divisible by the zero polynomial. Furthermore, if some of the polynomials $a _ { j } ( \lambda )$ are (nonzero) scalars, then they must be equal to 1 and be placed in the first positions of the canonical matrix, since 1 is divisible only by 1. Thus, the canonical matrix is generally of the form

$$
A _ { 0 } ( \lambda ) = \mathrm { d i a g } [ 1 , \ldots , 1 , a _ { 1 } ( \lambda ) , \ldots , a _ { k } ( \lambda ) , 0 , \ldots 0 ] ,\tag{2}
$$

where $a _ { j } ( \lambda )$ is a monic polynomial of degree at least 1 and is divisible (for $j = 2 , \ldots , k )$ by $a _ { j - 1 } ( \lambda )$ . It is also possible that the diagonal of the matrix in (2) contains no zeros or ones.

Theorem 1. Any $n \times n$ matrix polynomial over $\mathcal { F }$ is equivalent to a canonical matrix polynomial.

ProOF. We may assume that $A ( \lambda ) \not \equiv 0 ,$ for otherwise there is nothing to prove. The proof is merely a description of a sequence of elementary transformations needed to reduce successively the rows and columns of $A ( \lambda )$ to the required form.

Step 1. Let $a _ { i j } ( \lambda )$ be a nonzero element of $A ( \lambda )$ of least degree; by interchanging rows and columns (elementary operations of type 2) bring this element to the 1, 1 position and call it $a _ { 1 1 } ( \lambda )$ . For each element of the first row and column of the resulting matrix, we find the quotient and remainder on division by $a _ { 1 1 } ( \lambda )$

$$
\begin{array} { r l } { a _ { 1 j } ( \lambda ) = a _ { 1 1 } ( \lambda ) q _ { 1 j } ( \lambda ) + r _ { 1 j } ( \lambda ) , \quad } & { j = 2 , 3 , \ldots , n , } \\ { a _ { i 1 } ( \lambda ) = a _ { 1 1 } ( \lambda ) q _ { i 1 } ( \lambda ) + r _ { i 1 } ( \lambda ) , \quad } & { i = 2 , 3 , \ldots , n . } \end{array}
$$

Now, for each i and $j ,$ subtract $q _ { 1 , i } ( \lambda )$ times the first column from the jth column and subtract ${ q _ { i 1 } ( \lambda ) }$ times the first row from the ith row (elementary operations of type 3). Then the elements $a _ { 1 j } ( \lambda ) , a _ { i 1 } ( \lambda )$ are replaced by $r _ { 1 j } ( \lambda )$ and $r _ { i 1 } ( \lambda )$ , respectively $( i , j = 2 , 3 , \ldots , n ) .$ , all of which are either the zero polynomial or have degree less than that of $a _ { 1 1 } ( \lambda )$ . If the polynomials are not all zero, we use an operation of type 2 to interchange $a _ { 1 1 } ( \lambda )$ with an element $r _ { 1 j } ( \lambda )$ or $r _ { i 1 } ( \lambda )$ of least degree. Now repeat the process of reducing the degree of the off-diagonal elements of the first row and column to be less than that of the new $a _ { 1 1 } ( \lambda )$ . Clearly, since the degree of $a _ { 1 1 } ( \lambda )$ is strictly decreasing at each step, we eventually reduce the λ-matrix to the form

$$
{ \left[ \begin{array} { l l l l } { a _ { 1 1 } ( \lambda ) } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { a _ { 2 2 } ( \lambda ) } & { \cdots } & { a _ { 2 n } ( \lambda ) } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { a _ { n 2 } ( \lambda ) } & { \cdots } & { a _ { n n } ( \lambda ) } \end{array} \right] } .\tag{3}
$$

Step 2. In the form (3) there may now be nonzero elements $a _ { i j } ( \lambda ) , 2 \leq i ,$ $j \leq n ,$ whose degree is less than that of $a _ { 1 1 } ( \lambda )$ . If so, we repeat Step 1 again and arrive at another matrix of the form (3) but with the degree of $a _ { 1 1 } ( \lambda )$ further reduced. Thus, by repeating Step 1 a sufficient number of times, we can find a matrix of the form (3) that is equivalent to $A ( \lambda )$ and for which $a _ { 1 1 } ( \lambda )$ is a nonzero element of least degree.

Step 3. Having completed Step 2, we now ask whether there are nonzero elements that are not divisible by $a _ { 1 1 } ( \lambda )$ . If there is one such, say $a _ { i j } ( \lambda )$ , we add column j to column 1, find remainders and quotients of the new column 1 on division by $a _ { 1 1 } ( \lambda )$ , and go on to repeat Steps 1 and 2, winding up with a form (3), again with $a _ { 1 1 } ( \lambda )$ replaced by a polynomial of smaller degree.

Again, this process can continue only for a finite number of steps before we arrive at a matrix of the form

$$
{ \left[ \begin{array} { l l l l } { a _ { 1 } ( \lambda ) } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { b _ { 2 2 } ( \lambda ) } & { \cdots } & { b _ { 2 n } ( \lambda ) } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { b _ { n 2 } ( \lambda ) } & { \cdots } & { b _ { n n } ( \lambda ) } \end{array} \right] } ,
$$

where, after an elementary operation of type 1 (if necessary), $a _ { 1 } ( \lambda )$ is monic and all the nonzero elements $b _ { i j } ( \lambda )$ are divisible by $a _ { 1 } ( \lambda )$ without remainder.

Step 4. If all $b _ { i j } ( \lambda )$ are zero, the theorem is proved. If not, the above matrix may be reduced to the form

$$
\left[ { \begin{array} { c c c c c } { a _ { 1 } ( \lambda ) } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { a _ { 2 } ( \lambda ) } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { c _ { 3 3 } ( \lambda ) } & { \cdots } & { c _ { 3 n } ( \lambda ) } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { 0 } & { c _ { n 3 } ( \lambda ) } & { \cdots } & { c _ { n n } ( \lambda ) } \end{array} } \right]
$$

where $a _ { 2 } ( \lambda )$ is divisible by $a _ { 1 } ( \lambda )$ and the elements $c _ { i j } ( \lambda ) , 3 \leq i , j \leq n ,$ are divisible by $a _ { 2 } ( \lambda )$ . Continuing the process we arrive at the statement of the theorem.■

Note that a matrix polynomial is regular if and only if all the elements $a _ { 1 } ( \lambda ) , \dots , a _ { n } ( \lambda )$ in Eq. (1) are nonzero polynomials.

Exercise 1. Prove that, by using left (right) elementary operations only, a matrix polynomial can be reduced to an upper- (lower-) triangular matrix polynomial $B ( \lambda )$ with the property that if the degree of $b _ { j j } ( \lambda )$ is $l _ { j } \left( j = 1 \right.$ 2 $2 , \ldots , n )$ , then

(a) $l _ { j } = 0$ implies that $b _ { k j } = 0 ( b _ { j k } = 0 ) , k = 1 , 2 , \ldots , j - 1$ , and

(b) $l _ { j } > 0$ implies that the degree of nonzero elements $b _ { k j } ( \lambda ) \ ( b _ { j k } ( \lambda ) )$ is less than $l _ { j } , k = 1 , 2 , \ldots , j - 1 . \quad \sqcup$

The reduction of matrix polynomials described above takes on a simple form in the important special case in which $A ( \lambda )$ does not depend explicitly on λ at all, that is, when $A ( \lambda ) \equiv A \in { \mathcal { F } } ^ { n \times n }$ . This observation can be used to show that Theorem 1 implies Theorem 2.7.2 (for square matrices).

The uniqueness of the polynomials $a _ { 1 } ( \lambda ) , \dots , a _ { n } ( \lambda )$ appearing in Eq. (1) is shown in the next section.

## 7.5 Invariant Polynomials and the Smith Canonical Form

We start this section by constructing a system of polynomials that is uniquely defined by a given matrix polynomial and that is invariant under equivalence transformations of the matrix. For this purpose, we first define the rank of a matrix polynomial to be the order of its largest minor that is not equal to the zero polynomial. For example, the rank of $A ( \lambda )$ defined in Exercise 7.3.5 is equal to 1, while the rank of the canonical matrix polynomial $A _ { 0 } ( \lambda ) = \mathrm { d i a g } [ a _ { 1 } ( \lambda ) , \ldots , a _ { r } ( \lambda ) , 0 , \ldots , 0 ]$ is equal to r. Note also that if $A ( \lambda )$ is an n × n matrix polynomial, then it is regular if and only if its rank is n.

Proposition 1. The rank of a matrix polynomial is invariant under equivalence transformations.

ProoF. Let the matrix polynomials $A ( \lambda )$ and $B ( \lambda )$ be equivalent. Then by Proposition 7.3.1 there are unimodular matrices $P ( \lambda )$ and $Q ( \lambda )$ such that $B ( \lambda ) = P ( \lambda ) A ( \lambda ) Q ( \lambda )$ . Apply the Binet-Cauchy formula twice to this equation to express a minor $b ( \lambda )$ of order j of $B ( \lambda )$ in terms of minors $a _ { s } ( \lambda )$ of $A ( \lambda )$ of the same order as follows (after a reordering):

$$
b ( \lambda ) = \sum _ { s } p _ { s } ( \lambda ) a _ { s } ( \lambda ) q _ { s } ( \lambda ) ,\tag{1}
$$

where $p _ { s } ( \lambda )$ and $q _ { s } ( \lambda )$ denote the appropriate minors of order j of the matrix polynomials $P ( \lambda )$ and $Q ( \lambda )$ , respectively. If now $b ( \lambda )$ is a nonzero minor of $B ( \lambda )$ of the greatest order r (that is, the rank of $B ( \lambda )$ is $r ) ,$ then it follows from Eq. (1) that at least one minor $a _ { s } ( \lambda )$ (of order r) is a nonzero polynomial and hence the rank of $B ( \lambda )$ does not exceed the rank of $A ( \lambda )$ . However, applying the same argument to the equation $A ( \lambda ) = [ P ( \lambda ) ] ^ { - 1 } B ( \lambda ) [ Q ( \lambda ) ] ^ { - 1 }$ , we see thatrank $A ( \lambda ) \leq \mathrm { r a n k } \ B ( \lambda )$ . Thus, the ranks of equivalent matrix polynomials coincide.

Suppose that the $n \times n$ matrix polynomial $A ( \lambda )$ over $\mathcal { F }$ has rank r and let $d _ { i } ( \lambda )$ be the greatest common divisor of all minors of $A ( \lambda )$ of order j, where $j = 1 , 2 , \dots , r .$ Clearly, any minor of order $j \geq 2$ may be expressed as a linear combination of minors of order $j - 1 ,$ , so that $d _ { j - 1 } ( \lambda )$ is necessarily a factor $d _ { j } ( \lambda )$ . Hence, if we define $d _ { \boldsymbol { \mathfrak { o } } } ( \lambda ) \equiv 1$ , then in the sequence

$$
d _ { 0 } ( \lambda ) , d _ { 1 } ( \lambda ) , \ldots , d _ { r } ( \lambda ) ,
$$

$d _ { j } ( \lambda )$ is divisible by $d _ { j - 1 } ( \lambda ) , j = 1 , 2 , \ldots , r .$

Exercise 1. Show that the polynomials $d _ { j } ( \lambda )$ defined in the previous paragraph for the canonical matrix polynomial $A _ { 0 } ( \lambda ) = \mathrm { d i a g } [ a _ { 1 } ( \lambda ) , a _ { 2 } ( \lambda ) , . . . ,$ $a _ { r } ( \lambda ) , 0 , \ldots , 0 ]$ are, respectively,

$$
d _ { 1 } ( \lambda ) = a _ { 1 } ( \lambda ) , d _ { 2 } ( \lambda ) = a _ { 1 } ( \lambda ) a _ { 2 } ( \lambda ) , \ c \ldots , d _ { r } ( \lambda ) = \prod _ { j = 1 } ^ { r } a _ { j } ( \lambda ) . \bigsqcup\tag{2}
$$

The polynomials $d _ { 0 } ( \lambda ) , d _ { 1 } ( \lambda ) , \dots , d _ { r } ( \lambda )$ have the important property of invariance under equivalence transformations. To see this, let $d _ { j } ( \lambda )$ and $\delta _ { j } ( \lambda )$ denote the (monic) greatest common divisor of all minors of order j of the matrix polynomials $A ( \lambda )$ and $B ( \lambda )$ , respectively. Note that by Proposition 1 the number of polynomials $d _ { j } ( \lambda )$ and $\delta _ { j } ( \lambda )$ is the same provided that $A ( \lambda )$ and $B ( \lambda )$ are equivalent.

Proposition 2. · Let the matrix polynomials $A ( \lambda )$ and $B ( \lambda )$ of rank r be equivalent. Then, with the notation of the previous paragraph, the polynomials $d _ { j } ( \lambda )$ and $\delta _ { j } ( \lambda )$ coincide $( j = 1 , 2 , \ldots , r )$

ProoF. Preserving the notation used in the proof of Proposition 1, it is easily seen from Eq. (1) that any common divisor of minors $a _ { s } ( \lambda )$ of $A ( \lambda )$ of order $j \left( 1 \leq j \leq r \right)$ is a divisor of $b ( \lambda )$ . Hence $\delta _ { i } ( \lambda )$ is divisible by $d _ { j } ( \lambda )$ But again, the equation $A ( \lambda ) = [ P ( \lambda ) ] ^ { - 1 } B ( \lambda ) [ Q ( \bar { \lambda } ) ] ^ { - 1 }$ implies that $\bar { d } _ { j } ( \lambda )$ is divisible by $\delta _ { j } ( \lambda )$ and, since both polynomials are assumed to be monic, we obtain

$$
\delta _ { j } ( \lambda ) = d _ { j } ( \lambda ) , ~ j = 1 , 2 , . . . , r . ~ 
$$

## 7.5 INVARIANT POLYNOMIALS

Now consider the quotients

$$
i _ { 1 } ( \lambda ) = \frac { d _ { 1 } ( \lambda ) } { d _ { 0 } ( \lambda ) } , \qquad i _ { 2 } ( \lambda ) = \frac { d _ { 2 } ( \lambda ) } { d _ { 1 } ( \lambda ) } , \ldots , \qquad i _ { r } = \frac { d _ { r } ( \lambda ) } { d _ { r - 1 } ( \lambda ) } .
$$

In view of the divisibility of $d _ { j } ( \lambda )$ by $d _ { j - 1 } ( \lambda )$ , the quotients $i _ { j } ( \lambda ) ( j = 1 , 2 , . . . , r )$ are polynomials. They are called the invariant polynomials of $A ( \lambda )$ ; the invariance refers to equivalence transformations. Note that for $j = 1 , 2 , \dots , r ,$

$$
d _ { j } ( \lambda ) = i _ { 1 } ( \lambda ) i _ { 2 } ( \lambda ) \cdot \cdot \cdot i _ { j } ( \lambda ) ,\tag{3}
$$

and for $j = 2 , 3 , \dots , r , i _ { j } ( \lambda )$ is divisible by $i _ { j - 1 } ( \lambda )$

Exercise 2. Find (from their definition) the invariant polynomials of the matrix polynomials

$$
{ \left[ \begin{array} { l l l l } { ~ 0 } & { 1 } & { ~ \lambda } \\ { ~ \lambda } & { ~ \lambda } & { ~ 1 } \\ { ~ \lambda ^ { 2 } ~ - ~ \lambda } & { \lambda ^ { 2 } ~ - ~ 1 } & { ~ \lambda ^ { 2 } ~ - ~ 1 } \end{array} \right] } ; \qquad ( \mathbf { b } ) ~ { \left[ \begin{array} { l l l } { ~ \lambda } & { \lambda ^ { 2 } } & { ~ 0 } \\ { ~ \lambda ^ { 3 } } & { \lambda ^ { 5 } } & { ~ 0 } \\ { ~ 0 } & { 0 } & { 2 \lambda } \end{array} \right] } .\tag{a}
$$

Answer.

$$
i _ { 1 } ( \lambda ) = 1 , i _ { 2 } ( \lambda ) = 1 ;\tag{a}
$$

$$
i _ { 1 } ( \lambda ) = \lambda , i _ { 2 } ( \lambda ) = \lambda , i _ { 3 } ( \lambda ) = \lambda ^ { 5 } - \lambda ^ { 4 } .
$$

Recalling the result of Exercise 1 and observing that the invariant polynomials of the canonical matrix polynomial are merely $a _ { j } \{ \lambda \}$ , we now use Proposition 2 to obtain the main result of the section.

Theorem 1. A matrix polynomial A(λ) of rank r is equivalent to the canonical matrix polynomial $\mathrm { d i a g } [ i _ { 1 } ( \lambda ) , \dots , i _ { r } ( \lambda ) , 0 , \dots , 0 ]$ , where $i _ { 1 } ( \lambda ) , i _ { 2 } ( \lambda ) , : \dots , i _ { r } ( \lambda )$ are the invariant polynomials of A(λ).

The canonical form

$$
\mathrm { d i a g } [ i _ { 1 } ( \lambda ) , \dots , i _ { r } ( \lambda ) , 0 , \dots , 0 ]
$$

is known as the Smith canonical form. H. J. S. Smith† obtained the form for matrices of integers (which have much the same algebraic structure as matrix polynomials) in 1861. Frobenius obtained the result for matrix polynomials in 1878. The matrix polynomial $A ( \lambda )$ and its canonical form are, of course, over the same field ${ \mathcal { F } } .$

Corollary 1. Two matrix polynomials are equivalent if and only if they have the same invariant polynomials.

PROOF. The “only $\mathrm { i f } ^ { \dag }$ statement is just Proposition 2. If two matrix polynomials have the same invariant polynomials, then Theorem 1 implies that they have the same Smith canonical form. The transitive property of equivalence relations (Exercise 7.3.2) then implies that they are equivalent.■

Exercise 3. Find the Smith canonical form of the matrices defined in Exercise 2.

Answer.

(a)

$$
\left[ { \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right]\tag{b}
$$

$$
\left[ { \begin{array} { l l l } { \lambda } & { 0 } & { 0 } \\ { 0 } & { \lambda } & { 0 } \\ { 0 } & { 0 } & { \lambda ^ { 5 } - \lambda ^ { 4 } } \end{array} } \right] . \ \sqsubseteq
$$

Exercise 3 illustrates the fact that the Smith canonical form of a matrix polynomial can be found either by performing elementary operations as described in the proof of Theorem 7.4.1 or by finding its invariant polynomials.

Exercise 4. Find the invariant polynomials of $\lambda I - C _ { a }$ where, as in Exercise $2 . 2 . 9 , C _ { a }$ denotes the $l \times l$ companion matrix associated with the polynomial $\begin{array} { r } { a ( \lambda ) = \bar { \lambda } ^ { \iota } + \sum _ { i = 0 } ^ { l - 1 } a _ { i } \lambda ^ { i } } \end{array}$

SoLUTion. Observe that there are nonzero minors of orders $1 , 2 , \ldots , l - 1$ of $\lambda I - C _ { a }$ that are independent of λ and therefore, in the previous notation, we have $d _ { 1 } = d _ { 2 } = \cdots = d _ { l - 1 } = 1$ . Since, by definition $d _ { \iota } ( \lambda ) = \operatorname* { d e t } ( \lambda I - C _ { a } ) ,$ then in view of Exercise 4.11.3, $d _ { l } ( \lambda ) = a ( \lambda )$ . Hence $i _ { 1 } = \cdots = i _ { l - 1 } = 1$ $i _ { l } ( \lambda ) = a ( \lambda )$

Exercise 5. Show that if $A \in { \mathcal { F } } ^ { n \times n }$ , then the sum of the degrees of the invariant polynomials of $\lambda I - A$ is n.

SOLUTION. Since $\lambda I - A$ is a matrix polynomial of rank $n ,$ there are (see Theorem 1) unimodular matrix polynomials P(λ) and Q(λ) such that

$$
P ( \lambda ) ( \lambda I - A ) Q ( \lambda ) = \mathrm { d i a g } [ i _ { 1 } ( \lambda ) , i _ { 2 } ( \lambda ) , \ldots , i _ { n } ( \lambda ) ] .
$$

On taking determinants, the left-hand side becomes a scalar multiple of the characteristic polynomial and hence has degree n. The result now follows immediately. □

## 7.6 Similarity and the First Normal Form

This section is devoted to the development of the connection between equivalence and similarity transformations. The first theorem will establish an important link between the theory of matrix polynomials, as discussed in this chapter, and the notion of similarity of matrices from ${ \mathcal { F } } ^ { n \times n }$

Theorem 1. Matrices $A , B \in { \mathcal { F } } ^ { n \times n }$ are similar $i f$ and only if the matrix polynomials $\lambda I - A$ and $\lambda I - B$ are equivalent.

Thus, using Theorem 7.5.1, A and B are similar if and only if $\lambda I - A$ and λI — B have the same invariant polynomials.

ProoF. Suppose first that A and B are similar. Then there is a nonsingular $\pmb { S } \in \mathcal { F } ^ { n \times n }$ such that $A = S B S ^ { - 1 }$ ; whence

$$
\lambda I - A = S ( \lambda I - B ) S ^ { - 1 } ,
$$

which implies that $\lambda I - A$ and $\lambda I - B$ are equivalent. The corollary to Theorem 7.5.1 now implies that λI — A and λI — B have the same invariant polynomials.

Conversely, suppose that λI - A and λI — B have the same invariant polynomials. Then they are equivalent and there exist unimodular matrix polynomials P(λ) and Q(λ) such that

$$
P ( \lambda ) ( \lambda I - A ) Q ( \lambda ) = \lambda I - B .
$$

Thus, defining $M ( \lambda ) = [ P ( \lambda ) ] ^ { - 1 }$ , we observe that M(λ) is a matrix polynomial and

$$
M ( \lambda ) ( \lambda I - B ) = ( \lambda I - A ) Q ( \lambda ) .
$$

Now division of M(λ) on the left by $\lambda I - A$ and of Q(λ) on the right by $\lambda I - B$ yields

$$
\begin{array} { r } { M ( \lambda ) = ( \lambda I - A ) S ( \lambda ) + M _ { 0 } , } \\ { Q ( \lambda ) = R ( \lambda ) ( \lambda I - B ) + Q _ { 0 } , } \end{array}\tag{1}
$$

where ${ \bf \nabla } \cdot { \cal M } _ { 0 } , { \cal Q } _ { 0 }$ are independent of λ. Then, substituting in the previous equation, we obtain

$$
( ( \lambda I - \mathit { A } ) S ( \lambda ) + M _ { 0 } ) ( \lambda I - \mathit { B } ) = ( \lambda I - \mathit { A } ) ( R ( \lambda ) ( \lambda I - \mathit { B } ) + \mathcal { Q } _ { 0 } ) ,
$$

whence

$$
( \lambda I - { \cal A } ) \{ S ( \lambda ) - R ( \lambda ) \} ( \lambda I - { \cal B } ) = ( \lambda I + { \cal A } ) Q _ { 0 } - M _ { 0 } ( \lambda I - \dot { \cal B } ) .
$$

But this is an identity between matrix polynomials, and since the degree of the polynomial on the right is 1, it follows that $S ( \lambda ) \equiv R ( \lambda )$ . (Otherwise the degree of the matrix polynomial on the left is at least 2.) Hence,

$$
M _ { 0 } ( \lambda I - B ) = ( \lambda I - A ) Q _ { 0 } ,\tag{2}
$$

so that

$$
M _ { 0 } = Q _ { 0 } , \qquad M _ { 0 } B = A Q _ { 0 } , \qquad \mathrm { a n d } \qquad M _ { 0 } B = A M _ { 0 } .\tag{3}
$$

Now we have only to prove that $M _ { 0 }$ is nonsingular and we are finished.

Suppose that division of $P ( \lambda )$ on the left by $\lambda I - B$ yields

$$
P ( \lambda ) = ( \lambda I - B ) U ( \lambda ) + P _ { 0 } ,
$$

where $P _ { 0 }$ is independent of λ. Then using Eqs. (1) and (2) we have

$$
\begin{array} { l } { I = M ( \lambda ) P ( \lambda ) } \\ { \ = ( ( \lambda I - A ) S ( \lambda ) + M _ { 0 } ) ( ( \lambda I - B ) U ( \lambda ) + P _ { 0 } ) } \\ { \ = ( \lambda I - A ) S ( \lambda ) ( \lambda I - B ) U ( \lambda ) + ( \lambda I - A ) Q _ { 0 } U ( \lambda ) } \\ { \ \quad \ + \ ( \lambda I - A ) S ( \lambda ) P _ { 0 } + M _ { 0 } P _ { 0 } } \\ { \ = ( \lambda I - A ) \{ Q ( \lambda ) U ( \lambda ) + S ( \lambda ) P _ { 0 } \} + M _ { 0 } P _ { 0 } . } \end{array}
$$

Hence $Q ( \lambda ) U ( \lambda ) + S ( \lambda ) P _ { 0 } = 0$ and $M _ { 0 } P _ { 0 } = I $ Thus, det $M _ { 0 } \neq 0$ and the last equation in (3) implies that A and B are similar.■

Now we are in a position to prove a theorem concerning a simple normal form to which a matrix from ${ \mathcal { F } } ^ { n \times n }$ can be reduced by similarity transformations. It is important to observe that the normal form obtained is also in ${ \mathcal { F } } ^ { n \times n }$ and that $\mathcal { F }$ is an arbitrary field.

Theorem 2. If $A \in { \mathcal { F } } ^ { n \times n }$ and the invariant polynomials of $\lambda I - A$ of nonzero degree are $i _ { s } ( \lambda ) , i _ { s + 1 } ( \lambda ) , \dots , i _ { n } ( \lambda )$ , then the matrix A is similar to the blockdiagonal matrix

$$
C _ { 1 } = \mathrm { d i a g } [ C _ { i _ { s } } , C _ { i _ { s + 1 } } , \ldots , C _ { i _ { n } } ] ,\tag{4}
$$

where $C _ { i _ { k } }$ denotes the companion matrix associated with the (invariant) polynomial $i _ { k } ( \lambda ) , ( s \leq k \leq n )$ •

The matrix $C _ { 1 }$ in Eq. (4) is often referred to as the first natural normal form of A.

PRooF. First we note that by Exercise 7.5.5 the matrix $C _ { 1 }$ in Eq. (4) is $n \times n ,$ and since the invariant polynomials are over ${ \mathcal F } ,$ we have $C _ { 1 } \in \mathcal { F } ^ { n \times n }$ We now show that $\lambda I - A$ and $\lambda I - C _ { 1 }$ have the same invariant polynomials and hence the result will follow from Theorem 1.

Indeed, by Theorem 7.5.1 and Exercise 7.5.4, the matrix polynomial $\lambda I \mathrm { ~ - ~ } C _ { i _ { k } } \enspace \left( s \le k \le n \right)$ is equivalent to the diagonal matrix $D _ { k } ( \lambda ) =$ diag[1, $\ddot { 1 } , \ldots , 1 , i _ { k } ( \lambda ) ]$ . Then it follows that $\lambda I - C _ { 1 }$ is equivalent to the matrix $D ( \boldsymbol { \lambda } ) = \mathrm { d i a g } [ D _ { s } ( \boldsymbol { \lambda } ) , D _ { s + 1 } ( \boldsymbol { \lambda } ) , \dots , D _ { n } ( \boldsymbol { \lambda } ) ]$ and thus

$$
\lambda I - C _ { 1 } = P ( \lambda ) D ( \lambda ) Q ( \lambda )\tag{5}
$$

for some unimodular matrices P(λ), Q(λ).

Now define

$$
\Delta ( \lambda ) = \mathrm { d i a g } [ 1 , \dots , 1 , i _ { s } ( \lambda ) , \dots , i _ { n } ( \lambda ) ]
$$

and observe that $\Delta ( \lambda )$ is the Smith canonical form of $\lambda I - A$ .Since by elementary operations of the second kind the matrix polynomial $D ( \boldsymbol { \lambda } )$ can be transformed into $\Delta ( \lambda )$ , they are equivalent. The relation (5) then implies the

equivalence of $\lambda I - C _ { 1 }$ and $\Delta ( \lambda )$ ; hence $1 , \dots , 1 , i _ { s } ( \lambda ) , \dots , i _ { n } ( \lambda )$ are the invariant polynomials of both $\lambda I - C _ { 1 }$ and $\lambda I - A$

Exercise 1. Check that the first natural normal forms of the matrices

$$
A _ { 1 } = { \left[ \begin{array} { l l l } { 3 } & { - 1 } & { 0 } \\ { - 1 } & { 3 } & { 0 } \\ { 1 } & { - 1 } & { 2 } \end{array} \right] } , \qquad A _ { 2 } = { \left[ \begin{array} { l l l } { 6 } & { 2 } & { 2 } \\ { - 2 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 2 } \end{array} \right] }
$$

are, respectively,

$$
C _ { 1 } ^ { ( 1 ) } = \left[ { \begin{array} { c c c } { 2 } & { \vdots } & { 0 } & { 0 } \\ { \cdots } & { \cdots } & { \cdots } \\ { 0 } & { \vdots } & { 0 } & { 1 } \\ { 0 } & { \vdots } & { - 8 } & { 6 } \end{array} } \right] , \qquad C _ { 1 } ^ { ( 2 ) } = \left[ { \begin{array} { c c c } { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 3 2 } & { - 3 2 } & { 1 0 } \end{array} } \right] . \quad \bigsqcup
$$

## 7.7 Elementary Divisors

The problem of reducing the companion matrices of invariant polynomials appearing in the first natural normal form to matrices of a smaller order depends on the field $\mathcal { F }$ over which these polynomials are defined. Indeed, we obtain the further reduction by considering the factorization of each invariant polynomial into irreducible polynomials over $\mathcal { F } .$ For simplicity, and because this is the most important case in applications, we are going to confine our attention to matrices (and hence invariant polynomials) defined over the field of complex numbers, $\mathbb { C }$ (but see also Section 6.7).

We consider the problem of an $n \times n$ matrix polynomial $A ( \lambda )$ with elements defined over $\mathbb { C } ,$ having rank $r , ( r \leq n )$ and invariant polynomials $i _ { 1 } ( \lambda ) , i _ { 2 } ( \lambda ) , \ldots , i _ { r } ( \lambda )$ . We define the zeros of det $A ( \lambda )$ to be the latent roots of $A ( \lambda )$ , and since det $A ( \lambda )$ is a polynomial over C we may write

$$
\operatorname * { d e t } { A ( \lambda ) } = k _ { 1 } \prod _ { j = 1 } ^ { s } ( \lambda - \lambda _ { j } ) ^ { m _ { j } } ,
$$

where $k _ { 1 } \neq 0 ; \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { s }$ are the distinct latent roots of $A ( \lambda )$ ; and $m _ { j } \geq 1$ for each j. From the Smith canonical form we deduce that

$$
\operatorname * { d e t } { A ( \lambda ) } = k _ { 2 } \prod _ { j = 1 } ^ { r } i _ { j } ( \lambda ) ,
$$

where $k _ { 2 } \neq 0 .$ Since the invariant polynomials are monic, it follows that $k _ { 1 } = k _ { 2 }$ and

$$
\prod _ { j = 1 } ^ { r } i _ { j } ( \lambda ) = \prod _ { k = 1 } ^ { s } ( \lambda - \lambda _ { k } ) ^ { m _ { k } } .
$$

Moreover, since $i _ { j } ( \lambda )$ is a divisor of $i _ { j + 1 } ( \lambda )$ for $j = 1 , 2 , \ldots , r - 1$ , it follows that there are integers $\alpha _ { j k } , 1 \le j \le r$ and $1 \leq k \leq s ,$ such that

$$
\begin{array} { c } { { i _ { 1 } ( \lambda ) = ( \lambda - \lambda _ { 1 } ) ^ { \alpha _ { 1 1 } } ( \lambda - \lambda _ { 2 } ) ^ { \alpha _ { 1 2 } } \cdot \cdot \cdot ( \lambda - \lambda _ { s } ) ^ { \alpha _ { 1 s } } , } } \\ { { i _ { 2 } ( \lambda ) = ( \lambda - \lambda _ { 1 } ) ^ { \alpha _ { 2 1 } } ( \lambda - \lambda _ { 2 } ) ^ { \alpha _ { 2 2 } } \cdot \cdot \cdot ( \lambda - \lambda _ { s } ) ^ { \alpha _ { 2 s } } , } } \\ { { \vdots } } \\ { { i _ { r } ( \lambda ) = ( \lambda - \lambda _ { 1 } ) ^ { \alpha _ { r 1 } } ( \lambda - \lambda _ { 2 } ) ^ { \alpha _ { r 2 } } \cdot \cdot \cdot ( \lambda - \lambda _ { s } ) ^ { \alpha _ { r s } } , } } \end{array}\tag{1}
$$

and for $k = 1 , 2 , \ldots , s ,$

$$
0 \leq \alpha _ { 1 k } \leq \alpha _ { 2 k } \leq \cdots \leq \alpha _ { r k } \leq m _ { k } , \qquad \sum _ { j = 1 } ^ { r } \alpha _ { j k } = m _ { k } .
$$

Each factor $( \lambda - \lambda _ { k } ) ^ { \alpha _ { j k } }$ appearing in the factorizations (1) with $\alpha _ { j k } > 0$ is called an elementary divisor of $A ( \lambda )$ . An elementary divisor for which $\alpha _ { j k } = 1$ is said to be linear; otherwise it is nonlinear. We may also refer to the elementary divisors $( \lambda - \lambda _ { k } ) ^ { \alpha _ { j k } }$ as those associated with $\lambda _ { k }$ , with the obvious meaning. Note that (over C) all elementary divisors are powers of a linear polynomial.

Exercise 1. Find the elementary divisors of the matrix polynomial defined in Exercise 7.5.2(b)

Answer. λ, λ, λ4, λ − 1. □

Note that an elementary divisor of a matrix polynomial may appear several times in the set of invariant polynomials of the matrix polynomial. Also, the factorizations (1) show that the system of all elementary divisors (along with the rank and order) of a matrix polynomial completely defines the set of its invariant polynomials and vice versa.

It therefore follows from Corollary 1 of Theorem 7.5.1 that the elementary divisors are invariant under equivalence transformations of the matrix polynomial.

Theorem 1. Two complex matrix polynomials are equivalent if and only if they have the same elementary divisors.

Exercise 2. Determine the invariant polynomials of a matrix polynomial of order 5 having rank 4 and elementary divisors $\lambda , \lambda , \lambda ^ { 3 } , \lambda - \overset { \cdot } { 2 } , ( \lambda - 2 ) ^ { 2 }$ $\lambda + 5$

SoLUTION. Since the order of the matrix polynomial is 5, there are five invariant polynomials $i _ { k } ( \lambda ) , k = 1 , 2 , \ldots , 5$ And since the rank is $4 , i _ { 5 } ( \lambda ) =$ $d _ { 5 } ( \lambda ) / d _ { 4 } ( \lambda ) \equiv 0 .$ Now recall that the invariant polynomial $i _ { j } ( \lambda )$ is divisible by $i _ { j - 1 } ( \lambda )$ for $j \geq 2$ . Hence, $i _ { 4 } ( \lambda )$ must contain elementary divisors associated with all eigenvalues of the matrix polynomial and those elementary divisors must be of the highest degrees. Thus, $i _ { 4 } ( \lambda ) = \lambda ^ { 3 } ( \lambda - 2 ) ^ { 2 } ( \lambda + 5 )$ . Applying the same argument to $i _ { 3 } ( \lambda )$ and the remaining elementary divisors, we obtain $i _ { 3 } ( \lambda ) = \lambda ( \lambda - 2 )$ and then $i _ { 2 } ( \lambda ) = \lambda$ . All elementary divisors are now exhausted and hence $i _ { 1 } ( \lambda ) \equiv 1 . \quad \bigsqcup$

The possibility of describing an equivalence class of matrix polynomials in terms of the set of elementary divisors permits a reformulation of the statement of Theorem 7.6.1.

Proposition 1. Two $n \times n$ matrices A and B with elements from C are similar if and only $i f \lambda I - A$ and $\lambda I - B$ have the same elementary divisors.

Before proceeding to the general reduction of matrices in $\mathbb { C } ^ { n \times n }$ , there is one more detail to be cleared up.

Theorem 2. If $A ( \lambda ) , B ( \lambda )$ are matrix polynomials over $\mathbb { C } ,$ then the set of elementary divisors of the block-diagonal matrix

$$
C ( \lambda ) = \left[ \begin{array} { c c } { A ( \lambda ) } & { 0 } \\ { 0 } & { B ( \lambda ) } \end{array} \right]
$$

is the union of the sets of elementary divisors of A(λ) and B(λ).

PROOF.. Let $D _ { 1 } ( \lambda )$ and $D _ { 2 } ( \lambda )$ be the Smith forms of $A ( \lambda )$ and $B ( \lambda )$ , respectively. Then clearly

$$
C ( \lambda ) = E ( \lambda ) { \left[ \begin{array} { l l } { D _ { 1 } ( \lambda ) } & { \quad 0 } \\ { \phantom { - } 0 } & { D _ { 2 } ( \lambda ) } \end{array} \right] } F ( \lambda )
$$

for some matrix polynomials E(λ) and $F ( \lambda )$ with constant nonzero determinants. Let $( \lambda - \lambda _ { 0 } ) ^ { \alpha _ { 1 } } , . . . , ( \lambda - \lambda _ { 0 } ) ^ { \alpha _ { p } }$ and $( \lambda - \lambda _ { 0 } ) ^ { \beta _ { 1 } } , . . . , ( \lambda - \lambda _ { 0 } ) ^ { \beta _ { q } }$ be the elementary divisors of $D _ { 1 } ( \lambda )$ and $D _ { 2 } ( \lambda )$ , respectively, corresponding to the same complex root $\lambda _ { 0 }$ . Arrange the set of exponents $\alpha _ { 1 } , \ldots , \alpha _ { p } , \beta _ { 1 } , \ldots , \beta _ { q } .$ in a nondecreasing order: $\{ \alpha _ { 1 } , \ldots , \alpha _ { p } , \beta _ { 1 } , \ldots , \beta _ { q } \} = \{ \gamma _ { 1 } , \ldots , \bar { \gamma } _ { p + q } \}$ , where $0 < \gamma _ { 1 } \leq \cdots \leq \gamma _ { p + q }$ . From the definition of invariant polynomials (Section 7.5), it is clear that in the Smith form $D = \mathrm { d i a g } [ i _ { 1 } ( \lambda ) , \ldots , i _ { r } ( \lambda ) , 0 , \ldots , 0 ]$ of diag[ $\cdot D _ { 1 } ( \lambda ) , D _ { 2 } ( \lambda ) ]$ , the invariant polynomial $i _ { r } ( \lambda )$ is divisible by $( \lambda - \lambda _ { 0 } ) ^ { \gamma _ { p } } + { \mathfrak { q } }$ but not by $( \lambda - \lambda _ { 0 } ) ^ { \gamma _ { p } } + g + 1$ ; and $i _ { r - 1 } ( \lambda )$ is divisible by $( \lambda - \lambda _ { 0 } ) ^ { \gamma _ { p } } + { \pmb q } - 1$ but not by $( \lambda - \lambda _ { 0 } ) ^ { \gamma _ { p + q - 1 } + 1 }$ ; and so on. It follows that the elementary divisors of

$$
\left[ \begin{array} { c c } { D _ { 1 } ( \lambda ) } & { \phantom { - } 0 } \\ { 0 } & { D _ { 2 } ( \lambda ) } \end{array} \right]
$$

(and therefore also those of $C ( \lambda ) )$ corresponding to $\lambda _ { 0 } )$ are just $( \lambda - \lambda _ { 0 } ) ^ { \gamma _ { 1 } }$ $\dots , ( \lambda - \lambda _ { 0 } ) ^ { \gamma _ { p } + q }$ , and the theorem is proved.■

Exercise 3. Determine the elementary divisors of the matrix

$$
\left[ \begin{array} { c c c c } { { \lambda - 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \lambda ^ { 2 } + 1 } } & { { \lambda ^ { 2 } + 1 } } \\ { { 0 } } & { { - 1 } } & { { \lambda _ { \sim } ^ { 2 } - 1 } } \end{array} \right]
$$

(a) over $\mathbb { C } ; ( \boldsymbol { \mathsf { b } } )$ over R.

Answers. (a) $\lambda - 1 , \lambda ^ { 2 } , \lambda - i , \lambda + i ; ( { \bf b } ) \lambda - 1 , \lambda ^ { 2 } , \lambda ^ { 2 } + 1 .$

Exercise 4. Let J be the Jordan block of order p associated with $\lambda _ { 0 }$

$$
J = \left[ { \begin{array} { c c c c c } { \lambda _ { 0 } } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \lambda _ { 0 } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { \lambda _ { 0 } } \end{array} } \right] .
$$

Show that the matrix $1 I - J$ has a unique elementary divisor $( \lambda - \lambda _ { 0 } ) ^ { p } .$

Exercise 5. Check that unimodular matrices, and only they, have no elementary divisors.

Exercise 6. Let $\ b { D } \in \mathbb { C } ^ { n \times n }$ be a diagonal matrix. Check that the elementary divisors of $\lambda I - D$ are linear.

Exercise 7. Verify that $( \lambda - \alpha _ { 0 } ) ^ { r }$ is the unique elementary divisor of the matrix polynomial $\lambda I - A ,$ , where

$$
A = \left[ \begin{array} { c c c c c } { \alpha _ { 0 } } & { \alpha _ { 1 } } & { \alpha _ { 2 } } & { \cdot \cdot \cdot } & { \alpha _ { r - 1 } } \\ { 0 } & { \alpha _ { 0 } } & { \alpha _ { 1 } } & { \cdot \cdot } & { \dot { \alpha _ { \cdot } } } \\ { \vdots } & { \cdot \ . } & { \cdot \cdot \cdot } & { \alpha _ { 2 } } \\ { 0 } & { \cdot \cdot \cdot } & { 0 } & { \alpha _ { 0 } } \end{array} \right]\tag{2}
$$

$( A \in \mathbb { C } ^ { r \times r } )$ and $\mathfrak { x } _ { 1 } \neq 0 .$

Hint. Observe that the minor of $\lambda I - A$ of order $r - 1$ obtained by striking out the first column and the last row is a nonzero number and, therefore, in the notation of Section 7.5, $d _ { 1 } = d _ { 2 } = \cdot \cdot \cdot = d _ { r - 1 } = 1$ and $d _ { r } ( \lambda ) = ( \lambda - \alpha _ { 0 } ) ^ { r }$

Exercise 8. Let $\pmb { A } \in \mathbb { C } ^ { r \times r }$ be defined by Eq. (2) and let $\alpha _ { 1 } = \alpha _ { 2 } = \cdots$ $= \alpha _ { l - 1 } = 0 , \alpha _ { l } \neq 0 ( 1 \leq l \leq r - 1 )$ . Verify that

$$
l _ { s } \triangleq \dim ( \operatorname { K e r } ( \alpha _ { 0 } I - A ) ^ { s } ) = { \left\{ \begin{array} { l l } { l s } & { { \mathrm { i f } } \quad l s \leq r } \\ { r } & { { \mathrm { i f } } \quad l s > r } \end{array} \right. }\tag{a}
$$

or, equivalently,

$$
l _ { 1 } = l , l _ { 2 } = 2 l , . . . , l _ { p } = p l , l _ { p + i } = r , i \geq 1 ,\tag{b}
$$

where $p = [ r / l ]$ , the integer part of $r / l .$

(c) The elementary divisors of $\lambda I - A$ are

$$
\underbrace { ( \lambda - \alpha _ { 0 } ) ^ { p } , \ldots , ( \lambda - \alpha _ { 0 } ) ^ { p } } _ { l \mathrm { ~ - ~ } q \mathrm { ~ t i m e s ~ } } , \underbrace { ( \lambda - \alpha _ { 0 } ) ^ { p + 1 } , \ldots , ( \lambda - \alpha _ { 0 } ) ^ { p + 1 } } _ { q \mathrm { ~ t i m e s ~ } } ,
$$

where the integers $p$ and $q$ satisfy the condition $r = p l + q ( 0 \leq q \leq l - 1$ $p > 0 )$

Hint. For part (c) use part (b) and Exercise 6.4.2 to obtain $k _ { 1 } = \cdots =$ $k _ { p ^ { - 1 } } = 0 , k _ { p } = l - q , k _ { p + 1 } = q$ (in the notation of Exercise 6.4.2). Also, observe that in view of Èxercise 4, the number $k _ { m }$ gives the number of elementary divisors $( \lambda - \lambda _ { 0 } ) ^ { m }$ of $A .$

Exercise 9. Let λ be an eigenvalue of $\pmb { A } \in \mathbb { C } ^ { n \times n }$ . Show that the index of λ is equal to the maximal degree of the elementary divisors of $\lambda I - A$ associated with λ. □

## 7.8 The Second Normal Form and the Jordan Normal Form

Let $A \in \mathbb { C } ^ { n \times n }$ and let $l _ { 1 } ( \lambda ) , l _ { 2 } ( \lambda ) , \dots , l _ { p } ( \lambda )$ denote the elementary divisors of the matrix $\lambda I - A$

Theorem 1 (The second natural normal form). With the notation of the previous paragraph, the matrix A is similar to the block-diagonal matrix

$$
C _ { 2 } = \mathrm { d i a g } [ C _ { l _ { 1 } } , C _ { l _ { 2 } } , . . . , C _ { l _ { p } } ] ,\tag{1}
$$

where $C _ { l _ { k } } \ ( 1 \le k \le p )$ denotes the companion matrix associated with the polynomial $l _ { k } ( \lambda )$

PRooF. By Exercise 7.5.4 the only nonconstant invariant polynomial of the matrix $\mathcal { U } \sim C _ { \iota _ { k } }$ is $l _ { k } ( \lambda )$ . Since $l _ { k } ( \lambda )$ is an elementary divisor of $\lambda I - A$ over the field $\mathbb { C } ,$ it is a power of a linear polynomial in $\lambda ,$ and hence the unique elementary divisor of $\lambda I - C _ { l _ { k } }$ . Applying Theorem 7.7.2, it follows that the matrix $\lambda I - C _ { 2 }$ , in which $C _ { 2 }$ is defined in Eq. (1), has the same elementary divisors as $\lambda I - A$ . Proposition 7.7.1 now provides the similarity of A and $C _ { 2 }$

Exercise 1. Show that the first and second natural normal forms of the matrix

$$
\left[ { \begin{array} { r r r r } { 3 } & { - 1 } & { - 5 } & { 1 } \\ { 1 } & { 1 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { - 2 } & { - 1 } \\ { 0 } & { 0 } & { 1 } & { 0 } \end{array} } \right]
$$

are, respectively, the matrices

$$
\left[ \begin{array} { c c c c } { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \\ { { - 4 } } & { { - 4 } } & { { 3 } } & { { 2 } } \end{array} \right] \qquad \mathrm { a n d } \qquad \left[ \begin{array} { c c c c } { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { - 1 } } & { { - 2 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { - 4 } } & { { 4 } } \end{array} \right] . \quad \bigsqcup
$$

Note that in contrast to the first natural normal form, the second normal form is defined only up to the order of companion matrices associated with the elementary divisors. For instance, the matrix

$$
\left[ { \begin{array} { r r r r } { 0 } & { 1 } & { 0 } & { 0 } \\ { - 4 } & { 4 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { - 1 } & { - 2 } \end{array} } \right]
$$

is also a second natural normal form of the matrix in Exercise 1.

In the statement of Theorem 1, each elementary divisor has the form $l _ { j } ( \lambda ) = ( \lambda - \lambda _ { j } ) ^ { \alpha _ { j } }$ Observe also that there may be repetitions in the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { p }$ , and that $\sum _ { i = 1 } ^ { p } \alpha _ { i } = n$

Now we apply Theorem 1 to meet one of the declared objectives of this chapter, namely, the reduction of a matrix to the Jordan normal form.

Theorem 2 (Jordan normal form). $\ b { I f A } \in \mathbb { C } ^ { n \times n }$ and $\lambda I - A$ has t elementary divisors $( \lambda - \lambda _ { i } ) ^ { p _ { i } } , i = 1 , 2 , . . . , t ,$ then A is similar to the matrix

$$
\boldsymbol { J } = \operatorname { d i a g } [ J _ { 1 } , J _ { 2 } , \ldots , J _ { t } ] \in \mathbb { C } ^ { n \times n }
$$

where $J _ { i }$ is the $p _ { i } \times p _ { i }$ Jordan block corresponding to $( \lambda - \lambda _ { i } ) ^ { p _ { i } }$ for $i = 1$ $2 , \ldots , t ;$

$$
J _ { i } = \left[ { \begin{array} { c c c c c } { \lambda _ { i } } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \lambda _ { i } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \cdots } & { } & { 0 } & { \lambda _ { i } } \end{array} } \right] .
$$

PRoOF. By Exercise 7.7.4, the only elementary divisor of $\lambda I - J _ { i } \mathrm { i } \mathrm { s } ( \lambda - \lambda _ { i } ) ^ { p _ { i } }$ The same is true for the matrix $\lambda I - C _ { l _ { i } }$ , where $l _ { i }$ refers to $l _ { i } ( \lambda ) = ( \lambda - \lambda _ { i } ) ^ { p _ { i } }$ (see the proof of Theorem 1). Thus, the matrices $J _ { i }$ and $C _ { l _ { i } }$ are similar (by Proposition 7.7.1) as are the matrices J and $C _ { 2 }$ in Eq. (1) (see Theorem 7.7.1). It remains now to apply Theorem 1 to obtain the desired result.

Exercise 2. Show that the Jordan normal forms of the matrix discussed in Exercise 1 are

$$
\left[ { \begin{array} { r r r r } { - 1 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 2 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 2 } \end{array} } \right] \qquad { \mathrm { o r } } \qquad { \left[ { \begin{array} { r r r r } { 2 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { - 1 } \end{array} } \right] } . \quad \bigsqcup
$$

Corollary 1. A matrix $\ b { A } \in \mathbb { C } ^ { n \times n }$ is simple if and only if all the elementary divisors of $\lambda I - A$ are linear.

PRoOF. First, if A is simple then (Theorem 4.8.2') $A = P D P ^ { - 1 }$ , where det $P \neq 0$ and $D = \mathrm { d i a g } [ \lambda _ { 1 } , . . . , \lambda _ { n } ]$ . Hence $\lambda I - A = P ( \lambda I - D ) P ^ { - 1 }$ and the matrices $\lambda I - A$ and $\lambda I - D$ are equivalent. But the elementary divisors of D are linear (Exercise 7.7.6) and, therefore, so are those of $\lambda I - A$

Conversely, if all the elementary divisors of $\lambda I - A$ are linear, then all the Jordan blocks in the Jordan normal form are $1 \times 1$ matrices. Thus, A is similar to a diagonal matrix and therefore is simple.■

Exercise 3. Let A be a singular matrix. Show that rank A = rank $A ^ { 2 }$ if and only if the zero eigenvalue of A has only linear elementary divisors.

## 7.9 The Characteristic and Minimal Polynomials

In this section we continue our investigation of the relationships between the characteristic and minimal polynomials. This was begun in Chapter 6.

Let $\pmb { A } \in \mathcal { F } ^ { n \times n }$ and let $B ( \lambda ) = \operatorname { a d j } ( \lambda I - A )$ . As noted in Section 7.2, B(λ) is a monic polynomial over $\mathcal { F }$ of order n and degree $n - 1$ . Let $\delta ( \lambda )$ denote the (monic) greatest common divisor of the elements of $B ( \lambda )$ . If $c ( \lambda )$ and $m ( \lambda )$ denote, respectively, the characteristic and the minimal polynomials of $A _ { i }$ then we already know (see Theorem 6.2.1) that $c ( \lambda )$ is divisible by $m ( \lambda )$ It turns out that the quotient $c ( \lambda ) / m ( \lambda )$ is simply the polynomial $\delta ( \lambda )$ just defined.

Theorem 1. With the notation of the previous paragraph,

$$
\begin{array} { r } { c ( \lambda ) = \delta ( \lambda ) m ( \lambda ) . } \end{array}\tag{1}
$$

ProoF. First, we introduce the matrix polynomial

$$
C ( \lambda ) = { \frac { 1 } { \delta ( \lambda ) } } B ( \lambda ) ,
$$

known as the reduced adjoint of $A ,$ and observe that the elements of $C ( \lambda )$ are relatively prime. In view of Eq. (7.2.1) we have $c ( \lambda ) I = \delta ( \lambda ) ( \lambda I - A ) C ( \lambda )$ This equation implies that $c ( \lambda )$ is divisible by $\delta ( \lambda )$ and, since both of them are monic, there exists a monic polynomial $\tilde { m } ( \lambda )$ such that $c ( \lambda ) = \delta ( \lambda ) \tilde { m } ( \lambda )$ . Thus

$$
\tilde { m } ( \lambda ) I = ( \lambda I - A ) C ( \lambda ) .\tag{2}
$$

Our aim is to show that $\tilde { m } ( \lambda ) = m ( \lambda )$ , that is, that $\tilde { m } ( \lambda )$ is the minimal polynomial of A. Indeed, the relation (2) shows that mñ(λ)I is divisible by $\lambda I - A$ and therefore, by the corollary to Theorem 7.2.3, $\tilde { m } ( A ) = O$ Thus, ñ(λ) is an annihilating polynomial of A and it remains to check that it is an annihilating polynomial for A of the least degree. To see this, suppose that $\tilde { m } ( \lambda ) = \theta ( \lambda ) m ( \lambda )$ . Since $m ( A ) = 0 ;$ , the same corollary yields

$$
m ( \lambda ) I = ( \lambda I - A ) \tilde { C } ( \lambda )
$$

for some matrix polynomial $\widetilde { C } ( \lambda )$ , and hence

$$
\tilde { m } ( \lambda ) I = ( \lambda I - A ) \theta ( \lambda ) \tilde { C } ( \lambda ) .
$$

Comparing this with $\mathbf { E q } . ( 2 )$ and recalling the uniqueness of the left quotient, we deduce that $C ( \lambda ) = \theta ( \lambda ) \widetilde C ( \lambda )$ . But this would mean $( \mathrm { i f } \theta ( \lambda ) \not \equiv 1 )$ that $\theta ( \lambda )$ is a common divisor of the elements of $C ( \lambda )$ , which contradicts the definition of δ(λ). Thus $\theta ( \lambda ) \equiv 1$ and $\tilde { m } ( \lambda ) = m ( \lambda )$

This result implies another useful description of the minimal polynomial.

Theorem 2. The minimal polynomial of a matrix $A \in { \mathcal { F } } ^ { n \times n }$ coincides with the invariant polynomial of $\lambda I - A$ of highest degree.

PROOF. Note that $\lambda I - A$ has rank n and that by Proposition 7.3.1 and Theorem 7.5.1,

$$
\operatorname* { d e t } ( \lambda I - A ) = \alpha i _ { 1 } ( \lambda ) i _ { 2 } ( \lambda ) \cdot \cdot \cdot i _ { n } ( \lambda ) ,\tag{3}
$$

in which none of $i _ { 1 } ( \lambda ) , \ldots , i _ { n } ( \lambda )$ is identically zero.

Also, $\alpha = 1$ since the invariant polynomials, as well as $\operatorname* { d e t } ( \lambda I - A )$ , are monic. Recalling Eq. (7.5.3), we deduce from Eq. (3) that

$$
c ( \lambda ) = \operatorname * { d e t } ( \lambda I - A ) = d _ { n - 1 } ( \lambda ) i _ { n } ( \lambda ) ,\tag{4}
$$

in which $d _ { n - 1 } ( \lambda )$ is the (monic) greatest common divisor of the minors of $\lambda I - A$ of order $n - 1 \mathrm { o r }$ , equivalently, the greatest common divisor of the elements of the adjoint matrix $B ( \lambda )$ of $A ( \lambda )$ . Thus, $d _ { n - 1 } ( \lambda ) = \delta ( \lambda )$ , where $\delta ( \lambda )$ is defined in the proof of Theorem 1. This yields $i _ { n } ( \lambda ) = m ( \lambda )$ on comparison of Eqs. (4) and (1).■

Now we can give an independent proof of the result obtained in Proposition 6.6.2.

Corollary 1. A matrix $A \in \mathbb { C } ^ { n \times n }$ is simple if and only if its minimal polynomial has only simple zeros.

ProoF. By Corollary 7.8.1, A is simple if and only if all the elementary divisors of $\lambda I - A$ are linear, that is, if and only if the invariant polynomial $\begin{array} { r } { i _ { n } ( \lambda ) = \prod _ { i = 1 } ^ { s } { ( \lambda - \lambda _ { i } ) } . } \end{array}$ where $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ are the distinct eigenvalues of A. The result follows immediately from Theorem 2.

Corollary 2. A matrix $A \in { \mathcal { F } } ^ { n \times n }$ is nonderogatory if and only if the $n - 1$ frst invariant polynomials of $\lambda I - A$ are of degree zero, that is, they are identically equal to 1.

ProoF. Let A be nonderogatory and let $i _ { 1 } ( \lambda ) , i _ { 2 } ( \lambda ) , . . . , i _ { n } ( \lambda )$ denote the invariant polynomials of $\lambda I - A . \ \mathrm { I f } \ c ( \lambda )$ is a characteristic polynomial of A then $\begin{array} { r } { c ( \lambda ) = \prod _ { k = 1 } ^ { n } i _ { k } ( \lambda ) } \end{array}$ , and by assumption $c ( \lambda )$ coincides with the minimal polynomial $m ( \lambda )$ of A. But by Theorem 2, $m ( \lambda ) = i _ { n } ( \lambda )$ and therefore the comparison gives $i _ { 1 } ( \lambda ) = \cdot \cdot \cdot = i _ { n - 1 } ( \lambda ) = 1$ Note that there are no zero invariant polynomials of λI — A since it is a regular matrix polynomial.

Now we show that the second natural normal form of Theorem 7.8.1 (as well as the Jordan form that is a consequence of it) is the best in the sense that no block $C _ { l _ { k } } , k = 1 , 2 , \ldots , p ,$ in Eq. (7.8.1) can be split into smaller blocks. More precisely, it will be shown that $C _ { l _ { k } }$ cannot be similar to a block-diagonal matrix (of more than one block). To see this, we first define a matrix $A \in { \mathcal { F } } ^ { n \times n }$ to be decomposable if it is similar to a block-diagonal matrix diag $[ A _ { 1 } , A _ { 2 } ]$ where $\ b { A _ { 1 } } \in \mathbb { C } ^ { n _ { 1 } \times n _ { 1 } } , \ b { A _ { 2 } } \in \mathbb { C } ^ { n _ { 2 } \times n _ { 2 } }$ , and $n _ { 1 } , n _ { 2 } > 0 , n _ { 1 } + n _ { 2 } = n .$ Otherwise, the matrix is said to be indecomposable.

Proposition 1. A matrix $A \in \mathbb { C } ^ { n \times n }$ is indecomposable if and only if it is nonderogatory and its characteristic polynomial $c ( \lambda )$ is of the form $( \lambda - \lambda _ { 0 } ) ^ { p }$ for some $\lambda _ { 0 } \in \mathbb { C }$ and positive integer p.

ProoF. Let A be indecomposable. If it is derogatory, then by Corollary 2 the matrix polynomial $\lambda I - A$ has at least two nonconstant invariant polynomials. Now Theorem 7.6.2 shows that A is decomposable, which is a contradiction. If the characteristic polynomial $c ( \lambda )$ has two or more distinct zeros, then $\lambda I - A$ has at least two elementary divisors. Theorem 7.8.1 then states that again A is decomposable.

Conversely, if A is nonderogatory and $c ( \lambda ) = ( \lambda - \lambda _ { 0 } ) ^ { p } ,$ , then A must be indecomposable. Indeed, these conditions imply, repeating the previous argument, that $\lambda I - A$ has only one elementary divisor. Since a matrix B is decomposable only if the matrix $\lambda I - B$ has at least two elementary divisors, the result follows.

Corollary 1. The matrices $C _ { l _ { k } } \left( k = 1 , 2 , \ldots , s \right)$ in Eq. (7.8.1) are indecomposable.

The proof relies on the fact that a companion matrix is nonderogatory (Exercise 6.6.3) and on the form of its characteristic polynomial (see Exercise 4.11.3).

## Corollary 2. Jordan blocks are indecomposable matrices.

To prove this see Exercises 6.6.2 and 7.7.4. Thus, these forms cannot be reduced further and are the best in this sense.

Exercise 1. The proof of Theorem 1 above [see especially Eq. (2)] shows that the reduced adjoint matrix C(λ) satisfies

$$
( \lambda I - A ) C ( \lambda ) = m ( \lambda ) I .
$$

Use this relation to show that if $\lambda _ { 0 }$ is an eigenvalue of A, then all nonzero columns of $C ( \lambda _ { 0 } )$ are eigenvectors of A corresponding to $\lambda _ { 0 }$ . Obtain an analogous result for the adjoint matrix $B ( \lambda _ { 0 } )$ 口

## 7.10 The Smith Form: Differential and Difference Equations

In this section an important application of the Smith normal form is made to the analysis of differential and difference equations. Consider first a set of n homogeneous scalar differential equations with constant complex coefficients in n scalar variables $x _ { 1 } ( t ) , \ldots , x _ { n } ( t )$ . Define ${ \boldsymbol x } ( t )$ by

$$
\mathbf { \boldsymbol { \mathbf { \mathit { x } } } } ( t ) = [ \mathbf { \boldsymbol { \mathbf { \mathit { x } } } } _ { 1 } ( t ) \quad \cdot \cdot \cdot \quad \mathbf { \boldsymbol { \mathbf { \mathit { x } } } } _ { n } ( t ) ] ^ { \mathbf { \mathit { T } } }
$$

and let l be the maximal order of derivatives in the n equations. Then the equations can be written in the form

$$
L _ { l } x ^ { ( l ) } ( t ) + L _ { l - 1 } x ^ { ( l - 1 ) } ( t ) + \cdots + L _ { 1 } x ^ { ( 1 ) } ( t ) + L _ { 0 } x ( t ) = 0\tag{1}
$$

for certain matrices $L _ { 0 } , L _ { 1 } , \ldots , L _ { l } \in \mathbb { C } ^ { n \times n }$ , where $L _ { \imath } \neq 0$ and the indices on the vector $x ( t )$ denote componentwise derivatives.

Let $\mathcal C ( \mathbb C ^ { n } )$ be the set of all continuous vector-valued functions $\mathbf { \boldsymbol { y } } ( t )$ defined for all real t with values in $\mathbb { C } ^ { n }$ Thus $\mathbf { \boldsymbol { \mathbf { \mathit { y } } } } ( t ) = [ \boldsymbol { \mathbf { \mathit { y } } } _ { 1 } ( t ) \quad \cdots \quad \boldsymbol { \mathbf { \mathit { y } } } _ { n } ( t ) ] ^ { \mathbf { \boldsymbol { \mathbf { I } } } }$ and $y _ { 1 } ( t ) , \ldots , y _ { n } ( t )$ are continuous for all real t. With the natural definitions of vector addition and scalar multiplication, $\mathcal { C } ( \mathbb { C } ^ { n } )$ is obviously a (infinitedimensional) linear space.

Here and in subsequent chapters we will investigate the nature of the solution space of Eq. (1), and our first observation is that every solution is a member of ${ \mathcal { C } } ( \mathbb { C } ^ { n } )$ . Then it is easily verified that the solution set is, in fact, a linear subspace of ${ \mathcal { C } } ( \mathbb { C } ^ { n } )$ . In this section, we examine the dimension of this subspace.

The matrix polynomial $\begin{array} { r } { L ( \lambda ) = \sum _ { j = 0 } ^ { l } \lambda ^ { j } L _ { j } } \end{array}$ is associated with Eq. (1), which can be abbreviated to the form $L ( d / d t ) x ( t ) = 0$ . Thus,

$$
L \bigg ( \frac { d } { d t } \bigg ) \pmb { x } ( t ) \triangleq \sum _ { j = 0 } ^ { l } L _ { j } \frac { d ^ { j } \pmb { x } } { d t ^ { j } } .
$$

To illustrate, if

$$
L ( \lambda ) = { \left[ \begin{array} { l l } { \lambda ^ { 2 } } & { 2 } \\ { \lambda - 1 } & { \lambda ^ { 2 } } \end{array} \right] } \qquad \mathrm { a n d } \qquad \pmb { x } ( t ) = { \left[ \begin{array} { l } { x _ { 1 } ( t ) } \\ { x _ { 2 } ( t ) } \end{array} \right] } \in \mathcal { C } ( \mathbb { C } ^ { 2 } ) ,
$$

and, in addition, $x _ { 1 } ( t )$ and $x _ { 2 } ( t )$ are twice differentiable, then

$$
L \bigg ( \frac { d } { d t } \bigg ) x ( t ) = \bigg [ \begin{array} { c } { x _ { 1 } ^ { ( 2 ) } ( t ) + 2 x _ { 2 } ( t ) } \\ { x _ { 1 } ^ { ( 1 ) } ( t ) - x _ { 1 } ( t ) + x _ { 2 } ^ { ( 2 ) } ( t ) \bigg ] . } \end{array}
$$

Exercise 1. Let $L _ { 1 } ( \lambda ) , L _ { 2 } ( \lambda )$ be $n \times n$ matrix polynomials and

$$
L ( \lambda ) = L _ { 1 } ( \lambda ) L _ { 2 } ( \lambda ) .
$$

Show that

$$
L \bigg ( \frac { d } { d t } \bigg ) x ( t ) = L _ { 1 } \bigg ( \frac { d } { d t } \bigg ) \bigg ( L _ { 2 } \bigg ( \frac { d } { d t } \bigg ) x ( t ) \bigg ) . \quad \bigsqcup
$$

With these conventions and the Smith normal form, we can now establish the dimension of the solution space of Eq. (1) as a subspace of $\mathcal { C } ( \mathbb { C } ^ { n } )$ . This result is sometimes known as Chrystal's theorem. The proof is based on the well-known fact that a scalar differential equation of the form (1) with order / has a solution space of dimension l.

Theorem 1 (G. Chrystal†). If det $L ( \lambda ) \not \equiv 0$ then the solution space of Eq. (1) has dimension equal to the degree of det $L ( \lambda )$

PROOF. Since det $L ( \lambda ) \not \equiv 0 .$ the Smith canonical form of $L ( \lambda )$ (see Section 7.5) is of the form $D ( \boldsymbol { \lambda } ) = \mathrm { d i a g } [ i _ { 1 } ( \boldsymbol { \lambda } ) , i _ { 2 } ( \boldsymbol { \lambda } ) , \ldots , i _ { n } ( \boldsymbol { \lambda } ) ]$ , where $i _ { 1 } ( \lambda ) , i _ { 2 } ( \lambda ) , \dots , i _ { n } ( \lambda )$ are the nonzero invariant polynomials of $L ( \lambda )$ . Thus, by Theorem 7.5.1,

$$
L ( \lambda ) = P ( \lambda ) D ( \lambda ) Q ( \lambda )\tag{2}
$$

for some unimodular matrix polynomials $P ( \lambda )$ and Q(λ). Applying the result of Exercise 1. we may rewrite Eq. (1) in the form

$$
P \bigg ( \frac { d } { d t } \bigg ) D \bigg ( \frac { d } { d t } \bigg ) Q \bigg ( \frac { d } { d t } \bigg ) \pmb { x } ( t ) = 0 .\tag{3}
$$

Let $\mathbf { y } ( t ) = Q ( d d t ) \mathbf { x } ( t )$ and multiply Eq. (3) on the left by $P ^ { - 1 } ( d / d t )$ (recall that $P ^ { - 1 } ( \dot { A } )$ is a polynomial) to obtain the system

$$
\mathrm { d i a g } \bigg [ i _ { 1 } \bigg ( \frac { d } { d t } \bigg ) , i _ { 2 } \bigg ( \frac { d } { d t } \bigg ) , \ldots , i _ { n } \bigg ( \frac { d } { d t } \bigg ) \bigg ] y ( t ) = 0 ,\tag{4}
$$

which is equivalent to Eq. (1). Clearly, the system in (4) splits into n independent scalar equations

$$
i _ { \bar { \boldsymbol { \imath } } } \left( { \frac { d } { d t } } \right) ! \rangle _ { k } ( t ) = 0 , \qquad k = 1 , 2 , \ldots , n ,\tag{5}
$$

where $y _ { 1 } ( t ) , \ldots , \mathbf { i } _ { n } ( t )$ are the components of $y ( t )$ . But the scalar differential equation $a ( d , d t ) \} \forall \{ t \} = 0$ has exactly $d = \deg a ( \lambda )$ linearly independent solutions. Apply this result to each of the equations in (5) and observe that the number of linearly independent vector-valued functions $y ( t )$ satisfying Eq. (4) is equal to the sum of the numbers of linearly independent solutions of the system (5). Thus the dimension of the solution space of Eq. (3) is $d _ { 1 } + d _ { 2 } + \cdots + d _ { n }$ . where $d _ { \pm } = \deg i _ { k } ( \lambda ) , 1 \le k \le n .$ On the other hand, Eq. (2) shows that

$$
\operatorname * { d e t } L ( \zeta . ) = x \operatorname * { d e t } D ( \lambda ) = \propto \prod _ { k = 1 } ^ { n } i _ { k } ( \lambda ) ,
$$

where α = det P(λ)Q(λ). Since x is a nonzero constant, it follows that

$$
\deg ( \operatorname* { d e t } L ( \lambda ) ) = \sum _ { k = 1 } ^ { n } \deg i _ { k } ( \lambda ) = d _ { 1 } + d _ { 2 } + + \cdot \cdot \cdot + d _ { n } .
$$

The equivalence of the systems (4) and (1) in the sense that

$$
x ( t ) = Q ^ { - 1 } \biggl ( \frac { d } { d t } \biggr ) y ( t )
$$

now gives the required result.

The following special cases arise frequently: if det $L _ { l } \neq \mathbf { 0 }$ and, in particular, if $L ( \lambda )$ is monic, then the solution space of Eq. (1) has dimension ln. This follows immediately from the obvious fact that the leading coefficient of det $L ( \lambda )$ is just det $L _ { l }$ . One special case is so important that it justifies a separate formulation:

Corollary 1. If $A \in \mathbb { C } ^ { n \times n }$ then the solution space of ${ \dot { \mathbf { x } } } ( t ) = A { \mathbf { x } } ( t )$ has dimension n.

We turn now to the study of a set of n homogeneous scalar difference equations with constant complex coefficients and order l. Such a system can be written in matrix form as

$$
L _ { l } { \bf { \Psi } } _ { l } + L _ { l - 1 } { \bf { \Psi } } _ { x _ { j + l - 1 } } + \cdot \cdot \cdot + L _ { 1 } { \bf { \Psi } } _ { x _ { j + 1 } } + L _ { 0 } { \bf { \Psi } } _ { x _ { j } } = 0\tag{6}
$$

for $j = 0 , 1 , 2 , \ldots$ where $L _ { 0 } , L _ { 1 } , \dots , L _ { l } \in \mathbb { C } ^ { n \times n } \left( L _ { l } \neq O \right)$ , and a solution is a sequence of vectors $( { \pmb x } _ { 0 } , { \pmb x } _ { 1 } , { \pmb x } _ { 2 } , \ldots )$ for which all the relations (6) hold with $j = 0 , 1 , 2 , \ldots$ . In this case, we introduce the linear space ${ \mathcal { S } } ( \mathbb { C } ^ { n } )$ consisting of all infinite sequences of vectors from $\mathbb { C } ^ { n } .$ , and with the natural componentwise definitions of vector addition and scalar multiplication. Then it is easily verified that the solution set of (6) is a subspace of ${ \mathcal { S } } ( \mathbb { C } ^ { n } )$

It will be convenient to introduce a transformation E acting on ${ \mathcal { S } } ( \mathbb { C } ^ { n } )$ defined by

$$
E ( \boldsymbol { u } _ { 0 } , \boldsymbol { u } _ { 1 } , \ldots ) = ( \boldsymbol { u } _ { 1 } , \boldsymbol { u } _ { 2 } , \ldots )
$$

for any. $( \pmb { u } _ { 0 } , \pmb { u } _ { 1 } , . . . ) \in \mathcal { S } ( \mathbb { C } ^ { n } )$ . It is clear that E is linear. It is called a shift operator and will be seen to play a role for difference equations analogous to that played by $d / d t$ for differential equations.

For $r = 1 , 2 , 3 , \ldots ,$ the powers of $E$ are defined recursively by

$$
E ^ { r } u = E ( E ^ { r - 1 } u ) , \qquad r = 1 , 2 , \ldots , \qquad u \in { \mathcal { S } } ( \mathbb { C } ^ { n } ) ,
$$

where $E ^ { 0 }$ is the identity of ${ \mathcal { S } } ( \mathbb { C } ^ { n } )$ . Consequently,

$$
E ^ { r } ( u _ { 0 } , u _ { 1 } , . . . ) = ( u _ { r } , u _ { r + 1 } , . . . ) .
$$

Also, if $\ b { A } \in \mathbb { C } ^ { n \times n }$ and $( \pmb { u } _ { 0 } , \pmb { u } _ { 1 } , \dots ) \in \mathcal { S } ( \mathbb { C } ^ { n } )$ , we define

$$
A ( \boldsymbol { u } _ { 0 } , \boldsymbol { u } _ { 1 } , \ldots ) \triangleq ( A \boldsymbol { u } _ { 0 } , A \boldsymbol { u } _ { 1 } , \ldots ) \in \mathcal { S } ( \mathbb { C } ^ { n } ) .
$$

Then it is easily verified that, if we write ${ \pmb x } = ( { \pmb x } _ { 0 } , { \pmb x } _ { 1 } , \dots )$ , Eq. (6) can be written in the form

$$
L ( E ) \pmb { x } \triangleq L _ { l } ( E ^ { l } \pmb { x } ) + \cdots + L _ { 1 } ( E \pmb { x } ) + L _ { 0 } \pmb { x } = 0 ,\tag{7}
$$

where the zero on the right side of Eq. (7) is the zero element of ${ \mathcal { S } } ( \mathbb { C } ^ { n } )$

Another illuminating way to see Eq. (6) is as an equation in infinite vectors and matrices. For simplicity, consider the case $l = 2$

$$
{ \left[ \begin{array} { l l l l l } { L _ { 0 } } & { L _ { 1 } } & { L _ { 2 } } & { 0 } & { \cdots } \\ { 0 } & { L _ { 0 } } & { L _ { 1 } } & { L _ { 2 } } & { \cdots } \\ { 0 } & { 0 } & { L _ { 0 } } & { L _ { 1 } } & { \cdots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 0 } } \\ { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \end{array} \right] } = { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { 0 } \\ { \vdots } \end{array} \right] } .
$$

Theorem 2. If det $L ( \lambda ) \not \equiv 0 ,$ then the dimension of the solution space of $E q$ (6) is equal to the degree of det $L ( \lambda )$

PRooF. Using the decomposition (2), reduce Eq. (7) to the equivalent form

$$
D ( E ) \mathbf { y } = \pmb { \theta } ,\tag{8}
$$

where $y = Q ( E ) x$ and $0 , x , y \in { \mathcal { S } } ( \mathbb { C } ^ { n } )$ . Observe that Eq. (8) splits into n independent scalar equations. Since the assertion of the theorem holds true for scalar difference equations, it remains to apply the argument used in the proof of Theorem 1.

Corollary 2. If $A \in \mathbb { C } ^ { n \times n } ,$ , then the solution space of the recurrence relation

$$
x _ { j + 1 } = A x _ { j } , \qquad j = 0 , 1 , 2 , \ldots ,
$$

has dimension n.

## 7.11 Miscellaneous Exercises

1. Let $\ b { A } \in \mathbb { C } ^ { 1 0 \times 1 0 }$ and suppose the invariant polynomials of $\lambda I - A$ are $i _ { 1 } ( \lambda ) = \cdots = i _ { 7 } ( \lambda ) = 1 , i _ { 8 } ( \lambda ) = \lambda + 1 , i _ { 9 } ( \lambda ) = \lambda ^ { 3 } + 1 , i _ { 1 0 } ( \lambda ) = ( \lambda ^ { 3 } + 1 ) ^ { 2 }$ Check that the first and second natural normal forms and the Jordan normal form of A are, respectively,

$$
C _ { 1 } = \mathrm { d i a g } \left[ - 1 , \left[ \begin{array} { r r r } { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { - 1 } & { 0 } & { 0 } \end{array} \right] , \left[ \begin{array} { r r r r r r } { 0 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { - 1 } & { 0 } & { 0 } & { - 2 } & { 0 } & { 0 } \end{array} \right] \right] ,
$$

$$
\begin{array} { c }  { C _ { 2 } = \mathrm { d i a g } \biggl [ - 1 , - 1 , [ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - 1 } } & { { - 2 } } \end{array} ] , \mu _ { 2 } , [ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - \mu _ { 2 } ^ { 2 } } } & { { 2 \mu _ { 2 } \biggl ] , \mu _ { 3 } , [ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - \mu _ { 3 } ^ { 2 } } } & { { 2 \mu _ { 3 } \biggr ] } \biggr ] , } } \end{array} ] , } } \\  { J = \mathrm { d i a g } \biggl [ - 1 , - 1 , [ \begin{array} { c c } { { - 1 } } & { { 1 } } \\ { { 0 } } & { { - 1 } } \end{array} ] , \mu _ { 2 } , [ \begin{array} { c c } { { \mu _ { 2 } } } & { { 1 } } \\ { { 0 } } & { { \mu _ { 2 } \biggl ] , \mu _ { 3 } , [ \begin{array} { c c } { { \mu _ { 3 } } } & { { 1 } } \\ { { 0 } } & { { \mu _ { 3 } \biggr ] } } \end{array} ] \biggr ] , } } } \end{array} \end{array} \end{array}
$$

where

$$
\mu _ { 2 } = \frac { ( 1 + \sqrt { 3 } i ) } { 2 } , \mu _ { 3 } = \frac { ( 1 - \sqrt { 3 } i ) } { 2 } .
$$

2. If $A ( \lambda ) , B ( \lambda ) , D ( \lambda )$ are matrix polynomials of size n, and $A ( \lambda ) ,$ and $B ( \lambda )$ have invertible leading coefficients and degrees l and $m ,$ respectively, show that the degree of $A ( \lambda ) D ( \lambda ) B ( \lambda )$ is not less than $l + m .$

3. Two $m \times n$ matrix polynomials $A ( \lambda )$ and $B ( \lambda )$ are said to be equivalent if there are unimodular matrices $P ( \lambda )$ of order m and $Q ( \lambda )$ of order n such that $B ( \lambda ) = P ( \lambda ) A ( \lambda ) Q ( \lambda )$ . Show that any $m \times n$ matrix polynomial is equivalent to a matrix polynomial of the form

$$
\left[ { \begin{array} { c c c c c c c } { a _ { 1 } ( \lambda ) } & { 0 } & { \cdots } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { a _ { 2 } ( \lambda ) } & { } & { } & { } & { } & { } \\ { \vdots } & { } & { \ddots } & { } & { \vdots } & { \vdots } & { } \\ { } & { \ddots } & { \ddots } & { } & { 0 } & { } & { } \\ { 0 } & { \cdots } & { 0 } & { a _ { m } ( \lambda ) } & { 0 } & { \cdots } & { 0 } \end{array} } \right]
$$

if $m \leq n ,$ or

$$
\left[ { \begin{array} { r r r r } { a _ { 1 } ( \lambda ) } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \cdots } & { \vdots } \\ & { \ddots } & { 0 } \\ { \vdots } & & { \ddots } & { a _ { n } ( \lambda ) } \\ & & { 0 } \\ & & { \vdots } \\ { 0 } & { \cdots } & { 0 } \end{array} } \right]
$$

if $m > n ,$ where $a _ { j } ( \lambda )$ is divisible by $a _ { j - 1 } ( \lambda ) , j \geq 2 .$

4. Show that if $A \in \mathbb { C } ^ { n \times n }$ is idempotent and $A \neq I , A \neq O ,$ then the minimal polynomial of A is $\lambda ^ { 2 } - \lambda$ and the characteristic polynomial has the form $( \lambda - 1 ) ^ { r } \lambda ^ { s }$ . Prove that A is similar to the matrix $\mathrm { d i a g } [ I _ { r } , O ]$

5. Prove that

(a) The geometric multiplicity of an eigenvalue is equal to the number of elementary divisors associated with it;

(b) The algebraic multiplicity of an eigenvalue is equal to the sum of degrees of all elementary divisors associated with it.

6. Define the multiplicity of a latent root $\lambda _ { 0 }$ of $A ( \lambda )$ as the number of times the factor $\lambda - \lambda _ { 0 }$ appears in the factorization of det $A ( \lambda )$ into linear factors.

Let $A ( \lambda )$ be a monic $n \times n$ matrix polynomial of degree l. Show that $A ( \lambda )$ has In latent roots (counted according to their multiplicities), and

that if the In latent roots are distinct, then all the elementary divisors of $A ( \lambda )$ are linear.

7. If $\lambda _ { 0 }$ is a latent root of multiplicity α of the n × n matrix polynomial $A ( \lambda )$ prove that the elementary divisors of $A ( \lambda )$ associated with $\lambda _ { 0 }$ are all linear if and only if dim(Ker $\begin{array} { r } { A ( \lambda _ { 0 } ) ) = \alpha . } \end{array}$

8. If $m ( \lambda )$ is the minimal polynomial of $\pmb { A } \in \mathbb { C } ^ { n \times n }$ and $f ( \lambda )$ is a polynomial over $\mathbb { C } ,$ prove that $f ( A )$ is nonsingular if and only if $m ( \lambda )$ and $f ( \lambda )$ are relatively prime.

9. Let A(λ) be a matrix polynomial and define a vector $\pmb { x } \neq \pmb { \theta }$ to be a latent vector of A(λ) associated with $\lambda _ { 0 }$ if $A ( \lambda _ { 0 } ) \mathbf { x } = \pmb { 0 }$

If $A ( \lambda ) = A _ { 0 } + \lambda A _ { 1 } + \lambda ^ { 2 } A _ { 2 }$ (det $A _ { 2 } \neq 0 )$ is an $n \times n$ matrix polynomial, prove that x is a latent vector of $A ( \lambda )$ associated with $\lambda _ { 0 }$ if and only if

$$
{ \biggl ( } \lambda _ { 0 } { \binom { A _ { 2 } } { A _ { 1 } } } \quad 0 { \biggr ] } + { \biggl [ } { \begin{array} { c c } { 0 } & { - A _ { 2 } } \\ { A _ { 0 } } & { 0 } \end{array} } { \biggr ] } { \biggr ) } { \biggl [ } \lambda _ { 0 } \mathbf { x } _ { 0 } { \biggr ] } = 0 .
$$

Generalise this result for matrix polynomials with invertible leading coefficients of general degree.

10. Let $A ( \lambda )$ be an $n \times n$ matrix polynomial with latent roots $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ and suppose that there exist linearly independent latent vectors $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ of $A ( \lambda )$ associated with $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ , respectively. Prove that if $X = [ \pmb { x } _ { 1 } \quad \pmb { x } _ { 2 } \quad \cdots \quad \pmb { x } _ { n } ]$ and $D = \mathrm { d i a g } [ \lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n } ]$ then $S = X D X ^ { - 1 }$ is a right solvent of $A ( \lambda )$

11. Let the matrix $A \in \mathbb { C } ^ { n \times n }$ have distinct eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { s }$ and suppose that the maximal degree of the elementary divisors associated with $\lambda _ { k } \left( 1 \leq k \leq s \right)$ is ${ \pmb { m } } _ { { \pmb { k } } }$ (the index of $\lambda _ { k } )$ . Prove that

$$
\mathbb { C } ^ { n } = \sum _ { k = 1 } ^ { s } \cdot \operatorname { K e r } ( \lambda _ { k } I - A ) ^ { m _ { k } } .
$$

12. Prove that if $\ b X \in \mathbb { C } ^ { n \times n }$ is a solvent of the n × n matrix polynomial $A ( \lambda )$ then each eigenvalue of X is a latent root of $A ( \lambda )$

Hint. Use the Corollary to Theorem 7.2.3.

13. Consider a matrix polynomial $\begin{array} { r } { A ( \lambda ) = \sum _ { j = 0 } ^ { l } \lambda ^ { j } A _ { j } } \end{array}$ with det $A _ { l } \neq 0$ , and define its companion matrix

$$
C _ { A } \triangleq \left[ \begin{array} { l l l l l } { 0 } & { I _ { n } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { I _ { n } } & { \ddots } & { \vdots } \\ { \vdots } & { \vdots } & { } & { \ddots } & { 0 } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { I _ { n } } \\ { - \hat { A } _ { 0 } } & { - \hat { A } _ { 1 } } & { \cdots } & { - \hat { A } _ { l - 1 } } \end{array} \right] ,
$$

where $\hat { A } _ { j } = A _ { l } ^ { - 1 } A _ { j } , j = 0 , 1 , \ldots , l - 1$ . Show that $\lambda _ { 0 }$ is a latent root of $A ( \lambda )$ if and only if it is an eigenvalue of $C _ { A }$

14. Let $\ b { X _ { 1 } } , \ b { X _ { 2 } } , \dotsc , \ b { X _ { \ell } } \in \mathbb { C } ^ { n \times n }$ be right solvents of the $n \times n$ matrix polynomial $A ( \lambda )$ . Show that, with $C _ { A }$ defined as in Exercise 13,

(a) $C _ { A } V = V { \mathrm { d i a g } } [ X _ { 1 } , X _ { 2 } , \ldots , X _ { l } ]$ , where V denotes the generalized Vandermonde matrix

$$
V = \left[ \begin{array} { c c c c } { I _ { n } } & { I _ { n } } & { \cdots } & { I _ { n } } \\ { X _ { 1 } } & { X _ { 2 } } & { \cdots } & { X _ { l } } \\ { \vdots } & { \vdots } & { } & { \vdots } \\ { X _ { 1 } ^ { l - 1 } } & { X _ { 2 } ^ { l - 1 } } & { \cdots } & { X _ { l } ^ { l - 1 } } \end{array} \right] ,
$$

(b) If V is invertible then the spectrum of $A ( \lambda ) { \mathrm { ~ } } ( { \mathrm { i } } . { \mathsf { e } } _ { \cdot } ,$ the set of all its latent roots) is the union of the eigenvalues of $X _ { 1 } , X _ { 2 } , \ldots , X _ { l }$

(c) $C _ { A }$ is similar to diag $[ X _ { 1 } , X _ { 2 } , \ldots , X _ { l } ]$ if and only if the set of all elementary divisors of $C _ { A }$ coincides with the union of the elementary divisors of $X _ { 1 } , X _ { 2 } , \ldots , X _ { l }$

## The Variational Method

The technique developed in this chapter can be visualized as the generalization of a geometrical approach to the eigenvalue problem for $3 \times 3$ real symmetric matrices. We saw in Exercise 5.10.5 that a quadric surface can be associated with such a matrix H by means of the equation $x ^ { \mathsf { T } } H x = 1$ or $( H \pmb { x } , \pmb { x } ) = 1$ , where $\mathbf { x } \in \mathbb { R } ^ { 3 }$ . In particular (see Exercise 5.10.6), if H is positive definite, then the corresponding surface is an ellipsoid. The vector $\vert \pmb { x _ { 0 } } \in \mathbb { R } ^ { 3 }$ from the origin to the farthest point on the ellipsoid can then be described as a vector at which $( { \pmb x } , { \pmb x } )$ attains the maximal value subject to the condition that x satisfies $( H \pmb { x } , \pmb { x } ) = 1$

Then the problem can be reformulated and the side condition eliminated by asking for the maximal value of the quotient $( { \pmb x } , { \pmb x } ) / ( H { \pmb x } , { \pmb x } )$ , where x varies over all nonzero vectors in $\mathbb { R } ^ { 3 }$ . Or, what is essentially the same thing, we seek the minimal value of the Rayleigh quotient:

$$
{ \frac { ( H x , \ x ) } { ( x , \ x ) } } , \qquad x \neq \theta .
$$

Now, this quotient makes sense for any n × n Hermitian matrix H and vector $\pmb { x } \in \mathbb { C } ^ { n }$ and is also known in this more general context as the Rayleigh quotient for H. The study of its properties in this context is one of the main subjects of this chapter.