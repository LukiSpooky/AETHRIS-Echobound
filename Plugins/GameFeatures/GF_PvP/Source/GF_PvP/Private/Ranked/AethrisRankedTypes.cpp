// Copyright AETHRIS Team.
#include "Ranked/AethrisRankedTypes.h"

namespace Aethris::Ranked
{
	namespace
	{
		constexpr double Scale = 173.7178;
		double G(double Phi) { return 1.0 / FMath::Sqrt(1.0 + 3.0 * Phi * Phi / (PI * PI)); }
	}

	FAethrisGlicko2 Update(const FAethrisGlicko2& Self, const FAethrisGlicko2& Opponent, double Score)
	{
		const double Mu = (Self.Rating - 1500.0) / Scale, Phi = Self.Deviation / Scale;
		const double MuJ = (Opponent.Rating - 1500.0) / Scale, PhiJ = Opponent.Deviation / Scale;
		const double Gj = G(PhiJ);
		const double E = 1.0 / (1.0 + FMath::Exp(-Gj * (Mu - MuJ)));
		const double V = 1.0 / (Gj * Gj * E * (1.0 - E));
		const double Delta = V * Gj * (Score - E);
		const double A0 = FMath::Loge(Self.Volatility * Self.Volatility);

		auto F = [&](double X)
		{
			const double Ex = FMath::Exp(X);
			return Ex * (Delta * Delta - Phi * Phi - V - Ex) / (2.0 * FMath::Square(Phi * Phi + V + Ex)) - (X - A0) / (Tau * Tau);
		};

		double A = A0, B;
		if (Delta * Delta > Phi * Phi + V)
		{
			B = FMath::Loge(Delta * Delta - Phi * Phi - V);
		}
		else
		{
			int32 K = 1;
			while (F(A0 - K * Tau) < 0.0) { ++K; }
			B = A0 - K * Tau;
		}
		double FA = F(A), FB = F(B);
		for (int32 Iter = 0; Iter < 100 && FMath::Abs(B - A) > 1e-6; ++Iter)   // Illinois-Verfahren
		{
			const double C = A + (A - B) * FA / (FB - FA);
			const double FC = F(C);
			if (FC * FB <= 0.0) { A = B; FA = FB; } else { FA *= 0.5; }
			B = C; FB = FC;
		}
		const double Sigma2 = FMath::Exp(A / 2.0);
		const double PhiStar = FMath::Sqrt(Phi * Phi + Sigma2 * Sigma2);
		const double Phi2 = 1.0 / FMath::Sqrt(1.0 / (PhiStar * PhiStar) + 1.0 / V);
		const double Mu2 = Mu + Phi2 * Phi2 * Gj * (Score - E);

		FAethrisGlicko2 Out;
		Out.Rating = Mu2 * Scale + 1500.0;
		Out.Deviation = Phi2 * Scale;
		Out.Volatility = Sigma2;
		Out.Matches = Self.Matches + 1;
		return Out;
	}

	FAethrisGlicko2 DecayWeek(const FAethrisGlicko2& Self)
	{
		FAethrisGlicko2 Out = Self;
		const double Phi = Self.Deviation / Scale;
		Out.Deviation = FMath::Min(350.0, FMath::Sqrt(Phi * Phi + Self.Volatility * Self.Volatility) * Scale);
		return Out;
	}

	EAethrisRankTier TierFor(double Conservative)
	{
		if (Conservative >= 2050.0) return EAethrisRankTier::Weltakkord;
		if (Conservative >= 1750.0) return EAethrisRankTier::Hymne;
		if (Conservative >= 1550.0) return EAethrisRankTier::Chor;
		if (Conservative >= 1350.0) return EAethrisRankTier::Lied;
		if (Conservative >= 1150.0) return EAethrisRankTier::Ruf;
		return EAethrisRankTier::Summen;
	}
}
