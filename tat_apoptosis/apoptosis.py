def apoptosis(chunks, coherence_threshold=0.3):
    return [c for c in chunks if c.get('coherence', 1.0) >= coherence_threshold]
