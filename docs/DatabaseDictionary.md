# RailSense Database Dictionary

## Purpose

This document defines every database table used in the RailSense platform.

Each table includes:
- Purpose
- Columns
- Data Types
- Primary Keys
- Foreign Keys
- Relationships
- Notes

This document serves as the single source of truth for the RailSense database.

---

# Tables

1. Stations
2. Trains
3. TrainRoutes
4. TrainSchedules
5. CoachTypes
6. Quotas
7. SeatAvailability
8. Predictions
9. Users
10. SearchHistory
11. Feedback
12. TrainClasses
13. BoardingStations
14. ReservationCharts
15. CoachComposition
16. TrainCancellations
17. Diversions
18. TemporaryTrains
19. PredictionHistory
20. ModelVersions
21. FeatureData
22. PredictionAccuracy
23. UserReportedOutcomes
24. Favorites
25. Notifications
26. SavedJourneys
27. UserSettings
28. Devices
29. AdminUsers
30. DataImportLogs
31. APIKeys
32. AuditLogs
33. SystemSettings
34. CachedPredictions
35. CachedSeatAvailability
36. BackgroundJobs
37. PopularRoutes
38. SearchAnalytics
39. PredictionStatistics
40. ErrorLogs
41. AlternateRoutes
42. FareInformation
43. LiveTrainStatus
44. PlatformInformation
45. StationFacilities
46. NearbyStations
47. TrainRuns
---

# Table: Trains

## Purpose

Stores master information about every train in the RailSense platform.

This table stores only permanent train information.
Date-specific information (seat availability, cancellations, predictions, etc.) is stored in separate tables.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| TrainID | UUID | PK | Unique train identifier |
| TrainNumber | VARCHAR(10) | UNIQUE | Railway train number |
| TrainName | VARCHAR(150) | | Official train name |
| TrainType | VARCHAR(50) | | Express, Superfast, Rajdhani, etc. |
| FromStationID | UUID | FK | Origin station |
| ToStationID | UUID | FK | Destination station |
| IsActive | BOOLEAN | | Active or discontinued |
| CreatedAt | TIMESTAMP | | Record creation time |
| UpdatedAt | TIMESTAMP | | Last update time |

## Relationships

- FromStationID → Stations.StationID
- ToStationID → Stations.StationID
- Referenced by TrainRoutes
- Referenced by TrainSchedules
- Referenced by CoachTypes
- Referenced by TrainRuns

## Notes

- One record per train.
- Does not store route details.
- Does not store coach composition.
- Does not store seat availability.
- These are maintained in separate tables.
---

# Table: TrainRoutes

## Purpose

Stores the complete route of every train, including every station it passes through, the sequence of stations, scheduled arrival/departure times, halt duration, and distance from the source.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|--------|-------------|
| RouteID | UUID | PK | Unique route record identifier |
| TrainID | UUID | FK | Train reference |
| StationID | UUID | FK | Station reference |
| SequenceNumber | INTEGER | | Order of the station in the route |
| ArrivalTime | TIME | | Scheduled arrival time |
| DepartureTime | TIME | | Scheduled departure time |
| HaltMinutes | INTEGER | | Scheduled halt duration |
| DistanceFromSource | DECIMAL(6,1) | | Distance from source station (km) |
| DayNumber | INTEGER | | Journey day (1, 2, 3...) |
| PlatformNumber | VARCHAR(10) | | Scheduled platform (if available) |
| IsTechnicalHalt | BOOLEAN | | Technical halt or commercial stop |
| CreatedAt | TIMESTAMP | | Record creation time |
| UpdatedAt | TIMESTAMP | | Last update time |

## Relationships

- TrainID → Trains.TrainID
- StationID → Stations.StationID

## Notes

- One record represents one station on one train's route.
- A train will have multiple records in this table.
- Used for route visualization, station sequence, boarding analysis, and AI prediction.
---

# Table: TrainSchedules

## Purpose

Stores the operating schedule of each train, including the days on which it runs and the validity period of the schedule.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|--------|-------------|
| ScheduleID | UUID | PK | Unique schedule identifier |
| TrainID | UUID | FK | Train reference |
| RunsOnMonday | BOOLEAN | | Runs on Monday |
| RunsOnTuesday | BOOLEAN | | Runs on Tuesday |
| RunsOnWednesday | BOOLEAN | | Runs on Wednesday |
| RunsOnThursday | BOOLEAN | | Runs on Thursday |
| RunsOnFriday | BOOLEAN | | Runs on Friday |
| RunsOnSaturday | BOOLEAN | | Runs on Saturday |
| RunsOnSunday | BOOLEAN | | Runs on Sunday |
| EffectiveFrom | DATE | | Schedule start date |
| EffectiveTo | DATE | | Schedule end date (nullable) |
| IsActive | BOOLEAN | | Schedule currently active |
| CreatedAt | TIMESTAMP | | Record creation time |
| UpdatedAt | TIMESTAMP | | Last update time |

## Relationships

- TrainID → Trains.TrainID

## Notes

- One active schedule per train.
- Historical schedules can be preserved by changing EffectiveTo.
---

# Table: CoachTypes

## Purpose

Stores the coach classes available for each train.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| CoachTypeID | UUID | PK | Unique coach type identifier |
| TrainID | UUID | FK | Train reference |
| CoachType | VARCHAR(20) | | SL, 3E, 3A, 2A, 1A, CC, EC, etc. |
| TotalCoaches | INTEGER | | Total number of coaches of this type |
| CreatedAt | TIMESTAMP | | Record creation time |
| UpdatedAt | TIMESTAMP | | Last update time |

## Relationships

- TrainID → Trains.TrainID

---

# Table: Quotas

## Purpose

Stores reservation quota information for trains.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| QuotaID | UUID | PK | Unique quota identifier |
| TrainID | UUID | FK | Train reference |
| FromStationID | UUID | FK | Boarding station |
| ToStationID | UUID | FK | Destination station |
| QuotaType | VARCHAR(20) | | GNWL, RLWL, PQWL, TQWL, LD, etc. |
| CreatedAt | TIMESTAMP | | Record creation time |
| UpdatedAt | TIMESTAMP | | Last update time |

## Relationships

- TrainID → Trains.TrainID
- FromStationID → Stations.StationID
- ToStationID → Stations.StationID

---

# Table: SeatAvailability

## Purpose

Stores historical seat availability and waiting list data.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| AvailabilityID | UUID | PK | Unique availability record |
| TrainRunID | UUID | FK | Train run reference |
| CoachType | VARCHAR(20) | | Coach class |
| QuotaType | VARCHAR(20) | | Reservation quota |
| AvailableSeats | INTEGER | | Available seats |
| RACCount | INTEGER | | RAC count |
| WaitingListCount | INTEGER | | Waiting list count |
| CapturedAt | TIMESTAMP | | Snapshot timestamp |

## Relationships

- TrainRunID → TrainRuns.TrainRunID

---

# Table: Predictions

## Purpose

Stores AI prediction results.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| PredictionID | UUID | PK | Unique prediction identifier |
| TrainRunID | UUID | FK | Train run reference |
| PredictionPercentage | DECIMAL(5,2) | | Confirmation probability |
| ConfidenceScore | DECIMAL(5,2) | | AI confidence score |
| ModelVersion | VARCHAR(50) | | AI model version |
| CreatedAt | TIMESTAMP | | Prediction timestamp |

## Relationships

- TrainRunID → TrainRuns.TrainRunID

---

# Table: Users

## Purpose

Stores user account information.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| UserID | UUID | PK | Unique user identifier |
| FullName | VARCHAR(100) | | User's full name |
| Email | VARCHAR(255) | UNIQUE | Email address |
| MobileNumber | VARCHAR(20) | | Mobile number |
| PasswordHash | TEXT | | Encrypted password |
| IsVerified | BOOLEAN | | Email/mobile verification status |
| CreatedAt | TIMESTAMP | | Account creation time |
| UpdatedAt | TIMESTAMP | | Last update time |

---

# Table: SearchHistory

## Purpose

Stores user search history.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| SearchID | UUID | PK | Unique search identifier |
| UserID | UUID | FK | User reference |
| FromStationID | UUID | FK | Source station |
| ToStationID | UUID | FK | Destination station |
| JourneyDate | DATE | | Journey date |
| CoachType | VARCHAR(20) | | Coach selected |
| QuotaType | VARCHAR(20) |
---

# Table: TrainClasses

## Purpose

Stores the master list of all railway coach classes.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| ClassID | UUID | PK | Unique class identifier |
| ClassCode | VARCHAR(10) | UNIQUE | SL, 3A, 2A, 1A, CC, EC, 3E, etc. |
| ClassName | VARCHAR(100) | | Full class name |
| IsAC | BOOLEAN | | AC or Non-AC |
| IsActive | BOOLEAN | | Active class |
| CreatedAt | TIMESTAMP | | Record creation time |
| UpdatedAt | TIMESTAMP | | Last update time |

---

# Table: BoardingStations

## Purpose

Stores boarding station changes selected by users.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| BoardingID | UUID | PK | Unique boarding record |
| UserID | UUID | FK | User reference |
| TrainRunID | UUID | FK | Train run |
| OriginalStationID | UUID | FK | Original boarding station |
| BoardingStationID | UUID | FK | New boarding station |
| UpdatedAt | TIMESTAMP | | Change timestamp |

---

# Table: ReservationCharts

## Purpose

Stores reservation chart preparation details.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| ChartID | UUID | PK | Unique chart identifier |
| TrainRunID | UUID | FK | Train run |
| ChartType | VARCHAR(30) | | First Chart, Final Chart |
| PreparedAt | TIMESTAMP | | Chart preparation time |
| CreatedAt | TIMESTAMP | | Record creation time |

---

# Table: CoachComposition

## Purpose

Stores the coach composition of a train.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| CompositionID | UUID | PK | Unique composition ID |
| TrainRunID | UUID | FK | Train run |
| CoachNumber | VARCHAR(20) | | B1, S1, A1, etc. |
| CoachType | VARCHAR(20) | | Coach class |
| Position | INTEGER | | Coach position |
| CreatedAt | TIMESTAMP | | Record creation time |

---

# Table: TrainCancellations

## Purpose

Stores cancelled train information.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| CancellationID | UUID | PK | Unique cancellation record |
| TrainRunID | UUID | FK | Train run |
| CancellationReason | TEXT | | Reason |
| CancelledAt | TIMESTAMP | | Cancellation time |
| CreatedAt | TIMESTAMP | | Record creation time |

---

# Table: Diversions

## Purpose

Stores diverted train information.

## Columns

| Column | Data Type | PK/FK | Description |
|---------|-----------|-------|-------------|
| DiversionID | UUID | PK | Unique diversion record |