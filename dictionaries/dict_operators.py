# List of operators defined using lambda functions (i.e. a lambda function is a small anonymous function
# that can take any number of arguments, but can only have one expression).


# t = mandelstam_t
# s= mandelstam_s

operators = {"O_F1": lambda t, m_t, m_dm, s: 4 * (4 * m_dm ** 2 - t) * (4 * m_t ** 2 - t),
             "O_F2": lambda t, m_t, m_dm, s: 4 * t * (t - 4 * m_t ** 2),
             "O_F3": lambda t, m_t, m_dm, s: 4 * t * (t - 4 * m_dm ** 2),
             "O_F4": lambda t, m_t, m_dm, s: 4 * t ** 2,
             "O_F5": lambda t, m_t, m_dm, s: 4 * (m_t ** 2 + m_dm ** 2) ** 2 - 8 * s * (
                     m_t ** 2 + m_dm ** 2) + 4 * s ** 2 + 4 * s * t + 2 * t ** 2,
             "O_F6": lambda t, m_t, m_dm, s: 4 * (m_t ** 2 - m_dm ** 2) ** 2 - 8 * s * (
                     m_t ** 2 + m_dm ** 2) - 8 * t * (m_dm ** 2) + 4 * (s ** 2) + 4 * s * t + 2 * t ** 2,
             "O_F7": lambda t, m_t, m_dm, s: 4 * (m_t ** 2 - m_dm ** 2) ** 2 - 8 * s * (
                     m_t ** 2 + m_dm ** 2) - 8 * t * m_t ** 2 + 4 * s ** 2 + 4 * s * t + 2 * t ** 2,
             "O_F8": lambda t, m_t, m_dm, s: 4 * (m_t ** 4 + 10 * m_t ** 2 * m_dm ** 2 + m_dm ** 4) - 8 * (
                     s + t) * (m_t ** 2 + m_dm ** 2) + 4 * s ** 2 + 4 * s * t + 2 * t ** 2,
             "O_F9": lambda t, m_t, m_dm, s: 8 * (4 * (m_t ** 4 + 4 * m_t ** 2 * m_dm ** 2 + m_dm ** 4) - 2 *
                                                  (4 * s + t) * (m_t ** 2 + m_dm ** 2) + (2 * s + t) ** 2),
             "O_F10": lambda t, m_t, m_dm, s: 8 * (
                     4 * (m_t ** 2 + m_dm ** 2) ** 2 - 2 * (4 * s + t) * (m_t ** 2 + m_dm ** 2) + (
                     2 * s + t) ** 2),
             "O_S1": lambda t, m_t, m_dm, s: (4 * m_t ** 2 - t),
             "O_S2": lambda t, m_t, m_dm, s: (-t),
             "O_S3": lambda t, m_t, m_dm, s: 4 * (
                     (m_t ** 2 + m_dm ** 2) ** 2 - 2 * s * (m_t ** 2 + m_dm ** 2) + s ** 2 + s * t - m_t ** 2 * t),
             "O_S4": lambda t, m_t, m_dm, s: 4 * (
                     (m_t ** 2 - m_dm ** 2) ** 2 - 2 * s * (m_t ** 2 + m_dm ** 2) + s ** 2 + s * t)}
