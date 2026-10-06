from pathlib import Path


def add_document_metadata(
    documents,
    document_id=None,
    document_title=None,
    authority=None,
    version=None,
    status=None,
):
    """
    Add document-specific metadata based on the PDF source path or explicit parameters.
    """

    for document in documents:

        source = document.metadata.get("source", "")

        source_path = Path(source)

        filename = source_path.stem
        folder = source_path.parent.name

        # Default values
        auto_doc_id = filename.lower() if filename else "unknown"
        auto_doc_title = filename.replace("_", " ") if filename else "Unknown Document"
        auto_status = "historical" if folder.lower() == "historical" else "current"
        auto_version = "unknown"
        auto_authority = "Government of Maharashtra"

        # Specific document metadata
        if filename == "DCPR_2018_PMRDA":

            auto_doc_id = "dcpr_2018_pmrda"
            auto_doc_title = "Development Control and Promotion Regulations 2018 - PMRDA"
            auto_version = "DCPR 2018"

        elif filename == "PMC_UDCPR":

            auto_doc_id = "pmc_udcpr"
            auto_doc_title = "PMC UDCPR"
            auto_version = "PMC UDCPR"

        elif filename == "PMRDA_Development_Permission_Checklist":

            auto_doc_id = "pmrda_development_permission_checklist"
            auto_doc_title = "PMRDA Development Permission Checklist"
            auto_version = "Development Permission Checklist"

        elif filename == "UDCPR_2020_updated_2025":

            auto_doc_id = "udcpr_2020"
            auto_doc_title = "Unified Development Control and Promotion Regulations"
            auto_version = "UDCPR 2020 Updated 2025"

        elif filename == "Pune_DCPR_2015_Vol1":

            auto_doc_id = "pune_dcpr_2015"
            auto_doc_title = "Pune DCPR 2015 Volume 1"
            auto_version = "DCPR 2015"

        # Use explicitly passed arguments if provided; otherwise fall back to auto-detected values
        document.metadata["document_id"] = document_id if document_id is not None else auto_doc_id
        document.metadata["document_title"] = document_title if document_title is not None else auto_doc_title
        document.metadata["authority"] = authority if authority is not None else auto_authority
        document.metadata["version"] = version if version is not None else auto_version
        document.metadata["status"] = status if status is not None else auto_status

    return documents