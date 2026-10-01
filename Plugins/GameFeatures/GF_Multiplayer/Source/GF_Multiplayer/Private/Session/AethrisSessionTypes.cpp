// Copyright AETHRIS Team.
#include "Session/AethrisSessionTypes.h"

namespace Aethris::Session
{
	bool IsTransitionAllowed(EAethrisSessionState From, EAethrisSessionState To)
	{
		using S = EAethrisSessionState;
		if (To == S::Offline)
		{
			return true;   // Abmelden/Verbindungsabbruch ist immer erlaubt – Spiel läuft offline weiter
		}
		switch (From)
		{
		case S::Offline:          return To == S::Connecting;
		case S::Connecting:       return To == S::OnlineIdle;
		case S::OnlineIdle:       return To == S::Hosting || To == S::JoiningHost || To == S::Matchmaking;
		case S::Hosting:          return To == S::OnlineIdle;
		case S::JoiningHost:      return To == S::InGuestWorld || To == S::OnlineIdle;
		case S::InGuestWorld:     return To == S::Returning || To == S::Reconnecting;
		case S::Matchmaking:      return To == S::InDedicatedMatch || To == S::OnlineIdle;
		case S::InDedicatedMatch: return To == S::OnlineIdle || To == S::Reconnecting;
		case S::Reconnecting:     return To == S::InGuestWorld || To == S::InDedicatedMatch || To == S::Returning;
		case S::Returning:        return To == S::OnlineIdle;
		default:                  return false;
		}
	}

	int32 ReconnectWindowSec(EAethrisOnlineMode Mode)
	{
		switch (Mode)
		{
		case EAethrisOnlineMode::Coop:      return 120;
		case EAethrisOnlineMode::Raid:      return 90;
		case EAethrisOnlineMode::PvpCasual:
		case EAethrisOnlineMode::PvpRanked: return 60;
		default:                            return 0;
		}
	}
}
