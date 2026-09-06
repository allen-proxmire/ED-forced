# -*- coding: utf-8 -*-
"""Why does the seam DIVIDE by 2 pi rather than multiply?

Note_a0_TwoPi_RepairRoutes section 4f isolated the whole remaining debt on a_0
to one sentence:

    "given that we compare at layer 1, why does the seam contribute 1/(2 pi)
     rather than 2 pi?"

and noted that dimensional analysis does NOT fix it -- both readings are
dimensionally legal and differ by (2 pi)^2, a factor of about 39.

This script checks the arithmetic of the two readings and states the argument
that settles the direction.

Run: python "internal notes/_check_twopi_direction.py"
"""
import math

C = 2.99792458e8            # m/s
H0_KM_S_MPC = 67.4          # Planck 2018-ish; the conclusion is insensitive
MPC_M = 3.0856775814913673e22
H0 = H0_KM_S_MPC * 1000.0 / MPC_M       # 1/s
A0_OBS = 1.2e-10            # m/s^2, standard MOND value

print("The 2 pi direction")
print("=" * 78)
print("\n  H0            = %.4e / s" % H0)
print("  c H0          = %.4e m/s^2" % (C * H0))
print("  observed a_0  = %.4e m/s^2\n" % A0_OBS)

for label, val in [("c H0 / (2 pi)   [divide]", C * H0 / (2 * math.pi)),
                   ("c H0            [no factor]", C * H0),
                   ("2 pi c H0       [multiply]", 2 * math.pi * C * H0)]:
    print("  %-28s = %.4e   ratio to observed = %8.2f" % (label, val, val / A0_OBS))
print("""
  So the two candidate directions differ by (2 pi)^2 = %.1f, and only the
  dividing one lands near the measured value.  That is not the argument --
  matching a_0 is what the whole route is trying to explain, so using it to
  pick the direction would be circular.  It is stated only to show the stakes.
""" % ((2 * math.pi) ** 2))

print("""THE ARGUMENT THAT FIXES THE DIRECTION

  The 2 pi in T = kappa / (2 pi) is not decoration.  It is the standard
  relation between an ANGULAR frequency and a CYCLIC one:

      omega = 2 pi nu

  In the Euclidean-period derivation the horizon's inverse temperature is the
  period, beta = 2 pi / kappa.  So kappa is radians per unit time -- an
  omega -- while T = 1/beta is cycles per unit time -- a nu.  Dividing by
  2 pi is just converting omega to nu.  Nothing else is happening.

  So "does the seam divide or multiply" is really: IS THE CHAIN'S SIDE AN
  OMEGA OR A NU?

  The corpus already answers it.  Note_a0_TwoPi_RepairRoutes section 4b:

      "A chain's acceleration is, in ED, a P11 commitment-rate asymmetry ...
       That is a BARE COUNT-RATE at the level of commitments."

  A count-rate is a nu.  Commitments are DISCRETE EVENTS (P11: "discrete,
  environmentally-phase-randomizing, irreversible substrate events"), so you
  count them; that is cycles per second, not radians per second.

  Meanwhile the horizon has no layer-1 kappa at all (Paper_028 section 3.4
  makes the cosmic surface statistical, not geometric) and presents only
  coarse-grained, as a de Sitter-like horizon with kappa_H = H0 -- an omega.

  So the comparison is nu-against-omega, and putting them on the same footing
  divides the omega by 2 pi.  One conversion, one factor, in the direction
  that divides:

      a_0 = c * T_H = c * H0 / (2 pi)

  THE DIRECTION IS FIXED BY P11'S DISCRETENESS.  Multiplying instead would
  require the chain's acceleration to be an angular rate, i.e. a continuous
  phase advance rather than a count of discrete events -- which is what P11
  denies.

WHY THIS ALSO EXPLAINS A PATTERN ALREADY OBSERVED

  Section 4b predicted, before any of this: every ED quantity comparing a bare
  chain rate to a horizon thermal state should carry exactly ONE 2 pi, and
  like-layer comparisons should carry NONE.  Section 4c found exactly that --
  expressing W_0 against (c H0)^2, a like-layer comparison, "the pi vanishes
  entirely".

  The omega/nu reading explains why: a cross-layer comparison is nu-against-
  omega and needs one conversion; a like-layer comparison is nu-against-nu or
  omega-against-omega and needs none.  The pattern was observed first and now
  has a cause.

TIER, STATED HONESTLY

  This is a TYPE argument -- about what KIND of quantity sits on each side --
  not a computation.  It is stronger than section 4b's "the chain is what
  responds, so the response is executed in the chain's machinery", because it
  cites P11's discreteness rather than an intuition about response.  It is
  weaker than a derivation of a_0, which nobody has.

  What it closes: section 4f's owed sentence, which asked for the direction
  and not for the value.

  What it does not close: the value.  a_0 ~ c H0 remains form-derived with the
  scale inherited from H0, exactly as before -- and per ledger #60, a_0 ~ c H0
  is Milgrom's (1983) and the 2 pi-normalised form is standard in the MOND
  review literature.  ED's claim is the coefficient's ORIGIN, and this
  supplies the origin's direction, not a new number.

  FALSIFIER.  If commitment were shown to be a continuous phase advance rather
  than a count of discrete events, the chain's side would be an omega, the
  comparison would be like-layer, and the 2 pi would vanish -- giving
  a_0 = c H0, which is 5.2x the measured value.
""")
