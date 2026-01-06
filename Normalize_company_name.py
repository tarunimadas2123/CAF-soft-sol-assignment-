def normalize_company_name(company_name):
    if not company_name:
        return ""

    cleaned_name = " ".join(company_name.split()).lower()

    if "caf" in cleaned_name:
        return "CAF SoftSol India Pvt Ltd."

    return cleaned_name


print(normalize_company_name("CAF softsol"))
print(normalize_company_name("CAF solution"))
print(normalize_company_name("CAF           softSolution  India Pvt Limited"))
print(normalize_company_name(""))
print(normalize_company_name(None))
print(normal)
