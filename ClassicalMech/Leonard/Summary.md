# Summary for Lagrange Mechanics

## Generalized Coordinates

Any system can be described by **at least** \(f\) real numbers, they are `generalized coordinates` .

1.  **Free particle in 3D space**

    Such the particle can be described by \(3\) coordinates in Cartesian system:

    $$q = (x^1, x^2, x^3) \sim x^1 \bm{e}_1 + x^2 \bm{e}_2 + x^3 \bm{e}_3$$

2.  **Particle constraint on a sphere**

    Same as 1, Cartesian coordinates can describe the particle : \((x^1,x^2,x^3)\) , but there is a constraint:

    $$(x^1)^2 + (x^2)^2 + (x^3)^2 = 1$$

    So \(f=2\) , one can use spherical coordinates:

    $$q = (\theta, \phi)$$

    Where

    $$x^1 = \sin\theta \cos \phi \ ; \ x^2 = \sin\theta \sin \phi \ ; \ x^3 = \cos\theta$$

3.  **Particles on a generic constraint**

    Consider there are \(3N\) Cartesian coordinates to describe \(N\) particles. And there are \(s\) (ideal) constraint equations:

    $$f^i (q^1,\cdots,q^{3N}) = 0 \ ; \ i=1,\cdots,s$$

    With the [theorem for implicit function](https://en.wikipedia.org/wiki/Implicit_function_theorem), at any point \(q_0\), if the Jacobian (a \(s\times 3N\) matrix):

    $$J_{ki} = \partial_k f^i (q_0)$$

    is \(r \leq \min(s,3N)\) rank, and near the \(q_0\), one can always find \(3N-r\) parameters so that \(q^j = q^{j}(z^1,\cdots, z^{3N-r}) \ ; \ j=1,\cdots, 3N\) is the function defined by these \(s\) constraints.

4.  **Rigid body**

    Free rigid body has \(6\) degrees of freedom (\(f=6\)). One can always specify a rigid body by its position and its orientation, where position is 3-Cartesian coordinates \(\bm{x} = (x^1,x^2,x^3)\) of some fixed (on the rigid body) point (like mass center), and the orientation can be described by a orthogonal matrix \(\bm{A}\). Then, at each time \(t\) , the point(mass point) at \(\bm{z}(0)\) initially will be at:

    $$\bm{z}(t) - \bm{x}(t) = \bm{A}(t) \Big(\bm{z}(0) - \bm{x}(0)\Big)$$

    Note that 3D orthogonal matrix(SO(3)) can be uniquely described by three parameters, so the rigid body has \(f=6\).

## Euler-Lagrange Equation

Any `ideal` dynamical system obeys the equation(s) of:

$$\frac {\td } {\td t}\frac {\partial L} {\partial \flo{q}^r} - \frac {\partial L} {\partial q^r} = 0 \ ; \ r=1,\cdots,f$$

Where \(f\) is the number of degrees of freedom. \(q^r\) are coordinates to describe the system. \(L=L(q,\flo{q},t)\) is called `Lagrangian` . These equations induce \(r\) second order ODEs about \(q^r(t)\) .

1.  **Single 1D particle in external potential**

    Consider the Lagrangian of:

    $$L = T - V = \frac 1 2 m \flo{q}^2 - V(q)$$

    Then the equation of motion should be:

    $$ m \frac {\td^2 q} {\td t^2} + \frac {\td V} {\td q} (q) = 0$$

    Which is the Newton's law of motion.

2.  **Free particles**

    In Cartesian coordinates, kinetic energy of a particle is: \(T = \frac 1 2 m \bm{v}^2\) where \(\bm{v} = \frac {\td} {\td t} \bm{x}\) . So the Lagrangian of the free particle is:

    $$L = \sum_{i=1}^N \frac 1 2 m_i \bm{v}_i^2 = \sum_{i=1}^N \sum_{r=1}^3 \frac 1 2 m_i (\flo{q}_{i}^r)^2$$

3.  **Particle on a sphere**

    In Cartesian coordinates we have \(L = \frac 1 2 m \Big((\flo{x}^1)^2+(\flo{x}^2)^2+(\flo{x}^3)^2\Big)\) . Then with the relation \(x^1 = \sin\theta \cos \phi \ ; \ x^2 = \sin\theta \sin \phi \ ; \ x^3 = \cos\theta\) one has:

    $$\begin{cases}
     \flo{x}^1 &= \cos \theta \cos \phi \flo{\theta} - \sin\theta \sin\phi \flo{\phi} \\
     \flo{x}^2 &= \cos\theta \sin\phi \flo{\theta} + \sin\theta \cos\phi \flo{\phi} \\
     \flo{x}^3 &= -\sin\theta \flo{\theta}
    \end{cases}$$

    So:

    $$L = \frac 1 2 m \Big(\flo{\theta}^2 + \sin^2\theta \flo{\phi}^2 \Big)$$

4.  **Particle on generic constraints**

    The constraint for \(N\) particles are:

    $$f^i (q^1,\cdots,q^{3N}) = 0 \ ; \ i=1,\cdots,s$$

    The Lagrangian should still be:

    $$L = \frac 1 2 \sum_{i=1}^{3N} m_i (\flo{q}^{i})^2$$

    in which \(m_{3k+1} = m_{3k+2} = m_{3k+3}\), they are masses of the same particle. With the constraints, one has:

    $$\partial_l f^i \td q^l = 0 \Rightarrow \flo{q}^l \partial_l f^i = 0 \ ; \ i = 1,\cdots,s$$

    If the rank of Jacobian \(J_{ij} = \partial_i f^j(q)\) is \(r\) , then we can choose the first \(3N-r\) `generalized velocity` \(\flo{q}^i \ ; \ i=1,\cdots, 3N-r\) be fixed and solve this linear equation to express the other \(r\) velocities with these \(3N-r\) velocities:

    $$\flo{q}^k = \sum_{l=1}^{3N-r} C_{kl} \flo{q}^l \ ; \ k=3N-r+1,\cdots,3N$$

    and get the Lagrangian as the function of velocity of d.o.f. variables.

    $$L = \frac 1 2 \sum_{i=1}^{3N-r} m_i (\flo{q}^i)^2 + \frac 1 2 \sum_{i=3N-r+1}^{3N} m_i \Big(\sum_{l=1}^{3N-r} C_{il} \flo{q}^l\Big)^2$$

5.  **Rigid Body**

    We have shown that any mass point on the rigid body has the position at time \(t\) of the form:

    $$\bm{x_i}(t) = \bm{x}(t) + \bm{A}(t)(\bm{x_i}(0)-\bm{x}(0))$$

    Now we assume the reference point \(\bm{x}(t)\) is the position of the mass center. The Lagrangian (kinetic energy) is simply:

    $$\begin{aligned}
    L &= \frac 1 2 \sum_i m_i \Big(\frac {\td \bm{x}} {\td t} + \frac {\td \bm{A}} {\td t} (\bm{x_i}(0) - \bm{x}(0))\Big)^2\rightarrow \frac 1 2 \int \td m \Big(\frac {\td \bm{x}} {\td t} + \frac {\td \bm{A}} {\td t} (\bm{x_i} - \bm{x})\Big)^2 \\
    &= \frac 1 2 \int_B \td^3 \bm{z} \ \rho(\bm{z})\Big(\frac {\td \bm{x}} {\td t} + \frac {\td \bm{A}} {\td t} \bm{z}\Big)^2
    \end{aligned}$$

    Where we applied the variable substitution, and region \(B\) is the rigid body's configuration at time \(t=0\), `initially the mass center is at the original point`, and \(\rho(\bm{z})\) is the mass-density at position \(\bm{z}\) at rigid body initially. We did not compute the kinetic energy of the mass elements' rotation, because it should be of the second order of \(\td^3 \bm{z} = \td V\), and will not make any difference to the integral.

    Let us further simplify the expression, note that \(\flo{\bm{x}} = \bm{V}_c , \flo{\bm{A}} = \bm{R}\) are independent of \(\bm{z}\):

    $$\begin{aligned}
    L &= \frac 1 2 \int_B \td^3 \bm{z} \ \rho(\bm{z})\Big(\bm{V}_c^2 + \bm{V}_c^T \bm{R}\bm{z} + \bm{z}^T \bm{R}^T \bm{V}_c + \bm{z}^T\bm{R}^T\bm{R}\bm{z}\Big) \\
    &=\frac 1 2 M \bm{V}_c^2 + \frac 1 2 \int_B \td^3 \bm{z} \ \rho(\bm{z}) \bm{z}^T \bm{R}^T \bm{R}\bm{z}
    \end{aligned}$$

    Where we used the fact that \(\int_B \td V \rho = M\) and \(\int_B \td V \rho \bm{z} = 0\) is the mass of rigid body and that initially the mass center is at the original point.

    Now we consider the time derivative of rotation (orthogonal) matrix \(\bm{A}\) , with the property of orthogonality:

    $$\bm{A}(t)\bm{A}^T(t) = \bm{A}^T(t)\bm{A}(t) = \bm{I}$$

    we have:

    $$\bm{0} = \bm{R}\bm{A}^T + \bm{A}\bm{R}^T \Rightarrow \bm{R} \bm{A}^T = -(\bm{R} \bm{A}^T)^T$$

    That is to say, matrix \(\bm{R}\bm{A}^T\) is an anti-symmetric matrix. Let:

    $$\bm{R}\bm{A}^T = \begin{bmatrix}0 & -\omega_z & \omega_y \\ \omega_z & 0 & -\omega_x \\ -\omega_y & \omega_x & 0 \end{bmatrix}$$

    One can check that with this form, for arbitrary vector \(\bm{u} = (u_x,u_y,u_z)^T\) :

    $$\bm{R}\bm{A}^T \bm{u} = \begin{bmatrix}-\omega_z u_y + \omega_y u_z \\ \omega_z u_x -\omega_x u_z \\ -\omega_y u_x +\omega_x u_y\end{bmatrix} = \bm{\omega}\times \bm{u}$$

    Where \(\bm{\omega} = (\omega_x,\omega_y,\omega_z)^T\) .

    With the identity of:

    $$\frac {\td } {\td t}\Big(\bm{z}(t)-\bm{x}(t)\Big) = \bm{R} (\bm{z}(0)-\bm{x}(0)) = \bm{R}\bm{A}^T (\bm{z}(t)-\bm{x}(t)) = \bm{\omega}\times(\bm{z}(t)-\bm{x}(t))$$

    One can see why the vector \(\bm{\omega}\) is called `angular velocity`. Note that the matrix form of \(\bm{\omega}\) is actually the generic form of elements in Lie algebra \(so(3)\)

    So the Lagrangian can be simplified much further:

    $$\begin{aligned}
    L &= \frac 1 2 M \bm{V}_c^2 + \frac 1 2 \int_B \td^3 \bm{z} \ \rho(\bm{z}) (\bm{\omega}\times \bm{z}) \cdot (\bm{\omega}\times \bm{z}) \\
    &=\frac 1 2M \bm{V}_c^2 +\sum_{ij} \omega^i \omega^j \frac 1 2 \int_B \td^3 \bm{z} \ \rho(\bm{z}) \big(\bm{z}^2 \delta_{ij} - z^i z^j\big) \\
    &=\frac 1 2 M\bm{V}_c^2 + \frac 1 2 \bm{\omega}^T \bm{J}\bm{\omega}
    \end{aligned}$$

    Where

    $$\bm{J}_{ij} =\int_B \td^3 \bm{z} \ \rho(\bm{z}) \big(\bm{z}^2 \delta_{ij} - z^i z^j\big) $$

    is `Inertial tensor` and we used the identity:

    $$\begin{aligned}
    (\bm{a}\times \bm{b})\cdot (\bm{a}\times \bm{b}) &= \delta_{ij}\epsilon_{imn}a^m b^n \epsilon_{jpq}a^pb^q \\
    &=(\delta_{mp}\delta_{nq}-\delta_{mq}\delta_{np})a^m b^n a^p b^q \\
    &=\bm{a}^2 \bm{b}^2 - (\bm{a}\cdot \bm{b})^2 \\
    &=a^i a^j (\bm{b}^2 \delta_{ij} - b_i b_j)
    \end{aligned}$$

    To write the angular velocity \(\bm{\omega}\) as time derivative of generalized coordinates one can use the definition of Euler angles.

6.  **Rigid body with fixed axis**

    Some times the rigid body is constraint on a fixed axis, that is, the angular velocity has a fixed orientation: \(\bm{\omega}(t) = \omega(t)\bm{n}\) . Then the Lagrangian (kinetic energy of rotation) should be:

    $$L = \frac 1 2 \omega^2 \bm{n}^T \bm{J} \bm{n}\equiv \frac 1 2 \omega^2 J_{\bm{n}}$$

    Where:

    $$\begin{aligned}
    J_{\bm{n}} &= \bm{n}^T \bm{J} \bm{n} \\
    &= \int_B \td^3 \bm{z} \ \rho(\bm{z}) (\bm{z^2} \bm{n}^2 - (\bm{z}\cdot \bm{n})^2) \\
    &= \int_B \td^3 \bm{z} \ \rho(\bm{z}) (\bm{z}^2 - (\bm{z}\cdot \bm{n})^2)
    \end{aligned}$$

    Note that \(|\bm{n}| = 1\) , and \(\bm{z}^2 - (\bm{z}\cdot \bm{n})^2\) is definitely the distance between \(\bm{z}\) point and the line along \(\bm{n}\) crossing original point.

7.  **Relativistic particle**

    Relativistic particle in `Cartesian coordinate` has the Lagrangian of:

    $$L = m \bm{v}^2 \sqrt{1 - \bm{v}^2 / c^2} - V(\bm{x})$$

    So the equation of motion is:

    $$\frac {\td} {\td t}\frac {\partial L} {\partial \bm{v}} = \frac {\td } {\td t} \frac {m \bm{v}} {\sqrt{1-\bm{v}^2/c^2}} = -\nabla V(\bm{x})$$

    i.e., the movement lets the mass get larger.

8.  **Charged particle in static electromagnetic field**

    Consider a particle with charge \(Q\) moves in electromagnetic field \((\bm{A}, \phi)\) , with the intensity of field: \(\bm{B} = \nabla \times \bm{A} \ ; \ \bm{E} = - \nabla \phi\). Note that we use Cartesian coordinate to describe the system. The Lagrangian is:

    $$L = \frac 1 2 m\bm{v}^2 + Q (\bm{A}\cdot \bm{v} - \phi)$$

    Then the equation of motion:

    $$\frac {\td } {\td t} \Big(m \bm{v} + Q\bm{A}\Big) = - Q \bm{E} + Q \nabla(\bm{A}\cdot \bm{v})$$

    Or:

    $$m\frac {\td \bm{v}} {\td t} = -Q \bm{E} + Q \bm{v}\times \bm{B}$$

## Integrating the Lagrange Equation

When Lagrangian is not dependent of time, one can use Legendre transformation to construct a integral of the equation of motion:

$$H = \sum_{i=1}^f \flo{q}^i \frac {\partial L} {\partial \flo{q}^i} - L = \text{Const}$$

Usually (when \(L\) is a second order homogeneous function of \(\flo{q}\)) , Hamiltonian has a simple form of \(H = T + V\).

When lagrangian is not dependent of a coordinate \(q^r\) , i.e. , \(\partial L /\partial q^r = 0\) ,  the generalized momentum is conversed (another first integral):

$$p^r = \frac {\partial L} {\partial \flo{q}^r} = \text{Const}$$

Using these first integral, one can reduce the Lagrange equation into a set of 1-order ODE, which is much easier to solve.

1.  **Particle in static electromagnetic field**

    The lagrangian is:

    $$L = \frac 1 2 m\bm{v}^2 + Q (\bm{A}\cdot \bm{v} - \phi)$$

    Obviously it is independent of time. So:

    $$H = \bm{v}\cdot \nabla_{\bm{v}} L - L = \frac 1 2 m\bm{v}^2 + Q \phi = E$$

    And one can obtain that:

    $$\bm{v}^2 =\sqrt{\frac {2(E - Q\phi(\bm{x}))} {m}}$$

2.  **Relativistic particle**

    The time independent Lagrangian is:

    $$L = m \bm{v}^2 \sqrt{1 - \bm{v}^2 / c^2} - V(\bm{x})$$

    So:

    $$H = \frac {m c^2} {\sqrt{1-\bm{v}^2/c^2}} + V(\bm{x}) = E$$

3.  **Central force**

    Consider a particle moves in a central force field:

    $$L = \frac 1 2 m \bm{v}^2 - V(r)$$

    Where \(r = |\bm{r}|\) . First of all, it is independent of time, one has:

    $$H = \frac 1 2 m \bm{v}^2 - V(r) = E$$

    And if we write it with spherical coordinate with:

    $$x = r \sin\theta \cos\phi \ ; \ y = r \sin\theta\sin\phi \ ; \ z = r\cos\phi$$

    we have:

    $$L = \frac 1 2 m \Big(\flo{r}^2 + r^2\flo{\theta}^2 + r^2\sin^2\theta \flo{\phi}^2\Big) - V(r)$$

    it is independent of angle \(\phi\), so:

    $$p_{\phi} = \frac {\partial L} {\partial \flo{\phi}} = m r^2 \sin^2\theta \flo{\phi} = \text{Const}$$

    Initially we can always choose a proper coordinate system so that \(\flo{\phi} \neq 0\) while \(\theta = \pi/2 \ ; \ \flo{\theta} = 0\) .

    We have the equation of motion for \(\theta\):

    $$\frac {\td } {\td t} m r^2 \flo{\theta} - \frac 1 2 m r^2\sin(2\theta) \flo{\phi}^2 = 0 $$

    It has a special solution of \(\theta \equiv \pi/2\) under our initial condition. i.e., the movement is constraint on a plane. Then the reduced effective Lagrangian should be:

    $$L = \frac 1 2 m\Big(\flo{r}^2 + r^2 \flo{\phi}^2\Big) - V(r)$$

# Summary of Hamilton Theory

## Hamiltonian Equation of Motion

Any system obeys the canonical equation of motion with its Hamiltonian \(H = H(q,p,t)\).

$$\begin{aligned}
\frac {\td p_i} {\td t} &= -\frac {\partial H} {\partial q_i} \\
\frac {\td q_i} {\td t} &= \frac {\partial H} {\partial p_i}
\end{aligned}$$

Or any function of \(q,p,t\): \(A=A(q,p,t)\) along the trajectory(the solution of canonical equation) \(\hat A(t)\equiv A(q(t),p(t),t)\) obeys the equation:

$$\frac {\td \hat A} {\td t} = \sum_{i=1}^f \frac {\partial A} {\partial q^i} \frac {\td q^i} {\td t} +\frac {\partial A} {\partial p^i} \frac {\td p^i} {\td t} + \frac {\partial A} {\partial t} =  \sum_{i=1}^f \frac {\partial A} {\partial q^i} \frac {\partial H} {\partial p^i} -\frac {\partial A} {\partial p^i} \frac {\partial H} {\partial q^i} + \frac {\partial A} {\partial t}$$

With the definition of Poisson bracket:

$$[A,B] =\sum_{i=1}^f \frac {\partial A} {\partial q^i} \frac {\partial B}{\partial p^i}-\frac {\partial A} {\partial p^i} \frac {\partial B}{\partial q^i} $$

the dynamical equation can be written as:

$$\frac {\td \hat A} {\td t} = \Big([A,H] + \frac {\partial A} {\partial t}\Big)(q(t),p(t),t)$$

Because of \([H,H] \equiv 0\) , so we have an identity:

$$\frac {\td \hat H} {\td t} = \frac {\partial H} {\partial t}(q(t),p(t),t)$$

That is to say, if \(H\) is independent of time: \(\partial_t H = 0\) , then along the trajectory \(\hat H = H(q(t),p(t),t)\) should be a constant.

Similarly, any function \(A\), if \([A,H] + \frac {\partial A} {\partial t} = 0\) , then it is constant along the trajectory.

1.  **Laplace-Runge-Lenz vector**

    Vector:

    $$\bm{K} = \bm{p}\times (\bm{r}\times \bm{p}) - m \frac {\bm{r}} r = \bm{r} \bm{p}^2 - \bm{p}(\bm{r}\cdot \bm{p}) - m \bm{r}/r$$

    is conserved in the Newton-gravity system:

    $$H = \frac {\bm{p}^2} {2m} - \frac 1 {r}$$

    The component of vector \(\bm{K}\) is:

    $$K^i = x^i p^jp^j - p^i x^j p^j - m x^i/r$$

    So:

    $$\begin{aligned}[]
    [K^i, H] &= \sum_{l=1}^3 \frac {\partial K^i} {\partial x^l} \frac {\partial H} {\partial p^l} - \frac {\partial K^i} {\partial p^l} \frac {\partial H} {\partial x^l} \\
    &=\sum_{l=1}^3 \Big(\bm{p}^2\delta_{il}-p^i p^j \delta_{lj} - \frac {m(\delta_{il}r - x^i x^l /r)} {r^2}\Big) \frac {p^l} {m} \\
    & - \Big(2x^i p^l - x^j(p^j\delta_{li}+p^i\delta_{lj})\Big)(\frac {x^l} {r^3}) \\
    &=\Big(\bm{p}^2 - p^i\sum_j p^jp^j - \frac {p^i r - x^i \bm{x}\cdot \bm{p}/r} {r^2}\Big) \\
    & - \Big(\frac {2 x^i \bm{x}\cdot \bm{p}} {r^3} -\frac {x^j p^j x^i} {r^3} - \frac {p^i} {r} \Big) \\
    &= \bm{p}^2  - p^i \sum_j p^jp^j = 0
    \end{aligned}$$

    q.e.d.

    With vector \(K\) , we have:

    $$\bm{r} \cdot \bm{K} = r K \cos\theta = r^2 p^2 - (\bm{p}\cdot\bm{r})^2 - mr = L^2 - mr$$

    So:

    $$\frac 1 r = \frac {K \cos\theta - m} {L^2}$$

    The ellipse orbital.

## Canonical Transformation

Consider the transform between \((Q,P)\) and \((q,p)\) (we only consider the transformation who has no explicit time dependence):

$$\begin{cases}P &= P(q,p) \\ Q &= Q(q,p)\end{cases} \ ; \ \begin{cases}p &= p(Q,P) \\ q &= q(Q,P)\end{cases}$$

It is a canonical transformation if and only if it holds the form of canonical equation. i.e.:

$$\tilde{H}(Q,P,t) \equiv H\Big(q(Q,P),p(Q,P),t\Big) \Rightarrow \frac {\td Q} {\td t} = \frac {\partial \tilde{H}} {\partial P} \ ; \ \frac {\td P} {\td t} = -\frac {\partial \tilde{H}} {\partial Q}$$

We can simplify this relationship:

$$\frac {\partial \tilde{H}} {\partial P} = \partial_p H \partial_P p + \partial_q H \partial_P q \ ; \ \frac {\td Q} {\td t} = \partial_q Q \flo{q} + \partial_p Q \flo{p}$$

So we need:

$$\begin{aligned}
\flo{q}\partial_P p  -\flo{p}\partial_P q &= \partial_q Q \flo{q} + \partial_p Q \flo{p} \\
\flo{p}\partial_Q q - \flo{q}\partial_Q p &= \partial_q P \flo{q} + \partial_p P \flo{p}
\end{aligned}$$

That is:

$$\frac {\partial p} {\partial P} = \frac {\partial Q} {\partial q} \ ; \ \frac {\partial q} {\partial P} = -\frac {\partial Q} {\partial p} \ ; \ \frac {\partial q} {\partial Q} = \frac {\partial P} {\partial p} \ ; \ \frac {\partial p} {\partial Q} = -\frac {\partial P} {\partial q}$$

## Hamilton Jacobi Equation

### Generating Function

Canonical transformation(CT) will not modify the variation rule:

$$\delta \int \Big(\flo{q} p  - H\Big)\td t = 0 \ ; \ \delta\int \Big(\flo{Q} P - \tilde{H}\Big)\td t = 0$$

So a class of CT can be generated by the equality:

$$\flo{q}p - H = \flo{Q} P - \tilde{H} + \frac {\td G} {\td t}$$

Where \(G\) can be an arbitrary function, as long as this equality holds.

We will "derive" the HJ equation in the following manner:

Let \(G = - QP + S(q,P,t)\) , with this form, the equality should be:

$$\flo{q} p - H = \flo{Q} P - \tilde{H} -\flo{Q} P - Q\flo{P} + \partial_1 S \flo{q} + \partial_2 S \flo{P} + \partial_3 S$$

So we need:

$$p = \frac {\partial S} {\partial q} (q,P,t) \ ; \ Q = \frac {\partial S} {\partial P}(q,P,t) \ ; \ \tilde{H} - H = \frac {\partial S} {\partial t}(q,P,t)$$

Find a function \(S(q,P,t)\) who obeys the equations above, we can find a "generating function" for a set of CTs by:

$$p = \partial_1 S (q,P,t) \ ; \ Q = \partial_2 S(q,P,t) \Rightarrow q=M(p,Q,t) \ ; \ P = N(p,Q,t)$$

Then one can reduce it into the standard form of CT:

$$p = p(Q,P,t) \ ; \ q = q(Q,P,t) \cdots$$

### HJ Equation

If we can find a CT with which the system can be solved easily in new variables. i.e., \(\tilde{H} = 0\), the solution is trivial:

$$\frac {\td P} {\td t} = \frac {\td Q} {\td t} = 0$$

If this CT can be generated by \(S\) , we need:

$$H(q,p,t) + \frac {\partial S} {\partial t} = 0 \Rightarrow H(q,\frac {\partial S} {\partial q},t) +\frac {\partial S} {\partial t} = 0$$

Solve this equation and obtain a non-trivial solution of \(S\), that is to say, the solution \(S\) should be a function of \(q,t\) and contain \(f\) parameters:

$$S = S(q,t; \alpha)$$

Then one can generate a CT by generating function \(S(q,t;P)\):

$$p = \partial_q S(q,t;P) \ ; \ Q = \partial_P S(q,t;P)$$

Since \(S\) satisfies the HJ equation (or equivalently, the requirement of CT), such a transformation will automatically be canonical.

1.  **1D Harmonic Oscilltor**

    The Hamiltonian is:

    $$H(q,p,t) = \frac 1 2 (q^2 + p^2)$$

    Then the HJE should be:

    $$\frac {\partial S} {\partial t} = \frac 1 2 q^2 + \frac 1 2 \Big(\frac {\partial S} {\partial q}\Big)^2$$

    We need only find a solution of this equation. Consider \(S = f(q) + Et/2\):

    $$\frac 1 2 E = \frac 1 2 q^2 + \frac 1 2 (f')^2 \Rightarrow \frac {\td f} {\td q} = \sqrt{E-q^2}$$

    Integral it one can find a solution of \(f\): \(f(q) = \frac 1 2 \Big(q\sqrt{E-q^2}+ E\arctan\frac {q} {\sqrt{E-q^2}}\Big) + C\) . Note that the parameter \(C\) will make no difference because \(\partial S/\partial C \equiv 0\) , then:

    $$S(q,t;E) = \frac {Et} 2 + \frac 1 2 \Big(q\sqrt{E-q^2}+ E\arctan\frac {q} {\sqrt{E-q^2}}\Big)$$

    Then the generated CT is:

    $$\begin{aligned}
    p &= \frac {\partial S(q,t;P)} {\partial q} = \sqrt{P - q^2} \\
    Q &= \frac {\partial S(q,t;P)} {\partial P} = \frac t 2 + \frac 1 2 \arctan \frac {q} {\sqrt{P-q^2}}
    \end{aligned}$$

    So that is:

    $$\begin{aligned}
    P &= q^2 + p^2 \\
    Q &= \frac 1 2 t + \frac 1 2 \arctan \frac {q} {p}
    \end{aligned}$$

    According to our assumption, they should be constant, then the solution w.r.t. \(q,p\) is:

    $$q^2 + p^2 = C_1 \ ; \ \frac {q} p = \tan(C_2 - t)$$

    That is the solution of Harmonic oscilltor.

    One can check that the \(P,Q\) indeed define a CT, and the Hamiltonian is zero.

2.  **Newton gravity**

    We know that the reduced Lagrangian is:

    $$L = \frac 1 2 m (\flo{r}^2 + r^2 \flo{\phi}^2) + \frac k r$$

    So the equivalent Hamiltonian is:

    $$H(q,p,t) = p_r^2 + \frac {p_{\phi}^2} {r^2} + \frac c r$$

    Then the HJE:

    $$\frac {\partial S} {\partial t} + \frac c r + (\frac {\partial S} {\partial r})^2 + \frac 1 {r^2} (\frac {\partial S} {\partial \phi})^2 = 0$$

    Assume: \(S(q,t) = a_1 t + f(r) + g(\phi)\) , then:

    $$\begin{aligned}
    a_1 + \frac c r + (f')^2 + \frac 1 {r^2} (g')^2 = 0
    \end{aligned}$$

    Note that \(g'\) is a function of \(\phi\) and \(f'\) is a function of \(r\), the equality holds only when:

    $$a_1 r^2 + c r + r^2 (f')^2 = - (g')^2 = -a_2$$

    So:

    $$g(\phi) = \sqrt{a_2} t \ ; \ f'(r) = \sqrt{\frac {-a_2 - a_1 r^2 - c r} {r^2}}$$

    It is solvable:

    $$f(r) = \frac{1}{2 \sqrt{a_1} \sqrt{r (a_1 r+c)+a_2}}\Big(r \sqrt{-\frac{r (a_1 r+c)+a_2}{r^2}} \\
    \left(c \tanh ^{-1}\left(\frac{2 a_1 r+c}{2 \sqrt{a_1} \sqrt{r (a_1 r+c)+a_2}}\right)+2 \sqrt{a_1} \left(\sqrt{r (a_1 r+c)+a_2} \\
    -\sqrt{a_2} \tanh ^{-1}\left(\frac{2 a_2+c r}{2 \sqrt{a_2} \sqrt{r (a_1 r+c)+a_2}}\right)\right)\right)\Big)$$
