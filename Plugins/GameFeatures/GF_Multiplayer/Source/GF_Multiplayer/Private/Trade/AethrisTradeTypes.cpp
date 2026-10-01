// Copyright AETHRIS Team.
#include "Trade/AethrisTradeTypes.h"

namespace Aethris::Trade
{
	bool IsTransitionAllowed(EAethrisTradeState From, EAethrisTradeState To)
	{
		using S = EAethrisTradeState;
		if (To == S::Cancelled)
		{
			// aus jedem nicht abgeschlossenen Zustand; im Escrow nur durch den Server (Fehler → Rückgabe)
			return From != S::Completed && From != S::Cancelled && From != S::Rejected;
		}
		switch (From)
		{
		case S::Draft:           return To == S::Validating;
		case S::Validating:      return To == S::AwaitingPartner || To == S::Rejected;
		case S::AwaitingPartner: return To == S::Review;
		case S::Review:          return To == S::Escrow || To == S::Validating;   // Änderung → neu prüfen
		case S::Escrow:          return To == S::Completed;
		default:                 return false;
		}
	}
}
