from __future__ import annotations
import faiss
import numpy
import torch
import transformers as transformers


def search_database(search_vectors: numpy.array,
                    encoder: transformers.PreTrainedModel,
                    tokenizer: transformers.PreTrainedTokenizer,
                    text: str,
                    index_of_summarised_vector: int,
                    num_samples: int = 2,
                    index: faiss.Index = None):
    """

    :param search_vectors: The vectors you wish to search over
    :param encoder: The encoder you are using
    :param tokenizer: The tokenizer for your encoder
    :param text: String that you wish to find the context for
    :param num_samples: number of things you wish to return
    :param index: optional index you have saved off otherwise created from your searched vectors
    :return: positions:positions from you document that match the query most closely
    """
    if index is None:
        d = encoder.config.hidden_size
        index = faiss.IndexFlatIP(d)
        index.add(search_vectors)
    encoder.eval()
    data = tokenizer.encode_plus(
        text,
        max_length=512,
        return_tensors='pt')
    ids = data['input_ids'].to(encoder.device)
    mask = data['attention_mask'].to(encoder.device)
    with torch.no_grad():
        vector = encoder(ids, mask)
    _, indices = index.search(vector[index_of_summarised_vector].numpy(), num_samples)
    return indices[0][:num_samples]


def vectorise_to_numpy(
        encoder: transformers.PreTrainedModel,
        tokenizer: transformers.PreTrainedTokenizer,
        input_strings: list,
        batch_size: int,
        index_of_summarised_vector: int):
    """

    :param encoder: The encoder you are using
    :param tokenizer: The tokenizer for your encoder
    :param input_strings: List of string that you wish to find the context for
    :param batch_size:
    :return:
    """
    # Vectorize the input strings in batches
    all_embeddings = []
    for i in range(0, len(input_strings), batch_size):
        text = input_strings[i:i + batch_size]
        data = tokenizer.batch_encode_plus(
            text,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors='pt')
        ids = data['input_ids'].to(encoder.device)
        mask = data['attention_mask'].to(encoder.device)
        with torch.no_grad():
            vectors = encoder(ids, mask)
        all_embeddings.append(vectors[index_of_summarised_vector])

    # Concatenate the embeddings for all batches
    if batch_size < len(input_strings):
        all_embeddings = all_embeddings[0].numpy()
    else:
        all_embeddings = torch.cat(all_embeddings, dim=0).numpy()
    return all_embeddings
