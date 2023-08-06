{
  allAvailableDates: [
    {
      epochSeconds: int,
      isoYearMonthDay: str,
      loaded: bool,
      localeMonthDay: str
    }
  ],
  attendanceData: {
    attendees: [
      {
        cmisId: int,
        displayName: str,
        entries: [
          {
            date: {
              epochSeconds: int,
              isoYearMonthDay: str,
              loaded: bool,
              localeMonthDay: str
            },
            isMarkedAttended: bool,
            markedAttended: bool
          }
        ],
        gender: str,
        sortName: str,
        unitOrgsCombined: [
          str
        ],
        uuid: str
      }
    ],
    visitorCategories: [
      {
        countsByDate: {
          2023-04-09: int,
          2023-04-16: int,
          2023-04-23: int,
          2023-04-30: int,
          2023-05-07: int
        },
        displayName: str,
        name: str
      }
    ]
  },
  dates: [
    {
      epochSeconds: int,
      isoYearMonthDay: str,
      loaded: bool,
      localeMonthDay: str
    }
  ]
}