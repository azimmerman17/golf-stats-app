# DESERT WILLOW GOLF RESORT SEED DATA - TEST FOR LOADING FACILITY WITH MULTIPLE GOLF COURSES, through a GHIN JSON
course_seed1 = {
	"GHIN": True,
	# Keys with values, cannot be accuratly defined through the ghin dataset
	"OVERRIDE": {
		"FACILITY": {
			"COURSE_COUNT": None,  
			"CLASSIFICATION": "R",
			"CITY": None,  # required for courses outide USA and Canada
			"STATE": None,
			"COUNTRY": None,  # required for courses outide USA and Canada
			"WEBSITE":  "www.desertwillow.com",
			"ESTABLISHED": 1997,
			"HANDLE": "desertwillowgr"  # this data is required, a None value will cause error 
		},
		"COURSE": [{
			"HOLE_COUNT": None,
			"ESTABLISHED": 1998,
			"ARCHITECT": "Michael J. Hurdzan",
			"EFFECTIVE_DATE": None  # if none will default to current date
		}, {
			"HOLE_COUNT": None,
			"ESTABLISHED": 1997,
			"ARCHITECT": "Michael J. Hurdzan",
			"EFFECTIVE_DATE": None # if none will default to current date
		}]
	},
	"DATA": [{
	"Facility": {
		"FacilityId": 2307,
		"FacilityStatus": "Active",
		"FacilityName": "Desert Willow Golf Resort",
		"FacilityNumber": None,
		"GolfAssociationId": 73,
		"GeoLocationFormattedAddress": "38-995 Desert Willow Dr, Palm Desert, CA 92260, USA",
		"GeoLocationLongitude": -116.365359,
		"GeoLocationLatitude": 33.766789
	},
	"Season": {
		"SeasonName": "All Year Round",
		"SeasonStartDate": "01/01",
		"SeasonEndDate": "12/31",
		"IsAllYear": True
	},
	"TeeSets": [
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 71.2,
					"SlopeRating": 128,
					"BogeyRating": 95
				},
				{
					"RatingType": "Front",
					"CourseRating": 35.4,
					"SlopeRating": 127,
					"BogeyRating": 47.2
				},
				{
					"RatingType": "Back",
					"CourseRating": 35.8,
					"SlopeRating": 129,
					"BogeyRating": 47.8
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 393671,
					"Length": 398,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 393672,
					"Length": 372,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 3,
					"HoleId": 393673,
					"Length": 436,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 4,
					"HoleId": 393674,
					"Length": 350,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 393675,
					"Length": 192,
					"Par": 3,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 393676,
					"Length": 455,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 7,
					"HoleId": 393677,
					"Length": 362,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 393678,
					"Length": 153,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 393679,
					"Length": 527,
					"Par": 5,
					"Allocation": 15
				},
				{
					"Number": 10,
					"HoleId": 393680,
					"Length": 391,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 393681,
					"Length": 172,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 12,
					"HoleId": 393682,
					"Length": 483,
					"Par": 5,
					"Allocation": 18
				},
				{
					"Number": 13,
					"HoleId": 393683,
					"Length": 181,
					"Par": 3,
					"Allocation": 14
				},
				{
					"Number": 14,
					"HoleId": 393684,
					"Length": 426,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 393685,
					"Length": 404,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 16,
					"HoleId": 393686,
					"Length": 362,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 17,
					"HoleId": 393687,
					"Length": 318,
					"Par": 4,
					"Allocation": 16
				},
				{
					"Number": 18,
					"HoleId": 393688,
					"Length": 514,
					"Par": 5,
					"Allocation": 12
				}
			],
			"TeeSetRatingId": 148900,
			"TeeSetRatingName": "Purple",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 6496,
			"TotalMeters": 5940,
			"LegacyCRPTeeId": 253116,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 73,
					"SlopeRating": 132,
					"BogeyRating": 97.6
				},
				{
					"RatingType": "Back",
					"CourseRating": 36.6,
					"SlopeRating": 133,
					"BogeyRating": 49
				},
				{
					"RatingType": "Front",
					"CourseRating": 36.4,
					"SlopeRating": 131,
					"BogeyRating": 48.6
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 216587,
					"Length": 415,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 216588,
					"Length": 391,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 3,
					"HoleId": 216589,
					"Length": 450,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 4,
					"HoleId": 216590,
					"Length": 374,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 216591,
					"Length": 226,
					"Par": 3,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 216592,
					"Length": 479,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 7,
					"HoleId": 216593,
					"Length": 388,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 216594,
					"Length": 175,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 216595,
					"Length": 550,
					"Par": 5,
					"Allocation": 15
				},
				{
					"Number": 10,
					"HoleId": 216596,
					"Length": 409,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 216597,
					"Length": 198,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 12,
					"HoleId": 216598,
					"Length": 497,
					"Par": 5,
					"Allocation": 18
				},
				{
					"Number": 13,
					"HoleId": 216599,
					"Length": 195,
					"Par": 3,
					"Allocation": 14
				},
				{
					"Number": 14,
					"HoleId": 216600,
					"Length": 446,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 216601,
					"Length": 424,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 16,
					"HoleId": 216602,
					"Length": 383,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 17,
					"HoleId": 216603,
					"Length": 340,
					"Par": 4,
					"Allocation": 16
				},
				{
					"Number": 18,
					"HoleId": 216604,
					"Length": 537,
					"Par": 5,
					"Allocation": 12
				}
			],
			"TeeSetRatingId": 148901,
			"TeeSetRatingName": "Black",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 6877,
			"TotalMeters": 6288,
			"LegacyCRPTeeId": 253117,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 72.4,
					"SlopeRating": 134,
					"BogeyRating": 103.9
				},
				{
					"RatingType": "Back",
					"CourseRating": 36.3,
					"SlopeRating": 138,
					"BogeyRating": 52.6
				},
				{
					"RatingType": "Front",
					"CourseRating": 36.1,
					"SlopeRating": 129,
					"BogeyRating": 51.3
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 866351,
					"Length": 343,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 2,
					"HoleId": 866352,
					"Length": 324,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 3,
					"HoleId": 866353,
					"Length": 376,
					"Par": 4,
					"Allocation": 11
				},
				{
					"Number": 4,
					"HoleId": 866354,
					"Length": 305,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 866355,
					"Length": 148,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 6,
					"HoleId": 866356,
					"Length": 393,
					"Par": 5,
					"Allocation": 1
				},
				{
					"Number": 7,
					"HoleId": 866357,
					"Length": 309,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 866358,
					"Length": 124,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 866359,
					"Length": 426,
					"Par": 5,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 866360,
					"Length": 323,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 11,
					"HoleId": 866361,
					"Length": 125,
					"Par": 3,
					"Allocation": 10
				},
				{
					"Number": 12,
					"HoleId": 866362,
					"Length": 440,
					"Par": 5,
					"Allocation": 16
				},
				{
					"Number": 13,
					"HoleId": 866363,
					"Length": 139,
					"Par": 3,
					"Allocation": 18
				},
				{
					"Number": 14,
					"HoleId": 866364,
					"Length": 366,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 866365,
					"Length": 360,
					"Par": 4,
					"Allocation": 14
				},
				{
					"Number": 16,
					"HoleId": 866366,
					"Length": 306,
					"Par": 4,
					"Allocation": 12
				},
				{
					"Number": 17,
					"HoleId": 866367,
					"Length": 284,
					"Par": 4,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 866368,
					"Length": 460,
					"Par": 5,
					"Allocation": 6
				}
			],
			"TeeSetRatingId": 208553,
			"TeeSetRatingName": "Tan",
			"Gender": "Female",
			"HolesNumber": 18,
			"TotalYardage": 5551,
			"TotalMeters": 5076,
			"LegacyCRPTeeId": 157233,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 69.6,
					"SlopeRating": 126,
					"BogeyRating": 99.3
				},
				{
					"RatingType": "Back",
					"CourseRating": 35,
					"SlopeRating": 131,
					"BogeyRating": 50.5
				},
				{
					"RatingType": "Front",
					"CourseRating": 34.6,
					"SlopeRating": 120,
					"BogeyRating": 48.8
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 1382996,
					"Length": 298,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 2,
					"HoleId": 1382997,
					"Length": 297,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 3,
					"HoleId": 1382998,
					"Length": 337,
					"Par": 4,
					"Allocation": 11
				},
				{
					"Number": 4,
					"HoleId": 1382999,
					"Length": 283,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 1383000,
					"Length": 123,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 6,
					"HoleId": 1383001,
					"Length": 360,
					"Par": 5,
					"Allocation": 1
				},
				{
					"Number": 7,
					"HoleId": 1383002,
					"Length": 271,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 1383003,
					"Length": 107,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 1383004,
					"Length": 399,
					"Par": 5,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 1383005,
					"Length": 296,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 11,
					"HoleId": 1383006,
					"Length": 116,
					"Par": 3,
					"Allocation": 10
				},
				{
					"Number": 12,
					"HoleId": 1383007,
					"Length": 400,
					"Par": 5,
					"Allocation": 16
				},
				{
					"Number": 13,
					"HoleId": 1383008,
					"Length": 120,
					"Par": 3,
					"Allocation": 18
				},
				{
					"Number": 14,
					"HoleId": 1383009,
					"Length": 338,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 1383010,
					"Length": 325,
					"Par": 4,
					"Allocation": 14
				},
				{
					"Number": 16,
					"HoleId": 1383011,
					"Length": 283,
					"Par": 4,
					"Allocation": 12
				},
				{
					"Number": 17,
					"HoleId": 1383012,
					"Length": 252,
					"Par": 4,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 1383013,
					"Length": 427,
					"Par": 5,
					"Allocation": 6
				}
			],
			"TeeSetRatingId": 208555,
			"TeeSetRatingName": "Green",
			"Gender": "Female",
			"HolesNumber": 18,
			"TotalYardage": 5032,
			"TotalMeters": 4601,
			"LegacyCRPTeeId": 157235,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 75.4,
					"SlopeRating": 139,
					"BogeyRating": 108.2
				},
				{
					"RatingType": "Back",
					"CourseRating": 37.7,
					"SlopeRating": 143,
					"BogeyRating": 54.6
				},
				{
					"RatingType": "Front",
					"CourseRating": 37.7,
					"SlopeRating": 135,
					"BogeyRating": 53.6
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 1924022,
					"Length": 371,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 2,
					"HoleId": 1924023,
					"Length": 357,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 3,
					"HoleId": 1924024,
					"Length": 416,
					"Par": 4,
					"Allocation": 11
				},
				{
					"Number": 4,
					"HoleId": 1924025,
					"Length": 324,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 1924026,
					"Length": 172,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 6,
					"HoleId": 1924027,
					"Length": 433,
					"Par": 5,
					"Allocation": 1
				},
				{
					"Number": 7,
					"HoleId": 1924028,
					"Length": 339,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 1924029,
					"Length": 146,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 1924030,
					"Length": 479,
					"Par": 5,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 1924031,
					"Length": 363,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 11,
					"HoleId": 1924032,
					"Length": 157,
					"Par": 3,
					"Allocation": 10
				},
				{
					"Number": 12,
					"HoleId": 1924033,
					"Length": 465,
					"Par": 5,
					"Allocation": 16
				},
				{
					"Number": 13,
					"HoleId": 1924034,
					"Length": 160,
					"Par": 3,
					"Allocation": 18
				},
				{
					"Number": 14,
					"HoleId": 1924035,
					"Length": 398,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 1924036,
					"Length": 381,
					"Par": 4,
					"Allocation": 14
				},
				{
					"Number": 16,
					"HoleId": 1924037,
					"Length": 345,
					"Par": 4,
					"Allocation": 12
				},
				{
					"Number": 17,
					"HoleId": 1924038,
					"Length": 300,
					"Par": 4,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 1924039,
					"Length": 485,
					"Par": 5,
					"Allocation": 6
				}
			],
			"TeeSetRatingId": 208558,
			"TeeSetRatingName": "White",
			"Gender": "Female",
			"HolesNumber": 18,
			"TotalYardage": 6091,
			"TotalMeters": 5570,
			"LegacyCRPTeeId": 157239,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 69.4,
					"SlopeRating": 124,
					"BogeyRating": 92.4
				},
				{
					"RatingType": "Front",
					"CourseRating": 34.5,
					"SlopeRating": 123,
					"BogeyRating": 45.9
				},
				{
					"RatingType": "Back",
					"CourseRating": 34.9,
					"SlopeRating": 125,
					"BogeyRating": 46.5
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 1924004,
					"Length": 371,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 1924005,
					"Length": 357,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 3,
					"HoleId": 1924006,
					"Length": 416,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 4,
					"HoleId": 1924007,
					"Length": 324,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 1924008,
					"Length": 172,
					"Par": 3,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 1924009,
					"Length": 420,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 7,
					"HoleId": 1924010,
					"Length": 339,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 1924011,
					"Length": 146,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 1924012,
					"Length": 502,
					"Par": 5,
					"Allocation": 15
				},
				{
					"Number": 10,
					"HoleId": 1924013,
					"Length": 363,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 1924014,
					"Length": 157,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 12,
					"HoleId": 1924015,
					"Length": 465,
					"Par": 5,
					"Allocation": 18
				},
				{
					"Number": 13,
					"HoleId": 1924016,
					"Length": 160,
					"Par": 3,
					"Allocation": 14
				},
				{
					"Number": 14,
					"HoleId": 1924017,
					"Length": 398,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 1924018,
					"Length": 381,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 16,
					"HoleId": 1924019,
					"Length": 345,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 17,
					"HoleId": 1924020,
					"Length": 300,
					"Par": 4,
					"Allocation": 16
				},
				{
					"Number": 18,
					"HoleId": 1924021,
					"Length": 485,
					"Par": 5,
					"Allocation": 12
				}
			],
			"TeeSetRatingId": 270535,
			"TeeSetRatingName": "White",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 6101,
			"TotalMeters": 5579,
			"LegacyCRPTeeId": 253118,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 66.6,
					"SlopeRating": 117,
					"BogeyRating": 88.3
				},
				{
					"RatingType": "Back",
					"CourseRating": 33.5,
					"SlopeRating": 120,
					"BogeyRating": 44.6
				},
				{
					"RatingType": "Front",
					"CourseRating": 33.1,
					"SlopeRating": 114,
					"BogeyRating": 43.7
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 866333,
					"Length": 343,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 866334,
					"Length": 324,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 3,
					"HoleId": 866335,
					"Length": 376,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 4,
					"HoleId": 866336,
					"Length": 305,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 866337,
					"Length": 148,
					"Par": 3,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 866338,
					"Length": 380,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 7,
					"HoleId": 866339,
					"Length": 309,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 866340,
					"Length": 124,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 866341,
					"Length": 426,
					"Par": 5,
					"Allocation": 15
				},
				{
					"Number": 10,
					"HoleId": 866342,
					"Length": 323,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 866343,
					"Length": 125,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 12,
					"HoleId": 866344,
					"Length": 440,
					"Par": 5,
					"Allocation": 18
				},
				{
					"Number": 13,
					"HoleId": 866345,
					"Length": 139,
					"Par": 3,
					"Allocation": 14
				},
				{
					"Number": 14,
					"HoleId": 866346,
					"Length": 366,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 866347,
					"Length": 360,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 16,
					"HoleId": 866348,
					"Length": 306,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 17,
					"HoleId": 866349,
					"Length": 284,
					"Par": 4,
					"Allocation": 16
				},
				{
					"Number": 18,
					"HoleId": 866350,
					"Length": 460,
					"Par": 5,
					"Allocation": 12
				}
			],
			"TeeSetRatingId": 270536,
			"TeeSetRatingName": "Tan",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 5538,
			"TotalMeters": 5064,
			"LegacyCRPTeeId": 253119,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 64,
					"SlopeRating": 110,
					"BogeyRating": 84.3
				},
				{
					"RatingType": "Back",
					"CourseRating": 32.2,
					"SlopeRating": 112,
					"BogeyRating": 42.6
				},
				{
					"RatingType": "Front",
					"CourseRating": 31.8,
					"SlopeRating": 107,
					"BogeyRating": 41.7
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 1382978,
					"Length": 298,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 1382979,
					"Length": 297,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 3,
					"HoleId": 1382980,
					"Length": 337,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 4,
					"HoleId": 1382981,
					"Length": 284,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 1382982,
					"Length": 123,
					"Par": 3,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 1382983,
					"Length": 348,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 7,
					"HoleId": 1382984,
					"Length": 271,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 1382985,
					"Length": 107,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 1382986,
					"Length": 399,
					"Par": 5,
					"Allocation": 15
				},
				{
					"Number": 10,
					"HoleId": 1382987,
					"Length": 296,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 1382988,
					"Length": 116,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 12,
					"HoleId": 1382989,
					"Length": 400,
					"Par": 5,
					"Allocation": 18
				},
				{
					"Number": 13,
					"HoleId": 1382990,
					"Length": 120,
					"Par": 3,
					"Allocation": 14
				},
				{
					"Number": 14,
					"HoleId": 1382991,
					"Length": 338,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 1382992,
					"Length": 325,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 16,
					"HoleId": 1382993,
					"Length": 283,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 17,
					"HoleId": 1382994,
					"Length": 252,
					"Par": 4,
					"Allocation": 16
				},
				{
					"Number": 18,
					"HoleId": 1382995,
					"Length": 427,
					"Par": 5,
					"Allocation": 12
				}
			],
			"TeeSetRatingId": 270539,
			"TeeSetRatingName": "Green",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 5021,
			"TotalMeters": 4591,
			"LegacyCRPTeeId": 253123,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 70.3,
					"SlopeRating": 126,
					"BogeyRating": 93.7
				},
				{
					"RatingType": "Back",
					"CourseRating": 35.4,
					"SlopeRating": 127,
					"BogeyRating": 47.2
				},
				{
					"RatingType": "Front",
					"CourseRating": 34.9,
					"SlopeRating": 125,
					"BogeyRating": 46.5
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 1924004,
					"Length": 371,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 1924005,
					"Length": 357,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 3,
					"HoleId": 1924006,
					"Length": 416,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 4,
					"HoleId": 1924007,
					"Length": 324,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 1924008,
					"Length": 172,
					"Par": 3,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 393676,
					"Length": 455,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 7,
					"HoleId": 393677,
					"Length": 362,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 393678,
					"Length": 153,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 393679,
					"Length": 527,
					"Par": 5,
					"Allocation": 15
				},
				{
					"Number": 10,
					"HoleId": 393680,
					"Length": 391,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 1924014,
					"Length": 157,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 12,
					"HoleId": 393682,
					"Length": 483,
					"Par": 5,
					"Allocation": 18
				},
				{
					"Number": 13,
					"HoleId": 393683,
					"Length": 181,
					"Par": 3,
					"Allocation": 14
				},
				{
					"Number": 14,
					"HoleId": 1924017,
					"Length": 398,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 1924018,
					"Length": 381,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 16,
					"HoleId": 1924019,
					"Length": 345,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 17,
					"HoleId": 393687,
					"Length": 318,
					"Par": 4,
					"Allocation": 16
				},
				{
					"Number": 18,
					"HoleId": 393688,
					"Length": 514,
					"Par": 5,
					"Allocation": 12
				}
			],
			"TeeSetRatingId": 299375,
			"TeeSetRatingName": "Purple/White",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 6305,
			"TotalMeters": 5765,
			"LegacyCRPTeeId": 377063,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 70.9,
					"SlopeRating": 130,
					"BogeyRating": 101.4
				},
				{
					"RatingType": "Back",
					"CourseRating": 35.6,
					"SlopeRating": 135,
					"BogeyRating": 51.5
				},
				{
					"RatingType": "Front",
					"CourseRating": 35.3,
					"SlopeRating": 124,
					"BogeyRating": 49.9
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 1382996,
					"Length": 298,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 2,
					"HoleId": 1382997,
					"Length": 297,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 3,
					"HoleId": 866353,
					"Length": 376,
					"Par": 4,
					"Allocation": 11
				},
				{
					"Number": 4,
					"HoleId": 1382999,
					"Length": 283,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 866355,
					"Length": 148,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 6,
					"HoleId": 1383001,
					"Length": 360,
					"Par": 5,
					"Allocation": 1
				},
				{
					"Number": 7,
					"HoleId": 866357,
					"Length": 309,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 866358,
					"Length": 124,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 1383004,
					"Length": 399,
					"Par": 5,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 1383005,
					"Length": 296,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 11,
					"HoleId": 866361,
					"Length": 125,
					"Par": 3,
					"Allocation": 10
				},
				{
					"Number": 12,
					"HoleId": 866362,
					"Length": 440,
					"Par": 5,
					"Allocation": 16
				},
				{
					"Number": 13,
					"HoleId": 866363,
					"Length": 139,
					"Par": 3,
					"Allocation": 18
				},
				{
					"Number": 14,
					"HoleId": 1383009,
					"Length": 338,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 866365,
					"Length": 360,
					"Par": 4,
					"Allocation": 14
				},
				{
					"Number": 16,
					"HoleId": 866366,
					"Length": 306,
					"Par": 4,
					"Allocation": 12
				},
				{
					"Number": 17,
					"HoleId": 1383012,
					"Length": 252,
					"Par": 4,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 1383013,
					"Length": 427,
					"Par": 5,
					"Allocation": 6
				}
			],
			"TeeSetRatingId": 543354,
			"TeeSetRatingName": "Tan/Green",
			"Gender": "Female",
			"HolesNumber": 18,
			"TotalYardage": 5277,
			"TotalMeters": 4825,
			"LegacyCRPTeeId": None,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 68.1,
					"SlopeRating": 121,
					"BogeyRating": 90.6
				},
				{
					"RatingType": "Front",
					"CourseRating": 33.8,
					"SlopeRating": 119,
					"BogeyRating": 44.9
				},
				{
					"RatingType": "Back",
					"CourseRating": 34.3,
					"SlopeRating": 123,
					"BogeyRating": 45.7
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 866333,
					"Length": 343,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 866334,
					"Length": 324,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 3,
					"HoleId": 866335,
					"Length": 376,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 4,
					"HoleId": 866336,
					"Length": 305,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 866337,
					"Length": 148,
					"Par": 3,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 1924009,
					"Length": 420,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 7,
					"HoleId": 1924010,
					"Length": 339,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 1924011,
					"Length": 146,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 1924012,
					"Length": 502,
					"Par": 5,
					"Allocation": 15
				},
				{
					"Number": 10,
					"HoleId": 1924013,
					"Length": 363,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 866343,
					"Length": 125,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 12,
					"HoleId": 1924015,
					"Length": 465,
					"Par": 5,
					"Allocation": 18
				},
				{
					"Number": 13,
					"HoleId": 1924016,
					"Length": 160,
					"Par": 3,
					"Allocation": 14
				},
				{
					"Number": 14,
					"HoleId": 866346,
					"Length": 366,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 866347,
					"Length": 360,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 16,
					"HoleId": 866348,
					"Length": 306,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 17,
					"HoleId": 1924020,
					"Length": 300,
					"Par": 4,
					"Allocation": 16
				},
				{
					"Number": 18,
					"HoleId": 1924021,
					"Length": 485,
					"Par": 5,
					"Allocation": 12
				}
			],
			"TeeSetRatingId": 622934,
			"TeeSetRatingName": "White/Tan",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 5833,
			"TotalMeters": 5334,
			"LegacyCRPTeeId": None,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 73.9,
					"SlopeRating": 137,
					"BogeyRating": 106.1
				},
				{
					"RatingType": "Back",
					"CourseRating": 37,
					"SlopeRating": 141,
					"BogeyRating": 53.6
				},
				{
					"RatingType": "Front",
					"CourseRating": 36.9,
					"SlopeRating": 132,
					"BogeyRating": 52.5
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 866351,
					"Length": 343,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 2,
					"HoleId": 866352,
					"Length": 324,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 3,
					"HoleId": 866353,
					"Length": 376,
					"Par": 4,
					"Allocation": 11
				},
				{
					"Number": 4,
					"HoleId": 866354,
					"Length": 305,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 866355,
					"Length": 148,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 6,
					"HoleId": 1924027,
					"Length": 433,
					"Par": 5,
					"Allocation": 1
				},
				{
					"Number": 7,
					"HoleId": 1924028,
					"Length": 339,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 8,
					"HoleId": 1924029,
					"Length": 146,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 1924030,
					"Length": 479,
					"Par": 5,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 1924031,
					"Length": 363,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 11,
					"HoleId": 866361,
					"Length": 125,
					"Par": 3,
					"Allocation": 10
				},
				{
					"Number": 12,
					"HoleId": 1924033,
					"Length": 465,
					"Par": 5,
					"Allocation": 16
				},
				{
					"Number": 13,
					"HoleId": 1924034,
					"Length": 160,
					"Par": 3,
					"Allocation": 18
				},
				{
					"Number": 14,
					"HoleId": 866364,
					"Length": 366,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 15,
					"HoleId": 866365,
					"Length": 360,
					"Par": 4,
					"Allocation": 14
				},
				{
					"Number": 16,
					"HoleId": 866366,
					"Length": 306,
					"Par": 4,
					"Allocation": 12
				},
				{
					"Number": 17,
					"HoleId": 1924038,
					"Length": 300,
					"Par": 4,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 1924039,
					"Length": 485,
					"Par": 5,
					"Allocation": 6
				}
			],
			"TeeSetRatingId": 622944,
			"TeeSetRatingName": "White/Tan",
			"Gender": "Female",
			"HolesNumber": 18,
			"TotalYardage": 5823,
			"TotalMeters": 5325,
			"LegacyCRPTeeId": None,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		}
	],
	"CourseId": 2366,
	"CourseName": "MOUNTAIN VIEW",
	"CourseStatus": "Active",
	"CourseNumber": None,
	"CourseCity": "Palm Desert",
	"CourseState": "US-CA"
}, {
	"Facility": {
		"FacilityId": 2307,
		"FacilityStatus": "Active",
		"FacilityName": "Desert Willow Golf Resort",
		"FacilityNumber": None,
		"GolfAssociationId": 73,
		"GeoLocationFormattedAddress": "38-995 Desert Willow Dr, Palm Desert, CA 92260, USA",
		"GeoLocationLongitude": -116.365359,
		"GeoLocationLatitude": 33.766789
	},
	"Season": {
		"SeasonName": "All Year Round",
		"SeasonStartDate": "01/01",
		"SeasonEndDate": "12/31",
		"IsAllYear": True
	},
	"TeeSets": [
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 72.5,
					"SlopeRating": 133,
					"BogeyRating": 103.8
				},
				{
					"RatingType": "Back",
					"CourseRating": 36.1,
					"SlopeRating": 131,
					"BogeyRating": 51.5
				},
				{
					"RatingType": "Front",
					"CourseRating": 36.4,
					"SlopeRating": 135,
					"BogeyRating": 52.3
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 866369,
					"Length": 445,
					"Par": 5,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 866370,
					"Length": 339,
					"Par": 4,
					"Allocation": 11
				},
				{
					"Number": 3,
					"HoleId": 866371,
					"Length": 126,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 866372,
					"Length": 354,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 866373,
					"Length": 337,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 6,
					"HoleId": 866374,
					"Length": 265,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 866375,
					"Length": 493,
					"Par": 5,
					"Allocation": 1
				},
				{
					"Number": 8,
					"HoleId": 866376,
					"Length": 105,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 866377,
					"Length": 370,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 10,
					"HoleId": 866378,
					"Length": 356,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 866379,
					"Length": 363,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 12,
					"HoleId": 866380,
					"Length": 337,
					"Par": 4,
					"Allocation": 12
				},
				{
					"Number": 13,
					"HoleId": 866381,
					"Length": 454,
					"Par": 5,
					"Allocation": 2
				},
				{
					"Number": 14,
					"HoleId": 866382,
					"Length": 120,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 866383,
					"Length": 255,
					"Par": 4,
					"Allocation": 14
				},
				{
					"Number": 16,
					"HoleId": 866384,
					"Length": 330,
					"Par": 4,
					"Allocation": 4
				},
				{
					"Number": 17,
					"HoleId": 866385,
					"Length": 153,
					"Par": 3,
					"Allocation": 18
				},
				{
					"Number": 18,
					"HoleId": 866386,
					"Length": 410,
					"Par": 5,
					"Allocation": 6
				}
			],
			"TeeSetRatingId": 208559,
			"TeeSetRatingName": "Tan",
			"Gender": "Female",
			"HolesNumber": 18,
			"TotalYardage": 5612,
			"TotalMeters": 5132,
			"LegacyCRPTeeId": 157240,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 72.1,
					"SlopeRating": 136,
					"BogeyRating": 97.2
				},
				{
					"RatingType": "Back",
					"CourseRating": 36,
					"SlopeRating": 136,
					"BogeyRating": 48.6
				},
				{
					"RatingType": "Front",
					"CourseRating": 36.1,
					"SlopeRating": 135,
					"BogeyRating": 48.6
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 2574908,
					"Length": 516,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 2,
					"HoleId": 2574909,
					"Length": 394,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 3,
					"HoleId": 2574910,
					"Length": 166,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 2574911,
					"Length": 427,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 5,
					"HoleId": 2574912,
					"Length": 400,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 2574913,
					"Length": 311,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 2574914,
					"Length": 545,
					"Par": 5,
					"Allocation": 7
				},
				{
					"Number": 8,
					"HoleId": 2574915,
					"Length": 138,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 2574916,
					"Length": 436,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 2574907,
					"Length": 420,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 11,
					"HoleId": 2574906,
					"Length": 429,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 12,
					"HoleId": 2574905,
					"Length": 395,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 13,
					"HoleId": 2574904,
					"Length": 523,
					"Par": 5,
					"Allocation": 12
				},
				{
					"Number": 14,
					"HoleId": 2574903,
					"Length": 161,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 2574902,
					"Length": 300,
					"Par": 4,
					"Allocation": 18
				},
				{
					"Number": 16,
					"HoleId": 2574901,
					"Length": 402,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 17,
					"HoleId": 2574900,
					"Length": 193,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 2574899,
					"Length": 512,
					"Par": 5,
					"Allocation": 14
				}
			],
			"TeeSetRatingId": 299387,
			"TeeSetRatingName": "Purple",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 6668,
			"TotalMeters": 6097,
			"LegacyCRPTeeId": 46189,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 71,
					"SlopeRating": 132,
					"BogeyRating": 95.5
				},
				{
					"RatingType": "Front",
					"CourseRating": 35.5,
					"SlopeRating": 130,
					"BogeyRating": 47.6
				},
				{
					"RatingType": "Back",
					"CourseRating": 35.5,
					"SlopeRating": 133,
					"BogeyRating": 47.9
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 2574908,
					"Length": 516,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 2,
					"HoleId": 2574919,
					"Length": 365,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 3,
					"HoleId": 2574910,
					"Length": 166,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 2574921,
					"Length": 387,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 5,
					"HoleId": 2574922,
					"Length": 377,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 2574913,
					"Length": 311,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 2574924,
					"Length": 517,
					"Par": 5,
					"Allocation": 7
				},
				{
					"Number": 8,
					"HoleId": 2574915,
					"Length": 138,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 2574926,
					"Length": 408,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 2574917,
					"Length": 393,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 11,
					"HoleId": 2574927,
					"Length": 395,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 12,
					"HoleId": 2574928,
					"Length": 366,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 13,
					"HoleId": 2574904,
					"Length": 523,
					"Par": 5,
					"Allocation": 12
				},
				{
					"Number": 14,
					"HoleId": 2574903,
					"Length": 161,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 2574902,
					"Length": 300,
					"Par": 4,
					"Allocation": 18
				},
				{
					"Number": 16,
					"HoleId": 2574901,
					"Length": 402,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 17,
					"HoleId": 2574933,
					"Length": 171,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 2574899,
					"Length": 512,
					"Par": 5,
					"Allocation": 14
				}
			],
			"TeeSetRatingId": 299389,
			"TeeSetRatingName": "Purple/White",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 6408,
			"TotalMeters": 5859,
			"LegacyCRPTeeId": 377065,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 74.1,
					"SlopeRating": 141,
					"BogeyRating": 100.2
				},
				{
					"RatingType": "Back",
					"CourseRating": 37.1,
					"SlopeRating": 141,
					"BogeyRating": 50.2
				},
				{
					"RatingType": "Front",
					"CourseRating": 37,
					"SlopeRating": 140,
					"BogeyRating": 50
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 2716337,
					"Length": 535,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 2,
					"HoleId": 2716338,
					"Length": 413,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 3,
					"HoleId": 2716339,
					"Length": 194,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 2716340,
					"Length": 448,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 5,
					"HoleId": 2716341,
					"Length": 429,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 2716342,
					"Length": 331,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 2716343,
					"Length": 569,
					"Par": 5,
					"Allocation": 7
				},
				{
					"Number": 8,
					"HoleId": 2716344,
					"Length": 155,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 2716345,
					"Length": 455,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 2716336,
					"Length": 435,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 11,
					"HoleId": 2716335,
					"Length": 452,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 12,
					"HoleId": 2716334,
					"Length": 427,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 13,
					"HoleId": 2716333,
					"Length": 550,
					"Par": 5,
					"Allocation": 12
				},
				{
					"Number": 14,
					"HoleId": 2716332,
					"Length": 176,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 2716331,
					"Length": 332,
					"Par": 4,
					"Allocation": 18
				},
				{
					"Number": 16,
					"HoleId": 2716330,
					"Length": 420,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 17,
					"HoleId": 2716329,
					"Length": 203,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 2716328,
					"Length": 536,
					"Par": 5,
					"Allocation": 14
				}
			],
			"TeeSetRatingId": 338224,
			"TeeSetRatingName": "Black",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 7060,
			"TotalMeters": 6456,
			"LegacyCRPTeeId": 46188,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 69.9,
					"SlopeRating": 128,
					"BogeyRating": 93.7
				},
				{
					"RatingType": "Back",
					"CourseRating": 34.9,
					"SlopeRating": 130,
					"BogeyRating": 47
				},
				{
					"RatingType": "Front",
					"CourseRating": 35,
					"SlopeRating": 126,
					"BogeyRating": 46.7
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 2574918,
					"Length": 486,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 2,
					"HoleId": 2574919,
					"Length": 365,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 3,
					"HoleId": 2574920,
					"Length": 137,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 2574921,
					"Length": 387,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 5,
					"HoleId": 2574922,
					"Length": 377,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 2574923,
					"Length": 281,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 2574924,
					"Length": 517,
					"Par": 5,
					"Allocation": 7
				},
				{
					"Number": 8,
					"HoleId": 2574925,
					"Length": 119,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 2574926,
					"Length": 408,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 2574917,
					"Length": 393,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 11,
					"HoleId": 2574927,
					"Length": 395,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 12,
					"HoleId": 2574928,
					"Length": 366,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 13,
					"HoleId": 2574929,
					"Length": 502,
					"Par": 5,
					"Allocation": 12
				},
				{
					"Number": 14,
					"HoleId": 2574930,
					"Length": 140,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 2574931,
					"Length": 277,
					"Par": 4,
					"Allocation": 18
				},
				{
					"Number": 16,
					"HoleId": 2574932,
					"Length": 366,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 17,
					"HoleId": 2574933,
					"Length": 171,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 2574934,
					"Length": 467,
					"Par": 5,
					"Allocation": 14
				}
			],
			"TeeSetRatingId": 338227,
			"TeeSetRatingName": "White",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 6154,
			"TotalMeters": 5627,
			"LegacyCRPTeeId": 46191,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 67.5,
					"SlopeRating": 120,
					"BogeyRating": 89.8
				},
				{
					"RatingType": "Back",
					"CourseRating": 33.7,
					"SlopeRating": 118,
					"BogeyRating": 44.7
				},
				{
					"RatingType": "Front",
					"CourseRating": 33.8,
					"SlopeRating": 122,
					"BogeyRating": 45.1
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 2716347,
					"Length": 445,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 2,
					"HoleId": 2716348,
					"Length": 339,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 3,
					"HoleId": 2716349,
					"Length": 126,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 2716350,
					"Length": 354,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 5,
					"HoleId": 2716351,
					"Length": 337,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 2716352,
					"Length": 265,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 2716353,
					"Length": 493,
					"Par": 5,
					"Allocation": 7
				},
				{
					"Number": 8,
					"HoleId": 2716354,
					"Length": 105,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 2716355,
					"Length": 370,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 2716346,
					"Length": 356,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 11,
					"HoleId": 2716356,
					"Length": 363,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 12,
					"HoleId": 2716357,
					"Length": 337,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 13,
					"HoleId": 2716358,
					"Length": 454,
					"Par": 5,
					"Allocation": 12
				},
				{
					"Number": 14,
					"HoleId": 2716359,
					"Length": 120,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 2716360,
					"Length": 255,
					"Par": 4,
					"Allocation": 18
				},
				{
					"Number": 16,
					"HoleId": 2716361,
					"Length": 330,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 17,
					"HoleId": 2716362,
					"Length": 153,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 2716363,
					"Length": 410,
					"Par": 5,
					"Allocation": 14
				}
			],
			"TeeSetRatingId": 338228,
			"TeeSetRatingName": "Tan",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 5612,
			"TotalMeters": 5132,
			"LegacyCRPTeeId": 46190,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 75.7,
					"SlopeRating": 140,
					"BogeyRating": 108.6
				},
				{
					"RatingType": "Back",
					"CourseRating": 37.8,
					"SlopeRating": 138,
					"BogeyRating": 54.1
				},
				{
					"RatingType": "Front",
					"CourseRating": 37.9,
					"SlopeRating": 141,
					"BogeyRating": 54.5
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 1924040,
					"Length": 486,
					"Par": 5,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 1924041,
					"Length": 365,
					"Par": 4,
					"Allocation": 11
				},
				{
					"Number": 3,
					"HoleId": 1924042,
					"Length": 137,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 1924043,
					"Length": 387,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 1924044,
					"Length": 377,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 6,
					"HoleId": 1924045,
					"Length": 281,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 1924046,
					"Length": 517,
					"Par": 5,
					"Allocation": 1
				},
				{
					"Number": 8,
					"HoleId": 1924047,
					"Length": 119,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 1924048,
					"Length": 408,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 10,
					"HoleId": 1924049,
					"Length": 393,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 1924050,
					"Length": 395,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 12,
					"HoleId": 1924051,
					"Length": 366,
					"Par": 4,
					"Allocation": 12
				},
				{
					"Number": 13,
					"HoleId": 1924052,
					"Length": 502,
					"Par": 5,
					"Allocation": 2
				},
				{
					"Number": 14,
					"HoleId": 1924053,
					"Length": 140,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 1924054,
					"Length": 277,
					"Par": 4,
					"Allocation": 14
				},
				{
					"Number": 16,
					"HoleId": 1924055,
					"Length": 366,
					"Par": 4,
					"Allocation": 4
				},
				{
					"Number": 17,
					"HoleId": 1924056,
					"Length": 171,
					"Par": 3,
					"Allocation": 18
				},
				{
					"Number": 18,
					"HoleId": 1924057,
					"Length": 467,
					"Par": 5,
					"Allocation": 6
				}
			],
			"TeeSetRatingId": 338230,
			"TeeSetRatingName": "White",
			"Gender": "Female",
			"HolesNumber": 18,
			"TotalYardage": 6154,
			"TotalMeters": 5627,
			"LegacyCRPTeeId": 157242,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 65,
					"SlopeRating": 112,
					"BogeyRating": 85.7
				},
				{
					"RatingType": "Back",
					"CourseRating": 32.4,
					"SlopeRating": 111,
					"BogeyRating": 42.7
				},
				{
					"RatingType": "Front",
					"CourseRating": 32.6,
					"SlopeRating": 112,
					"BogeyRating": 43
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 2716383,
					"Length": 416,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 2,
					"HoleId": 2716384,
					"Length": 313,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 3,
					"HoleId": 2716385,
					"Length": 107,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 2716386,
					"Length": 315,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 5,
					"HoleId": 2716387,
					"Length": 302,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 2716388,
					"Length": 235,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 2716389,
					"Length": 465,
					"Par": 5,
					"Allocation": 7
				},
				{
					"Number": 8,
					"HoleId": 2716390,
					"Length": 80,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 2716391,
					"Length": 321,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 2716382,
					"Length": 323,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 11,
					"HoleId": 2716392,
					"Length": 331,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 12,
					"HoleId": 2716393,
					"Length": 313,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 13,
					"HoleId": 2716394,
					"Length": 425,
					"Par": 5,
					"Allocation": 12
				},
				{
					"Number": 14,
					"HoleId": 2716395,
					"Length": 98,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 2716396,
					"Length": 225,
					"Par": 4,
					"Allocation": 18
				},
				{
					"Number": 16,
					"HoleId": 2716397,
					"Length": 298,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 17,
					"HoleId": 2716398,
					"Length": 129,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 2716399,
					"Length": 386,
					"Par": 5,
					"Allocation": 14
				}
			],
			"TeeSetRatingId": 451447,
			"TeeSetRatingName": "Green",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 5082,
			"TotalMeters": 4647,
			"LegacyCRPTeeId": None,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 69.4,
					"SlopeRating": 127,
					"BogeyRating": 99.2
				},
				{
					"RatingType": "Back",
					"CourseRating": 34.8,
					"SlopeRating": 125,
					"BogeyRating": 49.5
				},
				{
					"RatingType": "Front",
					"CourseRating": 34.6,
					"SlopeRating": 128,
					"BogeyRating": 49.7
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 1383014,
					"Length": 416,
					"Par": 5,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 1383015,
					"Length": 313,
					"Par": 4,
					"Allocation": 11
				},
				{
					"Number": 3,
					"HoleId": 1383016,
					"Length": 107,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 1383017,
					"Length": 315,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 1383018,
					"Length": 302,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 6,
					"HoleId": 1383019,
					"Length": 235,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 1383020,
					"Length": 465,
					"Par": 5,
					"Allocation": 1
				},
				{
					"Number": 8,
					"HoleId": 1383021,
					"Length": 80,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 1383022,
					"Length": 321,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 10,
					"HoleId": 1383023,
					"Length": 323,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 1383024,
					"Length": 331,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 12,
					"HoleId": 1383025,
					"Length": 313,
					"Par": 4,
					"Allocation": 12
				},
				{
					"Number": 13,
					"HoleId": 1383026,
					"Length": 425,
					"Par": 5,
					"Allocation": 2
				},
				{
					"Number": 14,
					"HoleId": 1383027,
					"Length": 98,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 1383028,
					"Length": 225,
					"Par": 4,
					"Allocation": 14
				},
				{
					"Number": 16,
					"HoleId": 1383029,
					"Length": 298,
					"Par": 4,
					"Allocation": 4
				},
				{
					"Number": 17,
					"HoleId": 1383030,
					"Length": 129,
					"Par": 3,
					"Allocation": 18
				},
				{
					"Number": 18,
					"HoleId": 1383031,
					"Length": 386,
					"Par": 5,
					"Allocation": 6
				}
			],
			"TeeSetRatingId": 451450,
			"TeeSetRatingName": "Green",
			"Gender": "Female",
			"HolesNumber": 18,
			"TotalYardage": 5082,
			"TotalMeters": 4647,
			"LegacyCRPTeeId": None,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 70.8,
					"SlopeRating": 130,
					"BogeyRating": 101.5
				},
				{
					"RatingType": "Front",
					"CourseRating": 35.3,
					"SlopeRating": 132,
					"BogeyRating": 50.9
				},
				{
					"RatingType": "Back",
					"CourseRating": 35.5,
					"SlopeRating": 128,
					"BogeyRating": 50.6
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 1383014,
					"Length": 416,
					"Par": 5,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 866370,
					"Length": 339,
					"Par": 4,
					"Allocation": 11
				},
				{
					"Number": 3,
					"HoleId": 866371,
					"Length": 126,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 1383017,
					"Length": 315,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 1383018,
					"Length": 302,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 6,
					"HoleId": 866374,
					"Length": 265,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 1383020,
					"Length": 465,
					"Par": 5,
					"Allocation": 1
				},
				{
					"Number": 8,
					"HoleId": 866376,
					"Length": 105,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 1383022,
					"Length": 321,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 10,
					"HoleId": 866378,
					"Length": 356,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 1383024,
					"Length": 331,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 12,
					"HoleId": 866380,
					"Length": 337,
					"Par": 4,
					"Allocation": 12
				},
				{
					"Number": 13,
					"HoleId": 1383026,
					"Length": 425,
					"Par": 5,
					"Allocation": 2
				},
				{
					"Number": 14,
					"HoleId": 866382,
					"Length": 120,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 866383,
					"Length": 255,
					"Par": 4,
					"Allocation": 14
				},
				{
					"Number": 16,
					"HoleId": 1383029,
					"Length": 298,
					"Par": 4,
					"Allocation": 4
				},
				{
					"Number": 17,
					"HoleId": 866385,
					"Length": 153,
					"Par": 3,
					"Allocation": 18
				},
				{
					"Number": 18,
					"HoleId": 1383031,
					"Length": 386,
					"Par": 5,
					"Allocation": 6
				}
			],
			"TeeSetRatingId": 543353,
			"TeeSetRatingName": "Tan/Green",
			"Gender": "Female",
			"HolesNumber": 18,
			"TotalYardage": 5315,
			"TotalMeters": 4860,
			"LegacyCRPTeeId": None,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 68.7,
					"SlopeRating": 124,
					"BogeyRating": 91.7
				},
				{
					"RatingType": "Back",
					"CourseRating": 34.4,
					"SlopeRating": 124,
					"BogeyRating": 45.9
				},
				{
					"RatingType": "Front",
					"CourseRating": 34.3,
					"SlopeRating": 124,
					"BogeyRating": 45.8
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 2574918,
					"Length": 486,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 2,
					"HoleId": 2716348,
					"Length": 339,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 3,
					"HoleId": 2574920,
					"Length": 137,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 2716350,
					"Length": 354,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 5,
					"HoleId": 2716351,
					"Length": 337,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 2574923,
					"Length": 281,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 2716353,
					"Length": 493,
					"Par": 5,
					"Allocation": 7
				},
				{
					"Number": 8,
					"HoleId": 2574925,
					"Length": 119,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 2716355,
					"Length": 370,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 2716346,
					"Length": 356,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 11,
					"HoleId": 2716356,
					"Length": 363,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 12,
					"HoleId": 2716357,
					"Length": 337,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 13,
					"HoleId": 2574929,
					"Length": 502,
					"Par": 5,
					"Allocation": 12
				},
				{
					"Number": 14,
					"HoleId": 2574930,
					"Length": 140,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 2574931,
					"Length": 277,
					"Par": 4,
					"Allocation": 18
				},
				{
					"Number": 16,
					"HoleId": 2574932,
					"Length": 366,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 17,
					"HoleId": 2716362,
					"Length": 153,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 2574934,
					"Length": 467,
					"Par": 5,
					"Allocation": 14
				}
			],
			"TeeSetRatingId": 622921,
			"TeeSetRatingName": "White/Tan",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 5877,
			"TotalMeters": 5374,
			"LegacyCRPTeeId": None,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 74.1,
					"SlopeRating": 136,
					"BogeyRating": 106.2
				},
				{
					"RatingType": "Back",
					"CourseRating": 37.1,
					"SlopeRating": 134,
					"BogeyRating": 52.9
				},
				{
					"RatingType": "Front",
					"CourseRating": 37,
					"SlopeRating": 138,
					"BogeyRating": 53.3
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 1924040,
					"Length": 486,
					"Par": 5,
					"Allocation": 3
				},
				{
					"Number": 2,
					"HoleId": 866370,
					"Length": 339,
					"Par": 4,
					"Allocation": 11
				},
				{
					"Number": 3,
					"HoleId": 1924042,
					"Length": 137,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 866372,
					"Length": 354,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 5,
					"HoleId": 866373,
					"Length": 337,
					"Par": 4,
					"Allocation": 7
				},
				{
					"Number": 6,
					"HoleId": 1924045,
					"Length": 281,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 866375,
					"Length": 493,
					"Par": 5,
					"Allocation": 1
				},
				{
					"Number": 8,
					"HoleId": 1924047,
					"Length": 119,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 866377,
					"Length": 370,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 10,
					"HoleId": 866378,
					"Length": 356,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 11,
					"HoleId": 866379,
					"Length": 363,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 12,
					"HoleId": 866380,
					"Length": 337,
					"Par": 4,
					"Allocation": 12
				},
				{
					"Number": 13,
					"HoleId": 1924052,
					"Length": 502,
					"Par": 5,
					"Allocation": 2
				},
				{
					"Number": 14,
					"HoleId": 1924053,
					"Length": 140,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 1924054,
					"Length": 277,
					"Par": 4,
					"Allocation": 14
				},
				{
					"Number": 16,
					"HoleId": 1924055,
					"Length": 366,
					"Par": 4,
					"Allocation": 4
				},
				{
					"Number": 17,
					"HoleId": 866385,
					"Length": 153,
					"Par": 3,
					"Allocation": 18
				},
				{
					"Number": 18,
					"HoleId": 1924057,
					"Length": 467,
					"Par": 5,
					"Allocation": 6
				}
			],
			"TeeSetRatingId": 622940,
			"TeeSetRatingName": "White/Tan",
			"Gender": "Female",
			"HolesNumber": 18,
			"TotalYardage": 5877,
			"TotalMeters": 5374,
			"LegacyCRPTeeId": None,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		},
		{
			"Ratings": [
				{
					"RatingType": "Total",
					"CourseRating": 66.1,
					"SlopeRating": 116,
					"BogeyRating": 87.7
				},
				{
					"RatingType": "Back",
					"CourseRating": 33.1,
					"SlopeRating": 115,
					"BogeyRating": 43.8
				},
				{
					"RatingType": "Front",
					"CourseRating": 33,
					"SlopeRating": 117,
					"BogeyRating": 43.9
				}
			],
			"Holes": [
				{
					"Number": 1,
					"HoleId": 2716383,
					"Length": 416,
					"Par": 5,
					"Allocation": 11
				},
				{
					"Number": 2,
					"HoleId": 2716348,
					"Length": 339,
					"Par": 4,
					"Allocation": 9
				},
				{
					"Number": 3,
					"HoleId": 2716349,
					"Length": 126,
					"Par": 3,
					"Allocation": 15
				},
				{
					"Number": 4,
					"HoleId": 2716386,
					"Length": 315,
					"Par": 4,
					"Allocation": 1
				},
				{
					"Number": 5,
					"HoleId": 2716387,
					"Length": 302,
					"Par": 4,
					"Allocation": 5
				},
				{
					"Number": 6,
					"HoleId": 2716352,
					"Length": 265,
					"Par": 4,
					"Allocation": 13
				},
				{
					"Number": 7,
					"HoleId": 2716389,
					"Length": 465,
					"Par": 5,
					"Allocation": 7
				},
				{
					"Number": 8,
					"HoleId": 2716354,
					"Length": 105,
					"Par": 3,
					"Allocation": 17
				},
				{
					"Number": 9,
					"HoleId": 2716391,
					"Length": 321,
					"Par": 4,
					"Allocation": 3
				},
				{
					"Number": 10,
					"HoleId": 2716346,
					"Length": 356,
					"Par": 4,
					"Allocation": 2
				},
				{
					"Number": 11,
					"HoleId": 2716392,
					"Length": 331,
					"Par": 4,
					"Allocation": 6
				},
				{
					"Number": 12,
					"HoleId": 2716357,
					"Length": 337,
					"Par": 4,
					"Allocation": 8
				},
				{
					"Number": 13,
					"HoleId": 2716394,
					"Length": 425,
					"Par": 5,
					"Allocation": 12
				},
				{
					"Number": 14,
					"HoleId": 2716359,
					"Length": 120,
					"Par": 3,
					"Allocation": 16
				},
				{
					"Number": 15,
					"HoleId": 2716360,
					"Length": 255,
					"Par": 4,
					"Allocation": 18
				},
				{
					"Number": 16,
					"HoleId": 2716397,
					"Length": 298,
					"Par": 4,
					"Allocation": 10
				},
				{
					"Number": 17,
					"HoleId": 2716362,
					"Length": 153,
					"Par": 3,
					"Allocation": 4
				},
				{
					"Number": 18,
					"HoleId": 2716399,
					"Length": 386,
					"Par": 5,
					"Allocation": 14
				}
			],
			"TeeSetRatingId": 729778,
			"TeeSetRatingName": "Tan/Green",
			"Gender": "Male",
			"HolesNumber": 18,
			"TotalYardage": 5315,
			"TotalMeters": 4860,
			"LegacyCRPTeeId": None,
			"StrokeAllocation": True,
			"TotalPar": 72,
			"IsShorter": None,
			"EligibleSides": None
		}
	],
	"CourseId": 2367,
	"CourseName": "FIRECLIFF",
	"CourseStatus": "Active",
	"CourseNumber": None,
	"CourseCity": "Palm Desert",
	"CourseState": "US-CA"
}]}