#pragma once

#include <qlat-utils/qacc.h>
#include <complex>

#ifdef QLAT_USE_ACC
#include <thrust/complex.h>
#endif

namespace qlat
{  //

using RealD = double;

using RealF = float;

using Real = RealD;  // default Real type

#ifdef QLAT_USE_ACC

template <class T = Real>
using ComplexT = thrust::complex<T>;

template <class T>
qacc ComplexT<T> qconj(const ComplexT<T>& x)
{
  return thrust::conj(x);
}

template <class T>
qacc T qnorm(const ComplexT<T>& x)
{
  return thrust::norm(x);
}

template <class T>
qacc ComplexT<T> qpolar(const T& r, const T& theta = T())
{
  return thrust::polar(r, theta);
}

#else

template <class T = Real>
using ComplexT = std::complex<T>;

template <class T>
ComplexT<T> qconj(const ComplexT<T>& x)
{
  return std::conj(x);
}

template <class T>
T qnorm(const ComplexT<T>& x)
{
  return std::norm(x);
}

template <class T>
qacc ComplexT<T> qpolar(const T& r, const T& theta = T())
{
  return std::polar(r, theta);
}

#endif

using ComplexD = ComplexT<RealD>;

using ComplexF = ComplexT<RealF>;

using Complex = ComplexT<Real>;

const ComplexD ii(0, 1);

template <class T>
inline std::string show(const ComplexT<T>& x)
{
  return ssprintf("(%24.17E + %24.17E j)", x.real(), x.imag());
}

}  // namespace qlat
