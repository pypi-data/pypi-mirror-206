from concurrent import futures

from ..log import liblogger


def download_sequences(sequences, max_workers=10):
    from propy.GetProteinFromUniprot import GetProteinSequence

    with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futured = {}
        for uniprot_id in sequences:
            futured[executor.submit(GetProteinSequence, uniprot_id)] = uniprot_id
        for future in futures.as_completed(futured):
            uniprot_id = futured[future]
            try:
                sequence = future.result()
                assert sequence, "fetched sequence is empty"
            except Exception as exc:
                liblogger.warning(f"Failed to fetch sequence for {uniprot_id}, skipping.")
                liblogger.debug(f"Detailed error: {exc}")
                yield None
            else:
                yield uniprot_id, sequence
